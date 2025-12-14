"""History source extractor."""

from datetime import datetime
from typing import Any, Dict, List, Optional

from database import MetricsDatabase
from utils import (
    get_claude_dir,
    read_jsonl_file,
    count_jsonl_lines,
    unix_ms_to_datetime,
)
from .base import BaseSource


class HistorySource(BaseSource):
    """Extractor for ~/.claude/history.jsonl.

    Contains user input history with timestamps and project context.
    This is a readline-style history of all user inputs.
    """

    name = "history"
    description = "User input history"
    source_paths = ["~/.claude/history.jsonl"]

    def __init__(self, include_sensitive: bool = False, limit: Optional[int] = None):
        """Initialize the history extractor.

        Args:
            include_sensitive: If True, include full input text
            limit: Maximum number of entries to extract (None = all)
        """
        super().__init__(include_sensitive)
        self.limit = limit

    def extract(self) -> Dict[str, Any]:
        """Extract history data.

        Returns:
            Dictionary containing:
            - total_entries: Total number of history entries
            - entries: List of history records
            - projects: Unique projects referenced
            - date_range: First and last entry dates
        """
        path = get_claude_dir() / "history.jsonl"

        if not path.exists():
            return {"error": "History file not found", "path": str(path)}

        total_count = count_jsonl_lines(path)

        entries = []
        projects = set()
        min_ts = None
        max_ts = None

        for i, record in enumerate(read_jsonl_file(path)):
            if self.limit and i >= self.limit:
                break

            # Extract fields
            timestamp = record.get("timestamp")
            project = record.get("project", "")
            display = record.get("display", "")
            pasted = record.get("pastedContents")

            if project:
                projects.add(project)

            if timestamp:
                if min_ts is None or timestamp < min_ts:
                    min_ts = timestamp
                if max_ts is None or timestamp > max_ts:
                    max_ts = timestamp

            entry = {
                "timestamp": timestamp,
                "timestamp_iso": unix_ms_to_datetime(timestamp).isoformat() if timestamp else None,
                "project": project,
                "display_length": len(display),
                "has_pasted_contents": pasted is not None,
            }

            # Include full display text if requested or short
            if self.include_sensitive or len(display) <= 200:
                entry["display"] = display
            else:
                entry["display"] = display[:200] + "...[truncated]"

            entries.append(entry)

        return {
            "path": str(path),
            "total_entries": total_count,
            "extracted_entries": len(entries),
            "entries": entries,
            "unique_projects": sorted(projects),
            "project_count": len(projects),
            "date_range": {
                "first": unix_ms_to_datetime(min_ts).isoformat() if min_ts else None,
                "last": unix_ms_to_datetime(max_ts).isoformat() if max_ts else None,
            },
        }

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write history to SQLite."""
        data = self.get_data()

        if "error" in data:
            return

        entries = data.get("entries", [])

        # Convert to format expected by database
        db_records = []
        for entry in entries:
            db_records.append({
                "display": entry.get("display", ""),
                "timestamp": entry.get("timestamp"),
                "timestamp_iso": entry.get("timestamp_iso"),
                "project": entry.get("project"),
                "pastedContents": entry.get("has_pasted_contents"),
            })

        db.insert_history(db_records)

    def get_summary(self) -> Dict[str, Any]:
        """Get history summary."""
        data = self.get_data()

        if "error" in data:
            return {"source": self.name, "error": data["error"]}

        entries = data.get("entries", [])

        # Calculate average display length
        total_length = sum(e.get("display_length", 0) for e in entries)
        avg_length = total_length / len(entries) if entries else 0

        # Count entries with pasted content
        pasted_count = sum(1 for e in entries if e.get("has_pasted_contents"))

        return {
            "source": self.name,
            "total_entries": data.get("total_entries", 0),
            "extracted_entries": len(entries),
            "unique_projects": data.get("project_count", 0),
            "avg_display_length": round(avg_length, 1),
            "pasted_content_entries": pasted_count,
            "date_range": data.get("date_range", {}),
        }

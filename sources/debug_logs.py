"""Debug logs extractor."""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_claude_dir, format_bytes, get_file_stats


class DebugLogsSource(BaseSource):
    """Extract debug log file information and statistics."""

    name = "debug_logs"
    description = "Session diagnostic logs"
    source_paths = ["~/.claude/debug/"]

    # Log level patterns
    ERROR_PATTERN = re.compile(r"\[ERROR\]|\bERROR\b|Error:|error:", re.IGNORECASE)
    WARNING_PATTERN = re.compile(r"\[WARN\]|\[WARNING\]|\bWARN\b|\bWARNING\b|Warning:", re.IGNORECASE)
    DEBUG_PATTERN = re.compile(r"\[DEBUG\]|\bDEBUG\b", re.IGNORECASE)

    def _get_debug_dir(self) -> Path:
        """Get the debug logs directory."""
        return get_claude_dir() / "debug"

    def _analyze_log_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a single log file for statistics."""
        stats = get_file_stats(file_path)

        line_count = 0
        error_count = 0
        warning_count = 0
        debug_count = 0
        first_timestamp = None
        last_timestamp = None

        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    line_count += 1

                    # Count log levels
                    if self.ERROR_PATTERN.search(line):
                        error_count += 1
                    if self.WARNING_PATTERN.search(line):
                        warning_count += 1
                    if self.DEBUG_PATTERN.search(line):
                        debug_count += 1

                    # Try to extract timestamp from line start
                    # Format: YYYY-MM-DDTHH:MM:SS.mmmZ
                    if line and len(line) > 24 and line[0].isdigit():
                        ts = line[:24]
                        if first_timestamp is None:
                            first_timestamp = ts
                        last_timestamp = ts
        except (OSError, PermissionError, UnicodeDecodeError):
            pass

        return {
            "size_bytes": stats.get("size_bytes", 0),
            "size_human": format_bytes(stats.get("size_bytes", 0)),
            "line_count": line_count,
            "error_count": error_count,
            "warning_count": warning_count,
            "debug_count": debug_count,
            "first_timestamp": first_timestamp,
            "last_timestamp": last_timestamp,
            "modified_at": stats.get("modified_at"),
        }

    def extract(self) -> Dict[str, Any]:
        """Extract debug log information."""
        debug_dir = self._get_debug_dir()

        if not debug_dir.exists():
            return {
                "directory_exists": False,
                "path": str(debug_dir),
                "total_files": 0,
                "total_size_bytes": 0,
                "total_errors": 0,
                "total_warnings": 0,
                "logs": [],
            }

        logs = []
        total_size = 0
        total_errors = 0
        total_warnings = 0
        total_lines = 0

        try:
            for file_path in debug_dir.glob("*.txt"):
                if not file_path.is_file():
                    continue

                analysis = self._analyze_log_file(file_path)

                # Session ID is the filename without extension
                session_id = file_path.stem

                log_info = {
                    "session_id": session_id,
                    "filename": file_path.name,
                    **analysis,
                }

                logs.append(log_info)
                total_size += analysis.get("size_bytes", 0)
                total_errors += analysis.get("error_count", 0)
                total_warnings += analysis.get("warning_count", 0)
                total_lines += analysis.get("line_count", 0)
        except (OSError, PermissionError):
            pass

        # Sort by modified time (newest first)
        logs.sort(key=lambda x: x.get("modified_at", ""), reverse=True)

        return {
            "directory_exists": True,
            "path": str(debug_dir),
            "total_files": len(logs),
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "total_lines": total_lines,
            "total_errors": total_errors,
            "total_warnings": total_warnings,
            "logs": logs,
        }

    def to_sqlite(self, db) -> None:
        """Write debug logs to SQLite."""
        data = self.get_data()
        logs = data.get("logs", [])
        if logs:
            db.insert_debug_logs(logs)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of debug logs."""
        data = self.get_data()
        return {
            "source": self.name,
            "total_files": data.get("total_files", 0),
            "total_size_bytes": data.get("total_size_bytes", 0),
            "total_errors": data.get("total_errors", 0),
            "total_warnings": data.get("total_warnings", 0),
        }

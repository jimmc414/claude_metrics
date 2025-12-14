"""Stats cache source extractor."""

from typing import Any, Dict

from database import MetricsDatabase
from utils import get_claude_dir, read_json_file
from .base import BaseSource


class StatsCacheSource(BaseSource):
    """Extractor for ~/.claude/stats-cache.json.

    Contains pre-aggregated statistics including:
    - Daily activity (messages, sessions, tool calls)
    - Model usage and token counts
    - Hourly activity distribution
    - Longest session records
    """

    name = "stats_cache"
    description = "Pre-aggregated statistics cache"
    source_paths = ["~/.claude/stats-cache.json"]

    def extract(self) -> Dict[str, Any]:
        """Extract stats cache data.

        Returns:
            Dictionary containing:
            - version: Cache format version
            - lastComputedDate: When stats were last computed
            - dailyActivity: List of daily activity records
            - dailyModelTokens: List of daily token usage by model
            - modelUsage: Cumulative model statistics
            - hourCounts: Activity by hour (0-23)
            - totalSessions: All-time session count
            - totalMessages: All-time message count
            - firstSessionDate: First session timestamp
            - longestSession: Longest session record
        """
        path = get_claude_dir() / "stats-cache.json"
        data = read_json_file(path)

        if data is None:
            return {"error": "Stats cache not found", "path": str(path)}

        return data

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write stats cache data to SQLite."""
        data = self.get_data()

        if "error" in data:
            return

        # Insert main stats cache record
        db.insert_stats_cache(data)

        # Insert daily activity
        if "dailyActivity" in data:
            db.insert_daily_activity(data["dailyActivity"])

        # Insert hourly activity
        if "hourCounts" in data:
            db.insert_hourly_activity(data["hourCounts"])

        # Insert model usage
        if "modelUsage" in data:
            db.insert_model_usage(data["modelUsage"])

    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics."""
        data = self.get_data()

        if "error" in data:
            return {"source": self.name, "error": data["error"]}

        return {
            "source": self.name,
            "total_sessions": data.get("totalSessions", 0),
            "total_messages": data.get("totalMessages", 0),
            "first_session_date": data.get("firstSessionDate"),
            "last_computed_date": data.get("lastComputedDate"),
            "daily_activity_days": len(data.get("dailyActivity", [])),
            "models_used": list(data.get("modelUsage", {}).keys()),
            "longest_session_duration_ms": (
                data.get("longestSession", {}).get("duration")
            ),
        }

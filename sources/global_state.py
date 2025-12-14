"""Global state source extractor."""

from typing import Any, Dict, List

from database import MetricsDatabase
from utils import get_claude_json_path, read_json_file
from .base import BaseSource


class GlobalStateSource(BaseSource):
    """Extractor for ~/.claude.json.

    Contains global Claude Code state including:
    - Startup count and usage metrics
    - Tips history (feature discovery tracking)
    - Feature flags (cached Statsig gates)
    - Per-project statistics and configuration
    """

    name = "global_state"
    description = "Global Claude Code state and per-project statistics"
    source_paths = ["~/.claude.json"]

    def extract(self) -> Dict[str, Any]:
        """Extract global state data.

        Returns:
            Dictionary containing:
            - numStartups: Total startup count
            - tipsHistory: Feature discovery tracking
            - cachedStatsigGates: Feature flags
            - projects: Per-project statistics and config
            - Plus other global settings
        """
        path = get_claude_json_path()
        data = read_json_file(path)

        if data is None:
            return {"error": "Global state file not found", "path": str(path)}

        # Organize the data
        result = {
            "path": str(path),
            "raw": data,
        }

        # Extract key sections
        result["usage"] = {
            "numStartups": data.get("numStartups", 0),
            "promptQueueUseCount": data.get("promptQueueUseCount", 0),
            "memoryUsageCount": data.get("memoryUsageCount", 0),
        }

        result["onboarding"] = {
            "hasCompletedOnboarding": data.get("hasCompletedOnboarding", False),
            "lastOnboardingVersion": data.get("lastOnboardingVersion"),
            "hasSeenTasksHint": data.get("hasSeenTasksHint", False),
            "hasSeenStashHint": data.get("hasSeenStashHint", False),
        }

        result["tips_history"] = data.get("tipsHistory", {})
        result["feature_flags"] = data.get("cachedStatsigGates", {})
        result["dynamic_configs"] = data.get("cachedDynamicConfigs", {})

        # Extract project data
        projects = data.get("projects", {})
        result["projects"] = {}
        for path_key, project_data in projects.items():
            result["projects"][path_key] = self._extract_project_data(project_data)

        result["project_count"] = len(projects)

        return result

    def _extract_project_data(self, project: Dict[str, Any]) -> Dict[str, Any]:
        """Extract relevant fields from a project entry."""
        return {
            # Trust & permissions
            "allowedTools": project.get("allowedTools", []),
            "hasTrustDialogAccepted": project.get("hasTrustDialogAccepted", False),
            "dontCrawlDirectory": project.get("dontCrawlDirectory", False),

            # MCP configuration
            "mcpServers": project.get("mcpServers", {}),
            "enabledMcpjsonServers": project.get("enabledMcpjsonServers", []),
            "disabledMcpjsonServers": project.get("disabledMcpjsonServers", []),

            # Onboarding
            "projectOnboardingSeenCount": project.get("projectOnboardingSeenCount", 0),
            "hasCompletedProjectOnboarding": project.get("hasCompletedProjectOnboarding", False),

            # Vulnerability cache
            "reactVulnerabilityCache": project.get("reactVulnerabilityCache", {}),

            # Last session stats
            "lastSessionId": project.get("lastSessionId"),
            "lastCost": project.get("lastCost", 0),
            "lastAPIDuration": project.get("lastAPIDuration", 0),
            "lastToolDuration": project.get("lastToolDuration", 0),
            "lastDuration": project.get("lastDuration", 0),
            "lastLinesAdded": project.get("lastLinesAdded", 0),
            "lastLinesRemoved": project.get("lastLinesRemoved", 0),
            "lastTotalInputTokens": project.get("lastTotalInputTokens", 0),
            "lastTotalOutputTokens": project.get("lastTotalOutputTokens", 0),
            "lastTotalCacheCreationInputTokens": project.get("lastTotalCacheCreationInputTokens", 0),
            "lastTotalCacheReadInputTokens": project.get("lastTotalCacheReadInputTokens", 0),
            "lastModelUsage": project.get("lastModelUsage", {}),
        }

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write global state to SQLite."""
        data = self.get_data()

        if "error" in data or db.conn is None:
            return

        # Insert tips history
        tips = data.get("tips_history", {})
        for tip_name, count in tips.items():
            db.conn.execute(
                """
                INSERT OR REPLACE INTO tips_history (tip_name, show_count)
                VALUES (?, ?)
                """,
                (tip_name, count),
            )

        # Insert feature flags
        flags = data.get("feature_flags", {})
        for flag_name, enabled in flags.items():
            db.conn.execute(
                """
                INSERT OR REPLACE INTO feature_flags (flag_name, enabled)
                VALUES (?, ?)
                """,
                (flag_name, 1 if enabled else 0),
            )

        # Insert projects
        projects = data.get("projects", {})
        for path, project_data in projects.items():
            db.insert_project(path, project_data)

        db.commit()

    def get_summary(self) -> Dict[str, Any]:
        """Get global state summary."""
        data = self.get_data()

        if "error" in data:
            return {"source": self.name, "error": data["error"]}

        usage = data.get("usage", {})
        tips = data.get("tips_history", {})
        flags = data.get("feature_flags", {})
        projects = data.get("projects", {})

        # Calculate total cost across projects
        total_cost = sum(
            p.get("lastCost", 0) or 0
            for p in projects.values()
        )

        # Calculate total lines changed
        total_lines_added = sum(
            p.get("lastLinesAdded", 0) or 0
            for p in projects.values()
        )
        total_lines_removed = sum(
            p.get("lastLinesRemoved", 0) or 0
            for p in projects.values()
        )

        return {
            "source": self.name,
            "num_startups": usage.get("numStartups", 0),
            "prompt_queue_uses": usage.get("promptQueueUseCount", 0),
            "tips_seen": len(tips),
            "total_tip_shows": sum(tips.values()),
            "feature_flags_count": len(flags),
            "enabled_flags_count": sum(1 for v in flags.values() if v),
            "project_count": len(projects),
            "total_last_session_cost": round(total_cost, 4),
            "total_lines_added": total_lines_added,
            "total_lines_removed": total_lines_removed,
        }

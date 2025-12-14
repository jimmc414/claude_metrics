"""Settings source extractor."""

import json
from typing import Any, Dict, List

from database import MetricsDatabase
from utils import get_claude_dir, get_config_dir, read_json_file
from .base import BaseSource


class SettingsSource(BaseSource):
    """Extractor for Claude Code settings files.

    Extracts from:
    - ~/.claude/settings.json (global settings)
    - ~/.claude/settings.local.json (local overrides)
    - ~/.config/claude/claude_code_config.json (system config)
    """

    name = "settings"
    description = "Claude Code settings and configuration"
    source_paths = [
        "~/.claude/settings.json",
        "~/.claude/settings.local.json",
        "~/.config/claude/claude_code_config.json",
    ]

    def extract(self) -> Dict[str, Any]:
        """Extract settings from all config files.

        Returns:
            Dictionary containing:
            - global_settings: Main settings.json content
            - local_settings: Local overrides from settings.local.json
            - system_config: System-level config from ~/.config/claude/
        """
        result = {}

        # Global settings
        global_path = get_claude_dir() / "settings.json"
        global_settings = read_json_file(global_path)
        result["global_settings"] = global_settings or {}
        result["global_settings_path"] = str(global_path)
        result["global_settings_exists"] = global_settings is not None

        # Local settings
        local_path = get_claude_dir() / "settings.local.json"
        local_settings = read_json_file(local_path)
        result["local_settings"] = local_settings or {}
        result["local_settings_path"] = str(local_path)
        result["local_settings_exists"] = local_settings is not None

        # System config
        system_path = get_config_dir() / "claude_code_config.json"
        system_config = read_json_file(system_path)
        result["system_config"] = system_config or {}
        result["system_config_path"] = str(system_path)
        result["system_config_exists"] = system_config is not None

        return result

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write settings to SQLite."""
        data = self.get_data()

        if db.conn is None:
            return

        # Insert global settings
        global_settings = data.get("global_settings", {})
        if global_settings:
            permissions = global_settings.get("permissions", {})
            db.conn.execute(
                """
                INSERT OR REPLACE INTO settings
                (scope, model, thinking_enabled, git_attribution,
                 permissions_mode, allowed_tools, denied_tools)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "global",
                    global_settings.get("model"),
                    1 if global_settings.get("alwaysThinkingEnabled") else 0,
                    1 if global_settings.get("gitAttribution") else 0,
                    permissions.get("defaultMode"),
                    json.dumps(permissions.get("allow", [])),
                    json.dumps(permissions.get("deny", [])),
                ),
            )

        # Insert local settings
        local_settings = data.get("local_settings", {})
        if local_settings:
            db.conn.execute(
                """
                INSERT OR REPLACE INTO settings
                (scope, model, thinking_enabled, git_attribution,
                 permissions_mode, allowed_tools, denied_tools)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "local",
                    local_settings.get("model"),
                    1 if local_settings.get("alwaysThinkingEnabled") else 0,
                    1 if local_settings.get("gitAttribution") else 0,
                    local_settings.get("permissions", {}).get("defaultMode"),
                    json.dumps(local_settings.get("permissions", {}).get("allow", [])),
                    json.dumps(local_settings.get("permissions", {}).get("deny", [])),
                ),
            )

        db.commit()

    def get_summary(self) -> Dict[str, Any]:
        """Get settings summary."""
        data = self.get_data()
        global_settings = data.get("global_settings", {})
        permissions = global_settings.get("permissions", {})

        return {
            "source": self.name,
            "global_settings_exists": data.get("global_settings_exists", False),
            "local_settings_exists": data.get("local_settings_exists", False),
            "system_config_exists": data.get("system_config_exists", False),
            "default_model": global_settings.get("model"),
            "thinking_enabled": global_settings.get("alwaysThinkingEnabled"),
            "permissions_mode": permissions.get("defaultMode"),
            "allowed_tools_count": len(permissions.get("allow", [])),
            "denied_tools_count": len(permissions.get("deny", [])),
        }

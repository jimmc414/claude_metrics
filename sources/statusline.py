"""Statusline data extractor (schema-only)."""

from typing import Any, Dict

from .base import BaseSource


class StatuslineSource(BaseSource):
    """Extract statusline data schema (runtime-only source).

    The statusline data is only available during an active Claude Code session
    when using a custom statusline command. This extractor documents the
    expected schema for reference.
    """

    name = "statusline"
    description = "Real-time session data passed to statusline command"
    source_paths = ["Runtime stdin to statusline command"]

    # Define the expected schema for statusline JSON
    STATUSLINE_SCHEMA = {
        "model": {
            "type": "object",
            "properties": {
                "display_name": {"type": "string", "example": "claude-opus-4-5"},
                "id": {"type": "string", "example": "claude-opus-4-5-20250514"},
            },
        },
        "workspace": {
            "type": "object",
            "properties": {
                "current_dir": {"type": "string", "example": "/home/user/project"},
                "project_dir": {"type": "string", "example": "/home/user/project"},
            },
        },
        "version": {"type": "string", "example": "2.0.69"},
        "cost": {
            "type": "object",
            "properties": {
                "total_cost_usd": {"type": "float", "example": 0.15},
                "total_lines_added": {"type": "int", "example": 150},
                "total_lines_removed": {"type": "int", "example": 45},
            },
        },
        "exceeds_200k_tokens": {"type": "bool", "example": False},
    }

    def extract(self) -> Dict[str, Any]:
        """Return schema documentation for statusline data.

        This source cannot extract live data - it documents the expected
        schema for statusline JSON that is passed via stdin during active sessions.
        """
        return {
            "source_type": "runtime",
            "availability": "Only available during active Claude Code session",
            "capture_method": "Via custom statusline command configured in settings.json",
            "configuration": {
                "setting": "statusLine.command",
                "example": "~/.claude/statusline-command.sh",
            },
            "schema": self.STATUSLINE_SCHEMA,
            "sample_data": {
                "model": {"display_name": "claude-opus-4-5"},
                "workspace": {
                    "current_dir": "/home/user/project",
                    "project_dir": "/home/user/project",
                },
                "version": "2.0.69",
                "cost": {
                    "total_cost_usd": 0.15,
                    "total_lines_added": 150,
                    "total_lines_removed": 45,
                },
                "exceeds_200k_tokens": False,
            },
            "note": "This is a runtime-only data source. No historical data is stored.",
        }

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of statusline source."""
        return {
            "source": self.name,
            "source_type": "runtime",
            "schema_fields": list(self.STATUSLINE_SCHEMA.keys()),
            "note": "Schema documentation only - no live data extraction",
        }

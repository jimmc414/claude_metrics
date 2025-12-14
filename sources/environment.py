"""Environment variables extractor."""

import os
from typing import Any, Dict, List

from .base import BaseSource


class EnvironmentSource(BaseSource):
    """Extract Claude Code related environment variables."""

    name = "environment"
    description = "Claude Code environment variables"
    source_paths = ["Process environment"]

    # Environment variables to extract (with sensitivity flags)
    CLAUDE_VARS = {
        # Non-sensitive - include value
        "CLAUDECODE": False,
        "CLAUDE_CODE_ENTRYPOINT": False,
        "CLAUDE_PROJECT_DIR": False,
        "CLAUDE_CONFIG_DIR": False,
        "CLAUDE_CODE_ENABLE_TELEMETRY": False,
        "OTEL_METRICS_EXPORTER": False,
        "OTEL_LOGS_EXPORTER": False,
        "OTEL_LOG_USER_PROMPTS": False,
        "MAX_MCP_OUTPUT_TOKENS": False,
        # Sensitive - only indicate presence
        "ANTHROPIC_API_KEY": True,
        "CLAUDE_CODE_OAUTH_TOKEN": True,
    }

    def extract(self) -> Dict[str, Any]:
        """Extract Claude-related environment variables."""
        result = {}
        sensitive_present = {}

        for var_name, is_sensitive in self.CLAUDE_VARS.items():
            value = os.environ.get(var_name)

            if is_sensitive:
                # For sensitive vars, only indicate presence
                sensitive_present[f"has_{var_name}"] = value is not None
                if self.include_sensitive and value is not None:
                    result[var_name] = value
            else:
                # For non-sensitive vars, include the value
                result[var_name] = value

        # Add sensitive presence flags
        result.update(sensitive_present)

        # Count how many Claude vars are set
        result["_total_vars_set"] = sum(
            1 for var in self.CLAUDE_VARS if os.environ.get(var) is not None
        )

        return result

    def to_sqlite(self, db) -> None:
        """Write environment variables to SQLite."""
        data = self.get_data()
        db.insert_environment_vars(data)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of environment variables."""
        data = self.get_data()
        return {
            "source": self.name,
            "total_vars_set": data.get("_total_vars_set", 0),
            "is_claude_code": data.get("CLAUDECODE") == "1",
            "entrypoint": data.get("CLAUDE_CODE_ENTRYPOINT"),
        }

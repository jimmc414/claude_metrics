"""MCP configuration extractor."""

from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_claude_json_path, read_json_file


class McpConfigSource(BaseSource):
    """Extract MCP (Model Context Protocol) server configurations."""

    name = "mcp_config"
    description = "MCP server configurations"
    source_paths = ["<project>/.mcp.json", "<project>/mcp.json"]

    # Sensitive fields to redact in env vars
    SENSITIVE_ENV_KEYS = {"API_KEY", "TOKEN", "SECRET", "PASSWORD", "KEY", "CREDENTIAL"}

    def _get_known_projects(self) -> List[str]:
        """Get list of known project paths from ~/.claude.json."""
        claude_json = read_json_file(get_claude_json_path())
        if claude_json and "projects" in claude_json:
            return list(claude_json["projects"].keys())
        return []

    def _is_sensitive_env_key(self, key: str) -> bool:
        """Check if an environment variable key is sensitive."""
        key_upper = key.upper()
        return any(s in key_upper for s in self.SENSITIVE_ENV_KEYS)

    def _redact_env_vars(self, env: Dict[str, str]) -> Dict[str, str]:
        """Redact sensitive environment variable values."""
        if self.include_sensitive:
            return env

        redacted = {}
        for key, value in env.items():
            if self._is_sensitive_env_key(key):
                redacted[key] = "[REDACTED]"
            else:
                redacted[key] = value
        return redacted

    def _extract_server_info(self, name: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Extract information about a single MCP server."""
        server_type = config.get("type", "unknown")
        command = config.get("command")
        args = config.get("args", [])
        env = config.get("env", {})

        return {
            "name": name,
            "type": server_type,
            "command": command,
            "args": args,
            "env": self._redact_env_vars(env) if env else {},
            "has_env": bool(env),
        }

    def _extract_mcp_config(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Extract MCP configuration from a file."""
        config = read_json_file(file_path)
        if not config:
            return None

        servers = []
        mcp_servers = config.get("mcpServers", {})

        for name, server_config in mcp_servers.items():
            server_info = self._extract_server_info(name, server_config)
            servers.append(server_info)

        return {
            "servers": servers,
            "server_count": len(servers),
        }

    def extract(self) -> Dict[str, Any]:
        """Extract MCP configurations from all known projects."""
        projects = self._get_known_projects()

        configs = []
        projects_scanned = 0
        projects_with_mcp = 0
        total_servers = 0

        for project_path in projects:
            projects_scanned += 1
            project_dir = Path(project_path)

            # Check for .mcp.json or mcp.json
            mcp_file = None
            for filename in [".mcp.json", "mcp.json"]:
                candidate = project_dir / filename
                if candidate.exists() and candidate.is_file():
                    mcp_file = candidate
                    break

            if mcp_file:
                config_data = self._extract_mcp_config(mcp_file)
                if config_data:
                    projects_with_mcp += 1
                    total_servers += config_data["server_count"]

                    configs.append({
                        "project": project_path,
                        "config_file": mcp_file.name,
                        **config_data,
                    })

        # Sort by project path
        configs.sort(key=lambda x: x["project"])

        return {
            "projects_scanned": projects_scanned,
            "projects_with_mcp": projects_with_mcp,
            "total_servers": total_servers,
            "adoption_rate": (
                projects_with_mcp / projects_scanned
                if projects_scanned > 0 else 0
            ),
            "configs": configs,
        }

    def to_sqlite(self, db) -> None:
        """Write MCP configurations to SQLite."""
        data = self.get_data()
        configs = data.get("configs", [])
        if configs:
            db.insert_mcp_configs(configs)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of MCP configurations."""
        data = self.get_data()
        return {
            "source": self.name,
            "projects_scanned": data.get("projects_scanned", 0),
            "projects_with_mcp": data.get("projects_with_mcp", 0),
            "total_servers": data.get("total_servers", 0),
        }

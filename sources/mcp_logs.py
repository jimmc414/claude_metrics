"""MCP server logs extractor."""

import re
from pathlib import Path
from typing import Any, Dict, List

from .base import BaseSource
from utils import get_cache_dir, format_bytes


class McpLogsSource(BaseSource):
    """Extract MCP server log information."""

    name = "mcp_logs"
    description = "MCP server logs"
    source_paths = ["~/.cache/claude-cli-nodejs/"]

    # Pattern for MCP log directories
    MCP_LOGS_PATTERN = re.compile(r"^mcp-logs-(.+)$")

    # Error patterns in log files
    ERROR_PATTERN = re.compile(r"\bERROR\b|\bError\b|error:", re.IGNORECASE)

    def _analyze_log_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a single log file for statistics."""
        size = 0
        line_count = 0
        error_count = 0

        try:
            size = file_path.stat().st_size
        except (OSError, PermissionError):
            pass

        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                for line in f:
                    line_count += 1
                    if self.ERROR_PATTERN.search(line):
                        error_count += 1
        except (OSError, PermissionError):
            pass

        return {
            "size_bytes": size,
            "line_count": line_count,
            "error_count": error_count,
        }

    def _extract_server_logs(self, logs_dir: Path, server_name: str) -> Dict[str, Any]:
        """Extract log information for a single MCP server."""
        log_files = []
        total_size = 0
        total_lines = 0
        total_errors = 0

        try:
            for log_file in logs_dir.glob("*.txt"):
                if not log_file.is_file():
                    continue

                analysis = self._analyze_log_file(log_file)
                total_size += analysis["size_bytes"]
                total_lines += analysis["line_count"]
                total_errors += analysis["error_count"]

                log_files.append({
                    "filename": log_file.name,
                    **analysis,
                })
        except (OSError, PermissionError):
            pass

        # Sort log files by name (which are timestamps)
        log_files.sort(key=lambda x: x["filename"], reverse=True)

        return {
            "server": server_name,
            "log_count": len(log_files),
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "total_lines": total_lines,
            "error_count": total_errors,
            "log_files": log_files[:10],  # Limit to 10 most recent
        }

    def _extract_project_logs(self, project_dir: Path) -> Dict[str, Any]:
        """Extract MCP logs for a single project."""
        servers = []
        total_log_count = 0
        total_size = 0
        total_errors = 0

        try:
            for entry in project_dir.iterdir():
                if not entry.is_dir():
                    continue

                match = self.MCP_LOGS_PATTERN.match(entry.name)
                if not match:
                    continue

                server_name = match.group(1)
                server_data = self._extract_server_logs(entry, server_name)

                servers.append(server_data)
                total_log_count += server_data["log_count"]
                total_size += server_data["total_size_bytes"]
                total_errors += server_data["error_count"]
        except (OSError, PermissionError):
            pass

        # Sort servers by log count (most active first)
        servers.sort(key=lambda x: x["log_count"], reverse=True)

        return {
            "servers": servers,
            "server_count": len(servers),
            "total_log_count": total_log_count,
            "total_size_bytes": total_size,
            "total_errors": total_errors,
        }

    def extract(self) -> Dict[str, Any]:
        """Extract MCP log information."""
        cache_dir = get_cache_dir()

        if not cache_dir.exists():
            return {
                "directory_exists": False,
                "path": str(cache_dir),
                "total_projects": 0,
                "total_servers": 0,
                "total_log_files": 0,
                "total_size_bytes": 0,
                "projects": [],
            }

        projects = []
        total_servers = 0
        total_log_files = 0
        total_size = 0
        total_errors = 0

        try:
            for project_dir in cache_dir.iterdir():
                if not project_dir.is_dir():
                    continue

                # Skip non-project directories
                if project_dir.name.startswith("."):
                    continue

                project_data = self._extract_project_logs(project_dir)

                if project_data["server_count"] > 0:
                    projects.append({
                        "project": project_dir.name,
                        **project_data,
                    })
                    total_servers += project_data["server_count"]
                    total_log_files += project_data["total_log_count"]
                    total_size += project_data["total_size_bytes"]
                    total_errors += project_data["total_errors"]
        except (OSError, PermissionError):
            pass

        # Sort by total log count
        projects.sort(key=lambda x: x["total_log_count"], reverse=True)

        return {
            "directory_exists": True,
            "path": str(cache_dir),
            "total_projects": len(projects),
            "total_servers": total_servers,
            "total_log_files": total_log_files,
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "total_errors": total_errors,
            "projects": projects,
        }

    def to_sqlite(self, db) -> None:
        """Write MCP log summaries to SQLite."""
        data = self.get_data()
        projects = data.get("projects", [])
        if projects:
            db.insert_mcp_log_summaries(projects)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of MCP logs."""
        data = self.get_data()
        return {
            "source": self.name,
            "total_projects": data.get("total_projects", 0),
            "total_servers": data.get("total_servers", 0),
            "total_log_files": data.get("total_log_files", 0),
            "total_errors": data.get("total_errors", 0),
        }

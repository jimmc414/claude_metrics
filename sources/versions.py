"""Versions extractor."""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_versions_dir, format_bytes, get_claude_json_path, read_json_file


class VersionsSource(BaseSource):
    """Extract installed Claude Code version information."""

    name = "versions"
    description = "Installed Claude Code binary versions"
    source_paths = ["~/.local/share/claude/versions/"]

    def _get_dir_size(self, path: Path) -> int:
        """Calculate total size of a directory."""
        total = 0
        try:
            for entry in path.rglob("*"):
                if entry.is_file():
                    try:
                        total += entry.stat().st_size
                    except (OSError, PermissionError):
                        pass
        except (OSError, PermissionError):
            pass
        return total

    def _get_current_version(self) -> Optional[str]:
        """Get the current version from ~/.claude.json."""
        claude_json = read_json_file(get_claude_json_path())
        if claude_json:
            return claude_json.get("lastOnboardingVersion")
        return None

    def extract(self) -> Dict[str, Any]:
        """Extract installed version information."""
        versions_dir = get_versions_dir()

        if not versions_dir.exists():
            return {
                "directory_exists": False,
                "path": str(versions_dir),
                "total_versions": 0,
                "total_size_bytes": 0,
                "current_version": self._get_current_version(),
                "versions": [],
            }

        versions = []
        total_size = 0

        try:
            for version_dir in versions_dir.iterdir():
                if not version_dir.is_dir():
                    continue

                version_name = version_dir.name
                size = self._get_dir_size(version_dir)
                total_size += size

                # Get modification time as installation date
                try:
                    stat = version_dir.stat()
                    installed_at = datetime.fromtimestamp(stat.st_mtime).isoformat()
                except (OSError, PermissionError):
                    installed_at = None

                versions.append({
                    "version": version_name,
                    "size_bytes": size,
                    "size_human": format_bytes(size),
                    "installed_at": installed_at,
                })
        except (OSError, PermissionError):
            pass

        # Sort by version (attempt semantic sort, fall back to string)
        def version_key(v):
            try:
                parts = v["version"].split(".")
                return tuple(int(p) for p in parts if p.isdigit())
            except (ValueError, AttributeError):
                return (0,)

        versions.sort(key=version_key, reverse=True)

        current_version = self._get_current_version()

        return {
            "directory_exists": True,
            "path": str(versions_dir),
            "total_versions": len(versions),
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "current_version": current_version,
            "versions": versions,
        }

    def to_sqlite(self, db) -> None:
        """Write versions to SQLite."""
        data = self.get_data()
        versions = data.get("versions", [])
        current_version = data.get("current_version")
        if versions:
            db.insert_versions(versions, current_version)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of installed versions."""
        data = self.get_data()
        return {
            "source": self.name,
            "total_versions": data.get("total_versions", 0),
            "total_size_bytes": data.get("total_size_bytes", 0),
            "current_version": data.get("current_version"),
        }

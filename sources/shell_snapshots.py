"""Shell snapshots extractor."""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_claude_dir, format_bytes, get_file_stats


class ShellSnapshotsSource(BaseSource):
    """Extract shell environment snapshot information."""

    name = "shell_snapshots"
    description = "Shell environment snapshots"
    source_paths = ["~/.claude/shell-snapshots/"]

    # Pattern: snapshot-{shell}-{timestamp}-{random}.sh
    SNAPSHOT_PATTERN = re.compile(
        r"snapshot-(?P<shell>[^-]+)-(?P<timestamp>\d+)-(?P<random>[a-zA-Z0-9]+)\.sh"
    )

    def _get_snapshots_dir(self) -> Path:
        """Get the shell snapshots directory."""
        return get_claude_dir() / "shell-snapshots"

    def _parse_snapshot_filename(self, filename: str) -> Optional[Dict[str, Any]]:
        """Parse snapshot filename to extract metadata."""
        match = self.SNAPSHOT_PATTERN.match(filename)
        if match:
            return {
                "shell": match.group("shell"),
                "timestamp": match.group("timestamp"),
                "random_id": match.group("random"),
            }
        return None

    def extract(self) -> Dict[str, Any]:
        """Extract shell snapshot information."""
        snapshots_dir = self._get_snapshots_dir()

        if not snapshots_dir.exists():
            return {
                "directory_exists": False,
                "path": str(snapshots_dir),
                "total_snapshots": 0,
                "total_size_bytes": 0,
                "by_shell": {},
                "snapshots": [],
            }

        snapshots = []
        by_shell: Dict[str, int] = {}
        total_size = 0

        try:
            for file_path in snapshots_dir.glob("snapshot-*.sh"):
                if not file_path.is_file():
                    continue

                metadata = self._parse_snapshot_filename(file_path.name)
                stats = get_file_stats(file_path)
                size = stats.get("size_bytes", 0)
                total_size += size

                snapshot_info = {
                    "filename": file_path.name,
                    "size_bytes": size,
                    "size_human": format_bytes(size),
                    "modified_at": stats.get("modified_at"),
                }

                if metadata:
                    snapshot_info.update(metadata)
                    shell = metadata["shell"]
                    by_shell[shell] = by_shell.get(shell, 0) + 1

                snapshots.append(snapshot_info)
        except (OSError, PermissionError):
            pass

        # Sort by modified time (newest first)
        snapshots.sort(key=lambda x: x.get("modified_at", ""), reverse=True)

        return {
            "directory_exists": True,
            "path": str(snapshots_dir),
            "total_snapshots": len(snapshots),
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "by_shell": by_shell,
            "snapshots": snapshots,
        }

    def to_sqlite(self, db) -> None:
        """Write shell snapshots to SQLite."""
        data = self.get_data()
        snapshots = data.get("snapshots", [])
        if snapshots:
            db.insert_shell_snapshots(snapshots)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of shell snapshots."""
        data = self.get_data()
        return {
            "source": self.name,
            "total_snapshots": data.get("total_snapshots", 0),
            "total_size_bytes": data.get("total_size_bytes", 0),
            "shells": list(data.get("by_shell", {}).keys()),
        }

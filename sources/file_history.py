"""File history extractor."""

import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_claude_dir, format_bytes


class FileHistorySource(BaseSource):
    """Extract file version history information."""

    name = "file_history"
    description = "File version backups"
    source_paths = ["~/.claude/file-history/"]

    # Pattern: {hash}@v{version}
    VERSION_PATTERN = re.compile(r"^(?P<hash>[a-fA-F0-9]+)@v(?P<version>\d+)$")

    def _get_file_history_dir(self) -> Path:
        """Get the file-history directory."""
        return get_claude_dir() / "file-history"

    def _parse_version_filename(self, filename: str) -> Optional[Dict[str, Any]]:
        """Parse version filename to extract hash and version."""
        match = self.VERSION_PATTERN.match(filename)
        if match:
            return {
                "hash": match.group("hash"),
                "version": int(match.group("version")),
            }
        return None

    def _extract_session_history(self, session_dir: Path) -> Dict[str, Any]:
        """Extract file history for a single session."""
        files_by_hash: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
        total_size = 0

        try:
            for file_path in session_dir.iterdir():
                if not file_path.is_file():
                    continue

                metadata = self._parse_version_filename(file_path.name)
                if not metadata:
                    continue

                try:
                    size = file_path.stat().st_size
                except (OSError, PermissionError):
                    size = 0

                total_size += size
                files_by_hash[metadata["hash"]].append({
                    "version": metadata["version"],
                    "size_bytes": size,
                    "filename": file_path.name,
                })
        except (OSError, PermissionError):
            pass

        # Aggregate file info
        files = []
        for file_hash, versions in files_by_hash.items():
            versions.sort(key=lambda x: x["version"])
            total_file_size = sum(v["size_bytes"] for v in versions)

            files.append({
                "hash": file_hash,
                "version_count": len(versions),
                "max_version": max(v["version"] for v in versions),
                "total_size_bytes": total_file_size,
                "versions": versions,
            })

        return {
            "file_count": len(files),
            "version_count": sum(len(v) for v in files_by_hash.values()),
            "total_size_bytes": total_size,
            "files": files,
        }

    def extract(self) -> Dict[str, Any]:
        """Extract file history information."""
        history_dir = self._get_file_history_dir()

        if not history_dir.exists():
            return {
                "directory_exists": False,
                "path": str(history_dir),
                "total_sessions": 0,
                "total_files": 0,
                "total_versions": 0,
                "total_size_bytes": 0,
                "sessions": [],
            }

        sessions = []
        total_files = 0
        total_versions = 0
        total_size = 0

        try:
            for session_dir in history_dir.iterdir():
                if not session_dir.is_dir():
                    continue

                session_data = self._extract_session_history(session_dir)

                session_info = {
                    "session_id": session_dir.name,
                    **session_data,
                }

                # Don't include detailed file list to keep output manageable
                # Remove the detailed versions list for summary
                for f in session_info.get("files", []):
                    del f["versions"]

                sessions.append(session_info)
                total_files += session_data["file_count"]
                total_versions += session_data["version_count"]
                total_size += session_data["total_size_bytes"]
        except (OSError, PermissionError):
            pass

        # Sort by session ID
        sessions.sort(key=lambda x: x["session_id"])

        return {
            "directory_exists": True,
            "path": str(history_dir),
            "total_sessions": len(sessions),
            "total_files": total_files,
            "total_versions": total_versions,
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "sessions": sessions,
        }

    def to_sqlite(self, db) -> None:
        """Write file history to SQLite."""
        data = self.get_data()
        sessions = data.get("sessions", [])
        if sessions:
            db.insert_file_history(sessions)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of file history."""
        data = self.get_data()
        return {
            "source": self.name,
            "total_sessions": data.get("total_sessions", 0),
            "total_files": data.get("total_files", 0),
            "total_versions": data.get("total_versions", 0),
            "total_size_bytes": data.get("total_size_bytes", 0),
        }

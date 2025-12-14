"""Session environment extractor."""

from pathlib import Path
from typing import Any, Dict, List

from .base import BaseSource
from utils import get_claude_dir, format_bytes


class SessionEnvSource(BaseSource):
    """Extract per-session environment data."""

    name = "session_env"
    description = "Per-session environment data"
    source_paths = ["~/.claude/session-env/"]

    def _get_session_env_dir(self) -> Path:
        """Get the session-env directory."""
        return get_claude_dir() / "session-env"

    def _get_session_size(self, session_dir: Path) -> int:
        """Calculate total size of a session directory."""
        total = 0
        try:
            for entry in session_dir.rglob("*"):
                if entry.is_file():
                    try:
                        total += entry.stat().st_size
                    except (OSError, PermissionError):
                        pass
        except (OSError, PermissionError):
            pass
        return total

    def _get_session_files(self, session_dir: Path) -> List[str]:
        """Get list of files in a session directory."""
        files = []
        try:
            for entry in session_dir.iterdir():
                if entry.is_file():
                    files.append(entry.name)
        except (OSError, PermissionError):
            pass
        return files

    def extract(self) -> Dict[str, Any]:
        """Extract session environment information."""
        session_env_dir = self._get_session_env_dir()

        if not session_env_dir.exists():
            return {
                "directory_exists": False,
                "path": str(session_env_dir),
                "total_sessions": 0,
                "sessions_with_data": 0,
                "total_size_bytes": 0,
                "sessions": [],
            }

        sessions = []
        total_size = 0
        sessions_with_data = 0

        try:
            for session_dir in session_env_dir.iterdir():
                if not session_dir.is_dir():
                    continue

                files = self._get_session_files(session_dir)
                size = self._get_session_size(session_dir)
                total_size += size

                session_info = {
                    "session_id": session_dir.name,
                    "files": files,
                    "file_count": len(files),
                    "size_bytes": size,
                    "size_human": format_bytes(size),
                }

                if files:
                    sessions_with_data += 1

                sessions.append(session_info)
        except (OSError, PermissionError):
            pass

        # Sort by session ID
        sessions.sort(key=lambda x: x["session_id"])

        return {
            "directory_exists": True,
            "path": str(session_env_dir),
            "total_sessions": len(sessions),
            "sessions_with_data": sessions_with_data,
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "sessions": sessions,
        }

    def to_sqlite(self, db) -> None:
        """Write session environments to SQLite."""
        data = self.get_data()
        sessions = data.get("sessions", [])
        if sessions:
            db.insert_session_env(sessions)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of session environments."""
        data = self.get_data()
        return {
            "source": self.name,
            "total_sessions": data.get("total_sessions", 0),
            "sessions_with_data": data.get("sessions_with_data", 0),
            "total_size_bytes": data.get("total_size_bytes", 0),
        }

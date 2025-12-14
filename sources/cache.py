"""Cache directory extractor."""

import os
from pathlib import Path
from typing import Any, Dict, List

from .base import BaseSource
from utils import format_bytes


class CacheSource(BaseSource):
    """Extract Claude Code cache directory information."""

    name = "cache"
    description = "Claude Code cache directory contents"
    source_paths = ["~/.cache/claude/"]

    def _get_cache_dir(self) -> Path:
        """Get the cache directory path."""
        return Path.home() / ".cache" / "claude"

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

    def _count_files(self, path: Path) -> int:
        """Count files in a directory."""
        count = 0
        try:
            for entry in path.rglob("*"):
                if entry.is_file():
                    count += 1
        except (OSError, PermissionError):
            pass
        return count

    def extract(self) -> Dict[str, Any]:
        """Extract cache directory information."""
        cache_dir = self._get_cache_dir()

        if not cache_dir.exists():
            return {
                "cache_exists": False,
                "path": str(cache_dir),
                "total_size_bytes": 0,
                "subdirectories": [],
                "file_count": 0,
            }

        # Get subdirectories
        subdirs = []
        try:
            for entry in cache_dir.iterdir():
                if entry.is_dir():
                    size = self._get_dir_size(entry)
                    file_count = self._count_files(entry)
                    subdirs.append({
                        "name": entry.name,
                        "size_bytes": size,
                        "size_human": format_bytes(size),
                        "file_count": file_count,
                    })
        except (OSError, PermissionError):
            pass

        # Calculate totals
        total_size = self._get_dir_size(cache_dir)
        total_files = self._count_files(cache_dir)

        return {
            "cache_exists": True,
            "path": str(cache_dir),
            "total_size_bytes": total_size,
            "total_size_human": format_bytes(total_size),
            "file_count": total_files,
            "subdirectories": subdirs,
        }

    def to_sqlite(self, db) -> None:
        """Write cache info to SQLite."""
        data = self.get_data()
        db.insert_cache_info(data)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of cache directory."""
        data = self.get_data()
        return {
            "source": self.name,
            "cache_exists": data.get("cache_exists", False),
            "total_size_bytes": data.get("total_size_bytes", 0),
            "subdirectory_count": len(data.get("subdirectories", [])),
        }

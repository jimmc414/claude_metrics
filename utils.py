"""Utility functions for Claude Metrics."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Generator, Iterator, List, Optional, Union


def get_claude_dir() -> Path:
    """Get the Claude Code data directory (~/.claude/)."""
    return Path.home() / ".claude"


def get_claude_json_path() -> Path:
    """Get the global Claude state file (~/.claude.json)."""
    return Path.home() / ".claude.json"


def get_config_dir() -> Path:
    """Get the Claude config directory (~/.config/claude/)."""
    return Path.home() / ".config" / "claude"


def get_cache_dir() -> Path:
    """Get the Claude cache directory (~/.cache/claude-cli-nodejs/)."""
    return Path.home() / ".cache" / "claude-cli-nodejs"


def get_versions_dir() -> Path:
    """Get the Claude versions directory (~/.local/share/claude/versions/)."""
    return Path.home() / ".local" / "share" / "claude" / "versions"


def read_json_file(path: Path) -> Optional[Dict[str, Any]]:
    """Read and parse a JSON file, returning None if it doesn't exist or is invalid."""
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError, UnicodeDecodeError):
        return None


def read_jsonl_file(path: Path) -> Generator[Dict[str, Any], None, None]:
    """Stream records from a JSONL file."""
    if not path.exists():
        return
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    # Skip malformed lines
                    continue
    except (IOError, UnicodeDecodeError):
        return


def count_jsonl_lines(path: Path) -> int:
    """Count valid JSONL lines in a file."""
    if not path.exists():
        return 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    count += 1
    except (IOError, UnicodeDecodeError):
        pass
    return count


def iter_jsonl_files(directory: Path, pattern: str = "*.jsonl") -> Iterator[Path]:
    """Iterate over JSONL files in a directory (non-recursive)."""
    if not directory.exists():
        return
    for path in directory.glob(pattern):
        if path.is_file():
            yield path


def iter_jsonl_files_recursive(directory: Path, pattern: str = "**/*.jsonl") -> Iterator[Path]:
    """Recursively iterate over JSONL files in a directory."""
    if not directory.exists():
        return
    for path in directory.glob(pattern):
        if path.is_file():
            yield path


def iter_json_files(directory: Path, pattern: str = "*.json") -> Iterator[Path]:
    """Iterate over JSON files in a directory (non-recursive)."""
    if not directory.exists():
        return
    for path in directory.glob(pattern):
        if path.is_file():
            yield path


def iter_markdown_files(directory: Path, pattern: str = "*.md") -> Iterator[Path]:
    """Iterate over Markdown files in a directory (non-recursive)."""
    if not directory.exists():
        return
    for path in directory.glob(pattern):
        if path.is_file():
            yield path


def parse_iso_timestamp(ts: str) -> Optional[datetime]:
    """Parse an ISO timestamp string to datetime."""
    if not ts:
        return None
    try:
        # Handle various ISO formats
        ts = ts.replace("Z", "+00:00")
        return datetime.fromisoformat(ts)
    except (ValueError, TypeError):
        return None


def unix_ms_to_datetime(ms: int) -> Optional[datetime]:
    """Convert Unix timestamp in milliseconds to datetime."""
    if not ms:
        return None
    try:
        return datetime.fromtimestamp(ms / 1000)
    except (ValueError, TypeError, OSError):
        return None


def format_bytes(num_bytes: int) -> str:
    """Format bytes as human-readable string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(num_bytes) < 1024:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f} PB"


def safe_get(data: Dict[str, Any], *keys: str, default: Any = None) -> Any:
    """Safely get a nested value from a dictionary."""
    current = data
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key, default)
        if current is None:
            return default
    return current


def project_path_to_dir_name(project_path: str) -> str:
    """Convert a project path to Claude's directory naming convention.

    Claude Code converts paths like /mnt/c/python/myproject to -mnt-c-python-myproject
    """
    return project_path.replace("/", "-").lstrip("-")


def dir_name_to_project_path(dir_name: str) -> str:
    """Convert Claude's directory name back to a path.

    Converts -mnt-c-python-myproject back to /mnt/c/python/myproject
    """
    if dir_name.startswith("-"):
        dir_name = dir_name[1:]
    return "/" + dir_name.replace("-", "/")


def get_file_stats(path: Path) -> Dict[str, Any]:
    """Get file statistics (size, mtime, etc.)."""
    if not path.exists():
        return {}
    stat = path.stat()
    return {
        "size_bytes": stat.st_size,
        "size_human": format_bytes(stat.st_size),
        "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "created_at": datetime.fromtimestamp(stat.st_ctime).isoformat(),
    }


def ensure_dir(path: Path) -> Path:
    """Ensure a directory exists, creating it if necessary."""
    path.mkdir(parents=True, exist_ok=True)
    return path

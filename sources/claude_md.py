"""CLAUDE.md extractor."""

import re
from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_claude_json_path, read_json_file, format_bytes


class ClaudeMdSource(BaseSource):
    """Extract CLAUDE.md file information from known projects."""

    name = "claude_md"
    description = "Project instruction files (CLAUDE.md)"
    source_paths = ["<project>/CLAUDE.md"]

    # Pattern to extract markdown headers
    HEADER_PATTERN = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

    # Pattern to detect include directives
    INCLUDE_PATTERN = re.compile(r"@include\s+(.+)|{{include\s+(.+?)}}", re.IGNORECASE)

    def _get_known_projects(self) -> List[str]:
        """Get list of known project paths from ~/.claude.json."""
        claude_json = read_json_file(get_claude_json_path())
        if claude_json and "projects" in claude_json:
            return list(claude_json["projects"].keys())
        return []

    def _analyze_claude_md(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a CLAUDE.md file."""
        try:
            content = file_path.read_text(encoding="utf-8")
        except (OSError, PermissionError, UnicodeDecodeError):
            return {"error": "Could not read file"}

        stat = file_path.stat()

        # Count lines and words
        lines = content.split("\n")
        line_count = len(lines)
        word_count = len(content.split())

        # Extract section headers
        headers = []
        for match in self.HEADER_PATTERN.finditer(content):
            level = len(match.group(1))
            title = match.group(2).strip()
            headers.append({"level": level, "title": title})

        # Find include directives
        includes = []
        for match in self.INCLUDE_PATTERN.finditer(content):
            include_path = match.group(1) or match.group(2)
            if include_path:
                includes.append(include_path.strip())

        return {
            "size_bytes": stat.st_size,
            "size_human": format_bytes(stat.st_size),
            "line_count": line_count,
            "word_count": word_count,
            "sections": headers,
            "section_count": len(headers),
            "includes": includes,
            "has_includes": len(includes) > 0,
        }

    def extract(self) -> Dict[str, Any]:
        """Extract CLAUDE.md information from all known projects."""
        projects = self._get_known_projects()

        files = []
        projects_scanned = 0
        projects_with_claude_md = 0

        for project_path in projects:
            projects_scanned += 1

            # Check for CLAUDE.md in project root
            project_dir = Path(project_path)
            claude_md_path = project_dir / "CLAUDE.md"

            if claude_md_path.exists() and claude_md_path.is_file():
                projects_with_claude_md += 1
                analysis = self._analyze_claude_md(claude_md_path)

                files.append({
                    "project": project_path,
                    "path": str(claude_md_path),
                    **analysis,
                })

        # Sort by project path
        files.sort(key=lambda x: x["project"])

        return {
            "projects_scanned": projects_scanned,
            "projects_with_claude_md": projects_with_claude_md,
            "adoption_rate": (
                projects_with_claude_md / projects_scanned
                if projects_scanned > 0 else 0
            ),
            "files": files,
        }

    def to_sqlite(self, db) -> None:
        """Write CLAUDE.md files to SQLite."""
        data = self.get_data()
        files = data.get("files", [])
        if files:
            db.insert_claude_md_files(files)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of CLAUDE.md files."""
        data = self.get_data()
        return {
            "source": self.name,
            "projects_scanned": data.get("projects_scanned", 0),
            "projects_with_claude_md": data.get("projects_with_claude_md", 0),
            "adoption_rate": data.get("adoption_rate", 0),
        }

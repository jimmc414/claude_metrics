"""Plans source extractor."""

import re
from typing import Any, Dict, List

from database import MetricsDatabase
from utils import get_claude_dir, iter_markdown_files, get_file_stats
from .base import BaseSource


class PlansSource(BaseSource):
    """Extractor for ~/.claude/plans/*.md.

    Contains implementation plan documents with objectives,
    deliverables, and implementation steps.
    """

    name = "plans"
    description = "Implementation plan documents"
    source_paths = ["~/.claude/plans/*.md"]

    def __init__(self, include_sensitive: bool = False, include_content: bool = False):
        """Initialize the plans extractor.

        Args:
            include_sensitive: If True, include sensitive data
            include_content: If True, include full plan content
        """
        super().__init__(include_sensitive)
        self.include_content = include_content

    def _analyze_plan(self, content: str) -> Dict[str, Any]:
        """Analyze a plan's structure."""
        lines = content.split("\n")

        # Count headers by level
        headers = {"h1": 0, "h2": 0, "h3": 0, "h4": 0}
        for line in lines:
            if line.startswith("#### "):
                headers["h4"] += 1
            elif line.startswith("### "):
                headers["h3"] += 1
            elif line.startswith("## "):
                headers["h2"] += 1
            elif line.startswith("# "):
                headers["h1"] += 1

        # Count code blocks
        code_blocks = len(re.findall(r"```", content)) // 2

        # Count checklist items
        checklist_total = len(re.findall(r"^\s*[-*]\s*\[[ x]\]", content, re.MULTILINE))
        checklist_checked = len(re.findall(r"^\s*[-*]\s*\[x\]", content, re.MULTILINE | re.IGNORECASE))

        # Count bullet points
        bullet_points = len(re.findall(r"^\s*[-*]\s+[^\[]", content, re.MULTILINE))

        # Extract title (first H1)
        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_match.group(1) if title_match else None

        return {
            "title": title,
            "line_count": len(lines),
            "char_count": len(content),
            "headers": headers,
            "total_headers": sum(headers.values()),
            "code_block_count": code_blocks,
            "checklist_total": checklist_total,
            "checklist_checked": checklist_checked,
            "bullet_points": bullet_points,
        }

    def extract(self) -> Dict[str, Any]:
        """Extract plans data.

        Returns:
            Dictionary containing:
            - total_plans: Number of plan files
            - plans: List of plan metadata
            - total_lines: Total lines across all plans
        """
        plans_dir = get_claude_dir() / "plans"

        if not plans_dir.exists():
            return {"error": "Plans directory not found", "path": str(plans_dir)}

        plans = []
        total_lines = 0
        total_code_blocks = 0

        for plan_file in iter_markdown_files(plans_dir):
            file_stats = get_file_stats(plan_file)

            try:
                content = plan_file.read_text(encoding="utf-8")
            except Exception:
                content = ""

            analysis = self._analyze_plan(content)
            total_lines += analysis["line_count"]
            total_code_blocks += analysis["code_block_count"]

            plan_data = {
                "filename": plan_file.name,
                "file_path": str(plan_file),
                "size_bytes": file_stats.get("size_bytes", 0),
                "created_at": file_stats.get("created_at"),
                "modified_at": file_stats.get("modified_at"),
                **analysis,
            }

            if self.include_content:
                plan_data["content"] = content

            plans.append(plan_data)

        # Sort by modification time (newest first)
        plans.sort(key=lambda x: x.get("modified_at", ""), reverse=True)

        return {
            "path": str(plans_dir),
            "total_plans": len(plans),
            "total_lines": total_lines,
            "total_code_blocks": total_code_blocks,
            "plans": plans,
        }

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write plans to SQLite."""
        data = self.get_data()

        if "error" in data or db.conn is None:
            return

        plans = data.get("plans", [])

        for plan in plans:
            db.conn.execute(
                """
                INSERT OR REPLACE INTO plans
                (filename, file_path, size_bytes, line_count,
                 header_count, code_block_count, created_at, modified_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    plan.get("filename"),
                    plan.get("file_path"),
                    plan.get("size_bytes"),
                    plan.get("line_count"),
                    plan.get("total_headers"),
                    plan.get("code_block_count"),
                    plan.get("created_at"),
                    plan.get("modified_at"),
                ),
            )

        db.commit()

    def get_summary(self) -> Dict[str, Any]:
        """Get plans summary."""
        data = self.get_data()

        if "error" in data:
            return {"source": self.name, "error": data["error"]}

        plans = data.get("plans", [])

        # Calculate averages
        if plans:
            avg_lines = sum(p.get("line_count", 0) for p in plans) / len(plans)
            avg_code_blocks = sum(p.get("code_block_count", 0) for p in plans) / len(plans)
        else:
            avg_lines = 0
            avg_code_blocks = 0

        return {
            "source": self.name,
            "total_plans": len(plans),
            "total_lines": data.get("total_lines", 0),
            "total_code_blocks": data.get("total_code_blocks", 0),
            "avg_lines_per_plan": round(avg_lines, 1),
            "avg_code_blocks_per_plan": round(avg_code_blocks, 1),
        }

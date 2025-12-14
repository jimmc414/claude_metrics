"""Project configuration extractor."""

from pathlib import Path
from typing import Any, Dict, List, Optional

from .base import BaseSource
from utils import get_claude_json_path, read_json_file, format_bytes


class ProjectConfigSource(BaseSource):
    """Extract project-level Claude Code configurations."""

    name = "project_config"
    description = "Project-level Claude Code configurations"
    source_paths = ["<project>/.claude/"]

    def _get_known_projects(self) -> List[str]:
        """Get list of known project paths from ~/.claude.json."""
        claude_json = read_json_file(get_claude_json_path())
        if claude_json and "projects" in claude_json:
            return list(claude_json["projects"].keys())
        return []

    def _list_extension_names(self, ext_dir: Path) -> List[str]:
        """List extension names (files without extension or directory names)."""
        names = []
        if not ext_dir.exists():
            return names

        try:
            for entry in ext_dir.iterdir():
                if entry.is_file() and entry.suffix == ".md":
                    names.append(entry.stem)
                elif entry.is_dir():
                    names.append(entry.name)
        except (OSError, PermissionError):
            pass

        return sorted(names)

    def _extract_settings_local(self, settings_path: Path) -> Optional[Dict[str, Any]]:
        """Extract settings.local.json configuration."""
        settings = read_json_file(settings_path)
        if not settings:
            return None

        permissions = settings.get("permissions", {})

        return {
            "has_permissions": bool(permissions),
            "allow_rules": len(permissions.get("allow", [])),
            "deny_rules": len(permissions.get("deny", [])),
        }

    def _extract_project_config(self, project_path: str) -> Dict[str, Any]:
        """Extract configuration for a single project."""
        project_dir = Path(project_path)
        claude_dir = project_dir / ".claude"

        result = {
            "path": project_path,
            "has_claude_dir": claude_dir.exists(),
        }

        if not claude_dir.exists():
            return result

        # Check for settings.local.json
        settings_path = claude_dir / "settings.local.json"
        if settings_path.exists():
            settings_info = self._extract_settings_local(settings_path)
            if settings_info:
                result["settings"] = settings_info
                result["has_settings"] = True
            else:
                result["has_settings"] = False
        else:
            result["has_settings"] = False

        # List agents
        agents_dir = claude_dir / "agents"
        result["agents"] = self._list_extension_names(agents_dir)
        result["agent_count"] = len(result["agents"])

        # List commands
        commands_dir = claude_dir / "commands"
        result["commands"] = self._list_extension_names(commands_dir)
        result["command_count"] = len(result["commands"])

        # List skills
        skills_dir = claude_dir / "skills"
        skill_names = []
        if skills_dir.exists():
            try:
                for entry in skills_dir.iterdir():
                    if entry.is_dir():
                        # Check for SKILL.md inside
                        skill_file = entry / "SKILL.md"
                        if skill_file.exists():
                            skill_names.append(entry.name)
            except (OSError, PermissionError):
                pass
        result["skills"] = sorted(skill_names)
        result["skill_count"] = len(skill_names)

        # Calculate customization score
        result["customization_score"] = (
            result["agent_count"] +
            result["command_count"] +
            result["skill_count"] +
            (1 if result["has_settings"] else 0)
        )

        return result

    def extract(self) -> Dict[str, Any]:
        """Extract project configurations from all known projects."""
        projects = self._get_known_projects()

        configs = []
        projects_scanned = 0
        projects_with_config = 0
        total_agents = 0
        total_commands = 0
        total_skills = 0

        for project_path in projects:
            projects_scanned += 1
            config = self._extract_project_config(project_path)

            if config.get("has_claude_dir"):
                projects_with_config += 1
                total_agents += config.get("agent_count", 0)
                total_commands += config.get("command_count", 0)
                total_skills += config.get("skill_count", 0)

            configs.append(config)

        # Sort by customization score (highest first)
        configs.sort(key=lambda x: x.get("customization_score", 0), reverse=True)

        return {
            "projects_scanned": projects_scanned,
            "projects_with_config": projects_with_config,
            "total_agents": total_agents,
            "total_commands": total_commands,
            "total_skills": total_skills,
            "adoption_rate": (
                projects_with_config / projects_scanned
                if projects_scanned > 0 else 0
            ),
            "projects": configs,
        }

    def to_sqlite(self, db) -> None:
        """Write project configurations to SQLite."""
        data = self.get_data()
        projects = data.get("projects", [])
        if projects:
            db.insert_project_configs(projects)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of project configurations."""
        data = self.get_data()
        return {
            "source": self.name,
            "projects_scanned": data.get("projects_scanned", 0),
            "projects_with_config": data.get("projects_with_config", 0),
            "total_agents": data.get("total_agents", 0),
            "total_commands": data.get("total_commands", 0),
            "total_skills": data.get("total_skills", 0),
        }

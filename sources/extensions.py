"""Extensions source extractor (agents, commands, skills, plugins)."""

import re
from typing import Any, Dict, List, Optional, Tuple

from database import MetricsDatabase
from utils import (
    get_claude_dir,
    iter_markdown_files,
    iter_json_files,
    read_json_file,
    get_file_stats,
)
from .base import BaseSource


class ExtensionsSource(BaseSource):
    """Extractor for Claude Code extensions.

    Extracts:
    - ~/.claude/agents/*.md - Custom agent definitions
    - ~/.claude/commands/*.md - Custom slash commands
    - ~/.claude/skills/*/SKILL.md - Custom skills
    - ~/.claude/plugins/ - Plugin configurations
    - ~/.claude/statsig/ - Feature flag cache
    """

    name = "extensions"
    description = "Custom agents, commands, skills, and plugins"
    source_paths = [
        "~/.claude/agents/*.md",
        "~/.claude/commands/*.md",
        "~/.claude/skills/*/SKILL.md",
        "~/.claude/plugins/",
        "~/.claude/statsig/",
    ]

    def _parse_markdown_extension(
        self, path, ext_type: str
    ) -> Dict[str, Any]:
        """Parse a markdown extension file (agent, command, skill)."""
        stats = get_file_stats(path)

        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            content = ""

        # Extract name from first H1
        name_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        name = name_match.group(1) if name_match else path.stem

        # Extract description (first non-empty, non-header line)
        description = ""
        for line in content.split("\n"):
            line = line.strip()
            if line and not line.startswith("#"):
                description = line[:200]  # Truncate
                break

        # Extract triggers for skills
        triggers = []
        trigger_match = re.search(
            r"(?:triggers?|keywords?):\s*(.+)",
            content,
            re.IGNORECASE
        )
        if trigger_match:
            triggers = [t.strip() for t in trigger_match.group(1).split(",")]

        return {
            "type": ext_type,
            "name": name,
            "description": description,
            "triggers": triggers,
            "file_path": str(path),
            "size_bytes": stats.get("size_bytes", 0),
            "line_count": len(content.split("\n")),
            "scope": "global",
        }

    def _extract_agents(self) -> List[Dict[str, Any]]:
        """Extract agent definitions."""
        agents_dir = get_claude_dir() / "agents"
        agents = []

        for agent_file in iter_markdown_files(agents_dir):
            agent = self._parse_markdown_extension(agent_file, "agent")
            agents.append(agent)

        return sorted(agents, key=lambda x: x["name"].lower())

    def _extract_commands(self) -> List[Dict[str, Any]]:
        """Extract command definitions."""
        commands_dir = get_claude_dir() / "commands"
        commands = []

        for cmd_file in iter_markdown_files(commands_dir):
            cmd = self._parse_markdown_extension(cmd_file, "command")
            commands.append(cmd)

        return sorted(commands, key=lambda x: x["name"].lower())

    def _extract_skills(self) -> List[Dict[str, Any]]:
        """Extract skill definitions."""
        skills_dir = get_claude_dir() / "skills"
        skills = []

        if not skills_dir.exists():
            return skills

        for skill_dir in skills_dir.iterdir():
            if not skill_dir.is_dir():
                continue

            skill_file = skill_dir / "SKILL.md"
            if skill_file.exists():
                skill = self._parse_markdown_extension(skill_file, "skill")
                skill["skill_dir"] = str(skill_dir)

                # Check for additional files
                skill["has_cheatsheet"] = (skill_dir / "CHEATSHEET.md").exists()
                skill["has_reference"] = (skill_dir / "reference.md").exists()
                skill["has_configs"] = (skill_dir / "configs").is_dir()
                skill["has_scripts"] = (skill_dir / "scripts").is_dir()

                skills.append(skill)

        return sorted(skills, key=lambda x: x["name"].lower())

    def _extract_plugins(self) -> Dict[str, Any]:
        """Extract plugin configuration."""
        plugins_dir = get_claude_dir() / "plugins"

        result = {
            "exists": plugins_dir.exists(),
            "path": str(plugins_dir),
        }

        if not plugins_dir.exists():
            return result

        # Read installed plugins
        installed = read_json_file(plugins_dir / "installed_plugins.json")
        result["installed_plugins"] = installed or {}

        # Read known marketplaces
        marketplaces = read_json_file(plugins_dir / "known_marketplaces.json")
        result["known_marketplaces"] = marketplaces or {}

        # Read config
        config = read_json_file(plugins_dir / "config.json")
        result["config"] = config or {}

        return result

    def _extract_statsig(self) -> Dict[str, Any]:
        """Extract Statsig feature flag cache."""
        statsig_dir = get_claude_dir() / "statsig"

        result = {
            "exists": statsig_dir.exists(),
            "path": str(statsig_dir),
        }

        if not statsig_dir.exists():
            return result

        # Count cache files
        cache_files = list(statsig_dir.glob("*"))
        result["cache_file_count"] = len(cache_files)
        result["cache_files"] = [f.name for f in cache_files[:20]]  # Limit

        return result

    def extract(self) -> Dict[str, Any]:
        """Extract all extension data.

        Returns:
            Dictionary containing:
            - agents: List of custom agents
            - commands: List of custom commands
            - skills: List of custom skills
            - plugins: Plugin configuration
            - statsig: Feature flag cache info
        """
        agents = self._extract_agents()
        commands = self._extract_commands()
        skills = self._extract_skills()
        plugins = self._extract_plugins()
        statsig = self._extract_statsig()

        return {
            "agents": agents,
            "agent_count": len(agents),
            "commands": commands,
            "command_count": len(commands),
            "skills": skills,
            "skill_count": len(skills),
            "plugins": plugins,
            "statsig": statsig,
            "total_extensions": len(agents) + len(commands) + len(skills),
        }

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write extensions to SQLite."""
        data = self.get_data()

        if db.conn is None:
            return

        # Insert agents
        for agent in data.get("agents", []):
            db.conn.execute(
                """
                INSERT OR REPLACE INTO extensions
                (type, name, description, file_path, size_bytes, scope)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    "agent",
                    agent.get("name"),
                    agent.get("description"),
                    agent.get("file_path"),
                    agent.get("size_bytes"),
                    "global",
                ),
            )

        # Insert commands
        for cmd in data.get("commands", []):
            db.conn.execute(
                """
                INSERT OR REPLACE INTO extensions
                (type, name, description, file_path, size_bytes, scope)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    "command",
                    cmd.get("name"),
                    cmd.get("description"),
                    cmd.get("file_path"),
                    cmd.get("size_bytes"),
                    "global",
                ),
            )

        # Insert skills
        for skill in data.get("skills", []):
            db.conn.execute(
                """
                INSERT OR REPLACE INTO extensions
                (type, name, description, file_path, size_bytes, scope)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    "skill",
                    skill.get("name"),
                    skill.get("description"),
                    skill.get("file_path"),
                    skill.get("size_bytes"),
                    "global",
                ),
            )

        db.commit()

    def get_summary(self) -> Dict[str, Any]:
        """Get extensions summary."""
        data = self.get_data()

        return {
            "source": self.name,
            "agent_count": data.get("agent_count", 0),
            "command_count": data.get("command_count", 0),
            "skill_count": data.get("skill_count", 0),
            "total_extensions": data.get("total_extensions", 0),
            "plugins_configured": bool(data.get("plugins", {}).get("installed_plugins")),
            "statsig_cache_files": data.get("statsig", {}).get("cache_file_count", 0),
        }

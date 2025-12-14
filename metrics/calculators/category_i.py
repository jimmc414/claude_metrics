"""Category I Calculator: Project Metrics (D173-D188)."""

from collections import defaultdict
from typing import Dict, List, Set

from .base import BaseCalculator
from .helpers import mean, safe_divide
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryICalculator(BaseCalculator):
    """Calculator for Category I: Project Metrics."""

    category = "I"

    MAIN_BRANCHES = {"main", "master"}

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _get_project_distribution(self) -> Dict[str, int]:
        """Get session count per project."""
        distribution: Dict[str, int] = defaultdict(int)
        for session in self.data.sessions:
            project = getattr(session, "project_path", "") or "unknown"
            distribution[project] += 1
        return dict(distribution)

    def _get_branch_info(self) -> Dict[str, int]:
        """Get branch usage statistics."""
        branches: Dict[str, int] = defaultdict(int)
        for session in self.data.sessions:
            branch = getattr(session, "git_branch", "")
            if branch:
                branches[branch] += 1
        return dict(branches)

    # D173-D178: Project Activity

    def _calc_d173(self, definition: MetricDefinition) -> MetricValue:
        """D173: Total projects."""
        projects = set()
        for session in self.data.sessions:
            project = getattr(session, "project_path", None)
            if project:
                projects.add(project)
        return self.create_value("D173", len(projects))

    def _calc_d174(self, definition: MetricDefinition) -> MetricValue:
        """D174: Sessions per project."""
        distribution = self._get_project_distribution()
        return self.create_value("D174", distribution, breakdown=distribution)

    def _calc_d175(self, definition: MetricDefinition) -> MetricValue:
        """D175: Most active project."""
        distribution = self.get_dependency_safe("D174", {})
        if not distribution:
            return self.create_value("D175", "none")
        most_active = max(distribution.items(), key=lambda x: x[1])[0]
        # Return just the project name (last part of path)
        project_name = most_active.split("/")[-1] if "/" in most_active else most_active
        return self.create_value("D175", project_name)

    def _calc_d176(self, definition: MetricDefinition) -> MetricValue:
        """D176: Messages per project."""
        distribution: Dict[str, int] = defaultdict(int)
        for session in self.data.sessions:
            project = getattr(session, "project_path", "") or "unknown"
            distribution[project] += session.message_count
        result = dict(distribution)
        return self.create_value("D176", result, breakdown=result)

    def _calc_d177(self, definition: MetricDefinition) -> MetricValue:
        """D177: Time per project (hours)."""
        distribution: Dict[str, float] = defaultdict(float)
        for session in self.data.sessions:
            project = getattr(session, "project_path", "") or "unknown"
            hours = session.duration_ms / 3600000
            distribution[project] += hours
        result = {k: round(v, 2) for k, v in distribution.items()}
        return self.create_value("D177", result, breakdown=result)

    def _calc_d178(self, definition: MetricDefinition) -> MetricValue:
        """D178: Tools per project."""
        distribution: Dict[str, int] = defaultdict(int)
        for tc in self.data.tool_calls:
            # Get project from session
            session = next(
                (s for s in self.data.sessions if s.session_id == tc.session_id),
                None
            )
            if session:
                project = getattr(session, "project_path", "") or "unknown"
                distribution[project] += 1
        result = dict(distribution)
        return self.create_value("D178", result, breakdown=result)

    # D179-D183: Git Activity

    def _calc_d179(self, definition: MetricDefinition) -> MetricValue:
        """D179: Branches worked on."""
        branches = set()
        for session in self.data.sessions:
            branch = getattr(session, "git_branch", "")
            if branch:
                branches.add(branch)
        return self.create_value("D179", len(branches))

    def _calc_d180(self, definition: MetricDefinition) -> MetricValue:
        """D180: Main/master branch activity."""
        count = sum(
            1 for session in self.data.sessions
            if getattr(session, "git_branch", "") in self.MAIN_BRANCHES
        )
        return self.create_value("D180", count)

    def _calc_d181(self, definition: MetricDefinition) -> MetricValue:
        """D181: Feature branch activity."""
        count = sum(
            1 for session in self.data.sessions
            if getattr(session, "git_branch", "") and
            getattr(session, "git_branch", "") not in self.MAIN_BRANCHES
        )
        return self.create_value("D181", count)

    def _calc_d182(self, definition: MetricDefinition) -> MetricValue:
        """D182: Branch switching frequency."""
        if not self.data.sessions:
            return self.create_value("D182", 0.0)

        # Count branch changes across sessions
        sorted_sessions = sorted(
            self.data.sessions,
            key=lambda s: s.start_time if s.start_time else self._now
        )

        switches = 0
        prev_branch = None
        for session in sorted_sessions:
            branch = getattr(session, "git_branch", "")
            if prev_branch is not None and branch and branch != prev_branch:
                switches += 1
            prev_branch = branch

        rate = safe_divide(switches, len(self.data.sessions))
        return self.create_value("D182", round(rate, 4))

    def _calc_d183(self, definition: MetricDefinition) -> MetricValue:
        """D183: Empty branch sessions."""
        count = sum(
            1 for session in self.data.sessions
            if not getattr(session, "git_branch", "")
        )
        return self.create_value("D183", count)

    # D184-D188: Project Complexity

    def _calc_d184(self, definition: MetricDefinition) -> MetricValue:
        """D184: Files per project."""
        distribution: Dict[str, Set[str]] = defaultdict(set)
        for tc in self.data.tool_calls:
            if tc.file_path:
                # Get project from session
                session = next(
                    (s for s in self.data.sessions if s.session_id == tc.session_id),
                    None
                )
                if session:
                    project = getattr(session, "project_path", "") or "unknown"
                    distribution[project].add(tc.file_path)
        result = {k: len(v) for k, v in distribution.items()}
        return self.create_value("D184", result, breakdown=result)

    def _calc_d185(self, definition: MetricDefinition) -> MetricValue:
        """D185: Tool diversity per project."""
        distribution: Dict[str, Set[str]] = defaultdict(set)
        for tc in self.data.tool_calls:
            session = next(
                (s for s in self.data.sessions if s.session_id == tc.session_id),
                None
            )
            if session:
                project = getattr(session, "project_path", "") or "unknown"
                distribution[project].add(tc.tool_name)
        result = {k: len(v) for k, v in distribution.items()}
        return self.create_value("D185", result, breakdown=result)

    def _calc_d186(self, definition: MetricDefinition) -> MetricValue:
        """D186: Session depth per project."""
        distribution: Dict[str, List[int]] = defaultdict(list)
        for session in self.data.sessions:
            project = getattr(session, "project_path", "") or "unknown"
            distribution[project].append(session.message_count)
        result = {k: round(mean(v), 2) for k, v in distribution.items()}
        return self.create_value("D186", result, breakdown=result)

    def _calc_d187(self, definition: MetricDefinition) -> MetricValue:
        """D187: Multi-project sessions."""
        # Count sessions that touched multiple projects (via file paths)
        multi_project_count = 0
        for session in self.data.sessions:
            projects = set()
            session_tools = [
                tc for tc in self.data.tool_calls
                if tc.session_id == session.session_id and tc.file_path
            ]
            for tc in session_tools:
                # Extract project from file path
                path_parts = tc.file_path.split("/")
                if len(path_parts) > 1:
                    projects.add(path_parts[0])
            if len(projects) > 1:
                multi_project_count += 1
        return self.create_value("D187", multi_project_count)

    def _calc_d188(self, definition: MetricDefinition) -> MetricValue:
        """D188: Project switching frequency (per day)."""
        if not self.data.window_days:
            return self.create_value("D188", 0.0)

        # Count project changes
        sorted_sessions = sorted(
            self.data.sessions,
            key=lambda s: s.start_time if s.start_time else self._now
        )

        switches = 0
        prev_project = None
        for session in sorted_sessions:
            project = getattr(session, "project_path", "")
            if prev_project is not None and project and project != prev_project:
                switches += 1
            prev_project = project

        rate = safe_divide(switches, self.data.window_days)
        return self.create_value("D188", round(rate, 2))

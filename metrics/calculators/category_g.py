"""Category G Calculator: Task Management Metrics (D143-D158)."""

from collections import defaultdict
from typing import Dict, List

from .base import BaseCalculator
from .helpers import mean, safe_divide
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryGCalculator(BaseCalculator):
    """Calculator for Category G: Task Management metrics."""

    category = "G"

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _get_todo_stats(self) -> Dict[str, int]:
        """Get aggregated todo statistics."""
        stats = {
            "total": 0,
            "completed": 0,
            "in_progress": 0,
            "pending": 0,
            "high_priority": 0,
        }

        for session in self.data.sessions:
            for todo in getattr(session, "todos", []):
                stats["total"] += 1
                status = getattr(todo, "status", "pending")
                if status == "completed":
                    stats["completed"] += 1
                elif status == "in_progress":
                    stats["in_progress"] += 1
                else:
                    stats["pending"] += 1

                priority = getattr(todo, "priority", "normal")
                if priority == "high":
                    stats["high_priority"] += 1

        return stats

    def _get_session_todo_counts(self) -> List[int]:
        """Get todo count per session."""
        counts = []
        for session in self.data.sessions:
            todos = getattr(session, "todos", [])
            if todos:
                counts.append(len(todos))
        return counts

    # D143-D151: Todo Completion

    def _calc_d143(self, definition: MetricDefinition) -> MetricValue:
        """D143: Total todos created."""
        stats = self._get_todo_stats()
        return self.create_value("D143", stats["total"])

    def _calc_d144(self, definition: MetricDefinition) -> MetricValue:
        """D144: Completed todos."""
        stats = self._get_todo_stats()
        return self.create_value("D144", stats["completed"])

    def _calc_d145(self, definition: MetricDefinition) -> MetricValue:
        """D145: Overall completion rate."""
        total = self.get_dependency_safe("D143", 0)
        completed = self.get_dependency_safe("D144", 0)
        ratio = safe_divide(completed, total)
        return self.create_value("D145", round(ratio, 4))

    def _calc_d146(self, definition: MetricDefinition) -> MetricValue:
        """D146: In-progress (abandoned) todos."""
        stats = self._get_todo_stats()
        return self.create_value("D146", stats["in_progress"])

    def _calc_d147(self, definition: MetricDefinition) -> MetricValue:
        """D147: Pending (never started) todos."""
        stats = self._get_todo_stats()
        return self.create_value("D147", stats["pending"])

    def _calc_d148(self, definition: MetricDefinition) -> MetricValue:
        """D148: Abandonment rate."""
        completed = self.get_dependency_safe("D144", 0)
        in_progress = self.get_dependency_safe("D146", 0)
        denominator = completed + in_progress
        ratio = safe_divide(in_progress, denominator)
        return self.create_value("D148", round(ratio, 4))

    def _calc_d149(self, definition: MetricDefinition) -> MetricValue:
        """D149: Average tasks per session."""
        counts = self._get_session_todo_counts()
        avg = mean(counts) if counts else 0
        return self.create_value("D149", round(avg, 2))

    def _calc_d150(self, definition: MetricDefinition) -> MetricValue:
        """D150: Max tasks in session."""
        counts = self._get_session_todo_counts()
        max_count = max(counts) if counts else 0
        return self.create_value("D150", max_count)

    def _calc_d151(self, definition: MetricDefinition) -> MetricValue:
        """D151: High priority ratio."""
        stats = self._get_todo_stats()
        ratio = safe_divide(stats["high_priority"], stats["total"])
        return self.create_value("D151", round(ratio, 4))

    # D152-D158: Planning Metrics

    def _calc_d152(self, definition: MetricDefinition) -> MetricValue:
        """D152: Plans created."""
        # Count EnterPlanMode tool calls
        plan_calls = sum(
            1 for tc in self.data.tool_calls
            if tc.tool_name == "EnterPlanMode"
        )
        return self.create_value("D152", plan_calls)

    def _calc_d153(self, definition: MetricDefinition) -> MetricValue:
        """D153: Average plan size."""
        # Get plan file sizes if available
        plan_sizes = []
        for tc in self.data.tool_calls:
            if tc.tool_name == "Write" and tc.file_path:
                if "plan" in tc.file_path.lower() or tc.file_path.endswith("_plan.md"):
                    size = getattr(tc, "content_size", 0)
                    if size > 0:
                        plan_sizes.append(size)
        avg = mean(plan_sizes) if plan_sizes else 0
        return self.create_value("D153", round(avg, 2))

    def _calc_d154(self, definition: MetricDefinition) -> MetricValue:
        """D154: Plan complexity score."""
        # Simplified: based on plan writes and message count in planning sessions
        plan_sessions = 0
        total_complexity = 0

        for session in self.data.sessions:
            # Check if session involved planning
            session_tools = [
                tc for tc in self.data.tool_calls
                if tc.session_id == session.session_id
            ]
            has_plan = any(
                tc.tool_name == "EnterPlanMode" for tc in session_tools
            )
            if has_plan:
                plan_sessions += 1
                # Complexity = message count * tool diversity
                tool_types = set(tc.tool_name for tc in session_tools)
                complexity = session.message_count * len(tool_types) / 10
                total_complexity += complexity

        avg_complexity = safe_divide(total_complexity, plan_sessions)
        return self.create_value("D154", round(avg_complexity, 2))

    def _calc_d155(self, definition: MetricDefinition) -> MetricValue:
        """D155: Technologies per plan."""
        # Count unique technology keywords in planning sessions
        tech_keywords = {
            "python", "javascript", "typescript", "react", "vue", "angular",
            "node", "django", "flask", "fastapi", "express", "sql", "postgres",
            "mongodb", "redis", "docker", "kubernetes", "aws", "azure", "gcp",
        }

        tech_per_session = []
        for session in self.data.sessions:
            session_tools = [
                tc for tc in self.data.tool_calls
                if tc.session_id == session.session_id and tc.tool_name == "EnterPlanMode"
            ]
            if session_tools:
                # Count tech mentions in session messages
                session_msgs = [
                    m.content.lower() for m in self.data.messages
                    if m.session_id == session.session_id and m.content
                ]
                techs_found = set()
                for msg in session_msgs:
                    for tech in tech_keywords:
                        if tech in msg:
                            techs_found.add(tech)
                if techs_found:
                    tech_per_session.append(len(techs_found))

        avg = mean(tech_per_session) if tech_per_session else 0
        return self.create_value("D155", round(avg, 2))

    def _calc_d156(self, definition: MetricDefinition) -> MetricValue:
        """D156: Action words per plan."""
        action_words = {
            "implement", "create", "add", "build", "update", "fix", "refactor",
            "test", "deploy", "configure", "setup", "install", "migrate",
        }

        action_counts = []
        for session in self.data.sessions:
            session_tools = [
                tc for tc in self.data.tool_calls
                if tc.session_id == session.session_id and tc.tool_name == "EnterPlanMode"
            ]
            if session_tools:
                session_msgs = [
                    m.content.lower() for m in self.data.messages
                    if m.session_id == session.session_id and m.content
                ]
                action_count = 0
                for msg in session_msgs:
                    for action in action_words:
                        action_count += msg.count(action)
                action_counts.append(action_count)

        avg = mean(action_counts) if action_counts else 0
        return self.create_value("D156", round(avg, 2))

    def _calc_d157(self, definition: MetricDefinition) -> MetricValue:
        """D157: Plan approval rate."""
        enter_count = sum(
            1 for tc in self.data.tool_calls
            if tc.tool_name == "EnterPlanMode"
        )
        exit_count = sum(
            1 for tc in self.data.tool_calls
            if tc.tool_name == "ExitPlanMode"
        )
        ratio = safe_divide(exit_count, enter_count)
        return self.create_value("D157", round(ratio, 4))

    def _calc_d158(self, definition: MetricDefinition) -> MetricValue:
        """D158: Planning to execution ratio."""
        plans = self.get_dependency_safe("D152", 0)
        # Count successful implementations (sessions with commits or multiple edits)
        implementations = sum(
            1 for session in self.data.sessions
            if len([
                tc for tc in self.data.tool_calls
                if tc.session_id == session.session_id and tc.tool_name in ("Edit", "Write")
            ]) >= 3
        )
        ratio = safe_divide(plans, implementations) if implementations else 0
        return self.create_value("D158", round(ratio, 4))

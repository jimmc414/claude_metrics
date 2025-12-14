"""Category H Calculator: Agent & Delegation Metrics (D159-D172)."""

from collections import defaultdict
from typing import Dict, List

from .base import BaseCalculator
from .helpers import mean, safe_divide
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryHCalculator(BaseCalculator):
    """Calculator for Category H: Agent & Delegation metrics."""

    category = "H"

    # Built-in agent types
    BUILTIN_AGENTS = {
        "Explore", "Plan", "general-purpose", "claude-code-guide",
        "statusline-setup",
    }

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _get_task_calls(self) -> List:
        """Get all Task tool calls."""
        return [tc for tc in self.data.tool_calls if tc.tool_name == "Task"]

    def _get_subagent_distribution(self) -> Dict[str, int]:
        """Get distribution of subagent types."""
        distribution: Dict[str, int] = defaultdict(int)
        for tc in self._get_task_calls():
            agent_type = getattr(tc, "subagent_type", "unknown")
            distribution[agent_type or "unknown"] += 1
        return dict(distribution)

    # D159-D166: Subagent Usage

    def _calc_d159(self, definition: MetricDefinition) -> MetricValue:
        """D159: Agent sessions."""
        task_calls = self._get_task_calls()
        return self.create_value("D159", len(task_calls))

    def _calc_d160(self, definition: MetricDefinition) -> MetricValue:
        """D160: Main vs agent ratio."""
        agent_count = self.get_dependency_safe("D159", 0)
        main_sessions = len(self.data.sessions)
        ratio = safe_divide(main_sessions, agent_count) if agent_count else float("inf")
        return self.create_value("D160", round(ratio, 2) if ratio != float("inf") else 0)

    def _calc_d161(self, definition: MetricDefinition) -> MetricValue:
        """D161: Agent usage percentage."""
        if not self.data.sessions:
            return self.create_value("D161", 0.0)

        # Sessions that used agents
        sessions_with_agents = set()
        for tc in self._get_task_calls():
            sessions_with_agents.add(tc.session_id)

        percentage = safe_divide(len(sessions_with_agents), len(self.data.sessions)) * 100
        return self.create_value("D161", round(percentage, 2))

    def _calc_d162(self, definition: MetricDefinition) -> MetricValue:
        """D162: Subagent type distribution."""
        distribution = self._get_subagent_distribution()
        return self.create_value("D162", distribution, breakdown=distribution)

    def _calc_d163(self, definition: MetricDefinition) -> MetricValue:
        """D163: Most used subagent."""
        distribution = self.get_dependency_safe("D162", {})
        if not distribution:
            return self.create_value("D163", "none")
        most_used = max(distribution.items(), key=lambda x: x[1])[0]
        return self.create_value("D163", most_used)

    def _calc_d164(self, definition: MetricDefinition) -> MetricValue:
        """D164: Explore agent usage."""
        count = sum(
            1 for tc in self._get_task_calls()
            if getattr(tc, "subagent_type", "") == "Explore"
        )
        return self.create_value("D164", count)

    def _calc_d165(self, definition: MetricDefinition) -> MetricValue:
        """D165: Plan agent usage."""
        count = sum(
            1 for tc in self._get_task_calls()
            if getattr(tc, "subagent_type", "") == "Plan"
        )
        return self.create_value("D165", count)

    def _calc_d166(self, definition: MetricDefinition) -> MetricValue:
        """D166: Custom agent usage."""
        count = sum(
            1 for tc in self._get_task_calls()
            if getattr(tc, "subagent_type", "") not in self.BUILTIN_AGENTS
        )
        return self.create_value("D166", count)

    # D167-D172: Agent Efficiency

    def _calc_d167(self, definition: MetricDefinition) -> MetricValue:
        """D167: Tokens per agent task."""
        task_calls = self._get_task_calls()
        if not task_calls:
            return self.create_value("D167", 0.0)

        total_tokens = sum(
            getattr(tc, "total_tokens", 0) for tc in task_calls
        )
        avg = safe_divide(total_tokens, len(task_calls))
        return self.create_value("D167", round(avg, 2))

    def _calc_d168(self, definition: MetricDefinition) -> MetricValue:
        """D168: Tools per agent task."""
        task_calls = self._get_task_calls()
        if not task_calls:
            return self.create_value("D168", 0.0)

        total_tools = sum(
            getattr(tc, "tool_use_count", 0) for tc in task_calls
        )
        avg = safe_divide(total_tools, len(task_calls))
        return self.create_value("D168", round(avg, 2))

    def _calc_d169(self, definition: MetricDefinition) -> MetricValue:
        """D169: Agent success rate."""
        task_calls = self._get_task_calls()
        if not task_calls:
            return self.create_value("D169", 0.0)

        successful = sum(1 for tc in task_calls if tc.success)
        ratio = safe_divide(successful, len(task_calls))
        return self.create_value("D169", round(ratio, 4))

    def _calc_d170(self, definition: MetricDefinition) -> MetricValue:
        """D170: Agent resume rate."""
        task_calls = self._get_task_calls()
        if not task_calls:
            return self.create_value("D170", 0.0)

        resumed = sum(
            1 for tc in task_calls
            if getattr(tc, "resume", None) is not None
        )
        ratio = safe_divide(resumed, len(task_calls))
        return self.create_value("D170", round(ratio, 4))

    def _calc_d171(self, definition: MetricDefinition) -> MetricValue:
        """D171: Parallel agent frequency."""
        # Count messages with multiple Task calls
        # Group task calls by message/turn
        message_task_counts: Dict[str, int] = defaultdict(int)
        for tc in self._get_task_calls():
            msg_id = getattr(tc, "message_id", tc.session_id)
            message_task_counts[msg_id] += 1

        parallel_count = sum(1 for count in message_task_counts.values() if count > 1)
        return self.create_value("D171", parallel_count)

    def _calc_d172(self, definition: MetricDefinition) -> MetricValue:
        """D172: Agent depth (max nesting)."""
        # Look for nested agent spawns
        max_depth = 0
        for tc in self._get_task_calls():
            depth = getattr(tc, "nesting_depth", 1)
            max_depth = max(max_depth, depth)
        return self.create_value("D172", max_depth)

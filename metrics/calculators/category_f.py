"""Category F Calculator: Thinking & Complexity Metrics (D137-D142)."""

from typing import List, Tuple

from .base import BaseCalculator
from .helpers import mean, safe_divide, linear_regression_slope
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryFCalculator(BaseCalculator):
    """Calculator for Category F: Thinking & Complexity metrics."""

    category = "F"

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _calc_d137(self, definition: MetricDefinition) -> MetricValue:
        """D137: Thinking length trend."""
        if len(self.data.sessions) < 2:
            return self.create_value("D137", 0.0)

        # Calculate average thinking length per session
        session_thinking: List[Tuple[float, float]] = []
        for i, session in enumerate(self.data.sessions):
            thinking_lengths = [
                m.thinking_length for m in self.data.messages
                if m.session_id == session.session_id and m.has_thinking
            ]
            avg_thinking = mean(thinking_lengths) if thinking_lengths else 0
            session_thinking.append((float(i), avg_thinking))

        slope = linear_regression_slope(session_thinking)
        return self.create_value("D137", round(slope, 4))

    def _calc_d138(self, definition: MetricDefinition) -> MetricValue:
        """D138: Sidechain exploration rate."""
        thinking_msgs = [m for m in self.data.messages if m.has_thinking]
        if not thinking_msgs:
            return self.create_value("D138", 0.0)

        sidechain_count = sum(
            1 for m in thinking_msgs
            if getattr(m, "is_sidechain", False)
        )
        ratio = safe_divide(sidechain_count, len(thinking_msgs))
        return self.create_value("D138", round(ratio, 4))

    def _calc_d139(self, definition: MetricDefinition) -> MetricValue:
        """D139: Conversation compaction rate."""
        if not self.data.sessions:
            return self.create_value("D139", 0.0)

        # Count sessions with compaction events
        sessions_with_compaction = sum(
            1 for s in self.data.sessions
            if any(
                getattr(m, "has_compaction", False) for m in self.data.messages
                if m.session_id == s.session_id
            )
        )
        ratio = safe_divide(sessions_with_compaction, len(self.data.sessions))
        return self.create_value("D139", round(ratio, 4))

    def _calc_d140(self, definition: MetricDefinition) -> MetricValue:
        """D140: Context clearing frequency."""
        if not self.data.sessions:
            return self.create_value("D140", 0.0)

        # Count context management events
        context_events = sum(
            1 for m in self.data.messages
            if getattr(m, "has_compaction", False) or getattr(m, "context_cleared", False)
        )
        rate = safe_divide(context_events, len(self.data.sessions))
        return self.create_value("D140", round(rate, 2))

    def _calc_d141(self, definition: MetricDefinition) -> MetricValue:
        """D141: Tokens cleared per compaction."""
        # Get all compaction events with cleared token counts
        cleared_tokens = [
            getattr(m, "cleared_input_tokens", 0) for m in self.data.messages
            if getattr(m, "has_compaction", False) and getattr(m, "cleared_input_tokens", 0) > 0
        ]
        avg = mean(cleared_tokens) if cleared_tokens else 0
        return self.create_value("D141", round(avg, 2))

    def _calc_d142(self, definition: MetricDefinition) -> MetricValue:
        """D142: Multi-turn problem rate (sessions with >20 messages)."""
        if not self.data.sessions:
            return self.create_value("D142", 0.0)

        multi_turn = sum(1 for s in self.data.sessions if s.message_count > 20)
        ratio = safe_divide(multi_turn, len(self.data.sessions))
        return self.create_value("D142", round(ratio, 4))

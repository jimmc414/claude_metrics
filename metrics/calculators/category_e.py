"""Category E Calculator: Conversation Analysis Metrics (D110-D136)."""

import re
from collections import defaultdict
from typing import Dict, List, Set

from .base import BaseCalculator
from .helpers import mean, median, safe_divide, linear_regression_slope
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryECalculator(BaseCalculator):
    """Calculator for Category E: Conversation Analysis metrics."""

    category = "E"

    # Keyword patterns for topic detection
    BUG_KEYWORDS = {"bug", "error", "fix", "broken", "crash", "fail", "issue"}
    FEATURE_KEYWORDS = {"add", "create", "implement", "build", "new", "feature"}
    REFACTOR_KEYWORDS = {"refactor", "clean", "improve", "optimize", "reorganize"}
    TEST_KEYWORDS = {"test", "pytest", "unittest", "coverage", "spec", "assert"}
    DOCS_KEYWORDS = {"document", "readme", "comment", "docstring", "docs"}
    DEBUG_KEYWORDS = {"debug", "why", "trace", "investigate", "inspect", "print"}
    REVIEW_KEYWORDS = {"review", "check", "examine", "look at", "analyze"}

    FRUSTRATION_PATTERNS = [
        r"\bwrong\b", r"\bstill not\b", r"\bdoesn't work\b", r"\bnot working\b",
        r"\bfailed\b", r"\bbroken\b", r"\bwhy (isn't|won't|doesn't)\b",
    ]
    GRATITUDE_PATTERNS = [
        r"\bthanks\b", r"\bthank you\b", r"\bperfect\b", r"\bgreat\b",
        r"\bawesome\b", r"\bexcellent\b", r"\bworks\b", r"\bnice\b",
    ]
    COMMAND_PATTERNS = [
        r"^(do|make|create|fix|add|remove|update|change|implement|write|run|build)\s",
    ]

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _get_user_messages(self) -> List[str]:
        """Get all user message contents."""
        return [
            m.content for m in self.data.messages
            if m.role == "user" and m.content
        ]

    def _count_pattern_matches(self, texts: List[str], patterns: List[str]) -> int:
        """Count messages matching any of the patterns."""
        count = 0
        compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
        for text in texts:
            if any(p.search(text) for p in compiled):
                count += 1
        return count

    def _count_keyword_matches(self, texts: List[str], keywords: Set[str]) -> int:
        """Count messages containing any of the keywords."""
        count = 0
        for text in texts:
            text_lower = text.lower()
            if any(kw in text_lower for kw in keywords):
                count += 1
        return count

    # D110-D118: Message Patterns

    def _calc_d110(self, definition: MetricDefinition) -> MetricValue:
        """D110: Conversation depth - max messages per session."""
        if not self.data.sessions:
            return self.create_value("D110", 0)
        max_depth = max(s.message_count for s in self.data.sessions)
        return self.create_value("D110", max_depth)

    def _calc_d111(self, definition: MetricDefinition) -> MetricValue:
        """D111: Questions asked by user."""
        user_msgs = self._get_user_messages()
        questions = sum(1 for m in user_msgs if "?" in m)
        return self.create_value("D111", questions)

    def _calc_d112(self, definition: MetricDefinition) -> MetricValue:
        """D112: Question ratio."""
        user_msgs = self._get_user_messages()
        questions = self.get_dependency_safe("D111", 0)
        ratio = safe_divide(questions, len(user_msgs))
        return self.create_value("D112", round(ratio, 4))

    def _calc_d113(self, definition: MetricDefinition) -> MetricValue:
        """D113: Commands given - imperative messages."""
        user_msgs = self._get_user_messages()
        commands = self._count_pattern_matches(user_msgs, self.COMMAND_PATTERNS)
        return self.create_value("D113", commands)

    def _calc_d114(self, definition: MetricDefinition) -> MetricValue:
        """D114: Code pastes by user."""
        user_msgs = self._get_user_messages()
        code_pastes = sum(
            1 for m in user_msgs
            if "```" in m or len(m) > 500
        )
        return self.create_value("D114", code_pastes)

    def _calc_d115(self, definition: MetricDefinition) -> MetricValue:
        """D115: Error reports by user."""
        user_msgs = self._get_user_messages()
        error_keywords = {"error", "traceback", "exception", "failed", "stack trace"}
        errors = self._count_keyword_matches(user_msgs, error_keywords)
        return self.create_value("D115", errors)

    def _calc_d116(self, definition: MetricDefinition) -> MetricValue:
        """D116: Frustration indicators."""
        user_msgs = self._get_user_messages()
        frustrations = self._count_pattern_matches(user_msgs, self.FRUSTRATION_PATTERNS)
        return self.create_value("D116", frustrations)

    def _calc_d117(self, definition: MetricDefinition) -> MetricValue:
        """D117: Gratitude expressions."""
        user_msgs = self._get_user_messages()
        gratitude = self._count_pattern_matches(user_msgs, self.GRATITUDE_PATTERNS)
        return self.create_value("D117", gratitude)

    def _calc_d118(self, definition: MetricDefinition) -> MetricValue:
        """D118: Frustration/gratitude ratio."""
        frustration = self.get_dependency_safe("D116", 0)
        gratitude = self.get_dependency_safe("D117", 1)  # Avoid div by zero
        ratio = safe_divide(frustration, gratitude)
        return self.create_value("D118", round(ratio, 4))

    # D119-D127: Topic Analysis

    def _calc_d119(self, definition: MetricDefinition) -> MetricValue:
        """D119: Bug-related messages."""
        user_msgs = self._get_user_messages()
        count = self._count_keyword_matches(user_msgs, self.BUG_KEYWORDS)
        return self.create_value("D119", count)

    def _calc_d120(self, definition: MetricDefinition) -> MetricValue:
        """D120: Feature-related messages."""
        user_msgs = self._get_user_messages()
        count = self._count_keyword_matches(user_msgs, self.FEATURE_KEYWORDS)
        return self.create_value("D120", count)

    def _calc_d121(self, definition: MetricDefinition) -> MetricValue:
        """D121: Refactor-related messages."""
        user_msgs = self._get_user_messages()
        count = self._count_keyword_matches(user_msgs, self.REFACTOR_KEYWORDS)
        return self.create_value("D121", count)

    def _calc_d122(self, definition: MetricDefinition) -> MetricValue:
        """D122: Test-related messages."""
        user_msgs = self._get_user_messages()
        count = self._count_keyword_matches(user_msgs, self.TEST_KEYWORDS)
        return self.create_value("D122", count)

    def _calc_d123(self, definition: MetricDefinition) -> MetricValue:
        """D123: Docs-related messages."""
        user_msgs = self._get_user_messages()
        count = self._count_keyword_matches(user_msgs, self.DOCS_KEYWORDS)
        return self.create_value("D123", count)

    def _calc_d124(self, definition: MetricDefinition) -> MetricValue:
        """D124: Debug-related messages."""
        user_msgs = self._get_user_messages()
        count = self._count_keyword_matches(user_msgs, self.DEBUG_KEYWORDS)
        return self.create_value("D124", count)

    def _calc_d125(self, definition: MetricDefinition) -> MetricValue:
        """D125: Review-related messages."""
        user_msgs = self._get_user_messages()
        count = self._count_keyword_matches(user_msgs, self.REVIEW_KEYWORDS)
        return self.create_value("D125", count)

    def _calc_d126(self, definition: MetricDefinition) -> MetricValue:
        """D126: Topic distribution."""
        distribution = {
            "bug": self.get_dependency_safe("D119", 0),
            "feature": self.get_dependency_safe("D120", 0),
            "refactor": self.get_dependency_safe("D121", 0),
            "test": self.get_dependency_safe("D122", 0),
            "docs": self.get_dependency_safe("D123", 0),
            "debug": self.get_dependency_safe("D124", 0),
            "review": self.get_dependency_safe("D125", 0),
        }
        return self.create_value("D126", distribution, breakdown=distribution)

    def _calc_d127(self, definition: MetricDefinition) -> MetricValue:
        """D127: Topic trend over time - slope of dominant topic."""
        # Simplified: calculate slope of bug-related messages over sessions
        if len(self.data.sessions) < 2:
            return self.create_value("D127", 0.0)

        # Count bug keywords per session (as representative topic)
        session_counts = []
        for i, session in enumerate(self.data.sessions):
            msg_count = sum(
                1 for m in self.data.messages
                if m.session_id == session.session_id
                and m.role == "user"
                and m.content
                and any(kw in m.content.lower() for kw in self.BUG_KEYWORDS)
            )
            session_counts.append((float(i), float(msg_count)))

        slope = linear_regression_slope(session_counts)
        return self.create_value("D127", round(slope, 4))

    # D128-D136: Extended Thinking Analysis

    def _calc_d128(self, definition: MetricDefinition) -> MetricValue:
        """D128: Sessions with thinking."""
        if not self.data.sessions:
            return self.create_value("D128", 0.0)

        sessions_with_thinking = sum(
            1 for s in self.data.sessions
            if any(
                m.has_thinking for m in self.data.messages
                if m.session_id == s.session_id
            )
        )
        ratio = safe_divide(sessions_with_thinking, len(self.data.sessions))
        return self.create_value("D128", round(ratio, 4))

    def _calc_d129(self, definition: MetricDefinition) -> MetricValue:
        """D129: Thinking blocks per session."""
        if not self.data.sessions:
            return self.create_value("D129", 0.0)

        thinking_blocks = sum(1 for m in self.data.messages if m.has_thinking)
        avg = safe_divide(thinking_blocks, len(self.data.sessions))
        return self.create_value("D129", round(avg, 2))

    def _calc_d130(self, definition: MetricDefinition) -> MetricValue:
        """D130: Average thinking length."""
        thinking_lengths = [
            m.thinking_length for m in self.data.messages
            if m.has_thinking and m.thinking_length > 0
        ]
        avg = mean(thinking_lengths) if thinking_lengths else 0
        return self.create_value("D130", round(avg, 2))

    def _calc_d131(self, definition: MetricDefinition) -> MetricValue:
        """D131: Median thinking length."""
        thinking_lengths = [
            m.thinking_length for m in self.data.messages
            if m.has_thinking and m.thinking_length > 0
        ]
        med = median(thinking_lengths) if thinking_lengths else 0
        return self.create_value("D131", round(med, 2))

    def _calc_d132(self, definition: MetricDefinition) -> MetricValue:
        """D132: Max thinking length."""
        thinking_lengths = [
            m.thinking_length for m in self.data.messages
            if m.has_thinking
        ]
        max_len = max(thinking_lengths) if thinking_lengths else 0
        return self.create_value("D132", max_len)

    def _calc_d133(self, definition: MetricDefinition) -> MetricValue:
        """D133: Thinking token percentage."""
        total_output = sum(m.output_tokens for m in self.data.messages)
        thinking_tokens = sum(
            m.thinking_length // 4  # Rough estimate: ~4 chars per token
            for m in self.data.messages
            if m.has_thinking
        )
        ratio = safe_divide(thinking_tokens, total_output)
        return self.create_value("D133", round(ratio, 4))

    def _calc_d134(self, definition: MetricDefinition) -> MetricValue:
        """D134: ULTRATHINK trigger count."""
        # Check for ULTRATHINK in user messages
        user_msgs = self._get_user_messages()
        count = sum(1 for m in user_msgs if "ULTRATHINK" in m.upper())
        return self.create_value("D134", count)

    def _calc_d135(self, definition: MetricDefinition) -> MetricValue:
        """D135: Thinking level distribution."""
        # Group by thinking level (if available)
        levels: Dict[str, int] = defaultdict(int)
        for m in self.data.messages:
            if m.has_thinking:
                level = getattr(m, "thinking_level", "standard")
                levels[level or "standard"] += 1
        distribution = dict(levels) if levels else {"none": 0}
        return self.create_value("D135", distribution, breakdown=distribution)

    def _calc_d136(self, definition: MetricDefinition) -> MetricValue:
        """D136: Thinking disabled rate."""
        total = len([m for m in self.data.messages if m.role == "assistant"])
        disabled = sum(
            1 for m in self.data.messages
            if m.role == "assistant" and getattr(m, "thinking_disabled", False)
        )
        ratio = safe_divide(disabled, total)
        return self.create_value("D136", round(ratio, 4))

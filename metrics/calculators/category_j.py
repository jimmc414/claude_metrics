"""Category J Calculator: Error & Recovery Metrics (D189-D203)."""

from collections import defaultdict
from typing import Dict, List

from .base import BaseCalculator
from .helpers import mean, safe_divide
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryJCalculator(BaseCalculator):
    """Calculator for Category J: Error & Recovery metrics."""

    category = "J"

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _get_error_counts(self) -> Dict[str, Dict[str, int]]:
        """Get error counts by tool type."""
        counts: Dict[str, Dict[str, int]] = defaultdict(lambda: {"total": 0, "errors": 0})
        for tc in self.data.tool_calls:
            counts[tc.tool_name]["total"] += 1
            if not tc.success:
                counts[tc.tool_name]["errors"] += 1
        return dict(counts)

    def _get_errors_by_session(self) -> Dict[str, int]:
        """Get error count per session."""
        errors: Dict[str, int] = defaultdict(int)
        for tc in self.data.tool_calls:
            if not tc.success:
                errors[tc.session_id] += 1
        return dict(errors)

    # D189-D194: Error Rates

    def _calc_d189(self, definition: MetricDefinition) -> MetricValue:
        """D189: Overall error rate."""
        total = len(self.data.tool_calls)
        errors = sum(1 for tc in self.data.tool_calls if not tc.success)
        ratio = safe_divide(errors, total)
        return self.create_value("D189", round(ratio, 4))

    def _calc_d190(self, definition: MetricDefinition) -> MetricValue:
        """D190: Bash error rate."""
        counts = self._get_error_counts()
        bash = counts.get("Bash", {"total": 0, "errors": 0})
        ratio = safe_divide(bash["errors"], bash["total"])
        return self.create_value("D190", round(ratio, 4))

    def _calc_d191(self, definition: MetricDefinition) -> MetricValue:
        """D191: Edit conflict rate."""
        counts = self._get_error_counts()
        edit = counts.get("Edit", {"total": 0, "errors": 0})
        ratio = safe_divide(edit["errors"], edit["total"])
        return self.create_value("D191", round(ratio, 4))

    def _calc_d192(self, definition: MetricDefinition) -> MetricValue:
        """D192: Read failure rate."""
        counts = self._get_error_counts()
        read = counts.get("Read", {"total": 0, "errors": 0})
        ratio = safe_divide(read["errors"], read["total"])
        return self.create_value("D192", round(ratio, 4))

    def _calc_d193(self, definition: MetricDefinition) -> MetricValue:
        """D193: Permission error rate."""
        total = len(self.data.tool_calls)
        # Look for permission-related error indicators
        permission_errors = sum(
            1 for tc in self.data.tool_calls
            if not tc.success and getattr(tc, "error_type", "") in
            ("permission_denied", "access_denied", "EACCES", "EPERM")
        )
        ratio = safe_divide(permission_errors, total)
        return self.create_value("D193", round(ratio, 4))

    def _calc_d194(self, definition: MetricDefinition) -> MetricValue:
        """D194: API error rate."""
        total = len(self.data.messages)
        api_errors = sum(
            1 for m in self.data.messages
            if getattr(m, "is_api_error", False)
        )
        ratio = safe_divide(api_errors, total)
        return self.create_value("D194", round(ratio, 4))

    # D195-D199: Recovery Patterns

    def _calc_d195(self, definition: MetricDefinition) -> MetricValue:
        """D195: Error recovery rate."""
        # Group tool calls by session and check for recovery patterns
        sorted_calls = sorted(
            self.data.tool_calls,
            key=lambda tc: tc.timestamp if tc.timestamp else self._now
        )

        errors = 0
        recoveries = 0
        prev_failed = False

        for tc in sorted_calls:
            if not tc.success:
                errors += 1
                prev_failed = True
            elif prev_failed:
                # Success after failure = recovery
                recoveries += 1
                prev_failed = False

        ratio = safe_divide(recoveries, errors)
        return self.create_value("D195", round(ratio, 4))

    def _calc_d196(self, definition: MetricDefinition) -> MetricValue:
        """D196: Retry success rate."""
        # Look for consecutive calls to the same tool (potential retries)
        sorted_calls = sorted(
            self.data.tool_calls,
            key=lambda tc: tc.timestamp if tc.timestamp else self._now
        )

        retries = 0
        successful_retries = 0

        for i in range(1, len(sorted_calls)):
            prev = sorted_calls[i - 1]
            curr = sorted_calls[i]

            # Check if this looks like a retry
            if (prev.tool_name == curr.tool_name and
                prev.file_path == curr.file_path and
                not prev.success):
                retries += 1
                if curr.success:
                    successful_retries += 1

        ratio = safe_divide(successful_retries, retries)
        return self.create_value("D196", round(ratio, 4))

    def _calc_d197(self, definition: MetricDefinition) -> MetricValue:
        """D197: Errors per session."""
        if not self.data.sessions:
            return self.create_value("D197", 0.0)

        total_errors = sum(1 for tc in self.data.tool_calls if not tc.success)
        avg = safe_divide(total_errors, len(self.data.sessions))
        return self.create_value("D197", round(avg, 2))

    def _calc_d198(self, definition: MetricDefinition) -> MetricValue:
        """D198: Error clustering (sessions with multiple errors)."""
        errors_by_session = self._get_errors_by_session()
        clustered = sum(1 for count in errors_by_session.values() if count >= 3)
        return self.create_value("D198", clustered)

    def _calc_d199(self, definition: MetricDefinition) -> MetricValue:
        """D199: Time to recovery (seconds)."""
        sorted_calls = sorted(
            self.data.tool_calls,
            key=lambda tc: tc.timestamp if tc.timestamp else self._now
        )

        recovery_times = []
        error_time = None

        for tc in sorted_calls:
            if not tc.success and tc.timestamp:
                error_time = tc.timestamp
            elif tc.success and error_time and tc.timestamp:
                recovery_time = (tc.timestamp - error_time).total_seconds()
                if recovery_time > 0:
                    recovery_times.append(recovery_time)
                error_time = None

        avg = mean(recovery_times) if recovery_times else 0
        return self.create_value("D199", round(avg, 2))

    # D200-D203: Interruption Metrics

    def _calc_d200(self, definition: MetricDefinition) -> MetricValue:
        """D200: Interrupted operations."""
        count = sum(
            1 for tc in self.data.tool_calls
            if getattr(tc, "interrupted", False)
        )
        return self.create_value("D200", count)

    def _calc_d201(self, definition: MetricDefinition) -> MetricValue:
        """D201: Truncated outputs."""
        count = sum(
            1 for tc in self.data.tool_calls
            if getattr(tc, "truncated", False)
        )
        return self.create_value("D201", count)

    def _calc_d202(self, definition: MetricDefinition) -> MetricValue:
        """D202: Killed shells."""
        count = sum(
            1 for tc in self.data.tool_calls
            if tc.tool_name == "KillShell"
        )
        return self.create_value("D202", count)

    def _calc_d203(self, definition: MetricDefinition) -> MetricValue:
        """D203: Hook prevention rate."""
        # Count hook executions and preventions from sessions
        total_hooks = 0
        prevented = 0
        for session in self.data.sessions:
            hook_count = getattr(session, "hook_count", 0)
            total_hooks += hook_count
            prevented_count = getattr(session, "hook_prevented_count", 0)
            prevented += prevented_count

        ratio = safe_divide(prevented, total_hooks)
        return self.create_value("D203", round(ratio, 4))

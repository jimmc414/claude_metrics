"""Category B Calculator: Tool Usage Metrics (D029-D048)."""

from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple

from .base import BaseCalculator
from .helpers import (
    mean,
    safe_divide,
    shannon_entropy,
    linear_regression_slope,
)
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryBCalculator(BaseCalculator):
    """Calculator for Category B: Tool Usage metrics."""

    category = "B"

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    # D029-D035: Tool Distribution

    def _calc_d029(self, definition: MetricDefinition) -> MetricValue:
        """D029: Tool usage distribution."""
        total = sum(self.data.tool_counts.values())
        if total == 0:
            return self.create_value("D029", {})

        distribution = {
            tool: round(count / total, 4)
            for tool, count in self.data.tool_counts.items()
        }
        return self.create_value("D029", distribution, breakdown=self.data.tool_counts)

    def _calc_d030(self, definition: MetricDefinition) -> MetricValue:
        """D030: Most used tool."""
        if not self.data.tool_counts:
            return self.create_value("D030", "None")

        most_used = max(self.data.tool_counts.items(), key=lambda x: x[1])[0]
        return self.create_value("D030", most_used)

    def _calc_d031(self, definition: MetricDefinition) -> MetricValue:
        """D031: Tool diversity index (Shannon entropy)."""
        entropy = shannon_entropy(self.data.tool_counts)
        return self.create_value("D031", round(entropy, 4))

    def _calc_d032(self, definition: MetricDefinition) -> MetricValue:
        """D032: Tool calls per hour."""
        total_hours = self.get_dependency_safe("D003", 1)
        if total_hours == 0:
            total_hours = 1
        rate = safe_divide(self.data.total_tool_calls, total_hours)
        return self.create_value("D032", round(rate, 2))

    def _calc_d033(self, definition: MetricDefinition) -> MetricValue:
        """D033: Tool calls per session."""
        rate = safe_divide(self.data.total_tool_calls, len(self.data.sessions))
        return self.create_value("D033", round(rate, 2))

    def _calc_d034(self, definition: MetricDefinition) -> MetricValue:
        """D034: Tool calls per message."""
        # Count assistant messages
        assistant_msgs = sum(
            s.assistant_message_count for s in self.data.sessions
        )
        rate = safe_divide(self.data.total_tool_calls, assistant_msgs)
        return self.create_value("D034", round(rate, 2))

    def _calc_d035(self, definition: MetricDefinition) -> MetricValue:
        """D035: Bash to Edit ratio."""
        bash_count = self.data.tool_counts.get("Bash", 0)
        edit_count = self.data.tool_counts.get("Edit", 0)
        ratio = safe_divide(bash_count, edit_count, default=0.0)
        return self.create_value("D035", round(ratio, 2))

    # D036-D043: Tool Performance

    def _calc_d036(self, definition: MetricDefinition) -> MetricValue:
        """D036: Daily tool call trend."""
        # Group tool calls by date
        daily_counts: Dict[str, int] = defaultdict(int)
        for tc in self.data.tool_calls:
            date_str = tc.timestamp.strftime("%Y-%m-%d")
            daily_counts[date_str] += 1

        if len(daily_counts) < 2:
            return self.create_value("D036", 0.0)

        # Convert to (day_index, count) pairs
        sorted_dates = sorted(daily_counts.keys())
        points: List[Tuple[float, float]] = [
            (float(i), float(daily_counts[d]))
            for i, d in enumerate(sorted_dates)
        ]

        slope = linear_regression_slope(points)
        return self.create_value("D036", round(slope, 4), trend=slope)

    def _calc_d037(self, definition: MetricDefinition) -> MetricValue:
        """D037: Tool success rate."""
        if not self.data.tool_calls:
            return self.create_value("D037", 1.0)

        successful = sum(1 for tc in self.data.tool_calls if tc.success)
        rate = safe_divide(successful, len(self.data.tool_calls))
        return self.create_value("D037", round(rate, 4))

    def _calc_d038(self, definition: MetricDefinition) -> MetricValue:
        """D038: Bash error rate."""
        bash_calls = [tc for tc in self.data.tool_calls if tc.tool_name == "Bash"]
        if not bash_calls:
            return self.create_value("D038", 0.0)

        errors = sum(1 for tc in bash_calls if tc.is_error)
        rate = safe_divide(errors, len(bash_calls))
        return self.create_value("D038", round(rate, 4))

    def _calc_d039(self, definition: MetricDefinition) -> MetricValue:
        """D039: Edit success rate."""
        edit_calls = [tc for tc in self.data.tool_calls if tc.tool_name == "Edit"]
        if not edit_calls:
            return self.create_value("D039", 1.0)

        successful = sum(1 for tc in edit_calls if tc.success)
        rate = safe_divide(successful, len(edit_calls))
        return self.create_value("D039", round(rate, 4))

    def _calc_d040(self, definition: MetricDefinition) -> MetricValue:
        """D040: Average tool execution time."""
        durations = [
            tc.duration_ms
            for tc in self.data.tool_calls
            if tc.duration_ms is not None
        ]
        avg = mean(durations) if durations else 0
        return self.create_value("D040", round(avg, 2))

    def _calc_d041(self, definition: MetricDefinition) -> MetricValue:
        """D041: Tool timeout rate."""
        if not self.data.tool_calls:
            return self.create_value("D041", 0.0)

        # Estimate timeouts as calls with is_interrupted=True
        timeouts = sum(1 for tc in self.data.tool_calls if tc.is_interrupted)
        rate = safe_divide(timeouts, len(self.data.tool_calls))
        return self.create_value("D041", round(rate, 4))

    def _calc_d042(self, definition: MetricDefinition) -> MetricValue:
        """D042: Longest tool execution."""
        durations = [
            tc.duration_ms
            for tc in self.data.tool_calls
            if tc.duration_ms is not None
        ]
        max_duration = max(durations) if durations else 0
        return self.create_value("D042", max_duration)

    def _calc_d043(self, definition: MetricDefinition) -> MetricValue:
        """D043: Tool retry rate."""
        # Estimate retries by looking for duplicate tool+file combinations
        # This is a simplified estimate
        if not self.data.tool_calls:
            return self.create_value("D043", 0.0)

        # Count potential retries (same tool on same file in short window)
        tool_file_pairs: Dict[Tuple[str, str], int] = defaultdict(int)
        for tc in self.data.tool_calls:
            if tc.file_path:
                key = (tc.tool_name, tc.file_path)
                tool_file_pairs[key] += 1

        retries = sum(count - 1 for count in tool_file_pairs.values() if count > 1)
        rate = safe_divide(retries, len(self.data.tool_calls))
        return self.create_value("D043", round(rate, 4))

    # D044-D048: Tool Patterns

    def _calc_d044(self, definition: MetricDefinition) -> MetricValue:
        """D044: Read before Edit ratio."""
        # Find Edit calls and check if preceded by Read on same file
        edit_calls = [tc for tc in self.data.tool_calls if tc.tool_name == "Edit"]
        if not edit_calls:
            return self.create_value("D044", 0.0)

        # Build read history by file
        read_files = set(
            tc.file_path
            for tc in self.data.tool_calls
            if tc.tool_name == "Read" and tc.file_path
        )

        preceded_count = sum(
            1 for ec in edit_calls
            if ec.file_path and ec.file_path in read_files
        )
        ratio = safe_divide(preceded_count, len(edit_calls))
        return self.create_value("D044", round(ratio, 4))

    def _calc_d045(self, definition: MetricDefinition) -> MetricValue:
        """D045: Glob before Read ratio."""
        read_calls = [tc for tc in self.data.tool_calls if tc.tool_name == "Read"]
        glob_calls = [tc for tc in self.data.tool_calls if tc.tool_name == "Glob"]

        if not read_calls:
            return self.create_value("D045", 0.0)

        # Simple heuristic: if there are Glob calls, assume some Read followed
        glob_count = len(glob_calls)
        read_count = len(read_calls)

        # Estimate based on presence of Glob activity
        ratio = safe_divide(min(glob_count, read_count), read_count)
        return self.create_value("D045", round(ratio, 4))

    def _calc_d046(self, definition: MetricDefinition) -> MetricValue:
        """D046: Grep then Read pattern count."""
        grep_calls = [tc for tc in self.data.tool_calls if tc.tool_name == "Grep"]
        read_calls = [tc for tc in self.data.tool_calls if tc.tool_name == "Read"]

        # Simple count of potential Grep->Read sequences
        pattern_count = min(len(grep_calls), len(read_calls))
        return self.create_value("D046", pattern_count)

    def _calc_d047(self, definition: MetricDefinition) -> MetricValue:
        """D047: Tool sequence patterns (2-tool sequences)."""
        if len(self.data.tool_calls) < 2:
            return self.create_value("D047", {})

        # Sort by timestamp and count consecutive pairs
        sorted_calls = sorted(self.data.tool_calls, key=lambda x: x.timestamp)
        sequences: Dict[str, int] = defaultdict(int)

        for i in range(1, len(sorted_calls)):
            pair = f"{sorted_calls[i-1].tool_name}->{sorted_calls[i].tool_name}"
            sequences[pair] += 1

        # Get top 10 sequences
        top_sequences = dict(
            sorted(sequences.items(), key=lambda x: x[1], reverse=True)[:10]
        )
        return self.create_value("D047", top_sequences, breakdown=top_sequences)

    def _calc_d048(self, definition: MetricDefinition) -> MetricValue:
        """D048: Tool co-occurrence (tools used together in same session)."""
        session_tools: Dict[str, set] = defaultdict(set)

        for tc in self.data.tool_calls:
            session_tools[tc.session_id].add(tc.tool_name)

        # Count co-occurrences
        co_occurrence: Dict[str, int] = defaultdict(int)
        for tools in session_tools.values():
            tool_list = sorted(tools)
            for i, t1 in enumerate(tool_list):
                for t2 in tool_list[i + 1:]:
                    pair = f"{t1}+{t2}"
                    co_occurrence[pair] += 1

        # Get top 10 pairs
        top_pairs = dict(
            sorted(co_occurrence.items(), key=lambda x: x[1], reverse=True)[:10]
        )
        return self.create_value("D048", top_pairs, breakdown=top_pairs)

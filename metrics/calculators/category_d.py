"""Category D Calculator: Model & Token Metrics (D074-D109)."""

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

from .base import BaseCalculator
from .helpers import mean, safe_divide, linear_regression_slope
from metrics.definitions.base import MetricDefinition, MetricValue


class CategoryDCalculator(BaseCalculator):
    """Calculator for Category D: Model & Token metrics."""

    category = "D"

    # Model family patterns
    OPUS_PATTERNS = ["opus", "claude-opus"]
    SONNET_PATTERNS = ["sonnet", "claude-sonnet"]
    HAIKU_PATTERNS = ["haiku", "claude-haiku"]

    # Estimated pricing (USD per 1M tokens) for cache savings calculation
    INPUT_PRICE_FULL = 3.0  # Approximate average
    INPUT_PRICE_CACHED = 0.3  # 90% discount for cached

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        return self._route_to_method(definition)

    def _is_model_family(self, model: str, patterns: List[str]) -> bool:
        """Check if model belongs to a family."""
        if not model:
            return False
        model_lower = model.lower()
        return any(p in model_lower for p in patterns)

    # D074-D080: Model Usage Distribution

    def _calc_d074(self, definition: MetricDefinition) -> MetricValue:
        """D074: Model usage distribution."""
        if not self.data.model_usage:
            return self.create_value("D074", {})

        total_msgs = sum(m.message_count for m in self.data.model_usage.values())
        if total_msgs == 0:
            return self.create_value("D074", {})

        distribution = {
            model: round(data.message_count / total_msgs, 4)
            for model, data in self.data.model_usage.items()
        }

        breakdown = {
            model: data.message_count
            for model, data in self.data.model_usage.items()
        }
        return self.create_value("D074", distribution, breakdown=breakdown)

    def _calc_d075(self, definition: MetricDefinition) -> MetricValue:
        """D075: Opus usage ratio."""
        if not self.data.model_usage:
            return self.create_value("D075", 0.0)

        opus_msgs = sum(
            data.message_count
            for model, data in self.data.model_usage.items()
            if self._is_model_family(model, self.OPUS_PATTERNS)
        )
        total_msgs = sum(m.message_count for m in self.data.model_usage.values())
        ratio = safe_divide(opus_msgs, total_msgs)
        return self.create_value("D075", round(ratio, 4))

    def _calc_d076(self, definition: MetricDefinition) -> MetricValue:
        """D076: Sonnet usage ratio."""
        if not self.data.model_usage:
            return self.create_value("D076", 0.0)

        sonnet_msgs = sum(
            data.message_count
            for model, data in self.data.model_usage.items()
            if self._is_model_family(model, self.SONNET_PATTERNS)
        )
        total_msgs = sum(m.message_count for m in self.data.model_usage.values())
        ratio = safe_divide(sonnet_msgs, total_msgs)
        return self.create_value("D076", round(ratio, 4))

    def _calc_d077(self, definition: MetricDefinition) -> MetricValue:
        """D077: Haiku usage ratio."""
        if not self.data.model_usage:
            return self.create_value("D077", 0.0)

        haiku_msgs = sum(
            data.message_count
            for model, data in self.data.model_usage.items()
            if self._is_model_family(model, self.HAIKU_PATTERNS)
        )
        total_msgs = sum(m.message_count for m in self.data.model_usage.values())
        ratio = safe_divide(haiku_msgs, total_msgs)
        return self.create_value("D077", round(ratio, 4))

    def _calc_d078(self, definition: MetricDefinition) -> MetricValue:
        """D078: Model switching frequency."""
        if not self.data.sessions:
            return self.create_value("D078", 0.0)

        multi_model_sessions = sum(
            1 for s in self.data.sessions
            if len(s.models_used) > 1
        )
        rate = safe_divide(multi_model_sessions, len(self.data.sessions))
        return self.create_value("D078", round(rate, 4))

    def _calc_d079(self, definition: MetricDefinition) -> MetricValue:
        """D079: Primary model."""
        if not self.data.model_usage:
            return self.create_value("D079", "None")

        primary = max(
            self.data.model_usage.items(),
            key=lambda x: x[1].message_count
        )[0]
        return self.create_value("D079", primary)

    def _calc_d080(self, definition: MetricDefinition) -> MetricValue:
        """D080: Model usage by subagent (agent sessions only)."""
        agent_sessions = [s for s in self.data.sessions if s.is_agent]
        if not agent_sessions:
            return self.create_value("D080", {})

        model_counts: Dict[str, int] = defaultdict(int)
        for s in agent_sessions:
            for model in s.models_used:
                model_counts[model] += 1

        return self.create_value("D080", dict(model_counts), breakdown=dict(model_counts))

    # D081-D092: Token Metrics

    def _calc_d081(self, definition: MetricDefinition) -> MetricValue:
        """D081: Average tokens per message."""
        total_tokens = (
            self.data.total_tokens.get("input", 0) +
            self.data.total_tokens.get("output", 0)
        )
        avg = safe_divide(total_tokens, self.data.total_messages)
        return self.create_value("D081", round(avg, 2))

    def _calc_d082(self, definition: MetricDefinition) -> MetricValue:
        """D082: Average tokens per session."""
        total_tokens = (
            self.data.total_tokens.get("input", 0) +
            self.data.total_tokens.get("output", 0)
        )
        avg = safe_divide(total_tokens, len(self.data.sessions))
        return self.create_value("D082", round(avg, 2))

    def _calc_d083(self, definition: MetricDefinition) -> MetricValue:
        """D083: Input to output token ratio."""
        input_tokens = self.data.total_tokens.get("input", 0)
        output_tokens = self.data.total_tokens.get("output", 0)
        ratio = safe_divide(input_tokens, output_tokens)
        return self.create_value("D083", round(ratio, 2))

    def _calc_d084(self, definition: MetricDefinition) -> MetricValue:
        """D084: Total input tokens."""
        return self.create_value("D084", self.data.total_tokens.get("input", 0))

    def _calc_d085(self, definition: MetricDefinition) -> MetricValue:
        """D085: Total output tokens."""
        return self.create_value("D085", self.data.total_tokens.get("output", 0))

    def _calc_d086(self, definition: MetricDefinition) -> MetricValue:
        """D086: Daily token consumption rate."""
        total_tokens = (
            self.data.total_tokens.get("input", 0) +
            self.data.total_tokens.get("output", 0)
        )
        rate = safe_divide(total_tokens, self.data.window_days)
        return self.create_value("D086", round(rate, 2))

    def _calc_d087(self, definition: MetricDefinition) -> MetricValue:
        """D087: Weekly token consumption."""
        week_ago = datetime.now() - timedelta(days=7)
        weekly_tokens = sum(
            s.total_input_tokens + s.total_output_tokens
            for s in self.data.sessions
            if s.start_time and s.start_time >= week_ago
        )
        return self.create_value("D087", weekly_tokens, window_days=7)

    def _calc_d088(self, definition: MetricDefinition) -> MetricValue:
        """D088: Token growth rate (trend)."""
        # Group by date
        daily_tokens: Dict[str, int] = defaultdict(int)
        for s in self.data.sessions:
            if s.start_time:
                date_str = s.start_time.strftime("%Y-%m-%d")
                daily_tokens[date_str] += s.total_input_tokens + s.total_output_tokens

        if len(daily_tokens) < 2:
            return self.create_value("D088", 0.0, trend=0.0)

        sorted_dates = sorted(daily_tokens.keys())
        points: List[Tuple[float, float]] = [
            (float(i), float(daily_tokens[d]))
            for i, d in enumerate(sorted_dates)
        ]
        slope = linear_regression_slope(points)
        return self.create_value("D088", round(slope, 2), trend=slope)

    def _calc_d089(self, definition: MetricDefinition) -> MetricValue:
        """D089: Cache hit ratio."""
        input_tokens = self.data.total_tokens.get("input", 0)
        cache_tokens = self.data.total_tokens.get("cache_read", 0)
        ratio = safe_divide(cache_tokens, input_tokens)
        return self.create_value("D089", round(ratio, 4))

    def _calc_d090(self, definition: MetricDefinition) -> MetricValue:
        """D090: Cache efficiency score (compound)."""
        cache_ratio = self.get_dependency_safe("D089", 0)
        # Simple score based on cache ratio
        score = min(cache_ratio * 100, 100)  # 0-100 scale
        return self.create_value("D090", round(score, 2))

    def _calc_d091(self, definition: MetricDefinition) -> MetricValue:
        """D091: Total cache read tokens."""
        return self.create_value("D091", self.data.total_tokens.get("cache_read", 0))

    def _calc_d092(self, definition: MetricDefinition) -> MetricValue:
        """D092: Effective input tokens (minus cache)."""
        input_tokens = self.get_dependency_safe("D084", 0)
        cache_tokens = self.get_dependency_safe("D091", 0)
        effective = input_tokens - cache_tokens
        return self.create_value("D092", max(0, effective))

    # D093-D102: Cost Metrics

    def _calc_d093(self, definition: MetricDefinition) -> MetricValue:
        """D093: Cache savings estimate (USD)."""
        cache_tokens = self.get_dependency_safe("D091", 0)
        # Estimate savings as difference between full and cached price
        savings_per_million = self.INPUT_PRICE_FULL - self.INPUT_PRICE_CACHED
        savings = (cache_tokens / 1_000_000) * savings_per_million
        return self.create_value("D093", round(savings, 4))

    def _calc_d094(self, definition: MetricDefinition) -> MetricValue:
        """D094: Total cost (USD)."""
        return self.create_value("D094", round(self.data.total_cost_usd, 4))

    def _calc_d095(self, definition: MetricDefinition) -> MetricValue:
        """D095: Daily cost (today)."""
        today = datetime.now().date()
        daily_cost = sum(
            s.cost_usd
            for s in self.data.sessions
            if s.start_time and s.start_time.date() == today
        )
        return self.create_value("D095", round(daily_cost, 4), window_days=1)

    def _calc_d096(self, definition: MetricDefinition) -> MetricValue:
        """D096: Weekly cost (past 7 days)."""
        week_ago = datetime.now() - timedelta(days=7)
        weekly_cost = sum(
            s.cost_usd
            for s in self.data.sessions
            if s.start_time and s.start_time >= week_ago
        )
        return self.create_value("D096", round(weekly_cost, 4), window_days=7)

    def _calc_d097(self, definition: MetricDefinition) -> MetricValue:
        """D097: Monthly cost (past 30 days)."""
        return self.create_value("D097", round(self.data.total_cost_usd, 4))

    def _calc_d098(self, definition: MetricDefinition) -> MetricValue:
        """D098: Cost per session."""
        avg = safe_divide(self.data.total_cost_usd, len(self.data.sessions))
        return self.create_value("D098", round(avg, 4))

    def _calc_d099(self, definition: MetricDefinition) -> MetricValue:
        """D099: Cost per message."""
        avg = safe_divide(self.data.total_cost_usd, self.data.total_messages)
        return self.create_value("D099", round(avg, 6))

    def _calc_d100(self, definition: MetricDefinition) -> MetricValue:
        """D100: Cost per tool call."""
        avg = safe_divide(self.data.total_cost_usd, self.data.total_tool_calls)
        return self.create_value("D100", round(avg, 6))

    def _calc_d101(self, definition: MetricDefinition) -> MetricValue:
        """D101: Cost distribution by model."""
        if not self.data.model_usage:
            return self.create_value("D101", {})

        total_cost = sum(m.cost_usd for m in self.data.model_usage.values())
        if total_cost == 0:
            return self.create_value("D101", {})

        distribution = {
            model: round(data.cost_usd / total_cost, 4)
            for model, data in self.data.model_usage.items()
            if data.cost_usd > 0
        }
        breakdown = {
            model: round(data.cost_usd, 4)
            for model, data in self.data.model_usage.items()
        }
        return self.create_value("D101", distribution, breakdown=breakdown)

    def _calc_d102(self, definition: MetricDefinition) -> MetricValue:
        """D102: Cost trend (slope of daily costs)."""
        daily_costs: Dict[str, float] = defaultdict(float)
        for s in self.data.sessions:
            if s.start_time:
                date_str = s.start_time.strftime("%Y-%m-%d")
                daily_costs[date_str] += s.cost_usd

        if len(daily_costs) < 2:
            return self.create_value("D102", 0.0, trend=0.0)

        sorted_dates = sorted(daily_costs.keys())
        points: List[Tuple[float, float]] = [
            (float(i), daily_costs[d])
            for i, d in enumerate(sorted_dates)
        ]
        slope = linear_regression_slope(points)
        return self.create_value("D102", round(slope, 4), trend=slope)

    # D103-D109: Extended Token/Message Metrics

    def _calc_d103(self, definition: MetricDefinition) -> MetricValue:
        """D103: Average input tokens per message."""
        avg = safe_divide(
            self.data.total_tokens.get("input", 0),
            self.data.total_messages
        )
        return self.create_value("D103", round(avg, 2))

    def _calc_d104(self, definition: MetricDefinition) -> MetricValue:
        """D104: Average output tokens per message."""
        avg = safe_divide(
            self.data.total_tokens.get("output", 0),
            self.data.total_messages
        )
        return self.create_value("D104", round(avg, 2))

    def _calc_d105(self, definition: MetricDefinition) -> MetricValue:
        """D105: Maximum tokens in single message."""
        if not self.data.messages:
            return self.create_value("D105", 0)

        max_tokens = max(
            m.input_tokens + m.output_tokens
            for m in self.data.messages
        )
        return self.create_value("D105", max_tokens)

    def _calc_d106(self, definition: MetricDefinition) -> MetricValue:
        """D106: Token efficiency ratio (output/input)."""
        input_tokens = self.get_dependency_safe("D084", 1)
        output_tokens = self.get_dependency_safe("D085", 0)
        if input_tokens == 0:
            input_tokens = 1
        ratio = safe_divide(output_tokens, input_tokens)
        return self.create_value("D106", round(ratio, 4))

    def _calc_d107(self, definition: MetricDefinition) -> MetricValue:
        """D107: Messages with extended thinking."""
        thinking_count = sum(1 for m in self.data.messages if m.has_thinking)
        return self.create_value("D107", thinking_count)

    def _calc_d108(self, definition: MetricDefinition) -> MetricValue:
        """D108: Thinking usage ratio."""
        thinking_count = self.get_dependency_safe("D107", 0)
        ratio = safe_divide(thinking_count, len(self.data.messages))
        return self.create_value("D108", round(ratio, 4))

    def _calc_d109(self, definition: MetricDefinition) -> MetricValue:
        """D109: Average thinking block length."""
        thinking_lengths = [
            m.thinking_length
            for m in self.data.messages
            if m.has_thinking and m.thinking_length > 0
        ]
        avg = mean(thinking_lengths) if thinking_lengths else 0
        return self.create_value("D109", round(avg, 2))

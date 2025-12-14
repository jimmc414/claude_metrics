"""Category F: Thinking & Complexity Metrics (D137-D142).

These metrics analyze thinking patterns, context management, and conversation
complexity indicators.
"""

from .base import MetricDefinition, MetricType, register_metric

# D137-D142: Thinking & Complexity

register_metric(MetricDefinition(
    id="D137",
    name="thinking_length_trend",
    category="F",
    metric_type=MetricType.TREND,
    description="Trend in thinking block length over time",
    calculation="Slope of thinking length over sessions",
    sources=["messages", "sessions"],
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D138",
    name="sidechain_exploration_rate",
    category="F",
    metric_type=MetricType.RATIO,
    description="Rate of sidechain/alternative exploration in thinking",
    calculation="Thinking blocks with isSidechain=true / total thinking blocks",
    sources=["messages"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D139",
    name="conversation_compaction_rate",
    category="F",
    metric_type=MetricType.RATIO,
    description="Rate of context compaction events",
    calculation="Sessions with compaction / total sessions",
    sources=["sessions", "messages"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D140",
    name="context_clearing_frequency",
    category="F",
    metric_type=MetricType.RATE,
    description="How often context is cleared or managed",
    calculation="Context management events / sessions",
    sources=["sessions", "messages"],
    unit="per session",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D141",
    name="tokens_cleared_per_compaction",
    category="F",
    metric_type=MetricType.FLOAT,
    description="Average tokens cleared per compaction event",
    calculation="Mean of cleared_input_tokens across compaction events",
    sources=["messages"],
    unit="tokens",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D142",
    name="multi_turn_problem_rate",
    category="F",
    metric_type=MetricType.RATIO,
    description="Rate of sessions with complex multi-turn conversations",
    calculation="Sessions with >20 messages / total sessions",
    sources=["sessions"],
    visualization="gauge",
))

"""Category D: Model & Token Metrics (D074-D109).

These metrics analyze model usage patterns, token consumption,
caching efficiency, and cost characteristics.
"""

from .base import MetricDefinition, MetricType, register_metric

# D074-D080: Model Usage Distribution

register_metric(MetricDefinition(
    id="D074",
    name="model_usage_distribution",
    category="D",
    metric_type=MetricType.DISTRIBUTION,
    description="Breakdown of usage by model",
    calculation="Message count per model / total messages",
    sources=["model_usage", "sessions"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D075",
    name="opus_usage_ratio",
    category="D",
    metric_type=MetricType.RATIO,
    description="Proportion of messages using Opus models",
    calculation="Opus messages / total messages",
    sources=["model_usage"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D076",
    name="sonnet_usage_ratio",
    category="D",
    metric_type=MetricType.RATIO,
    description="Proportion of messages using Sonnet models",
    calculation="Sonnet messages / total messages",
    sources=["model_usage"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D077",
    name="haiku_usage_ratio",
    category="D",
    metric_type=MetricType.RATIO,
    description="Proportion of messages using Haiku models",
    calculation="Haiku messages / total messages",
    sources=["model_usage"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D078",
    name="model_switching_frequency",
    category="D",
    metric_type=MetricType.RATE,
    description="Rate of model switches per session",
    calculation="Sessions with >1 model / total sessions",
    sources=["sessions"],
    unit="switches/session",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D079",
    name="primary_model",
    category="D",
    metric_type=MetricType.CATEGORY,
    description="Most frequently used model",
    calculation="Model with highest message count",
    sources=["model_usage"],
    visualization="badge",
))

register_metric(MetricDefinition(
    id="D080",
    name="model_usage_by_subagent",
    category="D",
    metric_type=MetricType.DISTRIBUTION,
    description="Model distribution for agent sessions",
    calculation="Model usage for sessions where is_agent=True",
    sources=["sessions", "model_usage"],
    visualization="stacked_bar",
))

# D081-D092: Token Metrics

register_metric(MetricDefinition(
    id="D081",
    name="tokens_per_message",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average tokens per message",
    calculation="Total tokens / total messages",
    sources=["sessions", "messages"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D082",
    name="tokens_per_session",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average tokens per session",
    calculation="Total tokens / total sessions",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D083",
    name="input_output_token_ratio",
    category="D",
    metric_type=MetricType.RATIO,
    description="Ratio of input tokens to output tokens",
    calculation="Total input tokens / total output tokens",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D084",
    name="total_input_tokens",
    category="D",
    metric_type=MetricType.INT,
    description="Sum of all input tokens in window",
    calculation="sum(session.total_input_tokens)",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D085",
    name="total_output_tokens",
    category="D",
    metric_type=MetricType.INT,
    description="Sum of all output tokens in window",
    calculation="sum(session.total_output_tokens)",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D086",
    name="daily_token_consumption",
    category="D",
    metric_type=MetricType.RATE,
    description="Average tokens consumed per day",
    calculation="Total tokens / window days",
    sources=["sessions"],
    unit="tokens/day",
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D087",
    name="weekly_token_consumption",
    category="D",
    metric_type=MetricType.RATE,
    description="Tokens consumed in the past week",
    calculation="Sum of tokens for past 7 days",
    sources=["sessions"],
    unit="tokens",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D088",
    name="token_growth_rate",
    category="D",
    metric_type=MetricType.TREND,
    description="Slope of daily token consumption",
    calculation="Linear regression of daily token usage",
    sources=["daily_activity"],
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D089",
    name="cache_hit_ratio",
    category="D",
    metric_type=MetricType.RATIO,
    description="Proportion of input tokens from cache",
    calculation="Cache read tokens / total input tokens",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D090",
    name="cache_efficiency_score",
    category="D",
    metric_type=MetricType.COMPOUND,
    description="Composite cache utilization score",
    calculation="Weighted average of cache metrics",
    sources=["sessions"],
    dependencies=["D089"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D091",
    name="cache_read_tokens",
    category="D",
    metric_type=MetricType.INT,
    description="Total tokens read from cache",
    calculation="sum(session.total_cache_read_tokens)",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D092",
    name="effective_input_tokens",
    category="D",
    metric_type=MetricType.INT,
    description="Input tokens minus cached tokens",
    calculation="Total input - cache read tokens",
    sources=["sessions"],
    dependencies=["D084", "D091"],
    visualization="counter",
))

# D093-D102: Cost Metrics

register_metric(MetricDefinition(
    id="D093",
    name="cache_savings_usd",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Estimated savings from cache usage",
    calculation="Cache tokens * input price differential",
    sources=["sessions"],
    dependencies=["D091"],
    unit="USD",
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D094",
    name="total_cost_usd",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Total API cost in window",
    calculation="sum(session.cost_usd)",
    sources=["sessions"],
    unit="USD",
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D095",
    name="daily_cost_usd",
    category="D",
    metric_type=MetricType.FLOAT,
    description="API cost for today",
    calculation="Sum of cost for today's sessions",
    sources=["sessions"],
    unit="USD",
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D096",
    name="weekly_cost_usd",
    category="D",
    metric_type=MetricType.FLOAT,
    description="API cost for past week",
    calculation="Sum of cost for past 7 days",
    sources=["sessions"],
    unit="USD",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D097",
    name="monthly_cost_usd",
    category="D",
    metric_type=MetricType.FLOAT,
    description="API cost for past month (30 days)",
    calculation="Sum of cost for past 30 days",
    sources=["sessions"],
    unit="USD",
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D098",
    name="cost_per_session",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average cost per session",
    calculation="Total cost / total sessions",
    sources=["sessions"],
    dependencies=["D094"],
    unit="USD",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D099",
    name="cost_per_message",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average cost per message",
    calculation="Total cost / total messages",
    sources=["sessions"],
    dependencies=["D094"],
    unit="USD",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D100",
    name="cost_per_tool_call",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average cost per tool call",
    calculation="Total cost / total tool calls",
    sources=["sessions", "tool_calls"],
    dependencies=["D094"],
    unit="USD",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D101",
    name="model_cost_distribution",
    category="D",
    metric_type=MetricType.DISTRIBUTION,
    description="Cost breakdown by model",
    calculation="Cost per model / total cost",
    sources=["model_usage"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D102",
    name="cost_trend",
    category="D",
    metric_type=MetricType.TREND,
    description="Slope of daily cost over time",
    calculation="Linear regression of daily costs",
    sources=["daily_activity"],
    visualization="line_chart",
))

# D103-D109: Extended Token/Message Metrics

register_metric(MetricDefinition(
    id="D103",
    name="avg_input_tokens_per_message",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average input tokens per message",
    calculation="Total input tokens / total messages",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D104",
    name="avg_output_tokens_per_message",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average output tokens per message",
    calculation="Total output tokens / total messages",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D105",
    name="max_tokens_single_message",
    category="D",
    metric_type=MetricType.INT,
    description="Maximum tokens in a single message",
    calculation="Max of (input + output) per message",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D106",
    name="token_efficiency_ratio",
    category="D",
    metric_type=MetricType.RATIO,
    description="Output tokens per input token",
    calculation="Total output / total input",
    sources=["sessions"],
    dependencies=["D084", "D085"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D107",
    name="messages_with_thinking",
    category="D",
    metric_type=MetricType.INT,
    description="Count of messages using extended thinking",
    calculation="Count where has_thinking=True",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D108",
    name="thinking_usage_ratio",
    category="D",
    metric_type=MetricType.RATIO,
    description="Proportion of messages using thinking",
    calculation="Messages with thinking / total messages",
    sources=["messages"],
    dependencies=["D107"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D109",
    name="avg_thinking_length",
    category="D",
    metric_type=MetricType.FLOAT,
    description="Average length of thinking blocks",
    calculation="Mean of thinking_length where has_thinking",
    sources=["messages"],
    unit="characters",
    visualization="gauge",
))

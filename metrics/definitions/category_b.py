"""Category B: Tool Usage Metrics (D029-D048).

These metrics analyze how tools are used, including distribution,
success rates, patterns, and performance characteristics.
"""

from .base import MetricDefinition, MetricType, register_metric

# D029-D035: Tool Distribution

register_metric(MetricDefinition(
    id="D029",
    name="tool_usage_distribution",
    category="B",
    metric_type=MetricType.DISTRIBUTION,
    description="Breakdown of tool usage by tool name",
    calculation="Count of each tool_name / total tool calls",
    sources=["tool_calls"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D030",
    name="most_used_tool",
    category="B",
    metric_type=MetricType.CATEGORY,
    description="Tool with the highest call count",
    calculation="Tool name with max count in tool_counts",
    sources=["tool_calls"],
    visualization="badge",
))

register_metric(MetricDefinition(
    id="D031",
    name="tool_diversity_index",
    category="B",
    metric_type=MetricType.FLOAT,
    description="Shannon entropy of tool usage distribution",
    calculation="-sum(p * log2(p)) for each tool proportion p",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D032",
    name="tool_calls_per_hour",
    category="B",
    metric_type=MetricType.RATE,
    description="Average tool calls per active hour",
    calculation="Total tool calls / total active hours",
    sources=["tool_calls", "sessions"],
    dependencies=["D003"],
    unit="calls/hour",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D033",
    name="tool_calls_per_session",
    category="B",
    metric_type=MetricType.FLOAT,
    description="Average tool calls per session",
    calculation="Total tool calls / total sessions",
    sources=["tool_calls", "sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D034",
    name="tool_calls_per_message",
    category="B",
    metric_type=MetricType.FLOAT,
    description="Average tool calls per assistant message",
    calculation="Total tool calls / assistant messages",
    sources=["tool_calls", "messages"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D035",
    name="bash_to_edit_ratio",
    category="B",
    metric_type=MetricType.RATIO,
    description="Ratio of Bash calls to Edit calls",
    calculation="Bash tool calls / Edit tool calls",
    sources=["tool_calls"],
    visualization="gauge",
))

# D036-D043: Tool Performance

register_metric(MetricDefinition(
    id="D036",
    name="daily_tool_call_trend",
    category="B",
    metric_type=MetricType.TREND,
    description="Slope of daily tool usage over time",
    calculation="Linear regression slope of daily tool counts",
    sources=["tool_calls", "daily_activity"],
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D037",
    name="tool_success_rate",
    category="B",
    metric_type=MetricType.RATIO,
    description="Proportion of successful tool calls",
    calculation="Successful tool calls / total tool calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D038",
    name="bash_error_rate",
    category="B",
    metric_type=MetricType.RATIO,
    description="Proportion of Bash calls that fail",
    calculation="Failed Bash calls / total Bash calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D039",
    name="edit_success_rate",
    category="B",
    metric_type=MetricType.RATIO,
    description="Proportion of Edit calls that succeed",
    calculation="Successful Edit calls / total Edit calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D040",
    name="avg_tool_execution_time_b",
    category="B",
    metric_type=MetricType.DURATION,
    description="Mean duration of tool execution",
    calculation="Mean of tool_call.duration_ms where not null",
    sources=["tool_calls"],
    unit="milliseconds",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D041",
    name="tool_timeout_rate",
    category="B",
    metric_type=MetricType.RATIO,
    description="Proportion of tool calls that timed out",
    calculation="Timed out / total tool calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D042",
    name="longest_tool_execution",
    category="B",
    metric_type=MetricType.DURATION,
    description="Maximum tool execution duration",
    calculation="Max tool_call.duration_ms",
    sources=["tool_calls"],
    unit="milliseconds",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D043",
    name="tool_retry_rate",
    category="B",
    metric_type=MetricType.RATIO,
    description="Proportion of tool calls that were retried",
    calculation="Retried tool calls / total tool calls",
    sources=["tool_calls"],
    visualization="gauge",
))

# D044-D048: Tool Patterns

register_metric(MetricDefinition(
    id="D044",
    name="read_before_edit_ratio",
    category="B",
    metric_type=MetricType.RATIO,
    description="Proportion of Edit calls preceded by Read on same file",
    calculation="Read->Edit sequences / total Edit calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D045",
    name="glob_before_read_ratio",
    category="B",
    metric_type=MetricType.RATIO,
    description="Proportion of Read calls preceded by Glob",
    calculation="Glob->Read sequences / total Read calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D046",
    name="grep_then_read_pattern",
    category="B",
    metric_type=MetricType.SEQUENCE,
    description="Frequency of Grep followed by Read sequences",
    calculation="Count of Grep->Read patterns",
    sources=["tool_calls"],
    visualization="flow_chart",
))

register_metric(MetricDefinition(
    id="D047",
    name="tool_sequence_patterns",
    category="B",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of common 2-tool sequences",
    calculation="Count of each (tool1, tool2) pair",
    sources=["tool_calls"],
    visualization="sankey",
))

register_metric(MetricDefinition(
    id="D048",
    name="tool_co_occurrence",
    category="B",
    metric_type=MetricType.DISTRIBUTION,
    description="Tools frequently used together in same session",
    calculation="Co-occurrence matrix of tools per session",
    sources=["tool_calls", "sessions"],
    visualization="heatmap",
))

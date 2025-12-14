"""Category J: Error & Recovery Metrics (D189-D203).

These metrics analyze error rates, recovery patterns, and interruption
behavior in Claude Code sessions.
"""

from .base import MetricDefinition, MetricType, register_metric

# D189-D194: Error Rates

register_metric(MetricDefinition(
    id="D189",
    name="overall_error_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Overall tool error rate",
    calculation="Failed tool calls / total tool calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D190",
    name="bash_error_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Error rate for Bash tool",
    calculation="Failed Bash calls / total Bash calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D191",
    name="edit_conflict_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Error rate for Edit tool",
    calculation="Failed Edit calls / total Edit calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D192",
    name="read_failure_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Error rate for Read tool",
    calculation="Failed Read calls / total Read calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D193",
    name="permission_error_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Rate of permission-related errors",
    calculation="Permission errors / total tool calls",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D194",
    name="api_error_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Rate of API errors",
    calculation="API error messages / total messages",
    sources=["messages"],
    visualization="gauge",
))

# D195-D199: Recovery Patterns

register_metric(MetricDefinition(
    id="D195",
    name="error_recovery_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Rate of successful recovery after errors",
    calculation="Errors followed by success / total errors",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D196",
    name="retry_success_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Success rate of retry attempts",
    calculation="Successful retries / total retry attempts",
    sources=["tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D197",
    name="errors_per_session",
    category="J",
    metric_type=MetricType.FLOAT,
    description="Average errors per session",
    calculation="Total errors / session count",
    sources=["sessions", "tool_calls"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D198",
    name="error_clustering",
    category="J",
    metric_type=MetricType.INT,
    description="Sessions with multiple errors clustered together",
    calculation="Sessions with 3+ errors in sequence",
    sources=["sessions", "tool_calls"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D199",
    name="time_to_recovery",
    category="J",
    metric_type=MetricType.DURATION,
    description="Average time from error to successful recovery",
    calculation="Mean time between error and next success",
    sources=["tool_calls"],
    unit="seconds",
    visualization="gauge",
))

# D200-D203: Interruption Metrics

register_metric(MetricDefinition(
    id="D200",
    name="interrupted_operations",
    category="J",
    metric_type=MetricType.INT,
    description="Count of interrupted tool operations",
    calculation="Tool calls with interrupted=true",
    sources=["tool_calls"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D201",
    name="truncated_outputs",
    category="J",
    metric_type=MetricType.INT,
    description="Count of truncated tool outputs",
    calculation="Tool calls with truncated=true",
    sources=["tool_calls"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D202",
    name="killed_shells",
    category="J",
    metric_type=MetricType.INT,
    description="Count of manually killed shell processes",
    calculation="KillShell tool call count",
    sources=["tool_calls"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D203",
    name="hook_prevention_rate",
    category="J",
    metric_type=MetricType.RATIO,
    description="Rate at which hooks prevented continuation",
    calculation="preventedContinuation / total hook executions",
    sources=["sessions"],
    visualization="gauge",
))

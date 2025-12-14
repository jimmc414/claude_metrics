"""Category H: Agent & Delegation Metrics (D159-D172).

These metrics analyze subagent usage patterns, delegation behavior,
and agent efficiency.
"""

from .base import MetricDefinition, MetricType, register_metric

# D159-D166: Subagent Usage

register_metric(MetricDefinition(
    id="D159",
    name="agent_sessions",
    category="H",
    metric_type=MetricType.INT,
    description="Total count of agent sessions",
    calculation="Count of agent-*.jsonl files or Task tool calls",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D160",
    name="main_vs_agent_ratio",
    category="H",
    metric_type=MetricType.RATIO,
    description="Ratio of main sessions to agent sessions",
    calculation="Main sessions / agent sessions",
    sources=["sessions"],
    dependencies=["D159"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D161",
    name="agent_usage_percentage",
    category="H",
    metric_type=MetricType.PERCENTAGE,
    description="Percentage of sessions using agents",
    calculation="Sessions with agents / total sessions * 100",
    sources=["sessions"],
    unit="%",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D162",
    name="subagent_type_distribution",
    category="H",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of subagent types used",
    calculation="Count by subagent_type parameter",
    sources=["sessions"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D163",
    name="most_used_subagent",
    category="H",
    metric_type=MetricType.CATEGORY,
    description="Most frequently used subagent type",
    calculation="Subagent type with highest count",
    sources=["sessions"],
    dependencies=["D162"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D164",
    name="explore_agent_usage",
    category="H",
    metric_type=MetricType.INT,
    description="Count of Explore agent invocations",
    calculation="Task calls with subagent_type='Explore'",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D165",
    name="plan_agent_usage",
    category="H",
    metric_type=MetricType.INT,
    description="Count of Plan agent invocations",
    calculation="Task calls with subagent_type='Plan'",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D166",
    name="custom_agent_usage",
    category="H",
    metric_type=MetricType.INT,
    description="Count of custom/non-built-in agent invocations",
    calculation="Task calls with non-standard subagent_type",
    sources=["sessions"],
    visualization="counter",
))

# D167-D172: Agent Efficiency

register_metric(MetricDefinition(
    id="D167",
    name="tokens_per_agent_task",
    category="H",
    metric_type=MetricType.FLOAT,
    description="Average tokens consumed per agent task",
    calculation="Total agent tokens / agent task count",
    sources=["sessions"],
    unit="tokens",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D168",
    name="tools_per_agent_task",
    category="H",
    metric_type=MetricType.FLOAT,
    description="Average tools used per agent task",
    calculation="Total agent tool calls / agent task count",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D169",
    name="agent_success_rate",
    category="H",
    metric_type=MetricType.RATIO,
    description="Success rate of agent tasks",
    calculation="Successful agent completions / total agent tasks",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D170",
    name="agent_resume_rate",
    category="H",
    metric_type=MetricType.RATIO,
    description="Rate of agent task resumption",
    calculation="Task calls with resume parameter / total Task calls",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D171",
    name="parallel_agent_frequency",
    category="H",
    metric_type=MetricType.INT,
    description="Count of parallel agent invocations",
    calculation="Messages with multiple simultaneous Task calls",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D172",
    name="agent_depth",
    category="H",
    metric_type=MetricType.INT,
    description="Maximum nesting depth of agent spawns",
    calculation="Max depth of nested Task calls",
    sources=["sessions"],
    visualization="bar_chart",
))

"""Category I: Project Metrics (D173-D188).

These metrics analyze project-level activity, git branch patterns,
and cross-project behavior.
"""

from .base import MetricDefinition, MetricType, register_metric

# D173-D178: Project Activity

register_metric(MetricDefinition(
    id="D173",
    name="total_projects",
    category="I",
    metric_type=MetricType.INT,
    description="Total number of unique projects worked on",
    calculation="Count of unique cwd values",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D174",
    name="sessions_per_project",
    category="I",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of sessions across projects",
    calculation="Session count grouped by cwd",
    sources=["sessions"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D175",
    name="most_active_project",
    category="I",
    metric_type=MetricType.CATEGORY,
    description="Project with the most sessions",
    calculation="cwd with highest session count",
    sources=["sessions"],
    dependencies=["D174"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D176",
    name="messages_per_project",
    category="I",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of messages across projects",
    calculation="Message count grouped by project cwd",
    sources=["sessions", "messages"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D177",
    name="time_per_project",
    category="I",
    metric_type=MetricType.DISTRIBUTION,
    description="Active hours distribution across projects",
    calculation="Session durations summed by project cwd",
    sources=["sessions"],
    unit="hours",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D178",
    name="tools_per_project",
    category="I",
    metric_type=MetricType.DISTRIBUTION,
    description="Tool call distribution across projects",
    calculation="Tool call count grouped by project cwd",
    sources=["sessions", "tool_calls"],
    visualization="bar_chart",
))

# D179-D183: Git Activity

register_metric(MetricDefinition(
    id="D179",
    name="branches_worked_on",
    category="I",
    metric_type=MetricType.INT,
    description="Number of unique git branches worked on",
    calculation="Count of unique gitBranch values",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D180",
    name="main_branch_activity",
    category="I",
    metric_type=MetricType.INT,
    description="Sessions on main/master branches",
    calculation="Sessions where gitBranch is 'main' or 'master'",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D181",
    name="feature_branch_activity",
    category="I",
    metric_type=MetricType.INT,
    description="Sessions on feature branches",
    calculation="Sessions on non-main branches",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D182",
    name="branch_switching_frequency",
    category="I",
    metric_type=MetricType.RATE,
    description="Rate of branch switches per session",
    calculation="Branch changes / session count",
    sources=["sessions"],
    unit="per session",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D183",
    name="empty_branch_sessions",
    category="I",
    metric_type=MetricType.INT,
    description="Sessions without git branch info",
    calculation="Sessions where gitBranch is empty",
    sources=["sessions"],
    visualization="counter",
))

# D184-D188: Project Complexity

register_metric(MetricDefinition(
    id="D184",
    name="files_per_project",
    category="I",
    metric_type=MetricType.DISTRIBUTION,
    description="Unique files touched per project",
    calculation="Distinct file paths grouped by project cwd",
    sources=["sessions", "tool_calls"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D185",
    name="tool_diversity_per_project",
    category="I",
    metric_type=MetricType.DISTRIBUTION,
    description="Unique tools used per project",
    calculation="Distinct tool types grouped by project cwd",
    sources=["sessions", "tool_calls"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D186",
    name="session_depth_per_project",
    category="I",
    metric_type=MetricType.DISTRIBUTION,
    description="Average message depth per project",
    calculation="Mean messages per session grouped by project",
    sources=["sessions"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D187",
    name="multi_project_sessions",
    category="I",
    metric_type=MetricType.INT,
    description="Sessions spanning multiple projects",
    calculation="Sessions with multiple distinct cwd values",
    sources=["sessions"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D188",
    name="project_switching_frequency",
    category="I",
    metric_type=MetricType.RATE,
    description="Rate of project context switches",
    calculation="Project changes per day",
    sources=["sessions"],
    unit="per day",
    visualization="line_chart",
))

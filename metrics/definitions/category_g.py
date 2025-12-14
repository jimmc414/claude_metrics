"""Category G: Task Management Metrics (D143-D158).

These metrics analyze todo completion patterns, planning behavior,
and task management effectiveness.
"""

from .base import MetricDefinition, MetricType, register_metric

# D143-D151: Todo Completion

register_metric(MetricDefinition(
    id="D143",
    name="total_todos_created",
    category="G",
    metric_type=MetricType.INT,
    description="Total number of todo items created",
    calculation="Sum of all todo items across sessions",
    sources=["sessions", "todos"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D144",
    name="completed_todos",
    category="G",
    metric_type=MetricType.INT,
    description="Number of todos marked as completed",
    calculation="Count where status='completed'",
    sources=["sessions", "todos"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D145",
    name="overall_completion_rate",
    category="G",
    metric_type=MetricType.RATIO,
    description="Overall todo completion rate",
    calculation="Completed todos / total todos",
    sources=["sessions", "todos"],
    dependencies=["D143", "D144"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D146",
    name="in_progress_abandoned",
    category="G",
    metric_type=MetricType.INT,
    description="Todos left in progress and never completed",
    calculation="Count where status='in_progress' at session end",
    sources=["sessions", "todos"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D147",
    name="pending_never_started",
    category="G",
    metric_type=MetricType.INT,
    description="Todos that were never started",
    calculation="Count where status='pending' at session end",
    sources=["sessions", "todos"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D148",
    name="abandonment_rate",
    category="G",
    metric_type=MetricType.RATIO,
    description="Rate of task abandonment",
    calculation="In-progress / (completed + in-progress)",
    sources=["sessions", "todos"],
    dependencies=["D144", "D146"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D149",
    name="avg_tasks_per_session",
    category="G",
    metric_type=MetricType.FLOAT,
    description="Average number of tasks per session",
    calculation="Total todos / sessions with todos",
    sources=["sessions", "todos"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D150",
    name="max_tasks_in_session",
    category="G",
    metric_type=MetricType.INT,
    description="Maximum todo count in a single session",
    calculation="Max todo count across all sessions",
    sources=["sessions", "todos"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D151",
    name="high_priority_ratio",
    category="G",
    metric_type=MetricType.RATIO,
    description="Ratio of high priority tasks",
    calculation="High priority todos / total todos",
    sources=["sessions", "todos"],
    visualization="gauge",
))

# D152-D158: Planning Metrics

register_metric(MetricDefinition(
    id="D152",
    name="plans_created",
    category="G",
    metric_type=MetricType.INT,
    description="Total number of plans created",
    calculation="Count of EnterPlanMode calls or plan files",
    sources=["sessions", "plans"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D153",
    name="avg_plan_size",
    category="G",
    metric_type=MetricType.FLOAT,
    description="Average plan file size",
    calculation="Mean of plan file sizes in bytes",
    sources=["plans"],
    unit="bytes",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D154",
    name="plan_complexity_score",
    category="G",
    metric_type=MetricType.COMPOUND,
    description="Composite plan complexity score",
    calculation="(header_count * 0.3) + (code_block_count * 0.3) + (normalized_size * 0.4)",
    sources=["plans"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D155",
    name="technologies_per_plan",
    category="G",
    metric_type=MetricType.FLOAT,
    description="Average number of technologies referenced per plan",
    calculation="Mean count of unique tech keywords per plan",
    sources=["plans"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D156",
    name="action_words_per_plan",
    category="G",
    metric_type=MetricType.FLOAT,
    description="Average implementation verbs per plan",
    calculation="Mean count of action verbs per plan",
    sources=["plans"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D157",
    name="plan_approval_rate",
    category="G",
    metric_type=MetricType.RATIO,
    description="Rate of plan approval",
    calculation="ExitPlanMode calls / EnterPlanMode calls",
    sources=["sessions"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D158",
    name="planning_to_execution_ratio",
    category="G",
    metric_type=MetricType.RATIO,
    description="Ratio of planning to actual execution",
    calculation="Plans created / features completed",
    sources=["sessions", "plans"],
    visualization="gauge",
))

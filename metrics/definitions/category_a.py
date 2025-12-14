"""Category A: Time & Activity Metrics (D001-D028).

These metrics focus on when and how long users interact with Claude Code,
including session patterns, activity streaks, and time-of-day analysis.
"""

from .base import MetricDefinition, MetricType, register_metric

# D001-D010: Active Time Calculations

register_metric(MetricDefinition(
    id="D001",
    name="daily_active_hours",
    category="A",
    metric_type=MetricType.DURATION,
    description="Hours active in coding today",
    calculation="Sum of session durations for today's date",
    sources=["sessions"],
    unit="hours",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D002",
    name="weekly_active_hours",
    category="A",
    metric_type=MetricType.DURATION,
    description="Hours active this week",
    calculation="Sum of session durations for past 7 days",
    sources=["sessions"],
    unit="hours",
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D003",
    name="monthly_active_hours",
    category="A",
    metric_type=MetricType.DURATION,
    description="Hours active this month (30 days)",
    calculation="Sum of session durations for past 30 days",
    sources=["sessions"],
    unit="hours",
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D004",
    name="total_thinking_time",
    category="A",
    metric_type=MetricType.DURATION,
    description="Total extended thinking time used",
    calculation="Sum of thinking block durations across all messages",
    sources=["sessions", "messages"],
    unit="minutes",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D005",
    name="avg_response_time",
    category="A",
    metric_type=MetricType.DURATION,
    description="Average time between user message and assistant response",
    calculation="Mean of (assistant_timestamp - user_timestamp) pairs",
    sources=["messages"],
    unit="seconds",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D006",
    name="longest_session_duration",
    category="A",
    metric_type=MetricType.DURATION,
    description="Duration of the longest session",
    calculation="Max session duration_ms / 3600000",
    sources=["sessions"],
    unit="hours",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D007",
    name="avg_session_duration",
    category="A",
    metric_type=MetricType.DURATION,
    description="Mean session length",
    calculation="Mean of session duration_ms / 3600000",
    sources=["sessions"],
    unit="hours",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D008",
    name="median_session_duration",
    category="A",
    metric_type=MetricType.DURATION,
    description="Median session length",
    calculation="Median of session duration_ms / 3600000",
    sources=["sessions"],
    unit="hours",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D009",
    name="total_api_time",
    category="A",
    metric_type=MetricType.DURATION,
    description="Total time spent in API calls",
    calculation="Sum of all tool execution times",
    sources=["tool_calls"],
    unit="minutes",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D010",
    name="avg_tool_execution_time",
    category="A",
    metric_type=MetricType.DURATION,
    description="Mean tool call duration",
    calculation="Mean of tool_call.duration_ms",
    sources=["tool_calls"],
    unit="milliseconds",
    visualization="gauge",
))

# D011-D020: Time Distribution Analysis

register_metric(MetricDefinition(
    id="D011",
    name="peak_activity_hour",
    category="A",
    metric_type=MetricType.CATEGORY,
    description="Most active hour of the day (0-23)",
    calculation="Hour with maximum session starts",
    sources=["sessions", "hourly_distribution"],
    unit="hour",
    visualization="heatmap",
))

register_metric(MetricDefinition(
    id="D012",
    name="peak_productivity_day",
    category="A",
    metric_type=MetricType.CATEGORY,
    description="Most productive day of the week",
    calculation="Weekday with highest message count",
    sources=["sessions", "daily_activity"],
    unit="weekday",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D013",
    name="morning_activity_ratio",
    category="A",
    metric_type=MetricType.RATIO,
    description="Proportion of activity between 6AM-12PM",
    calculation="Sessions 6-12 / total sessions",
    sources=["sessions", "hourly_distribution"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D014",
    name="afternoon_activity_ratio",
    category="A",
    metric_type=MetricType.RATIO,
    description="Proportion of activity between 12PM-6PM",
    calculation="Sessions 12-18 / total sessions",
    sources=["sessions", "hourly_distribution"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D015",
    name="evening_activity_ratio",
    category="A",
    metric_type=MetricType.RATIO,
    description="Proportion of activity between 6PM-12AM",
    calculation="Sessions 18-24 / total sessions",
    sources=["sessions", "hourly_distribution"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D016",
    name="night_activity_ratio",
    category="A",
    metric_type=MetricType.RATIO,
    description="Proportion of activity between 12AM-6AM",
    calculation="Sessions 0-6 / total sessions",
    sources=["sessions", "hourly_distribution"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D017",
    name="weekday_vs_weekend_ratio",
    category="A",
    metric_type=MetricType.RATIO,
    description="Ratio of weekday to weekend activity",
    calculation="Weekday sessions / weekend sessions",
    sources=["sessions", "daily_activity"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D018",
    name="session_start_time_variance",
    category="A",
    metric_type=MetricType.FLOAT,
    description="Variance in daily session start times",
    calculation="Std dev of session start hour",
    sources=["sessions"],
    unit="hours",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D019",
    name="session_start_time_distribution",
    category="A",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of session start times by hour",
    calculation="Count of sessions starting in each hour bucket",
    sources=["sessions", "hourly_distribution"],
    visualization="histogram",
))

register_metric(MetricDefinition(
    id="D020",
    name="session_end_time_distribution",
    category="A",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of session end times by hour",
    calculation="Count of sessions ending in each hour bucket",
    sources=["sessions"],
    visualization="histogram",
))

# D021-D028: Streaks and Frequency

register_metric(MetricDefinition(
    id="D021",
    name="longest_activity_streak",
    category="A",
    metric_type=MetricType.INT,
    description="Maximum consecutive days with activity",
    calculation="Max consecutive dates with sessions",
    sources=["sessions", "daily_activity"],
    unit="days",
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D022",
    name="current_activity_streak",
    category="A",
    metric_type=MetricType.INT,
    description="Current consecutive active days ending today",
    calculation="Consecutive dates ending at today with sessions",
    sources=["sessions", "daily_activity"],
    unit="days",
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D023",
    name="weekly_active_days",
    category="A",
    metric_type=MetricType.INT,
    description="Number of days with activity in the past week",
    calculation="Count of unique dates with sessions in past 7 days",
    sources=["sessions"],
    unit="days",
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D024",
    name="monthly_active_days",
    category="A",
    metric_type=MetricType.INT,
    description="Number of days with activity in the past month",
    calculation="Count of unique dates with sessions in past 30 days",
    sources=["sessions"],
    unit="days",
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D025",
    name="avg_sessions_per_active_day",
    category="A",
    metric_type=MetricType.FLOAT,
    description="Average number of sessions per day with activity",
    calculation="Total sessions / active days",
    sources=["sessions"],
    dependencies=["D024"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D026",
    name="session_frequency",
    category="A",
    metric_type=MetricType.RATE,
    description="Average sessions per calendar day",
    calculation="Total sessions / window days",
    sources=["sessions"],
    unit="sessions/day",
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D027",
    name="inter_session_gap",
    category="A",
    metric_type=MetricType.DURATION,
    description="Average time between consecutive sessions",
    calculation="Mean of (session[n+1].start - session[n].end)",
    sources=["sessions"],
    unit="hours",
    visualization="histogram",
))

register_metric(MetricDefinition(
    id="D028",
    name="activity_density",
    category="A",
    metric_type=MetricType.RATE,
    description="Messages per active hour",
    calculation="Total messages / total active hours",
    sources=["sessions", "messages"],
    dependencies=["D003"],
    unit="messages/hour",
    visualization="gauge",
))

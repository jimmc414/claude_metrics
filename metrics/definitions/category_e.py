"""Category E: Conversation Analysis Metrics (D110-D136).

These metrics analyze conversation patterns, message content, topic distribution,
and thinking patterns within Claude Code sessions.
"""

from .base import MetricDefinition, MetricType, register_metric

# D110-D118: Message Patterns

register_metric(MetricDefinition(
    id="D110",
    name="conversation_depth",
    category="E",
    metric_type=MetricType.INT,
    description="Maximum message chain length in a session",
    calculation="Max count of consecutive messages in sessions",
    sources=["sessions", "messages"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D111",
    name="questions_asked_by_user",
    category="E",
    metric_type=MetricType.INT,
    description="Number of user messages containing question marks",
    calculation="Count of user messages containing '?'",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D112",
    name="question_ratio",
    category="E",
    metric_type=MetricType.RATIO,
    description="Proportion of user messages that are questions",
    calculation="Messages with '?' / total user messages",
    sources=["messages"],
    dependencies=["D111"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D113",
    name="commands_given",
    category="E",
    metric_type=MetricType.INT,
    description="Count of imperative/directive user messages",
    calculation="Messages starting with verbs like 'do', 'make', 'create', 'fix'",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D114",
    name="code_pastes_by_user",
    category="E",
    metric_type=MetricType.INT,
    description="Number of user messages containing code blocks or long text",
    calculation="Messages with triple backticks or length > 500 chars",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D115",
    name="error_reports_by_user",
    category="E",
    metric_type=MetricType.INT,
    description="Number of user messages reporting errors",
    calculation="Messages containing 'error', 'traceback', 'exception', 'failed'",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D116",
    name="frustration_indicators",
    category="E",
    metric_type=MetricType.INT,
    description="Count of messages indicating user frustration",
    calculation="Messages with 'wrong', 'still not', 'doesn't work', 'not working'",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D117",
    name="gratitude_expressions",
    category="E",
    metric_type=MetricType.INT,
    description="Count of messages expressing user satisfaction",
    calculation="Messages with 'thanks', 'perfect', 'great', 'awesome', 'works'",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D118",
    name="frustration_gratitude_ratio",
    category="E",
    metric_type=MetricType.RATIO,
    description="Ratio of frustration to gratitude expressions",
    calculation="Frustration count / gratitude count",
    sources=["messages"],
    dependencies=["D116", "D117"],
    visualization="gauge",
))

# D119-D127: Topic Analysis

register_metric(MetricDefinition(
    id="D119",
    name="bug_related_messages",
    category="E",
    metric_type=MetricType.INT,
    description="Messages related to bug fixing",
    calculation="Messages with bug/error/fix/debug keywords",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D120",
    name="feature_related_messages",
    category="E",
    metric_type=MetricType.INT,
    description="Messages related to feature development",
    calculation="Messages with add/create/implement/build keywords",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D121",
    name="refactor_related_messages",
    category="E",
    metric_type=MetricType.INT,
    description="Messages related to code refactoring",
    calculation="Messages with refactor/clean/improve/optimize keywords",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D122",
    name="test_related_messages",
    category="E",
    metric_type=MetricType.INT,
    description="Messages related to testing",
    calculation="Messages with test/pytest/unittest/coverage keywords",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D123",
    name="docs_related_messages",
    category="E",
    metric_type=MetricType.INT,
    description="Messages related to documentation",
    calculation="Messages with document/readme/comment/docstring keywords",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D124",
    name="debug_related_messages",
    category="E",
    metric_type=MetricType.INT,
    description="Messages related to debugging and investigation",
    calculation="Messages with debug/why/trace/investigate keywords",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D125",
    name="review_related_messages",
    category="E",
    metric_type=MetricType.INT,
    description="Messages related to code review",
    calculation="Messages with review/check/examine/look at keywords",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D126",
    name="topic_distribution",
    category="E",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of messages by topic category",
    calculation="Percentage breakdown by bug/feature/refactor/test/docs/debug/review",
    sources=["messages"],
    dependencies=["D119", "D120", "D121", "D122", "D123", "D124", "D125"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D127",
    name="topic_trend_over_time",
    category="E",
    metric_type=MetricType.TREND,
    description="How topic focus changes over the time window",
    calculation="Slope of dominant topic frequency over sessions",
    sources=["messages", "sessions"],
    visualization="line_chart",
))

# D128-D136: Extended Thinking Analysis

register_metric(MetricDefinition(
    id="D128",
    name="sessions_with_thinking",
    category="E",
    metric_type=MetricType.RATIO,
    description="Proportion of sessions containing thinking blocks",
    calculation="Sessions with thinking / total sessions",
    sources=["sessions", "messages"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D129",
    name="thinking_blocks_per_session",
    category="E",
    metric_type=MetricType.FLOAT,
    description="Average number of thinking blocks per session",
    calculation="Total thinking blocks / session count",
    sources=["sessions", "messages"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D130",
    name="avg_thinking_length",
    category="E",
    metric_type=MetricType.FLOAT,
    description="Average character length of thinking blocks",
    calculation="Mean of thinking block character counts",
    sources=["messages"],
    unit="characters",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D131",
    name="median_thinking_length",
    category="E",
    metric_type=MetricType.FLOAT,
    description="Median character length of thinking blocks",
    calculation="Median of thinking block character counts",
    sources=["messages"],
    unit="characters",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D132",
    name="max_thinking_length",
    category="E",
    metric_type=MetricType.INT,
    description="Longest thinking block encountered",
    calculation="Max of thinking block character counts",
    sources=["messages"],
    unit="characters",
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D133",
    name="thinking_token_percentage",
    category="E",
    metric_type=MetricType.RATIO,
    description="Proportion of output tokens used for thinking",
    calculation="Thinking tokens / total output tokens",
    sources=["messages"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D134",
    name="ultrathink_trigger_count",
    category="E",
    metric_type=MetricType.INT,
    description="Number of times ULTRATHINK mode was triggered",
    calculation="Count of messages with ULTRATHINK in thinking metadata",
    sources=["messages"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D135",
    name="thinking_level_distribution",
    category="E",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of thinking levels used",
    calculation="Count by thinkingMetadata.level values",
    sources=["messages"],
    visualization="bar_chart",
))

register_metric(MetricDefinition(
    id="D136",
    name="thinking_disabled_rate",
    category="E",
    metric_type=MetricType.RATIO,
    description="Rate at which thinking was disabled",
    calculation="Messages with thinking disabled / total messages",
    sources=["messages"],
    visualization="gauge",
))

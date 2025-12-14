"""Category C: File Operations Metrics (D049-D073).

These metrics analyze file reading, editing, and writing patterns,
including file types, frequency, and relationships.
"""

from .base import MetricDefinition, MetricType, register_metric

# D049-D055: File Counts and Frequency

register_metric(MetricDefinition(
    id="D049",
    name="unique_files_read",
    category="C",
    metric_type=MetricType.INT,
    description="Count of distinct files read",
    calculation="len(files_read)",
    sources=["tool_calls", "files_read"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D050",
    name="unique_files_edited",
    category="C",
    metric_type=MetricType.INT,
    description="Count of distinct files edited",
    calculation="len(files_edited)",
    sources=["tool_calls", "files_edited"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D051",
    name="file_read_frequency",
    category="C",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of read counts per file",
    calculation="Histogram of files_read values",
    sources=["files_read"],
    visualization="histogram",
))

register_metric(MetricDefinition(
    id="D052",
    name="file_edit_frequency",
    category="C",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of edit counts per file",
    calculation="Histogram of files_edited values",
    sources=["files_edited"],
    visualization="histogram",
))

register_metric(MetricDefinition(
    id="D053",
    name="most_read_file",
    category="C",
    metric_type=MetricType.CATEGORY,
    description="File with the most read operations",
    calculation="Key with max value in files_read",
    sources=["files_read"],
    visualization="badge",
))

register_metric(MetricDefinition(
    id="D054",
    name="most_edited_file",
    category="C",
    metric_type=MetricType.CATEGORY,
    description="File with the most edit operations",
    calculation="Key with max value in files_edited",
    sources=["files_edited"],
    visualization="badge",
))

register_metric(MetricDefinition(
    id="D055",
    name="read_to_write_ratio",
    category="C",
    metric_type=MetricType.RATIO,
    description="Ratio of read operations to write/edit operations",
    calculation="Read tool calls / (Edit + Write tool calls)",
    sources=["tool_calls"],
    visualization="gauge",
))

# D056-D063: File Types and Creation

register_metric(MetricDefinition(
    id="D056",
    name="new_file_creation_rate",
    category="C",
    metric_type=MetricType.RATE,
    description="Rate of new file creation per session",
    calculation="Write tool calls (new files) / total sessions",
    sources=["tool_calls", "sessions"],
    unit="files/session",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D057",
    name="file_deletion_rate",
    category="C",
    metric_type=MetricType.RATE,
    description="Rate of file deletion per session",
    calculation="Bash rm calls / total sessions",
    sources=["tool_calls", "sessions"],
    unit="files/session",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D058",
    name="file_type_distribution",
    category="C",
    metric_type=MetricType.DISTRIBUTION,
    description="Breakdown of file operations by extension",
    calculation="Group files by extension, count operations",
    sources=["files_read", "files_edited"],
    visualization="pie_chart",
))

register_metric(MetricDefinition(
    id="D059",
    name="python_file_ratio",
    category="C",
    metric_type=MetricType.RATIO,
    description="Proportion of operations on .py files",
    calculation=".py file operations / total file operations",
    sources=["files_read", "files_edited"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D060",
    name="javascript_file_ratio",
    category="C",
    metric_type=MetricType.RATIO,
    description="Proportion of operations on .js/.ts files",
    calculation=".js/.ts/.jsx/.tsx file operations / total",
    sources=["files_read", "files_edited"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D061",
    name="markdown_file_ratio",
    category="C",
    metric_type=MetricType.RATIO,
    description="Proportion of operations on .md files",
    calculation=".md file operations / total file operations",
    sources=["files_read", "files_edited"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D062",
    name="config_file_ratio",
    category="C",
    metric_type=MetricType.RATIO,
    description="Proportion of operations on config files",
    calculation="Config file operations / total file operations",
    sources=["files_read", "files_edited"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D063",
    name="test_file_ratio",
    category="C",
    metric_type=MetricType.RATIO,
    description="Proportion of operations on test files",
    calculation="Test file operations / total file operations",
    sources=["files_read", "files_edited"],
    visualization="gauge",
))

# D064-D069: File Size and Churn

register_metric(MetricDefinition(
    id="D064",
    name="avg_file_size_read",
    category="C",
    metric_type=MetricType.FLOAT,
    description="Average size of files read",
    calculation="Mean of file sizes for Read operations",
    sources=["tool_calls"],
    unit="bytes",
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D065",
    name="file_versions_created",
    category="C",
    metric_type=MetricType.INT,
    description="Total file version backups created",
    calculation="Count of file history entries",
    sources=["file_history"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D066",
    name="avg_versions_per_file",
    category="C",
    metric_type=MetricType.FLOAT,
    description="Average version backups per edited file",
    calculation="Total versions / unique edited files",
    sources=["file_history", "files_edited"],
    dependencies=["D050", "D065"],
    visualization="gauge",
))

register_metric(MetricDefinition(
    id="D067",
    name="max_versions_per_file",
    category="C",
    metric_type=MetricType.INT,
    description="Maximum versions for any single file",
    calculation="Max version count across all files",
    sources=["file_history"],
    visualization="counter",
))

register_metric(MetricDefinition(
    id="D068",
    name="file_churn_rate",
    category="C",
    metric_type=MetricType.RATE,
    description="Rate of file edits per day",
    calculation="Total Edit operations / window days",
    sources=["tool_calls"],
    unit="edits/day",
    visualization="line_chart",
))

register_metric(MetricDefinition(
    id="D069",
    name="file_stability_index",
    category="C",
    metric_type=MetricType.INVERSE,
    description="Inverse of file churn rate (higher = more stable)",
    calculation="1 / file_churn_rate",
    sources=["tool_calls"],
    dependencies=["D068"],
    visualization="gauge",
))

# D070-D073: Directory and Relationships

register_metric(MetricDefinition(
    id="D070",
    name="directory_depth_distribution",
    category="C",
    metric_type=MetricType.DISTRIBUTION,
    description="Distribution of file path depths",
    calculation="Count files at each directory depth level",
    sources=["files_read", "files_edited"],
    visualization="histogram",
))

register_metric(MetricDefinition(
    id="D071",
    name="files_modified_together",
    category="C",
    metric_type=MetricType.DISTRIBUTION,
    description="Files frequently edited in same session",
    calculation="Co-occurrence of file edits per session",
    sources=["tool_calls", "sessions"],
    visualization="network",
))

register_metric(MetricDefinition(
    id="D072",
    name="file_dependency_graph",
    category="C",
    metric_type=MetricType.COMPOUND,
    description="Graph of file read/edit relationships",
    calculation="Build graph from Read->Edit sequences on files",
    sources=["tool_calls"],
    visualization="network",
))

register_metric(MetricDefinition(
    id="D073",
    name="cross_directory_edits",
    category="C",
    metric_type=MetricType.RATIO,
    description="Sessions editing files in multiple directories",
    calculation="Sessions with >1 unique dir / total sessions",
    sources=["tool_calls", "sessions"],
    visualization="gauge",
))

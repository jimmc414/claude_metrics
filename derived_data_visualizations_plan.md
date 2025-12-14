# Derived Metrics Visualization System - Implementation Plan

## Current Focus: Phase 5 - Extended Metrics (E-J) [COMPLETED]

**Goal**: Implement Categories E-J derived metrics (94 additional metrics)

**Status**: All deliverables completed on 2024-12-14

**Deliverables**:
1. [x] `metrics/definitions/category_e.py` - D110-D136 definitions (27 metrics)
2. [x] `metrics/definitions/category_f.py` - D137-D142 definitions (6 metrics)
3. [x] `metrics/definitions/category_g.py` - D143-D158 definitions (16 metrics)
4. [x] `metrics/definitions/category_h.py` - D159-D172 definitions (14 metrics)
5. [x] `metrics/definitions/category_i.py` - D173-D188 definitions (16 metrics)
6. [x] `metrics/definitions/category_j.py` - D189-D203 definitions (15 metrics)
7. [x] `metrics/calculators/category_e.py` - Conversation Analysis calculators
8. [x] `metrics/calculators/category_f.py` - Thinking & Complexity calculators
9. [x] `metrics/calculators/category_g.py` - Task Management calculators
10. [x] `metrics/calculators/category_h.py` - Agent & Delegation calculators
11. [x] `metrics/calculators/category_i.py` - Project Metrics calculators
12. [x] `metrics/calculators/category_j.py` - Error & Recovery calculators

**Files Created (12 total)**:
- `metrics/definitions/category_e.py`
- `metrics/definitions/category_f.py`
- `metrics/definitions/category_g.py`
- `metrics/definitions/category_h.py`
- `metrics/definitions/category_i.py`
- `metrics/definitions/category_j.py`
- `metrics/calculators/category_e.py`
- `metrics/calculators/category_f.py`
- `metrics/calculators/category_g.py`
- `metrics/calculators/category_h.py`
- `metrics/calculators/category_i.py`
- `metrics/calculators/category_j.py`

**Files Modified (4)**:
- `metrics/definitions/__init__.py` - Import new category modules
- `metrics/calculators/__init__.py` - Import new calculator classes
- `metrics/engine.py` - Add new calculators to engine
- `cli.py` - Update category choices to include E-J

**Usage**:
```bash
# Calculate metrics for Categories E-J
python cli.py metrics calculate -c E -c F -c G -c H -c I -c J

# Calculate all metrics (A-J)
python cli.py metrics calculate

# List Category E metrics
python cli.py metrics list -c E
```

**Categories Implemented**:
- [x] Category E: Conversation Analysis (D110-D136) - Message patterns, topic analysis, thinking
- [x] Category F: Thinking & Complexity (D137-D142) - Thinking trends, compaction, complexity
- [x] Category G: Task Management (D143-D158) - Todo completion, planning metrics
- [x] Category H: Agent & Delegation (D159-D172) - Subagent usage, agent efficiency
- [x] Category I: Project Metrics (D173-D188) - Project activity, git activity
- [x] Category J: Error & Recovery (D189-D203) - Error rates, recovery patterns

**Total Metrics Implemented**: 203 (109 from A-D + 94 from E-J)

---

## Phase 4 - HTML Dashboard [COMPLETED]

**Goal**: Build interactive HTML dashboard using Plotly.js and Jinja2

**Status**: All deliverables completed on 2024-12-14

**Deliverables**:
1. [x] `visualizations/html/__init__.py` - HTML module exports
2. [x] `visualizations/html/charts/` - Plotly chart wrappers (6 chart types)
3. [x] `visualizations/html/templates/` - Jinja2 templates (base.html, dashboard.html)
4. [x] `visualizations/html/generator.py` - DashboardGenerator class
5. [x] CLI integration with `--format html` option

**Files Created (10 total)**:
- `visualizations/html/__init__.py`
- `visualizations/html/charts/__init__.py`
- `visualizations/html/charts/base.py`
- `visualizations/html/charts/line.py`
- `visualizations/html/charts/bar.py`
- `visualizations/html/charts/pie.py`
- `visualizations/html/charts/gauge.py`
- `visualizations/html/charts/heatmap.py`
- `visualizations/html/charts/scatter.py`
- `visualizations/html/generator.py`
- `visualizations/html/templates/base.html`
- `visualizations/html/templates/dashboard.html`

**Files Modified (2)**:
- `cli.py` - Added `--format html` and `--output` options to `metrics report`
- `requirements.txt` - Added jinja2 dependency

**Usage**:
```bash
# Generate HTML dashboard
python cli.py metrics report --format html

# Specify output file
python cli.py metrics report --format html --output report.html

# Specify time window
python cli.py metrics report --format html --days 7
```

**Chart Types Implemented**:
- [x] LineChart / AreaChart - Time series, trends
- [x] BarChart / StackedBarChart - Distributions, comparisons
- [x] PieChart / DonutChart - Proportions
- [x] GaugeChart / NumberIndicator - KPIs, ratios
- [x] HeatmapChart / CalendarHeatmap - 2D distributions
- [x] ScatterChart / BubbleChart - Correlations

**Dashboard Sections**:
- [x] Key Metrics Summary (sessions, messages, tools, cost)
- [x] Activity Patterns (daily trend, hourly distribution)
- [x] Tool Usage (distribution pie, trend line)
- [x] File Operations (type distribution, read/edit chart)
- [x] Model Usage (distribution pie, token bar)
- [x] Cost Analysis (trend line, cost by model)

---

## Phase 3 - Terminal Visualization [COMPLETED]

**Goal**: Build terminal visualization components using Rich library

**Status**: All deliverables completed on 2024-12-14

**Deliverables**:
1. [x] `visualizations/__init__.py` - Package init
2. [x] `visualizations/terminal/__init__.py` - Terminal module exports
3. [x] `visualizations/terminal/themes.py` - Color themes (default, mono, dark)
4. [x] `visualizations/terminal/components.py` - Visualization building blocks
5. [x] `visualizations/terminal/report.py` - TerminalReport generator
6. [x] CLI integration with `metrics report` command

**Files Created (5 total)**:
- `visualizations/__init__.py`
- `visualizations/terminal/__init__.py`
- `visualizations/terminal/themes.py`
- `visualizations/terminal/components.py`
- `visualizations/terminal/report.py`

**Files Modified (1)**:
- `cli.py` - Added `metrics report` command

**Usage**:
```bash
# Generate visual report
python cli.py metrics report

# Specify time window
python cli.py metrics report --days 7

# Use different theme
python cli.py metrics report --theme dark

# Show detailed metrics by category
python cli.py metrics report --detail
```

**Components Implemented**:
- [x] Sparklines (trend visualization)
- [x] Bar charts (horizontal bar charts for distributions)
- [x] Progress bars (ratio/completion visualization)
- [x] Gauges (KPI visualization with thresholds)
- [x] Metric panels (grouped metrics display)
- [x] Distribution tables (category breakdowns)
- [x] Trend indicators (change indicators)
- [x] Summary rows (key metrics at a glance)
- [x] Formatting utilities (duration, currency, numbers, percentages)

---

## Phase 1 - Foundation Infrastructure [COMPLETED]

**Goal**: Build the extraction layer, metric definitions, and calculation engine for Categories A-D (109 metrics)

**Status**: All deliverables completed on 2024-12-14

**Deliverables**:
1. [x] `extraction/` package with TimeFilteredExtractor and data classes
2. [x] `metrics/definitions/` package with MetricDefinition, MetricValue, and A-D definitions
3. [x] `metrics/calculators/` package with calculation engine and A-D calculators
4. [x] CLI integration with `metrics calculate` command

**Files Created (20 total)**:
- `extraction/__init__.py`
- `extraction/data_classes.py`
- `extraction/time_filtered.py`
- `metrics/__init__.py`
- `metrics/definitions/__init__.py`
- `metrics/definitions/base.py`
- `metrics/definitions/category_a.py`
- `metrics/definitions/category_b.py`
- `metrics/definitions/category_c.py`
- `metrics/definitions/category_d.py`
- `metrics/calculators/__init__.py`
- `metrics/calculators/base.py`
- `metrics/calculators/helpers.py`
- `metrics/calculators/category_a.py`
- `metrics/calculators/category_b.py`
- `metrics/calculators/category_c.py`
- `metrics/calculators/category_d.py`
- `metrics/engine.py`

**Files Modified (2)**:
- `utils.py` - Added time window helpers
- `cli.py` - Added `metrics calculate` and `metrics list` commands

**Usage**:
```bash
# Calculate all metrics for past 30 days
python cli.py metrics calculate

# Calculate specific categories
python cli.py metrics calculate -c A -c B

# Save results to JSON
python cli.py metrics calculate --output results.json

# List available metrics
python cli.py metrics list
python cli.py metrics list -c A
```

---

## Documentation Requirements

**After completing each implementation phase:**

1. Mark completed items in this plan document with `[x]` and add completion status
2. Update `README.md` with:
   - New CLI commands and usage examples
   - Updated project structure if new packages were added
   - Updated roadmap status
3. Use clear, technical language without emojis or marketing speak
4. Include concrete code examples that can be copy-pasted
5. Keep descriptions factual and concise

---

## Implementation Order (17 files total)

### Step 1: Data Classes & Extraction (4 files) [COMPLETED]
- [x] `extraction/__init__.py`
- [x] `extraction/data_classes.py` - ExtractedData30Day and supporting dataclasses
- [x] `extraction/time_filtered.py` - TimeFilteredExtractor class
- [x] Update `utils.py` - Add time window helpers

### Step 2: Metric Definitions (7 files) [COMPLETED]
- [x] `metrics/__init__.py`
- [x] `metrics/definitions/__init__.py`
- [x] `metrics/definitions/base.py` - MetricDefinition, MetricValue dataclasses
- [x] `metrics/definitions/category_a.py` - D001-D028 definitions (28 metrics)
- [x] `metrics/definitions/category_b.py` - D029-D048 definitions (20 metrics)
- [x] `metrics/definitions/category_c.py` - D049-D073 definitions (25 metrics)
- [x] `metrics/definitions/category_d.py` - D074-D109 definitions (36 metrics)

### Step 3: Calculation Engine (8 files) [COMPLETED]
- [x] `metrics/calculators/__init__.py`
- [x] `metrics/calculators/base.py` - BaseCalculator abstract class
- [x] `metrics/calculators/helpers.py` - Statistical utilities (mean, median, std, trend)
- [x] `metrics/calculators/category_a.py` - Time & productivity calculators
- [x] `metrics/calculators/category_b.py` - Tool usage calculators
- [x] `metrics/calculators/category_c.py` - File operation calculators
- [x] `metrics/calculators/category_d.py` - Model & token calculators
- [x] `metrics/engine.py` - DerivedMetricsEngine orchestrator

### Step 4: CLI Integration (1 file) [COMPLETED]
- [x] Update `cli.py` - Add `metrics` command group

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Data Extraction Layer](#2-data-extraction-layer)
3. [Derived Metrics Engine](#3-derived-metrics-engine)
4. [Visualization System](#4-visualization-system)
5. [Implementation Phases](#5-implementation-phases)
6. [File Structure](#6-file-structure)
7. [Category-by-Category Implementation](#7-category-by-category-implementation)
8. [Testing Strategy](#8-testing-strategy)
9. [Dependencies](#9-dependencies)

---

## 1. Architecture Overview

### System Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                     DERIVED METRICS PIPELINE                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐  │
│  │ Raw Data     │    │ Derived      │    │ Visualization        │  │
│  │ Extraction   │───▶│ Metrics      │───▶│ Generation           │  │
│  │ (30 days)    │    │ Engine       │    │ (Terminal + HTML)    │  │
│  └──────────────┘    └──────────────┘    └──────────────────────┘  │
│         │                   │                      │                │
│         ▼                   ▼                      ▼                │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────────────┐  │
│  │ 22 Sources   │    │ 592 Metrics  │    │ Rich Text Output     │  │
│  │ - sessions   │    │ - Category A │    │ HTML Dashboard       │  │
│  │ - stats_cache│    │ - Category B │    │ - Interactive Charts │  │
│  │ - sqlite_store│   │ - ...        │    │ - Gauges & Trends    │  │
│  │ - history    │    │ - Category BB│    │ - Network Graphs     │  │
│  │ - todos      │    │              │    │                      │  │
│  │ - plans      │    │ 18 Data Types│    │ 7 Chart Types        │  │
│  │ - ...        │    │              │    │                      │  │
│  └──────────────┘    └──────────────┘    └──────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Data Types to Visualization Mapping

| Data Type | Count | Primary Visualization | Secondary |
|-----------|-------|----------------------|-----------|
| `ratio` | ~180 | Gauge, Progress Bar | Trend Line |
| `int` | ~120 | Bar Chart, Counter | Sparkline |
| `float` | ~80 | Line Chart, Gauge | Table |
| `distribution` | ~50 | Pie/Donut, Treemap | Stacked Bar |
| `duration` | ~40 | Timeline, Bar | Histogram |
| `rate` | ~30 | Line Chart, Gauge | Area Chart |
| `trend` | ~25 | Line + Slope | Arrow Indicator |
| `compound` | ~25 | Radar Chart | Multi-Gauge |
| `correlation` | ~15 | Scatter Plot | Heatmap |
| `category` | ~15 | Label, Badge | Pie Chart |
| `probability` | ~10 | Gauge (0-100%) | Progress |
| `percentage` | ~8 | Gauge, Progress | Pie Slice |
| `binary` | ~7 | Indicator (✓/✗) | Status Badge |
| `timestamp` | ~5 | Timeline Marker | Date Label |
| `sequence` | ~5 | Flow Chart | Sankey |
| `delta` | ~8 | Delta Indicator (↑↓) | Bar Delta |
| `inverse` | ~6 | Inverted Gauge | Bar (reversed) |
| `lag` | ~3 | Timeline Arrow | Duration Bar |

---

## 2. Data Extraction Layer

### 2.1 Time-Filtered Extraction

**Objective**: Extract only data from the last 30 days for efficient processing.

```python
# Core time filter logic
from datetime import datetime, timedelta

WINDOW_DAYS = 30
cutoff_date = datetime.now() - timedelta(days=WINDOW_DAYS)
cutoff_iso = cutoff_date.isoformat()
cutoff_unix_ms = int(cutoff_date.timestamp() * 1000)
```

### 2.2 Source-by-Source Extraction Checklist

#### Primary Time-Series Sources (Critical)

- [ ] **Sessions** (`~/.claude/projects/*/*.jsonl`)
  - Filter: `start_time >= cutoff_iso`
  - Extract: All messages, tool calls, tokens, costs per session
  - Fields: `session_id`, `start_time`, `end_time`, `duration_ms`, `cost_usd`, `messages[]`

- [ ] **Stats Cache** (`~/.claude/stats-cache.json`)
  - Filter: `dailyActivity[].date >= cutoff_date`
  - Extract: Daily aggregates, model usage, hourly counts
  - Fields: `dailyActivity[]`, `modelUsage{}`, `hourCounts[]`

- [ ] **SQLite Store** (`~/.claude/__store.db`)
  - Filter: `timestamp >= cutoff_unix_ms` in `assistant_messages`
  - Extract: Message metadata, costs, model usage
  - Tables: `base_messages`, `assistant_messages`

- [ ] **History** (`~/.claude/history.jsonl`)
  - Filter: `timestamp >= cutoff_unix_ms`
  - Extract: User input patterns, projects, timestamps
  - Fields: `timestamp`, `project`, `display`, `pastedContents`

#### Secondary Sources (Supporting Data)

- [ ] **Todos** (`~/.claude/todos/*.json`)
  - Filter: Linked to sessions in 30-day window
  - Extract: Task completion rates, priorities
  - Fields: `content`, `status`, `priority`, `session_id`

- [ ] **Plans** (`~/.claude/plans/*.md`)
  - Filter: `modified_at >= cutoff_date`
  - Extract: Plan metrics, completion rates
  - Fields: `title`, `checklist_total`, `checklist_checked`

- [ ] **Debug Logs** (`~/.claude/debug/*.txt`)
  - Filter: Files modified in last 30 days
  - Extract: Error counts, warning counts
  - Fields: `session_id`, `error_count`, `warning_count`

- [ ] **File History** (`~/.claude/file-history/`)
  - Filter: Sessions in 30-day window
  - Extract: File versions, churn metrics
  - Fields: `session_id`, `hash`, `version_count`

#### Static/Config Sources (Context Data)

- [ ] **Global State** (`~/.claude.json`) - Latest state only
- [ ] **Settings** (`~/.claude/settings.json`) - Current config
- [ ] **Credentials** (`~/.claude/.credentials.json`) - Subscription info
- [ ] **Extensions** (`~/.claude/{agents,commands,skills}/`) - Customization counts
- [ ] **Project Config** (`<project>/.claude/`) - Project customizations
- [ ] **CLAUDE.md** (`<project>/CLAUDE.md`) - File presence/size
- [ ] **MCP Config** (`<project>/.mcp.json`) - Server configurations
- [ ] **MCP Logs** (`~/.cache/claude-cli-nodejs/`) - Server activity
- [ ] **Environment** (Process env) - Runtime variables
- [ ] **Cache** (`~/.cache/claude/`) - Cache size/counts
- [ ] **Versions** (`~/.local/share/claude/versions/`) - Installed versions
- [ ] **Shell Snapshots** (`~/.claude/shell-snapshots/`) - Snapshot counts
- [ ] **Session Env** (`~/.claude/session-env/`) - Environment data
- [ ] **Statusline** (Runtime) - Schema documentation only

### 2.3 Extracted Data Schema

```python
@dataclass
class ExtractedData30Day:
    """All raw data extracted for 30-day window."""
    window_start: datetime
    window_end: datetime
    sessions: List[SessionData]
    daily_activity: List[DailyActivity]
    hourly_distribution: Dict[int, int]
    messages: List[MessageData]
    tool_calls: List[ToolCallData]
    history_entries: List[HistoryEntry]
    todos: List[TodoData]
    plans: List[PlanData]
    debug_logs: List[DebugLogData]
    file_history: List[FileHistoryData]
    global_state: GlobalStateData
    settings: SettingsData
    credentials: CredentialsData
    extensions: ExtensionsData
    project_configs: List[ProjectConfigData]
    mcp_configs: List[McpConfigData]
    environment: EnvironmentData
    model_usage: Dict[str, ModelUsageData]
    project_summaries: Dict[str, ProjectSummary]
```

---

## 3. Derived Metrics Engine

### 3.1 Metric Definition Schema

```python
@dataclass
class MetricDefinition:
    """Definition of a single derived metric."""
    id: str                    # e.g., "D001"
    name: str                  # e.g., "daily_active_hours"
    category: str              # e.g., "A"
    data_type: str             # e.g., "duration"
    calculation: str           # Description of calculation
    sources: List[str]         # Required data sources
    dependencies: List[str]    # Other metrics this depends on
    visualization: str         # Recommended viz type
    unit: Optional[str]        # e.g., "hours", "USD", "%"

@dataclass
class MetricValue:
    """Calculated value for a metric."""
    metric_id: str
    value: Any
    timestamp: datetime
    window_days: int
    breakdown: Optional[Dict]
    trend: Optional[float]
```

### 3.2 Category Implementation Checklist

#### Category A: Time & Activity (D001-D028) - 28 metrics

- [ ] **D001** `daily_active_hours` - `duration` - Hours active today
- [ ] **D002** `weekly_active_hours` - `duration` - Hours active this week
- [ ] **D003** `monthly_active_hours` - `duration` - Hours active this month
- [ ] **D004** `total_thinking_time` - `duration` - Sum of extended thinking
- [ ] **D005** `avg_response_time` - `duration` - Avg time between user msg and response
- [ ] **D006** `longest_session_duration` - `duration` - Max session length
- [ ] **D007** `avg_session_duration` - `duration` - Mean session length
- [ ] **D008** `median_session_duration` - `duration` - Median session length
- [ ] **D009** `total_api_time` - `duration` - Total API call time
- [ ] **D010** `avg_tool_execution_time` - `duration` - Mean tool call duration
- [ ] **D011** `peak_activity_hour` - `category` - Most active hour (0-23)
- [ ] **D012** `peak_productivity_day` - `category` - Most productive weekday
- [ ] **D013** `morning_activity_ratio` - `ratio` - 6AM-12PM / total
- [ ] **D014** `afternoon_activity_ratio` - `ratio` - 12PM-6PM / total
- [ ] **D015** `evening_activity_ratio` - `ratio` - 6PM-12AM / total
- [ ] **D016** `night_activity_ratio` - `ratio` - 12AM-6AM / total
- [ ] **D017** `weekday_vs_weekend_ratio` - `ratio` - Weekday / weekend activity
- [ ] **D018** `session_start_time_variance` - `float` - Variance in start times
- [ ] **D019** `session_start_time_distribution` - `distribution` - Start time histogram
- [ ] **D020** `session_end_time_distribution` - `distribution` - End time histogram
- [ ] **D021** `longest_activity_streak` - `int` - Consecutive active days
- [ ] **D022** `current_activity_streak` - `int` - Current streak
- [ ] **D023** `weekly_active_days` - `int` - Days active this week
- [ ] **D024** `monthly_active_days` - `int` - Days active this month
- [ ] **D025** `avg_sessions_per_active_day` - `float` - Sessions / active days
- [ ] **D026** `session_frequency` - `rate` - Sessions per day
- [ ] **D027** `inter_session_gap` - `duration` - Avg time between sessions
- [ ] **D028** `activity_density` - `rate` - Messages per active hour

#### Category B: Tool Usage (D029-D048) - 20 metrics

- [ ] **D029** `tool_usage_distribution` - `distribution` - Breakdown by tool
- [ ] **D030** `most_used_tool` - `category` - Tool with highest count
- [ ] **D031** `tool_diversity_index` - `float` - Shannon entropy of tool usage
- [ ] **D032** `tool_calls_per_hour` - `rate` - Tool calls / active hour
- [ ] **D033** `tool_calls_per_session` - `float` - Avg tools per session
- [ ] **D034** `tool_calls_per_message` - `float` - Avg tools per message
- [ ] **D035** `bash_to_edit_ratio` - `ratio` - Bash calls / Edit calls
- [ ] **D036** `daily_tool_call_trend` - `trend` - Slope of daily tool usage
- [ ] **D037** `tool_success_rate` - `ratio` - Successful / total tool calls
- [ ] **D038** `bash_error_rate` - `ratio` - Failed Bash / total Bash
- [ ] **D039** `edit_success_rate` - `ratio` - Successful Edit / total Edit
- [ ] **D040** `avg_tool_execution_time` - `duration` - Mean tool duration
- [ ] **D041** `tool_timeout_rate` - `ratio` - Timed out / total
- [ ] **D042** `longest_tool_execution` - `duration` - Max tool duration
- [ ] **D043** `tool_retry_rate` - `ratio` - Retried / total
- [ ] **D044** `read_before_edit_ratio` - `ratio` - Read→Edit patterns
- [ ] **D045** `glob_before_read_ratio` - `ratio` - Glob→Read patterns
- [ ] **D046** `grep_then_read_pattern` - `sequence` - Grep→Read sequences
- [ ] **D047** `tool_sequence_patterns` - `distribution` - Common tool chains
- [ ] **D048** `tool_co_occurrence` - `distribution` - Tools used together

#### Category C: File Operations (D049-D073) - 25 metrics

- [ ] **D049** `unique_files_read` - `int` - Distinct files read
- [ ] **D050** `unique_files_edited` - `int` - Distinct files edited
- [ ] **D051** `file_read_frequency` - `distribution` - Reads per file
- [ ] **D052** `file_edit_frequency` - `distribution` - Edits per file
- [ ] **D053** `most_read_file` - `category` - File with most reads
- [ ] **D054** `most_edited_file` - `category` - File with most edits
- [ ] **D055** `read_to_write_ratio` - `ratio` - Reads / writes
- [ ] **D056** `new_file_creation_rate` - `rate` - New files / session
- [ ] **D057** `file_deletion_rate` - `rate` - Deleted files / session
- [ ] **D058** `file_type_distribution` - `distribution` - By extension
- [ ] **D059** `python_file_ratio` - `ratio` - .py files / total
- [ ] **D060** `javascript_file_ratio` - `ratio` - .js/.ts files / total
- [ ] **D061** `markdown_file_ratio` - `ratio` - .md files / total
- [ ] **D062** `config_file_ratio` - `ratio` - Config files / total
- [ ] **D063** `test_file_ratio` - `ratio` - Test files / total
- [ ] **D064** `avg_file_size_read` - `float` - Mean size of read files
- [ ] **D065** `file_versions_created` - `int` - Total version backups
- [ ] **D066** `avg_versions_per_file` - `float` - Versions / unique file
- [ ] **D067** `max_versions_per_file` - `int` - Max versions for any file
- [ ] **D068** `file_churn_rate` - `rate` - Edits / day
- [ ] **D069** `file_stability_index` - `inverse` - 1 / churn rate
- [ ] **D070** `directory_depth_distribution` - `distribution` - Path depths
- [ ] **D071** `files_modified_together` - `distribution` - Co-modification
- [ ] **D072** `file_dependency_graph` - `compound` - File relationships
- [ ] **D073** `cross_directory_edits` - `ratio` - Multi-dir sessions

#### Category D: Model & Token Metrics (D074-D109) - 36 metrics

- [ ] **D074** `model_usage_distribution` - `distribution` - By model
- [ ] **D075** `opus_usage_ratio` - `ratio` - Opus / total
- [ ] **D076** `sonnet_usage_ratio` - `ratio` - Sonnet / total
- [ ] **D077** `haiku_usage_ratio` - `ratio` - Haiku / total
- [ ] **D078** `model_switching_frequency` - `rate` - Switches / session
- [ ] **D079** `primary_model` - `category` - Most used model
- [ ] **D080** `model_usage_by_subagent` - `distribution` - Model per agent type
- [ ] **D081** `tokens_per_message` - `float` - Avg tokens / message
- [ ] **D082** `tokens_per_session` - `float` - Avg tokens / session
- [ ] **D083** `input_output_token_ratio` - `ratio` - Input / output
- [ ] **D084** `total_input_tokens` - `int` - Sum input tokens
- [ ] **D085** `total_output_tokens` - `int` - Sum output tokens
- [ ] **D086** `daily_token_consumption` - `rate` - Tokens / day
- [ ] **D087** `weekly_token_consumption` - `rate` - Tokens / week
- [ ] **D088** `token_growth_rate` - `trend` - Token usage slope
- [ ] **D089** `cache_hit_ratio` - `ratio` - Cache read / total input
- [ ] **D090** `cache_efficiency_score` - `compound` - Cache utilization
- [ ] **D091** `cache_read_tokens` - `int` - Total cache tokens
- [ ] **D092** `effective_input_tokens` - `int` - Input - cache
- [ ] **D093** `cache_savings_usd` - `float` - Estimated savings
- [ ] **D094** `total_cost_usd` - `float` - Total API cost
- [ ] **D095** `daily_cost_usd` - `float` - Cost today
- [ ] **D096** `weekly_cost_usd` - `float` - Cost this week
- [ ] **D097** `monthly_cost_usd` - `float` - Cost this month
- [ ] **D098** `cost_per_session` - `float` - Avg cost / session
- [ ] **D099** `cost_per_message` - `float` - Avg cost / message
- [ ] **D100** `cost_per_tool_call` - `float` - Avg cost / tool
- [ ] **D101** `model_cost_distribution` - `distribution` - Cost by model
- [ ] **D102** `cost_trend` - `trend` - Daily cost slope
- [ ] **D103-D109** Additional token/message metrics

#### Categories E-BB: Extended Metrics (D110-D592) - 483 metrics

*Complete definitions in DERIVED_METRICS_CATALOG.md*

| Category | Range | Count | Focus Area |
|----------|-------|-------|------------|
| E | D110-D136 | 27 | Conversation Analysis |
| F | D137-D142 | 6 | Thinking & Complexity |
| G | D143-D158 | 16 | Task Management |
| H | D159-D172 | 14 | Agent & Delegation |
| I | D173-D188 | 16 | Project Metrics |
| J | D189-D203 | 15 | Error & Recovery |
| K | D204-D228 | 25 | Code Generation |
| L | D229-D238 | 10 | Web Research |
| M | D239-D252 | 14 | Hooks & Customization |
| N | D253-D259 | 7 | MCP Metrics |
| O | D260-D300 | 41 | Advanced Derived (productivity, quality, behavioral) |
| P | D301-D343 | 43 | Global State & Project |
| Q-Z | D344-D442 | 99 | Feature adoption, correlations, economics |
| AA-BB | D443-D592 | 150 | Behavioral, psychological, phenomenological |

### 3.3 Calculation Engine Architecture

```python
class DerivedMetricsEngine:
    """Engine for calculating all 592 derived metrics."""

    def __init__(self, extracted_data: ExtractedData30Day):
        self.data = extracted_data
        self.cache = {}  # Cache calculated metrics for dependencies

    def calculate_all(self) -> Dict[str, MetricValue]:
        """Calculate all metrics in dependency order."""
        results = {}

        # Phase 1: Foundational metrics (no dependencies)
        for category in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            results.update(self._calculate_category(category))

        # Phase 2: Derived metrics (depend on Phase 1)
        for category in ['L', 'M', 'N', 'O']:
            results.update(self._calculate_category(category))

        # Phase 3: Advanced metrics (depend on Phases 1-2)
        for category in ['P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            results.update(self._calculate_category(category))

        # Phase 4: Meta metrics (depend on all previous)
        for category in ['AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI',
                         'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR',
                         'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB']:
            results.update(self._calculate_category(category))

        return results
```

---

## 4. Visualization System

### 4.1 Terminal Visualization (Rich Library) [COMPLETED]

#### Components Checklist

- [x] **Summary Table** - Key metrics overview
- [x] **Sparklines** - Trend indicators (▁▂▃▄▅▆▇█)
- [x] **Progress Bars** - Ratio/completion metrics
- [x] **Bar Charts** - Distribution visualization
- [x] **Panels** - Category groupings
- [ ] **Trees** - Hierarchical data (deferred to future phase)
- [x] **Status Indicators** - Binary/category metrics (via gauges)

#### Terminal Output Example

```
╭─────────────────────────────────────────────────────────────────────╮
│                   CLAUDE CODE METRICS - 30 DAY REPORT               │
│                        2024-10-15 → 2024-11-14                      │
╰─────────────────────────────────────────────────────────────────────╯

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        KEY METRICS SUMMARY                          ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

  Activity                     │ Cost                        │ Quality
  ─────────────────────────────┼─────────────────────────────┼─────────
  Sessions: 145                │ Total: $45.67               │ Error Rate: 2.3%
  Messages: 3,847              │ Daily Avg: $1.52            │ Success: 97.7%
  Tool Calls: 12,456           │ Per Session: $0.31          │ Recovery: 94.1%
  Active Hours: 89.3           │ Trend: ↓ -5.2%              │ Completion: 87.3%

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        ACTIVITY TRENDS (30 days)                    ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

  Daily Messages   ▁▂▃▅▇█▆▄▃▂▁▂▄▅▆▇█▇▆▅▄▃▂▁▂▃▄▅▆▇▆
  Daily Sessions   ▁▁▂▃▄▄▃▂▁▁▂▃▄▅▄▃▂▂▃▄▅▄▃▂▁▂▃▄▄▃
  Daily Cost       ▂▃▄▅▆▇█▇▆▅▄▃▂▃▄▅▆▇▇▆▅▄▃▂▂▃▄▅▆▅

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                        TOOL USAGE DISTRIBUTION                      ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

  Read          ████████████████████████████████████ 4,521 (36.3%)
  Bash          ██████████████████████████           3,245 (26.1%)
  Edit          █████████████████████                2,678 (21.5%)
  Glob          ████████                               987 (7.9%)
  Grep          ██████                                 756 (6.1%)
  Other         ██                                     269 (2.2%)
```

### 4.2 HTML Visualization (Plotly + Jinja2) [IMPLEMENTED]

#### Chart Types Checklist

- [x] **Line Charts** - Time series, trends
- [x] **Area Charts** - Cumulative metrics, stacked breakdowns
- [x] **Bar Charts** - Distributions, comparisons
- [x] **Pie/Donut Charts** - Proportions, breakdowns
- [x] **Scatter Plots** - Correlations, relationships
- [x] **Heatmaps** - 2D distributions, hourly patterns
- [x] **Gauges** - KPIs, ratios, completion rates
- [ ] **Radar Charts** - Multi-dimensional comparisons (future)
- [ ] **Treemaps** - Hierarchical breakdowns (future)
- [ ] **Sankey Diagrams** - Flow visualization (future)
- [ ] **Network Graphs** - Relationships, dependencies (future)
- [x] **Calendar Heatmaps** - Daily activity patterns
- [ ] **Histograms** - Value distributions (future)
- [ ] **Box Plots** - Statistical summaries (future)
- [ ] **Funnel Charts** - Conversion flows (future)

#### Dashboard Sections

```html
<div class="dashboard">
  <!-- Section 1: Executive Summary -->
  <section id="summary">
    <div class="metric-card">Total Sessions</div>
    <div class="metric-card">Total Cost</div>
    <div class="metric-card">Success Rate</div>
    <div class="metric-card">Productivity Score</div>
  </section>

  <!-- Section 2: Activity Over Time -->
  <section id="activity">
    <div class="chart" id="daily-activity"><!-- Line chart --></div>
    <div class="chart" id="hourly-heatmap"><!-- Heatmap --></div>
    <div class="chart" id="calendar-view"><!-- Calendar --></div>
  </section>

  <!-- Section 3: Tool Analysis -->
  <section id="tools">
    <div class="chart" id="tool-distribution"><!-- Bar chart --></div>
    <div class="chart" id="tool-trends"><!-- Line chart --></div>
    <div class="chart" id="tool-success"><!-- Gauge --></div>
  </section>

  <!-- Section 4: Model & Cost -->
  <section id="models">
    <div class="chart" id="model-pie"><!-- Pie chart --></div>
    <div class="chart" id="token-trend"><!-- Area chart --></div>
    <div class="chart" id="cost-breakdown"><!-- Stacked bar --></div>
  </section>

  <!-- Section 5: Quality Metrics -->
  <section id="quality">
    <div class="chart" id="error-rates"><!-- Multi-gauge --></div>
    <div class="chart" id="completion-funnel"><!-- Funnel --></div>
    <div class="chart" id="recovery-trend"><!-- Line chart --></div>
  </section>

  <!-- Section 6: Project Analysis -->
  <section id="projects">
    <div class="chart" id="project-treemap"><!-- Treemap --></div>
    <div class="chart" id="project-scatter"><!-- Scatter --></div>
  </section>

  <!-- Section 7: Advanced Insights -->
  <section id="advanced">
    <div class="chart" id="productivity-score"><!-- Gauge --></div>
    <div class="chart" id="behavioral-patterns"><!-- Heatmap --></div>
    <div class="chart" id="predictions"><!-- Line + projection --></div>
  </section>
</div>
```

### 4.3 Visualization Mapping by Category

| Category | Primary Chart | Secondary Chart | Terminal Rep |
|----------|---------------|-----------------|--------------|
| A (Time) | Line Chart | Calendar Heatmap | Sparkline |
| B (Tools) | Bar Chart | Sankey Diagram | Bar Chart |
| C (Files) | Treemap | Network Graph | Tree |
| D (Model) | Pie Chart | Stacked Area | Table |
| E (Conv) | Line Chart | Word Cloud | Stats |
| F (Think) | Line Chart | Gauge | Sparkline |
| G (Tasks) | Funnel | Progress Bars | Progress |
| H (Agent) | Bar Chart | Sankey | Table |
| I (Project) | Scatter Plot | Treemap | Table |
| J (Error) | Multi-Gauge | Line Chart | Status |
| K (Code) | Stacked Area | Histogram | Bar |
| L (Web) | Bar Chart | Network | Table |
| M (Custom) | Bar Chart | Gauge | Status |
| N-O (Adv) | Radar Chart | Correlation Matrix | Multi-stat |
| P (Global) | Dashboard | Multi-gauge | Panel |
| Q-Z | Scatter | Heatmap | Table |
| AA-BB | Radar | Trend Lines | Multi-stat |

---

## 5. Phase 1 Detailed Implementation

### 5.1 extraction/data_classes.py

```python
"""Data classes for time-filtered extraction."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional

@dataclass
class SessionData:
    """Session with messages and tool calls."""
    session_id: str
    project_path: str
    start_time: datetime
    end_time: Optional[datetime]
    duration_ms: int
    message_count: int
    tool_call_count: int
    cost_usd: float
    model: Optional[str]
    messages: List[Dict[str, Any]] = field(default_factory=list)
    tool_calls: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class DailyActivity:
    """Daily activity aggregation."""
    date: str  # YYYY-MM-DD
    session_count: int
    message_count: int
    tool_call_count: int
    cost_usd: float
    active_hours: float

@dataclass
class ToolCallData:
    """Individual tool call record."""
    tool_name: str
    timestamp: datetime
    session_id: str
    duration_ms: Optional[int]
    success: bool
    file_path: Optional[str]  # For Read/Edit/Write tools

@dataclass
class ExtractedData30Day:
    """All raw data extracted for 30-day window."""
    window_start: datetime
    window_end: datetime
    window_days: int

    # Session data
    sessions: List[SessionData] = field(default_factory=list)

    # Aggregations
    daily_activity: List[DailyActivity] = field(default_factory=list)
    hourly_distribution: Dict[int, int] = field(default_factory=dict)  # hour -> count

    # Tool data
    tool_calls: List[ToolCallData] = field(default_factory=list)
    tool_counts: Dict[str, int] = field(default_factory=dict)  # tool_name -> count

    # File data
    files_read: Dict[str, int] = field(default_factory=dict)  # path -> count
    files_edited: Dict[str, int] = field(default_factory=dict)

    # Model/token data
    model_usage: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    total_tokens: Dict[str, int] = field(default_factory=dict)  # input/output/cache

    # Totals
    total_sessions: int = 0
    total_messages: int = 0
    total_tool_calls: int = 0
    total_cost_usd: float = 0.0
```

### 5.2 extraction/time_filtered.py

```python
"""Time-filtered extractor combining multiple sources."""
from datetime import datetime, timedelta
from typing import Optional
from .data_classes import ExtractedData30Day, SessionData, DailyActivity, ToolCallData

class TimeFilteredExtractor:
    """Extract data from all sources within a time window."""

    def __init__(self, days: int = 30, include_sensitive: bool = False):
        self.days = days
        self.include_sensitive = include_sensitive
        self.cutoff = datetime.now() - timedelta(days=days)
        self.cutoff_iso = self.cutoff.isoformat()
        self.cutoff_unix_ms = int(self.cutoff.timestamp() * 1000)

    def extract(self) -> ExtractedData30Day:
        """Extract all data within the time window."""
        data = ExtractedData30Day(
            window_start=self.cutoff,
            window_end=datetime.now(),
            window_days=self.days
        )

        # Extract from each source
        self._extract_sessions(data)
        self._extract_stats_cache(data)
        self._extract_sqlite_store(data)
        self._extract_history(data)
        self._aggregate_tool_calls(data)
        self._aggregate_file_operations(data)

        return data

    def _extract_sessions(self, data: ExtractedData30Day):
        """Extract sessions from JSONL files."""
        # Use existing SessionsSource, filter by start_time >= cutoff_iso
        pass

    def _extract_stats_cache(self, data: ExtractedData30Day):
        """Extract from stats-cache.json."""
        # Filter dailyActivity by date >= cutoff
        pass

    # ... other extraction methods
```

### 5.3 metrics/definitions/base.py

```python
"""Base metric definition and value classes."""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
from enum import Enum

class MetricType(str, Enum):
    DURATION = "duration"
    RATIO = "ratio"
    INT = "int"
    FLOAT = "float"
    DISTRIBUTION = "distribution"
    RATE = "rate"
    TREND = "trend"
    CATEGORY = "category"
    COMPOUND = "compound"

@dataclass
class MetricDefinition:
    """Definition of a single derived metric."""
    id: str                              # e.g., "D001"
    name: str                            # e.g., "daily_active_hours"
    category: str                        # e.g., "A"
    metric_type: MetricType
    description: str
    calculation: str                     # How to calculate
    sources: List[str]                   # Required data sources
    dependencies: List[str] = field(default_factory=list)  # Other metric IDs
    unit: Optional[str] = None           # e.g., "hours", "USD", "%"

@dataclass
class MetricValue:
    """Calculated value for a metric."""
    metric_id: str
    value: Any
    timestamp: datetime
    window_days: int
    breakdown: Optional[Dict[str, Any]] = None  # For distributions
    trend: Optional[float] = None               # Slope if applicable

# Registry of all metric definitions
METRIC_DEFINITIONS: Dict[str, MetricDefinition] = {}

def register_metric(definition: MetricDefinition):
    """Register a metric definition."""
    METRIC_DEFINITIONS[definition.id] = definition
    return definition
```

### 5.4 metrics/definitions/category_a.py (Sample)

```python
"""Category A: Time & Productivity Metrics (D001-D028)."""
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
    unit="hours"
))

register_metric(MetricDefinition(
    id="D002",
    name="weekly_active_hours",
    category="A",
    metric_type=MetricType.DURATION,
    description="Hours active this week",
    calculation="Sum of session durations for past 7 days",
    sources=["sessions"],
    unit="hours"
))

# ... D003-D028 follow same pattern
```

### 5.5 metrics/calculators/base.py

```python
"""Base calculator class."""
from abc import ABC, abstractmethod
from typing import Dict, Any
from ..definitions.base import MetricValue, MetricDefinition
from extraction.data_classes import ExtractedData30Day

class BaseCalculator(ABC):
    """Base class for metric calculators."""

    def __init__(self, data: ExtractedData30Day, cache: Dict[str, MetricValue]):
        self.data = data
        self.cache = cache  # Access to previously calculated metrics

    @abstractmethod
    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Calculate a single metric."""
        pass

    def get_dependency(self, metric_id: str) -> Any:
        """Get a previously calculated metric value."""
        if metric_id in self.cache:
            return self.cache[metric_id].value
        raise ValueError(f"Dependency {metric_id} not calculated yet")
```

### 5.6 metrics/calculators/helpers.py

```python
"""Statistical calculation helpers."""
from typing import List, Optional, Tuple
from datetime import datetime, date
import math

def mean(values: List[float]) -> float:
    """Calculate mean of values."""
    return sum(values) / len(values) if values else 0.0

def median(values: List[float]) -> float:
    """Calculate median of values."""
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]

def std_dev(values: List[float]) -> float:
    """Calculate standard deviation."""
    if len(values) < 2:
        return 0.0
    m = mean(values)
    variance = sum((x - m) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

def linear_regression_slope(values: List[Tuple[float, float]]) -> float:
    """Calculate slope of linear regression (trend)."""
    if len(values) < 2:
        return 0.0
    n = len(values)
    sum_x = sum(x for x, _ in values)
    sum_y = sum(y for _, y in values)
    sum_xy = sum(x * y for x, y in values)
    sum_x2 = sum(x * x for x, _ in values)

    denominator = n * sum_x2 - sum_x ** 2
    if denominator == 0:
        return 0.0
    return (n * sum_xy - sum_x * sum_y) / denominator

def calculate_streak(dates: List[date], end_date: Optional[date] = None) -> int:
    """Calculate consecutive day streak ending at end_date."""
    if not dates:
        return 0
    if end_date is None:
        end_date = date.today()

    sorted_dates = sorted(set(dates), reverse=True)
    if sorted_dates[0] != end_date:
        return 0

    streak = 1
    for i in range(1, len(sorted_dates)):
        if (sorted_dates[i - 1] - sorted_dates[i]).days == 1:
            streak += 1
        else:
            break
    return streak

def shannon_entropy(distribution: Dict[str, int]) -> float:
    """Calculate Shannon entropy (diversity index)."""
    total = sum(distribution.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for count in distribution.values():
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    return entropy
```

### 5.7 metrics/calculators/category_a.py (Sample)

```python
"""Category A calculators: Time & Productivity."""
from datetime import datetime, date, timedelta
from typing import Dict
from .base import BaseCalculator
from .helpers import mean, median, std_dev, calculate_streak
from ..definitions.base import MetricValue, MetricDefinition
from extraction.data_classes import ExtractedData30Day

class CategoryACalculator(BaseCalculator):
    """Calculate Category A metrics (D001-D028)."""

    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Route to specific calculation method."""
        method_name = f"_calc_{definition.id.lower()}"
        method = getattr(self, method_name, None)
        if method is None:
            raise NotImplementedError(f"No calculator for {definition.id}")
        return method(definition)

    def _calc_d001(self, definition: MetricDefinition) -> MetricValue:
        """D001: Daily active hours."""
        today = date.today()
        hours = sum(
            s.duration_ms / 3600000
            for s in self.data.sessions
            if s.start_time.date() == today
        )
        return MetricValue(
            metric_id="D001",
            value=round(hours, 2),
            timestamp=datetime.now(),
            window_days=1
        )

    def _calc_d002(self, definition: MetricDefinition) -> MetricValue:
        """D002: Weekly active hours."""
        week_ago = date.today() - timedelta(days=7)
        hours = sum(
            s.duration_ms / 3600000
            for s in self.data.sessions
            if s.start_time.date() >= week_ago
        )
        return MetricValue(
            metric_id="D002",
            value=round(hours, 2),
            timestamp=datetime.now(),
            window_days=7
        )

    # ... D003-D028 implementations
```

### 5.8 metrics/engine.py

```python
"""Derived metrics calculation engine."""
from typing import Dict, List, Optional
from datetime import datetime
from .definitions.base import MetricDefinition, MetricValue, METRIC_DEFINITIONS
from .calculators.category_a import CategoryACalculator
from .calculators.category_b import CategoryBCalculator
from .calculators.category_c import CategoryCCalculator
from .calculators.category_d import CategoryDCalculator
from extraction.data_classes import ExtractedData30Day

class DerivedMetricsEngine:
    """Engine for calculating all derived metrics."""

    CALCULATORS = {
        'A': CategoryACalculator,
        'B': CategoryBCalculator,
        'C': CategoryCCalculator,
        'D': CategoryDCalculator,
    }

    def __init__(self, data: ExtractedData30Day):
        self.data = data
        self.cache: Dict[str, MetricValue] = {}

    def calculate_all(self, categories: Optional[List[str]] = None) -> Dict[str, MetricValue]:
        """Calculate all metrics (or filtered by category)."""
        if categories is None:
            categories = list(self.CALCULATORS.keys())

        for category in categories:
            self._calculate_category(category)

        return self.cache

    def _calculate_category(self, category: str):
        """Calculate all metrics in a category."""
        calculator_class = self.CALCULATORS.get(category)
        if not calculator_class:
            return

        calculator = calculator_class(self.data, self.cache)

        # Get all definitions for this category
        definitions = [
            d for d in METRIC_DEFINITIONS.values()
            if d.category == category
        ]

        # Sort by dependencies (topological sort)
        sorted_defs = self._topological_sort(definitions)

        for definition in sorted_defs:
            try:
                value = calculator.calculate(definition)
                self.cache[definition.id] = value
            except Exception as e:
                # Log error but continue
                print(f"Error calculating {definition.id}: {e}")

    def _topological_sort(self, definitions: List[MetricDefinition]) -> List[MetricDefinition]:
        """Sort definitions by dependencies."""
        # Simple implementation - can be optimized
        sorted_list = []
        remaining = list(definitions)

        while remaining:
            for d in remaining[:]:
                deps_satisfied = all(
                    dep in self.cache or dep not in [x.id for x in definitions]
                    for dep in d.dependencies
                )
                if deps_satisfied:
                    sorted_list.append(d)
                    remaining.remove(d)

        return sorted_list
```

### 5.9 CLI Integration (cli.py additions)

```python
@click.group()
def metrics():
    """Derived metrics commands."""
    pass

@metrics.command()
@click.option('--days', '-d', default=30, help='Time window in days')
@click.option('--categories', '-c', multiple=True, help='Filter categories (A,B,C,D)')
@click.option('--output', '-o', type=click.Path(), help='Output JSON file')
def calculate(days: int, categories: tuple, output: str):
    """Calculate derived metrics."""
    from extraction.time_filtered import TimeFilteredExtractor
    from metrics.engine import DerivedMetricsEngine

    # Extract data
    extractor = TimeFilteredExtractor(days=days)
    data = extractor.extract()

    # Calculate metrics
    engine = DerivedMetricsEngine(data)
    cat_list = list(categories) if categories else None
    results = engine.calculate_all(categories=cat_list)

    # Output
    if output:
        # Write to JSON
        pass
    else:
        # Print summary
        click.echo(f"Calculated {len(results)} metrics")
        for metric_id, value in sorted(results.items()):
            click.echo(f"  {metric_id}: {value.value}")

cli.add_command(metrics)
```

---

## Future Phases (Summary)

### Phase 5: Extended Metrics (E-J) [COMPLETED]
- Categories E-J (94 metrics) - Conversation, Thinking, Tasks, Agents, Projects, Errors
- Full calculator implementations with dependencies

### Phase 6: Extended Metrics (K-BB) [PLANNED]
- Categories K-BB (389 additional metrics)
- Code generation, web research, hooks, MCP, advanced derived metrics
- Behavioral, psychological, phenomenological metrics

### Phase 7-8: Polish
- Full testing coverage
- Documentation updates

---

## 6. File Structure

```
claude_metrics/
├── sources/                    # Existing - 22 data source extractors
│
├── metrics/                    # NEW - derived metrics
│   ├── __init__.py
│   ├── definitions/            # Metric definitions (54 files)
│   │   ├── __init__.py
│   │   ├── base.py             # MetricDefinition, MetricValue
│   │   ├── category_a.py       # D001-D028
│   │   ├── category_b.py       # D029-D048
│   │   └── ...                 # Through category_bb.py
│   │
│   ├── calculators/            # Metric calculators (54 files)
│   │   ├── __init__.py
│   │   ├── base.py             # BaseCalculator
│   │   ├── helpers.py          # Calculation utilities
│   │   ├── category_a.py       # D001-D028 calculators
│   │   └── ...                 # Through category_bb.py
│   │
│   └── engine.py               # DerivedMetricsEngine
│
├── visualizations/             # NEW - visualization system
│   ├── __init__.py
│   │
│   ├── terminal/               # Rich terminal output
│   │   ├── __init__.py
│   │   ├── components.py       # Reusable Rich components
│   │   ├── report.py           # TerminalReport class
│   │   └── themes.py           # Color themes
│   │
│   ├── html/                   # HTML dashboard
│   │   ├── __init__.py
│   │   ├── charts/             # 15 Plotly chart wrappers
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── line.py
│   │   │   ├── bar.py
│   │   │   ├── pie.py
│   │   │   ├── scatter.py
│   │   │   ├── heatmap.py
│   │   │   ├── gauge.py
│   │   │   ├── radar.py
│   │   │   ├── tree.py
│   │   │   ├── flow.py
│   │   │   └── network.py
│   │   │
│   │   ├── templates/          # Jinja2 templates
│   │   │   ├── base.html
│   │   │   ├── dashboard.html
│   │   │   ├── sections/       # 7 section templates
│   │   │   └── components/     # Reusable components
│   │   │
│   │   ├── static/             # CSS & JS
│   │   │   ├── css/
│   │   │   └── js/
│   │   │
│   │   └── generator.py        # DashboardGenerator
│   │
│   └── export/                 # Export utilities
│       ├── __init__.py
│       ├── pdf.py
│       ├── csv.py
│       └── json.py
│
├── extraction/                 # NEW - enhanced extraction
│   ├── __init__.py
│   ├── time_filtered.py        # TimeFilteredExtractor
│   └── data_classes.py         # ExtractedData30Day
│
├── cli.py                      # Updated with metrics commands
├── database.py                 # Existing
├── main.py                     # Existing
└── utils.py                    # Existing
```

---

## 7. Category-by-Category Implementation Details

### Category A: Time & Activity (D001-D028)

**Data Sources**: sessions, daily_activity, hourly_activity

**Sample Calculations**:
```python
# D001: daily_active_hours
def calc_d001(sessions):
    today = datetime.now().date()
    today_sessions = [s for s in sessions if s.start_time.date() == today]
    return sum(s.duration_ms for s in today_sessions) / 3600000

# D011: peak_activity_hour
def calc_d011(hourly):
    return max(hourly.items(), key=lambda x: x[1])[0]

# D021: longest_activity_streak
def calc_d021(daily):
    dates = sorted(d.date for d in daily if d.session_count > 0)
    max_streak = current = 1
    for i in range(1, len(dates)):
        if (dates[i] - dates[i-1]).days == 1:
            current += 1
            max_streak = max(max_streak, current)
        else:
            current = 1
    return max_streak
```

**Visualizations**:
- Line chart: Daily active hours trend
- Heatmap: Activity by hour × day of week
- Sparklines: Session frequency
- Calendar heatmap: 30-day activity

### Category D: Model & Token Metrics (D074-D109)

**Data Sources**: model_usage, messages, sessions

**Sample Calculations**:
```python
# D074: model_usage_distribution
def calc_d074(model_usage):
    total = sum(m.message_count for m in model_usage.values())
    return {model: m.message_count / total for model, m in model_usage.items()}

# D089: cache_hit_ratio
def calc_d089(messages):
    total_input = sum(m.input_tokens for m in messages)
    cache_read = sum(m.cache_read_tokens for m in messages)
    return cache_read / total_input if total_input > 0 else 0
```

**Visualizations**:
- Pie chart: Model distribution
- Stacked area: Token consumption over time
- Gauge: Cache hit ratio
- Line chart: Cost trend

### Category O: Advanced Derived (D260-D300)

**Dependencies**: Multiple Category A-N metrics

**Sample Calculations**:
```python
# D260: focus_score (compound)
def calc_d260(metrics):
    session_length = metrics['D007'].value
    error_rate = metrics['D189'].value
    completion = metrics['D145'].value
    return (
        0.4 * normalize(session_length, 0, 7200) +
        0.3 * (1 - error_rate) +
        0.3 * completion
    )

# D296: thinking_to_success_correlation
def calc_d296(sessions):
    thinking_usage = [s.thinking_ratio for s in sessions]
    success_rates = [s.success_rate for s in sessions]
    return pearson_correlation(thinking_usage, success_rates)
```

**Visualizations**:
- Radar chart: Multi-dimensional productivity
- Correlation heatmap: Metric relationships
- Gauge: Focus score

---

## 8. Testing Strategy

### Unit Tests
```python
def test_d001_daily_active_hours():
    sessions = [
        Session(start_time=today_9am, duration_ms=3600000),
        Session(start_time=today_2pm, duration_ms=7200000),
    ]
    result = calc_d001(sessions)
    assert result == 3.0

def test_d021_longest_streak():
    daily = [
        DailyActivity(date=date(2024, 11, 1), session_count=2),
        DailyActivity(date=date(2024, 11, 2), session_count=1),
        DailyActivity(date=date(2024, 11, 3), session_count=3),
        DailyActivity(date=date(2024, 11, 5), session_count=1),  # gap
    ]
    result = calc_d021(daily)
    assert result == 3
```

### Integration Tests
```python
def test_full_pipeline():
    extractor = TimeFilteredExtractor(days=30)
    data = extractor.extract_all()
    engine = DerivedMetricsEngine(data)
    metrics = engine.calculate_all()
    assert len(metrics) == 592
```

---

## 9. Dependencies

### Required Packages (add to requirements.txt)

```
# Visualization
plotly>=5.18.0          # Interactive charts
jinja2>=3.1.0           # HTML templates
pandas>=2.0.0           # Data manipulation

# Statistics
scipy>=1.11.0           # Statistical calculations
numpy>=1.24.0           # Numerical operations

# Network graphs (optional)
networkx>=3.2           # Graph analysis
pyvis>=0.3.2            # Interactive network viz

# Export (optional)
weasyprint>=60.0        # PDF export
```

---

## Summary

**Total Scope**:
- 592 derived metrics across 54 categories
- 22 data sources with 30-day filtering
- 2 output formats (Rich terminal + HTML dashboard)
- 15 chart types
- 8 implementation phases (~13 weeks)

**Key Deliverables**:
- `claude-metrics metrics calculate` - Calculate all metrics
- `claude-metrics metrics report --terminal` - Terminal report
- `claude-metrics metrics report --html` - HTML dashboard
- `claude-metrics metrics report --all` - Both outputs

**Files to Create**: ~100+ new files
**Files to Modify**: cli.py, requirements.txt

---

## Next Steps

1. Review and approve this plan
2. Copy to `derived_data_visualizations_plan.md` in project root
3. Begin Phase 1: Foundation (data extraction + metric definitions)
4. Iterate through phases, testing each category
5. Final integration and documentation

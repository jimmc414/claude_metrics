# Claude Metrics

Extract, analyze, and visualize your Claude Code usage data.

## Overview

Claude Metrics is a Python tool that extracts and analyzes data from Claude Code's local storage, providing insights into:

- **Session activity** - Total sessions, messages, duration
- **Token usage** - Input/output tokens by model
- **Tool usage** - Which tools you use most
- **Cost tracking** - API costs over time
- **Project activity** - Activity per project
- **And 900+ more metrics** - See `docs/CLAUDE_CODE_METRICS_CATALOG.md`

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd claude-metrics

# Install in development mode
pip install -e .

# Or install dependencies directly
pip install -r requirements.txt
```

## Quick Start

### Raw Data Extraction

```bash
# Extract all raw data to default output directory
claude-metrics extract

# Extract specific sources only
claude-metrics extract --source stats_cache --source sessions

# Output to custom directory
claude-metrics extract --output-dir ./my_metrics

# Include sensitive data (tokens, keys) - use with caution
claude-metrics extract --include-sensitive

# List available data sources
claude-metrics sources

# View extraction summary
claude-metrics summary ./claude_metrics_output
```

### Derived Metrics

Calculate 109 derived metrics from your Claude Code usage data:

```bash
# Calculate all metrics for past 30 days
python cli.py metrics calculate

# Specify time window
python cli.py metrics calculate --days 7

# Calculate specific categories only
python cli.py metrics calculate -c A -c B

# Save results to JSON
python cli.py metrics calculate --output metrics.json

# List available metrics
python cli.py metrics list

# List metrics for a specific category
python cli.py metrics list -c A
```

### Visual Reports

Generate visual reports in terminal or HTML format:

```bash
# Generate terminal report for past 30 days
python cli.py metrics report

# Specify time window
python cli.py metrics report --days 7

# Use different color theme (default, mono, dark)
python cli.py metrics report --theme dark

# Show detailed metrics by category
python cli.py metrics report --detail
```

#### HTML Dashboard

Generate an interactive HTML dashboard with Plotly charts:

```bash
# Generate HTML dashboard
python cli.py metrics report --format html

# Specify output file
python cli.py metrics report --format html --output dashboard.html

# Specify time window
python cli.py metrics report --format html --days 7
```

The HTML dashboard includes interactive charts:
- Daily activity line charts with session and message trends
- Hourly activity distribution bar chart
- Tool usage pie chart and trend line
- File type distribution and read/edit operations
- Model usage distribution pie chart
- Token consumption bar chart
- Cost trend line and cost by model breakdown

The report includes:
- Key metrics summary with session counts, costs, and averages
- Activity patterns with sparklines and time-of-day distribution
- Tool usage breakdown with bar charts
- File operations summary
- Model usage distribution
- Cost and token metrics with cache efficiency

**Metric Categories:**

| Category | Count | Description |
|----------|-------|-------------|
| A | 28 | Time and activity patterns (session duration, active hours, streaks) |
| B | 20 | Tool usage (distribution, success rates, patterns) |
| C | 25 | File operations (read/edit frequency, file types, churn) |
| D | 36 | Model and token metrics (usage distribution, costs, cache efficiency) |

## Output

The extractor produces:

1. **JSON files** in `./claude_metrics_output/json/`
   - One file per data source
   - Human-readable format

2. **SQLite database** at `./claude_metrics_output/claude_metrics.db`
   - 18 normalized tables
   - Queryable with any SQLite client

3. **Summary file** at `./claude_metrics_output/extraction_summary.json`
   - Overview of extracted data
   - Statistics per source

## Data Sources

| Source | Description | Key Data |
|--------|-------------|----------|
| `stats_cache` | Aggregate usage statistics | Total sessions, messages, cost |
| `settings` | User settings and preferences | Theme, permissions, key bindings |
| `global_state` | Global application state | Current project, auth status |
| `credentials` | Authentication information | API key status (redacted) |
| `history` | Command history | Recent commands per project |
| `sessions` | Session transcripts | Messages, tool calls, tokens |
| `todos` | Task lists | Todo items across sessions |
| `plans` | Implementation plans | Plan files and metadata |
| `extensions` | Custom extensions | Agents, commands, skills |

## Project Structure

```
claude-metrics/
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
│
├── __init__.py          # Package init
├── cli.py               # CLI commands
├── metrics_extractor.py # Main orchestrator
├── database.py          # SQLite schema & operations
├── redaction.py         # Sensitive data handling
├── utils.py             # Utilities
│
├── sources/             # Data source extractors (22 sources)
│   ├── __init__.py
│   ├── base.py
│   ├── stats_cache.py
│   ├── settings.py
│   ├── sessions.py
│   └── ...
│
├── extraction/          # Time-filtered data extraction
│   ├── __init__.py
│   ├── data_classes.py  # SessionData, ToolCallData, etc.
│   └── time_filtered.py # TimeFilteredExtractor
│
├── metrics/             # Derived metrics system
│   ├── __init__.py
│   ├── engine.py        # DerivedMetricsEngine
│   ├── definitions/     # Metric definitions (109 metrics)
│   │   ├── base.py      # MetricDefinition, MetricValue
│   │   ├── category_a.py
│   │   ├── category_b.py
│   │   ├── category_c.py
│   │   └── category_d.py
│   └── calculators/     # Metric calculators
│       ├── base.py
│       ├── helpers.py
│       ├── category_a.py
│       ├── category_b.py
│       ├── category_c.py
│       └── category_d.py
│
├── visualizations/      # Visualization system
│   ├── __init__.py
│   ├── terminal/        # Terminal output (Rich library)
│   │   ├── __init__.py
│   │   ├── components.py  # Sparklines, bar charts, gauges
│   │   ├── report.py      # TerminalReport generator
│   │   └── themes.py      # Color themes
│   └── html/            # HTML dashboard (Plotly + Jinja2)
│       ├── __init__.py
│       ├── generator.py   # DashboardGenerator class
│       ├── charts/        # Plotly chart wrappers
│       │   ├── base.py
│       │   ├── line.py
│       │   ├── bar.py
│       │   ├── pie.py
│       │   ├── gauge.py
│       │   ├── heatmap.py
│       │   └── scatter.py
│       └── templates/     # Jinja2 HTML templates
│           ├── base.html
│           └── dashboard.html
│
├── docs/
│   ├── CLAUDE_CODE_DATA_SOURCES.md
│   ├── CLAUDE_CODE_METRICS_CATALOG.md
│   ├── DERIVED_METRICS_CATALOG.md
│   └── ...
│
└── tests/
    └── ...
```

## Roadmap

### Phase 1: Raw Data Extraction (Complete)
- 22 data source extractors
- 18 SQLite tables
- JSON + SQLite output

### Phase 2: Derived Metrics - Foundation (Complete)
- 109 derived metrics across 4 categories (A-D)
- Time-filtered extraction (configurable window)
- Calculation engine with dependency resolution
- CLI integration

### Phase 3: Terminal Visualization (Complete)
- Rich terminal output with sparklines, gauges, and tables
- Bar charts for distributions
- Metric panels and summary rows
- Three color themes (default, mono, dark)

### Phase 4: HTML Dashboard (Complete)
- Interactive HTML dashboard with Plotly.js
- Line, bar, pie, gauge, heatmap, scatter charts
- Responsive layout with dark mode support
- Jinja2 templating for customization

### Phase 2.5: Derived Metrics - Extended (Planned)
- Categories E-BB (483 additional metrics)
- Conversation analysis, task management, error recovery
- Cross-metric correlations

## Development

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=claude_metrics

# Install dev dependencies
pip install -e ".[dev]"
```

## Privacy & Security

By default, sensitive data is redacted:
- API keys → `[REDACTED_API_KEY]`
- OAuth tokens → `[REDACTED_TOKEN]`
- Passwords → `[REDACTED_PASSWORD]`

Use `--include-sensitive` only if you need the raw data and understand the risks.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Documentation

- [Data Sources](docs/CLAUDE_CODE_DATA_SOURCES.md) - Claude Code local data reference guide
- [Metrics Catalog](docs/CLAUDE_CODE_METRICS_CATALOG.md) - Raw data schemas and extractable fields
- [Derived Metrics](docs/DERIVED_METRICS_CATALOG.md) - 592 derived/computed metrics with types
- [Implementation Plan](docs/IMPLEMENTATION_PLAN.md) - Detailed project roadmap
- [Brainstorm Prompt](docs/BRAINSTORM_METRICS_PROMPT.md) - Prompt for generating new metrics

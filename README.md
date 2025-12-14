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

```bash
# Extract all metrics to default output directory
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
├── sources/             # Data source extractors
│   ├── __init__.py
│   ├── base.py
│   ├── stats_cache.py
│   ├── settings.py
│   ├── global_state.py
│   ├── credentials.py
│   ├── history.py
│   ├── sessions.py
│   ├── todos.py
│   ├── plans.py
│   └── extensions.py
│
├── docs/
│   ├── CLAUDE_CODE_DATA_SOURCES.md    # Claude Code local data reference
│   ├── CLAUDE_CODE_METRICS_CATALOG.md # Raw data schemas
│   ├── DERIVED_METRICS_CATALOG.md     # 592 derived metrics with types
│   ├── IMPLEMENTATION_PLAN.md         # Full project plan
│   └── BRAINSTORM_METRICS_PROMPT.md   # Metrics brainstorm prompt
│
└── tests/
    ├── conftest.py
    └── test_extractor.py
```

## Roadmap

### Phase 1: Raw Data Extraction (Complete)
- 9 data source extractors
- 18 SQLite tables
- JSON + SQLite output

### Phase 1.5: Data Validation (Planned)
- Cross-source consistency checks
- Data type validation
- Completeness verification

### Phase 2: Derived Metrics (Planned)
- 592 computed metrics across 54 categories
- Behavioral analysis
- Trend detection

### Phase 3: Visualizations (Planned)
- Interactive HTML dashboard
- Time-series charts
- Network graphs

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

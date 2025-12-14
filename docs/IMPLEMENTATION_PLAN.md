# Claude Metrics: Complete Implementation Plan

## Executive Summary

A 3-phase project to extract, analyze, and visualize Claude Code usage data:

| Phase | Status | Description | Est. Lines |
|-------|--------|-------------|------------|
| **Phase 1** | ✅ COMPLETE | Raw data extraction (17 files, 9 sources, 18 DB tables) | 2,500 |
| **Phase 1.5** | 📋 PLANNED | Data integrity validation & verification | 400 |
| **Phase 2** | 📋 PLANNED | Derived metrics compilation (592 metrics, 54 categories) | 3,000 |
| **Phase 3** | 📋 PLANNED | Visualizations & dashboards | 2,000 |

**Total Metrics Documented**: 914+ (322 direct + 592 derived)

---

# PHASE 1: RAW DATA EXTRACTION ✅ COMPLETE

## What Was Built

### Files Created (17 total)
```
claude-metrics/
├── __init__.py           # Package init, version 0.1.0
├── extractor.py          # Main MetricsExtractor orchestrator
├── database.py           # SQLite schema (18 tables) & writers
├── redaction.py          # Sensitive data handling
├── utils.py              # Path helpers, JSONL parsing
├── cli.py                # CLI with rich output
├── sources/
│   ├── __init__.py       # Source registry (9 sources)
│   ├── base.py           # BaseSource abstract class
│   ├── stats_cache.py    # Pre-aggregated statistics
│   ├── settings.py       # Global/local/system settings
│   ├── global_state.py   # ~/.claude.json with per-project stats
│   ├── credentials.py    # OAuth tokens (redacted by default)
│   ├── history.py        # User input history
│   ├── sessions.py       # Full conversation transcripts
│   ├── todos.py          # Task lists per session
│   ├── plans.py          # Implementation plans
│   └── extensions.py     # Agents, commands, skills, plugins
```

### Database Schema (18 tables)
- `extraction_info` - Metadata about extraction runs
- `stats_cache` - Pre-aggregated statistics
- `daily_activity` - Daily message/session/tool counts
- `hourly_activity` - Activity by hour (0-23)
- `model_usage` - Token usage per model
- `sessions` - Session summaries
- `messages` - Message metadata (not full content)
- `tool_calls` - Tool invocation records
- `history` - User input history
- `todos` - Task/todo items
- `plans` - Plan file metadata
- `projects` - Per-project statistics
- `extensions` - Agents/commands/skills
- `tips_history` - Feature discovery tracking
- `feature_flags` - Statsig gate cache
- `settings` - Configuration values
- `debug_logs` - Debug log summaries
- `file_history` - File version metadata

### CLI Commands
```bash
# List available sources
claude-metrics sources

# Extract all data
claude-metrics extract

# Extract to specific directory
claude-metrics extract --output-dir ./my-data

# Extract specific sources only
claude-metrics extract -s stats_cache -s history

# Include sensitive data (tokens, keys)
claude-metrics extract --include-sensitive

# JSON only (no SQLite)
claude-metrics extract -f json

# Show extraction summary
claude-metrics summary ./claude_metrics_output
```

### Extraction Results (Your Data)
| Source | Records |
|--------|---------|
| Sessions | 4,477 files |
| Messages | 67,155 total |
| History entries | 2,680 |
| Todos | 191 across 21 sessions |
| Plans | 44 files |
| Extensions | 27 (9 agents, 9 commands, 9 skills) |
| Projects | 44 unique |

---

# PHASE 1.5: DATA INTEGRITY VALIDATION

## Objective

Verify that Phase 1 extraction is accurate, complete, and properly parsed before building derived metrics.

---

## 1.5.1: Cross-Source Validation Checks

### Stats Cache vs Actual Data
| Check | Source A | Source B | Validation |
|-------|----------|----------|------------|
| Total sessions | `stats_cache.totalSessions` | `COUNT(*) FROM sessions` | Should match ±5% |
| Total messages | `stats_cache.totalMessages` | `COUNT(*) FROM messages` | Should match ±5% |
| First session date | `stats_cache.firstSessionDate` | `MIN(start_time) FROM sessions` | Should match |
| Daily message counts | `daily_activity.message_count` | `COUNT(*) FROM messages GROUP BY date(timestamp)` | Should match |
| Model token totals | `model_usage.input_tokens` | `SUM(input_tokens) FROM messages WHERE model=X` | Should match |

### History vs Sessions
| Check | Validation |
|-------|------------|
| History project paths | All `history.project` values should exist in `sessions.project` |
| Timestamp coverage | `history` timestamps should fall within session date ranges |
| Entry count sanity | `history` entries ≈ user message count (within 2x) |

### Session Integrity
| Check | Validation |
|-------|------------|
| Orphan messages | All `messages.session_id` should exist in `sessions.session_id` |
| Orphan tool_calls | All `tool_calls.session_id` should exist in `sessions.session_id` |
| Parent chain validity | All `messages.parent_uuid` should exist as `messages.uuid` OR be NULL |
| Timestamp ordering | Within each session: `messages.timestamp` should be monotonically increasing |

---

## 1.5.2: Data Type & Format Validation

### Timestamp Validation
```sql
-- Find invalid ISO timestamps
SELECT uuid, timestamp FROM messages
WHERE timestamp NOT GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]T*';

-- Find timestamps outside reasonable range (2024-2030)
SELECT uuid, timestamp FROM messages
WHERE timestamp < '2024-01-01' OR timestamp > '2030-01-01';
```

### Token Count Validation
```sql
-- Find suspiciously large token counts (> 1M tokens in single message)
SELECT uuid, input_tokens, output_tokens FROM messages
WHERE input_tokens > 1000000 OR output_tokens > 1000000;

-- Find negative token counts
SELECT uuid, input_tokens, output_tokens FROM messages
WHERE input_tokens < 0 OR output_tokens < 0;
```

### Duration Validation
```sql
-- Find sessions with negative or impossibly long durations
SELECT session_id, duration_ms FROM sessions
WHERE duration_ms < 0 OR duration_ms > 86400000 * 30; -- > 30 days

-- Find tool calls with impossible durations
SELECT id, duration_ms FROM tool_calls
WHERE duration_ms < 0 OR duration_ms > 3600000; -- > 1 hour
```

---

## 1.5.3: Completeness Checks

### Required Fields Present
| Table | Required Fields | Check |
|-------|-----------------|-------|
| `sessions` | session_id, project, start_time | No NULLs |
| `messages` | uuid, session_id, timestamp, type | No NULLs |
| `tool_calls` | id, tool_name | No NULLs |
| `history` | timestamp | No NULLs |

### Coverage Checks
| Check | Expected | Query |
|-------|----------|-------|
| Sessions have messages | 100% | `SELECT COUNT(*) FROM sessions WHERE session_id NOT IN (SELECT DISTINCT session_id FROM messages)` = 0 |
| Active days have activity | 100% | Cross-check `daily_activity` dates with actual message dates |
| All tool types present | 15+ tools | `SELECT COUNT(DISTINCT tool_name) FROM tool_calls` > 15 |

---

## 1.5.4: Duplicate Detection

```sql
-- Duplicate session IDs (should be 0)
SELECT session_id, COUNT(*) FROM sessions GROUP BY session_id HAVING COUNT(*) > 1;

-- Duplicate message UUIDs (should be 0)
SELECT uuid, COUNT(*) FROM messages GROUP BY uuid HAVING COUNT(*) > 1;

-- Duplicate tool call IDs (should be 0)
SELECT id, COUNT(*) FROM tool_calls GROUP BY id HAVING COUNT(*) > 1;
```

---

## 1.5.5: Semantic Validation

### Model Name Validation
```sql
-- All models should be valid Claude model IDs
SELECT DISTINCT model FROM messages
WHERE model NOT LIKE 'claude-%' AND model IS NOT NULL;
```

### Tool Name Validation
```sql
-- Known tool names
SELECT DISTINCT tool_name FROM tool_calls
WHERE tool_name NOT IN (
    'Bash', 'Read', 'Edit', 'Write', 'Glob', 'Grep',
    'Task', 'WebFetch', 'WebSearch', 'TodoWrite',
    'AskUserQuestion', 'EnterPlanMode', 'ExitPlanMode',
    'Skill', 'SlashCommand', 'KillShell', 'NotebookEdit'
) AND tool_name NOT LIKE 'mcp__%';
```

### Status Value Validation
```sql
-- Todo statuses should be valid
SELECT DISTINCT status FROM todos
WHERE status NOT IN ('pending', 'in_progress', 'completed');

-- Message types should be valid
SELECT DISTINCT type FROM messages
WHERE type NOT IN ('user', 'assistant', 'file-history-snapshot');
```

---

## 1.5.6: Validation Implementation

### New File: `validation.py`

```python
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional
import sqlite3


class ValidationSeverity(Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


@dataclass
class ValidationResult:
    check_name: str
    passed: bool
    severity: ValidationSeverity
    message: str
    details: Optional[Dict[str, Any]] = None
    query: Optional[str] = None
    fix_query: Optional[str] = None


class DataValidator:
    """Validates extracted data integrity."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.results: List[ValidationResult] = []

    def run_all_checks(self) -> Dict[str, Any]:
        """Run all validation checks and return comprehensive report."""
        self.results = []

        checks = [
            self.check_cross_source_consistency,
            self.check_data_types,
            self.check_completeness,
            self.check_duplicates,
            self.check_semantic_validity,
            self.check_referential_integrity,
        ]

        for check in checks:
            try:
                check()
            except Exception as e:
                self.results.append(ValidationResult(
                    check_name=check.__name__,
                    passed=False,
                    severity=ValidationSeverity.ERROR,
                    message=f"Check failed with exception: {e}",
                ))

        return self.generate_report()

    def check_cross_source_consistency(self) -> None:
        """Verify counts match between stats_cache and actual data."""
        # Implementation details...
        pass

    def check_data_types(self) -> None:
        """Verify data types and formats are valid."""
        # Implementation details...
        pass

    def check_completeness(self) -> None:
        """Verify all required fields are present."""
        # Implementation details...
        pass

    def check_duplicates(self) -> None:
        """Verify no duplicate primary keys."""
        # Implementation details...
        pass

    def check_semantic_validity(self) -> None:
        """Verify values are semantically valid."""
        # Implementation details...
        pass

    def check_referential_integrity(self) -> None:
        """Verify foreign key relationships are valid."""
        # Implementation details...
        pass

    def generate_report(self) -> Dict[str, Any]:
        """Generate validation summary report."""
        passed = sum(1 for r in self.results if r.passed)
        failed = len(self.results) - passed

        by_severity = {}
        for r in self.results:
            sev = r.severity.value
            by_severity[sev] = by_severity.get(sev, 0) + (0 if r.passed else 1)

        return {
            "total_checks": len(self.results),
            "passed": passed,
            "failed": failed,
            "pass_rate": passed / len(self.results) if self.results else 1.0,
            "by_severity": by_severity,
            "results": [
                {
                    "check": r.check_name,
                    "passed": r.passed,
                    "severity": r.severity.value,
                    "message": r.message,
                    "details": r.details,
                }
                for r in self.results
            ],
        }
```

### CLI Command
```bash
# Run all validation checks
claude-metrics validate ./claude_metrics_output

# Generate detailed report
claude-metrics validate --report validation_report.json

# Show only failures
claude-metrics validate --failures-only

# Auto-fix where possible (e.g., remove duplicates)
claude-metrics validate --fix
```

---

## 1.5.7: Pre-Derived Metrics Validation Checklist

Before proceeding to Phase 2, verify:

- [ ] **Cross-source counts match within 5% tolerance**
  - Stats cache session count vs actual sessions
  - Stats cache message count vs actual messages
  - Daily activity sums vs total messages

- [ ] **All timestamps are valid**
  - ISO 8601 format
  - Within reasonable date range (2024-2030)
  - Monotonically increasing within sessions

- [ ] **Token counts are plausible**
  - No negative values
  - No single-message counts > 1M
  - Sums approximately match stats cache

- [ ] **Durations are plausible**
  - No negative values
  - Sessions < 30 days
  - Tool calls < 1 hour

- [ ] **No orphan records**
  - All messages have valid session_id
  - All tool_calls have valid session_id
  - Parent-child message chains are valid

- [ ] **No duplicate primary keys**
  - Unique session_id
  - Unique message uuid
  - Unique tool_call id

- [ ] **All required fields are non-NULL**
  - session_id, project, start_time in sessions
  - uuid, session_id, timestamp, type in messages
  - id, tool_name in tool_calls

- [ ] **All enum values are valid**
  - Model names match `claude-*` pattern
  - Tool names are recognized
  - Todo status in {pending, in_progress, completed}
  - Message type in {user, assistant, file-history-snapshot}

---

# PHASE 2: DERIVED METRICS COMPILATION

## Objective

Compute 592 derived metrics across 54 categories from the validated raw data.

---

## 2.1: Architecture Overview

```
claude-metrics/
├── derived/
│   ├── __init__.py
│   ├── base.py              # BaseMetric abstract class
│   ├── registry.py          # Metric registry & discovery
│   ├── engine.py            # Computation engine
│   ├── storage.py           # Results storage
│   │
│   └── categories/
│       ├── __init__.py
│       │
│       # Original Categories (A-Z: 442 metrics)
│       ├── time_activity.py     # A: D001-D028 (28 metrics)
│       ├── tool_usage.py        # B: D029-D048 (20 metrics)
│       ├── file_operations.py   # C: D049-D073 (25 metrics)
│       ├── model_tokens.py      # D: D074-D109 (36 metrics)
│       ├── conversation.py      # E: D110-D136 (27 metrics)
│       ├── thinking.py          # F: D137-D142 (6 metrics)
│       ├── task_management.py   # G: D143-D158 (16 metrics)
│       ├── agent_delegation.py  # H: D159-D172 (14 metrics)
│       ├── project_activity.py  # I: D173-D188 (16 metrics)
│       ├── error_recovery.py    # J: D189-D203 (15 metrics)
│       ├── code_generation.py   # K: D204-D228 (25 metrics)
│       ├── web_research.py      # L: D229-D238 (10 metrics)
│       ├── hooks_custom.py      # M: D239-D252 (14 metrics)
│       ├── user_interaction.py  # N: D253-D259 (7 metrics)
│       ├── advanced.py          # O: D260-D300 (41 metrics)
│       ├── previous.py          # P: D301-D343 (43 metrics)
│       ├── startup.py           # Q: D344-D348 (5 metrics)
│       ├── feature_discovery.py # R: D349-D357 (9 metrics)
│       ├── feature_flags.py     # S: D358-D362 (5 metrics)
│       ├── per_project.py       # T: D363-D395 (33 metrics)
│       ├── subscription.py      # U: D396-D399 (4 metrics)
│       ├── project_custom.py    # V: D400-D411 (12 metrics)
│       ├── mcp_server.py        # W: D412-D417 (6 metrics)
│       ├── realtime.py          # X: D418-D423 (6 metrics)
│       ├── cross_source.py      # Y: D424-D430 (7 metrics)
│       ├── behavioral.py        # Z: D431-D442 (12 metrics)
│       │
│       # Extended Categories (AA-BB: 150 metrics)
│       ├── psychology.py        # AA: D443-D447 (5 metrics)
│       ├── learning.py          # AB: D448-D452 (5 metrics)
│       ├── collaboration.py     # AC: D453-D457 (5 metrics)
│       ├── code_quality.py      # AD: D458-D462 (5 metrics)
│       ├── economic.py          # AE: D463-D467 (5 metrics)
│       ├── problem_solving.py   # AF: D468-D471 (4 metrics)
│       ├── metacognitive.py     # AG: D472-D475 (4 metrics)
│       ├── network.py           # AH: D476-D478 (3 metrics)
│       ├── security.py          # AI: D479-D481 (3 metrics)
│       ├── temporal.py          # AJ: D482-D484 (3 metrics)
│       ├── customization.py     # AK: D485-D488 (4 metrics)
│       ├── counterfactual.py    # AL: D489-D492 (4 metrics)
│       ├── biological.py        # AM: D493-D497 (5 metrics)
│       ├── information.py       # AN: D498-D502 (5 metrics)
│       ├── predictive.py        # AO: D503-D507 (5 metrics)
│       ├── game_theory.py       # AP: D508-D511 (4 metrics)
│       ├── developmental.py     # AQ: D512-D515 (4 metrics)
│       ├── systems.py           # AR: D516-D519 (4 metrics)
│       ├── comparative.py       # AS: D520-D524 (5 metrics)
│       ├── ecosystem.py         # AT: D525-D529 (5 metrics)
│       ├── quality.py           # AU: D530-D534 (5 metrics)
│       ├── workflow.py          # AV: D535-D539 (5 metrics)
│       ├── communication.py     # AW: D540-D542 (3 metrics)
│       ├── hybrid.py            # AX: D543-D552 (10 metrics)
│       ├── meta.py              # AY: D553-D562 (10 metrics)
│       ├── epistemological.py   # AZ: D563-D572 (10 metrics)
│       ├── narrative.py         # BA: D573-D582 (10 metrics)
│       └── phenomenological.py  # BB: D583-D592 (10 metrics)
```

---

## 2.2: Base Metric Pattern

### MetricDefinition Dataclass
```python
from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class MetricType(Enum):
    COUNT = "count"
    SUM = "sum"
    AVERAGE = "average"
    RATIO = "ratio"
    PERCENTAGE = "percentage"
    TREND = "trend"
    SEQUENCE = "sequence"
    DISTRIBUTION = "distribution"
    COMPOUND = "compound"
    CORRELATION = "correlation"


@dataclass
class MetricDefinition:
    id: str                      # D001, D002, etc.
    name: str                    # Human-readable name
    category: str                # A, B, ..., BB
    description: str             # What it measures
    calculation: str             # Formula/SQL description
    data_sources: List[str]      # Required tables
    metric_type: MetricType      # Type classification
    unit: Optional[str] = None   # "count", "ms", "USD", "%", etc.
    higher_is_better: Optional[bool] = None  # For interpretation
```

### BaseMetric Abstract Class
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional
import sqlite3


@dataclass
class MetricResult:
    id: str
    name: str
    category: str
    value: Any
    computed_at: str
    computation_time_ms: int
    metadata: Optional[Dict[str, Any]] = None


class BaseMetric(ABC):
    """Abstract base class for all derived metrics."""

    definition: MetricDefinition

    def __init__(self, db_path: Path):
        self.db_path = db_path

    @abstractmethod
    def compute(self, conn: sqlite3.Connection) -> MetricResult:
        """Compute the metric value from the database."""
        pass

    def validate_inputs(self, conn: sqlite3.Connection) -> bool:
        """Check that required data exists."""
        for table in self.definition.data_sources:
            cursor = conn.execute(
                f"SELECT COUNT(*) FROM {table}"
            )
            if cursor.fetchone()[0] == 0:
                return False
        return True

    def _timed_compute(self, conn: sqlite3.Connection) -> MetricResult:
        """Compute with timing."""
        start = datetime.now()
        result = self.compute(conn)
        elapsed = (datetime.now() - start).total_seconds() * 1000
        result.computation_time_ms = int(elapsed)
        return result
```

### Example Metric Implementations
```python
class D001_TotalMessagesAllTime(BaseMetric):
    definition = MetricDefinition(
        id="D001",
        name="Total Messages All-Time",
        category="A",
        description="Total number of messages across all sessions",
        calculation="COUNT(*) FROM messages",
        data_sources=["messages"],
        metric_type=MetricType.COUNT,
        unit="count",
        higher_is_better=None,  # Neutral
    )

    def compute(self, conn: sqlite3.Connection) -> MetricResult:
        cursor = conn.execute("SELECT COUNT(*) FROM messages")
        value = cursor.fetchone()[0]
        return MetricResult(
            id=self.definition.id,
            name=self.definition.name,
            category=self.definition.category,
            value=value,
            computed_at=datetime.now().isoformat(),
            computation_time_ms=0,
        )


class D017_AverageSessionDuration(BaseMetric):
    definition = MetricDefinition(
        id="D017",
        name="Average Session Duration",
        category="A",
        description="Mean duration of sessions in milliseconds",
        calculation="AVG(duration_ms) FROM sessions WHERE duration_ms > 0",
        data_sources=["sessions"],
        metric_type=MetricType.AVERAGE,
        unit="ms",
    )

    def compute(self, conn: sqlite3.Connection) -> MetricResult:
        cursor = conn.execute(
            "SELECT AVG(duration_ms) FROM sessions WHERE duration_ms > 0"
        )
        value = cursor.fetchone()[0] or 0
        return MetricResult(
            id=self.definition.id,
            name=self.definition.name,
            category=self.definition.category,
            value=round(value, 2),
            computed_at=datetime.now().isoformat(),
            computation_time_ms=0,
            metadata={"unit": "ms", "human": f"{value/1000/60:.1f} minutes"},
        )


class D100_CacheHitRatio(BaseMetric):
    definition = MetricDefinition(
        id="D100",
        name="Cache Hit Ratio",
        category="D",
        description="Ratio of cache reads to total input tokens",
        calculation="SUM(cache_read_tokens) / SUM(input_tokens + cache_read_tokens)",
        data_sources=["messages"],
        metric_type=MetricType.RATIO,
        unit="ratio",
        higher_is_better=True,
    )

    def compute(self, conn: sqlite3.Connection) -> MetricResult:
        cursor = conn.execute("""
            SELECT
                SUM(cache_read_tokens) as cache_read,
                SUM(input_tokens) as input_tokens
            FROM messages
            WHERE input_tokens > 0 OR cache_read_tokens > 0
        """)
        row = cursor.fetchone()
        cache_read = row[0] or 0
        input_tokens = row[1] or 0
        total = cache_read + input_tokens
        ratio = cache_read / total if total > 0 else 0

        return MetricResult(
            id=self.definition.id,
            name=self.definition.name,
            category=self.definition.category,
            value=round(ratio, 4),
            computed_at=datetime.now().isoformat(),
            computation_time_ms=0,
            metadata={
                "cache_read_tokens": cache_read,
                "input_tokens": input_tokens,
                "percentage": f"{ratio*100:.1f}%",
            },
        )
```

---

## 2.3: Metric Categories by Implementation Complexity

### Tier 1: Simple Aggregations (92 metrics) - EASY
Direct SQL queries with COUNT, SUM, AVG, GROUP BY.

| Category | ID Range | Count | Key SQL Patterns |
|----------|----------|-------|------------------|
| A: Time & Activity | D001-D028 | 28 | `COUNT(*)`, `SUM()`, date functions |
| B: Tool Usage | D029-D048 | 20 | `GROUP BY tool_name` |
| C: File Operations | D049-D073 | 25 | `WHERE file_path LIKE '%'` |
| D: Model & Tokens | D074-D109 | 36 | `GROUP BY model`, `SUM(tokens)` |
| Q: Startup | D344-D348 | 5 | Direct value reads |

**Implementation time estimate**: 1-2 days

### Tier 2: Time-Series Analysis (31 metrics) - MEDIUM
Requires date/time parsing, rolling windows, trend detection.

| Category | ID Range | Count | Key Techniques |
|----------|----------|-------|----------------|
| I: Project Activity | D173-D188 | 16 | Date grouping, project filtering |
| AJ: Temporal | D482-D484 | 3 | Hour-of-day analysis |
| Z: Behavioral | D431-D442 | 12 | Trend slopes, moving averages |

**Implementation time estimate**: 2-3 days

### Tier 3: Cross-Source Joins (17 metrics) - MEDIUM-HARD
Requires joining multiple tables, denormalization.

| Category | ID Range | Count | Key Techniques |
|----------|----------|-------|----------------|
| Y: Cross-Source | D424-D430 | 7 | Multi-table JOINs |
| AS: Comparative | D520-D524 | 5 | Percentile calculations |
| AT: Ecosystem | D525-D529 | 5 | Multi-source aggregation |

**Implementation time estimate**: 2-3 days

### Tier 4: Sequence Analysis (19 metrics) - HARD
Requires analyzing ordered sequences, pattern detection.

| Category | ID Range | Count | Key Techniques |
|----------|----------|-------|----------------|
| AF: Problem-Solving | D468-D471 | 4 | Consecutive sequence detection |
| BA: Narrative | D573-D582 | 10 | Session arc analysis |
| AC: Collaboration | D453-D457 | 5 | Interaction pattern matching |

**Implementation time estimate**: 3-4 days

### Tier 5: Statistical/ML (20 metrics) - ADVANCED
Requires statistical models, inference, prediction.

| Category | ID Range | Count | Key Techniques |
|----------|----------|-------|----------------|
| AA: Psychology | D443-D447 | 5 | Behavioral inference |
| AO: Predictive | D503-D507 | 5 | Simple predictive models |
| BB: Phenomenological | D583-D592 | 10 | Experience state inference |

**Implementation time estimate**: 4-5 days

### Remaining Categories (413 metrics)
The remaining metrics follow similar patterns and can be implemented incrementally.

---

## 2.4: Derived Metrics Database Schema

```sql
-- Add to existing schema

-- Computed metric values
CREATE TABLE IF NOT EXISTS derived_metrics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metric_id TEXT NOT NULL,         -- D001, D002, etc.
    metric_name TEXT NOT NULL,
    category TEXT NOT NULL,
    value REAL,
    value_text TEXT,                 -- For non-numeric values
    value_json TEXT,                 -- For complex values (JSON)
    unit TEXT,
    computed_at TEXT NOT NULL,
    computation_time_ms INTEGER,
    UNIQUE(metric_id, computed_at)
);

-- Metric computation history (for trend tracking)
CREATE TABLE IF NOT EXISTS metric_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    metric_id TEXT NOT NULL,
    value REAL,
    computed_at TEXT NOT NULL
);

-- Metric definitions (for self-documentation)
CREATE TABLE IF NOT EXISTS metric_definitions (
    metric_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    calculation TEXT,
    data_sources TEXT,              -- JSON array
    metric_type TEXT,
    unit TEXT,
    higher_is_better INTEGER        -- 1=true, 0=false, NULL=neutral
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_derived_metrics_category ON derived_metrics(category);
CREATE INDEX IF NOT EXISTS idx_derived_metrics_computed ON derived_metrics(computed_at);
CREATE INDEX IF NOT EXISTS idx_metric_history_metric ON metric_history(metric_id);
CREATE INDEX IF NOT EXISTS idx_metric_history_date ON metric_history(computed_at);
```

---

## 2.5: Phase 2 Implementation Checklist

### Setup & Infrastructure
- [ ] Create `derived/` package structure
- [ ] Implement `MetricDefinition` dataclass
- [ ] Implement `MetricResult` dataclass
- [ ] Implement `BaseMetric` abstract class
- [ ] Implement `MetricRegistry` for auto-discovery
- [ ] Implement `ComputeEngine` for batch execution
- [ ] Add database tables for derived metrics
- [ ] Add CLI command: `claude-metrics compute`
- [ ] Add CLI command: `claude-metrics compute --metric D001`
- [ ] Add CLI command: `claude-metrics compute --category A`

### Tier 1: Simple Aggregations (92 metrics)
- [ ] Category A: Time & Activity (D001-D028)
- [ ] Category B: Tool Usage (D029-D048)
- [ ] Category C: File Operations (D049-D073)
- [ ] Category D: Model & Tokens (D074-D109)
- [ ] Category Q: Startup (D344-D348)
- [ ] Unit tests for Tier 1

### Tier 2: Time-Series (31 metrics)
- [ ] Category I: Project Activity (D173-D188)
- [ ] Category AJ: Temporal Dynamics (D482-D484)
- [ ] Category Z: Behavioral Patterns (D431-D442)
- [ ] Unit tests for Tier 2

### Tier 3: Cross-Source (17 metrics)
- [ ] Category Y: Cross-Source Correlation (D424-D430)
- [ ] Category AS: Comparative/Benchmark (D520-D524)
- [ ] Category AT: Ecosystem (D525-D529)
- [ ] Unit tests for Tier 3

### Tier 4: Sequence Analysis (19 metrics)
- [ ] Category AF: Problem-Solving (D468-D471)
- [ ] Category BA: Narrative (D573-D582)
- [ ] Category AC: Collaboration Quality (D453-D457)
- [ ] Unit tests for Tier 4

### Tier 5: Statistical (20 metrics)
- [ ] Category AA: Psychology (D443-D447)
- [ ] Category AO: Predictive (D503-D507)
- [ ] Category BB: Phenomenological (D583-D592)
- [ ] Unit tests for Tier 5

### Remaining Categories (413 metrics)
- [ ] Categories E-H (63 metrics)
- [ ] Categories J-P (188 metrics)
- [ ] Categories R-X (62 metrics)
- [ ] Categories AB-AN (46 metrics)
- [ ] Categories AP-AZ (54 metrics)
- [ ] Unit tests for remaining

### Integration & Performance
- [ ] Integration test with full dataset
- [ ] Performance benchmark (target: all metrics <60s)
- [ ] Memory profiling for large datasets
- [ ] Error handling and recovery

---

# PHASE 3: VISUALIZATIONS

## Objective

Create interactive dashboards and static reports to visualize the 914+ metrics.

---

## 3.1: Visualization Categories

### Category 1: Time-Series Dashboards
Interactive line/area charts showing trends over time.

| Visualization | Metrics Used | Description |
|---------------|--------------|-------------|
| Daily Activity | D001-D005 | Messages, sessions, tools per day |
| Token Consumption | D097-D099 | Daily token usage trends |
| Cost Accumulation | D105-D107 | Cumulative cost over time |
| Session Duration | D017 | Session length trends |
| Model Usage Timeline | D096 | Model distribution over time |

### Category 2: Distribution Charts
Pie charts, bar charts, histograms showing breakdowns.

| Visualization | Metrics Used | Description |
|---------------|--------------|-------------|
| Tool Usage Breakdown | D029-D048 | Pie/bar chart of tool frequency |
| Model Distribution | D096 | Model usage percentages |
| Message Length Histogram | D133 | Distribution of message sizes |
| Session Length Distribution | D017 | Histogram of session durations |
| File Type Distribution | D077 | Breakdown by file extension |

### Category 3: Heatmaps
Grid-based visualizations showing patterns.

| Visualization | Metrics Used | Description |
|---------------|--------------|-------------|
| Hourly Activity | hourCounts | 24-hour activity pattern |
| Day-of-Week × Hour | D025, hourCounts | 7×24 activity heatmap |
| Tool × Project | D029-D048, projects | Tool usage by project |

### Category 4: Network Graphs
Node-link diagrams showing relationships.

| Visualization | Metrics Used | Description |
|---------------|--------------|-------------|
| File Co-modification | D080 | Files edited together |
| Agent Delegation | D159-D172 | Parent-child agent relationships |
| Project Knowledge Graph | various | Connections between projects |

### Category 5: Progress Indicators
Gauge charts, progress bars, scorecards.

| Visualization | Metrics Used | Description |
|---------------|--------------|-------------|
| Feature Adoption | D349-D357 | % of features used |
| Skill Mastery | D448-D452 | Learning progress |
| Completion Rates | D143-D158 | Todo completion % |

### Category 6: Comparative Views
Side-by-side comparisons.

| Visualization | Metrics Used | Description |
|---------------|--------------|-------------|
| Project Comparison | D363-D395 | Compare metrics across projects |
| Week-over-Week | D431-D442 | This week vs last week |
| Model Efficiency | D074-D109 | Compare model performance |

---

## 3.2: Dashboard Architecture

```
claude-metrics/
├── visualizations/
│   ├── __init__.py
│   │
│   ├── dashboard.py          # Main dashboard generator
│   ├── server.py             # Optional local web server
│   │
│   ├── charts/
│   │   ├── __init__.py
│   │   ├── base.py           # BaseChart class
│   │   ├── time_series.py    # Line, area, bar charts
│   │   ├── distributions.py  # Pie, histogram, bar
│   │   ├── heatmaps.py       # Calendar, hour×day grids
│   │   ├── networks.py       # NetworkX + PyVis graphs
│   │   ├── progress.py       # Gauges, progress bars
│   │   └── comparative.py    # Side-by-side views
│   │
│   ├── reports/
│   │   ├── __init__.py
│   │   ├── html.py           # Full HTML report
│   │   ├── markdown.py       # Markdown summary
│   │   └── pdf.py            # PDF export (optional)
│   │
│   └── templates/
│       ├── dashboard.html    # Main Jinja2 template
│       ├── report.html       # Report template
│       ├── base.html         # Base template
│       └── components/
│           ├── header.html
│           ├── card.html
│           ├── chart.html
│           └── table.html
```

---

## 3.3: Technology Stack

| Component | Technology | Justification |
|-----------|------------|---------------|
| Interactive Charts | Plotly | Best-in-class, exports to HTML |
| Network Graphs | NetworkX + PyVis | Python-native, interactive output |
| Static Charts | Matplotlib | Fallback for simple charts |
| Templating | Jinja2 | Standard, powerful |
| CSS Framework | Tailwind CSS | Modern, utility-first |
| CLI Progress | Rich | Already in use |

### Dependencies to Add
```toml
[project.optional-dependencies]
visualize = [
    "plotly>=5.0.0",
    "networkx>=3.0",
    "pyvis>=0.3.0",
    "jinja2>=3.0.0",
    "pandas>=2.0.0",  # For data manipulation
]
```

---

## 3.4: Sample Dashboard Layout

```
┌────────────────────────────────────────────────────────────────────────────┐
│  📊 Claude Code Metrics Dashboard                    [Export ▼] [Theme 🌙] │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌───────────┐ │
│  │ 📝 Sessions     │ │ 💬 Messages     │ │ 🔧 Tool Calls   │ │ 💰 Cost   │ │
│  │    1,513        │ │    67,155       │ │    12,847       │ │  $42.17   │ │
│  │ ▲ 12% this week │ │ ▲ 8% this week  │ │ ▼ 3% this week  │ │ ▲ $5.20   │ │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘ └───────────┘ │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 📈 Daily Activity                                    [7d|30d|90d|All] │  │
│  │                                                                      │  │
│  │  Messages ━━━━━━━━━━━━━━━━━━━━━━━                                    │  │
│  │  Sessions ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄                                        │  │
│  │  Tool Calls ─ ─ ─ ─ ─ ─ ─ ─                                          │  │
│  │                                                                      │  │
│  │  ▲                                                                   │  │
│  │  │     ╭─────╮                                                       │  │
│  │  │    ╱       ╲      ╭───────╮                                       │  │
│  │  │   ╱         ╲    ╱         ╲   ╭─╮                                │  │
│  │  │  ╱           ╲──╱           ╲─╱   ╲                               │  │
│  │  └────────────────────────────────────────────────────────────▶     │  │
│  │    Nov 6   Nov 13   Nov 20   Nov 27   Dec 4    Dec 11               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
│  ┌────────────────────────────┐  ┌────────────────────────────────────┐   │
│  │ 🛠️ Tool Usage              │  │ 🕐 Hourly Activity                 │   │
│  │                            │  │                                    │   │
│  │  ████████████ Bash    32%  │  │    Hour  0  4  8  12 16 20 24     │   │
│  │  █████████ Read      24%  │  │    ─────────────────────────────   │   │
│  │  ███████ Edit        18%  │  │    Mon  ⬜⬜⬜🟨🟨🟧🟥🟧🟨⬜⬜⬜   │   │
│  │  █████ Grep          14%  │  │    Tue  ⬜⬜⬜🟨🟧🟧🟧🟨🟨⬜⬜⬜   │   │
│  │  ████ Glob            8%  │  │    Wed  ⬜⬜⬜🟨🟧🟥🟥🟧🟨⬜⬜⬜   │   │
│  │  ██ Other             4%  │  │    Thu  ⬜⬜⬜🟨🟧🟧🟧🟧🟨⬜⬜⬜   │   │
│  │                            │  │    Fri  ⬜⬜⬜🟨🟨🟧🟨🟨⬜⬜⬜⬜   │   │
│  │                            │  │    Sat  ⬜⬜⬜⬜🟨🟨🟨⬜⬜⬜⬜⬜   │   │
│  │                            │  │    Sun  ⬜⬜⬜⬜⬜🟨⬜⬜⬜⬜⬜⬜   │   │
│  └────────────────────────────┘  └────────────────────────────────────┘   │
│                                                                            │
│  ┌────────────────────────────┐  ┌────────────────────────────────────┐   │
│  │ 🤖 Model Distribution      │  │ 📁 Top Projects                    │   │
│  │                            │  │                                    │   │
│  │      Opus 4.5              │  │  claude-hooks-manager    $12.50   │   │
│  │        ████████████ 78%    │  │  ██████████████████████           │   │
│  │                            │  │                                    │   │
│  │      Sonnet 3.5            │  │  kosmos-project           $8.20   │   │
│  │        █████ 18%           │  │  █████████████████                │   │
│  │                            │  │                                    │   │
│  │      Haiku 3.5             │  │  document-tracker         $5.10   │   │
│  │        █ 4%                │  │  ██████████                        │   │
│  │                            │  │                                    │   │
│  └────────────────────────────┘  └────────────────────────────────────┘   │
│                                                                            │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │ 🎯 Feature Adoption                                                  │  │
│  │                                                                      │  │
│  │  Plan Mode      ████████████████████████████████████░░░░  85%       │  │
│  │  Thinking Mode  ████████████████████████████████████████  100%      │  │
│  │  Custom Agents  ████████████████████████░░░░░░░░░░░░░░░░  55%       │  │
│  │  MCP Servers    ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  25%       │  │
│  │  Hooks          ████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  10%       │  │
│  │                                                                      │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## 3.5: Phase 3 Implementation Checklist

### Setup & Infrastructure
- [ ] Create `visualizations/` package structure
- [ ] Add visualization dependencies to pyproject.toml
- [ ] Implement `BaseChart` abstract class
- [ ] Create Jinja2 template structure
- [ ] Add CLI command: `claude-metrics visualize`
- [ ] Add CLI command: `claude-metrics visualize --server` (local preview)
- [ ] Add CLI command: `claude-metrics report`

### Core Charts
- [ ] Time series line chart (daily activity)
- [ ] Multi-series line chart (messages/sessions/tools)
- [ ] Bar chart (tool usage)
- [ ] Pie chart (model distribution)
- [ ] Histogram (session length distribution)
- [ ] Heatmap (hourly activity)
- [ ] Calendar heatmap (daily activity)

### Advanced Charts
- [ ] Network graph (file co-modification)
- [ ] Treemap (project breakdown)
- [ ] Sunburst (hierarchical tool usage)
- [ ] Radar chart (feature adoption)
- [ ] Gauge chart (completion rates)

### Dashboard
- [ ] Dashboard template with responsive grid
- [ ] Summary cards (sessions, messages, cost)
- [ ] Filter controls (date range, project)
- [ ] Dark mode toggle
- [ ] Export button (PNG/HTML)

### Reports
- [ ] HTML report generator
- [ ] Markdown report generator
- [ ] Executive summary (1-page)
- [ ] Detailed breakdown report

### Polish
- [ ] Responsive design (mobile-friendly)
- [ ] Loading states and placeholders
- [ ] Error handling for missing data
- [ ] Performance optimization
- [ ] Unit tests for chart generators

---

# PACKAGING FOR PORTABILITY

## Objective

Package all files needed to create a standalone repository.

---

## Final Package Structure

```
claude-metrics/
├── README.md                     # Comprehensive project README
├── LICENSE                       # MIT License
├── pyproject.toml                # Python package config
├── requirements.txt              # Pinned dependencies
├── .gitignore                    # Python gitignore
│
├── __init__.py                   # v0.1.0
├── extractor.py                  # Main extraction orchestrator
├── database.py                   # SQLite schema & operations
├── redaction.py                  # Sensitive data handling
├── utils.py                      # Utilities
├── cli.py                        # CLI entry point
├── validation.py                 # Data integrity validation
│
├── sources/
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
├── derived/                      # Phase 2
│   ├── __init__.py
│   ├── base.py
│   ├── registry.py
│   ├── engine.py
│   └── categories/
│       └── ... (45+ files)
│
├── visualizations/               # Phase 3
│   ├── __init__.py
│   ├── dashboard.py
│   ├── charts/
│   │   └── ... (7 files)
│   ├── reports/
│   │   └── ... (3 files)
│   └── templates/
│       └── ... (5+ files)
│
├── docs/
│   ├── CLAUDE_CODE_DATA_SOURCES.md  # Claude Code local data reference
│   ├── METRICS_CATALOG.md           # Raw data schemas
│   ├── DERIVED_METRICS_CATALOG.md   # 592 derived metrics with types
│   ├── BRAINSTORM_PROMPT.md         # Brainstorm prompt for extensions
│   ├── IMPLEMENTATION_PLAN.md       # This document
│   └── API.md                       # API documentation
│
└── tests/
    ├── __init__.py
    ├── conftest.py               # Pytest fixtures
    ├── test_extractor.py
    ├── test_validation.py
    ├── test_derived/
    │   └── test_category_a.py
    └── fixtures/
        └── sample_data/
            ├── stats_cache.json
            ├── history.jsonl
            └── ... (sanitized samples)
```

---

## Files to Create for Packaging

### Root Files

**README.md**
```markdown
# Claude Metrics

Extract, analyze, and visualize your Claude Code usage data.

## Features
- Extract data from 28 local data sources
- Compute 592 derived metrics across 54 categories
- Generate interactive HTML dashboards
- SQLite database for custom queries

## Installation
pip install claude-metrics

## Quick Start
# Extract your data
claude-metrics extract

# Validate integrity
claude-metrics validate

# Compute derived metrics
claude-metrics compute

# Generate dashboard
claude-metrics visualize

## Documentation
- [Metrics Catalog](docs/METRICS_CATALOG.md) - 914+ documented metrics
- [Implementation Plan](docs/IMPLEMENTATION_PLAN.md) - Project roadmap
```

**requirements.txt**
```
rich>=13.0.0
plotly>=5.0.0
networkx>=3.0
pyvis>=0.3.0
jinja2>=3.0.0
pandas>=2.0.0
```

**.gitignore**
```
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.eggs/

# Virtual environments
venv/
.venv/
env/

# IDE
.idea/
.vscode/
*.swp

# Output
claude_metrics_output/
*.db

# OS
.DS_Store
Thumbs.db
```

---

## Packaging Checklist

### File Collection
- [ ] Copy root Python files (6 files)
- [ ] Copy `pyproject.toml`
- [ ] Copy `CLAUDE_CODE_DATA_SOURCES.md` to `docs/`
- [ ] Copy `CLAUDE_CODE_METRICS_CATALOG.md` to `docs/METRICS_CATALOG.md`
- [ ] Copy `BRAINSTORM_METRICS_PROMPT.md` to `docs/BRAINSTORM_PROMPT.md`
- [ ] Copy this plan to `docs/IMPLEMENTATION_PLAN.md`

### New Files to Create
- [ ] Create `README.md` with quick start guide
- [ ] Create `LICENSE` (MIT)
- [ ] Create `requirements.txt`
- [ ] Create `.gitignore`
- [ ] Create `tests/__init__.py`
- [ ] Create `tests/conftest.py`
- [ ] Create sample fixture data (sanitized)

### Verification
- [ ] Run `pip install -e .` successfully
- [ ] Run `claude-metrics sources` successfully
- [ ] Run `claude-metrics extract --help` successfully
- [ ] Run `pytest` successfully (once tests exist)

---

# SUMMARY

## Total Scope

| Phase | Files | Lines | Status |
|-------|-------|-------|--------|
| Phase 1: Extraction | 17 | ~2,500 | ✅ Complete |
| Phase 1.5: Validation | 1 | ~400 | 📋 Planned |
| Phase 2: Derived Metrics | ~50 | ~3,000 | 📋 Planned |
| Phase 3: Visualizations | ~15 | ~2,000 | 📋 Planned |
| Packaging | ~10 | ~500 | 📋 Planned |
| **TOTAL** | ~93 | ~8,400 | |

## Implementation Order

1. **Package files** → Create portable directory structure
2. **Phase 1.5** → Validate data integrity
3. **Phase 2 Tier 1** → Simple aggregation metrics
4. **Phase 2 Tier 2-5** → Complex metrics
5. **Phase 3** → Visualizations and dashboard
6. **Polish** → Tests, docs, optimization

## Success Metrics

- [ ] 100% of validation checks pass
- [ ] 592 derived metrics computed
- [ ] Computation completes in <60 seconds
- [ ] Interactive dashboard renders correctly
- [ ] Clean install from package works
- [ ] All tests pass

"""SQLite database handling for Claude Metrics."""

import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


# SQL schema for the metrics database
SCHEMA = """
-- Extraction metadata
CREATE TABLE IF NOT EXISTS extraction_info (
    id INTEGER PRIMARY KEY,
    extracted_at TEXT NOT NULL,
    claude_metrics_version TEXT,
    include_sensitive INTEGER DEFAULT 0,
    sources_extracted TEXT
);

-- Stats cache summary
CREATE TABLE IF NOT EXISTS stats_cache (
    id INTEGER PRIMARY KEY,
    version INTEGER,
    last_computed_date TEXT,
    total_sessions INTEGER,
    total_messages INTEGER,
    first_session_date TEXT
);

-- Daily activity records
CREATE TABLE IF NOT EXISTS daily_activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL UNIQUE,
    message_count INTEGER DEFAULT 0,
    session_count INTEGER DEFAULT 0,
    tool_call_count INTEGER DEFAULT 0
);

-- Hourly activity distribution
CREATE TABLE IF NOT EXISTS hourly_activity (
    hour INTEGER PRIMARY KEY,
    count INTEGER DEFAULT 0
);

-- Model usage statistics
CREATE TABLE IF NOT EXISTS model_usage (
    model TEXT PRIMARY KEY,
    input_tokens INTEGER DEFAULT 0,
    output_tokens INTEGER DEFAULT 0,
    cache_read_tokens INTEGER DEFAULT 0,
    cache_creation_tokens INTEGER DEFAULT 0,
    web_search_requests INTEGER DEFAULT 0,
    cost_usd REAL DEFAULT 0
);

-- Sessions summary
CREATE TABLE IF NOT EXISTS sessions (
    session_id TEXT PRIMARY KEY,
    project TEXT,
    project_dir TEXT,
    start_time TEXT,
    end_time TEXT,
    duration_ms INTEGER,
    message_count INTEGER DEFAULT 0,
    user_message_count INTEGER DEFAULT 0,
    assistant_message_count INTEGER DEFAULT 0,
    tool_call_count INTEGER DEFAULT 0,
    total_input_tokens INTEGER DEFAULT 0,
    total_output_tokens INTEGER DEFAULT 0,
    primary_model TEXT,
    cost_usd REAL DEFAULT 0,
    is_agent INTEGER DEFAULT 0,
    agent_id TEXT,
    file_path TEXT
);

-- Messages (summary, not full content)
CREATE TABLE IF NOT EXISTS messages (
    uuid TEXT PRIMARY KEY,
    session_id TEXT,
    parent_uuid TEXT,
    timestamp TEXT,
    type TEXT,
    role TEXT,
    model TEXT,
    input_tokens INTEGER DEFAULT 0,
    output_tokens INTEGER DEFAULT 0,
    cache_read_tokens INTEGER DEFAULT 0,
    cost_usd REAL DEFAULT 0,
    has_thinking INTEGER DEFAULT 0,
    thinking_length INTEGER DEFAULT 0,
    tool_call_count INTEGER DEFAULT 0,
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

-- Tool calls
CREATE TABLE IF NOT EXISTS tool_calls (
    id TEXT PRIMARY KEY,
    message_uuid TEXT,
    session_id TEXT,
    tool_name TEXT NOT NULL,
    duration_ms INTEGER,
    total_duration_ms INTEGER,
    is_error INTEGER DEFAULT 0,
    is_interrupted INTEGER DEFAULT 0,
    file_path TEXT,
    FOREIGN KEY (message_uuid) REFERENCES messages(uuid),
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

-- User input history
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    display TEXT,
    timestamp INTEGER,
    timestamp_iso TEXT,
    project TEXT,
    has_pasted_contents INTEGER DEFAULT 0
);

-- Todo items
CREATE TABLE IF NOT EXISTS todos (
    id TEXT,
    session_id TEXT,
    content TEXT,
    status TEXT,
    priority TEXT,
    active_form TEXT,
    PRIMARY KEY (id, session_id)
);

-- Plans
CREATE TABLE IF NOT EXISTS plans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL UNIQUE,
    file_path TEXT,
    size_bytes INTEGER,
    line_count INTEGER,
    header_count INTEGER,
    code_block_count INTEGER,
    created_at TEXT,
    modified_at TEXT
);

-- Projects (from ~/.claude.json)
CREATE TABLE IF NOT EXISTS projects (
    path TEXT PRIMARY KEY,
    last_session_id TEXT,
    last_cost REAL,
    last_duration_ms INTEGER,
    last_lines_added INTEGER,
    last_lines_removed INTEGER,
    last_input_tokens INTEGER,
    last_output_tokens INTEGER,
    last_cache_read_tokens INTEGER,
    last_cache_creation_tokens INTEGER,
    has_trust_accepted INTEGER DEFAULT 0,
    allowed_tools TEXT,
    mcp_servers TEXT
);

-- Extensions (agents, commands, skills)
CREATE TABLE IF NOT EXISTS extensions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    file_path TEXT,
    size_bytes INTEGER,
    scope TEXT DEFAULT 'global',
    UNIQUE(type, name, scope)
);

-- Tips history
CREATE TABLE IF NOT EXISTS tips_history (
    tip_name TEXT PRIMARY KEY,
    show_count INTEGER DEFAULT 0
);

-- Feature flags
CREATE TABLE IF NOT EXISTS feature_flags (
    flag_name TEXT PRIMARY KEY,
    enabled INTEGER DEFAULT 0
);

-- Settings
CREATE TABLE IF NOT EXISTS settings (
    scope TEXT PRIMARY KEY,
    model TEXT,
    thinking_enabled INTEGER,
    git_attribution INTEGER,
    permissions_mode TEXT,
    allowed_tools TEXT,
    denied_tools TEXT
);

-- Debug log summary
CREATE TABLE IF NOT EXISTS debug_logs (
    session_id TEXT PRIMARY KEY,
    file_path TEXT,
    size_bytes INTEGER,
    line_count INTEGER,
    error_count INTEGER DEFAULT 0,
    warning_count INTEGER DEFAULT 0
);

-- File history summary
CREATE TABLE IF NOT EXISTS file_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id TEXT,
    file_hash TEXT,
    version INTEGER,
    file_path TEXT,
    size_bytes INTEGER
);

-- Claude store summary (from __store.db)
CREATE TABLE IF NOT EXISTS store_summary (
    id INTEGER PRIMARY KEY,
    size_bytes INTEGER,
    total_messages INTEGER DEFAULT 0,
    total_cost_usd REAL DEFAULT 0,
    sessions_count INTEGER DEFAULT 0,
    first_message_date TEXT,
    last_message_date TEXT,
    models_used TEXT
);

-- Shell snapshots
CREATE TABLE IF NOT EXISTS shell_snapshots (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL UNIQUE,
    shell TEXT,
    timestamp TEXT,
    size_bytes INTEGER,
    modified_at TEXT
);

-- Session environment
CREATE TABLE IF NOT EXISTS session_env (
    session_id TEXT PRIMARY KEY,
    file_count INTEGER DEFAULT 0,
    size_bytes INTEGER DEFAULT 0,
    files TEXT
);

-- Installed versions
CREATE TABLE IF NOT EXISTS versions (
    version TEXT PRIMARY KEY,
    size_bytes INTEGER,
    installed_at TEXT,
    is_current INTEGER DEFAULT 0
);

-- Project configurations
CREATE TABLE IF NOT EXISTS project_configs (
    path TEXT PRIMARY KEY,
    has_claude_dir INTEGER DEFAULT 0,
    has_settings INTEGER DEFAULT 0,
    agent_count INTEGER DEFAULT 0,
    command_count INTEGER DEFAULT 0,
    skill_count INTEGER DEFAULT 0,
    agents TEXT,
    commands TEXT,
    skills TEXT
);

-- CLAUDE.md files
CREATE TABLE IF NOT EXISTS claude_md_files (
    project TEXT PRIMARY KEY,
    path TEXT,
    size_bytes INTEGER,
    line_count INTEGER,
    word_count INTEGER,
    section_count INTEGER,
    sections TEXT,
    has_includes INTEGER DEFAULT 0
);

-- MCP configurations
CREATE TABLE IF NOT EXISTS mcp_configs (
    project TEXT PRIMARY KEY,
    config_file TEXT,
    server_count INTEGER DEFAULT 0
);

-- MCP servers
CREATE TABLE IF NOT EXISTS mcp_servers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project TEXT,
    name TEXT NOT NULL,
    type TEXT,
    command TEXT,
    FOREIGN KEY (project) REFERENCES mcp_configs(project)
);

-- Environment variables
CREATE TABLE IF NOT EXISTS environment_vars (
    id INTEGER PRIMARY KEY,
    claudecode TEXT,
    entrypoint TEXT,
    project_dir TEXT,
    config_dir TEXT,
    has_api_key INTEGER DEFAULT 0,
    has_oauth_token INTEGER DEFAULT 0,
    telemetry_enabled TEXT,
    total_vars_set INTEGER DEFAULT 0
);

-- Cache info
CREATE TABLE IF NOT EXISTS cache_info (
    id INTEGER PRIMARY KEY,
    path TEXT,
    cache_exists INTEGER DEFAULT 0,
    total_size_bytes INTEGER DEFAULT 0,
    file_count INTEGER DEFAULT 0,
    subdirectories TEXT
);

-- MCP log summaries
CREATE TABLE IF NOT EXISTS mcp_log_summaries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project TEXT,
    server TEXT,
    log_count INTEGER DEFAULT 0,
    total_size_bytes INTEGER DEFAULT 0,
    error_count INTEGER DEFAULT 0
);

-- Create indexes for common queries
CREATE INDEX IF NOT EXISTS idx_sessions_project ON sessions(project);
CREATE INDEX IF NOT EXISTS idx_sessions_start_time ON sessions(start_time);
CREATE INDEX IF NOT EXISTS idx_messages_session ON messages(session_id);
CREATE INDEX IF NOT EXISTS idx_messages_timestamp ON messages(timestamp);
CREATE INDEX IF NOT EXISTS idx_tool_calls_session ON tool_calls(session_id);
CREATE INDEX IF NOT EXISTS idx_tool_calls_name ON tool_calls(tool_name);
CREATE INDEX IF NOT EXISTS idx_history_timestamp ON history(timestamp);
CREATE INDEX IF NOT EXISTS idx_daily_activity_date ON daily_activity(date);
"""


class MetricsDatabase:
    """SQLite database for Claude metrics."""

    def __init__(self, db_path: Path):
        """Initialize the database.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self.conn: Optional[sqlite3.Connection] = None

    def connect(self) -> sqlite3.Connection:
        """Open database connection and initialize schema."""
        self.conn = sqlite3.connect(str(self.db_path))
        self.conn.row_factory = sqlite3.Row
        self._init_schema()
        return self.conn

    def _init_schema(self):
        """Create database tables if they don't exist."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executescript(SCHEMA)
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            self.conn = None

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def record_extraction(
        self,
        version: str,
        include_sensitive: bool,
        sources: List[str]
    ):
        """Record extraction metadata."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT INTO extraction_info
            (extracted_at, claude_metrics_version, include_sensitive, sources_extracted)
            VALUES (?, ?, ?, ?)
            """,
            (
                datetime.now().isoformat(),
                version,
                1 if include_sensitive else 0,
                json.dumps(sources),
            ),
        )
        self.conn.commit()

    def insert_stats_cache(self, data: Dict[str, Any]):
        """Insert stats cache data."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO stats_cache
            (id, version, last_computed_date, total_sessions, total_messages, first_session_date)
            VALUES (1, ?, ?, ?, ?, ?)
            """,
            (
                data.get("version"),
                data.get("lastComputedDate"),
                data.get("totalSessions"),
                data.get("totalMessages"),
                data.get("firstSessionDate"),
            ),
        )
        self.conn.commit()

    def insert_daily_activity(self, records: List[Dict[str, Any]]):
        """Insert daily activity records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO daily_activity
            (date, message_count, session_count, tool_call_count)
            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    r.get("date"),
                    r.get("messageCount", 0),
                    r.get("sessionCount", 0),
                    r.get("toolCallCount", 0),
                )
                for r in records
            ],
        )
        self.conn.commit()

    def insert_hourly_activity(self, hour_counts: Dict[str, int]):
        """Insert hourly activity distribution."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO hourly_activity (hour, count)
            VALUES (?, ?)
            """,
            [(int(h), c) for h, c in hour_counts.items()],
        )
        self.conn.commit()

    def insert_model_usage(self, model_usage: Dict[str, Dict[str, Any]]):
        """Insert model usage statistics."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        for model, stats in model_usage.items():
            self.conn.execute(
                """
                INSERT OR REPLACE INTO model_usage
                (model, input_tokens, output_tokens, cache_read_tokens,
                 cache_creation_tokens, web_search_requests, cost_usd)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    model,
                    stats.get("inputTokens", 0),
                    stats.get("outputTokens", 0),
                    stats.get("cacheReadInputTokens", 0),
                    stats.get("cacheCreationInputTokens", 0),
                    stats.get("webSearchRequests", 0),
                    stats.get("costUSD", 0),
                ),
            )
        self.conn.commit()

    def insert_session(self, session: Dict[str, Any]):
        """Insert a session record."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO sessions
            (session_id, project, project_dir, start_time, end_time, duration_ms,
             message_count, user_message_count, assistant_message_count,
             tool_call_count, total_input_tokens, total_output_tokens,
             primary_model, cost_usd, is_agent, agent_id, file_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                session.get("session_id"),
                session.get("project"),
                session.get("project_dir"),
                session.get("start_time"),
                session.get("end_time"),
                session.get("duration_ms"),
                session.get("message_count", 0),
                session.get("user_message_count", 0),
                session.get("assistant_message_count", 0),
                session.get("tool_call_count", 0),
                session.get("total_input_tokens", 0),
                session.get("total_output_tokens", 0),
                session.get("primary_model"),
                session.get("cost_usd", 0),
                1 if session.get("is_agent") else 0,
                session.get("agent_id"),
                session.get("file_path"),
            ),
        )

    def insert_message(self, message: Dict[str, Any]):
        """Insert a message record."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT OR IGNORE INTO messages
            (uuid, session_id, parent_uuid, timestamp, type, role, model,
             input_tokens, output_tokens, cache_read_tokens, cost_usd,
             has_thinking, thinking_length, tool_call_count)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                message.get("uuid"),
                message.get("session_id"),
                message.get("parent_uuid"),
                message.get("timestamp"),
                message.get("type"),
                message.get("role"),
                message.get("model"),
                message.get("input_tokens", 0),
                message.get("output_tokens", 0),
                message.get("cache_read_tokens", 0),
                message.get("cost_usd", 0),
                1 if message.get("has_thinking") else 0,
                message.get("thinking_length", 0),
                message.get("tool_call_count", 0),
            ),
        )

    def insert_tool_call(self, tool_call: Dict[str, Any]):
        """Insert a tool call record."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT OR IGNORE INTO tool_calls
            (id, message_uuid, session_id, tool_name, duration_ms,
             total_duration_ms, is_error, is_interrupted, file_path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                tool_call.get("id"),
                tool_call.get("message_uuid"),
                tool_call.get("session_id"),
                tool_call.get("tool_name"),
                tool_call.get("duration_ms"),
                tool_call.get("total_duration_ms"),
                1 if tool_call.get("is_error") else 0,
                1 if tool_call.get("is_interrupted") else 0,
                tool_call.get("file_path"),
            ),
        )

    def insert_history(self, records: List[Dict[str, Any]]):
        """Insert history records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT INTO history
            (display, timestamp, timestamp_iso, project, has_pasted_contents)
            VALUES (?, ?, ?, ?, ?)
            """,
            [
                (
                    r.get("display"),
                    r.get("timestamp"),
                    r.get("timestamp_iso"),
                    r.get("project"),
                    1 if r.get("pastedContents") else 0,
                )
                for r in records
            ],
        )
        self.conn.commit()

    def insert_project(self, path: str, data: Dict[str, Any]):
        """Insert a project record."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO projects
            (path, last_session_id, last_cost, last_duration_ms,
             last_lines_added, last_lines_removed,
             last_input_tokens, last_output_tokens,
             last_cache_read_tokens, last_cache_creation_tokens,
             has_trust_accepted, allowed_tools, mcp_servers)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                path,
                data.get("lastSessionId"),
                data.get("lastCost"),
                data.get("lastDuration"),
                data.get("lastLinesAdded"),
                data.get("lastLinesRemoved"),
                data.get("lastTotalInputTokens"),
                data.get("lastTotalOutputTokens"),
                data.get("lastTotalCacheReadInputTokens"),
                data.get("lastTotalCacheCreationInputTokens"),
                1 if data.get("hasTrustDialogAccepted") else 0,
                json.dumps(data.get("allowedTools", [])),
                json.dumps(data.get("mcpServers", {})),
            ),
        )
        self.conn.commit()

    def insert_sqlite_store_summary(self, data: Dict[str, Any]):
        """Insert SQLite store summary."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        stats = data.get("assistant_stats", {})
        date_range = stats.get("date_range", {})
        self.conn.execute(
            """
            INSERT OR REPLACE INTO store_summary
            (id, size_bytes, total_messages, total_cost_usd, sessions_count,
             first_message_date, last_message_date, models_used)
            VALUES (1, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data.get("size_bytes", 0),
                stats.get("total_messages", 0),
                stats.get("total_cost_usd", 0),
                stats.get("sessions_count", 0),
                date_range.get("first"),
                date_range.get("last"),
                json.dumps(stats.get("models_used", [])),
            ),
        )
        self.conn.commit()

    def insert_shell_snapshots(self, snapshots: List[Dict[str, Any]]):
        """Insert shell snapshot records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO shell_snapshots
            (filename, shell, timestamp, size_bytes, modified_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            [
                (
                    s.get("filename"),
                    s.get("shell"),
                    s.get("timestamp"),
                    s.get("size_bytes", 0),
                    s.get("modified_at"),
                )
                for s in snapshots
            ],
        )
        self.conn.commit()

    def insert_session_env(self, sessions: List[Dict[str, Any]]):
        """Insert session environment records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO session_env
            (session_id, file_count, size_bytes, files)
            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    s.get("session_id"),
                    s.get("file_count", 0),
                    s.get("size_bytes", 0),
                    json.dumps(s.get("files", [])),
                )
                for s in sessions
            ],
        )
        self.conn.commit()

    def insert_versions(self, versions: List[Dict[str, Any]], current_version: Optional[str]):
        """Insert version records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO versions
            (version, size_bytes, installed_at, is_current)
            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    v.get("version"),
                    v.get("size_bytes", 0),
                    v.get("installed_at"),
                    1 if v.get("version") == current_version else 0,
                )
                for v in versions
            ],
        )
        self.conn.commit()

    def insert_project_configs(self, projects: List[Dict[str, Any]]):
        """Insert project configuration records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO project_configs
            (path, has_claude_dir, has_settings, agent_count, command_count,
             skill_count, agents, commands, skills)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    p.get("path"),
                    1 if p.get("has_claude_dir") else 0,
                    1 if p.get("has_settings") else 0,
                    p.get("agent_count", 0),
                    p.get("command_count", 0),
                    p.get("skill_count", 0),
                    json.dumps(p.get("agents", [])),
                    json.dumps(p.get("commands", [])),
                    json.dumps(p.get("skills", [])),
                )
                for p in projects
            ],
        )
        self.conn.commit()

    def insert_claude_md_files(self, files: List[Dict[str, Any]]):
        """Insert CLAUDE.md file records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO claude_md_files
            (project, path, size_bytes, line_count, word_count,
             section_count, sections, has_includes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    f.get("project"),
                    f.get("path"),
                    f.get("size_bytes", 0),
                    f.get("line_count", 0),
                    f.get("word_count", 0),
                    f.get("section_count", 0),
                    json.dumps(f.get("sections", [])),
                    1 if f.get("has_includes") else 0,
                )
                for f in files
            ],
        )
        self.conn.commit()

    def insert_mcp_configs(self, configs: List[Dict[str, Any]]):
        """Insert MCP configuration records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")

        for config in configs:
            project = config.get("project")
            self.conn.execute(
                """
                INSERT OR REPLACE INTO mcp_configs
                (project, config_file, server_count)
                VALUES (?, ?, ?)
                """,
                (
                    project,
                    config.get("config_file"),
                    config.get("server_count", 0),
                ),
            )

            # Insert servers
            for server in config.get("servers", []):
                self.conn.execute(
                    """
                    INSERT INTO mcp_servers (project, name, type, command)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        project,
                        server.get("name"),
                        server.get("type"),
                        server.get("command"),
                    ),
                )

        self.conn.commit()

    def insert_environment_vars(self, data: Dict[str, Any]):
        """Insert environment variable record."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO environment_vars
            (id, claudecode, entrypoint, project_dir, config_dir,
             has_api_key, has_oauth_token, telemetry_enabled, total_vars_set)
            VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data.get("CLAUDECODE"),
                data.get("CLAUDE_CODE_ENTRYPOINT"),
                data.get("CLAUDE_PROJECT_DIR"),
                data.get("CLAUDE_CONFIG_DIR"),
                1 if data.get("has_ANTHROPIC_API_KEY") else 0,
                1 if data.get("has_CLAUDE_CODE_OAUTH_TOKEN") else 0,
                data.get("CLAUDE_CODE_ENABLE_TELEMETRY"),
                data.get("_total_vars_set", 0),
            ),
        )
        self.conn.commit()

    def insert_cache_info(self, data: Dict[str, Any]):
        """Insert cache info record."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO cache_info
            (id, path, cache_exists, total_size_bytes, file_count, subdirectories)
            VALUES (1, ?, ?, ?, ?, ?)
            """,
            (
                data.get("path"),
                1 if data.get("cache_exists") else 0,
                data.get("total_size_bytes", 0),
                data.get("file_count", 0),
                json.dumps([s.get("name") for s in data.get("subdirectories", [])]),
            ),
        )
        self.conn.commit()

    def insert_mcp_log_summaries(self, projects: List[Dict[str, Any]]):
        """Insert MCP log summary records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        for project in projects:
            project_name = project.get("project")
            for server in project.get("servers", []):
                self.conn.execute(
                    """
                    INSERT INTO mcp_log_summaries
                    (project, server, log_count, total_size_bytes, error_count)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        project_name,
                        server.get("server"),
                        server.get("log_count", 0),
                        server.get("total_size_bytes", 0),
                        server.get("error_count", 0),
                    ),
                )
        self.conn.commit()

    def insert_debug_logs(self, logs: List[Dict[str, Any]]):
        """Insert debug log records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        self.conn.executemany(
            """
            INSERT OR REPLACE INTO debug_logs
            (session_id, file_path, size_bytes, line_count, error_count, warning_count)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    l.get("session_id"),
                    l.get("filename"),
                    l.get("size_bytes", 0),
                    l.get("line_count", 0),
                    l.get("error_count", 0),
                    l.get("warning_count", 0),
                )
                for l in logs
            ],
        )
        self.conn.commit()

    def insert_file_history(self, sessions: List[Dict[str, Any]]):
        """Insert file history records."""
        if self.conn is None:
            raise RuntimeError("Database not connected")
        for session in sessions:
            session_id = session.get("session_id")
            for file_info in session.get("files", []):
                self.conn.execute(
                    """
                    INSERT INTO file_history
                    (session_id, file_hash, version, size_bytes)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        session_id,
                        file_info.get("hash"),
                        file_info.get("max_version", 0),
                        file_info.get("total_size_bytes", 0),
                    ),
                )
        self.conn.commit()

    def commit(self):
        """Commit pending changes."""
        if self.conn:
            self.conn.commit()

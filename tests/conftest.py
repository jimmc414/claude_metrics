"""Pytest fixtures for claude_metrics tests.

Provides factory fixtures for building test data at any granularity:
  make_message()        -> MessageData
  make_tool_call()      -> ToolCallData
  make_session()        -> SessionData
  make_extracted_data() -> ExtractedData30Day (the central aggregate)
  make_jsonl_session()  -> writes a synthetic JSONL file to tmp_path
  mock_claude_dir       -> creates mock ~/.claude/ directory tree
"""

import json
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import pytest

from extraction.data_classes import (
    ConversationThread,
    DailyActivity,
    ExtractedData30Day,
    MessageData,
    ModelUsageData,
    SessionData,
    ToolCallData,
    ToolChainLink,
)

# ---------------------------------------------------------------------------
# Fixed timestamps for deterministic tests
# ---------------------------------------------------------------------------
FIXED_NOW = datetime(2025, 1, 15, 14, 0, 0, tzinfo=timezone.utc)
FIXED_YESTERDAY = FIXED_NOW - timedelta(days=1)
FIXED_WEEK_AGO = FIXED_NOW - timedelta(days=7)
FIXED_MONTH_AGO = FIXED_NOW - timedelta(days=30)

_MSG_COUNTER = 0
_SESSION_COUNTER = 0


def _next_msg_id() -> str:
    global _MSG_COUNTER
    _MSG_COUNTER += 1
    return f"msg-{_MSG_COUNTER:06d}"


def _next_session_id() -> str:
    global _SESSION_COUNTER
    _SESSION_COUNTER += 1
    return f"session-{_SESSION_COUNTER:06d}"


# ---------------------------------------------------------------------------
# Factory: MessageData
# ---------------------------------------------------------------------------
@pytest.fixture
def make_message():
    """Factory fixture that returns a MessageData builder."""

    def _make(
        *,
        uuid: Optional[str] = None,
        session_id: str = "test-session",
        timestamp: Optional[datetime] = None,
        message_type: str = "assistant",
        role: Optional[str] = None,
        model: Optional[str] = "claude-sonnet-4-20250514",
        input_tokens: int = 100,
        output_tokens: int = 200,
        cache_read_tokens: int = 0,
        cost_usd: float = 0.001,
        has_thinking: bool = False,
        thinking_length: int = 0,
        tool_call_count: int = 0,
        content: Optional[str] = "Test response",
        parent_uuid: Optional[str] = None,
        stop_reason: Optional[str] = "end_turn",
        is_sidechain: bool = False,
    ) -> MessageData:
        return MessageData(
            uuid=uuid or _next_msg_id(),
            session_id=session_id,
            timestamp=timestamp or FIXED_NOW,
            message_type=message_type,
            role=role or message_type,
            model=model if message_type == "assistant" else None,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cache_read_tokens=cache_read_tokens,
            cost_usd=cost_usd,
            has_thinking=has_thinking,
            thinking_length=thinking_length,
            tool_call_count=tool_call_count,
            content=content,
            parent_uuid=parent_uuid,
            stop_reason=stop_reason,
            is_sidechain=is_sidechain,
        )

    return _make


# ---------------------------------------------------------------------------
# Factory: ToolCallData
# ---------------------------------------------------------------------------
@pytest.fixture
def make_tool_call():
    """Factory fixture that returns a ToolCallData builder."""

    def _make(
        *,
        tool_name: str = "Read",
        timestamp: Optional[datetime] = None,
        session_id: str = "test-session",
        message_uuid: Optional[str] = None,
        duration_ms: Optional[int] = 50,
        total_duration_ms: Optional[int] = 55,
        success: bool = True,
        is_error: bool = False,
        is_interrupted: bool = False,
        file_path: Optional[str] = "/tmp/test.py",
        tool_use_id: Optional[str] = None,
        edit_old_string: Optional[str] = None,
        edit_new_string: Optional[str] = None,
        edit_replace_all: bool = False,
        web_url: Optional[str] = None,
        search_query: Optional[str] = None,
        question_header: Optional[str] = None,
        question_text: Optional[str] = None,
        question_options: Optional[List[str]] = None,
    ) -> ToolCallData:
        return ToolCallData(
            tool_name=tool_name,
            timestamp=timestamp or FIXED_NOW,
            session_id=session_id,
            message_uuid=message_uuid or _next_msg_id(),
            duration_ms=duration_ms,
            total_duration_ms=total_duration_ms,
            success=success,
            is_error=is_error,
            is_interrupted=is_interrupted,
            file_path=file_path,
            tool_use_id=tool_use_id or f"tu-{_next_msg_id()}",
            edit_old_string=edit_old_string,
            edit_new_string=edit_new_string,
            edit_replace_all=edit_replace_all,
            web_url=web_url,
            search_query=search_query,
            question_header=question_header,
            question_text=question_text,
            question_options=question_options or [],
        )

    return _make


# ---------------------------------------------------------------------------
# Factory: SessionData
# ---------------------------------------------------------------------------
@pytest.fixture
def make_session():
    """Factory fixture that returns a SessionData builder."""

    def _make(
        *,
        session_id: Optional[str] = None,
        project_path: str = "/mnt/c/python/myproject",
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        duration_ms: int = 600_000,  # 10 minutes
        message_count: int = 10,
        user_message_count: int = 5,
        assistant_message_count: int = 5,
        tool_call_count: int = 3,
        cost_usd: float = 0.05,
        model: Optional[str] = "claude-sonnet-4-20250514",
        models_used: Optional[List[str]] = None,
        total_input_tokens: int = 5000,
        total_output_tokens: int = 3000,
        total_cache_read_tokens: int = 1000,
        is_agent: bool = False,
    ) -> SessionData:
        _start = start_time or FIXED_NOW - timedelta(minutes=10)
        _end = end_time or FIXED_NOW
        return SessionData(
            session_id=session_id or _next_session_id(),
            project_path=project_path,
            start_time=_start,
            end_time=_end,
            duration_ms=duration_ms,
            message_count=message_count,
            user_message_count=user_message_count,
            assistant_message_count=assistant_message_count,
            tool_call_count=tool_call_count,
            cost_usd=cost_usd,
            model=model,
            models_used=models_used or [model or "claude-sonnet-4-20250514"],
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_cache_read_tokens=total_cache_read_tokens,
            is_agent=is_agent,
        )

    return _make


# ---------------------------------------------------------------------------
# Factory: ExtractedData30Day
# ---------------------------------------------------------------------------
@pytest.fixture
def make_extracted_data(make_session, make_message, make_tool_call):
    """Factory fixture that returns an ExtractedData30Day builder.

    Accepts optional lists of sessions/messages/tool_calls and auto-computes
    aggregate totals.  Pass empty lists for a bare-minimum data object.
    """

    def _make(
        *,
        window_start: Optional[datetime] = None,
        window_end: Optional[datetime] = None,
        window_days: int = 30,
        sessions: Optional[List[SessionData]] = None,
        messages: Optional[List[MessageData]] = None,
        tool_calls: Optional[List[ToolCallData]] = None,
        daily_activity: Optional[List[DailyActivity]] = None,
        hourly_distribution: Optional[Dict[int, int]] = None,
        tool_counts: Optional[Dict[str, int]] = None,
        files_read: Optional[Dict[str, int]] = None,
        files_edited: Optional[Dict[str, int]] = None,
        files_written: Optional[Dict[str, int]] = None,
        model_usage: Optional[Dict[str, ModelUsageData]] = None,
        total_tokens: Optional[Dict[str, int]] = None,
        active_dates: Optional[List[str]] = None,
        web_urls_fetched: Optional[List[str]] = None,
        search_queries: Optional[List[str]] = None,
        questions_asked: Optional[List[Dict[str, Any]]] = None,
        edit_operations: Optional[List[Dict[str, Any]]] = None,
        tool_chains: Optional[List[List[ToolChainLink]]] = None,
        conversation_threads: Optional[List[ConversationThread]] = None,
        custom_agents: int = 0,
        custom_commands: int = 0,
        custom_skills: int = 0,
        hook_executions: int = 0,
        hook_errors: int = 0,
        hook_preventions: int = 0,
    ) -> ExtractedData30Day:
        _sessions = sessions if sessions is not None else []
        _messages = messages if messages is not None else []
        _tool_calls = tool_calls if tool_calls is not None else []

        # Auto-compute totals from provided data
        _total_sessions = len(_sessions)
        _total_messages = sum(s.message_count for s in _sessions) if _sessions else len(_messages)
        _total_tool_calls = len(_tool_calls)
        _total_cost = sum(s.cost_usd for s in _sessions)

        # Auto-compute token totals
        if total_tokens is not None:
            _total_tokens = total_tokens
        else:
            _total_tokens = {
                "input": sum(s.total_input_tokens for s in _sessions),
                "output": sum(s.total_output_tokens for s in _sessions),
                "cache_read": sum(s.total_cache_read_tokens for s in _sessions),
            }

        # Auto-compute tool_counts
        if tool_counts is not None:
            _tool_counts = tool_counts
        else:
            _tool_counts: Dict[str, int] = {}
            for tc in _tool_calls:
                _tool_counts[tc.tool_name] = _tool_counts.get(tc.tool_name, 0) + 1

        data = ExtractedData30Day(
            window_start=window_start or FIXED_NOW - timedelta(days=window_days),
            window_end=window_end or FIXED_NOW,
            window_days=window_days,
        )

        data.sessions = _sessions
        data.messages = _messages
        data.tool_calls = _tool_calls
        data.daily_activity = daily_activity or []
        if hourly_distribution is not None:
            data.hourly_distribution = hourly_distribution
        data.tool_counts = _tool_counts
        data.files_read = files_read or {}
        data.files_edited = files_edited or {}
        data.files_written = files_written or {}
        data.model_usage = model_usage or {}
        data.total_tokens = _total_tokens
        data.total_sessions = _total_sessions
        data.total_messages = _total_messages
        data.total_tool_calls = _total_tool_calls
        data.total_cost_usd = _total_cost
        data.active_dates = active_dates or []
        data.web_urls_fetched = web_urls_fetched or []
        data.search_queries = search_queries or []
        data.questions_asked = questions_asked or []
        data.edit_operations = edit_operations or []
        data.tool_chains = tool_chains or []
        data.conversation_threads = conversation_threads or []
        data.custom_agents = custom_agents
        data.custom_commands = custom_commands
        data.custom_skills = custom_skills
        data.hook_executions = hook_executions
        data.hook_errors = hook_errors
        data.hook_preventions = hook_preventions

        return data

    return _make


# ---------------------------------------------------------------------------
# Factory: JSONL session writer
# ---------------------------------------------------------------------------
@pytest.fixture
def make_jsonl_session(tmp_path):
    """Factory that writes a synthetic JSONL session file and returns its path."""

    def _make(
        *,
        session_id: str = "test-session",
        project_dir_name: str = "-mnt-c-python-myproject",
        records: Optional[List[Dict[str, Any]]] = None,
    ) -> Path:
        projects_dir = tmp_path / ".claude" / "projects" / project_dir_name
        projects_dir.mkdir(parents=True, exist_ok=True)
        jsonl_path = projects_dir / f"{session_id}.jsonl"

        if records is None:
            ts_base = FIXED_NOW
            records = [
                {
                    "uuid": "msg-u1",
                    "parentUuid": None,
                    "type": "user",
                    "message": {"role": "user", "content": "Hello"},
                    "timestamp": ts_base.isoformat(),
                },
                {
                    "uuid": "msg-a1",
                    "parentUuid": "msg-u1",
                    "type": "assistant",
                    "message": {
                        "role": "assistant",
                        "model": "claude-sonnet-4-20250514",
                        "content": [{"type": "text", "text": "Hi there!"}],
                        "usage": {
                            "input_tokens": 100,
                            "output_tokens": 50,
                            "cache_read_input_tokens": 20,
                        },
                        "stop_reason": "end_turn",
                    },
                    "timestamp": (ts_base + timedelta(seconds=2)).isoformat(),
                    "costUSD": 0.002,
                },
            ]

        with open(jsonl_path, "w") as f:
            for record in records:
                f.write(json.dumps(record) + "\n")

        return jsonl_path

    return _make


# ---------------------------------------------------------------------------
# Mock Claude directory (fixes Bug #3: correct filename is stats-cache.json)
# ---------------------------------------------------------------------------
@pytest.fixture
def mock_claude_dir(tmp_path):
    """Create a mock ~/.claude directory structure for testing.

    Uses correct filename ``stats-cache.json`` (not ``statsCache.json``).
    """
    claude_dir = tmp_path / ".claude"
    claude_dir.mkdir()

    # Create subdirectories
    (claude_dir / "projects").mkdir()
    (claude_dir / "agents").mkdir()
    (claude_dir / "commands").mkdir()
    (claude_dir / "skills").mkdir()
    (claude_dir / "statsig").mkdir()

    # Create mock settings.json
    settings = {
        "permissions": {
            "allow": ["Read", "Grep", "Glob"],
            "deny": [],
        },
        "theme": "dark",
    }
    (claude_dir / "settings.json").write_text(json.dumps(settings))

    # Correct filename: stats-cache.json (Bug #3 documents the mismatch)
    # Field names match real Claude Code stats-cache.json format
    stats_cache = {
        "dailyActivity": [
            {
                "date": "2025-01-14",
                "sessionCount": 5,
                "messageCount": 100,
                "toolCallCount": 40,
                "totalCost": 1.25,
                "inputTokens": 50000,
                "outputTokens": 25000,
            },
            {
                "date": "2025-01-15",
                "sessionCount": 3,
                "messageCount": 60,
                "toolCallCount": 20,
                "totalCost": 0.75,
                "inputTokens": 30000,
                "outputTokens": 15000,
            },
        ],
        "hourCounts": {str(h): h * 10 for h in range(24)},
    }
    (claude_dir / "stats-cache.json").write_text(json.dumps(stats_cache))

    yield claude_dir


# ---------------------------------------------------------------------------
# Legacy fixtures (kept for backward compatibility with test_extractor.py)
# ---------------------------------------------------------------------------
@pytest.fixture
def temp_output_dir():
    """Create a temporary output directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_session_data():
    """Sample session JSONL data for testing (legacy)."""
    return [
        {
            "uuid": "msg-001",
            "type": "user",
            "message": {"role": "user", "content": "Hello"},
            "timestamp": "2024-11-15T10:00:00.000Z",
        },
        {
            "uuid": "msg-002",
            "type": "assistant",
            "message": {"role": "assistant", "content": "Hi there!"},
            "timestamp": "2024-11-15T10:00:01.000Z",
            "costUSD": 0.001,
            "inputTokens": 10,
            "outputTokens": 5,
        },
    ]

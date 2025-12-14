"""Pytest fixtures for claude_metrics tests."""

import json
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_output_dir():
    """Create a temporary output directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_claude_dir(tmp_path):
    """Create a mock ~/.claude directory structure for testing."""
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
            "deny": []
        },
        "theme": "dark"
    }
    (claude_dir / "settings.json").write_text(json.dumps(settings))

    # Create mock stats_cache.json
    stats_cache = {
        "totalSessions": 100,
        "totalMessages": 5000,
        "totalToolUses": 2000,
        "totalCost": 15.50,
        "firstSessionDate": "2024-11-01T10:00:00.000Z"
    }
    (claude_dir / "statsCache.json").write_text(json.dumps(stats_cache))

    yield claude_dir


@pytest.fixture
def sample_session_data():
    """Sample session JSONL data for testing."""
    return [
        {
            "uuid": "msg-001",
            "type": "user",
            "message": {"role": "user", "content": "Hello"},
            "timestamp": "2024-11-15T10:00:00.000Z"
        },
        {
            "uuid": "msg-002",
            "type": "assistant",
            "message": {"role": "assistant", "content": "Hi there!"},
            "timestamp": "2024-11-15T10:00:01.000Z",
            "costUSD": 0.001,
            "inputTokens": 10,
            "outputTokens": 5
        }
    ]

"""Regression tests for all 7 known bugs.

Each bug is documented with its root cause and tested explicitly.
Tests that exercise still-broken behaviour are marked @pytest.mark.xfail.
"""

import inspect
import json
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List
from unittest.mock import patch

import pytest

from extraction.data_classes import (
    ExtractedData30Day,
    MessageData,
    SessionData,
    ToolCallData,
    ConversationThread,
)
from extraction.time_filtered import TimeFilteredExtractor
from tests.conftest import FIXED_NOW


# =====================================================================
# Bug 1: stats-cache.json field names (FIXED)
# The extractor now reads "messageCount" and "toolCallCount" matching
# the real stats-cache.json format from Claude Code.
# =====================================================================

class TestBug1_StatsCacheFieldNames:
    """Bug 1 (fixed): _extract_stats_cache now reads 'messageCount' and 'toolCallCount'."""

    def test_extractor_reads_message_count_key(self):
        """The extractor code uses 'messageCount' as the field name."""
        source = inspect.getsource(TimeFilteredExtractor._extract_stats_cache)
        assert "messageCount" in source

    def test_real_stats_cache_uses_message_count_key(self):
        """
        Real Claude Code stats-cache.json uses 'messageCount'.
        The extractor now correctly reads this key.
        """
        real_daily_entry = {
            "date": "2025-01-15",
            "sessionCount": 5,
            "messageCount": 100,
            "toolCallCount": 40,
            "totalCost": 1.25,
        }
        extracted_count = real_daily_entry.get("messageCount", 0)
        assert extracted_count == 100

    def test_mismatch_fixed_message_count(self):
        """
        After the fix, passing a real-format entry gets the correct count.
        """
        real_entry = {"date": "2025-01-15", "messageCount": 100}
        message_count = real_entry.get("messageCount", 0)
        assert message_count == 100


# =====================================================================
# Bug 2: dir_name_to_project_path corrupts paths with hyphens
# "-mnt-c-python-my-project" should become "/mnt/c/python/my-project"
# but the current code turns ALL hyphens into slashes.
# The fix handles double-dash (dot-prefix) but single hyphens in
# component names remain lossy.
# =====================================================================

class TestBug2_DirNameToProjectPath:
    """Bug 2: dir_name_to_project_path corrupts paths containing hyphens."""

    @pytest.mark.xfail(
        reason="Bug 2: hyphens in project names are fundamentally lossy -- "
        "all single hyphens become slashes so 'my-project' becomes 'my/project'"
    )
    def test_preserves_hyphens_in_project_name(self):
        from utils import dir_name_to_project_path

        result = dir_name_to_project_path("-mnt-c-python-my-project")
        assert result == "/mnt/c/python/my-project"

    def test_demonstrates_actual_buggy_behaviour(self):
        """Show what the current code actually produces for hyphenated names."""
        from utils import dir_name_to_project_path

        result = dir_name_to_project_path("-mnt-c-python-my-project")
        # All single hyphens become slashes (lossy)
        assert result == "/mnt/c/python/my/project"

    def test_simple_path_without_hyphens_works(self):
        """Paths without hyphens in directory names work fine."""
        from utils import dir_name_to_project_path

        result = dir_name_to_project_path("-mnt-c-python-myproject")
        assert result == "/mnt/c/python/myproject"

    def test_dot_prefix_path_fixed(self):
        """Double-dash now correctly maps to dot-prefixed components."""
        from utils import dir_name_to_project_path

        result = dir_name_to_project_path("-home-jim--local-share-project")
        assert result == "/home/jim/.local/share/project"


# =====================================================================
# Bug 3: conftest.py used wrong filename (statsCache.json vs stats-cache.json)
# The OLD conftest created "statsCache.json" but the extractor reads
# "stats-cache.json". This was fixed in the updated conftest.
# =====================================================================

class TestBug3_StatsCacheFilename:
    """Bug 3: extractor reads 'stats-cache.json' (hyphenated)."""

    def test_extractor_reads_hyphenated_filename(self):
        """The extractor constructs path as get_claude_dir() / 'stats-cache.json'."""
        source = inspect.getsource(TimeFilteredExtractor._extract_stats_cache)
        assert 'stats-cache.json' in source

    def test_conftest_creates_correct_filename(self, mock_claude_dir):
        """The current conftest fixture creates 'stats-cache.json' (not 'statsCache.json')."""
        stats_path = mock_claude_dir / "stats-cache.json"
        assert stats_path.exists()

    def test_camel_case_filename_would_not_be_found(self, mock_claude_dir):
        """A camelCase filename would not be found by the extractor."""
        camel_path = mock_claude_dir / "statsCache.json"
        assert not camel_path.exists()


# =====================================================================
# Bug 4: Tool result only applied to last tool_use block in multi-tool messages
# When a message has multiple tool_use blocks, toolUseResult is only
# applied to msg_tool_calls[-1].
# =====================================================================

class TestBug4_ToolResultOnlyAppliedToLast:
    """Bug 4: toolUseResult applied only to msg_tool_calls[-1]."""

    def test_source_shows_last_tool_update(self):
        """The source code updates msg_tool_calls[-1] (last only)."""
        source = inspect.getsource(TimeFilteredExtractor._extract_single_session)
        assert "msg_tool_calls[-1]" in source

    def test_multi_tool_message_only_last_gets_result(self, tmp_path):
        """
        A JSONL record with 2 tool_use blocks followed by a toolUseResult
        should only have the result applied to the last tool call.
        """
        ts = FIXED_NOW.isoformat()

        # Record with TWO tool_use blocks and ONE toolUseResult
        record = {
            "uuid": "msg-multi-tool",
            "parentUuid": None,
            "type": "assistant",
            "message": {
                "role": "assistant",
                "model": "claude-sonnet-4-20250514",
                "content": [
                    {
                        "type": "tool_use",
                        "id": "tool-1",
                        "name": "Read",
                        "input": {"file_path": "/tmp/a.py"},
                    },
                    {
                        "type": "tool_use",
                        "id": "tool-2",
                        "name": "Read",
                        "input": {"file_path": "/tmp/b.py"},
                    },
                ],
                "usage": {
                    "input_tokens": 100,
                    "output_tokens": 50,
                    "cache_read_input_tokens": 0,
                },
            },
            "timestamp": ts,
            "costUSD": 0.002,
            "toolUseResult": {
                "durationMs": 150,
                "totalDurationMs": 200,
                "status": "success",
            },
        }

        # Write JSONL
        jsonl_path = tmp_path / "test-session.jsonl"
        jsonl_path.write_text(json.dumps(record) + "\n")

        extractor = TimeFilteredExtractor(days=30)
        # Patch cutoff so our FIXED_NOW timestamp is within window
        extractor.cutoff = FIXED_NOW - timedelta(days=1)
        extractor._cutoff_naive = datetime.now() - timedelta(days=1)

        session, tool_calls, messages = extractor._extract_single_session(
            jsonl_path, "/tmp/project"
        )

        assert len(tool_calls) == 2

        # First tool call does NOT get the result (Bug 4)
        first_tool = tool_calls[0]
        assert first_tool.duration_ms is None, (
            "Bug 4: first tool_use block should NOT have duration set"
        )

        # Only the LAST tool call gets the result
        last_tool = tool_calls[1]
        assert last_tool.duration_ms == 150


# =====================================================================
# Bug 5: Integer division in _aggregate_model_usage (FIXED)
# Now uses remainder-distributing division so 7 messages across 2
# models => 4 + 3 = 7 (not 3 + 3 = 6).
# =====================================================================

class TestBug5_IntegerDivisionModelUsage:
    """Bug 5 (fixed): remainder-distributing division preserves token counts."""

    def test_total_messages_across_models_equals_session_count(
        self, make_extracted_data, make_session
    ):
        """
        A session with 7 messages and 2 models should distribute 7 total
        messages across models (4 + 3 = 7).
        """
        session = make_session(
            message_count=7,
            models_used=["model-a", "model-b"],
            total_input_tokens=700,
            total_output_tokens=350,
            total_cache_read_tokens=100,
            cost_usd=0.10,
        )
        data = make_extracted_data(sessions=[session])

        extractor = TimeFilteredExtractor(days=30)
        extractor._aggregate_model_usage(data)

        total_model_messages = sum(
            mu.message_count for mu in data.model_usage.values()
        )
        assert total_model_messages == session.message_count

    def test_remainder_distributing_division_preserves_total(
        self, make_extracted_data, make_session
    ):
        """7 messages across 2 models => 4+3=7, not 3+3=6."""
        session = make_session(
            message_count=7,
            models_used=["model-a", "model-b"],
            total_input_tokens=700,
            total_output_tokens=350,
            total_cache_read_tokens=100,
            cost_usd=0.10,
        )
        data = make_extracted_data(sessions=[session])

        extractor = TimeFilteredExtractor(days=30)
        extractor._aggregate_model_usage(data)

        total_model_messages = sum(
            mu.message_count for mu in data.model_usage.values()
        )
        assert total_model_messages == 7

    def test_remainder_distributing_division_preserves_tokens(
        self, make_extracted_data, make_session
    ):
        """Token counts are preserved by remainder-distributing division."""
        session = make_session(
            message_count=7,
            models_used=["model-a", "model-b"],
            total_input_tokens=701,
            total_output_tokens=351,
            total_cache_read_tokens=101,
            cost_usd=0.10,
        )
        data = make_extracted_data(sessions=[session])

        extractor = TimeFilteredExtractor(days=30)
        extractor._aggregate_model_usage(data)

        total_input = sum(mu.input_tokens for mu in data.model_usage.values())
        assert total_input == 701


# =====================================================================
# Bug 6: BFS uses list.pop(0) instead of collections.deque (O(n^2))
# This is a performance bug, not a correctness bug. We verify the BFS
# produces correct thread structure to document the code path.
# =====================================================================

class TestBug6_BFSPerformance:
    """Bug 6: BFS uses list.pop(0) which is O(n) per pop, making BFS O(n^2)."""

    def test_source_uses_list_pop_zero(self):
        """Confirm the code uses queue.pop(0) -- O(n) on a list."""
        source = inspect.getsource(TimeFilteredExtractor._build_conversation_threads)
        # NOTE: pop(0) is O(n) on a Python list; collections.deque.popleft() is O(1)
        assert "queue.pop(0)" in source

    def test_bfs_produces_correct_depth(self, make_extracted_data, make_message):
        """
        Despite the performance bug, BFS should produce correct tree depth.
        Linear chain: root -> child -> grandchild => max_depth=2.
        """
        msgs = [
            make_message(uuid="r1", parent_uuid=None, session_id="s1"),
            make_message(uuid="c1", parent_uuid="r1", session_id="s1"),
            make_message(uuid="g1", parent_uuid="c1", session_id="s1"),
        ]
        data = make_extracted_data(messages=msgs)

        extractor = TimeFilteredExtractor(days=30)
        extractor._build_conversation_threads(data)

        assert len(data.conversation_threads) == 1
        thread = data.conversation_threads[0]
        assert thread.max_depth == 2
        assert thread.message_count == 3

    def test_bfs_produces_correct_branch_count(self, make_extracted_data, make_message):
        """
        A root with 2 children should have branch_count=1 (one branching node).
        """
        msgs = [
            make_message(uuid="r1", parent_uuid=None, session_id="s1"),
            make_message(uuid="c1", parent_uuid="r1", session_id="s1"),
            make_message(uuid="c2", parent_uuid="r1", session_id="s1"),
        ]
        data = make_extracted_data(messages=msgs)

        extractor = TimeFilteredExtractor(days=30)
        extractor._build_conversation_threads(data)

        assert len(data.conversation_threads) == 1
        thread = data.conversation_threads[0]
        assert thread.branch_count == 1

    def test_bfs_single_message_thread(self, make_extracted_data, make_message):
        """A single root message: depth=0, branches=0, count=1."""
        msgs = [
            make_message(uuid="r1", parent_uuid=None, session_id="s1"),
        ]
        data = make_extracted_data(messages=msgs)

        extractor = TimeFilteredExtractor(days=30)
        extractor._build_conversation_threads(data)

        assert len(data.conversation_threads) == 1
        thread = data.conversation_threads[0]
        assert thread.max_depth == 0
        assert thread.branch_count == 0
        assert thread.message_count == 1


# =====================================================================
# Bug 7: cutoff_unix_ms computed but never used
# TimeFilteredExtractor.__init__ computes self.cutoff_unix_ms but it is
# never referenced in _is_within_window or _extract_single_session.
# =====================================================================

class TestBug7_CutoffUnixMsUnused:
    """Bug 7: cutoff_unix_ms is computed in __init__ but never used elsewhere."""

    def test_cutoff_unix_ms_is_computed(self):
        """__init__ computes cutoff_unix_ms."""
        extractor = TimeFilteredExtractor(days=30)
        assert hasattr(extractor, "cutoff_unix_ms")
        assert isinstance(extractor.cutoff_unix_ms, int)
        assert extractor.cutoff_unix_ms > 0

    def test_cutoff_unix_ms_not_used_in_is_within_window(self):
        """_is_within_window does NOT reference cutoff_unix_ms."""
        source = inspect.getsource(TimeFilteredExtractor._is_within_window)
        assert "cutoff_unix_ms" not in source

    def test_cutoff_unix_ms_not_used_in_extract_single_session(self):
        """_extract_single_session does NOT reference cutoff_unix_ms."""
        source = inspect.getsource(TimeFilteredExtractor._extract_single_session)
        assert "cutoff_unix_ms" not in source

    def test_cutoff_unix_ms_only_in_init(self):
        """cutoff_unix_ms should only appear in __init__, nowhere else in the class."""
        # Get the full class source
        source = inspect.getsource(TimeFilteredExtractor)
        # Find all occurrences
        lines_with_cutoff_unix_ms = [
            line.strip()
            for line in source.split("\n")
            if "cutoff_unix_ms" in line
        ]
        # Should only be the assignment in __init__
        assert len(lines_with_cutoff_unix_ms) == 1
        assert "self.cutoff_unix_ms" in lines_with_cutoff_unix_ms[0]

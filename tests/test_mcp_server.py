"""Tests for the MCP server tools and caching layer."""

import json
import time
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

# Skip entire module if mcp package is not installed
pytest.importorskip("mcp")

from extraction.data_classes import ExtractedData30Day, ModelUsageData
from metrics.definitions.base import METRIC_DEFINITIONS
from mcp_server import (
    CATEGORY_THEMES,
    MetricsCache,
    _definition_summary,
    _metric_result,
)


# ---------------------------------------------------------------------------
# MetricsCache tests
# ---------------------------------------------------------------------------

class TestMetricsCache:
    """Tests for the lazy, TTL-based MetricsCache."""

    def test_initial_state(self):
        cache = MetricsCache(ttl_seconds=60)
        assert cache.is_loaded is False
        assert cache.last_refresh_iso is None
        assert cache.cached_days == 30

    @patch("mcp_server.TimeFilteredExtractor")
    def test_lazy_load_on_first_access(self, mock_extractor_cls, make_extracted_data):
        data = make_extracted_data()
        mock_extractor_cls.return_value.extract.return_value = data

        cache = MetricsCache(ttl_seconds=60)
        assert cache.is_loaded is False

        result = cache.get_data(days=30)
        assert cache.is_loaded is True
        assert result is data
        mock_extractor_cls.assert_called_once_with(days=30)

    @patch("mcp_server.TimeFilteredExtractor")
    def test_cached_data_reused_within_ttl(self, mock_extractor_cls, make_extracted_data):
        data = make_extracted_data()
        mock_extractor_cls.return_value.extract.return_value = data

        cache = MetricsCache(ttl_seconds=300)
        cache.get_data(days=30)
        cache.get_data(days=30)

        # Should only extract once
        assert mock_extractor_cls.return_value.extract.call_count == 1

    @patch("mcp_server.TimeFilteredExtractor")
    def test_stale_data_refreshed_after_ttl(self, mock_extractor_cls, make_extracted_data):
        data = make_extracted_data()
        mock_extractor_cls.return_value.extract.return_value = data

        cache = MetricsCache(ttl_seconds=0)  # Immediate expiry
        cache.get_data(days=30)
        cache.get_data(days=30)

        # Should extract twice since TTL=0
        assert mock_extractor_cls.return_value.extract.call_count == 2

    @patch("mcp_server.TimeFilteredExtractor")
    def test_force_refresh(self, mock_extractor_cls, make_extracted_data):
        data = make_extracted_data()
        mock_extractor_cls.return_value.extract.return_value = data

        cache = MetricsCache(ttl_seconds=300)
        cache.get_data(days=30)
        cache.get_data(days=30, force_refresh=True)

        assert mock_extractor_cls.return_value.extract.call_count == 2

    @patch("mcp_server.TimeFilteredExtractor")
    def test_different_days_triggers_refresh(self, mock_extractor_cls, make_extracted_data):
        data = make_extracted_data()
        mock_extractor_cls.return_value.extract.return_value = data

        cache = MetricsCache(ttl_seconds=300)
        cache.get_data(days=30)
        cache.get_data(days=7)

        assert mock_extractor_cls.return_value.extract.call_count == 2
        assert cache.cached_days == 7

    @patch("mcp_server.TimeFilteredExtractor")
    def test_get_engine_returns_engine(self, mock_extractor_cls, make_extracted_data):
        data = make_extracted_data()
        mock_extractor_cls.return_value.extract.return_value = data

        cache = MetricsCache(ttl_seconds=300)
        engine = cache.get_engine(days=30)

        assert engine is not None
        assert engine.data is data

    @patch("mcp_server.TimeFilteredExtractor")
    def test_last_refresh_iso_populated(self, mock_extractor_cls, make_extracted_data):
        data = make_extracted_data()
        mock_extractor_cls.return_value.extract.return_value = data

        cache = MetricsCache(ttl_seconds=300)
        cache.get_data(days=30)

        assert cache.last_refresh_iso is not None
        # Should be a valid ISO timestamp
        datetime.fromisoformat(cache.last_refresh_iso)


# ---------------------------------------------------------------------------
# Helper function tests
# ---------------------------------------------------------------------------

class TestHelpers:

    def test_definition_summary(self):
        # Pick a known metric definition
        if not METRIC_DEFINITIONS:
            pytest.skip("No metric definitions registered")
        defn = next(iter(METRIC_DEFINITIONS.values()))
        summary = _definition_summary(defn)
        assert summary["id"] == defn.id
        assert summary["name"] == defn.name
        assert summary["category"] == defn.category
        assert "description" in summary

    def test_metric_result_unknown_id(self, make_extracted_data):
        from metrics import DerivedMetricsEngine
        data = make_extracted_data()
        engine = DerivedMetricsEngine(data)
        result = _metric_result("ZZZZ_NONEXISTENT", engine)
        assert "error" in result


# ---------------------------------------------------------------------------
# Tool function tests (import the tool functions, call them directly)
# ---------------------------------------------------------------------------

class TestGetMetricTool:

    @patch("mcp_server._cache")
    def test_returns_valid_json(self, mock_cache, make_extracted_data):
        from metrics import DerivedMetricsEngine
        data = make_extracted_data(
            sessions=[],
            messages=[],
            tool_calls=[],
        )
        engine = DerivedMetricsEngine(data)
        mock_cache.get_engine.return_value = engine

        from mcp_server import get_metric
        # Use a known metric ID
        first_id = sorted(METRIC_DEFINITIONS.keys())[0] if METRIC_DEFINITIONS else None
        if first_id is None:
            pytest.skip("No metrics defined")

        result_json = get_metric(first_id, days=30)
        result = json.loads(result_json)
        # Should have either value or error
        assert "metric_id" in result or "error" in result

    @patch("mcp_server._cache")
    def test_unknown_metric_returns_error(self, mock_cache, make_extracted_data):
        from metrics import DerivedMetricsEngine
        data = make_extracted_data()
        engine = DerivedMetricsEngine(data)
        mock_cache.get_engine.return_value = engine

        from mcp_server import get_metric
        result = json.loads(get_metric("ZZZZ999", days=30))
        assert "error" in result


class TestCalculateCategoryTool:

    @patch("mcp_server._cache")
    def test_valid_category(self, mock_cache, make_extracted_data):
        from metrics import DerivedMetricsEngine
        data = make_extracted_data(sessions=[], messages=[], tool_calls=[])
        engine = DerivedMetricsEngine(data)
        mock_cache.get_engine.return_value = engine

        from mcp_server import calculate_category
        result = json.loads(calculate_category("A", days=30))
        assert result["category"] == "A"
        assert "theme" in result
        assert "metrics" in result
        assert "count" in result

    @patch("mcp_server._cache")
    def test_unknown_category(self, mock_cache):
        from mcp_server import calculate_category
        result = json.loads(calculate_category("ZZZ_BAD", days=30))
        assert "error" in result

    @patch("mcp_server._cache")
    def test_case_insensitive(self, mock_cache, make_extracted_data):
        from metrics import DerivedMetricsEngine
        data = make_extracted_data(sessions=[], messages=[], tool_calls=[])
        engine = DerivedMetricsEngine(data)
        mock_cache.get_engine.return_value = engine

        from mcp_server import calculate_category
        result = json.loads(calculate_category("a", days=30))
        assert result["category"] == "A"


class TestGetUsageSummaryTool:

    @patch("mcp_server._cache")
    def test_returns_summary(self, mock_cache, make_extracted_data, make_session):
        sessions = [make_session(cost_usd=0.10), make_session(cost_usd=0.20)]
        data = make_extracted_data(
            sessions=sessions,
            tool_counts={"Read": 5, "Edit": 3},
            model_usage={
                "claude-sonnet-4-20250514": ModelUsageData(
                    model="claude-sonnet-4-20250514",
                    message_count=10,
                    input_tokens=5000,
                    output_tokens=3000,
                    cache_read_tokens=1000,
                    cost_usd=0.30,
                ),
            },
            active_dates=["2025-01-14", "2025-01-15"],
        )
        mock_cache.get_data.return_value = data

        from mcp_server import get_usage_summary
        result = json.loads(get_usage_summary(days=30))

        assert result["sessions"] == 2
        assert result["cost_usd"] == 0.30
        assert result["active_days"] == 2
        assert "top_tools" in result
        assert "Read" in result["top_tools"]

    @patch("mcp_server._cache")
    def test_empty_data(self, mock_cache, make_extracted_data):
        data = make_extracted_data(sessions=[], messages=[], tool_calls=[])
        mock_cache.get_data.return_value = data

        from mcp_server import get_usage_summary
        result = json.loads(get_usage_summary(days=30))
        assert result["sessions"] == 0
        assert result["cost_usd"] == 0.0


class TestSearchMetricsTool:

    def test_search_by_keyword(self):
        from mcp_server import search_metrics
        result = json.loads(search_metrics("cost"))
        # Should find metrics related to "cost" in name or description
        assert isinstance(result, list)
        # All results should have the required fields
        for item in result:
            assert "id" in item
            assert "name" in item
            assert "description" in item

    def test_search_case_insensitive(self):
        from mcp_server import search_metrics
        lower_result = json.loads(search_metrics("cost"))
        upper_result = json.loads(search_metrics("COST"))
        assert len(lower_result) == len(upper_result)

    def test_search_no_results(self):
        from mcp_server import search_metrics
        result = json.loads(search_metrics("xyzzy_impossible_query_12345"))
        assert result == []

    def test_search_max_results(self):
        from mcp_server import search_metrics
        # Search for something very common
        result = json.loads(search_metrics(""))  # Empty string matches everything
        assert len(result) <= 20


class TestCalculateMetricsTool:

    @patch("mcp_server._cache")
    def test_batch_calculate(self, mock_cache, make_extracted_data):
        from metrics import DerivedMetricsEngine
        data = make_extracted_data(sessions=[], messages=[], tool_calls=[])
        engine = DerivedMetricsEngine(data)
        mock_cache.get_engine.return_value = engine

        from mcp_server import calculate_metrics
        ids = sorted(METRIC_DEFINITIONS.keys())[:3] if METRIC_DEFINITIONS else []
        if not ids:
            pytest.skip("No metrics defined")

        result = json.loads(calculate_metrics(ids, days=30))
        assert "metrics" in result
        assert "errors" in result

    @patch("mcp_server._cache")
    def test_batch_with_invalid_id(self, mock_cache, make_extracted_data):
        from metrics import DerivedMetricsEngine
        data = make_extracted_data(sessions=[], messages=[], tool_calls=[])
        engine = DerivedMetricsEngine(data)
        mock_cache.get_engine.return_value = engine

        from mcp_server import calculate_metrics
        result = json.loads(calculate_metrics(["INVALID_ID"], days=30))
        assert len(result["errors"]) == 1


class TestGetSessionDetailsTool:

    @patch("mcp_server._cache")
    def test_returns_sessions(self, mock_cache, make_extracted_data, make_session):
        sessions = [
            make_session(session_id="s1", cost_usd=0.05, duration_ms=600_000),
            make_session(session_id="s2", cost_usd=0.10, duration_ms=300_000),
        ]
        data = make_extracted_data(sessions=sessions)
        mock_cache.get_data.return_value = data

        from mcp_server import get_session_details
        result = json.loads(get_session_details(days=7, limit=10))

        assert len(result) == 2
        assert "session_id" in result[0]
        assert "project" in result[0]
        assert "duration_min" in result[0]
        assert "cost_usd" in result[0]

    @patch("mcp_server._cache")
    def test_limit_respected(self, mock_cache, make_extracted_data, make_session):
        sessions = [make_session() for _ in range(5)]
        data = make_extracted_data(sessions=sessions)
        mock_cache.get_data.return_value = data

        from mcp_server import get_session_details
        result = json.loads(get_session_details(days=7, limit=2))
        assert len(result) == 2

    @patch("mcp_server._cache")
    def test_empty_sessions(self, mock_cache, make_extracted_data):
        data = make_extracted_data(sessions=[])
        mock_cache.get_data.return_value = data

        from mcp_server import get_session_details
        result = json.loads(get_session_details(days=7))
        assert result == []


class TestRefreshDataTool:

    @patch("mcp_server._cache")
    def test_refresh(self, mock_cache, make_extracted_data, make_session):
        data = make_extracted_data(sessions=[make_session()])
        mock_cache.get_data.return_value = data

        from mcp_server import refresh_data
        result = json.loads(refresh_data(days=30))

        assert result["status"] == "refreshed"
        assert result["sessions"] == 1
        mock_cache.get_data.assert_called_once_with(days=30, force_refresh=True)


# ---------------------------------------------------------------------------
# Resource tests
# ---------------------------------------------------------------------------

class TestResources:

    def test_metrics_catalog(self):
        from mcp_server import metrics_catalog
        result = json.loads(metrics_catalog())
        assert isinstance(result, list)
        assert len(result) == len(METRIC_DEFINITIONS)
        # Check structure
        if result:
            assert "id" in result[0]
            assert "name" in result[0]
            assert "category" in result[0]

    def test_metrics_categories(self):
        from mcp_server import metrics_categories
        result = json.loads(metrics_categories())
        assert isinstance(result, list)
        assert len(result) > 0
        first = result[0]
        assert "category" in first
        assert "theme" in first
        assert "count" in first
        assert "id_range" in first

    def test_metrics_status_unloaded(self):
        # Test with a fresh cache that hasn't been loaded
        import mcp_server
        original_cache = mcp_server._cache

        try:
            mcp_server._cache = MetricsCache()
            result = json.loads(mcp_server.metrics_status())
            assert result["loaded"] is False
            assert result["last_refresh"] is None
            assert result["sessions"] is None
        finally:
            mcp_server._cache = original_cache


# ---------------------------------------------------------------------------
# CATEGORY_THEMES completeness
# ---------------------------------------------------------------------------

class TestCategoryThemes:

    def test_all_categories_have_themes(self):
        """Every category in CATEGORY_ORDER should have a theme."""
        from metrics import DerivedMetricsEngine
        for cat in DerivedMetricsEngine.CATEGORY_ORDER:
            assert cat in CATEGORY_THEMES, f"Missing theme for category {cat}"

    def test_theme_values_are_strings(self):
        for cat, theme in CATEGORY_THEMES.items():
            assert isinstance(theme, str)
            assert len(theme) > 0

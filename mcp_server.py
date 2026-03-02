#!/usr/bin/env python3
"""MCP server for Claude Code self-introspection.

Exposes claude_metrics as an MCP server so Claude Code can introspect
on its own usage patterns in real-time during any conversation.
"""

import json
import threading
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    FastMCP = None

from extraction import TimeFilteredExtractor
from extraction.data_classes import ExtractedData30Day
from metrics import DerivedMetricsEngine
from metrics.definitions.base import (
    METRIC_DEFINITIONS,
    MetricDefinition,
    get_metric,
    get_metrics_by_category,
)

# ---------------------------------------------------------------------------
# Caching layer
# ---------------------------------------------------------------------------

class MetricsCache:
    """Lazy, TTL-based cache for extracted data and metrics engine.

    - Lazy: only extracts on first access, not on server startup.
    - TTL: cached data expires after ``ttl_seconds`` (default 300 = 5 min).
    - Thread-safe via a reentrant lock.
    """

    def __init__(self, ttl_seconds: int = 300):
        self.ttl_seconds = ttl_seconds
        self._lock = threading.RLock()
        self._data: Optional[ExtractedData30Day] = None
        self._engine: Optional[DerivedMetricsEngine] = None
        self._days: int = 30
        self._last_refresh: float = 0.0

    def _is_stale(self) -> bool:
        if self._data is None:
            return True
        return (time.monotonic() - self._last_refresh) > self.ttl_seconds

    def _refresh(self, days: int) -> None:
        extractor = TimeFilteredExtractor(days=days)
        self._data = extractor.extract()
        self._engine = DerivedMetricsEngine(self._data)
        self._days = days
        self._last_refresh = time.monotonic()

    def get_data(self, days: int = 30, force_refresh: bool = False) -> ExtractedData30Day:
        with self._lock:
            if force_refresh or self._is_stale() or days != self._days:
                self._refresh(days)
            assert self._data is not None
            return self._data

    def get_engine(self, days: int = 30, force_refresh: bool = False) -> DerivedMetricsEngine:
        with self._lock:
            if force_refresh or self._is_stale() or days != self._days:
                self._refresh(days)
            assert self._engine is not None
            return self._engine

    @property
    def last_refresh_iso(self) -> Optional[str]:
        if self._last_refresh == 0.0:
            return None
        # Convert monotonic offset to wall-clock approximation
        age = time.monotonic() - self._last_refresh
        ts = datetime.now(timezone.utc).timestamp() - age
        return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()

    @property
    def cached_days(self) -> int:
        return self._days

    @property
    def is_loaded(self) -> bool:
        return self._data is not None


# ---------------------------------------------------------------------------
# Server + cache singleton
# ---------------------------------------------------------------------------

if FastMCP is not None:
    mcp = FastMCP(
        "claude-metrics",
        instructions="Claude Code self-introspection: 612 derived metrics from local usage data",
    )
else:
    mcp = None

_cache = MetricsCache()


# ---------------------------------------------------------------------------
# Helper: serialise a MetricValue for tool output
# ---------------------------------------------------------------------------

def _metric_result(metric_id: str, engine: DerivedMetricsEngine) -> Dict[str, Any]:
    """Calculate a single metric and return a JSON-friendly dict."""
    definition = METRIC_DEFINITIONS.get(metric_id)
    if definition is None:
        return {"error": f"Unknown metric ID: {metric_id}"}

    value = engine.calculate_metric(metric_id)
    if value is None:
        return {"error": f"Calculation failed for {metric_id}"}

    result: Dict[str, Any] = {
        "metric_id": metric_id,
        "name": definition.name,
        "value": value.value,
        "unit": definition.unit,
        "description": definition.description,
        "category": definition.category,
        "type": definition.metric_type.value,
    }
    if value.breakdown:
        result["breakdown"] = value.breakdown
    if value.trend is not None:
        result["trend"] = value.trend
    return result


def _definition_summary(d: MetricDefinition) -> Dict[str, str]:
    return {
        "id": d.id,
        "name": d.name,
        "category": d.category,
        "type": d.metric_type.value,
        "unit": d.unit or "",
        "description": d.description,
    }


# ---------------------------------------------------------------------------
# Category themes (for catalog / calculate_category output)
# ---------------------------------------------------------------------------

CATEGORY_THEMES: Dict[str, str] = {
    "A": "Time and Activity Patterns",
    "B": "Tool Usage and Distribution",
    "C": "File Operations",
    "D": "Model and Token Usage",
    "E": "Conversation Depth",
    "F": "Thinking Patterns",
    "G": "Task Management",
    "H": "Agent Sessions",
    "I": "Project Analysis",
    "J": "Error Rates and Recovery",
    "K": "Code Generation",
    "L": "Web and Search",
    "M": "Hooks and Automation",
    "N": "Question Patterns",
    "O": "Productivity Scoring",
    "P": "Project Analytics",
    "Q": "Session Timeline",
    "R": "Tool Discovery",
    "S": "Background Tasks",
    "T": "Top Project Analysis",
    "U": "Cost Analysis",
    "V": "Project Hooks",
    "W": "MCP Servers",
    "X": "Current Session",
    "Y": "Tool-to-File Ratios",
    "Z": "Work Patterns",
    "AA": "Cognitive Load",
    "AB": "Skill Progression",
    "AC": "Code Review",
    "AD": "Single Responsibility",
    "AE": "Cost per Task",
    "AF": "Problem Decomposition",
    "AG": "Self-Correction",
    "AH": "Project Interconnection",
    "AI": "Permission Requests",
    "AJ": "Work Rhythm",
    "AK": "Customization Usage",
    "AL": "Cache Savings",
    "AM": "Circadian Alignment",
    "AN": "Session Entropy",
    "AO": "Tool Predictability",
    "AP": "Exploration Payoff",
    "AQ": "Expertise Stage",
    "AR": "Feedback Responsiveness",
    "AS": "Session Quality",
    "AT": "Tool Ecosystem",
    "AU": "Error Detection",
    "AV": "Workflow Efficiency",
    "AW": "Question-Response",
    "AX": "Cognitive Efficiency",
    "AY": "Metrics Coverage",
    "AZ": "Knowledge Acquisition",
    "BA": "Session Narrative",
    "BB": "Engagement Intensity",
    "BC": "Conversation Analysis",
}


# ===================================================================
# Tools and Resources (only defined when mcp package is available)
# ===================================================================

if mcp is not None:

    @mcp.tool()
    def get_metric(metric_id: str, days: int = 30) -> str:
        """Get a single metric value by ID.

        Args:
            metric_id: Metric identifier (e.g. "D001", "D029").
            days: Time window in days (default 30).

        Returns:
            JSON with metric_id, name, value, unit, description, breakdown, trend.
        """
        engine = _cache.get_engine(days=days)
        return json.dumps(_metric_result(metric_id, engine), default=str)


    @mcp.tool()
    def calculate_category(category: str, days: int = 30) -> str:
        """Calculate all metrics in a category.

        Args:
            category: Category letter(s), e.g. "A", "D", "AA", "BC".
            days: Time window in days (default 30).

        Returns:
            JSON with category, theme, metrics list, and count.
        """
        category = category.upper()
        definitions = get_metrics_by_category(category)
        if not definitions:
            return json.dumps({"error": f"Unknown category: {category}"})

        engine = _cache.get_engine(days=days)
        engine.calculate_all(categories=[category])

        metrics = []
        for d in sorted(definitions, key=lambda x: x.id):
            mv = engine.cache.get(d.id)
            if mv is not None:
                metrics.append({
                    "id": d.id,
                    "name": d.name,
                    "value": mv.value,
                    "unit": d.unit or "",
                })

        return json.dumps({
            "category": category,
            "theme": CATEGORY_THEMES.get(category, ""),
            "metrics": metrics,
            "count": len(metrics),
        }, default=str)


    @mcp.tool()
    def get_usage_summary(days: int = 30) -> str:
        """High-level usage overview -- fast, no metric calculation needed.

        Args:
            days: Time window in days (default 30).

        Returns:
            JSON with sessions, messages, tool_calls, cost, active_days,
            top_tools, top_models, window start/end.
        """
        data = _cache.get_data(days=days)

        # Top tools (sorted by count descending)
        top_tools = dict(
            sorted(data.tool_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        )

        # Top models (sorted by cost descending)
        top_models = {
            m.model: {"messages": m.message_count, "cost_usd": round(m.cost_usd, 4)}
            for m in sorted(
                data.model_usage.values(), key=lambda x: x.cost_usd, reverse=True
            )[:5]
        }

        return json.dumps({
            "sessions": data.total_sessions,
            "messages": data.total_messages,
            "tool_calls": data.total_tool_calls,
            "cost_usd": round(data.total_cost_usd, 4),
            "active_days": len(data.active_dates),
            "top_tools": top_tools,
            "top_models": top_models,
            "total_tokens": data.total_tokens,
            "window_start": data.window_start.isoformat(),
            "window_end": data.window_end.isoformat(),
            "window_days": data.window_days,
        }, default=str)


    @mcp.tool()
    def search_metrics(query: str) -> str:
        """Find metrics by keyword search in name and description.

        Args:
            query: Search term (case-insensitive substring match).

        Returns:
            JSON list of matching metric definitions (max 20).
        """
        query_lower = query.lower()
        results: List[Dict[str, str]] = []

        for d in METRIC_DEFINITIONS.values():
            if query_lower in d.name.lower() or query_lower in d.description.lower():
                results.append(_definition_summary(d))
                if len(results) >= 20:
                    break

        return json.dumps(results)


    @mcp.tool()
    def calculate_metrics(metric_ids: list[str], days: int = 30) -> str:
        """Batch calculate specific metrics by ID.

        Args:
            metric_ids: List of metric IDs to calculate (e.g. ["D001", "D029"]).
            days: Time window in days (default 30).

        Returns:
            JSON with metrics list and any errors.
        """
        engine = _cache.get_engine(days=days)
        metrics: List[Dict[str, Any]] = []
        errors: List[str] = []

        for mid in metric_ids:
            result = _metric_result(mid, engine)
            if "error" in result:
                errors.append(result["error"])
            else:
                metrics.append(result)

        return json.dumps({"metrics": metrics, "errors": errors}, default=str)


    @mcp.tool()
    def get_session_details(days: int = 7, limit: int = 10) -> str:
        """Detailed breakdown of recent sessions.

        Args:
            days: Time window in days (default 7).
            limit: Maximum sessions to return (default 10).

        Returns:
            JSON list of session details (project, duration, messages,
            tools, cost, model).
        """
        data = _cache.get_data(days=days)
        sessions = sorted(data.sessions, key=lambda s: s.start_time, reverse=True)[:limit]

        result = []
        for s in sessions:
            result.append({
                "session_id": s.session_id,
                "project": s.project_path,
                "start": s.start_time.isoformat(),
                "duration_min": round(s.duration_ms / 60_000, 1) if s.duration_ms else 0,
                "messages": s.message_count,
                "tools": s.tool_call_count,
                "cost_usd": round(s.cost_usd, 4),
                "model": s.model,
                "is_agent": s.is_agent,
            })

        return json.dumps(result, default=str)


    @mcp.tool()
    def refresh_data(days: int = 30) -> str:
        """Force cache invalidation and re-extraction.

        Args:
            days: Time window in days (default 30).

        Returns:
            JSON confirmation with session/message/tool counts.
        """
        data = _cache.get_data(days=days, force_refresh=True)
        return json.dumps({
            "status": "refreshed",
            "sessions": data.total_sessions,
            "messages": data.total_messages,
            "tool_calls": data.total_tool_calls,
            "window_start": data.window_start.isoformat(),
            "window_end": data.window_end.isoformat(),
        }, default=str)


    # ===================================================================
    # Resources
    # ===================================================================

    @mcp.resource("metrics://catalog")
    def metrics_catalog() -> str:
        """Complete catalog of all 612 metric definitions."""
        catalog = [_definition_summary(d) for d in sorted(METRIC_DEFINITIONS.values(), key=lambda x: x.id)]
        return json.dumps(catalog)


    @mcp.resource("metrics://categories")
    def metrics_categories() -> str:
        """All 55 categories with ID ranges, counts, and themes."""
        categories = []
        for cat_id in DerivedMetricsEngine.CATEGORY_ORDER:
            defs = get_metrics_by_category(cat_id)
            if not defs:
                continue
            ids = sorted(d.id for d in defs)
            categories.append({
                "category": cat_id,
                "theme": CATEGORY_THEMES.get(cat_id, ""),
                "count": len(defs),
                "id_range": f"{ids[0]}-{ids[-1]}" if ids else "",
            })
        return json.dumps(categories)


    @mcp.resource("metrics://status")
    def metrics_status() -> str:
        """Current cache status: loaded, last refresh, data window."""
        return json.dumps({
            "loaded": _cache.is_loaded,
            "last_refresh": _cache.last_refresh_iso,
            "cached_days": _cache.cached_days,
            "sessions": _cache._data.total_sessions if _cache._data else None,
            "messages": _cache._data.total_messages if _cache._data else None,
            "tool_calls": _cache._data.total_tool_calls if _cache._data else None,
            "window_start": _cache._data.window_start.isoformat() if _cache._data else None,
            "window_end": _cache._data.window_end.isoformat() if _cache._data else None,
        })


# ===================================================================
# Entry point
# ===================================================================

def main():
    """Run the MCP server via stdio transport."""
    if mcp is None:
        import sys
        print(
            "Error: mcp package required. Install with: pip install 'claude-metrics[mcp]'",
            file=sys.stderr,
        )
        sys.exit(1)
    mcp.run()


if __name__ == "__main__":
    main()

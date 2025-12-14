"""HTML dashboard generator for Claude Metrics."""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape

from extraction.data_classes import ExtractedData30Day
from metrics.definitions.base import MetricValue

from .charts import (
    LineChart,
    BarChart,
    PieChart,
    GaugeChart,
    HeatmapChart,
    ChartConfig,
)
from .charts.line import LineSeries
from .charts.bar import BarSeries


class DashboardGenerator:
    """Generate HTML dashboard from metrics data."""

    def __init__(
        self,
        data: ExtractedData30Day,
        metrics: Dict[str, MetricValue],
        template_dir: Optional[Path] = None,
    ):
        """Initialize the dashboard generator.

        Args:
            data: Extracted data for the time window
            metrics: Calculated metric values
            template_dir: Custom template directory (optional)
        """
        self.data = data
        self.metrics = metrics

        # Set up Jinja2 environment
        if template_dir is None:
            template_dir = Path(__file__).parent / "templates"

        self.env = Environment(
            loader=FileSystemLoader(str(template_dir)),
            autoescape=select_autoescape(["html", "xml"]),
        )

        # Add custom filters
        self.env.filters["format_number"] = self._format_number
        self.env.filters["format_currency"] = self._format_currency
        self.env.filters["format_percentage"] = self._format_percentage

    def get_metric(self, metric_id: str, default: Any = None) -> Any:
        """Get a metric value by ID."""
        if metric_id in self.metrics:
            return self.metrics[metric_id].value
        return default

    def generate(self, output_path: Optional[Path] = None) -> str:
        """Generate the HTML dashboard.

        Args:
            output_path: Optional path to write the HTML file

        Returns:
            The generated HTML string
        """
        # Build template context
        context = self._build_context()

        # Render template
        template = self.env.get_template("dashboard.html")
        html = template.render(**context)

        # Write to file if path provided
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(html, encoding="utf-8")

        return html

    def _build_context(self) -> Dict[str, Any]:
        """Build the template context with all data and charts."""
        context = {
            # Window info
            "window_days": self.data.window_days,
            "window_start": self.data.window_start.strftime("%Y-%m-%d"),
            "window_end": self.data.window_end.strftime("%Y-%m-%d"),
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "metrics_count": len(self.metrics),

            # Summary metrics
            "total_sessions": self.data.total_sessions,
            "total_messages": self.data.total_messages,
            "total_tool_calls": self.data.total_tool_calls,
            "total_cost": self.data.total_cost_usd,
            "sessions_per_day": self.get_metric("D026", 0),
            "messages_per_session": self._safe_div(self.data.total_messages, self.data.total_sessions),
            "tools_per_message": self.get_metric("D034", 0),
            "cost_per_session": self.get_metric("D098", 0),

            # Activity metrics
            "active_days": int(self.get_metric("D024", 0)),
            "current_streak": int(self.get_metric("D022", 0)),
            "peak_hour": self.get_metric("D011", 12),
            "avg_session_duration": self._format_duration_ms(self.get_metric("D007", 0)),

            # Tool metrics
            "most_used_tool": self.get_metric("D030", "N/A"),
            "most_used_tool_count": self._get_most_used_tool_count(),
            "tool_success_rate": self.get_metric("D037", 0),
            "unique_tools": len(self.data.tool_counts),

            # File metrics
            "files_read": int(self.get_metric("D049", 0)),
            "files_edited": int(self.get_metric("D050", 0)),
            "read_write_ratio": self.get_metric("D055", 0),
            "file_churn": self.get_metric("D068", 0),

            # Model metrics
            "primary_model": self._get_primary_model(),
            "total_tokens": self.data.total_tokens.get("input", 0) + self.data.total_tokens.get("output", 0),
            "cache_hit_rate": self.get_metric("D089", 0),
            "cache_savings": self.get_metric("D093", 0),

            # Cost metrics
            "daily_cost": self.get_metric("D095", 0),
            "cost_per_message": self.get_metric("D099", 0),

            # Charts
            "daily_activity_chart": self._create_daily_activity_chart(),
            "hourly_chart": self._create_hourly_chart(),
            "tool_distribution_chart": self._create_tool_distribution_chart(),
            "tool_trend_chart": self._create_tool_trend_chart(),
            "file_type_chart": self._create_file_type_chart(),
            "file_ops_chart": self._create_file_ops_chart(),
            "model_distribution_chart": self._create_model_distribution_chart(),
            "token_chart": self._create_token_chart(),
            "cost_trend_chart": self._create_cost_trend_chart(),
            "cost_model_chart": self._create_cost_model_chart(),
        }

        return context

    def _create_daily_activity_chart(self) -> Optional[Dict[str, Any]]:
        """Create daily activity line chart."""
        if not self.data.daily_activity:
            return None

        dates = [d.date for d in self.data.daily_activity]
        messages = [d.message_count for d in self.data.daily_activity]
        sessions = [d.session_count for d in self.data.daily_activity]

        chart = LineChart(ChartConfig(height=300, show_legend=True))
        return chart.create(
            [
                LineSeries(x=dates, y=messages, name="Messages"),
                LineSeries(x=dates, y=sessions, name="Sessions"),
            ],
            x_title="Date",
            y_title="Count",
        )

    def _create_hourly_chart(self) -> Optional[Dict[str, Any]]:
        """Create hourly activity bar chart."""
        hourly = self.data.hourly_distribution
        if not hourly:
            return None

        hours = list(range(24))
        counts = [hourly.get(h, 0) for h in hours]
        labels = [f"{h:02d}:00" for h in hours]

        chart = BarChart(ChartConfig(height=300, show_legend=False))
        return chart.create(
            BarSeries(x=labels, y=counts),
            x_title="Hour",
            y_title="Activity",
        )

    def _create_tool_distribution_chart(self) -> Optional[Dict[str, Any]]:
        """Create tool distribution pie chart."""
        if not self.data.tool_counts:
            return None

        # Get top 8 tools
        sorted_tools = sorted(
            self.data.tool_counts.items(), key=lambda x: -x[1]
        )[:8]

        chart = PieChart(ChartConfig(height=300))
        return chart.create(
            dict(sorted_tools),
            hole=0.4,
            text_info="percent+label",
        )

    def _create_tool_trend_chart(self) -> Optional[Dict[str, Any]]:
        """Create tool usage trend line chart."""
        if not self.data.daily_activity:
            return None

        dates = [d.date for d in self.data.daily_activity]
        tool_calls = [d.tool_call_count for d in self.data.daily_activity]

        chart = LineChart(ChartConfig(height=300, show_legend=False))
        return chart.create(
            LineSeries(x=dates, y=tool_calls, name="Tool Calls", fill="tozeroy"),
            x_title="Date",
            y_title="Tool Calls",
        )

    def _create_file_type_chart(self) -> Optional[Dict[str, Any]]:
        """Create file type distribution chart."""
        file_dist = self.get_metric("D058", {})
        if not file_dist:
            return None

        # Get top 6 file types
        sorted_types = sorted(file_dist.items(), key=lambda x: -x[1])[:6]

        chart = PieChart(ChartConfig(height=300))
        return chart.create(dict(sorted_types), hole=0.4)

    def _create_file_ops_chart(self) -> Optional[Dict[str, Any]]:
        """Create file operations bar chart."""
        reads = len(self.data.files_read)
        edits = len(self.data.files_edited)

        if reads == 0 and edits == 0:
            return None

        chart = BarChart(ChartConfig(height=300, show_legend=False))
        return chart.create(
            {"Files Read": reads, "Files Edited": edits},
            show_values=True,
        )

    def _create_model_distribution_chart(self) -> Optional[Dict[str, Any]]:
        """Create model usage distribution chart."""
        model_dist = self.get_metric("D074", {})
        if not model_dist:
            # Fall back to session model counts
            model_counts = {}
            for session in self.data.sessions:
                if session.model:
                    model_counts[session.model] = model_counts.get(session.model, 0) + 1
            if not model_counts:
                return None
            model_dist = model_counts

        chart = PieChart(ChartConfig(height=300))
        return chart.create(model_dist, hole=0.4)

    def _create_token_chart(self) -> Optional[Dict[str, Any]]:
        """Create token usage bar chart."""
        input_tokens = self.data.total_tokens.get("input", 0)
        output_tokens = self.data.total_tokens.get("output", 0)
        cache_tokens = self.data.total_tokens.get("cache_read", 0)

        if input_tokens == 0 and output_tokens == 0:
            return None

        chart = BarChart(ChartConfig(height=300, show_legend=False))
        return chart.create(
            {"Input": input_tokens, "Output": output_tokens, "Cache": cache_tokens},
            show_values=True,
            horizontal=True,
        )

    def _create_cost_trend_chart(self) -> Optional[Dict[str, Any]]:
        """Create cost trend line chart."""
        if not self.data.daily_activity:
            return None

        dates = [d.date for d in self.data.daily_activity]
        costs = [d.cost_usd for d in self.data.daily_activity]

        chart = LineChart(ChartConfig(height=300, show_legend=False))
        return chart.create(
            LineSeries(x=dates, y=costs, name="Cost", fill="tozeroy"),
            x_title="Date",
            y_title="Cost (USD)",
        )

    def _create_cost_model_chart(self) -> Optional[Dict[str, Any]]:
        """Create cost by model chart."""
        cost_dist = self.get_metric("D101", {})
        if not cost_dist:
            return None

        chart = PieChart(ChartConfig(height=300))
        return chart.create(cost_dist, hole=0.4)

    def _get_most_used_tool_count(self) -> int:
        """Get the count for the most used tool."""
        if not self.data.tool_counts:
            return 0
        return max(self.data.tool_counts.values())

    def _get_primary_model(self) -> str:
        """Get the primary model name, shortened."""
        model = self.get_metric("D079", "N/A")
        if model and len(model) > 15:
            # Shorten long model names
            if "sonnet" in model.lower():
                return "Sonnet"
            elif "opus" in model.lower():
                return "Opus"
            elif "haiku" in model.lower():
                return "Haiku"
            return model[:15] + "..."
        return model

    @staticmethod
    def _safe_div(a: float, b: float) -> float:
        """Safe division returning 0 if divisor is 0."""
        return a / b if b else 0

    @staticmethod
    def _format_number(value: Any, decimals: int = 0) -> str:
        """Format a number with thousands separator."""
        if value is None:
            return "0"
        try:
            if decimals > 0:
                return f"{float(value):,.{decimals}f}"
            return f"{int(value):,}"
        except (ValueError, TypeError):
            return str(value)

    @staticmethod
    def _format_currency(value: Any, decimals: int = 2) -> str:
        """Format a value as currency."""
        if value is None:
            return "$0.00"
        try:
            return f"${float(value):,.{decimals}f}"
        except (ValueError, TypeError):
            return "$0.00"

    @staticmethod
    def _format_percentage(value: Any) -> str:
        """Format a ratio as percentage."""
        if value is None:
            return "0%"
        try:
            return f"{float(value) * 100:.1f}%"
        except (ValueError, TypeError):
            return "0%"

    @staticmethod
    def _format_duration_ms(ms: float) -> str:
        """Format milliseconds as human-readable duration."""
        if not ms or ms <= 0:
            return "0m"
        seconds = ms / 1000
        if seconds < 60:
            return f"{int(seconds)}s"
        minutes = seconds / 60
        if minutes < 60:
            return f"{int(minutes)}m"
        hours = minutes / 60
        if hours < 24:
            return f"{hours:.1f}h"
        days = hours / 24
        return f"{days:.1f}d"

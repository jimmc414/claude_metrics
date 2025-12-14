"""Terminal report generator for Claude Metrics."""

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple

from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.columns import Columns
from rich.rule import Rule
from rich import box

from extraction.data_classes import ExtractedData30Day
from metrics.definitions.base import MetricValue, METRIC_DEFINITIONS
from .components import (
    create_sparkline,
    create_bar_chart,
    create_progress_bar,
    create_gauge,
    create_metric_panel,
    create_distribution_table,
    create_trend_indicator,
    create_summary_row,
    format_duration,
    format_duration_ms,
    format_currency,
    format_number,
    format_percentage,
    format_ratio,
)
from .themes import Theme, get_theme


class TerminalReport:
    """Generate terminal reports for Claude Metrics."""

    def __init__(
        self,
        data: ExtractedData30Day,
        metrics: Dict[str, MetricValue],
        theme: Optional[Theme] = None,
        console: Optional[Console] = None,
    ):
        """Initialize the report generator.

        Args:
            data: Extracted data for the time window
            metrics: Calculated metric values
            theme: Color theme
            console: Rich console (created if not provided)
        """
        self.data = data
        self.metrics = metrics
        self.theme = theme or get_theme()
        self.console = console or Console()

    def get_metric(self, metric_id: str, default: Any = None) -> Any:
        """Get a metric value by ID.

        Args:
            metric_id: The metric ID
            default: Default value if not found

        Returns:
            The metric value or default
        """
        if metric_id in self.metrics:
            return self.metrics[metric_id].value
        return default

    def print_full_report(self) -> None:
        """Print the complete metrics report."""
        self.print_header()
        self.print_summary()
        self.console.print()
        self.print_activity_section()
        self.console.print()
        self.print_tools_section()
        self.console.print()
        self.print_files_section()
        self.console.print()
        self.print_models_section()
        self.console.print()
        self.print_cost_section()
        self.console.print()
        self.print_footer()

    def print_header(self) -> None:
        """Print report header."""
        start_str = self.data.window_start.strftime("%Y-%m-%d")
        end_str = self.data.window_end.strftime("%Y-%m-%d")

        header = Panel(
            Text.from_markup(
                f"[bold]CLAUDE CODE METRICS - {self.data.window_days} DAY REPORT[/bold]\n"
                f"[dim]{start_str} to {end_str}[/dim]"
            ),
            box=box.DOUBLE,
            border_style=self.theme.primary,
            padding=(0, 2),
        )
        self.console.print(header)

    def print_summary(self) -> None:
        """Print executive summary section."""
        self.console.print()
        self.console.print(
            Rule(
                "[bold]KEY METRICS SUMMARY[/bold]",
                style=self.theme.primary,
            )
        )
        self.console.print()

        # Build summary items
        items = [
            (
                "Sessions",
                format_number(self.data.total_sessions),
                "",
            ),
            (
                "Messages",
                format_number(self.data.total_messages),
                "",
            ),
            (
                "Tool Calls",
                format_number(self.data.total_tool_calls),
                "",
            ),
            (
                "Total Cost",
                format_currency(self.data.total_cost_usd),
                "",
            ),
        ]

        self.console.print(create_summary_row(items, self.theme))

        # Second row with derived metrics
        avg_session = self.get_metric("D007", 0)
        session_freq = self.get_metric("D026", 0)
        active_days = self.get_metric("D024", 0)
        cost_per_session = self.get_metric("D098", 0)

        items2 = [
            (
                "Avg Session",
                format_duration_ms(avg_session),
                "",
            ),
            (
                "Sessions/Day",
                format_ratio(session_freq),
                "",
            ),
            (
                "Active Days",
                str(int(active_days)),
                "",
            ),
            (
                "Cost/Session",
                format_currency(cost_per_session),
                "",
            ),
        ]

        self.console.print(create_summary_row(items2, self.theme))

    def print_activity_section(self) -> None:
        """Print activity and time metrics section."""
        self.console.print(
            Rule(
                "[bold]ACTIVITY PATTERNS[/bold]",
                style=self.theme.primary,
            )
        )
        self.console.print()

        # Daily activity sparkline
        if self.data.daily_activity:
            daily_msgs = [d.message_count for d in self.data.daily_activity]
            daily_sessions = [d.session_count for d in self.data.daily_activity]

            self.console.print(f"  Daily Messages   [{self.theme.sparkline}]{create_sparkline(daily_msgs, 30)}[/]")
            self.console.print(f"  Daily Sessions   [{self.theme.sparkline}]{create_sparkline(daily_sessions, 30)}[/]")
            self.console.print()

        # Hourly distribution
        hourly = self.data.hourly_distribution
        if hourly:
            # Create hour groups
            morning = sum(hourly.get(h, 0) for h in range(6, 12))
            afternoon = sum(hourly.get(h, 0) for h in range(12, 18))
            evening = sum(hourly.get(h, 0) for h in range(18, 24))
            night = sum(hourly.get(h, 0) for h in range(0, 6))

            time_dist = {
                "Morning (6-12)": morning,
                "Afternoon (12-18)": afternoon,
                "Evening (18-24)": evening,
                "Night (0-6)": night,
            }

            self.console.print(
                create_bar_chart(time_dist, max_width=30, theme=self.theme)
            )
            self.console.print()

        # Activity metrics table
        metrics_data = [
            ("Daily Active Hours", self.get_metric("D001", 0), "hours"),
            ("Weekly Active Hours", self.get_metric("D002", 0), "hours"),
            ("Monthly Active Hours", self.get_metric("D003", 0), "hours"),
            ("Peak Activity Hour", self.get_metric("D011", "-"), None),
            ("Longest Session", format_duration_ms(self.get_metric("D006", 0)), None),
            ("Current Streak", self.get_metric("D022", 0), "days"),
            ("Longest Streak", self.get_metric("D021", 0), "days"),
        ]

        self.console.print(
            create_metric_panel("Time Metrics", metrics_data, self.theme)
        )

    def print_tools_section(self) -> None:
        """Print tool usage section."""
        self.console.print(
            Rule(
                "[bold]TOOL USAGE[/bold]",
                style=self.theme.primary,
            )
        )
        self.console.print()

        # Tool distribution
        tool_dist = self.get_metric("D029", {})
        if tool_dist:
            # Convert ratios to counts
            tool_counts = self.data.tool_counts
            if tool_counts:
                self.console.print(
                    create_bar_chart(
                        dict(list(tool_counts.items())[:8]),
                        max_width=40,
                        theme=self.theme,
                    )
                )
                self.console.print()

        # Tool metrics
        metrics_data = [
            ("Most Used Tool", self.get_metric("D030", "-"), None),
            ("Tool Diversity", format_ratio(self.get_metric("D031", 0)), "entropy"),
            ("Tools/Session", format_ratio(self.get_metric("D033", 0)), None),
            ("Tools/Message", format_ratio(self.get_metric("D034", 0)), None),
            ("Success Rate", format_percentage(self.get_metric("D037", 0)), None),
            ("Bash/Edit Ratio", format_ratio(self.get_metric("D035", 0)), None),
        ]

        self.console.print(
            create_metric_panel("Tool Metrics", metrics_data, self.theme)
        )

    def print_files_section(self) -> None:
        """Print file operations section."""
        self.console.print(
            Rule(
                "[bold]FILE OPERATIONS[/bold]",
                style=self.theme.primary,
            )
        )
        self.console.print()

        # File type distribution
        file_dist = self.get_metric("D058", {})
        if file_dist:
            # Get top file types
            top_types = dict(
                sorted(file_dist.items(), key=lambda x: -x[1])[:6]
            )
            self.console.print(
                create_bar_chart(top_types, max_width=30, theme=self.theme)
            )
            self.console.print()

        # File metrics
        metrics_data = [
            ("Files Read", self.get_metric("D049", 0), "unique"),
            ("Files Edited", self.get_metric("D050", 0), "unique"),
            ("Most Read File", self._truncate_path(self.get_metric("D053", "-")), None),
            ("Most Edited File", self._truncate_path(self.get_metric("D054", "-")), None),
            ("Read/Write Ratio", format_ratio(self.get_metric("D055", 0)), None),
            ("File Churn Rate", format_ratio(self.get_metric("D068", 0)), "edits/day"),
        ]

        self.console.print(
            create_metric_panel("File Metrics", metrics_data, self.theme)
        )

    def print_models_section(self) -> None:
        """Print model usage section."""
        self.console.print(
            Rule(
                "[bold]MODEL USAGE[/bold]",
                style=self.theme.primary,
            )
        )
        self.console.print()

        # Model distribution
        model_dist = self.get_metric("D074", {})
        if model_dist:
            # Convert to percentages
            model_pcts = {k: v * 100 for k, v in model_dist.items()}
            self.console.print(
                create_bar_chart(
                    model_pcts,
                    max_width=35,
                    show_percentages=False,
                    theme=self.theme,
                )
            )
            self.console.print()

        # Model metrics
        primary_model = self.get_metric("D079", "-")
        opus_ratio = self.get_metric("D075", 0)
        sonnet_ratio = self.get_metric("D076", 0)
        haiku_ratio = self.get_metric("D077", 0)

        metrics_data = [
            ("Primary Model", primary_model, None),
            ("Opus Usage", format_percentage(opus_ratio), None),
            ("Sonnet Usage", format_percentage(sonnet_ratio), None),
            ("Haiku Usage", format_percentage(haiku_ratio), None),
            ("Switch Rate", format_percentage(self.get_metric("D078", 0)), "per session"),
        ]

        self.console.print(
            create_metric_panel("Model Metrics", metrics_data, self.theme)
        )

    def print_cost_section(self) -> None:
        """Print cost and token metrics section."""
        self.console.print(
            Rule(
                "[bold]COST & TOKENS[/bold]",
                style=self.theme.primary,
            )
        )
        self.console.print()

        # Token metrics
        input_tokens = self.get_metric("D084", 0)
        output_tokens = self.get_metric("D085", 0)
        cache_tokens = self.get_metric("D091", 0)
        total_tokens = input_tokens + output_tokens

        # Token bar chart
        token_data = {
            "Input": input_tokens,
            "Output": output_tokens,
            "Cache": cache_tokens,
        }
        self.console.print(
            create_bar_chart(token_data, max_width=35, theme=self.theme)
        )
        self.console.print()

        # Cost metrics panel
        cost_data = [
            ("Total Cost", format_currency(self.get_metric("D094", 0)), None),
            ("Daily Cost", format_currency(self.get_metric("D095", 0)), None),
            ("Weekly Cost", format_currency(self.get_metric("D096", 0)), None),
            ("Cost/Session", format_currency(self.get_metric("D098", 0)), None),
            ("Cost/Message", format_currency(self.get_metric("D099", 0), precision=4), None),
            ("Cache Savings", format_currency(self.get_metric("D093", 0)), "estimated"),
        ]

        token_data = [
            ("Total Tokens", format_number(total_tokens), None),
            ("Tokens/Message", format_number(self.get_metric("D081", 0)), None),
            ("Tokens/Session", format_number(self.get_metric("D082", 0)), None),
            ("Input/Output Ratio", format_ratio(self.get_metric("D083", 0)), None),
            ("Cache Hit Ratio", format_percentage(self.get_metric("D089", 0)), None),
            ("Daily Token Rate", format_number(self.get_metric("D086", 0)), "tokens/day"),
        ]

        self.console.print(
            Columns(
                [
                    create_metric_panel("Cost Summary", cost_data, self.theme),
                    create_metric_panel("Token Summary", token_data, self.theme),
                ],
                equal=True,
            )
        )

    def print_footer(self) -> None:
        """Print report footer."""
        self.console.print()
        self.console.print(
            Panel(
                Text.from_markup(
                    f"[dim]Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"{len(self.metrics)} metrics calculated[/dim]"
                ),
                box=box.MINIMAL,
                border_style=self.theme.muted,
            )
        )

    def print_category_detail(self, category: str) -> None:
        """Print detailed metrics for a specific category.

        Args:
            category: Category letter (A, B, C, D)
        """
        category_names = {
            "A": "Time & Activity",
            "B": "Tool Usage",
            "C": "File Operations",
            "D": "Model & Token",
        }

        name = category_names.get(category, f"Category {category}")
        self.console.print(
            Rule(f"[bold]{name} Metrics[/bold]", style=self.theme.primary)
        )
        self.console.print()

        # Get all metrics for this category
        category_metrics = [
            (mid, mv)
            for mid, mv in sorted(self.metrics.items())
            if mid.startswith(f"D") and mid in METRIC_DEFINITIONS
            and METRIC_DEFINITIONS[mid].category == category
        ]

        if not category_metrics:
            self.console.print(f"  [dim]No metrics calculated for category {category}[/dim]")
            return

        # Create table
        table = Table(show_header=True, header_style=self.theme.heading)
        table.add_column("ID", style=self.theme.primary, width=6)
        table.add_column("Name", style=self.theme.label)
        table.add_column("Value", style=self.theme.value, justify="right")
        table.add_column("Unit", style=self.theme.muted)

        for metric_id, metric_value in category_metrics:
            definition = METRIC_DEFINITIONS[metric_id]
            value = metric_value.value

            # Format value based on type
            if isinstance(value, float):
                value_str = f"{value:.4f}"
            elif isinstance(value, dict):
                value_str = f"{{...}} ({len(value)} items)"
            else:
                value_str = str(value)

            table.add_row(
                metric_id,
                definition.name,
                value_str[:20],
                definition.unit or "-",
            )

        self.console.print(table)

    def print_all_metrics(self) -> None:
        """Print all calculated metrics."""
        self.print_header()
        self.console.print()

        for category in ["A", "B", "C", "D"]:
            self.print_category_detail(category)
            self.console.print()

        self.print_footer()

    def _truncate_path(self, path: str, max_len: int = 30) -> str:
        """Truncate a file path for display.

        Args:
            path: File path
            max_len: Maximum length

        Returns:
            Truncated path
        """
        if not path or path == "-":
            return "-"
        if len(path) <= max_len:
            return path
        return "..." + path[-(max_len - 3):]

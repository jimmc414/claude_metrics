"""Terminal visualization using Rich library."""

from .components import (
    create_sparkline,
    create_bar_chart,
    create_progress_bar,
    create_gauge,
    create_metric_panel,
    create_distribution_table,
    format_duration,
    format_hours,
    format_currency,
    format_number,
    format_percentage,
)
from .report import TerminalReport
from .themes import THEMES, get_theme

__all__ = [
    # Components
    "create_sparkline",
    "create_bar_chart",
    "create_progress_bar",
    "create_gauge",
    "create_metric_panel",
    "create_distribution_table",
    "format_duration",
    "format_hours",
    "format_currency",
    "format_number",
    "format_percentage",
    # Report
    "TerminalReport",
    # Themes
    "THEMES",
    "get_theme",
]

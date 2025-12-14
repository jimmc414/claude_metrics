"""Visualization system for Claude Metrics.

This package provides terminal and HTML visualization capabilities
for derived metrics.
"""

from .terminal import TerminalReport, create_sparkline, create_bar_chart
from .html import DashboardGenerator

__all__ = [
    "TerminalReport",
    "create_sparkline",
    "create_bar_chart",
    "DashboardGenerator",
]

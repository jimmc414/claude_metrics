"""Terminal visualization components using Rich library."""

from typing import Any, Dict, List, Optional, Tuple, Union
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Console, Group
from rich.columns import Columns

from .themes import Theme, get_theme


# Sparkline characters (8 levels)
SPARKLINE_CHARS = "▁▂▃▄▅▆▇█"


def create_sparkline(
    values: List[float],
    width: Optional[int] = None,
    theme: Optional[Theme] = None,
) -> str:
    """Create a sparkline from a list of values.

    Args:
        values: List of numeric values
        width: Optional fixed width (will sample values if needed)
        theme: Color theme

    Returns:
        Sparkline string
    """
    if not values:
        return ""

    theme = theme or get_theme()

    # Sample values if width is specified
    if width and len(values) > width:
        step = len(values) / width
        values = [values[int(i * step)] for i in range(width)]
    elif width and len(values) < width:
        # Pad with zeros at start
        values = [0] * (width - len(values)) + values

    min_val = min(values)
    max_val = max(values)
    range_val = max_val - min_val

    if range_val == 0:
        return SPARKLINE_CHARS[4] * len(values)

    sparkline = ""
    for v in values:
        # Normalize to 0-7 index
        idx = int((v - min_val) / range_val * 7)
        idx = max(0, min(7, idx))
        sparkline += SPARKLINE_CHARS[idx]

    return sparkline


def create_bar_chart(
    data: Dict[str, Union[int, float]],
    max_width: int = 40,
    show_values: bool = True,
    show_percentages: bool = True,
    theme: Optional[Theme] = None,
) -> Table:
    """Create a horizontal bar chart table.

    Args:
        data: Dictionary of label -> value
        max_width: Maximum bar width in characters
        show_values: Show raw values
        show_percentages: Show percentages
        theme: Color theme

    Returns:
        Rich Table object
    """
    theme = theme or get_theme()

    if not data:
        table = Table(show_header=False, box=None)
        table.add_row("No data")
        return table

    max_val = max(data.values()) if data.values() else 1
    total = sum(data.values())

    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column("Label", style=theme.label, no_wrap=True)
    table.add_column("Bar", no_wrap=True)
    if show_values:
        table.add_column("Value", style=theme.value, justify="right")
    if show_percentages:
        table.add_column("Pct", style=theme.muted, justify="right")

    for label, value in sorted(data.items(), key=lambda x: -x[1]):
        bar_width = int((value / max_val) * max_width) if max_val > 0 else 0
        bar = f"[{theme.bar_fill}]{'█' * bar_width}[/{theme.bar_fill}]"
        bar += f"[{theme.bar_empty}]{'░' * (max_width - bar_width)}[/{theme.bar_empty}]"

        row = [label, bar]
        if show_values:
            row.append(format_number(value))
        if show_percentages and total > 0:
            pct = (value / total) * 100
            row.append(f"{pct:.1f}%")
        elif show_percentages:
            row.append("-")

        table.add_row(*row)

    return table


def create_progress_bar(
    value: float,
    max_value: float = 1.0,
    width: int = 20,
    theme: Optional[Theme] = None,
) -> str:
    """Create a progress bar string.

    Args:
        value: Current value
        max_value: Maximum value (default 1.0 for ratios)
        width: Bar width in characters
        theme: Color theme

    Returns:
        Progress bar string with markup
    """
    theme = theme or get_theme()

    if max_value <= 0:
        pct = 0
    else:
        pct = min(1.0, max(0.0, value / max_value))

    filled = int(pct * width)
    empty = width - filled

    bar = f"[{theme.bar_fill}]{'█' * filled}[/{theme.bar_fill}]"
    bar += f"[{theme.bar_empty}]{'░' * empty}[/{theme.bar_empty}]"
    bar += f" [{theme.value}]{pct * 100:.1f}%[/{theme.value}]"

    return bar


def create_gauge(
    value: float,
    min_value: float = 0.0,
    max_value: float = 100.0,
    thresholds: Optional[Dict[str, float]] = None,
    width: int = 20,
    theme: Optional[Theme] = None,
) -> str:
    """Create a gauge visualization.

    Args:
        value: Current value
        min_value: Minimum value
        max_value: Maximum value
        thresholds: Dict with 'low', 'medium', 'high' thresholds for coloring
        width: Gauge width in characters
        theme: Color theme

    Returns:
        Gauge string with markup
    """
    theme = theme or get_theme()

    # Default thresholds
    if thresholds is None:
        thresholds = {"low": 0.33, "high": 0.67}

    # Normalize value to 0-1 range
    range_val = max_value - min_value
    if range_val <= 0:
        normalized = 0.5
    else:
        normalized = (value - min_value) / range_val
        normalized = max(0.0, min(1.0, normalized))

    # Determine color based on thresholds
    if normalized < thresholds.get("low", 0.33):
        color = theme.error
    elif normalized > thresholds.get("high", 0.67):
        color = theme.success
    else:
        color = theme.warning

    # Create gauge
    filled = int(normalized * width)
    empty = width - filled

    gauge = f"[{color}]{'▓' * filled}[/{color}]"
    gauge += f"[{theme.bar_empty}]{'░' * empty}[/{theme.bar_empty}]"
    gauge += f" [{theme.value}]{value:.1f}[/{theme.value}]"

    return gauge


def create_metric_panel(
    title: str,
    metrics: List[Tuple[str, Any, Optional[str]]],
    theme: Optional[Theme] = None,
) -> Panel:
    """Create a panel displaying multiple metrics.

    Args:
        title: Panel title
        metrics: List of (label, value, unit) tuples
        theme: Color theme

    Returns:
        Rich Panel object
    """
    theme = theme or get_theme()

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Label", style=theme.label)
    table.add_column("Value", style=theme.value, justify="right")
    table.add_column("Unit", style=theme.muted)

    for label, value, unit in metrics:
        if isinstance(value, float):
            value_str = f"{value:.2f}"
        else:
            value_str = str(value)
        table.add_row(label, value_str, unit or "")

    return Panel(
        table,
        title=f"[{theme.heading}]{title}[/{theme.heading}]",
        border_style=theme.primary,
    )


def create_distribution_table(
    data: Dict[str, Union[int, float]],
    title: str = "Distribution",
    sort_by_value: bool = True,
    limit: int = 10,
    theme: Optional[Theme] = None,
) -> Table:
    """Create a table showing distribution data.

    Args:
        data: Dictionary of category -> value
        title: Table title
        sort_by_value: Sort by value descending
        limit: Maximum rows to show
        theme: Color theme

    Returns:
        Rich Table object
    """
    theme = theme or get_theme()

    table = Table(title=title, show_header=True, header_style=theme.heading)
    table.add_column("Category", style=theme.label)
    table.add_column("Count", style=theme.value, justify="right")
    table.add_column("Percentage", style=theme.muted, justify="right")

    total = sum(data.values())
    items = list(data.items())

    if sort_by_value:
        items.sort(key=lambda x: -x[1])

    for i, (category, value) in enumerate(items):
        if i >= limit:
            remaining = len(items) - limit
            remaining_value = sum(v for _, v in items[limit:])
            pct = (remaining_value / total * 100) if total > 0 else 0
            table.add_row(
                f"... and {remaining} more",
                format_number(remaining_value),
                f"{pct:.1f}%",
            )
            break

        pct = (value / total * 100) if total > 0 else 0
        table.add_row(category, format_number(value), f"{pct:.1f}%")

    return table


def create_trend_indicator(
    current: float,
    previous: float,
    higher_is_better: bool = True,
    theme: Optional[Theme] = None,
) -> str:
    """Create a trend indicator showing change.

    Args:
        current: Current value
        previous: Previous value
        higher_is_better: Whether higher values are good
        theme: Color theme

    Returns:
        Trend indicator string with markup
    """
    theme = theme or get_theme()

    if previous == 0:
        if current > 0:
            return f"[{theme.positive}]+100%[/{theme.positive}]"
        return f"[{theme.neutral}]0%[/{theme.neutral}]"

    change = ((current - previous) / abs(previous)) * 100

    if change > 0:
        arrow = "↑"
        color = theme.positive if higher_is_better else theme.negative
    elif change < 0:
        arrow = "↓"
        color = theme.negative if higher_is_better else theme.positive
    else:
        return f"[{theme.neutral}]→ 0%[/{theme.neutral}]"

    return f"[{color}]{arrow} {abs(change):.1f}%[/{color}]"


def create_summary_row(
    items: List[Tuple[str, str, str]],
    theme: Optional[Theme] = None,
) -> Columns:
    """Create a row of summary items.

    Args:
        items: List of (label, value, trend) tuples
        theme: Color theme

    Returns:
        Rich Columns object
    """
    theme = theme or get_theme()

    panels = []
    for label, value, trend in items:
        content = Text()
        content.append(f"{label}\n", style=theme.muted)
        content.append(f"{value}", style=f"bold {theme.value}")
        if trend:
            content.append(f" {trend}")
        panels.append(Panel(content, expand=True, border_style=theme.primary))

    return Columns(panels, equal=True, expand=True)


# Formatting functions

def format_duration(seconds: float, precision: int = 2) -> str:
    """Format seconds as human-readable duration.

    Args:
        seconds: Duration in seconds
        precision: Decimal places for seconds

    Returns:
        Formatted duration string
    """
    if seconds < 0:
        return "-" + format_duration(-seconds, precision)

    if seconds < 60:
        return f"{seconds:.{precision}f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.0f}s"
    elif seconds < 86400:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}h {minutes}m"
    else:
        days = int(seconds // 86400)
        hours = int((seconds % 86400) // 3600)
        return f"{days}d {hours}h"


def format_duration_ms(milliseconds: float) -> str:
    """Format milliseconds as human-readable duration.

    Args:
        milliseconds: Duration in milliseconds

    Returns:
        Formatted duration string
    """
    return format_duration(milliseconds / 1000)


def format_hours(hours: float) -> str:
    """Format hours as human-readable duration.

    Args:
        hours: Duration in hours

    Returns:
        Formatted duration string
    """
    return format_duration(hours * 3600)


def format_currency(amount: float, symbol: str = "$", precision: int = 2) -> str:
    """Format amount as currency.

    Args:
        amount: Amount
        symbol: Currency symbol
        precision: Decimal places

    Returns:
        Formatted currency string
    """
    if amount < 0:
        return f"-{symbol}{abs(amount):,.{precision}f}"
    return f"{symbol}{amount:,.{precision}f}"


def format_number(value: Union[int, float], precision: int = 0) -> str:
    """Format number with thousands separator.

    Args:
        value: Number to format
        precision: Decimal places (0 for integers)

    Returns:
        Formatted number string
    """
    if isinstance(value, int) or precision == 0:
        return f"{int(value):,}"
    return f"{value:,.{precision}f}"


def format_percentage(value: float, precision: int = 1) -> str:
    """Format value as percentage.

    Args:
        value: Value (0-1 or 0-100)
        precision: Decimal places

    Returns:
        Formatted percentage string
    """
    # Assume values > 1 are already percentages
    if value > 1:
        return f"{value:.{precision}f}%"
    return f"{value * 100:.{precision}f}%"


def format_ratio(value: float, precision: int = 2) -> str:
    """Format a ratio value.

    Args:
        value: Ratio value
        precision: Decimal places

    Returns:
        Formatted ratio string
    """
    return f"{value:.{precision}f}"

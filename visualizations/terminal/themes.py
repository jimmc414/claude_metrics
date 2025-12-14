"""Color themes for terminal visualization."""

from dataclasses import dataclass
from typing import Dict


@dataclass
class Theme:
    """Color theme for terminal output."""

    # Primary colors
    primary: str
    secondary: str
    accent: str

    # Status colors
    success: str
    warning: str
    error: str
    info: str

    # Value colors
    positive: str
    negative: str
    neutral: str

    # Chart colors
    bar_fill: str
    bar_empty: str
    sparkline: str

    # Text colors
    heading: str
    label: str
    value: str
    muted: str


# Default theme
DEFAULT_THEME = Theme(
    primary="cyan",
    secondary="blue",
    accent="magenta",
    success="green",
    warning="yellow",
    error="red",
    info="blue",
    positive="green",
    negative="red",
    neutral="white",
    bar_fill="cyan",
    bar_empty="dim",
    sparkline="cyan",
    heading="bold white",
    label="white",
    value="cyan",
    muted="dim",
)

# Monochrome theme for cleaner output
MONO_THEME = Theme(
    primary="white",
    secondary="white",
    accent="white",
    success="white",
    warning="white",
    error="white",
    info="white",
    positive="white",
    negative="white",
    neutral="white",
    bar_fill="white",
    bar_empty="dim",
    sparkline="white",
    heading="bold",
    label="white",
    value="bold",
    muted="dim",
)

# Dark theme with vibrant colors
DARK_THEME = Theme(
    primary="bright_cyan",
    secondary="bright_blue",
    accent="bright_magenta",
    success="bright_green",
    warning="bright_yellow",
    error="bright_red",
    info="bright_blue",
    positive="bright_green",
    negative="bright_red",
    neutral="bright_white",
    bar_fill="bright_cyan",
    bar_empty="dim",
    sparkline="bright_cyan",
    heading="bold bright_white",
    label="bright_white",
    value="bright_cyan",
    muted="dim",
)

# Available themes
THEMES: Dict[str, Theme] = {
    "default": DEFAULT_THEME,
    "mono": MONO_THEME,
    "dark": DARK_THEME,
}


def get_theme(name: str = "default") -> Theme:
    """Get a theme by name.

    Args:
        name: Theme name (default, mono, dark)

    Returns:
        Theme instance
    """
    return THEMES.get(name, DEFAULT_THEME)

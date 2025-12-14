"""
Claude Metrics - Extract and analyze Claude Code usage data.

A Python library and CLI tool for extracting raw data from Claude Code's
local storage into clean JSON files and SQLite databases.
"""

__version__ = "0.1.0"
__author__ = "Claude Code Metrics"


def __getattr__(name):
    """Lazy import to avoid module name conflicts."""
    if name == "MetricsExtractor":
        from metrics_extractor import MetricsExtractor
        return MetricsExtractor
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = ["MetricsExtractor", "__version__"]

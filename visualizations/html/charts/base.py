"""Base chart class for Plotly charts."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union
import json


@dataclass
class ChartConfig:
    """Configuration for a chart."""

    title: str = ""
    width: Optional[int] = None
    height: int = 400
    show_legend: bool = True
    margin: Dict[str, int] = field(
        default_factory=lambda: {"l": 50, "r": 50, "t": 50, "b": 50}
    )
    colors: List[str] = field(
        default_factory=lambda: [
            "#2563eb",  # Blue
            "#16a34a",  # Green
            "#dc2626",  # Red
            "#ca8a04",  # Yellow
            "#9333ea",  # Purple
            "#0891b2",  # Cyan
            "#ea580c",  # Orange
            "#4f46e5",  # Indigo
        ]
    )
    font_family: str = "Inter, system-ui, sans-serif"
    font_size: int = 12
    paper_bgcolor: str = "rgba(0,0,0,0)"
    plot_bgcolor: str = "rgba(0,0,0,0)"
    animation: bool = False


class BaseChart(ABC):
    """Abstract base class for all chart types."""

    def __init__(self, config: Optional[ChartConfig] = None):
        """Initialize the chart with optional configuration.

        Args:
            config: Chart configuration options
        """
        self.config = config or ChartConfig()

    @abstractmethod
    def create(self, data: Any, **kwargs) -> Dict[str, Any]:
        """Create the chart data structure.

        Args:
            data: Chart-specific data
            **kwargs: Additional chart options

        Returns:
            Dictionary with 'data' and 'layout' keys for Plotly
        """
        pass

    def to_json(self, data: Any, **kwargs) -> str:
        """Convert chart to JSON string for embedding.

        Args:
            data: Chart-specific data
            **kwargs: Additional chart options

        Returns:
            JSON string representation of the chart
        """
        chart_data = self.create(data, **kwargs)
        return json.dumps(chart_data)

    def to_html_div(
        self, data: Any, div_id: str = "chart", **kwargs
    ) -> str:
        """Generate HTML div with embedded chart.

        Args:
            data: Chart-specific data
            div_id: ID for the chart container div
            **kwargs: Additional chart options

        Returns:
            HTML string with chart div and script
        """
        chart_json = self.to_json(data, **kwargs)
        return f"""
<div id="{div_id}" class="chart-container"></div>
<script>
    Plotly.newPlot('{div_id}', {chart_json}.data, {chart_json}.layout, {{responsive: true}});
</script>
"""

    def _get_base_layout(self, **overrides) -> Dict[str, Any]:
        """Get base layout configuration.

        Args:
            **overrides: Layout properties to override

        Returns:
            Layout dictionary for Plotly
        """
        layout = {
            "title": {
                "text": self.config.title,
                "font": {
                    "family": self.config.font_family,
                    "size": self.config.font_size + 4,
                },
            },
            "font": {
                "family": self.config.font_family,
                "size": self.config.font_size,
            },
            "showlegend": self.config.show_legend,
            "margin": self.config.margin,
            "paper_bgcolor": self.config.paper_bgcolor,
            "plot_bgcolor": self.config.plot_bgcolor,
            "height": self.config.height,
        }

        if self.config.width:
            layout["width"] = self.config.width

        # Apply overrides
        for key, value in overrides.items():
            if isinstance(value, dict) and key in layout and isinstance(layout[key], dict):
                layout[key].update(value)
            else:
                layout[key] = value

        return layout

    def _get_color(self, index: int) -> str:
        """Get color from palette by index.

        Args:
            index: Color index

        Returns:
            Hex color string
        """
        return self.config.colors[index % len(self.config.colors)]

"""Scatter chart component."""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass

from .base import BaseChart, ChartConfig


@dataclass
class ScatterSeries:
    """Data for a scatter series."""

    x: List[float]
    y: List[float]
    name: str = ""
    text: Optional[List[str]] = None
    size: Optional[List[float]] = None  # For bubble charts
    color: Optional[List[float]] = None  # For color-coded points


class ScatterChart(BaseChart):
    """Scatter chart for correlations and relationships."""

    def create(
        self,
        data: ScatterSeries | List[ScatterSeries],
        x_title: str = "",
        y_title: str = "",
        show_grid: bool = True,
        show_trendline: bool = False,
        marker_size: int = 8,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a scatter chart.

        Args:
            data: ScatterSeries or list of ScatterSeries
            x_title: X-axis title
            y_title: Y-axis title
            show_grid: Whether to show grid lines
            show_trendline: Whether to show regression line
            marker_size: Default marker size

        Returns:
            Plotly figure dictionary
        """
        if isinstance(data, ScatterSeries):
            series_list = [data]
        else:
            series_list = data

        traces = []
        for i, series in enumerate(series_list):
            trace = {
                "type": "scatter",
                "mode": "markers",
                "x": series.x,
                "y": series.y,
                "name": series.name,
                "marker": {
                    "color": self._get_color(i),
                    "size": series.size if series.size else marker_size,
                },
            }

            if series.text:
                trace["text"] = series.text
                trace["hoverinfo"] = "text+x+y"

            if series.color:
                trace["marker"]["color"] = series.color
                trace["marker"]["colorscale"] = "Viridis"
                trace["marker"]["showscale"] = True

            traces.append(trace)

            # Add trendline if requested
            if show_trendline and len(series.x) > 1:
                trendline = self._calculate_trendline(series.x, series.y)
                traces.append({
                    "type": "scatter",
                    "mode": "lines",
                    "x": trendline["x"],
                    "y": trendline["y"],
                    "name": f"{series.name} trend" if series.name else "Trend",
                    "line": {
                        "color": self._get_color(i),
                        "dash": "dash",
                        "width": 2,
                    },
                    "showlegend": False,
                })

        layout = self._get_base_layout(
            xaxis={
                "title": x_title,
                "showgrid": show_grid,
                "gridcolor": "rgba(128,128,128,0.2)",
            },
            yaxis={
                "title": y_title,
                "showgrid": show_grid,
                "gridcolor": "rgba(128,128,128,0.2)",
            },
        )

        return {"data": traces, "layout": layout}

    def _calculate_trendline(
        self, x: List[float], y: List[float]
    ) -> Dict[str, List[float]]:
        """Calculate linear regression trendline.

        Args:
            x: X values
            y: Y values

        Returns:
            Dict with x and y values for the trendline
        """
        n = len(x)
        if n < 2:
            return {"x": [], "y": []}

        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))
        sum_x2 = sum(xi * xi for xi in x)

        denominator = n * sum_x2 - sum_x ** 2
        if denominator == 0:
            return {"x": [], "y": []}

        slope = (n * sum_xy - sum_x * sum_y) / denominator
        intercept = (sum_y - slope * sum_x) / n

        min_x, max_x = min(x), max(x)
        return {
            "x": [min_x, max_x],
            "y": [slope * min_x + intercept, slope * max_x + intercept],
        }


class BubbleChart(ScatterChart):
    """Bubble chart (scatter with size dimension)."""

    def create(
        self,
        data: ScatterSeries | List[ScatterSeries],
        size_scale: float = 1.0,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a bubble chart.

        Args:
            data: ScatterSeries with size values
            size_scale: Scale factor for bubble sizes

        Returns:
            Plotly figure dictionary
        """
        if isinstance(data, ScatterSeries):
            series_list = [data]
        else:
            series_list = data

        # Scale sizes
        for series in series_list:
            if series.size:
                max_size = max(series.size)
                if max_size > 0:
                    series.size = [s / max_size * 50 * size_scale for s in series.size]

        return super().create(data, **kwargs)

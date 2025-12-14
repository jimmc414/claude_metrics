"""Heatmap chart component."""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass

from .base import BaseChart, ChartConfig


@dataclass
class HeatmapData:
    """Data for a heatmap chart."""

    z: List[List[float]]  # 2D array of values
    x: Optional[List[Any]] = None  # X-axis labels
    y: Optional[List[Any]] = None  # Y-axis labels
    text: Optional[List[List[str]]] = None  # Text to show on hover


class HeatmapChart(BaseChart):
    """Heatmap chart for 2D distributions."""

    def create(
        self,
        data: HeatmapData | List[List[float]],
        x_labels: Optional[List[Any]] = None,
        y_labels: Optional[List[Any]] = None,
        colorscale: str = "Blues",
        show_scale: bool = True,
        show_values: bool = False,
        x_title: str = "",
        y_title: str = "",
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a heatmap chart.

        Args:
            data: HeatmapData or 2D list of values
            x_labels: Labels for x-axis
            y_labels: Labels for y-axis
            colorscale: Plotly colorscale name
            show_scale: Whether to show the color scale
            show_values: Whether to show values on cells
            x_title: X-axis title
            y_title: Y-axis title

        Returns:
            Plotly figure dictionary
        """
        # Handle list input
        if isinstance(data, list):
            heatmap_data = HeatmapData(z=data, x=x_labels, y=y_labels)
        else:
            heatmap_data = data

        trace = {
            "type": "heatmap",
            "z": heatmap_data.z,
            "colorscale": colorscale,
            "showscale": show_scale,
            "hoverongaps": False,
        }

        if heatmap_data.x:
            trace["x"] = heatmap_data.x
        if heatmap_data.y:
            trace["y"] = heatmap_data.y

        if show_values:
            trace["text"] = heatmap_data.text or [
                [f"{val:.1f}" for val in row] for row in heatmap_data.z
            ]
            trace["texttemplate"] = "%{text}"
            trace["textfont"] = {"size": 10}

        layout = self._get_base_layout(
            xaxis={
                "title": x_title,
                "side": "bottom",
            },
            yaxis={
                "title": y_title,
                "autorange": "reversed",  # Top to bottom
            },
        )

        return {"data": [trace], "layout": layout}


class CalendarHeatmap(BaseChart):
    """Calendar heatmap for daily activity."""

    def create(
        self,
        data: Dict[str, float],
        colorscale: str = "Greens",
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a calendar heatmap.

        Args:
            data: Dict mapping date strings (YYYY-MM-DD) to values
            colorscale: Plotly colorscale name

        Returns:
            Plotly figure dictionary
        """
        if not data:
            return {"data": [], "layout": self._get_base_layout()}

        # Convert dates to week/day structure
        from datetime import datetime

        dates = sorted(data.keys())
        start_date = datetime.strptime(dates[0], "%Y-%m-%d")
        end_date = datetime.strptime(dates[-1], "%Y-%m-%d")

        # Build week/day grid
        weeks = []
        days = []
        values = []
        texts = []

        current = start_date
        while current <= end_date:
            date_str = current.strftime("%Y-%m-%d")
            week_num = (current - start_date).days // 7
            day_of_week = current.weekday()

            weeks.append(week_num)
            days.append(day_of_week)
            values.append(data.get(date_str, 0))
            texts.append(f"{date_str}: {data.get(date_str, 0):.0f}")

            current = current.replace(day=current.day + 1) if current.day < 28 else current

        trace = {
            "type": "heatmap",
            "x": weeks,
            "y": days,
            "z": values,
            "text": texts,
            "hoverinfo": "text",
            "colorscale": colorscale,
            "showscale": True,
        }

        layout = self._get_base_layout(
            yaxis={
                "tickmode": "array",
                "tickvals": list(range(7)),
                "ticktext": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            },
            xaxis={
                "showticklabels": False,
            },
        )

        return {"data": [trace], "layout": layout}

"""Bar chart component."""

from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass

from .base import BaseChart, ChartConfig


@dataclass
class BarSeries:
    """Data for a single bar series."""

    x: List[Any]
    y: List[float]
    name: str = ""
    orientation: str = "v"  # v for vertical, h for horizontal
    text: Optional[List[str]] = None
    text_position: str = "auto"  # inside, outside, auto, none


class BarChart(BaseChart):
    """Bar chart for distributions and comparisons."""

    def create(
        self,
        data: Union[BarSeries, List[BarSeries], Dict[str, float]],
        x_title: str = "",
        y_title: str = "",
        show_grid: bool = True,
        stacked: bool = False,
        horizontal: bool = False,
        show_values: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a bar chart.

        Args:
            data: BarSeries, list of BarSeries, or dict of label->value
            x_title: X-axis title
            y_title: Y-axis title
            show_grid: Whether to show grid lines
            stacked: Whether to stack bars
            horizontal: Whether to use horizontal orientation
            show_values: Whether to show values on bars

        Returns:
            Plotly figure dictionary
        """
        # Handle dict input
        if isinstance(data, dict):
            series_list = [
                BarSeries(
                    x=list(data.keys()),
                    y=list(data.values()),
                    orientation="h" if horizontal else "v",
                )
            ]
        elif isinstance(data, BarSeries):
            series_list = [data]
        else:
            series_list = data

        traces = []
        for i, series in enumerate(series_list):
            orientation = "h" if horizontal else series.orientation

            if horizontal:
                x_vals, y_vals = series.y, series.x
            else:
                x_vals, y_vals = series.x, series.y

            trace = {
                "type": "bar",
                "x": x_vals,
                "y": y_vals,
                "name": series.name,
                "orientation": orientation,
                "marker": {"color": self._get_color(i)},
            }

            if show_values or series.text:
                trace["text"] = series.text or [f"{v:,.0f}" for v in series.y]
                trace["textposition"] = series.text_position

            traces.append(trace)

        barmode = "stack" if stacked else "group"

        layout = self._get_base_layout(
            barmode=barmode,
            xaxis={
                "title": y_title if horizontal else x_title,
                "showgrid": show_grid and horizontal,
                "gridcolor": "rgba(128,128,128,0.2)",
            },
            yaxis={
                "title": x_title if horizontal else y_title,
                "showgrid": show_grid and not horizontal,
                "gridcolor": "rgba(128,128,128,0.2)",
            },
        )

        return {"data": traces, "layout": layout}


class StackedBarChart(BarChart):
    """Stacked bar chart."""

    def create(self, data: Union[BarSeries, List[BarSeries]], **kwargs) -> Dict[str, Any]:
        """Create a stacked bar chart."""
        return super().create(data, stacked=True, **kwargs)

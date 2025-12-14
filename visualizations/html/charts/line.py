"""Line chart component."""

from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass

from .base import BaseChart, ChartConfig


@dataclass
class LineSeries:
    """Data for a single line series."""

    x: List[Any]
    y: List[float]
    name: str = ""
    mode: str = "lines"  # lines, markers, lines+markers
    fill: Optional[str] = None  # none, tozeroy, tonexty
    line_width: int = 2
    line_dash: Optional[str] = None  # solid, dot, dash, dashdot


class LineChart(BaseChart):
    """Line chart for time series and trends."""

    def create(
        self,
        data: Union[LineSeries, List[LineSeries]],
        x_title: str = "",
        y_title: str = "",
        show_grid: bool = True,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a line chart.

        Args:
            data: Single LineSeries or list of LineSeries
            x_title: X-axis title
            y_title: Y-axis title
            show_grid: Whether to show grid lines

        Returns:
            Plotly figure dictionary
        """
        if isinstance(data, LineSeries):
            series_list = [data]
        else:
            series_list = data

        traces = []
        for i, series in enumerate(series_list):
            trace = {
                "type": "scatter",
                "x": series.x,
                "y": series.y,
                "mode": series.mode,
                "name": series.name,
                "line": {
                    "color": self._get_color(i),
                    "width": series.line_width,
                },
            }

            if series.line_dash:
                trace["line"]["dash"] = series.line_dash

            if series.fill:
                trace["fill"] = series.fill
                trace["fillcolor"] = self._get_color(i).replace(")", ", 0.2)")

            traces.append(trace)

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


class AreaChart(LineChart):
    """Area chart (line chart with fill)."""

    def create(
        self,
        data: Union[LineSeries, List[LineSeries]],
        stacked: bool = False,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create an area chart.

        Args:
            data: Single LineSeries or list of LineSeries
            stacked: Whether to stack areas

        Returns:
            Plotly figure dictionary
        """
        if isinstance(data, LineSeries):
            series_list = [data]
        else:
            series_list = data

        # Set fill mode for area charts
        for i, series in enumerate(series_list):
            if stacked and i > 0:
                series.fill = "tonexty"
            else:
                series.fill = "tozeroy"

        return super().create(data, **kwargs)

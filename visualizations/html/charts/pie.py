"""Pie and donut chart components."""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass

from .base import BaseChart, ChartConfig


@dataclass
class PieData:
    """Data for a pie/donut chart."""

    labels: List[str]
    values: List[float]
    text: Optional[List[str]] = None


class PieChart(BaseChart):
    """Pie chart for proportions."""

    def create(
        self,
        data: PieData | Dict[str, float],
        hole: float = 0,
        text_info: str = "percent+label",
        pull: Optional[List[float]] = None,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a pie chart.

        Args:
            data: PieData or dict of label->value
            hole: Size of center hole (0 for pie, 0.3-0.6 for donut)
            text_info: What text to show (label, percent, value, etc.)
            pull: List of pull amounts for each slice

        Returns:
            Plotly figure dictionary
        """
        # Handle dict input
        if isinstance(data, dict):
            pie_data = PieData(
                labels=list(data.keys()),
                values=list(data.values()),
            )
        else:
            pie_data = data

        trace = {
            "type": "pie",
            "labels": pie_data.labels,
            "values": pie_data.values,
            "hole": hole,
            "textinfo": text_info,
            "marker": {"colors": self.config.colors[: len(pie_data.labels)]},
            "hovertemplate": "%{label}: %{value:,.0f} (%{percent})<extra></extra>",
        }

        if pull:
            trace["pull"] = pull

        if pie_data.text:
            trace["text"] = pie_data.text

        layout = self._get_base_layout()

        return {"data": [trace], "layout": layout}


class DonutChart(PieChart):
    """Donut chart (pie with hole)."""

    def create(self, data: PieData | Dict[str, float], **kwargs) -> Dict[str, Any]:
        """Create a donut chart with default hole size."""
        return super().create(data, hole=0.4, **kwargs)

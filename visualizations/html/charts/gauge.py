"""Gauge chart component for KPIs."""

from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field

from .base import BaseChart, ChartConfig


@dataclass
class GaugeThreshold:
    """Threshold configuration for gauge coloring."""

    value: float
    color: str


@dataclass
class GaugeData:
    """Data for a gauge chart."""

    value: float
    min_value: float = 0
    max_value: float = 100
    title: str = ""
    suffix: str = ""
    thresholds: List[GaugeThreshold] = field(default_factory=list)


class GaugeChart(BaseChart):
    """Gauge chart for KPIs and ratios."""

    def create(
        self,
        data: GaugeData | float,
        min_value: float = 0,
        max_value: float = 100,
        suffix: str = "",
        gauge_color: str = "#2563eb",
        show_threshold_colors: bool = True,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a gauge chart.

        Args:
            data: GaugeData or float value
            min_value: Minimum gauge value
            max_value: Maximum gauge value
            suffix: Suffix for the displayed value
            gauge_color: Primary gauge color
            show_threshold_colors: Whether to show colored regions

        Returns:
            Plotly figure dictionary
        """
        # Handle float input
        if isinstance(data, (int, float)):
            gauge_data = GaugeData(
                value=float(data),
                min_value=min_value,
                max_value=max_value,
                suffix=suffix,
            )
        else:
            gauge_data = data

        # Build steps for threshold colors
        steps = []
        if gauge_data.thresholds and show_threshold_colors:
            sorted_thresholds = sorted(gauge_data.thresholds, key=lambda t: t.value)
            prev_value = gauge_data.min_value
            for threshold in sorted_thresholds:
                steps.append({
                    "range": [prev_value, threshold.value],
                    "color": threshold.color,
                })
                prev_value = threshold.value
            # Add final segment to max
            if prev_value < gauge_data.max_value:
                steps.append({
                    "range": [prev_value, gauge_data.max_value],
                    "color": sorted_thresholds[-1].color if sorted_thresholds else gauge_color,
                })
        else:
            # Default gradient
            steps = [
                {"range": [gauge_data.min_value, gauge_data.max_value], "color": "rgba(37, 99, 235, 0.1)"}
            ]

        trace = {
            "type": "indicator",
            "mode": "gauge+number",
            "value": gauge_data.value,
            "title": {"text": gauge_data.title or self.config.title},
            "number": {
                "suffix": gauge_data.suffix or suffix,
                "font": {"size": 40},
            },
            "gauge": {
                "axis": {
                    "range": [gauge_data.min_value, gauge_data.max_value],
                    "tickwidth": 1,
                },
                "bar": {"color": gauge_color},
                "bgcolor": "rgba(0,0,0,0)",
                "borderwidth": 0,
                "steps": steps,
            },
        }

        layout = self._get_base_layout(
            margin={"l": 30, "r": 30, "t": 50, "b": 30},
        )

        return {"data": [trace], "layout": layout}


class NumberIndicator(BaseChart):
    """Simple number indicator with optional delta."""

    def create(
        self,
        value: float,
        delta: Optional[float] = None,
        title: str = "",
        suffix: str = "",
        prefix: str = "",
        delta_relative: bool = True,
        **kwargs,
    ) -> Dict[str, Any]:
        """Create a number indicator.

        Args:
            value: The main value to display
            delta: Optional delta/change value
            title: Indicator title
            suffix: Suffix for the value
            prefix: Prefix for the value
            delta_relative: Whether delta is relative (percentage)

        Returns:
            Plotly figure dictionary
        """
        mode = "number"
        if delta is not None:
            mode = "number+delta"

        trace = {
            "type": "indicator",
            "mode": mode,
            "value": value,
            "title": {"text": title or self.config.title},
            "number": {
                "prefix": prefix,
                "suffix": suffix,
                "font": {"size": 48},
            },
        }

        if delta is not None:
            trace["delta"] = {
                "reference": value - delta if not delta_relative else value / (1 + delta),
                "relative": delta_relative,
                "valueformat": ".1%" if delta_relative else ".1f",
            }

        layout = self._get_base_layout(
            height=200,
            margin={"l": 20, "r": 20, "t": 50, "b": 20},
        )

        return {"data": [trace], "layout": layout}

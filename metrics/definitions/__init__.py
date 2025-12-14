"""Metric definitions for derived metrics."""

from .base import (
    MetricType,
    MetricDefinition,
    MetricValue,
    METRIC_DEFINITIONS,
    register_metric,
    get_metric,
    get_metrics_by_category,
)

# Import category modules to register their metrics
from . import category_a
from . import category_b
from . import category_c
from . import category_d

__all__ = [
    "MetricType",
    "MetricDefinition",
    "MetricValue",
    "METRIC_DEFINITIONS",
    "register_metric",
    "get_metric",
    "get_metrics_by_category",
]

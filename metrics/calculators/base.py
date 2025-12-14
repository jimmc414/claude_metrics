"""Base calculator class for metric calculations."""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, List, Optional

from extraction.data_classes import ExtractedData30Day
from metrics.definitions.base import MetricDefinition, MetricValue


class BaseCalculator(ABC):
    """Base class for metric calculators.

    Each calculator handles metrics for a specific category and
    has access to the extracted data and previously calculated metrics.
    """

    # Category this calculator handles (e.g., "A", "B", "C", "D")
    category: str = ""

    def __init__(
        self, data: ExtractedData30Day, cache: Dict[str, MetricValue]
    ):
        """Initialize the calculator.

        Args:
            data: Extracted data for the time window
            cache: Dictionary of previously calculated metrics
        """
        self.data = data
        self.cache = cache
        self._now = datetime.now()

    @abstractmethod
    def calculate(self, definition: MetricDefinition) -> MetricValue:
        """Calculate a single metric.

        Args:
            definition: The metric definition to calculate

        Returns:
            MetricValue with the calculated result
        """
        pass

    def get_dependency(self, metric_id: str) -> Any:
        """Get a previously calculated metric value.

        Args:
            metric_id: The metric ID (e.g., "D001")

        Returns:
            The metric value

        Raises:
            ValueError: If the dependency hasn't been calculated yet
        """
        if metric_id in self.cache:
            return self.cache[metric_id].value
        raise ValueError(f"Dependency {metric_id} not calculated yet")

    def get_dependency_safe(self, metric_id: str, default: Any = None) -> Any:
        """Get a previously calculated metric value, with default.

        Args:
            metric_id: The metric ID (e.g., "D001")
            default: Default value if not found

        Returns:
            The metric value or default
        """
        if metric_id in self.cache:
            return self.cache[metric_id].value
        return default

    def create_value(
        self,
        metric_id: str,
        value: Any,
        window_days: Optional[int] = None,
        breakdown: Optional[Dict[str, Any]] = None,
        trend: Optional[float] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> MetricValue:
        """Create a MetricValue with common fields.

        Args:
            metric_id: The metric ID
            value: The calculated value
            window_days: Override for window days (default: data.window_days)
            breakdown: Optional breakdown dictionary
            trend: Optional trend value
            metadata: Optional metadata dictionary

        Returns:
            MetricValue instance
        """
        return MetricValue(
            metric_id=metric_id,
            value=value,
            timestamp=self._now,
            window_days=window_days or self.data.window_days,
            breakdown=breakdown,
            trend=trend,
            metadata=metadata,
        )

    def _route_to_method(self, definition: MetricDefinition) -> MetricValue:
        """Route calculation to specific method based on metric ID.

        Looks for a method named _calc_{metric_id.lower()} (e.g., _calc_d001).

        Args:
            definition: The metric definition

        Returns:
            MetricValue from the specific calculator method

        Raises:
            NotImplementedError: If no method exists for the metric
        """
        method_name = f"_calc_{definition.id.lower()}"
        method = getattr(self, method_name, None)
        if method is None:
            raise NotImplementedError(
                f"No calculator method for {definition.id} "
                f"(expected {method_name})"
            )
        return method(definition)

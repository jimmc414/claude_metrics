"""Base metric definition and value classes."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


class MetricType(str, Enum):
    """Types of derived metrics."""

    DURATION = "duration"  # Time measurements (hours, minutes, ms)
    RATIO = "ratio"  # Proportional values (0-1)
    INT = "int"  # Integer counts
    FLOAT = "float"  # Decimal values
    DISTRIBUTION = "distribution"  # Breakdown by category
    RATE = "rate"  # Value per unit time
    TREND = "trend"  # Slope/direction indicator
    CATEGORY = "category"  # Categorical label
    COMPOUND = "compound"  # Multi-dimensional metric
    SEQUENCE = "sequence"  # Ordered pattern
    INVERSE = "inverse"  # Inverted metric (lower is better)
    PERCENTAGE = "percentage"  # 0-100% value
    BINARY = "binary"  # True/False indicator


@dataclass
class MetricDefinition:
    """Definition of a single derived metric."""

    id: str  # e.g., "D001"
    name: str  # e.g., "daily_active_hours"
    category: str  # e.g., "A"
    metric_type: MetricType
    description: str  # Human-readable description
    calculation: str  # How to calculate
    sources: List[str]  # Required data sources
    dependencies: List[str] = field(default_factory=list)  # Other metric IDs
    unit: Optional[str] = None  # e.g., "hours", "USD", "%"
    visualization: Optional[str] = None  # Recommended viz type

    def __post_init__(self):
        """Validate and normalize the definition."""
        # Ensure metric_type is a MetricType enum
        if isinstance(self.metric_type, str):
            self.metric_type = MetricType(self.metric_type)


@dataclass
class MetricValue:
    """Calculated value for a metric."""

    metric_id: str
    value: Any
    timestamp: datetime
    window_days: int
    breakdown: Optional[Dict[str, Any]] = None  # For distributions
    trend: Optional[float] = None  # Slope if applicable
    metadata: Optional[Dict[str, Any]] = None  # Additional context

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        result = {
            "metric_id": self.metric_id,
            "value": self.value,
            "timestamp": self.timestamp.isoformat(),
            "window_days": self.window_days,
        }
        if self.breakdown:
            result["breakdown"] = self.breakdown
        if self.trend is not None:
            result["trend"] = self.trend
        if self.metadata:
            result["metadata"] = self.metadata
        return result


# Registry of all metric definitions
METRIC_DEFINITIONS: Dict[str, MetricDefinition] = {}


def register_metric(definition: MetricDefinition) -> MetricDefinition:
    """Register a metric definition in the global registry.

    Args:
        definition: The MetricDefinition to register

    Returns:
        The registered definition
    """
    METRIC_DEFINITIONS[definition.id] = definition
    return definition


def get_metric(metric_id: str) -> Optional[MetricDefinition]:
    """Get a metric definition by ID.

    Args:
        metric_id: The metric ID (e.g., "D001")

    Returns:
        The MetricDefinition or None if not found
    """
    return METRIC_DEFINITIONS.get(metric_id)


def get_metrics_by_category(category: str) -> List[MetricDefinition]:
    """Get all metric definitions for a category.

    Args:
        category: The category letter (e.g., "A")

    Returns:
        List of MetricDefinitions in that category
    """
    return [d for d in METRIC_DEFINITIONS.values() if d.category == category]

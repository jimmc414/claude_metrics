"""Derived metrics calculation engine."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Type

from extraction.data_classes import ExtractedData30Day
from .definitions.base import (
    MetricDefinition,
    MetricValue,
    METRIC_DEFINITIONS,
    get_metrics_by_category,
)
from .calculators.base import BaseCalculator
from .calculators.category_a import CategoryACalculator
from .calculators.category_b import CategoryBCalculator
from .calculators.category_c import CategoryCCalculator
from .calculators.category_d import CategoryDCalculator
from .calculators.category_e import CategoryECalculator
from .calculators.category_f import CategoryFCalculator
from .calculators.category_g import CategoryGCalculator
from .calculators.category_h import CategoryHCalculator
from .calculators.category_i import CategoryICalculator
from .calculators.category_j import CategoryJCalculator


class DerivedMetricsEngine:
    """Engine for calculating all derived metrics.

    This engine orchestrates the calculation of metrics across all categories,
    handling dependencies and caching results.
    """

    # Map of category -> calculator class
    CALCULATORS: Dict[str, Type[BaseCalculator]] = {
        "A": CategoryACalculator,
        "B": CategoryBCalculator,
        "C": CategoryCCalculator,
        "D": CategoryDCalculator,
        "E": CategoryECalculator,
        "F": CategoryFCalculator,
        "G": CategoryGCalculator,
        "H": CategoryHCalculator,
        "I": CategoryICalculator,
        "J": CategoryJCalculator,
    }

    # Order in which categories should be calculated (for dependencies)
    CATEGORY_ORDER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    def __init__(self, data: ExtractedData30Day):
        """Initialize the engine.

        Args:
            data: Extracted data for the time window
        """
        self.data = data
        self.cache: Dict[str, MetricValue] = {}
        self._errors: List[Dict[str, Any]] = []

    def calculate_all(
        self,
        categories: Optional[List[str]] = None,
        progress_callback: Optional[Callable[[str, str], None]] = None,
    ) -> Dict[str, MetricValue]:
        """Calculate all metrics (or filtered by category).

        Args:
            categories: List of category letters to calculate (default: all)
            progress_callback: Optional callback(metric_id, status) for progress

        Returns:
            Dictionary of metric_id -> MetricValue
        """
        if categories is None:
            categories = self.CATEGORY_ORDER

        # Ensure categories are in dependency order
        ordered_categories = [c for c in self.CATEGORY_ORDER if c in categories]

        for category in ordered_categories:
            self._calculate_category(category, progress_callback)

        return self.cache

    def calculate_metric(self, metric_id: str) -> Optional[MetricValue]:
        """Calculate a single metric by ID.

        Args:
            metric_id: The metric ID (e.g., "D001")

        Returns:
            MetricValue or None if not found/error
        """
        # Check cache first
        if metric_id in self.cache:
            return self.cache[metric_id]

        # Get definition
        definition = METRIC_DEFINITIONS.get(metric_id)
        if not definition:
            return None

        # Calculate dependencies first
        for dep_id in definition.dependencies:
            if dep_id not in self.cache:
                self.calculate_metric(dep_id)

        # Get calculator and calculate
        calculator_class = self.CALCULATORS.get(definition.category)
        if not calculator_class:
            return None

        calculator = calculator_class(self.data, self.cache)
        try:
            value = calculator.calculate(definition)
            self.cache[metric_id] = value
            return value
        except Exception as e:
            self._errors.append({
                "metric_id": metric_id,
                "error": str(e),
            })
            return None

    def _calculate_category(
        self,
        category: str,
        progress_callback: Optional[Callable[[str, str], None]] = None,
    ) -> None:
        """Calculate all metrics in a category.

        Args:
            category: Category letter (e.g., "A")
            progress_callback: Optional progress callback
        """
        calculator_class = self.CALCULATORS.get(category)
        if not calculator_class:
            return

        calculator = calculator_class(self.data, self.cache)

        # Get all definitions for this category
        definitions = get_metrics_by_category(category)

        # Sort by dependencies (topological sort)
        sorted_defs = self._topological_sort(definitions)

        for definition in sorted_defs:
            if progress_callback:
                progress_callback(definition.id, "calculating")

            try:
                value = calculator.calculate(definition)
                self.cache[definition.id] = value
                if progress_callback:
                    progress_callback(definition.id, "done")
            except Exception as e:
                self._errors.append({
                    "metric_id": definition.id,
                    "error": str(e),
                })
                if progress_callback:
                    progress_callback(definition.id, "error")

    def _topological_sort(
        self, definitions: List[MetricDefinition]
    ) -> List[MetricDefinition]:
        """Sort definitions by dependencies.

        Args:
            definitions: List of metric definitions

        Returns:
            Sorted list with dependencies first
        """
        sorted_list = []
        remaining = list(definitions)
        definition_ids = {d.id for d in definitions}

        # Iterate until all are sorted
        max_iterations = len(remaining) * 2  # Safety limit
        iterations = 0

        while remaining and iterations < max_iterations:
            iterations += 1
            for d in remaining[:]:
                # Check if all dependencies are satisfied
                deps_satisfied = all(
                    dep in self.cache or dep not in definition_ids
                    for dep in d.dependencies
                )
                if deps_satisfied:
                    sorted_list.append(d)
                    remaining.remove(d)

        # Add any remaining (may have circular deps)
        sorted_list.extend(remaining)
        return sorted_list

    def get_errors(self) -> List[Dict[str, Any]]:
        """Get list of calculation errors.

        Returns:
            List of error dictionaries
        """
        return self._errors

    def get_summary(self) -> Dict[str, Any]:
        """Get summary of calculated metrics.

        Returns:
            Summary dictionary
        """
        categories = {}
        for metric_id, value in self.cache.items():
            category = metric_id[1] if len(metric_id) > 1 else "?"
            if category not in categories:
                categories[category] = {"count": 0, "metrics": []}
            categories[category]["count"] += 1
            categories[category]["metrics"].append(metric_id)

        return {
            "total_calculated": len(self.cache),
            "total_errors": len(self._errors),
            "categories": categories,
            "window_days": self.data.window_days,
            "window_start": self.data.window_start.isoformat(),
            "window_end": self.data.window_end.isoformat(),
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert all results to dictionary.

        Returns:
            Dictionary with all metric values
        """
        return {
            metric_id: value.to_dict()
            for metric_id, value in sorted(self.cache.items())
        }

    def to_json(self, path: Path, indent: int = 2) -> Path:
        """Write results to JSON file.

        Args:
            path: Output file path
            indent: JSON indentation

        Returns:
            Path to written file
        """
        path.parent.mkdir(parents=True, exist_ok=True)

        output = {
            "generated_at": datetime.now().isoformat(),
            "summary": self.get_summary(),
            "metrics": self.to_dict(),
            "errors": self._errors,
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=indent, ensure_ascii=False, default=str)

        return path

    def get_metric_value(self, metric_id: str) -> Any:
        """Get just the value for a metric.

        Args:
            metric_id: The metric ID

        Returns:
            The metric value or None
        """
        if metric_id in self.cache:
            return self.cache[metric_id].value
        return None

    def get_metrics_by_type(self, metric_type: str) -> Dict[str, MetricValue]:
        """Get all calculated metrics of a specific type.

        Args:
            metric_type: Type like "ratio", "int", "duration"

        Returns:
            Dictionary of matching metrics
        """
        return {
            metric_id: value
            for metric_id, value in self.cache.items()
            if metric_id in METRIC_DEFINITIONS
            and METRIC_DEFINITIONS[metric_id].metric_type.value == metric_type
        }

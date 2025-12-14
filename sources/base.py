"""Base class for data source extractors."""

import json
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from database import MetricsDatabase
from redaction import redact_dict


class BaseSource(ABC):
    """Abstract base class for all data source extractors.

    Each source extractor handles one or more related data sources
    from Claude Code's local storage.
    """

    # Unique identifier for this source
    name: str = "base"

    # Human-readable description
    description: str = "Base source extractor"

    # List of paths this source reads from (for documentation)
    source_paths: List[str] = []

    def __init__(self, include_sensitive: bool = False):
        """Initialize the extractor.

        Args:
            include_sensitive: If True, include sensitive data without redaction
        """
        self.include_sensitive = include_sensitive
        self._data: Optional[Dict[str, Any]] = None
        self._extracted_at: Optional[str] = None

    @abstractmethod
    def extract(self) -> Dict[str, Any]:
        """Extract data from the source.

        Returns:
            Dictionary containing the extracted data
        """
        pass

    def get_data(self) -> Dict[str, Any]:
        """Get the extracted data, extracting if necessary.

        Returns:
            Dictionary containing the extracted data
        """
        if self._data is None:
            self._data = self.extract()
            self._extracted_at = datetime.now().isoformat()
        return self._data

    def to_dict(self) -> Dict[str, Any]:
        """Get the data as a dictionary with metadata.

        Returns:
            Dictionary with source info and extracted data
        """
        data = self.get_data()
        return {
            "source": self.name,
            "description": self.description,
            "source_paths": self.source_paths,
            "extracted_at": self._extracted_at,
            "include_sensitive": self.include_sensitive,
            "data": data,
        }

    def to_json(self, path: Path, indent: int = 2) -> Path:
        """Write the extracted data to a JSON file.

        Args:
            path: Path to write the JSON file
            indent: JSON indentation level

        Returns:
            Path to the written file
        """
        data = self.to_dict()

        # Apply redaction if needed
        if not self.include_sensitive:
            data = redact_dict(data, include_sensitive=False)

        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False, default=str)

        return path

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write the extracted data to SQLite database.

        Override this method in subclasses to implement
        source-specific database insertion.

        Args:
            db: MetricsDatabase instance
        """
        pass

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the extracted data.

        Override this method in subclasses to provide
        source-specific summary statistics.

        Returns:
            Dictionary with summary statistics
        """
        data = self.get_data()
        return {
            "source": self.name,
            "record_count": len(data) if isinstance(data, (list, dict)) else 1,
        }

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name})>"


class CompositeSource(BaseSource):
    """A source that combines multiple sub-sources."""

    name = "composite"
    description = "Composite source combining multiple extractors"

    def __init__(
        self,
        sources: List[BaseSource],
        include_sensitive: bool = False
    ):
        """Initialize the composite source.

        Args:
            sources: List of source extractors to combine
            include_sensitive: If True, include sensitive data
        """
        super().__init__(include_sensitive)
        self.sources = sources

    def extract(self) -> Dict[str, Any]:
        """Extract data from all sub-sources.

        Returns:
            Dictionary mapping source names to their data
        """
        result = {}
        for source in self.sources:
            try:
                result[source.name] = source.get_data()
            except Exception as e:
                result[source.name] = {"error": str(e)}
        return result

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write all sub-source data to SQLite."""
        for source in self.sources:
            try:
                source.to_sqlite(db)
            except Exception:
                pass  # Skip sources that fail

    def get_summary(self) -> Dict[str, Any]:
        """Get summary from all sub-sources."""
        summaries = {}
        for source in self.sources:
            try:
                summaries[source.name] = source.get_summary()
            except Exception as e:
                summaries[source.name] = {"error": str(e)}
        return {
            "source": self.name,
            "sub_sources": summaries,
            "total_sources": len(self.sources),
        }

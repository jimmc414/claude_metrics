"""Main metrics extractor orchestrator."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Type

__version__ = "0.1.0"
from database import MetricsDatabase
from sources import (
    ALL_SOURCES,
    BaseSource,
    StatsCacheSource,
    SettingsSource,
    GlobalStateSource,
    CredentialsSource,
    HistorySource,
    SessionsSource,
    TodosSource,
    PlansSource,
    ExtensionsSource,
)


class MetricsExtractor:
    """Main orchestrator for extracting Claude Code metrics.

    Coordinates extraction from all data sources and writes
    to JSON files and/or SQLite database.
    """

    def __init__(
        self,
        output_dir: Optional[Path] = None,
        include_sensitive: bool = False,
        sources: Optional[List[str]] = None,
    ):
        """Initialize the extractor.

        Args:
            output_dir: Directory for output files (default: ./claude_metrics_output)
            include_sensitive: If True, include sensitive data
            sources: List of source names to extract (default: all)
        """
        self.output_dir = output_dir or Path("./claude_metrics_output")
        self.include_sensitive = include_sensitive
        self.sources_to_extract = sources or list(ALL_SOURCES.keys())
        self._extractors: Dict[str, BaseSource] = {}
        self._results: Dict[str, Any] = {}
        self._extraction_time: Optional[str] = None

    def _create_extractor(self, name: str) -> Optional[BaseSource]:
        """Create an extractor instance for the given source."""
        if name not in ALL_SOURCES:
            return None

        source_class = ALL_SOURCES[name]

        # Handle sources with special initialization
        if name == "sessions":
            return source_class(
                include_sensitive=self.include_sensitive,
                include_full_content=False,  # Don't include full content by default
            )
        elif name == "plans":
            return source_class(
                include_sensitive=self.include_sensitive,
                include_content=False,  # Don't include full content by default
            )
        else:
            return source_class(include_sensitive=self.include_sensitive)

    def extract_all(self, progress_callback=None) -> Dict[str, Any]:
        """Extract data from all configured sources.

        Args:
            progress_callback: Optional callback(source_name, status) for progress

        Returns:
            Dictionary with extraction results and summary
        """
        self._extraction_time = datetime.now().isoformat()
        self._results = {}
        errors = []

        for i, source_name in enumerate(self.sources_to_extract):
            if progress_callback:
                progress_callback(source_name, "extracting")

            try:
                extractor = self._create_extractor(source_name)
                if extractor is None:
                    errors.append({"source": source_name, "error": "Unknown source"})
                    continue

                self._extractors[source_name] = extractor
                self._results[source_name] = extractor.get_data()

                if progress_callback:
                    progress_callback(source_name, "done")

            except Exception as e:
                errors.append({"source": source_name, "error": str(e)})
                if progress_callback:
                    progress_callback(source_name, "error")

        return {
            "version": __version__,
            "extracted_at": self._extraction_time,
            "include_sensitive": self.include_sensitive,
            "sources_extracted": list(self._results.keys()),
            "sources_failed": [e["source"] for e in errors],
            "errors": errors,
            "data": self._results,
        }

    def extract_source(self, source_name: str) -> Dict[str, Any]:
        """Extract data from a single source.

        Args:
            source_name: Name of the source to extract

        Returns:
            Extracted data from the source
        """
        extractor = self._create_extractor(source_name)
        if extractor is None:
            return {"error": f"Unknown source: {source_name}"}

        self._extractors[source_name] = extractor
        return extractor.get_data()

    def write_json(self, output_dir: Optional[Path] = None) -> List[Path]:
        """Write extracted data to JSON files.

        Args:
            output_dir: Override output directory

        Returns:
            List of paths to written files
        """
        out_dir = output_dir or self.output_dir
        json_dir = out_dir / "json"
        json_dir.mkdir(parents=True, exist_ok=True)

        written_files = []

        for source_name, extractor in self._extractors.items():
            try:
                output_path = json_dir / f"{source_name}.json"
                extractor.to_json(output_path)
                written_files.append(output_path)
            except Exception as e:
                # Log error but continue
                pass

        # Write summary file
        summary_path = out_dir / "extraction_summary.json"
        summary = self.get_summary()
        with open(summary_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False, default=str)
        written_files.append(summary_path)

        return written_files

    def write_sqlite(self, output_dir: Optional[Path] = None) -> Path:
        """Write extracted data to SQLite database.

        Args:
            output_dir: Override output directory

        Returns:
            Path to the database file
        """
        out_dir = output_dir or self.output_dir
        out_dir.mkdir(parents=True, exist_ok=True)

        db_path = out_dir / "claude_metrics.db"

        with MetricsDatabase(db_path) as db:
            # Record extraction metadata
            db.record_extraction(
                version=__version__,
                include_sensitive=self.include_sensitive,
                sources=list(self._extractors.keys()),
            )

            # Write each source
            for source_name, extractor in self._extractors.items():
                try:
                    extractor.to_sqlite(db)
                except Exception as e:
                    # Log error but continue
                    pass

        return db_path

    def write_all(self, output_dir: Optional[Path] = None) -> Dict[str, Any]:
        """Write extracted data to both JSON and SQLite.

        Args:
            output_dir: Override output directory

        Returns:
            Dictionary with paths to written files
        """
        out_dir = output_dir or self.output_dir

        json_files = self.write_json(out_dir)
        db_path = self.write_sqlite(out_dir)

        return {
            "output_dir": str(out_dir),
            "json_files": [str(p) for p in json_files],
            "database": str(db_path),
        }

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the extraction.

        Returns:
            Dictionary with summary statistics
        """
        summaries = {}

        for source_name, extractor in self._extractors.items():
            try:
                summaries[source_name] = extractor.get_summary()
            except Exception as e:
                summaries[source_name] = {"error": str(e)}

        return {
            "version": __version__,
            "extracted_at": self._extraction_time,
            "include_sensitive": self.include_sensitive,
            "sources_extracted": list(self._extractors.keys()),
            "source_count": len(self._extractors),
            "summaries": summaries,
        }

    @classmethod
    def list_sources(cls) -> List[Dict[str, str]]:
        """List all available sources.

        Returns:
            List of source info dictionaries
        """
        sources = []
        for name, source_class in ALL_SOURCES.items():
            sources.append({
                "name": name,
                "description": source_class.description,
                "paths": source_class.source_paths,
            })
        return sources

"""Tests for the MetricsExtractor class."""

import json
from pathlib import Path

import pytest

from metrics_extractor import MetricsExtractor
from sources import ALL_SOURCES


class TestMetricsExtractor:
    """Tests for MetricsExtractor."""

    def test_init_default(self, temp_output_dir):
        """Test default initialization."""
        extractor = MetricsExtractor(output_dir=temp_output_dir)

        assert extractor.output_dir == temp_output_dir
        assert extractor.include_sensitive is False
        assert set(extractor.sources_to_extract) == set(ALL_SOURCES.keys())

    def test_init_with_sources(self, temp_output_dir):
        """Test initialization with specific sources."""
        extractor = MetricsExtractor(
            output_dir=temp_output_dir,
            sources=["stats_cache", "settings"]
        )

        assert extractor.sources_to_extract == ["stats_cache", "settings"]

    def test_init_include_sensitive(self, temp_output_dir):
        """Test initialization with include_sensitive=True."""
        extractor = MetricsExtractor(
            output_dir=temp_output_dir,
            include_sensitive=True
        )

        assert extractor.include_sensitive is True

    def test_list_sources(self):
        """Test listing available sources."""
        sources = MetricsExtractor.list_sources()

        assert isinstance(sources, list)
        assert len(sources) == len(ALL_SOURCES)

        for source in sources:
            assert "name" in source
            assert "description" in source
            assert "paths" in source
            assert source["name"] in ALL_SOURCES

    def test_extract_unknown_source(self, temp_output_dir):
        """Test extracting from unknown source returns error."""
        extractor = MetricsExtractor(output_dir=temp_output_dir)
        result = extractor.extract_source("nonexistent_source")

        assert "error" in result

    def test_get_summary_empty(self, temp_output_dir):
        """Test getting summary before extraction."""
        extractor = MetricsExtractor(output_dir=temp_output_dir)
        summary = extractor.get_summary()

        assert "version" in summary
        assert summary["source_count"] == 0


class TestSourceNames:
    """Test source name consistency."""

    def test_all_sources_have_required_attributes(self):
        """Test all sources have name, description, source_paths."""
        for name, source_class in ALL_SOURCES.items():
            assert hasattr(source_class, "name"), f"{name} missing 'name'"
            assert hasattr(source_class, "description"), f"{name} missing 'description'"
            assert hasattr(source_class, "source_paths"), f"{name} missing 'source_paths'"

    def test_source_names_match_keys(self):
        """Test source class names match dictionary keys."""
        for key, source_class in ALL_SOURCES.items():
            assert source_class.name == key, f"Key '{key}' != class name '{source_class.name}'"

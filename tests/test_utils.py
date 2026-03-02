"""Tests for utils.py -- utility functions."""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

from tests.conftest import FIXED_NOW
from utils import (
    count_jsonl_lines,
    date_to_str,
    datetime_to_hour,
    datetime_to_weekday,
    dir_name_to_project_path,
    format_bytes,
    get_claude_dir,
    get_date_range,
    is_weekend,
    is_within_window,
    parse_iso_timestamp,
    project_path_to_dir_name,
    read_json_file,
    read_jsonl_file,
    safe_get,
    str_to_date,
    unix_ms_to_datetime,
)


# -- get_claude_dir -------------------------------------------------------------

class TestGetClaudeDir:
    def test_returns_path_ending_in_dot_claude(self):
        result = get_claude_dir()
        assert isinstance(result, Path)
        assert result.name == ".claude"

    def test_returns_path_under_home(self):
        result = get_claude_dir()
        assert result.parent == Path.home()


# -- parse_iso_timestamp --------------------------------------------------------

class TestParseIsoTimestamp:
    def test_none_input(self):
        assert parse_iso_timestamp(None) is None

    def test_empty_string(self):
        assert parse_iso_timestamp("") is None

    def test_valid_iso_with_offset(self):
        result = parse_iso_timestamp("2025-01-15T14:00:00+00:00")
        assert result is not None
        assert result.year == 2025
        assert result.month == 1
        assert result.day == 15
        assert result.hour == 14

    def test_z_suffix(self):
        result = parse_iso_timestamp("2025-01-15T14:00:00Z")
        assert result is not None
        assert result.year == 2025

    def test_invalid_format(self):
        assert parse_iso_timestamp("not-a-date") is None

    def test_partial_date_string(self):
        # fromisoformat can parse date-only in Python 3.7+
        result = parse_iso_timestamp("2025-01-15")
        assert result is not None
        assert result.year == 2025


# -- unix_ms_to_datetime --------------------------------------------------------

class TestUnixMsToDatetime:
    def test_zero_returns_none(self):
        # 0 is falsy, so unix_ms_to_datetime returns None
        assert unix_ms_to_datetime(0) is None

    def test_valid_ms(self):
        # 1737000000000 ms = 2025-01-16 approximately
        result = unix_ms_to_datetime(1737000000000)
        assert result is not None
        assert result.year == 2025

    def test_negative_value(self):
        # Negative ms is truthy but represents pre-epoch date
        result = unix_ms_to_datetime(-1000)
        # datetime.fromtimestamp(-1) should work on most platforms
        assert result is not None

    def test_none_input(self):
        assert unix_ms_to_datetime(None) is None


# -- format_bytes ---------------------------------------------------------------

class TestFormatBytes:
    def test_zero(self):
        assert format_bytes(0) == "0.0 B"

    def test_small_bytes(self):
        assert format_bytes(500) == "500.0 B"

    def test_exact_kb(self):
        assert format_bytes(1024) == "1.0 KB"

    def test_kilobytes(self):
        assert format_bytes(1536) == "1.5 KB"

    def test_megabytes(self):
        result = format_bytes(2 * 1024 * 1024)
        assert result == "2.0 MB"

    def test_gigabytes(self):
        result = format_bytes(3 * 1024 * 1024 * 1024)
        assert result == "3.0 GB"

    def test_terabytes(self):
        result = format_bytes(1024 ** 4)
        assert result == "1.0 TB"


# -- safe_get -------------------------------------------------------------------

class TestSafeGet:
    def test_top_level_key(self):
        data = {"key": "value"}
        assert safe_get(data, "key") == "value"

    def test_nested_keys(self):
        data = {"a": {"b": {"c": 42}}}
        assert safe_get(data, "a", "b", "c") == 42

    def test_missing_key_returns_none(self):
        data = {"a": 1}
        assert safe_get(data, "b") is None

    def test_missing_key_custom_default(self):
        data = {"a": 1}
        assert safe_get(data, "b", default="missing") == "missing"

    def test_non_dict_intermediate(self):
        data = {"a": "string_not_dict"}
        assert safe_get(data, "a", "b") is None

    def test_none_intermediate_value(self):
        data = {"a": None}
        assert safe_get(data, "a", "b") is None

    def test_deeply_nested(self):
        data = {"l1": {"l2": {"l3": {"l4": "deep"}}}}
        assert safe_get(data, "l1", "l2", "l3", "l4") == "deep"


# -- project_path_to_dir_name ---------------------------------------------------

class TestProjectPathToDirName:
    def test_standard_path(self):
        result = project_path_to_dir_name("/mnt/c/python/myproject")
        assert result == "mnt-c-python-myproject"

    def test_leading_slash_stripped(self):
        result = project_path_to_dir_name("/home/user/code")
        assert result == "home-user-code"

    def test_root_path(self):
        result = project_path_to_dir_name("/")
        # "/" -> "-" -> lstrip "-" -> ""
        assert result == ""


# -- dir_name_to_project_path ---------------------------------------------------

class TestDirNameToProjectPath:
    def test_standard_conversion(self):
        result = dir_name_to_project_path("-mnt-c-python-myproject")
        assert result == "/mnt/c/python/myproject"

    def test_no_leading_dash(self):
        result = dir_name_to_project_path("mnt-c-python-myproject")
        assert result == "/mnt/c/python/myproject"

    @pytest.mark.xfail(
        reason="Bug #2: hyphens in project names are fundamentally lossy -- "
        "all single hyphens become slashes so 'my-project' becomes 'my/project'"
    )
    def test_hyphenated_project_name(self):
        """Regression test: project names containing hyphens are mangled."""
        result = dir_name_to_project_path("-mnt-c-python-my-project")
        assert result == "/mnt/c/python/my-project"

    def test_dot_prefix_path(self):
        """Double-dash correctly maps to dot-prefixed path components."""
        result = dir_name_to_project_path("-home-jim--local-share-project")
        assert result == "/home/jim/.local/share/project"


# -- read_json_file -------------------------------------------------------------

class TestReadJsonFile:
    def test_nonexistent_file(self, tmp_path):
        result = read_json_file(tmp_path / "nonexistent.json")
        assert result is None

    def test_valid_json(self, tmp_path):
        f = tmp_path / "data.json"
        f.write_text(json.dumps({"key": "value"}))
        result = read_json_file(f)
        assert result == {"key": "value"}

    def test_invalid_json(self, tmp_path):
        f = tmp_path / "bad.json"
        f.write_text("{invalid json")
        result = read_json_file(f)
        assert result is None

    def test_empty_file(self, tmp_path):
        f = tmp_path / "empty.json"
        f.write_text("")
        result = read_json_file(f)
        assert result is None


# -- read_jsonl_file ------------------------------------------------------------

class TestReadJsonlFile:
    def test_nonexistent_file(self, tmp_path):
        records = list(read_jsonl_file(tmp_path / "nonexistent.jsonl"))
        assert records == []

    def test_empty_file(self, tmp_path):
        f = tmp_path / "empty.jsonl"
        f.write_text("")
        records = list(read_jsonl_file(f))
        assert records == []

    def test_valid_records(self, tmp_path):
        f = tmp_path / "data.jsonl"
        f.write_text('{"a":1}\n{"b":2}\n')
        records = list(read_jsonl_file(f))
        assert len(records) == 2
        assert records[0] == {"a": 1}
        assert records[1] == {"b": 2}

    def test_malformed_lines_skipped(self, tmp_path):
        f = tmp_path / "data.jsonl"
        f.write_text('{"a":1}\n{bad line\n{"b":2}\n')
        records = list(read_jsonl_file(f))
        assert len(records) == 2

    def test_empty_lines_skipped(self, tmp_path):
        f = tmp_path / "data.jsonl"
        f.write_text('{"a":1}\n\n\n{"b":2}\n')
        records = list(read_jsonl_file(f))
        assert len(records) == 2


# -- count_jsonl_lines ----------------------------------------------------------

class TestCountJsonlLines:
    def test_nonexistent_file(self, tmp_path):
        assert count_jsonl_lines(tmp_path / "nonexistent.jsonl") == 0

    def test_empty_file(self, tmp_path):
        f = tmp_path / "empty.jsonl"
        f.write_text("")
        assert count_jsonl_lines(f) == 0

    def test_normal_file(self, tmp_path):
        f = tmp_path / "data.jsonl"
        f.write_text('{"a":1}\n{"b":2}\n{"c":3}\n')
        assert count_jsonl_lines(f) == 3

    def test_blank_lines_not_counted(self, tmp_path):
        f = tmp_path / "data.jsonl"
        f.write_text('{"a":1}\n\n{"b":2}\n\n')
        assert count_jsonl_lines(f) == 2


# -- date_to_str / str_to_date --------------------------------------------------

class TestDateConversions:
    def test_date_to_str(self):
        dt = datetime(2025, 1, 15, 10, 30, 0)
        assert date_to_str(dt) == "2025-01-15"

    def test_str_to_date_valid(self):
        result = str_to_date("2025-01-15")
        assert result is not None
        assert result.year == 2025
        assert result.month == 1
        assert result.day == 15

    def test_str_to_date_invalid(self):
        assert str_to_date("not-a-date") is None

    def test_str_to_date_none(self):
        assert str_to_date(None) is None

    def test_roundtrip(self):
        dt = datetime(2025, 6, 20, 12, 0, 0)
        s = date_to_str(dt)
        result = str_to_date(s)
        assert result.year == dt.year
        assert result.month == dt.month
        assert result.day == dt.day


# -- is_within_window -----------------------------------------------------------

class TestIsWithinWindow:
    def test_none_returns_false(self):
        cutoff = FIXED_NOW
        assert is_within_window(None, cutoff) is False

    def test_datetime_before_cutoff(self):
        cutoff = FIXED_NOW
        past = FIXED_NOW - timedelta(days=5)
        assert is_within_window(past, cutoff) is False

    def test_datetime_after_cutoff(self):
        cutoff = FIXED_NOW - timedelta(days=1)
        assert is_within_window(FIXED_NOW, cutoff) is True

    def test_datetime_equal_to_cutoff(self):
        assert is_within_window(FIXED_NOW, FIXED_NOW) is True

    def test_iso_string_timestamp(self):
        cutoff = datetime(2025, 1, 14, 0, 0, 0, tzinfo=timezone.utc)
        assert is_within_window("2025-01-15T14:00:00+00:00", cutoff) is True

    def test_int_unix_ms_timestamp(self):
        cutoff = datetime(2025, 1, 1, 0, 0, 0)
        ts_ms = int(datetime(2025, 1, 15, 0, 0, 0).timestamp() * 1000)
        assert is_within_window(ts_ms, cutoff) is True


# -- is_weekend -----------------------------------------------------------------

class TestIsWeekend:
    def test_weekday_wednesday(self):
        # 2025-01-15 is a Wednesday
        assert is_weekend(datetime(2025, 1, 15)) is False

    def test_weekday_monday(self):
        # 2025-01-13 is a Monday
        assert is_weekend(datetime(2025, 1, 13)) is False

    def test_saturday(self):
        # 2025-01-18 is a Saturday
        assert is_weekend(datetime(2025, 1, 18)) is True

    def test_sunday(self):
        # 2025-01-19 is a Sunday
        assert is_weekend(datetime(2025, 1, 19)) is True


# -- get_date_range -------------------------------------------------------------

class TestGetDateRange:
    def test_same_day(self):
        dt = datetime(2025, 1, 15, 10, 0)
        result = get_date_range(dt, dt)
        assert result == ["2025-01-15"]

    def test_multi_day_range(self):
        start = datetime(2025, 1, 10, 8, 0)
        end = datetime(2025, 1, 13, 18, 0)
        result = get_date_range(start, end)
        assert result == ["2025-01-10", "2025-01-11", "2025-01-12", "2025-01-13"]

    def test_single_day_different_times(self):
        start = datetime(2025, 1, 15, 1, 0)
        end = datetime(2025, 1, 15, 23, 0)
        result = get_date_range(start, end)
        assert result == ["2025-01-15"]

    def test_two_consecutive_days(self):
        start = datetime(2025, 1, 10, 0, 0)
        end = datetime(2025, 1, 11, 0, 0)
        result = get_date_range(start, end)
        assert result == ["2025-01-10", "2025-01-11"]


# -- datetime_to_hour -----------------------------------------------------------

class TestDatetimeToHour:
    def test_extracts_hour(self):
        dt = datetime(2025, 1, 15, 14, 30, 0)
        assert datetime_to_hour(dt) == 14

    def test_midnight(self):
        dt = datetime(2025, 1, 15, 0, 0, 0)
        assert datetime_to_hour(dt) == 0

    def test_end_of_day(self):
        dt = datetime(2025, 1, 15, 23, 59, 59)
        assert datetime_to_hour(dt) == 23


# -- datetime_to_weekday --------------------------------------------------------

class TestDatetimeToWeekday:
    def test_monday(self):
        # 2025-01-13 is a Monday
        dt = datetime(2025, 1, 13)
        assert datetime_to_weekday(dt) == 0

    def test_sunday(self):
        # 2025-01-19 is a Sunday
        dt = datetime(2025, 1, 19)
        assert datetime_to_weekday(dt) == 6

    def test_friday(self):
        # 2025-01-17 is a Friday
        dt = datetime(2025, 1, 17)
        assert datetime_to_weekday(dt) == 4

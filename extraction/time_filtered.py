"""Time-filtered extractor combining multiple sources."""

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Generator

from .data_classes import (
    ExtractedData30Day,
    SessionData,
    DailyActivity,
    ToolCallData,
    MessageData,
    ModelUsageData,
)


class TimeFilteredExtractor:
    """Extract data from all sources within a time window.

    This extractor filters data to the last N days (default 30) for
    efficient derived metrics calculation.
    """

    def __init__(self, days: int = 30, include_sensitive: bool = False):
        """Initialize the time-filtered extractor.

        Args:
            days: Number of days to include in the time window
            include_sensitive: If True, include sensitive data without redaction
        """
        self.days = days
        self.include_sensitive = include_sensitive
        # Use UTC timezone-aware datetime to match parsed timestamps
        self._now_utc = datetime.now(timezone.utc)
        self.cutoff = self._now_utc - timedelta(days=days)
        self.cutoff_iso = self.cutoff.isoformat()
        self.cutoff_unix_ms = int(self.cutoff.timestamp() * 1000)
        # Also keep a naive datetime for comparisons with naive timestamps
        self._now = datetime.now()
        self._cutoff_naive = self._now - timedelta(days=days)

    def _is_within_window(self, timestamp: Optional[datetime]) -> bool:
        """Check if a timestamp is within the time window.

        Handles both timezone-aware and naive datetimes.

        Args:
            timestamp: The timestamp to check

        Returns:
            True if timestamp is within window
        """
        if timestamp is None:
            return False

        # Handle timezone-aware timestamps
        if timestamp.tzinfo is not None:
            return timestamp >= self.cutoff
        # Handle naive timestamps
        return timestamp >= self._cutoff_naive

    def extract(self) -> ExtractedData30Day:
        """Extract all data within the time window.

        Returns:
            ExtractedData30Day containing all filtered data
        """
        data = ExtractedData30Day(
            window_start=self.cutoff,
            window_end=self._now,
            window_days=self.days,
        )

        # Extract from each source
        self._extract_sessions(data)
        self._extract_stats_cache(data)
        self._aggregate_tool_calls(data)
        self._aggregate_file_operations(data)
        self._aggregate_model_usage(data)
        self._compute_hourly_distribution(data)
        self._compute_active_dates(data)

        return data

    def _extract_sessions(self, data: ExtractedData30Day) -> None:
        """Extract sessions from JSONL files within the time window."""
        from utils import (
            get_claude_dir,
            read_jsonl_file,
            parse_iso_timestamp,
            dir_name_to_project_path,
            safe_get,
        )

        projects_dir = get_claude_dir() / "projects"
        if not projects_dir.exists():
            return

        for project_dir in projects_dir.iterdir():
            if not project_dir.is_dir():
                continue

            project_path = dir_name_to_project_path(project_dir.name)

            for jsonl_file in project_dir.glob("*.jsonl"):
                if not jsonl_file.is_file():
                    continue

                session = self._extract_single_session(
                    jsonl_file, project_path
                )
                if session is not None:
                    data.sessions.append(session)
                    data.total_sessions += 1
                    data.total_messages += session.message_count
                    data.total_cost_usd += session.cost_usd
                    data.total_tokens["input"] += session.total_input_tokens
                    data.total_tokens["output"] += session.total_output_tokens
                    data.total_tokens["cache_read"] += session.total_cache_read_tokens

    def _extract_single_session(
        self, file_path: Path, project_path: str
    ) -> Optional[SessionData]:
        """Extract a single session if it falls within the time window."""
        from utils import read_jsonl_file, parse_iso_timestamp, safe_get

        session_id = file_path.stem
        is_agent = session_id.startswith("agent-")

        messages_in_window = []
        tool_calls_in_window = []
        models_used = set()
        total_input_tokens = 0
        total_output_tokens = 0
        total_cache_read = 0
        total_cost = 0.0
        user_count = 0
        assistant_count = 0
        first_timestamp = None
        last_timestamp = None
        session_in_window = False

        for record in read_jsonl_file(file_path):
            msg_type = record.get("type")

            # Skip file history snapshots
            if msg_type == "file-history-snapshot":
                continue

            # Check timestamp against window
            timestamp_str = record.get("timestamp")
            timestamp = parse_iso_timestamp(timestamp_str) if timestamp_str else None

            if timestamp:
                if self._is_within_window(timestamp):
                    session_in_window = True
                else:
                    continue  # Skip messages before cutoff

                if first_timestamp is None:
                    first_timestamp = timestamp
                last_timestamp = timestamp

            # Count by type
            if msg_type == "user":
                user_count += 1
            elif msg_type == "assistant":
                assistant_count += 1

            # Extract message content
            message = record.get("message", {})
            role = message.get("role")
            model = message.get("model")

            if model:
                models_used.add(model)

            # Extract usage stats
            usage = message.get("usage", {})
            input_tokens = usage.get("input_tokens", 0)
            output_tokens = usage.get("output_tokens", 0)
            cache_read = usage.get("cache_read_input_tokens", 0)

            total_input_tokens += input_tokens
            total_output_tokens += output_tokens
            total_cache_read += cache_read

            # Extract cost
            cost_usd = record.get("costUSD", 0) or 0
            total_cost += cost_usd

            # Extract thinking info
            content = message.get("content", [])
            has_thinking = False
            thinking_length = 0
            msg_tool_calls = []

            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict):
                        block_type = block.get("type")

                        if block_type == "thinking":
                            has_thinking = True
                            thinking_length = len(block.get("thinking", ""))

                        elif block_type == "tool_use":
                            tool_call = ToolCallData(
                                tool_name=block.get("name", "unknown"),
                                timestamp=timestamp or self._now,
                                session_id=session_id,
                                message_uuid=record.get("uuid"),
                                duration_ms=None,
                                total_duration_ms=None,
                                success=True,  # Default, updated by result
                                is_error=False,
                                is_interrupted=False,
                                file_path=None,
                            )
                            msg_tool_calls.append(tool_call)

            # Extract tool result info
            tool_result = record.get("toolUseResult")
            if tool_result and isinstance(tool_result, dict):
                duration_ms = tool_result.get("durationMs")
                total_duration_ms = tool_result.get("totalDurationMs")
                is_error = tool_result.get("status") == "error"
                is_interrupted = tool_result.get("interrupted", False)
                file_path_result = tool_result.get("filePath") or safe_get(
                    tool_result, "file", "filePath"
                )

                # Update the last tool call with result info
                if msg_tool_calls:
                    last_tool = msg_tool_calls[-1]
                    last_tool.duration_ms = duration_ms
                    last_tool.total_duration_ms = total_duration_ms
                    last_tool.is_error = is_error
                    last_tool.is_interrupted = is_interrupted
                    last_tool.success = not is_error and not is_interrupted
                    last_tool.file_path = file_path_result

            tool_calls_in_window.extend(msg_tool_calls)

            # Create message data
            if timestamp:
                msg_data = MessageData(
                    uuid=record.get("uuid", ""),
                    session_id=session_id,
                    timestamp=timestamp,
                    message_type=msg_type or "unknown",
                    role=role,
                    model=model,
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    cache_read_tokens=cache_read,
                    cost_usd=cost_usd,
                    has_thinking=has_thinking,
                    thinking_length=thinking_length,
                    tool_call_count=len(msg_tool_calls),
                )
                messages_in_window.append(msg_data)

        # Only return session if it has messages in window
        if not session_in_window or not messages_in_window:
            return None

        # Calculate duration
        duration_ms = 0
        if first_timestamp and last_timestamp:
            duration_ms = int((last_timestamp - first_timestamp).total_seconds() * 1000)

        # Determine primary model
        primary_model = None
        if models_used:
            primary_model = sorted(models_used)[-1]

        session = SessionData(
            session_id=session_id,
            project_path=project_path,
            start_time=first_timestamp or self.cutoff,
            end_time=last_timestamp,
            duration_ms=duration_ms,
            message_count=len(messages_in_window),
            user_message_count=user_count,
            assistant_message_count=assistant_count,
            tool_call_count=len(tool_calls_in_window),
            cost_usd=total_cost,
            model=primary_model,
            models_used=sorted(models_used),
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_cache_read_tokens=total_cache_read,
            is_agent=is_agent,
        )

        # Add messages and tool calls to the main data
        # (This will be done via data.messages and data.tool_calls)

        return session

    def _extract_stats_cache(self, data: ExtractedData30Day) -> None:
        """Extract from stats-cache.json, filtering by date."""
        from utils import get_claude_dir, read_json_file

        path = get_claude_dir() / "stats-cache.json"
        stats = read_json_file(path)

        if not stats:
            return

        cutoff_date_str = self.cutoff.strftime("%Y-%m-%d")

        # Filter daily activity
        daily_activity = stats.get("dailyActivity", [])
        for day in daily_activity:
            date_str = day.get("date", "")
            if date_str >= cutoff_date_str:
                daily = DailyActivity(
                    date=date_str,
                    session_count=day.get("sessionCount", 0),
                    message_count=day.get("totalMessages", 0),
                    tool_call_count=day.get("toolCalls", 0),
                    cost_usd=day.get("totalCost", 0.0),
                    input_tokens=day.get("inputTokens", 0),
                    output_tokens=day.get("outputTokens", 0),
                    active_hours=0.0,  # Will compute later if needed
                )
                data.daily_activity.append(daily)

        # Get hour counts (cumulative, not filtered by date)
        hour_counts = stats.get("hourCounts", {})
        for hour_str, count in hour_counts.items():
            try:
                hour = int(hour_str)
                if 0 <= hour < 24:
                    data.hourly_distribution[hour] = count
            except (ValueError, TypeError):
                pass

    def _aggregate_tool_calls(self, data: ExtractedData30Day) -> None:
        """Aggregate tool calls from sessions."""
        for session in data.sessions:
            # Re-extract tool calls for this session
            self._extract_session_tool_calls(session, data)

    def _extract_session_tool_calls(
        self, session: SessionData, data: ExtractedData30Day
    ) -> None:
        """Extract tool calls for a specific session."""
        from utils import get_claude_dir, read_jsonl_file, parse_iso_timestamp, safe_get

        projects_dir = get_claude_dir() / "projects"
        # Convert project path back to directory name
        project_dir_name = session.project_path.replace("/", "-").lstrip("-")
        session_file = projects_dir / project_dir_name / f"{session.session_id}.jsonl"

        if not session_file.exists():
            return

        for record in read_jsonl_file(session_file):
            timestamp_str = record.get("timestamp")
            timestamp = parse_iso_timestamp(timestamp_str) if timestamp_str else None

            if not self._is_within_window(timestamp):
                continue

            message = record.get("message", {})
            content = message.get("content", [])

            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "tool_use":
                        tool_name = block.get("name", "unknown")

                        tool_call = ToolCallData(
                            tool_name=tool_name,
                            timestamp=timestamp,
                            session_id=session.session_id,
                            message_uuid=record.get("uuid"),
                            duration_ms=None,
                            total_duration_ms=None,
                            success=True,
                            is_error=False,
                            is_interrupted=False,
                            file_path=None,
                        )

                        # Check for tool result
                        tool_result = record.get("toolUseResult")
                        if tool_result and isinstance(tool_result, dict):
                            tool_call.duration_ms = tool_result.get("durationMs")
                            tool_call.total_duration_ms = tool_result.get(
                                "totalDurationMs"
                            )
                            tool_call.is_error = tool_result.get("status") == "error"
                            tool_call.is_interrupted = tool_result.get(
                                "interrupted", False
                            )
                            tool_call.success = (
                                not tool_call.is_error and not tool_call.is_interrupted
                            )
                            tool_call.file_path = tool_result.get(
                                "filePath"
                            ) or safe_get(tool_result, "file", "filePath")

                        data.tool_calls.append(tool_call)
                        data.total_tool_calls += 1

                        # Update tool counts
                        data.tool_counts[tool_name] = (
                            data.tool_counts.get(tool_name, 0) + 1
                        )

    def _aggregate_file_operations(self, data: ExtractedData30Day) -> None:
        """Aggregate file operations from tool calls."""
        for tool_call in data.tool_calls:
            if not tool_call.file_path:
                continue

            file_path = tool_call.file_path

            if tool_call.tool_name == "Read":
                data.files_read[file_path] = data.files_read.get(file_path, 0) + 1
            elif tool_call.tool_name == "Edit":
                data.files_edited[file_path] = data.files_edited.get(file_path, 0) + 1
            elif tool_call.tool_name == "Write":
                data.files_written[file_path] = data.files_written.get(file_path, 0) + 1

    def _aggregate_model_usage(self, data: ExtractedData30Day) -> None:
        """Aggregate model usage from sessions."""
        model_data: Dict[str, Dict[str, Any]] = defaultdict(
            lambda: {
                "message_count": 0,
                "input_tokens": 0,
                "output_tokens": 0,
                "cache_read_tokens": 0,
                "cost_usd": 0.0,
            }
        )

        for session in data.sessions:
            for model in session.models_used:
                # Estimate tokens per model (simplified - assumes even distribution)
                # A more accurate version would track per-message model usage
                model_count = len(session.models_used) or 1
                model_data[model]["message_count"] += (
                    session.message_count // model_count
                )
                model_data[model]["input_tokens"] += (
                    session.total_input_tokens // model_count
                )
                model_data[model]["output_tokens"] += (
                    session.total_output_tokens // model_count
                )
                model_data[model]["cache_read_tokens"] += (
                    session.total_cache_read_tokens // model_count
                )
                model_data[model]["cost_usd"] += session.cost_usd / model_count

        for model, stats in model_data.items():
            data.model_usage[model] = ModelUsageData(
                model=model,
                message_count=stats["message_count"],
                input_tokens=stats["input_tokens"],
                output_tokens=stats["output_tokens"],
                cache_read_tokens=stats["cache_read_tokens"],
                cost_usd=stats["cost_usd"],
            )

    def _compute_hourly_distribution(self, data: ExtractedData30Day) -> None:
        """Compute hourly distribution from session start times."""
        # If we already have hourly data from stats cache, use that
        if any(data.hourly_distribution.values()):
            return

        # Otherwise compute from sessions
        for session in data.sessions:
            if session.start_time:
                hour = session.start_time.hour
                data.hourly_distribution[hour] = (
                    data.hourly_distribution.get(hour, 0) + 1
                )

    def _compute_active_dates(self, data: ExtractedData30Day) -> None:
        """Compute list of active dates from sessions."""
        active_dates = set()

        for session in data.sessions:
            if session.start_time:
                date_str = session.start_time.strftime("%Y-%m-%d")
                active_dates.add(date_str)

        data.active_dates = sorted(active_dates)

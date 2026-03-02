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
    ToolChainLink,
    ConversationThread,
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
        # Note: tool calls are now aggregated directly in _extract_sessions()
        self._aggregate_file_operations(data)
        self._aggregate_model_usage(data)
        self._compute_hourly_distribution(data)
        self._compute_active_dates(data)
        self._extract_config(data)
        self._build_conversation_threads(data)
        self._build_tool_chains(data)

        return data

    def _extract_sessions(self, data: ExtractedData30Day) -> None:
        """Extract sessions from JSONL files within the time window."""
        from utils import (
            get_claude_dir,
            dir_name_to_project_path,
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

                session, tool_calls, messages = self._extract_single_session(
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

                    # Aggregate tool calls directly (fixes path conversion bug)
                    data.tool_calls.extend(tool_calls)
                    data.total_tool_calls += len(tool_calls)
                    for tc in tool_calls:
                        data.tool_counts[tc.tool_name] = (
                            data.tool_counts.get(tc.tool_name, 0) + 1
                        )

                        # Aggregate enhanced extraction data for K-N metrics
                        if tc.web_url:
                            data.web_urls_fetched.append(tc.web_url)
                        if tc.search_query:
                            data.search_queries.append(tc.search_query)
                        if tc.question_text:
                            data.questions_asked.append({
                                "header": tc.question_header,
                                "text": tc.question_text,
                                "options": tc.question_options,
                            })
                        if tc.tool_name == "Edit" and tc.edit_old_string is not None:
                            data.edit_operations.append({
                                "old_string": tc.edit_old_string,
                                "new_string": tc.edit_new_string,
                                "replace_all": tc.edit_replace_all,
                                "file_path": tc.file_path,
                            })

                    # Aggregate messages
                    data.messages.extend(messages)

    def _build_conversation_threads(self, data: ExtractedData30Day) -> None:
        """Build conversation thread trees from uuid/parentUuid linkage."""
        # Group messages by session
        session_messages: Dict[str, List[MessageData]] = defaultdict(list)
        for m in data.messages:
            session_messages[m.session_id].append(m)

        for session_id, messages in session_messages.items():
            # Build parent -> children map
            uuid_map = {m.uuid: m for m in messages if m.uuid}
            children: Dict[str, List[str]] = defaultdict(list)
            root_uuids = []

            for m in messages:
                if m.parent_uuid and m.parent_uuid in uuid_map:
                    children[m.parent_uuid].append(m.uuid)
                elif m.uuid:
                    root_uuids.append(m.uuid)

            # BFS from each root to compute thread stats
            for root_uuid in root_uuids:
                max_depth = 0
                branch_count = 0
                msg_count = 0
                sidechain_count = 0
                stop_reasons: Dict[str, int] = {}

                queue = [(root_uuid, 0)]
                while queue:
                    uuid, depth = queue.pop(0)
                    msg_count += 1
                    max_depth = max(max_depth, depth)

                    msg = uuid_map.get(uuid)
                    if msg:
                        if msg.is_sidechain:
                            sidechain_count += 1
                        if msg.stop_reason:
                            stop_reasons[msg.stop_reason] = (
                                stop_reasons.get(msg.stop_reason, 0) + 1
                            )

                    child_list = children.get(uuid, [])
                    if len(child_list) > 1:
                        branch_count += 1
                    for child_uuid in child_list:
                        queue.append((child_uuid, depth + 1))

                thread = ConversationThread(
                    session_id=session_id,
                    root_uuid=root_uuid,
                    max_depth=max_depth,
                    branch_count=branch_count,
                    message_count=msg_count,
                    sidechain_count=sidechain_count,
                    stop_reasons=stop_reasons,
                )
                data.conversation_threads.append(thread)

    def _build_tool_chains(self, data: ExtractedData30Day) -> None:
        """Build tool execution chains from consecutive tool calls."""
        # Group tool calls by session, sorted by timestamp
        session_tools: Dict[str, List[ToolCallData]] = defaultdict(list)
        for tc in data.tool_calls:
            if tc.tool_use_id:
                session_tools[tc.session_id].append(tc)

        for session_id, tools in session_tools.items():
            tools.sort(key=lambda t: t.timestamp)

            # Group into chains: consecutive calls in same message or within 60s
            current_chain: List[ToolChainLink] = []
            prev_tc = None

            for tc in tools:
                same_message = (
                    prev_tc is not None
                    and tc.message_uuid
                    and tc.message_uuid == prev_tc.message_uuid
                )
                within_window = (
                    prev_tc is not None
                    and (tc.timestamp - prev_tc.timestamp).total_seconds() <= 60
                )

                if current_chain and (same_message or within_window):
                    current_chain.append(ToolChainLink(
                        tool_use_id=tc.tool_use_id,
                        tool_name=tc.tool_name,
                        message_uuid=tc.message_uuid or "",
                        session_id=session_id,
                        timestamp=tc.timestamp,
                        is_error=tc.is_error,
                        duration_ms=tc.duration_ms,
                    ))
                else:
                    if len(current_chain) >= 2:
                        data.tool_chains.append(current_chain)
                    current_chain = [ToolChainLink(
                        tool_use_id=tc.tool_use_id,
                        tool_name=tc.tool_name,
                        message_uuid=tc.message_uuid or "",
                        session_id=session_id,
                        timestamp=tc.timestamp,
                        is_error=tc.is_error,
                        duration_ms=tc.duration_ms,
                    )]
                prev_tc = tc

            # Don't forget the last chain
            if len(current_chain) >= 2:
                data.tool_chains.append(current_chain)

    def _extract_single_session(
        self, file_path: Path, project_path: str
    ) -> Tuple[Optional[SessionData], List[ToolCallData], List[MessageData]]:
        """Extract a single session if it falls within the time window.

        Returns:
            Tuple of (SessionData or None, list of tool calls, list of messages)
        """
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
            else:
                continue  # Skip records without timestamps entirely

            # Count by type
            if msg_type == "user":
                user_count += 1
            elif msg_type == "assistant":
                assistant_count += 1

            # Extract message content
            message = record.get("message", {})
            role = message.get("role")
            model = message.get("model")

            # Extract structural fields
            parent_uuid = record.get("parentUuid")
            stop_reason = message.get("stop_reason") or record.get("stopReason")
            is_sidechain = record.get("isSidechain", False)

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

            # Extract thinking info and text content
            content = message.get("content", [])
            has_thinking = False
            thinking_length = 0
            msg_tool_calls = []
            text_parts = []

            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict):
                        block_type = block.get("type")

                        if block_type == "text":
                            text_parts.append(block.get("text", ""))

                        elif block_type == "thinking":
                            has_thinking = True
                            thinking_length = len(block.get("thinking", ""))

                        elif block_type == "tool_use":
                            tool_name = block.get("name", "unknown")
                            tool_input = block.get("input", {})

                            # Extract file_path from tool input for Read/Edit/Write
                            tool_file_path = None
                            if tool_name in ("Read", "Edit", "Write"):
                                tool_file_path = tool_input.get("file_path")

                            # Enhanced extraction for Categories K-N metrics
                            edit_old_string = None
                            edit_new_string = None
                            edit_replace_all = False
                            web_url = None
                            search_query = None
                            question_header = None
                            question_text = None
                            question_options = []

                            if tool_name == "Edit":
                                edit_old_string = tool_input.get("old_string")
                                edit_new_string = tool_input.get("new_string")
                                edit_replace_all = tool_input.get("replace_all", False)
                            elif tool_name == "WebFetch":
                                web_url = tool_input.get("url")
                            elif tool_name == "WebSearch":
                                search_query = tool_input.get("query")
                            elif tool_name == "AskUserQuestion":
                                questions = tool_input.get("questions", [])
                                if questions:
                                    q = questions[0]  # First question
                                    question_header = q.get("header")
                                    question_text = q.get("question")
                                    question_options = [
                                        opt.get("label", "")
                                        for opt in q.get("options", [])
                                    ]

                            tool_call = ToolCallData(
                                tool_name=tool_name,
                                timestamp=timestamp or self._now_utc,
                                session_id=session_id,
                                message_uuid=record.get("uuid"),
                                duration_ms=None,
                                total_duration_ms=None,
                                success=True,  # Default, updated by result
                                is_error=False,
                                is_interrupted=False,
                                file_path=tool_file_path,
                                tool_use_id=block.get("id"),
                                edit_old_string=edit_old_string,
                                edit_new_string=edit_new_string,
                                edit_replace_all=edit_replace_all,
                                web_url=web_url,
                                search_query=search_query,
                                question_header=question_header,
                                question_text=question_text,
                                question_options=question_options,
                            )
                            msg_tool_calls.append(tool_call)

            # Assemble text content from blocks
            text_content = None
            if isinstance(content, str):
                text_content = content
            elif text_parts:
                text_content = "\n".join(text_parts)
            if text_content and len(text_content) > 2000:
                text_content = text_content[:2000]

            # Extract tool result info (for duration, success status)
            tool_result = record.get("toolUseResult")
            if tool_result and isinstance(tool_result, dict):
                duration_ms = tool_result.get("durationMs")
                total_duration_ms = tool_result.get("totalDurationMs")
                is_error = tool_result.get("status") == "error"
                is_interrupted = tool_result.get("interrupted", False)

                # Update the last tool call with result info
                if msg_tool_calls:
                    last_tool = msg_tool_calls[-1]
                    last_tool.duration_ms = duration_ms
                    last_tool.total_duration_ms = total_duration_ms
                    last_tool.is_error = is_error
                    last_tool.is_interrupted = is_interrupted
                    last_tool.success = not is_error and not is_interrupted

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
                    content=text_content,
                    parent_uuid=parent_uuid,
                    stop_reason=stop_reason,
                    is_sidechain=is_sidechain,
                )
                messages_in_window.append(msg_data)

        # Only return session if it has messages in window
        if not session_in_window or not messages_in_window:
            return None, [], []

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

        return session, tool_calls_in_window, messages_in_window

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
                    message_count=day.get("messageCount", 0),
                    tool_call_count=day.get("toolCallCount", 0),
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
            model_count = len(session.models_used) or 1
            for i, model in enumerate(session.models_used):
                model_data[model]["message_count"] += (
                    session.message_count // model_count
                    + (1 if i < session.message_count % model_count else 0)
                )
                model_data[model]["input_tokens"] += (
                    session.total_input_tokens // model_count
                    + (1 if i < session.total_input_tokens % model_count else 0)
                )
                model_data[model]["output_tokens"] += (
                    session.total_output_tokens // model_count
                    + (1 if i < session.total_output_tokens % model_count else 0)
                )
                model_data[model]["cache_read_tokens"] += (
                    session.total_cache_read_tokens // model_count
                    + (1 if i < session.total_cache_read_tokens % model_count else 0)
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

    def _extract_config(self, data: ExtractedData30Day) -> None:
        """Extract customization counts from .claude/ directory."""
        from utils import get_claude_dir

        claude_dir = get_claude_dir()

        # Count custom agents
        agents_dir = claude_dir / "agents"
        if agents_dir.exists():
            data.custom_agents = len(list(agents_dir.glob("*.md")))

        # Count custom commands
        commands_dir = claude_dir / "commands"
        if commands_dir.exists():
            data.custom_commands = len(list(commands_dir.glob("*.md")))

        # Count custom skills
        skills_dir = claude_dir / "skills"
        if skills_dir.exists():
            # Count directories (each skill is a directory)
            data.custom_skills = len([
                d for d in skills_dir.iterdir() if d.is_dir()
            ])

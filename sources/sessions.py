"""Sessions source extractor."""

import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple

from database import MetricsDatabase
from utils import (
    get_claude_dir,
    read_jsonl_file,
    iter_jsonl_files_recursive,
    parse_iso_timestamp,
    dir_name_to_project_path,
    get_file_stats,
    safe_get,
)
from .base import BaseSource


class SessionsSource(BaseSource):
    """Extractor for ~/.claude/projects/*/*.jsonl session files.

    Contains complete conversation transcripts including:
    - All messages (user and assistant)
    - Tool calls and results
    - Thinking blocks
    - Token usage per message
    - File history snapshots
    """

    name = "sessions"
    description = "Complete conversation session transcripts"
    source_paths = ["~/.claude/projects/*/*.jsonl"]

    def __init__(
        self,
        include_sensitive: bool = False,
        include_full_content: bool = False,
        limit_sessions: Optional[int] = None,
        limit_messages_per_session: Optional[int] = None,
    ):
        """Initialize the sessions extractor.

        Args:
            include_sensitive: If True, include sensitive data
            include_full_content: If True, include full message content
            limit_sessions: Maximum sessions to extract (None = all)
            limit_messages_per_session: Max messages per session (None = all)
        """
        super().__init__(include_sensitive)
        self.include_full_content = include_full_content
        self.limit_sessions = limit_sessions
        self.limit_messages_per_session = limit_messages_per_session

    def _iter_session_files(self) -> Generator[Tuple[Path, str], None, None]:
        """Iterate over session files with project info.

        Yields:
            Tuple of (file_path, project_path)
        """
        projects_dir = get_claude_dir() / "projects"
        if not projects_dir.exists():
            return

        for project_dir in projects_dir.iterdir():
            if not project_dir.is_dir():
                continue

            project_path = dir_name_to_project_path(project_dir.name)

            for jsonl_file in project_dir.glob("*.jsonl"):
                if jsonl_file.is_file():
                    yield jsonl_file, project_path

    def _extract_session(
        self, file_path: Path, project_path: str
    ) -> Dict[str, Any]:
        """Extract data from a single session file."""
        session_id = file_path.stem
        is_agent = session_id.startswith("agent-")

        messages = []
        tool_calls = []
        models_used = set()
        total_input_tokens = 0
        total_output_tokens = 0
        total_cache_read = 0
        total_cost = 0.0
        user_count = 0
        assistant_count = 0
        first_timestamp = None
        last_timestamp = None

        msg_count = 0
        for record in read_jsonl_file(file_path):
            # Check message limit
            if self.limit_messages_per_session and msg_count >= self.limit_messages_per_session:
                break

            msg_type = record.get("type")

            # Skip file history snapshots for summary
            if msg_type == "file-history-snapshot":
                continue

            msg_count += 1

            # Extract timestamp
            timestamp = record.get("timestamp")
            if timestamp:
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
                            tool_call = {
                                "id": block.get("id"),
                                "tool_name": block.get("name"),
                                "message_uuid": record.get("uuid"),
                                "session_id": session_id,
                            }
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
                    msg_tool_calls[-1].update({
                        "duration_ms": duration_ms,
                        "total_duration_ms": total_duration_ms,
                        "is_error": is_error,
                        "is_interrupted": is_interrupted,
                        "file_path": file_path_result,
                    })

            tool_calls.extend(msg_tool_calls)

            # Create message summary
            msg_summary = {
                "uuid": record.get("uuid"),
                "parent_uuid": record.get("parentUuid"),
                "session_id": session_id,
                "timestamp": timestamp,
                "type": msg_type,
                "role": role,
                "model": model,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "cache_read_tokens": cache_read,
                "cost_usd": cost_usd,
                "has_thinking": has_thinking,
                "thinking_length": thinking_length,
                "tool_call_count": len(msg_tool_calls),
            }

            if self.include_full_content:
                msg_summary["content"] = content

            messages.append(msg_summary)

        # Calculate duration
        duration_ms = None
        if first_timestamp and last_timestamp:
            try:
                first_dt = parse_iso_timestamp(first_timestamp)
                last_dt = parse_iso_timestamp(last_timestamp)
                if first_dt and last_dt:
                    duration_ms = int((last_dt - first_dt).total_seconds() * 1000)
            except Exception:
                pass

        # Determine primary model
        primary_model = None
        if models_used:
            # Use most recent or most common model
            primary_model = sorted(models_used)[-1]

        file_stats = get_file_stats(file_path)

        return {
            "session_id": session_id,
            "project": project_path,
            "project_dir": file_path.parent.name,
            "file_path": str(file_path),
            "file_size": file_stats.get("size_bytes", 0),
            "is_agent": is_agent,
            "agent_id": session_id if is_agent else None,
            "start_time": first_timestamp,
            "end_time": last_timestamp,
            "duration_ms": duration_ms,
            "message_count": len(messages),
            "user_message_count": user_count,
            "assistant_message_count": assistant_count,
            "tool_call_count": len(tool_calls),
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "total_cache_read_tokens": total_cache_read,
            "models_used": sorted(models_used),
            "primary_model": primary_model,
            "cost_usd": total_cost,
            "messages": messages,
            "tool_calls": tool_calls,
        }

    def extract(self) -> Dict[str, Any]:
        """Extract session data.

        Returns:
            Dictionary containing:
            - total_files: Total session files found
            - extracted_sessions: Number of sessions extracted
            - sessions: List of session summaries
            - by_project: Sessions grouped by project
        """
        sessions = []
        by_project = defaultdict(list)
        total_files = 0

        for file_path, project_path in self._iter_session_files():
            total_files += 1

            if self.limit_sessions and len(sessions) >= self.limit_sessions:
                continue

            try:
                session = self._extract_session(file_path, project_path)
                sessions.append(session)
                by_project[project_path].append(session["session_id"])
            except Exception as e:
                sessions.append({
                    "session_id": file_path.stem,
                    "error": str(e),
                    "file_path": str(file_path),
                })

        # Calculate totals
        total_messages = sum(s.get("message_count", 0) for s in sessions if "error" not in s)
        total_tool_calls = sum(s.get("tool_call_count", 0) for s in sessions if "error" not in s)
        total_input_tokens = sum(s.get("total_input_tokens", 0) for s in sessions if "error" not in s)
        total_output_tokens = sum(s.get("total_output_tokens", 0) for s in sessions if "error" not in s)

        return {
            "total_files": total_files,
            "extracted_sessions": len(sessions),
            "total_messages": total_messages,
            "total_tool_calls": total_tool_calls,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "project_count": len(by_project),
            "sessions": sessions,
            "by_project": dict(by_project),
        }

    def to_sqlite(self, db: MetricsDatabase) -> None:
        """Write sessions to SQLite."""
        data = self.get_data()

        if "error" in data:
            return

        sessions = data.get("sessions", [])

        for session in sessions:
            if "error" in session:
                continue

            # Insert session
            db.insert_session(session)

            # Insert messages
            for msg in session.get("messages", []):
                db.insert_message(msg)

            # Insert tool calls
            for tool_call in session.get("tool_calls", []):
                db.insert_tool_call(tool_call)

        db.commit()

    def get_summary(self) -> Dict[str, Any]:
        """Get sessions summary."""
        data = self.get_data()

        if "error" in data:
            return {"source": self.name, "error": data["error"]}

        sessions = data.get("sessions", [])
        valid_sessions = [s for s in sessions if "error" not in s]

        # Get model distribution
        model_counts = defaultdict(int)
        for s in valid_sessions:
            for model in s.get("models_used", []):
                model_counts[model] += 1

        # Get agent vs regular session counts
        agent_count = sum(1 for s in valid_sessions if s.get("is_agent"))

        return {
            "source": self.name,
            "total_files": data.get("total_files", 0),
            "extracted_sessions": len(sessions),
            "valid_sessions": len(valid_sessions),
            "error_sessions": len(sessions) - len(valid_sessions),
            "agent_sessions": agent_count,
            "regular_sessions": len(valid_sessions) - agent_count,
            "total_messages": data.get("total_messages", 0),
            "total_tool_calls": data.get("total_tool_calls", 0),
            "total_input_tokens": data.get("total_input_tokens", 0),
            "total_output_tokens": data.get("total_output_tokens", 0),
            "project_count": data.get("project_count", 0),
            "model_distribution": dict(model_counts),
        }

    def to_json(self, path: Path, indent: int = 2) -> Path:
        """Write session data to JSON files.

        For sessions, we create an index file and individual session files
        to avoid creating one massive file.
        """
        from redaction import redact_dict

        data = self.get_data()

        # Apply redaction if needed
        if not self.include_sensitive:
            data = redact_dict(data, include_sensitive=False)

        path.parent.mkdir(parents=True, exist_ok=True)

        # Create sessions directory
        sessions_dir = path.parent / "sessions"
        sessions_dir.mkdir(exist_ok=True)

        # Write individual session files
        sessions = data.get("sessions", [])
        session_index = []

        for session in sessions:
            session_id = session.get("session_id", "unknown")
            session_file = sessions_dir / f"{session_id}.json"

            with open(session_file, "w", encoding="utf-8") as f:
                json.dump(session, f, indent=indent, ensure_ascii=False, default=str)

            # Create index entry (without messages/tool_calls)
            index_entry = {k: v for k, v in session.items()
                          if k not in ("messages", "tool_calls")}
            index_entry["file"] = str(session_file.name)
            session_index.append(index_entry)

        # Write index file
        index_data = {
            "source": self.name,
            "description": self.description,
            "extracted_at": self._extracted_at,
            "total_files": data.get("total_files", 0),
            "extracted_sessions": len(sessions),
            "sessions_dir": str(sessions_dir),
            "sessions": session_index,
            "by_project": data.get("by_project", {}),
        }

        with open(path, "w", encoding="utf-8") as f:
            json.dump(index_data, f, indent=indent, ensure_ascii=False, default=str)

        return path

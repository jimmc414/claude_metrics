"""Data classes for time-filtered extraction."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class MessageData:
    """Individual message record."""

    uuid: str
    session_id: str
    timestamp: datetime
    message_type: str  # "user", "assistant", etc.
    role: Optional[str]
    model: Optional[str]
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cost_usd: float
    has_thinking: bool
    thinking_length: int
    tool_call_count: int


@dataclass
class ToolCallData:
    """Individual tool call record."""

    tool_name: str
    timestamp: datetime
    session_id: str
    message_uuid: Optional[str]
    duration_ms: Optional[int]
    total_duration_ms: Optional[int]
    success: bool
    is_error: bool
    is_interrupted: bool
    file_path: Optional[str]  # For Read/Edit/Write tools


@dataclass
class SessionData:
    """Session with messages and tool calls."""

    session_id: str
    project_path: str
    start_time: datetime
    end_time: Optional[datetime]
    duration_ms: int
    message_count: int
    user_message_count: int
    assistant_message_count: int
    tool_call_count: int
    cost_usd: float
    model: Optional[str]  # Primary model
    models_used: List[str] = field(default_factory=list)
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    total_cache_read_tokens: int = 0
    is_agent: bool = False


@dataclass
class DailyActivity:
    """Daily activity aggregation."""

    date: str  # YYYY-MM-DD
    session_count: int
    message_count: int
    tool_call_count: int
    cost_usd: float
    input_tokens: int = 0
    output_tokens: int = 0
    active_hours: float = 0.0


@dataclass
class ModelUsageData:
    """Model usage statistics."""

    model: str
    message_count: int
    input_tokens: int
    output_tokens: int
    cache_read_tokens: int
    cost_usd: float


@dataclass
class ExtractedData30Day:
    """All raw data extracted for 30-day window."""

    window_start: datetime
    window_end: datetime
    window_days: int

    # Session data
    sessions: List[SessionData] = field(default_factory=list)

    # Message data
    messages: List[MessageData] = field(default_factory=list)

    # Aggregations
    daily_activity: List[DailyActivity] = field(default_factory=list)
    hourly_distribution: Dict[int, int] = field(
        default_factory=lambda: {h: 0 for h in range(24)}
    )

    # Tool data
    tool_calls: List[ToolCallData] = field(default_factory=list)
    tool_counts: Dict[str, int] = field(default_factory=dict)  # tool_name -> count

    # File data
    files_read: Dict[str, int] = field(default_factory=dict)  # path -> count
    files_edited: Dict[str, int] = field(default_factory=dict)  # path -> count
    files_written: Dict[str, int] = field(default_factory=dict)  # path -> count

    # Model/token data
    model_usage: Dict[str, ModelUsageData] = field(default_factory=dict)
    total_tokens: Dict[str, int] = field(
        default_factory=lambda: {"input": 0, "output": 0, "cache_read": 0}
    )

    # Totals
    total_sessions: int = 0
    total_messages: int = 0
    total_tool_calls: int = 0
    total_cost_usd: float = 0.0

    # Active days tracking
    active_dates: List[str] = field(default_factory=list)  # YYYY-MM-DD format

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "window_start": self.window_start.isoformat(),
            "window_end": self.window_end.isoformat(),
            "window_days": self.window_days,
            "total_sessions": self.total_sessions,
            "total_messages": self.total_messages,
            "total_tool_calls": self.total_tool_calls,
            "total_cost_usd": round(self.total_cost_usd, 4),
            "total_tokens": self.total_tokens,
            "session_count": len(self.sessions),
            "message_count": len(self.messages),
            "tool_call_count": len(self.tool_calls),
            "daily_activity_count": len(self.daily_activity),
            "active_dates_count": len(self.active_dates),
            "files_read_count": len(self.files_read),
            "files_edited_count": len(self.files_edited),
            "files_written_count": len(self.files_written),
            "model_count": len(self.model_usage),
            "hourly_distribution": self.hourly_distribution,
            "tool_counts": self.tool_counts,
        }

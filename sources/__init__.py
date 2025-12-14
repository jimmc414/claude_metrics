"""Source extractors for Claude Code data."""

from .base import BaseSource, CompositeSource

# Original 9 sources
from .stats_cache import StatsCacheSource
from .settings import SettingsSource
from .global_state import GlobalStateSource
from .credentials import CredentialsSource
from .history import HistorySource
from .sessions import SessionsSource
from .todos import TodosSource
from .plans import PlansSource
from .extensions import ExtensionsSource

# New 13 sources (10-22)
from .sqlite_store import SqliteStoreSource
from .debug_logs import DebugLogsSource
from .file_history import FileHistorySource
from .shell_snapshots import ShellSnapshotsSource
from .session_env import SessionEnvSource
from .versions import VersionsSource
from .project_config import ProjectConfigSource
from .claude_md import ClaudeMdSource
from .mcp_config import McpConfigSource
from .environment import EnvironmentSource
from .cache import CacheSource
from .mcp_logs import McpLogsSource
from .statusline import StatuslineSource

# All available sources (22 total)
ALL_SOURCES = {
    # Original 9 sources
    "stats_cache": StatsCacheSource,
    "settings": SettingsSource,
    "global_state": GlobalStateSource,
    "credentials": CredentialsSource,
    "history": HistorySource,
    "sessions": SessionsSource,
    "todos": TodosSource,
    "plans": PlansSource,
    "extensions": ExtensionsSource,
    # New 13 sources
    "sqlite_store": SqliteStoreSource,
    "debug_logs": DebugLogsSource,
    "file_history": FileHistorySource,
    "shell_snapshots": ShellSnapshotsSource,
    "session_env": SessionEnvSource,
    "versions": VersionsSource,
    "project_config": ProjectConfigSource,
    "claude_md": ClaudeMdSource,
    "mcp_config": McpConfigSource,
    "environment": EnvironmentSource,
    "cache": CacheSource,
    "mcp_logs": McpLogsSource,
    "statusline": StatuslineSource,
}

__all__ = [
    "BaseSource",
    "CompositeSource",
    # Original 9 sources
    "StatsCacheSource",
    "SettingsSource",
    "GlobalStateSource",
    "CredentialsSource",
    "HistorySource",
    "SessionsSource",
    "TodosSource",
    "PlansSource",
    "ExtensionsSource",
    # New 13 sources
    "SqliteStoreSource",
    "DebugLogsSource",
    "FileHistorySource",
    "ShellSnapshotsSource",
    "SessionEnvSource",
    "VersionsSource",
    "ProjectConfigSource",
    "ClaudeMdSource",
    "McpConfigSource",
    "EnvironmentSource",
    "CacheSource",
    "McpLogsSource",
    "StatuslineSource",
    # Registry
    "ALL_SOURCES",
]

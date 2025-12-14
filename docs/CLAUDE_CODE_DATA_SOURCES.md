# Claude Code Data Sources

A quick reference guide to all data that Claude Code stores locally.

---

## Directory Structure

```
~/.claude/                          # Main data directory
├── .credentials.json               # OAuth tokens & subscription
├── settings.json                   # Global settings
├── settings.local.json             # Local setting overrides
├── stats-cache.json                # Aggregated usage stats
├── history.jsonl                   # Command history
├── __store.db                      # SQLite message storage
├── projects/                       # Session transcripts
│   └── {project-hash}/
│       └── {session-id}.jsonl
├── todos/                          # Task lists
│   └── {session-id}.json
├── plans/                          # Implementation plans
│   └── {plan-name}.md
├── debug/                          # Debug/diagnostic logs
│   └── {session-id}.txt
├── file-history/                   # File version backups
│   └── {session-id}/
│       └── {hash}@v{n}
├── shell-snapshots/                # Shell environment snapshots
│   └── snapshot-*.sh
├── session-env/                    # Session environment data
│   └── {session-id}/
├── agents/                         # Custom agents
│   └── {agent-name}.md
├── commands/                       # Custom slash commands
│   └── {command-name}.md
├── skills/                         # Custom skills
│   └── {skill-name}/
│       └── SKILL.md
├── statsig/                        # Feature flag cache
└── plugins/                        # Plugin configs

~/.claude.json                      # Global state & feature flags
~/.config/claude/claude_code_config.json  # System config
~/.local/share/claude/versions/     # Installed Claude Code binaries
~/.cache/claude/                    # Cache & staging directory
~/.cache/claude-cli-nodejs/         # MCP server logs
    └── {project}/mcp-logs-{server}/

<project>/.claude/                  # Project-level configuration
<project>/CLAUDE.md                 # Project instructions
<project>/.mcp.json                 # MCP server configuration
```

---

## Data Sources Overview

| # | Source | Primary Path | Description |
|---|--------|--------------|-------------|
| 1 | [Stats Cache](#1-stats-cache) | `~/.claude/stats-cache.json` | Aggregated usage statistics |
| 2 | [Settings](#2-settings) | `~/.claude/settings.json` | User preferences & permissions |
| 3 | [Global State](#3-global-state) | `~/.claude.json` | App state, feature flags, project configs |
| 4 | [Credentials](#4-credentials) | `~/.claude/.credentials.json` | OAuth tokens & subscription info |
| 5 | [History](#5-history) | `~/.claude/history.jsonl` | Command/input history |
| 6 | [Sessions](#6-sessions) | `~/.claude/projects/*/*.jsonl` | Conversation transcripts |
| 7 | [Todos](#7-todos) | `~/.claude/todos/*.json` | Task lists per session |
| 8 | [Plans](#8-plans) | `~/.claude/plans/*.md` | Implementation plan documents |
| 9 | [Extensions](#9-extensions) | `~/.claude/{agents,commands,skills,plugins,statsig}/` | Custom agents, commands, skills, plugins, feature flags |
| 10 | [SQLite Store](#10-sqlite-store) | `~/.claude/__store.db` | Structured message database |
| 11 | [Debug Logs](#11-debug-logs) | `~/.claude/debug/*.txt` | Session diagnostic logs |
| 12 | [File History](#12-file-history) | `~/.claude/file-history/` | File version backups |
| 13 | [Shell Snapshots](#13-shell-snapshots) | `~/.claude/shell-snapshots/` | Shell environment captures |
| 14 | [Session Env](#14-session-environment) | `~/.claude/session-env/` | Session environment data |
| 15 | [Versions](#15-versions) | `~/.local/share/claude/versions/` | Installed Claude Code binaries |
| 16 | [Project Config](#16-project-configuration) | `<project>/.claude/` | Project-level settings |
| 17 | [CLAUDE.md](#17-claudemd) | `<project>/CLAUDE.md` | Project instructions |
| 18 | [MCP Config](#18-mcp-configuration) | `<project>/.mcp.json` | MCP server configuration |
| 19 | [Environment](#19-environment-variables) | Process environment | Runtime variables |
| 20 | [Cache](#20-cache-directory) | `~/.cache/claude/` | Staging/cache data |
| 21 | [MCP Logs](#21-mcp-server-logs) | `~/.cache/claude-cli-nodejs/` | MCP server logs |
| 22 | [Statusline](#22-statusline-data) | Runtime stdin | Real-time session data |

---

## 1. Stats Cache

**Path:** `~/.claude/stats-cache.json`

Pre-computed aggregate statistics updated after each session.

### Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `totalSessions` | number | All-time session count |
| `totalMessages` | number | All-time message count |
| `totalToolUses` | number | All-time tool call count |
| `totalCost` | number | Cumulative API cost (USD) |
| `firstSessionDate` | string | ISO timestamp of first session |
| `lastComputedDate` | string | When stats were last updated |

### Nested Structures

**`dailyActivity[]`** - Activity per day:
```json
{
  "date": "2024-11-15",
  "sessionCount": 5,
  "messageCount": 142,
  "toolUseCount": 87,
  "cost": 0.45
}
```

**`modelUsage{}`** - Stats per model:
```json
{
  "claude-sonnet-4-20250514": {
    "inputTokens": 1250000,
    "outputTokens": 450000,
    "cacheReadInputTokens": 800000,
    "cost": 12.50
  }
}
```

**`hourCounts[]`** - Activity by hour (0-23):
```json
[0, 0, 0, 5, 12, 45, 89, 120, ...]
```

---

## 2. Settings

**Paths:**
- `~/.claude/settings.json` (global)
- `~/.claude/settings.local.json` (local overrides)
- `~/.config/claude/claude_code_config.json` (system)

User preferences and tool permissions.

### Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `model` | string | Default model (e.g., `claude-sonnet-4-20250514`) |
| `alwaysThinkingEnabled` | boolean | Extended thinking mode |
| `gitAttribution` | boolean | Add git co-author attribution |

### Permissions Structure

```json
{
  "permissions": {
    "defaultMode": "allowEdits",
    "allow": ["Read", "Grep", "Glob", "Bash(git:*)"],
    "deny": ["Write(/etc/*)", "Bash(rm -rf:*)"]
  }
}
```

---

## 3. Global State

**Path:** `~/.claude.json`

Application-wide state, feature flags, and per-project configurations.

### Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `numStartups` | number | Total app startup count |
| `hasCompletedOnboarding` | boolean | Onboarding completion status |
| `promptQueueUseCount` | number | Prompt queue feature uses |
| `tipsHistory` | object | Feature tip show counts |
| `cachedStatsigGates` | object | Feature flag states |

### Per-Project Data (`projects{}`)

Each project path maps to:
```json
{
  "/path/to/project": {
    "allowedTools": ["Bash", "Read", "Edit"],
    "hasTrustDialogAccepted": true,
    "mcpServers": { ... },
    "lastSessionId": "abc123",
    "lastCost": 0.25,
    "lastLinesAdded": 150,
    "lastLinesRemoved": 45,
    "lastTotalInputTokens": 50000,
    "lastTotalOutputTokens": 12000
  }
}
```

---

## 4. Credentials

**Path:** `~/.claude/.credentials.json`

OAuth authentication and subscription information. **Sensitive data - redacted by default.**

### Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `subscriptionType` | string | `"max"`, `"pro"`, or `"free"` |
| `rateLimitTier` | string | Rate limit tier name |
| `scopes` | array | Granted OAuth scopes |
| `expiresAt` | number | Token expiration timestamp |
| `accessToken` | string | OAuth access token (redacted) |
| `refreshToken` | string | OAuth refresh token (redacted) |

---

## 5. History

**Path:** `~/.claude/history.jsonl`

Readline-style history of user inputs across all sessions.

### Record Format

```json
{
  "timestamp": 1699999999999,
  "project": "/path/to/project",
  "display": "fix the bug in auth.py",
  "pastedContents": null
}
```

| Field | Type | Description |
|-------|------|-------------|
| `timestamp` | number | Unix timestamp (milliseconds) |
| `project` | string | Project path where input occurred |
| `display` | string | The actual user input text |
| `pastedContents` | string? | Content if pasted (vs typed) |

---

## 6. Sessions

**Path:** `~/.claude/projects/{project-hash}/{session-id}.jsonl`

Complete conversation transcripts including all messages, tool calls, and metadata.

### Message Record Types

**User Message:**
```json
{
  "uuid": "msg-001",
  "parentUuid": null,
  "type": "user",
  "timestamp": "2024-11-15T10:30:00.000Z",
  "message": {
    "role": "user",
    "content": "Fix the login bug"
  }
}
```

**Assistant Message:**
```json
{
  "uuid": "msg-002",
  "parentUuid": "msg-001",
  "type": "assistant",
  "timestamp": "2024-11-15T10:30:05.000Z",
  "message": {
    "role": "assistant",
    "model": "claude-sonnet-4-20250514",
    "content": [
      {
        "type": "thinking",
        "thinking": "Let me analyze the auth code..."
      },
      {
        "type": "text",
        "text": "I'll fix that bug."
      },
      {
        "type": "tool_use",
        "id": "tool-001",
        "name": "Read",
        "input": { "file_path": "/src/auth.py" }
      }
    ],
    "usage": {
      "input_tokens": 1500,
      "output_tokens": 450,
      "cache_read_input_tokens": 1200
    }
  },
  "costUSD": 0.015
}
```

### Key Message Fields

| Field | Type | Description |
|-------|------|-------------|
| `uuid` | string | Unique message identifier |
| `parentUuid` | string? | Parent message (conversation tree) |
| `type` | string | `"user"`, `"assistant"`, `"file-history-snapshot"` |
| `timestamp` | string | ISO 8601 timestamp |
| `message.model` | string | Model used (assistant only) |
| `message.content` | array | Content blocks (text, tool_use, thinking) |
| `message.usage` | object | Token counts |
| `costUSD` | number | Cost for this message |

### Tool Result Record

```json
{
  "uuid": "result-001",
  "type": "assistant",
  "toolUseResult": {
    "toolUseId": "tool-001",
    "status": "success",
    "durationMs": 45,
    "filePath": "/src/auth.py"
  }
}
```

---

## 7. Todos

**Path:** `~/.claude/todos/{session-id}.json`

Task lists created during sessions.

### Format

```json
[
  {
    "id": "todo-001",
    "content": "Fix authentication bug",
    "activeForm": "Fixing authentication bug",
    "status": "completed",
    "priority": null
  },
  {
    "id": "todo-002",
    "content": "Add unit tests",
    "activeForm": "Adding unit tests",
    "status": "in_progress",
    "priority": 1
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique todo identifier |
| `content` | string | Task description (imperative) |
| `activeForm` | string | Present tense version |
| `status` | string | `"pending"`, `"in_progress"`, `"completed"` |
| `priority` | number? | Optional priority level |

---

## 8. Plans

**Path:** `~/.claude/plans/{plan-name}.md`

Implementation plan documents created during plan mode.

### Structure

Plans are markdown files with typical structure:
- Title (H1)
- Objective/Summary
- Implementation steps
- Checklists (`- [ ]` / `- [x]`)
- Code blocks

### Extracted Metadata

| Field | Description |
|-------|-------------|
| `title` | First H1 heading |
| `line_count` | Total lines |
| `code_block_count` | Number of code blocks |
| `checklist_total` | Total checklist items |
| `checklist_checked` | Completed checklist items |

---

## 9. Extensions

Custom agents, commands, skills, plugins, and feature flag cache.

### Agents
**Path:** `~/.claude/agents/{name}.md`

Custom agent definitions with specialized behaviors.

### Commands
**Path:** `~/.claude/commands/{name}.md`

Custom slash commands (e.g., `/commit`, `/review`).

### Skills
**Path:** `~/.claude/skills/{name}/SKILL.md`

Skills with optional supporting files:
- `CHEATSHEET.md` - Quick reference
- `reference.md` - Detailed reference
- `configs/` - Configuration files
- `scripts/` - Helper scripts

### Plugins
**Path:** `~/.claude/plugins/`

Plugin configurations and marketplace information:
- `installed_plugins.json` - Installed plugin registry
- `known_marketplaces.json` - Known plugin marketplaces
- `config.json` - Plugin configuration

### Statsig (Feature Flags)
**Path:** `~/.claude/statsig/`

Cached feature flag data from Statsig service. Contains cache files for feature gate evaluations.

### Extracted Fields

| Field | Type | Description |
|-------|------|-------------|
| `type` | string | `"agent"`, `"command"`, `"skill"` |
| `name` | string | Extension name (from H1) |
| `description` | string | First non-header line |
| `triggers` | array | Trigger keywords (skills) |
| `file_path` | string | Full file path |
| `line_count` | number | File line count |
| `plugins.installed_plugins` | object | Installed plugins registry |
| `plugins.known_marketplaces` | object | Known marketplaces |
| `statsig.cache_file_count` | number | Number of cache files |

---

## 10. SQLite Store

**Path:** `~/.claude/__store.db`

Structured message storage in SQLite format.

### Tables

| Table | Purpose |
|-------|---------|
| `base_messages` | Core message metadata (uuid, session_id, timestamp, type) |
| `user_messages` | User message content and tool results |
| `assistant_messages` | Assistant responses with cost, model, duration |
| `conversation_summaries` | Conversation summary text per leaf message |

### Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `uuid` | TEXT | Message UUID (primary key) |
| `session_id` | TEXT | Session reference |
| `timestamp` | INTEGER | Unix ms timestamp |
| `cost_usd` | REAL | Message cost |
| `model` | TEXT | Model used |
| `duration_ms` | INTEGER | Response time |

---

## 11. Debug Logs

**Path:** `~/.claude/debug/{session-id}.txt`

Timestamped diagnostic logs per session.

### Format

```
YYYY-MM-DDTHH:MM:SS.mmmZ [LEVEL] Message
```

### Log Levels

| Level | Description |
|-------|-------------|
| `[DEBUG]` | Detailed diagnostics |
| `[ERROR]` | Error conditions |
| `[WARN]` | Warnings |

### Key Log Events

- Settings file watching
- LSP server initialization
- Plugin/skill loading
- Permission updates
- Slow operation detection

---

## 12. File History

**Path:** `~/.claude/file-history/{session-id}/{hash}@v{version}`

File backup/versioning system that preserves file states before edits.

### Filename Format

- `{hash}` - 16-character hex hash of file path
- `{version}` - Sequential version number (1, 2, 3...)

Example: `d801d63c5ca66400@v3`

### Content

Raw file content at that version, preserving original permissions.

---

## 13. Shell Snapshots

**Path:** `~/.claude/shell-snapshots/snapshot-{shell}-{timestamp}-{random}.sh`

Shell environment captures for session restoration.

### Contents

- Base64-encoded shell aliases
- Base64-encoded shell functions
- Shell options (shopt settings)
- Environment reconstruction script

---

## 14. Session Environment

**Path:** `~/.claude/session-env/{session-id}/`

Per-session environment data. Often empty or minimal.

---

## 15. Versions

**Path:** `~/.local/share/claude/versions/{version}`

Installed Claude Code binary versions.

### Details

| Field | Value |
|-------|-------|
| Size | ~200MB per version |
| Format | Executable binary |
| Naming | Semantic version (e.g., `2.0.69`) |

---

## 16. Project Configuration

**Path:** `<project>/.claude/`

Project-specific customizations that override global settings.

### Structure

```
.claude/
├── settings.local.json     # Permission overrides
├── agents/                 # Project-specific agents
│   └── {name}.md
├── commands/               # Project-specific slash commands
│   └── {name}.md
└── skills/                 # Project-specific skills
    └── {name}/
        └── SKILL.md
```

### settings.local.json

```json
{
  "permissions": {
    "allow": ["Bash(npm:*)"],
    "deny": ["Write(/etc/*)"]
  }
}
```

---

## 17. CLAUDE.md

**Path:** `<project>/CLAUDE.md`

Project instructions read by Claude at session start.

### Typical Content

- Coding standards and style guidelines
- Commit message conventions
- Project-specific context
- External includes (with approval required)

---

## 18. MCP Configuration

**Path:** `<project>/.mcp.json` or `<project>/mcp.json`

Model Context Protocol server configuration.

### Schema

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "server-package"],
      "cwd": "/path/to/cwd",
      "env": {
        "API_KEY": "..."
      }
    }
  }
}
```

---

## 19. Environment Variables

Runtime configuration via process environment.

| Variable | Description |
|----------|-------------|
| `CLAUDECODE` | `"1"` when running in Claude Code |
| `CLAUDE_CODE_ENTRYPOINT` | Entry point (e.g., `"cli"`) |
| `ANTHROPIC_API_KEY` | API key if custom key is set |
| `CLAUDE_PROJECT_DIR` | Current project directory |

---

## 20. Cache Directory

**Path:** `~/.cache/claude/`

General cache and staging area.

### Contents

- `staging/` - Temporary staging files for operations

---

## 21. MCP Server Logs

**Path:** `~/.cache/claude-cli-nodejs/{project}/mcp-logs-{server}/`

Per-server log files with timestamps.

### Filename Format

`YYYY-MM-DDTHH-MM-SS-mmmZ.txt`

### Content

- Server startup/shutdown events
- MCP protocol messages
- Error traces
- Request/response logs

---

## 22. Statusline Data

**Source:** Runtime stdin to statusline command

Real-time session data passed to custom statusline scripts.

### Schema

```json
{
  "model": {
    "display_name": "claude-opus-4-5"
  },
  "workspace": {
    "current_dir": "/path/to/current",
    "project_dir": "/path/to/project"
  },
  "version": "2.0.69",
  "cost": {
    "total_cost_usd": 0.15,
    "total_lines_added": 150,
    "total_lines_removed": 45
  },
  "exceeds_200k_tokens": false
}
```

---

## Quick Reference: File Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| JSON | `.json` | Single object/array |
| JSONL | `.jsonl` | Newline-delimited JSON records |
| Markdown | `.md` | Markdown documents |

---

## Data Sensitivity

| Source | Sensitivity | Notes |
|--------|-------------|-------|
| Credentials | **HIGH** | OAuth tokens redacted by default |
| Sessions | Medium | May contain code/prompts |
| History | Medium | User inputs |
| SQLite Store | Medium | Contains message content |
| Debug Logs | Medium | May contain file paths/errors |
| File History | Medium | Contains file contents |
| CLAUDE.md | Medium | Project-specific instructions |
| MCP Config | Medium | May contain API keys in env |
| Environment Vars | Medium | May contain API keys |
| Settings | Low | Preferences only |
| Stats Cache | Low | Aggregate numbers |
| Todos/Plans | Low | Task metadata |
| Extensions | Low | User-defined content |
| Shell Snapshots | Low | Shell environment |
| Session Env | Low | Minimal data |
| Versions | Low | Binary files |
| Project Config | Low | Permission overrides |
| Cache | Low | Temporary files |
| MCP Logs | Low | Server logs |
| Statusline | Low | Runtime data |

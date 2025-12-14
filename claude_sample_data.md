# Claude Code Sample Data

Generated: 2025-12-14T00:47:50.675891

This document contains sample data (up to 10 records) extracted from each of the 22 Claude Code data sources.

---

## Table of Contents

1. [Stats Cache](#1-stats-cache)
2. [Settings](#2-settings)
3. [Global State](#3-global-state)
4. [Credentials](#4-credentials)
5. [History](#5-history)
6. [Sessions](#6-sessions)
7. [Todos](#7-todos)
8. [Plans](#8-plans)
9. [Extensions](#9-extensions)
10. [Sqlite Store](#10-sqlite-store)
11. [Debug Logs](#11-debug-logs)
12. [File History](#12-file-history)
13. [Shell Snapshots](#13-shell-snapshots)
14. [Session Env](#14-session-env)
15. [Versions](#15-versions)
16. [Project Config](#16-project-config)
17. [Claude Md](#17-claude-md)
18. [Mcp Config](#18-mcp-config)
19. [Environment](#19-environment)
20. [Cache](#20-cache)
21. [Mcp Logs](#21-mcp-logs)
22. [Statusline](#22-statusline)

---

## 1. Stats Cache

**Path:** `~/.claude/stats-cache.json`

**Description:** Pre-computed aggregate statistics updated after each session

### Sample Data

```json
{
  "version": 1,
  "lastComputedDate": "2025-12-13",
  "dailyActivity": [
    {
      "date": "2025-11-06",
      "messageCount": 3335,
      "sessionCount": 1,
      "toolCallCount": 968
    },
    {
      "date": "2025-11-07",
      "messageCount": 6113,
      "sessionCount": 1,
      "toolCallCount": 1684
    },
    {
      "date": "2025-11-12",
      "messageCount": 2619,
      "sessionCount": 4,
      "toolCallCount": 751
    },
    {
      "date": "2025-11-13",
      "messageCount": 2060,
      "sessionCount": 3,
      "toolCallCount": 558
    },
    {
      "date": "2025-11-14",
      "messageCount": 1585,
      "sessionCount": 1,
      "toolCallCount": 432
    },
    {
      "date": "2025-11-15",
      "messageCount": 149,
      "sessionCount": 1,
      "toolCallCount": 46
    },
    {
      "date": "2025-11-17",
      "messageCount": 3316,
      "sessionCount": 4,
      "toolCallCount": 899
    },
    {
      "date": "2025-11-18",
      "messageCount": 8,
      "sessionCount": 4,
      "toolCallCount": 0
    },
    {
      "date": "2025-11-19",
      "messageCount": 3662,
      "sessionCount": 9,
      "toolCallCount": 1191
    },
    {
      "date": "2025-11-20",
      "messageCount": 2211,
      "sessionCount": 3,
      "toolCallCount": 642
    }
  ],
  "_dailyActivity_total": 31,
  "dailyModelTokens": [
    {
      "date": "2025-11-06",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 1639388
      }
    },
    {
      "date": "2025-11-07",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 4931183
      }
    },
    {
      "date": "2025-11-12",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 1667056
      }
    },
    {
      "date": "2025-11-13",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 1452550
      }
    },
    {
      "date": "2025-11-14",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 1543473
      }
    },
    {
      "date": "2025-11-15",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 55626
      }
    },
    {
      "date": "2025-11-17",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 1661941
      }
    },
    {
      "date": "2025-11-19",
      "tokensByModel": {
        "claude-opus-4-1-20250805": 664811,
        "claude-sonnet-4-5-20250929": 359089
      }
    },
    {
      "date": "2025-11-20",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 1031353
      }
    },
    {
      "date": "2025-11-22",
      "tokensByModel": {
        "claude-sonnet-4-5-20250929": 120556
      }
    }
  ],
  "_dailyModelTokens_total": 29,
  "modelUsage": {
    "claude-opus-4-5-20251101": {
      "inputTokens": 1353803,
      "outputTokens": 4773480,
      "cacheReadInputTokens": 2189448130,
      "cacheCreationInputTokens": 140454086,
      "webSearchRequests": 0,
      "costUSD": 0,
      "contextWindow": 0
    },
    "claude-sonnet-4-5-20250929": {
      "inputTokens": 559420,
      "outputTokens": 14510976,
      "cacheReadInputTokens": 1521656159,
      "cacheCreationInputTokens": 180386810,
      "webSearchRequests": 0,
      "costUSD": 0,
      "contextWindow": 0
    },
    "claude-opus-4-1-20250805": {
      "inputTokens": 12923,
      "outputTokens": 651888,
      "cacheReadInputTokens": 124635648,
      "cacheCreationInputTokens": 9501828,
      "webSearchRequests": 0,
      "costUSD": 0,
      "contextWindow": 0
    }
  },
  "totalSessions": 1517,
  "totalMessages": 68868,
  "longestSession": {
    "sessionId": "b8421125-9602-4f2c-969e-cb47e6e47599",
    "duration": 510062881,
    "messageCount": 6113,
    "timestamp": "2025-11-07T05:12:31.430Z"
  },
  "firstSessionDate": "2025-11-06T20:18:40.075Z",
  "hourCounts": {
    "0": 61,
    "1": 55,
    "2": 32,
    "4": 1,
    "8": 1,
    "10": 55,
    "11": 81,
    "12": 44,
    "13": 168,
    "14": 177,
    "15": 114,
    "16": 6,
    "17": 4,
    "18": 10,
    "19": 10,
    "20": 3,
    "21": 278,
    "22": 115,
    "23": 302
  }
}
```

---

## 2. Settings

**Path:** `~/.claude/settings.json`, `settings.local.json`

**Description:** User preferences and tool permissions

### Sample Data

```json
{
  "global_settings": {
    "env": {
      "MAX_THINKING_TOKENS": "63999"
    },
    "includeCoAuthoredBy": false,
    "permissions": {
      "allow": [
        "WebFetch(domain:github.com)",
        "Bash(python3:*)",
        "Bash(tree:*)",
        "Bash(git log:*)",
        "Bash(python:*)",
        "WebSearch",
        "Bash(find:*)",
        "Bash(pytest:*)",
        "Bash(test:*)",
        "Bash(pip show:*)"
      ],
      "_allow_total": 40,
      "deny": [],
      "ask": [],
      "defaultMode": "default"
    },
    "model": "opus",
    "statusLine": {
      "type": "command",
      "command": "bash /home/jim/.claude/statusline-command.sh"
    },
    "alwaysThinkingEnabled": true,
    "gitAttribution": false,
    "hooks": {}
  },
  "global_settings_path": "/home/jim/.claude/settings.json",
  "global_settings_exists": true,
  "local_settings": {
    "enableAllProjectMcpServers": false
  },
  "local_settings_path": "/home/jim/.claude/settings.local.json",
  "local_settings_exists": true,
  "system_config": {
    "mcpServers": {
      "playwright": {
        "command": "npx",
        "args": [
          "-y",
          "@playwright/mcp"
        ]
      }
    }
  },
  "system_config_path": "/home/jim/.config/claude/claude_code_config.json",
  "system_config_exists": true
}
```

---

## 3. Global State

**Path:** `~/.claude.json`

**Description:** Application-wide state, feature flags, and per-project configurations

### Sample Data

```json
{
  "path": "/home/jim/.claude.json",
  "raw": {
    "numStartups": 293,
    "installMethod": "native",
    "autoUpdates": false,
    "verbose": true,
    "autoCompactEnabled": false,
    "hasSeenTasksHint": true,
    "hasSeenStashHint": true,
    "customApiKeyResponses": {
      "approved": [],
      "rejected": [
        "99999999999999999999",
        "not-used",
        "00000000000000000000",
        "m4UQ2kCsH6g-p7qBiQAA"
      ]
    },
    "tipsHistory": {
      "new-user-warmup": 1,
      "plan-mode-for-complex-tasks": 67,
      "terminal-setup": 284,
      "theme-command": 283,
      "status-line": 146,
      "prompt-queue": 29,
      "enter-to-steer-in-relatime": 283,
      "todo-list": 274,
      "# for memory": 284,
      "install-github-app": 13,
      "permissions": 287,
      "drag-and-drop-images": 287,
      "double-esc": 35,
      "continue": 287,
      "custom-commands": 289,
      "shift-tab": 287,
      "image-paste": 286,
      "custom-agents": 289,
      "double-esc-code-restore": 287,
      "git-worktrees": 289,
      "tab-toggle-thinking": 286,
      "ultrathink-keyword": 287,
      "stickers-command": 277,
      "default-permission-mode-config": 184,
      "rename-conversation": 279,
      "colorterm-truecolor": 292,
      "config-thinking-mode": 292,
      "frontend-design-plugin": 271
    },
    "memoryUsageCount": 1,
    "promptQueueUseCount": 202,
    "cachedStatsigGates": {
      "tengu_disable_bypass_permissions_mode": false,
      "tengu_use_file_checkpoints": true,
      "tengu_tool_pear": false,
      "tengu_migrate_ignore_patterns": false,
      "tengu_halloween": false,
      "tengu_glob_with_rg": false,
      "tengu_web_tasks": true,
      "tengu_log_1p_events": true,
      "tengu_enable_versioned_plugins": false,
      "code_slack_app_install_banner": false,
      "tengu_sumi": false,
      "tengu_react_vulnerability_warning": false,
      "tengu_tool_result_persistence": false,
      "tengu_c4w_usage_limit_notifications_enabled": false,
      "tengu_thinkback": false
    },
    "cachedDynamicConfigs": {
      "tengu-top-of-feed-tip": {
        "tip": "",
        "color": ""
      }
    },
    "cachedGrowthBookFeatures": {
      "tengu_pid_based_version_locking": false
    },
    "userID": "aff334d39ed37df08898ab123b72f7f0108feaee73c58ce0c0ce6621a4fd4733",
    "statsigModel": {
      "bedrock": "us.anthropic.claude-3-7-sonnet-20250219-v1:0",
      "vertex": "claude-3-7-sonnet@20250219",
      "firstParty": "claude-3-7-sonnet-20250219"
    },
    "hasCompletedOnboarding": true,
    "lastOnboardingVersion": "2.0.67",
    "projects": {
      "/home/jim/code_install": {
        "allowedTools": [],
        "dontCrawlDirectory": false,
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "enableAllProjectMcpServers": false,
        "hasTrustDialogAccepted": true,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 1,
        "lastCost": 0.7597266999999999,
        "lastAPIDuration": 196143,
        "lastDuration": 1272446,
        "lastLinesAdded": 123,
        "lastLinesRemoved": 53,
        "lastSessionId": "01505466-39cc-4f61-b2b2-cc83419a41b9"
      },
      "/home/jim/code_install/onefilellm": {
        "allowedTools": [],
        "dontCrawlDirectory": false,
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "enableAllProjectMcpServers": false,
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 2,
        "exampleFiles": [
          "onefilellm.py",
          "test_onefilellm.py",
          "onefilerepo.py",
          "README.md",
          "requirements.txt"
        ],
        "exampleFilesGeneratedAt": 1746332265417,
        "lastCost": 0.3129548,
        "lastAPIDuration": 98344,
        "lastDuration": 68728956,
        "lastLinesAdded": 21,
        "lastLinesRemoved": 1,
        "lastSessionId": "56e45cd3-7fc5-41aa-b14c-74a3df2a9a4a"
      },
      "/home/jim": {
        "allowedTools": [],
        "dontCrawlDirectory": true,
        "mcpContextUris": [],
        "mcpServers": {},
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 2,
        "lastCost": 0.31100314999999995,
        "lastAPIDuration": 9950,
        "lastToolDuration": 0,
        "lastDuration": 54129972,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 131,
        "lastTotalOutputTokens": 261,
        "lastTotalCacheCreationInputTokens": 15641,
        "lastTotalCacheReadInputTokens": 0,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "cd47fb6d-a2a3-49e3-ba7e-0f9df20acbd2"
      },
      "/mnt/c/python/mcp_start": {
        "allowedTools": [],
        "dontCrawlDirectory": false,
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "enableAllProjectMcpServers": false,
        "hasTrustDialogAccepted": true,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 1,
        "hasCompletedProjectOnboarding": true,
        "lastCost": 0.29963755000000003,
        "lastAPIDuration": 70080,
        "lastDuration": 18803684,
        "lastLinesAdded": 20,
        "lastLinesRemoved": 0,
        "lastSessionId": "df9a3171-5b2a-4930-8ec6-659d15993f08"
      },
      "/mnt/c/python/jack": {
        "allowedTools": [],
        "dontCrawlDirectory": false,
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "enableAllProjectMcpServers": false,
        "hasTrustDialogAccepted": true,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 1,
        "lastCost": 3.7580959999999983,
        "lastAPIDuration": 1713205,
        "lastDuration": 6622889,
        "lastLinesAdded": 3731,
        "lastLinesRemoved": 230,
        "lastSessionId": "451b2810-9539-4dcc-be53-291f90110a59"
      },
      "/mnt/c/python/jack_page": {
        "allowedTools": [],
        "dontCrawlDirectory": false,
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "enableAllProjectMcpServers": false,
        "hasTrustDialogAccepted": true,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 1,
        "hasCompletedProjectOnboarding": true
      },
      "/mnt/c/python/onefilellm": {
        "allowedTools": [],
        "dontCrawlDirectory": false,
        "mcpContextUris": [],
        "mcpServers": {},
        "hasTrustDialogAccepted": true,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 2,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "onefilellm.py",
          "test_all.py",
          "utils.py",
          "cli.py",
          "onefilerepo.py"
        ],
        "exampleFilesGeneratedAt": 1765312123918,
        "hasCompletedProjectOnboarding": true,
        "lastTotalWebSearchRequests": 0,
        "lastCost": 0.26258205000000007,
        "lastAPIDuration": 73107,
        "lastToolDuration": 57078,
        "lastDuration": 77089767,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 15524,
        "lastTotalOutputTokens": 4807,
        "lastTotalCacheCreationInputTokens": 54141,
        "lastTotalCacheReadInputTokens": 230492,
        "lastSessionId": "7a951406-d7d1-4572-92bc-5b443aeca741"
      },
      "/mnt/c/python": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": true,
        "projectOnboardingSeenCount": 4,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0,
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 2.6845739500000017,
        "lastAPIDuration": 531123,
        "lastAPIDurationWithoutRetries": 528240,
        "lastToolDuration": 248242,
        "lastDuration": 25372118,
        "lastLinesAdded": 2150,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 32849,
        "lastTotalOutputTokens": 42127,
        "lastTotalCacheCreationInputTokens": 406993,
        "lastTotalCacheReadInputTokens": 784063,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 31808,
            "outputTokens": 19095,
            "cacheReadInputTokens": 249267,
            "cacheCreationInputTokens": 171949,
            "webSearchRequests": 0,
            "costUSD": 0.36714595000000005
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 1041,
            "outputTokens": 23032,
            "cacheReadInputTokens": 534796,
            "cacheCreationInputTokens": 235044,
            "webSearchRequests": 0,
            "costUSD": 2.317428
          }
        },
        "lastSessionId": "335f8a35-9a1c-42f3-858a-5eb62a0748be"
      },
      "/mnt/c/python/claude_codex_collab": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 4,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0,
        "lastCost": 22.113691599999996,
        "lastAPIDuration": 1442516,
        "lastToolDuration": 8449,
        "lastDuration": 60262092,
        "lastLinesAdded": 3574,
        "lastLinesRemoved": 77,
        "lastTotalInputTokens": 46930,
        "lastTotalOutputTokens": 59073,
        "lastTotalCacheCreationInputTokens": 362080,
        "lastTotalCacheReadInputTokens": 7361104,
        "lastSessionId": "b35c9d60-7b0f-41aa-a3fa-53d95bf95eaa"
      },
      "/mnt/c/python/temp": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 4,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0,
        "lastCost": 0.0009376,
        "lastAPIDuration": 2001,
        "lastToolDuration": 0,
        "lastDuration": 105957872,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 1067,
        "lastTotalOutputTokens": 21,
        "lastTotalCacheCreationInputTokens": 0,
        "lastTotalCacheReadInputTokens": 0,
        "lastSessionId": "3fd04f1b-3aef-4a9f-9c48-a853fe5433bb"
      },
      "/mnt/c/python/claude_control": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 7,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "core.py",
          "claude_helpers.py",
          "test_core.py",
          "test_helpers.py",
          "cli.py"
        ],
        "exampleFilesGeneratedAt": 1758745940651,
        "lastTotalWebSearchRequests": 0,
        "lastCost": 91.02183265000014,
        "lastAPIDuration": 4327638,
        "lastToolDuration": 65474,
        "lastDuration": 9953236,
        "lastLinesAdded": 3686,
        "lastLinesRemoved": 500,
        "lastTotalInputTokens": 56585,
        "lastTotalOutputTokens": 178286,
        "lastTotalCacheCreationInputTokens": 1348185,
        "lastTotalCacheReadInputTokens": 34972783,
        "lastSessionId": "319c8ef3-904d-4af0-92d4-6dcf79760d42"
      },
      "/mnt/c/python/Generic_Reg_F_Import": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastCost": 0.68690025,
        "lastAPIDuration": 70345,
        "lastToolDuration": 8019,
        "lastDuration": 11086418,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 6598,
        "lastTotalOutputTokens": 1564,
        "lastTotalCacheCreationInputTokens": 16037,
        "lastTotalCacheReadInputTokens": 189403,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "bbbeb53a-73b7-4458-a51d-2c0b19582c73"
      },
      "/mnt/c/python/claude_prism": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 5,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0,
        "lastCost": 63.680972749999995,
        "lastAPIDuration": 3656937,
        "lastToolDuration": 231342,
        "lastDuration": 35069502,
        "lastLinesAdded": 13212,
        "lastLinesRemoved": 95,
        "lastTotalInputTokens": 15439,
        "lastTotalOutputTokens": 174802,
        "lastTotalCacheCreationInputTokens": 1234079,
        "lastTotalCacheReadInputTokens": 20420937,
        "lastSessionId": "55186c3f-5a31-4b1b-b85c-aaaec73320c1"
      },
      "/mnt/c/python/mainframe_copilot": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": true,
        "projectOnboardingSeenCount": 8,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0,
        "exampleFiles": [
          "demo.sh",
          "agent_controller.py",
          "tn3270_client.py",
          "flow_runner.py",
          "api_enhanced.py"
        ],
        "exampleFilesGeneratedAt": 1759105181212
      },
      "/mnt/c/python/prompt_ambiguity_analyzer": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 2,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0,
        "hasCompletedProjectOnboarding": true,
        "exampleFiles": [
          "README.md",
          "01-objective.md",
          "02-hypothesis.md",
          "03-mercury-experiment.md",
          "04-mechanisms.md"
        ],
        "exampleFilesGeneratedAt": 1759204729823,
        "lastCost": 0.29329344999999996,
        "lastAPIDuration": 520573,
        "lastToolDuration": 620,
        "lastDuration": 38392164,
        "lastLinesAdded": 697,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 468,
        "lastTotalOutputTokens": 9013,
        "lastTotalCacheCreationInputTokens": 38851,
        "lastTotalCacheReadInputTokens": 43094,
        "lastSessionId": "b8a0ac78-31a3-4661-920d-5d7a926552bd"
      },
      "/mnt/c/python/cp": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": true,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0,
        "hasCompletedProjectOnboarding": true
      },
      "/mnt/c/python/press_enter": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 4,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "lastTotalWebSearchRequests": 0
      },
      "/mnt/c/python/agent-ui": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {
          "playwright": {
            "type": "stdio",
            "command": "npx",
            "args": [
              "-y",
              "@playwright/mcp"
            ],
            "env": {}
          }
        },
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 4,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastTotalWebSearchRequests": 0
      },
      "/mnt/c/python/BAR_AI": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 2,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastTotalWebSearchRequests": 0,
        "lastCost": 0,
        "lastAPIDuration": 0,
        "lastToolDuration": 0,
        "lastDuration": 44453163,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 0,
        "lastTotalOutputTokens": 0,
        "lastTotalCacheCreationInputTokens": 0,
        "lastTotalCacheReadInputTokens": 0,
        "lastSessionId": "7d30c79d-d39a-4fad-83d3-870343a4a56e"
      },
      "/mnt/c/python/pyapp": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 3,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastTotalWebSearchRequests": 0,
        "lastCost": 0.000915,
        "lastAPIDuration": 1992,
        "lastToolDuration": 0,
        "lastDuration": 25794,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 410,
        "lastTotalOutputTokens": 101,
        "lastTotalCacheCreationInputTokens": 0,
        "lastTotalCacheReadInputTokens": 0,
        "lastSessionId": "b930c7ba-e404-4c88-bc17-a56453885eee"
      },
      "/mnt/c/python/memleak_detector": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 3,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastTotalWebSearchRequests": 0
      },
      "/mnt/c/python/FedSpeak": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 5,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "I don't have enough data to provide a meaningful response. The input only shows one file (`PROJECT_STATUS.md`) with minimal modification counts, and it's a documentation/status file rather than core a...",
          "",
          "To properly identify five frequently modified core application files, I would need:",
          "- A larger dataset with more files and higher modification counts",
          "- Files representing actual business logic (not documentation, config, or generated files)",
          "- More diversity in modification patterns across different users",
          "",
          "Could you provide a more complete git history dataset?"
        ],
        "lastTotalWebSearchRequests": 0,
        "exampleFilesGeneratedAt": 1762317843600,
        "lastCost": 1.7458593499999995,
        "lastAPIDuration": 288378,
        "lastToolDuration": 83359,
        "lastDuration": 86428542,
        "lastLinesAdded": 15,
        "lastLinesRemoved": 17,
        "lastTotalInputTokens": 20264,
        "lastTotalOutputTokens": 15093,
        "lastTotalCacheCreationInputTokens": 214569,
        "lastTotalCacheReadInputTokens": 2339382,
        "lastSessionId": "286e097e-cb02-41ff-adf8-ae2fddb80afd"
      },
      "/mnt/c/python/market-dislocation-monitor": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": []
      },
      "/mnt/c/python/judgment_import": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 2,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 0.012353,
        "lastAPIDuration": 9865,
        "lastAPIDurationWithoutRetries": 9862,
        "lastToolDuration": 0,
        "lastDuration": 174982110,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 1674,
        "lastTotalOutputTokens": 499,
        "lastTotalCacheCreationInputTokens": 0,
        "lastTotalCacheReadInputTokens": 0,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 773,
            "outputTokens": 270,
            "cacheReadInputTokens": 0,
            "cacheCreationInputTokens": 0,
            "webSearchRequests": 0,
            "costUSD": 0.002123
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 901,
            "outputTokens": 229,
            "cacheReadInputTokens": 0,
            "cacheCreationInputTokens": 0,
            "webSearchRequests": 0,
            "costUSD": 0.01023
          }
        },
        "lastSessionId": "87a30258-cdf8-41d3-8a1a-31207af748e4"
      },
      "/mnt/c/python/Torn": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastCost": 0.12539224999999998,
        "lastAPIDuration": 76176,
        "lastToolDuration": 0,
        "lastDuration": 86686271,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 989,
        "lastTotalOutputTokens": 2742,
        "lastTotalCacheCreationInputTokens": 14461,
        "lastTotalCacheReadInputTokens": 97955,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "9e648b5c-e34f-4484-b59a-2e228276f341"
      },
      "/mnt/c/python/Kosmos": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 9,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "research_director.py",
          "convergence.py",
          "llm.py",
          "result_collector.py",
          "code_validator.py"
        ],
        "lastTotalWebSearchRequests": 0,
        "exampleFilesGeneratedAt": 1763968320579,
        "hasCompletedProjectOnboarding": true,
        "lastCost": 0.001929,
        "lastAPIDuration": 2995,
        "lastToolDuration": 0,
        "lastDuration": 12391,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 1099,
        "lastTotalOutputTokens": 166,
        "lastTotalCacheCreationInputTokens": 0,
        "lastTotalCacheReadInputTokens": 0,
        "lastSessionId": "ebcc511a-fa0f-4b0f-814a-dc4f7ba811fe"
      },
      "/mnt/c/python/workflow_templates": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "ignorePatterns": [],
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": []
      },
      "/mnt/c/python/import_Sol": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": []
      },
      "/mnt/c/python/data_formulator": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 6,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "I don't have enough information to provide five filenames. The data shows only one file (IMPLEMENTATION_PLAN.md) with minimal modifications, and it's a documentation/planning file rather than core app...",
          "",
          "To properly identify frequently modified core application files, I would need:",
          "- A larger dataset with more files",
          "- Files with higher modification counts",
          "- Files that represent actual application code (not documentation or configuration)",
          "",
          "Please provide a more complete git history with additional files and their modification counts."
        ],
        "lastTotalWebSearchRequests": 0,
        "exampleFilesGeneratedAt": 1763228717372,
        "lastCost": 0.004512,
        "lastAPIDuration": 4613,
        "lastToolDuration": 0,
        "lastDuration": 60710,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 1223,
        "lastTotalOutputTokens": 211,
        "lastTotalCacheCreationInputTokens": 0,
        "lastTotalCacheReadInputTokens": 0,
        "lastSessionId": "70fbcefe-28f8-464f-92c5-ad5fc1489fd6"
      },
      "/mnt/c/python/gigamoon": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastCost": 1.4813946000000002,
        "lastAPIDuration": 428488,
        "lastToolDuration": 387294,
        "lastDuration": 6080342,
        "lastLinesAdded": 579,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 297828,
        "lastTotalOutputTokens": 19312,
        "lastTotalCacheCreationInputTokens": 137290,
        "lastTotalCacheReadInputTokens": 1221117,
        "lastTotalWebSearchRequests": 3,
        "lastSessionId": "e61da86f-bae2-45d0-b456-e32f8ec0d95c"
      },
      "/mnt/c/python/data-formulator-claude-code-proxy": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 4,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "I need at least 5 diverse files from core application logic to provide a meaningful answer, but the data shows only 1 file with minimal modifications across the repository.",
          "",
          "Based on the extremely limited git history provided, I cannot reliably identify five frequently modified core application files. The data shows only `IMPLEMENTATION_PLAN.md` with 1 modification each f...",
          "",
          "To properly complete this task, I would need:",
          "- A larger repository with more file modification history",
          "- Files with higher modification counts",
          "- Multiple source files representing different application components",
          "",
          "Please provide a repository with more substantial git history."
        ],
        "exampleFilesGeneratedAt": 1763420999001,
        "lastTotalWebSearchRequests": 0
      },
      "/mnt/c/python/gemini-cli": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastCost": 0.0013959999999999999,
        "lastAPIDuration": 2045,
        "lastToolDuration": 0,
        "lastDuration": 4972,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 606,
        "lastTotalOutputTokens": 158,
        "lastTotalCacheCreationInputTokens": 0,
        "lastTotalCacheReadInputTokens": 0,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "82a0d6c9-4f00-4912-abe3-0dfacc4e1097"
      },
      "/mnt/c/python/claudecode_swebench": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "code_swe_agent.py",
          "evaluate_predictions.py",
          "prompt_formatter.py",
          "swe_bench.py",
          "claude_interface.py"
        ],
        "lastTotalWebSearchRequests": 7,
        "exampleFilesGeneratedAt": 1763689890541
      },
      "/mnt/c/python/kosmos-research": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastCost": 14.173071250000001,
        "lastAPIDuration": 4069413,
        "lastToolDuration": 2529364,
        "lastDuration": 222987732,
        "lastLinesAdded": 3183,
        "lastLinesRemoved": 134,
        "lastTotalInputTokens": 177294,
        "lastTotalOutputTokens": 173932,
        "lastTotalCacheCreationInputTokens": 2032355,
        "lastTotalCacheReadInputTokens": 12850409,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "7cb96bb3-70ae-4f2e-b250-a9a18d8c6c26"
      },
      "/mnt/c/python/llm_mastermind_benchmark": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 2,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "I cannot provide a response because no files were listed in your request. The \"Files modified by user:\" and \"Files modified by other users:\" sections are both empty.",
          "",
          "Please provide:",
          "1. A list of files modified by the user with their modification counts",
          "2. A list of files modified by other users with their modification counts",
          "",
          "Once you provide this data, I'll analyze it and return five diverse, frequently-modified filenames representing core application logic."
        ],
        "exampleFilesGeneratedAt": 1763951778951,
        "lastTotalWebSearchRequests": 0,
        "lastCost": 46.47902320000006,
        "lastAPIDuration": 6162222,
        "lastToolDuration": 5611456,
        "lastDuration": 97577640,
        "lastLinesAdded": 3902,
        "lastLinesRemoved": 731,
        "lastTotalInputTokens": 255241,
        "lastTotalOutputTokens": 193913,
        "lastTotalCacheCreationInputTokens": 2939494,
        "lastTotalCacheReadInputTokens": 47492777,
        "lastSessionId": "009036d7-1c9a-41f6-940d-41293b09431e"
      },
      "/mnt/c/python/kosmos": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "config.py",
          "research_director.py",
          "artifacts.py",
          "llm.py",
          "executor.py"
        ],
        "exampleFilesGeneratedAt": 1765524657715,
        "hasCompletedProjectOnboarding": true,
        "lastTotalWebSearchRequests": 0,
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 116.3823395000002,
        "lastAPIDuration": 9697349,
        "lastAPIDurationWithoutRetries": 1180216,
        "lastToolDuration": 6445127,
        "lastDuration": 313379502,
        "lastLinesAdded": 16238,
        "lastLinesRemoved": 2173,
        "lastTotalInputTokens": 468637,
        "lastTotalOutputTokens": 455728,
        "lastTotalCacheCreationInputTokens": 4797028,
        "lastTotalCacheReadInputTokens": 159213257,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 134031,
            "outputTokens": 14175,
            "cacheReadInputTokens": 340380,
            "cacheCreationInputTokens": 99275,
            "webSearchRequests": 0,
            "costUSD": 0.3630377499999998
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 2122,
            "outputTokens": 57279,
            "cacheReadInputTokens": 5450025,
            "cacheCreationInputTokens": 799438,
            "webSearchRequests": 0,
            "costUSD": 9.164084999999998
          }
        },
        "lastSessionId": "7712103f-beca-4ddd-9de8-b1004867c0ae"
      },
      "/mnt/c/python/local_model": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastTotalWebSearchRequests": 12
      },
      "/mnt/c/python/skill_creator": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastCost": 0.15018349999999997,
        "lastAPIDuration": 51691,
        "lastToolDuration": 0,
        "lastDuration": 5177542,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 2074,
        "lastTotalOutputTokens": 2933,
        "lastTotalCacheCreationInputTokens": 6600,
        "lastTotalCacheReadInputTokens": 68581,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "fdcca94b-0593-41ac-80a8-3bc0bfd09581"
      },
      "/mnt/c/python/outlook-mcp": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "index.js",
          "outlook-auth-server.js",
          "list.js",
          "create.js",
          "calendar.js"
        ],
        "exampleFilesGeneratedAt": 1764450824632,
        "lastCost": 0.1039725,
        "lastAPIDuration": 54549,
        "lastToolDuration": 0,
        "lastDuration": 159967939,
        "lastLinesAdded": 0,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 2480,
        "lastTotalOutputTokens": 2643,
        "lastTotalCacheCreationInputTokens": 2634,
        "lastTotalCacheReadInputTokens": 37774,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "4e3abece-15b9-4313-b06a-b8bb49b899a9"
      },
      "/mnt/c/python/claude_code_orchestrator_skill_builder": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 1,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "I don't have any file modification data to analyze. The lists provided are empty - there are no files modified by the user or other users.",
          "",
          "Please provide the actual git history data with:",
          "- A list of files with their modification counts from the user",
          "- A list of files with their modification counts from other users",
          "",
          "Once you provide this data, I'll return exactly five filenames representing core application logic."
        ],
        "lastTotalWebSearchRequests": 0,
        "exampleFilesGeneratedAt": 1764648528710,
        "lastCost": 7.833992749999999,
        "lastAPIDuration": 297944,
        "lastToolDuration": 9012,
        "lastDuration": 8058734,
        "lastLinesAdded": 314,
        "lastLinesRemoved": 102,
        "lastTotalInputTokens": 16292,
        "lastTotalOutputTokens": 11381,
        "lastTotalCacheCreationInputTokens": 785559,
        "lastTotalCacheReadInputTokens": 5273864,
        "lastSessionId": "f9dc238a-f21e-4a9f-944e-bcccc2c0f245"
      },
      "/mnt/c/python/column_mapper": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastTotalWebSearchRequests": 0,
        "hasCompletedProjectOnboarding": true,
        "lastCost": 1.2233215000000006,
        "lastAPIDuration": 286023,
        "lastToolDuration": 36314,
        "lastDuration": 39433788,
        "lastLinesAdded": 107,
        "lastLinesRemoved": 63,
        "lastTotalInputTokens": 8089,
        "lastTotalOutputTokens": 14580,
        "lastTotalCacheCreationInputTokens": 83136,
        "lastTotalCacheReadInputTokens": 1005555,
        "lastSessionId": "5a7bd008-1149-444b-b6b3-5a241a98057a"
      },
      "/mnt/c/python/security_questionnaire": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "hasCompletedProjectOnboarding": true,
        "lastTotalWebSearchRequests": 1,
        "lastCost": 0.9386067000000001,
        "lastAPIDuration": 293819,
        "lastToolDuration": 132711,
        "lastDuration": 24879803,
        "lastLinesAdded": 352,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 54081,
        "lastTotalOutputTokens": 13728,
        "lastTotalCacheCreationInputTokens": 122066,
        "lastTotalCacheReadInputTokens": 540314,
        "lastSessionId": "a0b1dba3-d66a-4476-a214-e5da48022afa",
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastAPIDurationWithoutRetries": 293803,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 48760,
            "outputTokens": 6128,
            "cacheReadInputTokens": 153382,
            "cacheCreationInputTokens": 67823,
            "webSearchRequests": 0,
            "costUSD": 0.17951694999999998
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 5321,
            "outputTokens": 7600,
            "cacheReadInputTokens": 386932,
            "cacheCreationInputTokens": 54243,
            "webSearchRequests": 1,
            "costUSD": 0.7590897500000001
          }
        }
      },
      "/mnt/c/python/cp_reporting": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 3,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastTotalWebSearchRequests": 0,
        "lastCost": 26.254375049999993,
        "lastAPIDuration": 2319688,
        "lastToolDuration": 560396,
        "lastDuration": 698887654,
        "lastLinesAdded": 2863,
        "lastLinesRemoved": 263,
        "lastTotalInputTokens": 108095,
        "lastTotalOutputTokens": 106736,
        "lastTotalCacheCreationInputTokens": 1933921,
        "lastTotalCacheReadInputTokens": 24985774,
        "lastSessionId": "6a4d68bc-0660-4a18-9467-3db3cb20c4c9",
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        }
      },
      "/mnt/c/python/claude-skills-reference-library": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "lastCost": 12.2725897,
        "lastAPIDuration": 1899843,
        "lastToolDuration": 915540,
        "lastDuration": 8904893,
        "lastLinesAdded": 2090,
        "lastLinesRemoved": 157,
        "lastTotalInputTokens": 255900,
        "lastTotalOutputTokens": 85784,
        "lastTotalCacheCreationInputTokens": 561168,
        "lastTotalCacheReadInputTokens": 14448631,
        "lastTotalWebSearchRequests": 0,
        "lastSessionId": "6dcd33fb-de5c-4a80-b3e0-8cb53ae37ce1"
      },
      "/mnt/c/python/claude-document-dependency-tracker": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "I don't have any files or modification data to analyze. Please provide:",
          "",
          "1. A list of files modified by the user with their modification counts",
          "2. A list of files modified by other users with their modification counts",
          "",
          "Once you provide this data, I'll return exactly five filenames that represent core application logic."
        ],
        "lastTotalWebSearchRequests": 0,
        "exampleFilesGeneratedAt": 1765316862927,
        "hasCompletedProjectOnboarding": true,
        "lastCost": 72.53871919999997,
        "lastAPIDuration": 10602498,
        "lastToolDuration": 549866,
        "lastDuration": 228914353,
        "lastLinesAdded": 13891,
        "lastLinesRemoved": 4853,
        "lastTotalInputTokens": 381083,
        "lastTotalOutputTokens": 576905,
        "lastTotalCacheCreationInputTokens": 4189202,
        "lastTotalCacheReadInputTokens": 65668949,
        "lastSessionId": "9c1304b1-85b0-4ab2-9cf8-72d4a2eaa628",
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastAPIDurationWithoutRetries": 10601923,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 361085,
            "outputTokens": 26735,
            "cacheReadInputTokens": 373882,
            "cacheCreationInputTokens": 135543,
            "webSearchRequests": 0,
            "costUSD": 0.7015769500000002
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 19998,
            "outputTokens": 550170,
            "cacheReadInputTokens": 65295067,
            "cacheCreationInputTokens": 4053659,
            "webSearchRequests": 0,
            "costUSD": 71.83714225
          }
        },
        "disabledMcpServers": [
          "specbuilder"
        ]
      },
      "/mnt/c/python/claude-hooks-manager": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 5,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "hooks_manager.py",
          "README.md",
          "renderers/__init__.py",
          "commands/hooks.md",
          ".gitignore"
        ],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 9.113008949999998,
        "lastAPIDuration": 810161,
        "lastAPIDurationWithoutRetries": 810068,
        "lastToolDuration": 113028,
        "lastDuration": 59095801,
        "lastLinesAdded": 2367,
        "lastLinesRemoved": 89,
        "lastTotalInputTokens": 68165,
        "lastTotalOutputTokens": 47832,
        "lastTotalCacheCreationInputTokens": 1020803,
        "lastTotalCacheReadInputTokens": 4236370,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 59055,
            "outputTokens": 9374,
            "cacheReadInputTokens": 342362,
            "cacheCreationInputTokens": 72235,
            "webSearchRequests": 0,
            "costUSD": 0.23045495
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 9110,
            "outputTokens": 38458,
            "cacheReadInputTokens": 3894008,
            "cacheCreationInputTokens": 948568,
            "webSearchRequests": 0,
            "costUSD": 8.882554
          }
        },
        "lastSessionId": "8a19dd8c-4b2e-4521-9a13-7e1b87e2d00c",
        "exampleFilesGeneratedAt": 1765521054929
      },
      "/mnt/c/python/claude-hooks-manager/worktrees/task-1-scanner-terminal": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 1.003721,
        "lastAPIDuration": 189190,
        "lastAPIDurationWithoutRetries": 189167,
        "lastToolDuration": 2530,
        "lastDuration": 71770497,
        "lastLinesAdded": 364,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 6517,
        "lastTotalOutputTokens": 9720,
        "lastTotalCacheCreationInputTokens": 39558,
        "lastTotalCacheReadInputTokens": 1027085,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 5261,
            "outputTokens": 580,
            "cacheReadInputTokens": 0,
            "cacheCreationInputTokens": 0,
            "webSearchRequests": 0,
            "costUSD": 0.008161
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 1256,
            "outputTokens": 9140,
            "cacheReadInputTokens": 1027085,
            "cacheCreationInputTokens": 39558,
            "webSearchRequests": 0,
            "costUSD": 0.9955599999999999
          }
        },
        "lastSessionId": "de2ccaa7-06eb-420d-b3f6-5fa87dd2f47b"
      },
      "/mnt/c/python/claude-hooks-manager/worktrees/task-2-html": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "hooks_manager.py",
          "README.md",
          "",
          "I can only identify 2 distinct files from your data. The same files appear in both user categories with identical modification counts, and there are only 2 unique filenames total (README.md appears to...",
          "",
          "To provide 5 filenames as requested, I would need a dataset with at least 5 distinct files."
        ],
        "exampleFilesGeneratedAt": 1765515741572,
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 0.6021782499999999,
        "lastAPIDuration": 104714,
        "lastAPIDurationWithoutRetries": 104692,
        "lastToolDuration": 1470,
        "lastDuration": 2871123,
        "lastLinesAdded": 33,
        "lastLinesRemoved": 3,
        "lastTotalInputTokens": 9379,
        "lastTotalOutputTokens": 4215,
        "lastTotalCacheCreationInputTokens": 32235,
        "lastTotalCacheReadInputTokens": 579799,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 8175,
            "outputTokens": 438,
            "cacheReadInputTokens": 0,
            "cacheCreationInputTokens": 0,
            "webSearchRequests": 0,
            "costUSD": 0.010365000000000001
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 1204,
            "outputTokens": 3777,
            "cacheReadInputTokens": 579799,
            "cacheCreationInputTokens": 32235,
            "webSearchRequests": 0,
            "costUSD": 0.59181325
          }
        },
        "lastSessionId": "9cd002dd-35f6-415a-8b48-7ca3ef39e371"
      },
      "/mnt/c/python/claude-hooks-manager/worktrees/task-3-markdown": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "hooks_manager.py",
          "README.md",
          "commands.py",
          "utils.py",
          "config.py"
        ],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "exampleFilesGeneratedAt": 1765515965141,
        "lastCost": 0.4069045,
        "lastAPIDuration": 108608,
        "lastAPIDurationWithoutRetries": 108593,
        "lastToolDuration": 2895,
        "lastDuration": 1986687,
        "lastLinesAdded": 134,
        "lastLinesRemoved": 1,
        "lastTotalInputTokens": 5791,
        "lastTotalOutputTokens": 5056,
        "lastTotalCacheCreationInputTokens": 13130,
        "lastTotalCacheReadInputTokens": 389534,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 4090,
            "outputTokens": 446,
            "cacheReadInputTokens": 0,
            "cacheCreationInputTokens": 0,
            "webSearchRequests": 0,
            "costUSD": 0.006319999999999999
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 1701,
            "outputTokens": 4610,
            "cacheReadInputTokens": 389534,
            "cacheCreationInputTokens": 13130,
            "webSearchRequests": 0,
            "costUSD": 0.4005845
          }
        },
        "lastSessionId": "0a495e09-924c-4433-9b05-ebaa3e93bad7"
      },
      "/mnt/c/python/claude-hooks-manager/worktrees/task-4-tui": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 0.9417687500000002,
        "lastAPIDuration": 182972,
        "lastAPIDurationWithoutRetries": 182947,
        "lastToolDuration": 1750,
        "lastDuration": 3139079,
        "lastLinesAdded": 383,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 6796,
        "lastTotalOutputTokens": 10723,
        "lastTotalCacheCreationInputTokens": 42431,
        "lastTotalCacheReadInputTokens": 817848,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 5416,
            "outputTokens": 637,
            "cacheReadInputTokens": 0,
            "cacheCreationInputTokens": 0,
            "webSearchRequests": 0,
            "costUSD": 0.008601
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 1380,
            "outputTokens": 10086,
            "cacheReadInputTokens": 817848,
            "cacheCreationInputTokens": 42431,
            "webSearchRequests": 0,
            "costUSD": 0.9331677499999999
          }
        },
        "lastSessionId": "d3974794-4abb-49b5-a3b5-4f8b50868d50"
      },
      "/mnt/c/python/claude-hooks-manager/worktrees/task-1-core": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 1.51589825,
        "lastAPIDuration": 248702,
        "lastAPIDurationWithoutRetries": 248677,
        "lastToolDuration": 5446,
        "lastDuration": 306197,
        "lastLinesAdded": 377,
        "lastLinesRemoved": 0,
        "lastTotalInputTokens": 9013,
        "lastTotalOutputTokens": 13916,
        "lastTotalCacheCreationInputTokens": 97745,
        "lastTotalCacheReadInputTokens": 1118886,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 7729,
            "outputTokens": 825,
            "cacheReadInputTokens": 0,
            "cacheCreationInputTokens": 0,
            "webSearchRequests": 0,
            "costUSD": 0.011854
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 1284,
            "outputTokens": 13091,
            "cacheReadInputTokens": 1118886,
            "cacheCreationInputTokens": 97745,
            "webSearchRequests": 0,
            "costUSD": 1.50404425
          }
        },
        "lastSessionId": "f41b99ab-1f04-4eaf-a39a-7ceb6267501d"
      },
      "/mnt/c/python/claude-repo-xray": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 2,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [
          "I need to identify five frequently modified files representing core application logic from the provided git history.",
          "",
          "However, the data provided shows only:",
          "- 2 modifications to README.md by the user",
          "- 2 modifications to README.md by other users",
          "",
          "This is insufficient data to return five diverse files representing core application logic. The dataset contains only one file (README.md), which is typically documentation rather than core applicatio...",
          "",
          "Since I cannot identify five legitimate core application logic files from this data, I cannot provide a valid response that meets the criteria of:",
          "- Five filenames"
        ],
        "_exampleFiles_total": 16,
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "lastCost": 41.50785895,
        "lastAPIDuration": 3093381,
        "lastAPIDurationWithoutRetries": 3093164,
        "lastToolDuration": 425507,
        "lastDuration": 26241708,
        "lastLinesAdded": 4015,
        "lastLinesRemoved": 1711,
        "lastTotalInputTokens": 133647,
        "lastTotalOutputTokens": 181006,
        "lastTotalCacheCreationInputTokens": 4362459,
        "lastTotalCacheReadInputTokens": 22422504,
        "lastTotalWebSearchRequests": 0,
        "lastModelUsage": {
          "claude-haiku-4-5-20251001": {
            "inputTokens": 127688,
            "outputTokens": 46128,
            "cacheReadInputTokens": 294237,
            "cacheCreationInputTokens": 122228,
            "webSearchRequests": 0,
            "costUSD": 0.5405366999999999
          },
          "claude-opus-4-5-20251101": {
            "inputTokens": 5959,
            "outputTokens": 134878,
            "cacheReadInputTokens": 22128267,
            "cacheCreationInputTokens": 4240231,
            "webSearchRequests": 0,
            "costUSD": 40.96732225
          }
        },
        "lastSessionId": "dced9bb5-2cbf-4594-96a1-091fb4ed10f1",
        "exampleFilesGeneratedAt": 1765587849274
      },
      "/mnt/c/python/claude-code-plugin-marketplace": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        },
        "hasCompletedProjectOnboarding": true
      },
      "/mnt/c/python/claude_adversarial_tester": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        }
      },
      "/mnt/c/python/claude_metrics": {
        "allowedTools": [],
        "mcpContextUris": [],
        "mcpServers": {},
        "enabledMcpjsonServers": [],
        "disabledMcpjsonServers": [],
        "hasTrustDialogAccepted": false,
        "projectOnboardingSeenCount": 0,
        "hasClaudeMdExternalIncludesApproved": false,
        "hasClaudeMdExternalIncludesWarningShown": false,
        "exampleFiles": [],
        "reactVulnerabilityCache": {
          "detected": false,
          "package": null,
          "packageName": null,
          "version": null,
          "packageManager": null
        }
      }
    },
    "maxSubscriptionNoticeCount": 0,
    "hasAvailableMaxSubscription": false,
    "cachedChangelog": "# Changelog\n\n## 2.0.69\n\n- Minor bugfixes\n\n## 2.0.68\n\n- Fixed IME (Input Method Editor) support for languages like Chinese, Japanese, and Korean by correctly positioning the composition window at the c...",
    "changelogLastFetched": 1765588500213,
    "firstStartTime": "2025-05-19T04:20:16.876Z",
    "s1mAccessCache": {
      "9bff8978-bf8d-4174-b2d3-37f4ce5c6d1c": {
        "hasAccess": false,
        "hasAccessNotAsDefault": false,
        "timestamp": 1765680347549
      }
    },
    "autoUpdatesProtectedForNative": true,
    "hasOpusPlanDefault": false,
    "isQualifiedForDataSharing": false,
    "subscriptionNoticeCount": 0,
    "hasAvailableSubscription": false,
    "bypassPermissionsModeAccepted": true,
    "fallbackAvailableWarningThreshold": 0.5,
    "githubActionSetupCount": 1,
    "lastReleaseNotesSeen": "2.0.69",
    "lastPlanModeUse": 1765693351183,
    "feedbackSurveyState": {
      "lastShownTime": 1765599282202
    },
    "sonnet45MigrationComplete": true,
    "sonnet45MigrationTimestamp": 1759178288330,
    "githubRepoPaths": {
      "jimmc414/claudecode_swebench": [
        "/mnt/c/python/claudecode_swebench"
      ],
      "jimmc414/kosmos-research": [
        "/mnt/c/python/kosmos-research/R&D"
      ],
      "jimmc414/llm_mastermind_benchmark": [
        "/mnt/c/python/llm_mastermind_benchmark"
      ],
      "jimmc414/kosmos": [
        "/mnt/c/python/kosmos",
        "/mnt/c/python/Kosmos"
      ],
      "jimmc414/onefilellm": [
        "/mnt/c/python/onefilellm"
      ],
      "ryaker/outlook-mcp": [
        "/mnt/c/python/outlook-mcp"
      ],
      "jimmc414/claude_code_orchestrator_skill_builder": [
        "/mnt/c/python/claude_code_orchestrator_skill_builder"
      ],
      "jimmc414/claude-document-dependency-tracker": [
        "/mnt/c/python/claude-document-dependency-tracker"
      ],
      "jimmc414/claude-hooks-manager": [
        "/mnt/c/python/claude-hooks-manager/worktrees/task-1-core",
        "/mnt/c/python/claude-hooks-manager/worktrees/task-4-tui",
        "/mnt/c/python/claude-hooks-manager/worktrees/task-3-markdown",
        "/mnt/c/python/claude-hooks-manager/worktrees/task-2-html",
        "/mnt/c/python/claude-hooks-manager/worktrees/task-1-scanner-terminal",
        "/mnt/c/python/claude-hooks-manager"
      ],
      "jimmc414/claude-repo-xray": [
        "/mnt/c/python/claude-repo-xray"
      ]
    },
    "opus45MigrationComplete": true,
    "hasShownOpus45Notice": {
      "9bff8978-bf8d-4174-b2d3-37f4ce5c6d1c": true
    },
    "officialMarketplaceAutoInstallAttempted": true,
    "officialMarketplaceAutoInstalled": false,
    "officialMarketplaceAutoInstallFailReason": "unknown",
    "oauthAccount": {
      "accountUuid": "2bc11f6e-99dd-46ce-b296-9a5eea2334d4",
      "emailAddress": "jimmc414@gmail.com",
      "organizationUuid": "9bff8978-bf8d-4174-b2d3-37f4ce5c6d1c",
      "hasExtraUsageEnabled": false,
      "displayName": "Jim",
      "organizationRole": "admin",
      "workspaceRole": null,
      "organizationName": "Jim McMillan"
    },
    "claudeCodeFirstTokenDate": "2025-05-03T08:22:27.347362Z",
    "passesEligibilityCache": {
      "9bff8978-bf8d-4174-b2d3-37f4ce5c6d1c": {
        "eligible": true,
        "referral_code_details": {
          "code": "Rs5pXdvuuw",
          "campaign": "claude_code_guest_pass",
          "referral_link": "https://claude.ai/referral/Rs5pXdvuuw"
        },
        "timestamp": 1765680346866
      }
    },
    "passesUpsellSeenCount": 3,
    "hasVisitedPasses": true
  },
  "usage": {
    "numStartups": 293,
    "promptQueueUseCount": 202,
    "memoryUsageCount": 1
  },
  "onboarding": {
    "hasCompletedOnboarding": true,
    "lastOnboardingVersion": "2.0.67",
    "hasSeenTasksHint": true,
    "hasSeenStashHint": true
  },
  "tips_history": {
    "new-user-warmup": 1,
    "plan-mode-for-complex-tasks": 67,
    "terminal-setup": 284,
    "theme-command": 283,
    "status-line": 146,
    "prompt-queue": 29,
    "enter-to-steer-in-relatime": 283,
    "todo-list": 274,
    "# for memory": 284,
    "install-github-app": 13,
    "permissions": 287,
    "drag-and-drop-images": 287,
    "double-esc": 35,
    "continue": 287,
    "custom-commands": 289,
    "shift-tab": 287,
    "image-paste": 286,
    "custom-agents": 289,
    "double-esc-code-restore": 287,
    "git-worktrees": 289,
    "tab-toggle-thinking": 286,
    "ultrathink-keyword": 287,
    "stickers-command": 277,
    "default-permission-mode-config": 184,
    "rename-conversation": 279,
    "colorterm-truecolor": 292,
    "config-thinking-mode": 292,
    "frontend-design-plugin": 271
  },
  "feature_flags": {
    "tengu_disable_bypass_permissions_mode": false,
    "tengu_use_file_checkpoints": true,
    "tengu_tool_pear": false,
    "tengu_migrate_ignore_patterns": false,
    "tengu_halloween": false,
    "tengu_glob_with_rg": false,
    "tengu_web_tasks": true,
    "tengu_log_1p_events": true,
    "tengu_enable_versioned_plugins": false,
    "code_slack_app_install_banner": false,
    "tengu_sumi": false,
    "tengu_react_vulnerability_warning": false,
    "tengu_tool_result_persistence": false,
    "tengu_c4w_usage_limit_notifications_enabled": false,
    "tengu_thinkback": false
  },
  "dynamic_configs": {
    "tengu-top-of-feed-tip": {
      "tip": "",
      "color": ""
    }
  },
  "projects": {
    "/home/jim/code_install": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "01505466-39cc-4f61-b2b2-cc83419a41b9",
      "lastCost": 0.7597266999999999,
      "lastAPIDuration": 196143,
      "lastToolDuration": 0,
      "lastDuration": 1272446,
      "lastLinesAdded": 123,
      "lastLinesRemoved": 53,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/home/jim/code_install/onefilellm": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "56e45cd3-7fc5-41aa-b14c-74a3df2a9a4a",
      "lastCost": 0.3129548,
      "lastAPIDuration": 98344,
      "lastToolDuration": 0,
      "lastDuration": 68728956,
      "lastLinesAdded": 21,
      "lastLinesRemoved": 1,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/home/jim": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": true,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "cd47fb6d-a2a3-49e3-ba7e-0f9df20acbd2",
      "lastCost": 0.31100314999999995,
      "lastAPIDuration": 9950,
      "lastToolDuration": 0,
      "lastDuration": 54129972,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 131,
      "lastTotalOutputTokens": 261,
      "lastTotalCacheCreationInputTokens": 15641,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/mcp_start": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {},
      "lastSessionId": "df9a3171-5b2a-4930-8ec6-659d15993f08",
      "lastCost": 0.29963755000000003,
      "lastAPIDuration": 70080,
      "lastToolDuration": 0,
      "lastDuration": 18803684,
      "lastLinesAdded": 20,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/jack": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "451b2810-9539-4dcc-be53-291f90110a59",
      "lastCost": 3.7580959999999983,
      "lastAPIDuration": 1713205,
      "lastToolDuration": 0,
      "lastDuration": 6622889,
      "lastLinesAdded": 3731,
      "lastLinesRemoved": 230,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/jack_page": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/onefilellm": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {},
      "lastSessionId": "7a951406-d7d1-4572-92bc-5b443aeca741",
      "lastCost": 0.26258205000000007,
      "lastAPIDuration": 73107,
      "lastToolDuration": 57078,
      "lastDuration": 77089767,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 15524,
      "lastTotalOutputTokens": 4807,
      "lastTotalCacheCreationInputTokens": 54141,
      "lastTotalCacheReadInputTokens": 230492,
      "lastModelUsage": {}
    },
    "/mnt/c/python": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 4,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "335f8a35-9a1c-42f3-858a-5eb62a0748be",
      "lastCost": 2.6845739500000017,
      "lastAPIDuration": 531123,
      "lastToolDuration": 248242,
      "lastDuration": 25372118,
      "lastLinesAdded": 2150,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 32849,
      "lastTotalOutputTokens": 42127,
      "lastTotalCacheCreationInputTokens": 406993,
      "lastTotalCacheReadInputTokens": 784063,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 31808,
          "outputTokens": 19095,
          "cacheReadInputTokens": 249267,
          "cacheCreationInputTokens": 171949,
          "webSearchRequests": 0,
          "costUSD": 0.36714595000000005
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 1041,
          "outputTokens": 23032,
          "cacheReadInputTokens": 534796,
          "cacheCreationInputTokens": 235044,
          "webSearchRequests": 0,
          "costUSD": 2.317428
        }
      }
    },
    "/mnt/c/python/claude_codex_collab": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 4,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "b35c9d60-7b0f-41aa-a3fa-53d95bf95eaa",
      "lastCost": 22.113691599999996,
      "lastAPIDuration": 1442516,
      "lastToolDuration": 8449,
      "lastDuration": 60262092,
      "lastLinesAdded": 3574,
      "lastLinesRemoved": 77,
      "lastTotalInputTokens": 46930,
      "lastTotalOutputTokens": 59073,
      "lastTotalCacheCreationInputTokens": 362080,
      "lastTotalCacheReadInputTokens": 7361104,
      "lastModelUsage": {}
    },
    "/mnt/c/python/temp": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 4,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "3fd04f1b-3aef-4a9f-9c48-a853fe5433bb",
      "lastCost": 0.0009376,
      "lastAPIDuration": 2001,
      "lastToolDuration": 0,
      "lastDuration": 105957872,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 1067,
      "lastTotalOutputTokens": 21,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claude_control": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 7,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "319c8ef3-904d-4af0-92d4-6dcf79760d42",
      "lastCost": 91.02183265000014,
      "lastAPIDuration": 4327638,
      "lastToolDuration": 65474,
      "lastDuration": 9953236,
      "lastLinesAdded": 3686,
      "lastLinesRemoved": 500,
      "lastTotalInputTokens": 56585,
      "lastTotalOutputTokens": 178286,
      "lastTotalCacheCreationInputTokens": 1348185,
      "lastTotalCacheReadInputTokens": 34972783,
      "lastModelUsage": {}
    },
    "/mnt/c/python/Generic_Reg_F_Import": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "bbbeb53a-73b7-4458-a51d-2c0b19582c73",
      "lastCost": 0.68690025,
      "lastAPIDuration": 70345,
      "lastToolDuration": 8019,
      "lastDuration": 11086418,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 6598,
      "lastTotalOutputTokens": 1564,
      "lastTotalCacheCreationInputTokens": 16037,
      "lastTotalCacheReadInputTokens": 189403,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claude_prism": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 5,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "55186c3f-5a31-4b1b-b85c-aaaec73320c1",
      "lastCost": 63.680972749999995,
      "lastAPIDuration": 3656937,
      "lastToolDuration": 231342,
      "lastDuration": 35069502,
      "lastLinesAdded": 13212,
      "lastLinesRemoved": 95,
      "lastTotalInputTokens": 15439,
      "lastTotalOutputTokens": 174802,
      "lastTotalCacheCreationInputTokens": 1234079,
      "lastTotalCacheReadInputTokens": 20420937,
      "lastModelUsage": {}
    },
    "/mnt/c/python/mainframe_copilot": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 8,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/prompt_ambiguity_analyzer": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {},
      "lastSessionId": "b8a0ac78-31a3-4661-920d-5d7a926552bd",
      "lastCost": 0.29329344999999996,
      "lastAPIDuration": 520573,
      "lastToolDuration": 620,
      "lastDuration": 38392164,
      "lastLinesAdded": 697,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 468,
      "lastTotalOutputTokens": 9013,
      "lastTotalCacheCreationInputTokens": 38851,
      "lastTotalCacheReadInputTokens": 43094,
      "lastModelUsage": {}
    },
    "/mnt/c/python/cp": {
      "allowedTools": [],
      "hasTrustDialogAccepted": true,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/press_enter": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 4,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/agent-ui": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {
        "playwright": {
          "type": "stdio",
          "command": "npx",
          "args": [
            "-y",
            "@playwright/mcp"
          ],
          "env": {}
        }
      },
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 4,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/BAR_AI": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "7d30c79d-d39a-4fad-83d3-870343a4a56e",
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 44453163,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/pyapp": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 3,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "b930c7ba-e404-4c88-bc17-a56453885eee",
      "lastCost": 0.000915,
      "lastAPIDuration": 1992,
      "lastToolDuration": 0,
      "lastDuration": 25794,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 410,
      "lastTotalOutputTokens": 101,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/memleak_detector": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 3,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/FedSpeak": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 5,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "286e097e-cb02-41ff-adf8-ae2fddb80afd",
      "lastCost": 1.7458593499999995,
      "lastAPIDuration": 288378,
      "lastToolDuration": 83359,
      "lastDuration": 86428542,
      "lastLinesAdded": 15,
      "lastLinesRemoved": 17,
      "lastTotalInputTokens": 20264,
      "lastTotalOutputTokens": 15093,
      "lastTotalCacheCreationInputTokens": 214569,
      "lastTotalCacheReadInputTokens": 2339382,
      "lastModelUsage": {}
    },
    "/mnt/c/python/market-dislocation-monitor": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/judgment_import": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "87a30258-cdf8-41d3-8a1a-31207af748e4",
      "lastCost": 0.012353,
      "lastAPIDuration": 9865,
      "lastToolDuration": 0,
      "lastDuration": 174982110,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 1674,
      "lastTotalOutputTokens": 499,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 773,
          "outputTokens": 270,
          "cacheReadInputTokens": 0,
          "cacheCreationInputTokens": 0,
          "webSearchRequests": 0,
          "costUSD": 0.002123
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 901,
          "outputTokens": 229,
          "cacheReadInputTokens": 0,
          "cacheCreationInputTokens": 0,
          "webSearchRequests": 0,
          "costUSD": 0.01023
        }
      }
    },
    "/mnt/c/python/Torn": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "9e648b5c-e34f-4484-b59a-2e228276f341",
      "lastCost": 0.12539224999999998,
      "lastAPIDuration": 76176,
      "lastToolDuration": 0,
      "lastDuration": 86686271,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 989,
      "lastTotalOutputTokens": 2742,
      "lastTotalCacheCreationInputTokens": 14461,
      "lastTotalCacheReadInputTokens": 97955,
      "lastModelUsage": {}
    },
    "/mnt/c/python/Kosmos": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 9,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {},
      "lastSessionId": "ebcc511a-fa0f-4b0f-814a-dc4f7ba811fe",
      "lastCost": 0.001929,
      "lastAPIDuration": 2995,
      "lastToolDuration": 0,
      "lastDuration": 12391,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 1099,
      "lastTotalOutputTokens": 166,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/workflow_templates": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/import_Sol": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/data_formulator": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 6,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "70fbcefe-28f8-464f-92c5-ad5fc1489fd6",
      "lastCost": 0.004512,
      "lastAPIDuration": 4613,
      "lastToolDuration": 0,
      "lastDuration": 60710,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 1223,
      "lastTotalOutputTokens": 211,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/gigamoon": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "e61da86f-bae2-45d0-b456-e32f8ec0d95c",
      "lastCost": 1.4813946000000002,
      "lastAPIDuration": 428488,
      "lastToolDuration": 387294,
      "lastDuration": 6080342,
      "lastLinesAdded": 579,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 297828,
      "lastTotalOutputTokens": 19312,
      "lastTotalCacheCreationInputTokens": 137290,
      "lastTotalCacheReadInputTokens": 1221117,
      "lastModelUsage": {}
    },
    "/mnt/c/python/data-formulator-claude-code-proxy": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 4,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/gemini-cli": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "82a0d6c9-4f00-4912-abe3-0dfacc4e1097",
      "lastCost": 0.0013959999999999999,
      "lastAPIDuration": 2045,
      "lastToolDuration": 0,
      "lastDuration": 4972,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 606,
      "lastTotalOutputTokens": 158,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claudecode_swebench": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/kosmos-research": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "7cb96bb3-70ae-4f2e-b250-a9a18d8c6c26",
      "lastCost": 14.173071250000001,
      "lastAPIDuration": 4069413,
      "lastToolDuration": 2529364,
      "lastDuration": 222987732,
      "lastLinesAdded": 3183,
      "lastLinesRemoved": 134,
      "lastTotalInputTokens": 177294,
      "lastTotalOutputTokens": 173932,
      "lastTotalCacheCreationInputTokens": 2032355,
      "lastTotalCacheReadInputTokens": 12850409,
      "lastModelUsage": {}
    },
    "/mnt/c/python/llm_mastermind_benchmark": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "009036d7-1c9a-41f6-940d-41293b09431e",
      "lastCost": 46.47902320000006,
      "lastAPIDuration": 6162222,
      "lastToolDuration": 5611456,
      "lastDuration": 97577640,
      "lastLinesAdded": 3902,
      "lastLinesRemoved": 731,
      "lastTotalInputTokens": 255241,
      "lastTotalOutputTokens": 193913,
      "lastTotalCacheCreationInputTokens": 2939494,
      "lastTotalCacheReadInputTokens": 47492777,
      "lastModelUsage": {}
    },
    "/mnt/c/python/kosmos": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "7712103f-beca-4ddd-9de8-b1004867c0ae",
      "lastCost": 116.3823395000002,
      "lastAPIDuration": 9697349,
      "lastToolDuration": 6445127,
      "lastDuration": 313379502,
      "lastLinesAdded": 16238,
      "lastLinesRemoved": 2173,
      "lastTotalInputTokens": 468637,
      "lastTotalOutputTokens": 455728,
      "lastTotalCacheCreationInputTokens": 4797028,
      "lastTotalCacheReadInputTokens": 159213257,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 134031,
          "outputTokens": 14175,
          "cacheReadInputTokens": 340380,
          "cacheCreationInputTokens": 99275,
          "webSearchRequests": 0,
          "costUSD": 0.3630377499999998
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 2122,
          "outputTokens": 57279,
          "cacheReadInputTokens": 5450025,
          "cacheCreationInputTokens": 799438,
          "webSearchRequests": 0,
          "costUSD": 9.164084999999998
        }
      }
    },
    "/mnt/c/python/local_model": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/skill_creator": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "fdcca94b-0593-41ac-80a8-3bc0bfd09581",
      "lastCost": 0.15018349999999997,
      "lastAPIDuration": 51691,
      "lastToolDuration": 0,
      "lastDuration": 5177542,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 2074,
      "lastTotalOutputTokens": 2933,
      "lastTotalCacheCreationInputTokens": 6600,
      "lastTotalCacheReadInputTokens": 68581,
      "lastModelUsage": {}
    },
    "/mnt/c/python/outlook-mcp": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "4e3abece-15b9-4313-b06a-b8bb49b899a9",
      "lastCost": 0.1039725,
      "lastAPIDuration": 54549,
      "lastToolDuration": 0,
      "lastDuration": 159967939,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 2480,
      "lastTotalOutputTokens": 2643,
      "lastTotalCacheCreationInputTokens": 2634,
      "lastTotalCacheReadInputTokens": 37774,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claude_code_orchestrator_skill_builder": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 1,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "f9dc238a-f21e-4a9f-944e-bcccc2c0f245",
      "lastCost": 7.833992749999999,
      "lastAPIDuration": 297944,
      "lastToolDuration": 9012,
      "lastDuration": 8058734,
      "lastLinesAdded": 314,
      "lastLinesRemoved": 102,
      "lastTotalInputTokens": 16292,
      "lastTotalOutputTokens": 11381,
      "lastTotalCacheCreationInputTokens": 785559,
      "lastTotalCacheReadInputTokens": 5273864,
      "lastModelUsage": {}
    },
    "/mnt/c/python/column_mapper": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {},
      "lastSessionId": "5a7bd008-1149-444b-b6b3-5a241a98057a",
      "lastCost": 1.2233215000000006,
      "lastAPIDuration": 286023,
      "lastToolDuration": 36314,
      "lastDuration": 39433788,
      "lastLinesAdded": 107,
      "lastLinesRemoved": 63,
      "lastTotalInputTokens": 8089,
      "lastTotalOutputTokens": 14580,
      "lastTotalCacheCreationInputTokens": 83136,
      "lastTotalCacheReadInputTokens": 1005555,
      "lastModelUsage": {}
    },
    "/mnt/c/python/security_questionnaire": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "a0b1dba3-d66a-4476-a214-e5da48022afa",
      "lastCost": 0.9386067000000001,
      "lastAPIDuration": 293819,
      "lastToolDuration": 132711,
      "lastDuration": 24879803,
      "lastLinesAdded": 352,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 54081,
      "lastTotalOutputTokens": 13728,
      "lastTotalCacheCreationInputTokens": 122066,
      "lastTotalCacheReadInputTokens": 540314,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 48760,
          "outputTokens": 6128,
          "cacheReadInputTokens": 153382,
          "cacheCreationInputTokens": 67823,
          "webSearchRequests": 0,
          "costUSD": 0.17951694999999998
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 5321,
          "outputTokens": 7600,
          "cacheReadInputTokens": 386932,
          "cacheCreationInputTokens": 54243,
          "webSearchRequests": 1,
          "costUSD": 0.7590897500000001
        }
      }
    },
    "/mnt/c/python/cp_reporting": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 3,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "6a4d68bc-0660-4a18-9467-3db3cb20c4c9",
      "lastCost": 26.254375049999993,
      "lastAPIDuration": 2319688,
      "lastToolDuration": 560396,
      "lastDuration": 698887654,
      "lastLinesAdded": 2863,
      "lastLinesRemoved": 263,
      "lastTotalInputTokens": 108095,
      "lastTotalOutputTokens": 106736,
      "lastTotalCacheCreationInputTokens": 1933921,
      "lastTotalCacheReadInputTokens": 24985774,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claude-skills-reference-library": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {},
      "lastSessionId": "6dcd33fb-de5c-4a80-b3e0-8cb53ae37ce1",
      "lastCost": 12.2725897,
      "lastAPIDuration": 1899843,
      "lastToolDuration": 915540,
      "lastDuration": 8904893,
      "lastLinesAdded": 2090,
      "lastLinesRemoved": 157,
      "lastTotalInputTokens": 255900,
      "lastTotalOutputTokens": 85784,
      "lastTotalCacheCreationInputTokens": 561168,
      "lastTotalCacheReadInputTokens": 14448631,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claude-document-dependency-tracker": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "9c1304b1-85b0-4ab2-9cf8-72d4a2eaa628",
      "lastCost": 72.53871919999997,
      "lastAPIDuration": 10602498,
      "lastToolDuration": 549866,
      "lastDuration": 228914353,
      "lastLinesAdded": 13891,
      "lastLinesRemoved": 4853,
      "lastTotalInputTokens": 381083,
      "lastTotalOutputTokens": 576905,
      "lastTotalCacheCreationInputTokens": 4189202,
      "lastTotalCacheReadInputTokens": 65668949,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 361085,
          "outputTokens": 26735,
          "cacheReadInputTokens": 373882,
          "cacheCreationInputTokens": 135543,
          "webSearchRequests": 0,
          "costUSD": 0.7015769500000002
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 19998,
          "outputTokens": 550170,
          "cacheReadInputTokens": 65295067,
          "cacheCreationInputTokens": 4053659,
          "webSearchRequests": 0,
          "costUSD": 71.83714225
        }
      }
    },
    "/mnt/c/python/claude-hooks-manager": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 5,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "8a19dd8c-4b2e-4521-9a13-7e1b87e2d00c",
      "lastCost": 9.113008949999998,
      "lastAPIDuration": 810161,
      "lastToolDuration": 113028,
      "lastDuration": 59095801,
      "lastLinesAdded": 2367,
      "lastLinesRemoved": 89,
      "lastTotalInputTokens": 68165,
      "lastTotalOutputTokens": 47832,
      "lastTotalCacheCreationInputTokens": 1020803,
      "lastTotalCacheReadInputTokens": 4236370,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 59055,
          "outputTokens": 9374,
          "cacheReadInputTokens": 342362,
          "cacheCreationInputTokens": 72235,
          "webSearchRequests": 0,
          "costUSD": 0.23045495
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 9110,
          "outputTokens": 38458,
          "cacheReadInputTokens": 3894008,
          "cacheCreationInputTokens": 948568,
          "webSearchRequests": 0,
          "costUSD": 8.882554
        }
      }
    },
    "/mnt/c/python/claude-hooks-manager/worktrees/task-1-scanner-terminal": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "de2ccaa7-06eb-420d-b3f6-5fa87dd2f47b",
      "lastCost": 1.003721,
      "lastAPIDuration": 189190,
      "lastToolDuration": 2530,
      "lastDuration": 71770497,
      "lastLinesAdded": 364,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 6517,
      "lastTotalOutputTokens": 9720,
      "lastTotalCacheCreationInputTokens": 39558,
      "lastTotalCacheReadInputTokens": 1027085,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 5261,
          "outputTokens": 580,
          "cacheReadInputTokens": 0,
          "cacheCreationInputTokens": 0,
          "webSearchRequests": 0,
          "costUSD": 0.008161
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 1256,
          "outputTokens": 9140,
          "cacheReadInputTokens": 1027085,
          "cacheCreationInputTokens": 39558,
          "webSearchRequests": 0,
          "costUSD": 0.9955599999999999
        }
      }
    },
    "/mnt/c/python/claude-hooks-manager/worktrees/task-2-html": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "9cd002dd-35f6-415a-8b48-7ca3ef39e371",
      "lastCost": 0.6021782499999999,
      "lastAPIDuration": 104714,
      "lastToolDuration": 1470,
      "lastDuration": 2871123,
      "lastLinesAdded": 33,
      "lastLinesRemoved": 3,
      "lastTotalInputTokens": 9379,
      "lastTotalOutputTokens": 4215,
      "lastTotalCacheCreationInputTokens": 32235,
      "lastTotalCacheReadInputTokens": 579799,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 8175,
          "outputTokens": 438,
          "cacheReadInputTokens": 0,
          "cacheCreationInputTokens": 0,
          "webSearchRequests": 0,
          "costUSD": 0.010365000000000001
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 1204,
          "outputTokens": 3777,
          "cacheReadInputTokens": 579799,
          "cacheCreationInputTokens": 32235,
          "webSearchRequests": 0,
          "costUSD": 0.59181325
        }
      }
    },
    "/mnt/c/python/claude-hooks-manager/worktrees/task-3-markdown": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "0a495e09-924c-4433-9b05-ebaa3e93bad7",
      "lastCost": 0.4069045,
      "lastAPIDuration": 108608,
      "lastToolDuration": 2895,
      "lastDuration": 1986687,
      "lastLinesAdded": 134,
      "lastLinesRemoved": 1,
      "lastTotalInputTokens": 5791,
      "lastTotalOutputTokens": 5056,
      "lastTotalCacheCreationInputTokens": 13130,
      "lastTotalCacheReadInputTokens": 389534,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 4090,
          "outputTokens": 446,
          "cacheReadInputTokens": 0,
          "cacheCreationInputTokens": 0,
          "webSearchRequests": 0,
          "costUSD": 0.006319999999999999
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 1701,
          "outputTokens": 4610,
          "cacheReadInputTokens": 389534,
          "cacheCreationInputTokens": 13130,
          "webSearchRequests": 0,
          "costUSD": 0.4005845
        }
      }
    },
    "/mnt/c/python/claude-hooks-manager/worktrees/task-4-tui": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "d3974794-4abb-49b5-a3b5-4f8b50868d50",
      "lastCost": 0.9417687500000002,
      "lastAPIDuration": 182972,
      "lastToolDuration": 1750,
      "lastDuration": 3139079,
      "lastLinesAdded": 383,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 6796,
      "lastTotalOutputTokens": 10723,
      "lastTotalCacheCreationInputTokens": 42431,
      "lastTotalCacheReadInputTokens": 817848,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 5416,
          "outputTokens": 637,
          "cacheReadInputTokens": 0,
          "cacheCreationInputTokens": 0,
          "webSearchRequests": 0,
          "costUSD": 0.008601
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 1380,
          "outputTokens": 10086,
          "cacheReadInputTokens": 817848,
          "cacheCreationInputTokens": 42431,
          "webSearchRequests": 0,
          "costUSD": 0.9331677499999999
        }
      }
    },
    "/mnt/c/python/claude-hooks-manager/worktrees/task-1-core": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "f41b99ab-1f04-4eaf-a39a-7ceb6267501d",
      "lastCost": 1.51589825,
      "lastAPIDuration": 248702,
      "lastToolDuration": 5446,
      "lastDuration": 306197,
      "lastLinesAdded": 377,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 9013,
      "lastTotalOutputTokens": 13916,
      "lastTotalCacheCreationInputTokens": 97745,
      "lastTotalCacheReadInputTokens": 1118886,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 7729,
          "outputTokens": 825,
          "cacheReadInputTokens": 0,
          "cacheCreationInputTokens": 0,
          "webSearchRequests": 0,
          "costUSD": 0.011854
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 1284,
          "outputTokens": 13091,
          "cacheReadInputTokens": 1118886,
          "cacheCreationInputTokens": 97745,
          "webSearchRequests": 0,
          "costUSD": 1.50404425
        }
      }
    },
    "/mnt/c/python/claude-repo-xray": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 2,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": "dced9bb5-2cbf-4594-96a1-091fb4ed10f1",
      "lastCost": 41.50785895,
      "lastAPIDuration": 3093381,
      "lastToolDuration": 425507,
      "lastDuration": 26241708,
      "lastLinesAdded": 4015,
      "lastLinesRemoved": 1711,
      "lastTotalInputTokens": 133647,
      "lastTotalOutputTokens": 181006,
      "lastTotalCacheCreationInputTokens": 4362459,
      "lastTotalCacheReadInputTokens": 22422504,
      "lastModelUsage": {
        "claude-haiku-4-5-20251001": {
          "inputTokens": 127688,
          "outputTokens": 46128,
          "cacheReadInputTokens": 294237,
          "cacheCreationInputTokens": 122228,
          "webSearchRequests": 0,
          "costUSD": 0.5405366999999999
        },
        "claude-opus-4-5-20251101": {
          "inputTokens": 5959,
          "outputTokens": 134878,
          "cacheReadInputTokens": 22128267,
          "cacheCreationInputTokens": 4240231,
          "webSearchRequests": 0,
          "costUSD": 40.96732225
        }
      }
    },
    "/mnt/c/python/claude-code-plugin-marketplace": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": true,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claude_adversarial_tester": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    },
    "/mnt/c/python/claude_metrics": {
      "allowedTools": [],
      "hasTrustDialogAccepted": false,
      "dontCrawlDirectory": false,
      "mcpServers": {},
      "enabledMcpjsonServers": [],
      "disabledMcpjsonServers": [],
      "projectOnboardingSeenCount": 0,
      "hasCompletedProjectOnboarding": false,
      "reactVulnerabilityCache": {
        "detected": false,
        "package": null,
        "packageName": null,
        "version": null,
        "packageManager": null
      },
      "lastSessionId": null,
      "lastCost": 0,
      "lastAPIDuration": 0,
      "lastToolDuration": 0,
      "lastDuration": 0,
      "lastLinesAdded": 0,
      "lastLinesRemoved": 0,
      "lastTotalInputTokens": 0,
      "lastTotalOutputTokens": 0,
      "lastTotalCacheCreationInputTokens": 0,
      "lastTotalCacheReadInputTokens": 0,
      "lastModelUsage": {}
    }
  },
  "project_count": 55
}
```

---

## 4. Credentials

**Path:** `~/.claude/.credentials.json`

**Description:** OAuth authentication and subscription information (sensitive data redacted)

### Sample Data

```json
{
  "path": "/home/jim/.claude/.credentials.json",
  "exists": true,
  "subscription_type": "max",
  "rate_limit_tier": "default_claude_max_20x",
  "scopes": [
    "user:inference",
    "user:profile",
    "user:sessions:claude_code"
  ],
  "expires_at": 1765708953613,
  "access_token": "[REDACTED]",
  "refresh_token": "[REDACTED]",
  "has_access_token": true,
  "has_refresh_token": true
}
```

---

## 5. History

**Path:** `~/.claude/history.jsonl`

**Description:** Readline-style history of user inputs across all sessions

### Sample Data

```json
{
  "path": "/home/jim/.claude/history.jsonl",
  "total_entries": 2786,
  "extracted_entries": 2786,
  "entries": [
    {
      "timestamp": 1759026214272,
      "timestamp_iso": "2025-09-27T21:23:34.272000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 8,
      "has_pasted_contents": true,
      "display": "continue"
    },
    {
      "timestamp": 1759026244429,
      "timestamp_iso": "2025-09-27T21:24:04.429000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 8,
      "has_pasted_contents": true,
      "display": "/config "
    },
    {
      "timestamp": 1759026244438,
      "timestamp_iso": "2025-09-27T21:24:04.438000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 8,
      "has_pasted_contents": true,
      "display": "/config "
    },
    {
      "timestamp": 1759026244439,
      "timestamp_iso": "2025-09-27T21:24:04.439000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 8,
      "has_pasted_contents": true,
      "display": "/config "
    },
    {
      "timestamp": 1759027231911,
      "timestamp_iso": "2025-09-27T21:40:31.911000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 8,
      "has_pasted_contents": true,
      "display": "/doctor "
    },
    {
      "timestamp": 1759027231922,
      "timestamp_iso": "2025-09-27T21:40:31.922000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 8,
      "has_pasted_contents": true,
      "display": "/doctor "
    },
    {
      "timestamp": 1759027231923,
      "timestamp_iso": "2025-09-27T21:40:31.923000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 8,
      "has_pasted_contents": true,
      "display": "/doctor "
    },
    {
      "timestamp": 1759027246289,
      "timestamp_iso": "2025-09-27T21:40:46.289000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 10,
      "has_pasted_contents": true,
      "display": "/describe "
    },
    {
      "timestamp": 1759027246301,
      "timestamp_iso": "2025-09-27T21:40:46.301000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 10,
      "has_pasted_contents": true,
      "display": "/describe "
    },
    {
      "timestamp": 1759027311005,
      "timestamp_iso": "2025-09-27T21:41:51.005000",
      "project": "/mnt/c/python/mainframe_copilot",
      "display_length": 13,
      "has_pasted_contents": true,
      "display": "/plancompact "
    }
  ],
  "_entries_total": 2786,
  "unique_projects": [
    "/home/jim",
    "/mnt/c/python",
    "/mnt/c/python/BAR_AI",
    "/mnt/c/python/FedSpeak",
    "/mnt/c/python/Kosmos",
    "/mnt/c/python/Torn",
    "/mnt/c/python/agent-ui",
    "/mnt/c/python/claude-code-plugin-marketplace",
    "/mnt/c/python/claude-document-dependency-tracker",
    "/mnt/c/python/claude-hooks-manager"
  ],
  "_unique_projects_total": 45,
  "project_count": 45,
  "date_range": {
    "first": "2025-09-27T21:23:34.272000",
    "last": "2025-12-14T00:46:43.576000"
  }
}
```

---

## 6. Sessions

**Path:** `~/.claude/projects/*/*.jsonl`

**Description:** Complete conversation transcripts including messages, tool calls, and metadata

### Sample Data

```json
{
  "total_files": 4477,
  "extracted_sessions": 4477,
  "total_messages": 82634,
  "total_tool_calls": 23213,
  "total_input_tokens": 10308172,
  "total_output_tokens": 16005968,
  "project_count": 32,
  "sessions": [
    {
      "session_id": "agent-ba912b75",
      "project": "/mnt/c/python/gemini/cli",
      "project_dir": "-mnt-c-python-gemini-cli",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-gemini-cli/agent-ba912b75.jsonl",
      "file_size": 1410,
      "is_agent": true,
      "agent_id": "agent-ba912b75",
      "start_time": "2025-11-18T19:15:04.394Z",
      "end_time": "2025-11-18T19:15:04.394Z",
      "duration_ms": 0,
      "message_count": 1,
      "user_message_count": 0,
      "assistant_message_count": 1,
      "tool_call_count": 0,
      "total_input_tokens": 606,
      "total_output_tokens": 158,
      "total_cache_read_tokens": 0,
      "models_used": [
        "claude-haiku-4-5-20251001"
      ],
      "primary_model": "claude-haiku-4-5-20251001",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "1eba94ba-b70a-4bb2-b57a-dc66f89c5f29",
          "parent_uuid": null,
          "session_id": "agent-ba912b75",
          "timestamp": "2025-11-18T19:15:04.394Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 606,
          "output_tokens": 158,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        }
      ],
      "tool_calls": []
    },
    {
      "session_id": "82a0d6c9-4f00-4912-abe3-0dfacc4e1097",
      "project": "/mnt/c/python/gemini/cli",
      "project_dir": "-mnt-c-python-gemini-cli",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-gemini-cli/82a0d6c9-4f00-4912-abe3-0dfacc4e1097.jsonl",
      "file_size": 0,
      "is_agent": false,
      "agent_id": null,
      "start_time": null,
      "end_time": null,
      "duration_ms": null,
      "message_count": 0,
      "user_message_count": 0,
      "assistant_message_count": 0,
      "tool_call_count": 0,
      "total_input_tokens": 0,
      "total_output_tokens": 0,
      "total_cache_read_tokens": 0,
      "models_used": [],
      "primary_model": null,
      "cost_usd": 0.0,
      "messages": [],
      "tool_calls": []
    },
    {
      "session_id": "agent-adb692e",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-adb692e.jsonl",
      "file_size": 142454,
      "is_agent": true,
      "agent_id": "agent-adb692e",
      "start_time": "2025-12-12T20:39:33.432Z",
      "end_time": "2025-12-12T20:40:14.253Z",
      "duration_ms": 40821,
      "message_count": 34,
      "user_message_count": 14,
      "assistant_message_count": 20,
      "tool_call_count": 13,
      "total_input_tokens": 10490,
      "total_output_tokens": 920,
      "total_cache_read_tokens": 236572,
      "models_used": [
        "claude-haiku-4-5-20251001"
      ],
      "primary_model": "claude-haiku-4-5-20251001",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "3014dd2e-5612-49fc-8906-de538693849c",
          "parent_uuid": null,
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:33.432Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "ff24250b-4e89-4c08-8505-97101333c85d",
          "parent_uuid": "3014dd2e-5612-49fc-8906-de538693849c",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:35.657Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 674,
          "tool_call_count": 0
        },
        {
          "uuid": "f29dde10-37ac-4452-9911-352471e76ecf",
          "parent_uuid": "ff24250b-4e89-4c08-8505-97101333c85d",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:36.080Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "bc25ac6e-8b11-44b1-a929-04e2cd759cff",
          "parent_uuid": "f29dde10-37ac-4452-9911-352471e76ecf",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:36.331Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "c598ac09-2d32-4743-adfa-85fc5d771d80",
          "parent_uuid": "bc25ac6e-8b11-44b1-a929-04e2cd759cff",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:36.747Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "3355d121-6250-48d9-a7a0-1b959302e956",
          "parent_uuid": "c598ac09-2d32-4743-adfa-85fc5d771d80",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:37.037Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 564,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "ad5a7492-d91e-4bcc-84cd-572521ed31a9",
          "parent_uuid": "3355d121-6250-48d9-a7a0-1b959302e956",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:37.260Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "9f2bbfaa-9e03-4445-9f84-ccdebdf44f10",
          "parent_uuid": "ad5a7492-d91e-4bcc-84cd-572521ed31a9",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:37.264Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "30b76b1a-e39c-4377-88bd-1fffd50871cc",
          "parent_uuid": "9f2bbfaa-9e03-4445-9f84-ccdebdf44f10",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:37.287Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "b81c2473-3b4f-4fad-b721-c721685e22c6",
          "parent_uuid": "30b76b1a-e39c-4377-88bd-1fffd50871cc",
          "session_id": "agent-adb692e",
          "timestamp": "2025-12-12T20:39:37.396Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        }
      ],
      "_messages_total": 34,
      "tool_calls": [
        {
          "id": "toolu_01H76ykEFeah4RKfXMcoqPrA",
          "tool_name": "Bash",
          "message_uuid": "f29dde10-37ac-4452-9911-352471e76ecf",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01NL2bNy45keyBkE3LNnJZCV",
          "tool_name": "Bash",
          "message_uuid": "bc25ac6e-8b11-44b1-a929-04e2cd759cff",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01J3ySawP6ZVuR9LBFq55CiM",
          "tool_name": "Bash",
          "message_uuid": "c598ac09-2d32-4743-adfa-85fc5d771d80",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01V8zgWiDNavZScG9tt3hSTP",
          "tool_name": "Bash",
          "message_uuid": "3355d121-6250-48d9-a7a0-1b959302e956",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01CVFQqyoR6KcrzsYnqSzZCa",
          "tool_name": "Bash",
          "message_uuid": "84d92288-b786-45ab-91ed-2986e37bea8f",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01BrEfqT1XscMHXWFp1ewoie",
          "tool_name": "Bash",
          "message_uuid": "1d099b56-efff-4efb-a64a-1eddbe7fe069",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01FyyL4faAXJx8dvE9NfMjNP",
          "tool_name": "Bash",
          "message_uuid": "9ad823bf-9359-47e8-84f2-7304c3b50167",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01YJ1yAgrddrKTyvumzUpUKV",
          "tool_name": "Bash",
          "message_uuid": "d0b87003-bab7-4d9e-beb0-8fd8244aaf04",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01WhxPkEkEY4iY9yuETtYC8r",
          "tool_name": "Bash",
          "message_uuid": "2057ec1b-de05-433f-a7b9-c5b4250699f7",
          "session_id": "agent-adb692e"
        },
        {
          "id": "toolu_01QyjRT6gqZUXrrHR5Xa7VZd",
          "tool_name": "Bash",
          "message_uuid": "e3d7b347-1534-4ae9-8435-1e75997f25d1",
          "session_id": "agent-adb692e"
        }
      ],
      "_tool_calls_total": 13
    },
    {
      "session_id": "agent-a3bad14",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-a3bad14.jsonl",
      "file_size": 330336,
      "is_agent": true,
      "agent_id": "agent-a3bad14",
      "start_time": "2025-12-13T22:13:55.993Z",
      "end_time": "2025-12-13T22:15:19.992Z",
      "duration_ms": 83999,
      "message_count": 17,
      "user_message_count": 7,
      "assistant_message_count": 10,
      "tool_call_count": 6,
      "total_input_tokens": 108,
      "total_output_tokens": 4228,
      "total_cache_read_tokens": 22978,
      "models_used": [
        "claude-haiku-4-5-20251001"
      ],
      "primary_model": "claude-haiku-4-5-20251001",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "fd89308b-f1fd-4519-8837-52bf1bbc77c3",
          "parent_uuid": null,
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:13:55.993Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "8a3ed29d-309f-4155-880f-e7d5ab236914",
          "parent_uuid": "fd89308b-f1fd-4519-8837-52bf1bbc77c3",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:00.609Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 1,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 946,
          "tool_call_count": 0
        },
        {
          "uuid": "19bba61f-e60b-4e6b-98b6-a8d5da711633",
          "parent_uuid": "8a3ed29d-309f-4155-880f-e7d5ab236914",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:01.168Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 1,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "de6fcb4a-2ccc-4f29-8e1e-03c83590a0fb",
          "parent_uuid": "19bba61f-e60b-4e6b-98b6-a8d5da711633",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:01.774Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 704,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "2c032042-ff0f-47d9-be52-9fc10af26667",
          "parent_uuid": "de6fcb4a-2ccc-4f29-8e1e-03c83590a0fb",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:02.952Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 704,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "745f4a55-f01b-4d54-b191-f6154db3eb90",
          "parent_uuid": "2c032042-ff0f-47d9-be52-9fc10af26667",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:03.534Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 704,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "c3b2ae34-84e0-4cd3-8b9e-5ef7f1198125",
          "parent_uuid": "745f4a55-f01b-4d54-b191-f6154db3eb90",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:04.097Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 704,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "9aa7176f-b3d4-4c0d-a901-98b28054953b",
          "parent_uuid": "c3b2ae34-84e0-4cd3-8b9e-5ef7f1198125",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:04.658Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 704,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "ea5a3f6d-d1c7-421f-9dae-5591c398e5f4",
          "parent_uuid": "9aa7176f-b3d4-4c0d-a901-98b28054953b",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:05.276Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 704,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "7c774cc4-b9b0-49bc-9389-0613a0cbcb5a",
          "parent_uuid": "ea5a3f6d-d1c7-421f-9dae-5591c398e5f4",
          "session_id": "agent-a3bad14",
          "timestamp": "2025-12-13T22:14:09.689Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        }
      ],
      "_messages_total": 17,
      "tool_calls": [
        {
          "id": "toolu_012TeXukAaYFMhYUg77pWHxk",
          "tool_name": "Read",
          "message_uuid": "de6fcb4a-2ccc-4f29-8e1e-03c83590a0fb",
          "session_id": "agent-a3bad14"
        },
        {
          "id": "toolu_01TQ43piaMhoKsoyipsuGgj6",
          "tool_name": "Read",
          "message_uuid": "2c032042-ff0f-47d9-be52-9fc10af26667",
          "session_id": "agent-a3bad14"
        },
        {
          "id": "toolu_01HjBtBbujpqb8ySvDg5edvE",
          "tool_name": "Read",
          "message_uuid": "745f4a55-f01b-4d54-b191-f6154db3eb90",
          "session_id": "agent-a3bad14"
        },
        {
          "id": "toolu_01QVjqtPDBCT14PH34qSnTTK",
          "tool_name": "Read",
          "message_uuid": "c3b2ae34-84e0-4cd3-8b9e-5ef7f1198125",
          "session_id": "agent-a3bad14"
        },
        {
          "id": "toolu_01E2jYg3GxVmLRex489xe6Zh",
          "tool_name": "Read",
          "message_uuid": "9aa7176f-b3d4-4c0d-a901-98b28054953b",
          "session_id": "agent-a3bad14"
        },
        {
          "id": "toolu_01GHVnNnco2V64sw5TNz7adu",
          "tool_name": "Read",
          "message_uuid": "ea5a3f6d-d1c7-421f-9dae-5591c398e5f4",
          "session_id": "agent-a3bad14"
        }
      ]
    },
    {
      "session_id": "agent-aab4342",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-aab4342.jsonl",
      "file_size": 53133,
      "is_agent": true,
      "agent_id": "agent-aab4342",
      "start_time": "2025-12-12T18:27:20.316Z",
      "end_time": "2025-12-12T18:27:49.915Z",
      "duration_ms": 29599,
      "message_count": 36,
      "user_message_count": 14,
      "assistant_message_count": 22,
      "tool_call_count": 13,
      "total_input_tokens": 2290,
      "total_output_tokens": 694,
      "total_cache_read_tokens": 235007,
      "models_used": [
        "claude-haiku-4-5-20251001"
      ],
      "primary_model": "claude-haiku-4-5-20251001",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "f23966b7-697d-4e20-b021-b78dc05c4b03",
          "parent_uuid": null,
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:20.316Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "08c53787-cbb8-4fa4-9f63-8e512d487c4d",
          "parent_uuid": "f23966b7-697d-4e20-b021-b78dc05c4b03",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:22.729Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 674,
          "tool_call_count": 0
        },
        {
          "uuid": "b6fce6e2-c737-47a4-a17f-ea159ec52185",
          "parent_uuid": "08c53787-cbb8-4fa4-9f63-8e512d487c4d",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:23.022Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "7da9bd2b-ff2a-449a-9442-f90dd8d5925a",
          "parent_uuid": "b6fce6e2-c737-47a4-a17f-ea159ec52185",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:23.356Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "99e5c46e-6a87-403d-a6f4-4dc4c530e2db",
          "parent_uuid": "7da9bd2b-ff2a-449a-9442-f90dd8d5925a",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:23.693Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 387,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "cb76e698-41af-466f-9a32-1d11e7518fad",
          "parent_uuid": "99e5c46e-6a87-403d-a6f4-4dc4c530e2db",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:23.907Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "bc18a812-6518-4aed-b73a-39b8f60b907a",
          "parent_uuid": "cb76e698-41af-466f-9a32-1d11e7518fad",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:23.978Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "08c9aa44-5b6f-4c46-a1be-2bf752783871",
          "parent_uuid": "bc18a812-6518-4aed-b73a-39b8f60b907a",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:25.639Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 239,
          "output_tokens": 1,
          "cache_read_tokens": 10950,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 190,
          "tool_call_count": 0
        },
        {
          "uuid": "b638cf4f-6f64-4e78-9238-232a58488dd6",
          "parent_uuid": "08c9aa44-5b6f-4c46-a1be-2bf752783871",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:25.805Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 239,
          "output_tokens": 1,
          "cache_read_tokens": 10950,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "2405a807-026a-4f40-96f1-7cc3db75389f",
          "parent_uuid": "b638cf4f-6f64-4e78-9238-232a58488dd6",
          "session_id": "agent-aab4342",
          "timestamp": "2025-12-12T18:27:26.201Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 239,
          "output_tokens": 1,
          "cache_read_tokens": 10950,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        }
      ],
      "_messages_total": 36,
      "tool_calls": [
        {
          "id": "toolu_01RAjFQsLRLLkX9Zq7xxijio",
          "tool_name": "Bash",
          "message_uuid": "7da9bd2b-ff2a-449a-9442-f90dd8d5925a",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_01HkZ2Q5oydkwAw6WkFFWTgA",
          "tool_name": "Bash",
          "message_uuid": "99e5c46e-6a87-403d-a6f4-4dc4c530e2db",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_01V2pPbJAQ6HPF6zJahWiUFK",
          "tool_name": "Bash",
          "message_uuid": "2405a807-026a-4f40-96f1-7cc3db75389f",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_01HxA1LySgNiCBno8F35JxDD",
          "tool_name": "Bash",
          "message_uuid": "14519d01-239e-4efe-b2af-db8cb57186c4",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_01CDV751chB2eTZq6n4NycBL",
          "tool_name": "Bash",
          "message_uuid": "950d39c3-a05d-4c5e-a24e-92d9203e1127",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_01N7VVhBx6M4Z76JcxM2abwt",
          "tool_name": "Bash",
          "message_uuid": "cfe2781b-bc5d-4168-894c-e2019385d310",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_01KJzmwaTW21tu3mh5YToSVT",
          "tool_name": "Bash",
          "message_uuid": "9420e9d7-488e-49fa-bf97-5548313170fb",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_01JQDRpdEDh2aicwDLTDLeyo",
          "tool_name": "Bash",
          "message_uuid": "604e4c2f-eafb-4ca3-8e20-2b5424fd6717",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_015soQNeGaeLnLoM8gaZ5AgB",
          "tool_name": "Bash",
          "message_uuid": "764e5ecb-4ed5-4419-827c-d5af3fe69148",
          "session_id": "agent-aab4342"
        },
        {
          "id": "toolu_014jwHeDXzmo1GWHYQyKdA4c",
          "tool_name": "Bash",
          "message_uuid": "95abe491-8d59-424f-a21d-9743597e0096",
          "session_id": "agent-aab4342"
        }
      ],
      "_tool_calls_total": 13
    },
    {
      "session_id": "agent-a3c3057",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-a3c3057.jsonl",
      "file_size": 3265,
      "is_agent": true,
      "agent_id": "agent-a3c3057",
      "start_time": "2025-12-13T01:04:06.965Z",
      "end_time": "2025-12-13T01:04:11.710Z",
      "duration_ms": 4745,
      "message_count": 3,
      "user_message_count": 1,
      "assistant_message_count": 2,
      "tool_call_count": 0,
      "total_input_tokens": 2122,
      "total_output_tokens": 167,
      "total_cache_read_tokens": 0,
      "models_used": [
        "claude-opus-4-5-20251101"
      ],
      "primary_model": "claude-opus-4-5-20251101",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "ec419017-6490-4762-8791-d8f6466dddb6",
          "parent_uuid": null,
          "session_id": "agent-a3c3057",
          "timestamp": "2025-12-13T01:04:06.965Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "4d4d737f-ca7a-4df8-947c-f96ed4dc276e",
          "parent_uuid": "ec419017-6490-4762-8791-d8f6466dddb6",
          "session_id": "agent-a3c3057",
          "timestamp": "2025-12-13T01:04:09.756Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-opus-4-5-20251101",
          "input_tokens": 1061,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 259,
          "tool_call_count": 0
        },
        {
          "uuid": "a1854786-abb8-4f82-a8dc-e34ac82da0ee",
          "parent_uuid": "4d4d737f-ca7a-4df8-947c-f96ed4dc276e",
          "session_id": "agent-a3c3057",
          "timestamp": "2025-12-13T01:04:11.710Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-opus-4-5-20251101",
          "input_tokens": 1061,
          "output_tokens": 164,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        }
      ],
      "tool_calls": []
    },
    {
      "session_id": "agent-a103bea",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-a103bea.jsonl",
      "file_size": 3149,
      "is_agent": true,
      "agent_id": "agent-a103bea",
      "start_time": "2025-12-12T17:46:34.422Z",
      "end_time": "2025-12-12T17:46:40.642Z",
      "duration_ms": 6220,
      "message_count": 3,
      "user_message_count": 1,
      "assistant_message_count": 2,
      "tool_call_count": 0,
      "total_input_tokens": 1808,
      "total_output_tokens": 6,
      "total_cache_read_tokens": 0,
      "models_used": [
        "claude-opus-4-5-20251101"
      ],
      "primary_model": "claude-opus-4-5-20251101",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "bd45f299-afd3-4955-b936-625931371da6",
          "parent_uuid": null,
          "session_id": "agent-a103bea",
          "timestamp": "2025-12-12T17:46:34.422Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "36cd8466-9d64-4184-9b89-51c80b1b51cf",
          "parent_uuid": "bd45f299-afd3-4955-b936-625931371da6",
          "session_id": "agent-a103bea",
          "timestamp": "2025-12-12T17:46:37.625Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-opus-4-5-20251101",
          "input_tokens": 904,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 156,
          "tool_call_count": 0
        },
        {
          "uuid": "d17c54c5-2588-459f-8452-ef0191e67d49",
          "parent_uuid": "36cd8466-9d64-4184-9b89-51c80b1b51cf",
          "session_id": "agent-a103bea",
          "timestamp": "2025-12-12T17:46:40.642Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-opus-4-5-20251101",
          "input_tokens": 904,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        }
      ],
      "tool_calls": []
    },
    {
      "session_id": "agent-a6490e7",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-a6490e7.jsonl",
      "file_size": 3434,
      "is_agent": true,
      "agent_id": "agent-a6490e7",
      "start_time": "2025-12-12T17:46:34.418Z",
      "end_time": "2025-12-12T17:46:37.417Z",
      "duration_ms": 2999,
      "message_count": 3,
      "user_message_count": 1,
      "assistant_message_count": 2,
      "tool_call_count": 0,
      "total_input_tokens": 1552,
      "total_output_tokens": 6,
      "total_cache_read_tokens": 0,
      "models_used": [
        "claude-haiku-4-5-20251001"
      ],
      "primary_model": "claude-haiku-4-5-20251001",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "ffbe9dda-76ef-433d-8c5d-ea5f06bd670e",
          "parent_uuid": null,
          "session_id": "agent-a6490e7",
          "timestamp": "2025-12-12T17:46:34.418Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "9ba226f2-c096-4188-981e-e561d838748b",
          "parent_uuid": "ffbe9dda-76ef-433d-8c5d-ea5f06bd670e",
          "session_id": "agent-a6490e7",
          "timestamp": "2025-12-12T17:46:36.615Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 776,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 304,
          "tool_call_count": 0
        },
        {
          "uuid": "f0b37946-e6d1-49ad-a342-53ed5694fdd9",
          "parent_uuid": "9ba226f2-c096-4188-981e-e561d838748b",
          "session_id": "agent-a6490e7",
          "timestamp": "2025-12-12T17:46:37.417Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 776,
          "output_tokens": 3,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        }
      ],
      "tool_calls": []
    },
    {
      "session_id": "agent-ac63a26",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-ac63a26.jsonl",
      "file_size": 188188,
      "is_agent": true,
      "agent_id": "agent-ac63a26",
      "start_time": "2025-12-12T18:27:20.318Z",
      "end_time": "2025-12-12T18:28:11.560Z",
      "duration_ms": 51242,
      "message_count": 44,
      "user_message_count": 16,
      "assistant_message_count": 28,
      "tool_call_count": 15,
      "total_input_tokens": 1712,
      "total_output_tokens": 3789,
      "total_cache_read_tokens": 468126,
      "models_used": [
        "claude-haiku-4-5-20251001"
      ],
      "primary_model": "claude-haiku-4-5-20251001",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "c5d0ebbd-e9a7-43e2-a9bd-9242df33a32a",
          "parent_uuid": null,
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:20.318Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "b97afe6b-225d-4208-a99d-d613699f9758",
          "parent_uuid": "c5d0ebbd-e9a7-43e2-a9bd-9242df33a32a",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:21.948Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 1,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 551,
          "tool_call_count": 0
        },
        {
          "uuid": "015550f0-6556-4ff7-8b54-7c6c2db0d987",
          "parent_uuid": "b97afe6b-225d-4208-a99d-d613699f9758",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:22.197Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 1,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "f5bb4ad2-e9e5-45d6-86ca-05e50d557131",
          "parent_uuid": "015550f0-6556-4ff7-8b54-7c6c2db0d987",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:22.533Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 1,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "99203a6c-44c8-4099-baae-707d9dad36d1",
          "parent_uuid": "f5bb4ad2-e9e5-45d6-86ca-05e50d557131",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:22.821Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 9,
          "output_tokens": 1,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "bdcc12fa-f742-44c2-8cf4-2910501a9a35",
          "parent_uuid": "99203a6c-44c8-4099-baae-707d9dad36d1",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:23.072Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "f284b10e-b304-436c-85ef-72e75936164d",
          "parent_uuid": "bdcc12fa-f742-44c2-8cf4-2910501a9a35",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:23.172Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "b369fc4f-e0dd-464e-a0bb-b33c27f222cd",
          "parent_uuid": "f284b10e-b304-436c-85ef-72e75936164d",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:25.443Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 239,
          "output_tokens": 1,
          "cache_read_tokens": 10985,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 231,
          "tool_call_count": 0
        },
        {
          "uuid": "3269df78-07ca-47f5-9dd7-cc1e3794cb3d",
          "parent_uuid": "b369fc4f-e0dd-464e-a0bb-b33c27f222cd",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:25.739Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 239,
          "output_tokens": 1,
          "cache_read_tokens": 10985,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "62f9ae09-a1e8-4a1c-9212-db9b9ca65eac",
          "parent_uuid": "3269df78-07ca-47f5-9dd7-cc1e3794cb3d",
          "session_id": "agent-ac63a26",
          "timestamp": "2025-12-12T18:27:26.021Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 239,
          "output_tokens": 1,
          "cache_read_tokens": 10985,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        }
      ],
      "_messages_total": 44,
      "tool_calls": [
        {
          "id": "toolu_012x2fhETLKjTgQKpaHcffSd",
          "tool_name": "Bash",
          "message_uuid": "f5bb4ad2-e9e5-45d6-86ca-05e50d557131",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_017LAqhANQmRrHgkmpdG2Lm8",
          "tool_name": "Bash",
          "message_uuid": "99203a6c-44c8-4099-baae-707d9dad36d1",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_01BdjUuj7nAZeiwJEXSUWhyz",
          "tool_name": "Bash",
          "message_uuid": "3269df78-07ca-47f5-9dd7-cc1e3794cb3d",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_014G6zZszWXxkYZa2SuJoAZq",
          "tool_name": "Bash",
          "message_uuid": "62f9ae09-a1e8-4a1c-9212-db9b9ca65eac",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_015seFBB9CU1fSDLVyRq2MHb",
          "tool_name": "Read",
          "message_uuid": "6f27fb00-c353-41f2-9d29-4a1586c45183",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_012j5bRA3JL5Fkq7q7Y3K1Wg",
          "tool_name": "Read",
          "message_uuid": "cc563104-d047-4a26-8c9b-2aaba60b7d89",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_017m29L8GjywxezihDyRMqVP",
          "tool_name": "Read",
          "message_uuid": "69815fd2-0504-4eba-843c-79d7f6fe79bd",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_01RKX36xStZ3nZdxxoQMyRKc",
          "tool_name": "Read",
          "message_uuid": "8187f730-5ba0-4c55-a11d-7325f88708e4",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_018twvyYR5bS4gc386wBkDmg",
          "tool_name": "Read",
          "message_uuid": "764caf6c-f997-47ae-8a98-5ec35e5494d4",
          "session_id": "agent-ac63a26"
        },
        {
          "id": "toolu_014dNQesev1ypPUJoAzYNAp7",
          "tool_name": "Read",
          "message_uuid": "a3ff2b96-55aa-4122-bac3-39f889ea872a",
          "session_id": "agent-ac63a26"
        }
      ],
      "_tool_calls_total": 15
    },
    {
      "session_id": "agent-a6a49bc",
      "project": "/mnt/c/python/claude/repo/xray",
      "project_dir": "-mnt-c-python-claude-repo-xray",
      "file_path": "/home/jim/.claude/projects/-mnt-c-python-claude-repo-xray/agent-a6a49bc.jsonl",
      "file_size": 268878,
      "is_agent": true,
      "agent_id": "agent-a6a49bc",
      "start_time": "2025-12-13T22:13:55.995Z",
      "end_time": "2025-12-13T22:15:19.990Z",
      "duration_ms": 83995,
      "message_count": 9,
      "user_message_count": 3,
      "assistant_message_count": 6,
      "tool_call_count": 2,
      "total_input_tokens": 39466,
      "total_output_tokens": 9381,
      "total_cache_read_tokens": 22742,
      "models_used": [
        "claude-haiku-4-5-20251001"
      ],
      "primary_model": "claude-haiku-4-5-20251001",
      "cost_usd": 0.0,
      "messages": [
        {
          "uuid": "5d9d7133-b23d-47da-97e7-ab5b665f232f",
          "parent_uuid": null,
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:13:55.995Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "82ef3317-32c6-45f4-94f1-c9b4c8027a21",
          "parent_uuid": "5d9d7133-b23d-47da-97e7-ab5b665f232f",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:14:00.021Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 8,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 655,
          "tool_call_count": 0
        },
        {
          "uuid": "dea03e36-6cac-409d-91e2-6db50233171d",
          "parent_uuid": "82ef3317-32c6-45f4-94f1-c9b4c8027a21",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:14:00.598Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 351,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "1e78dd81-559c-4134-a3ac-f6ad5f99cd83",
          "parent_uuid": "dea03e36-6cac-409d-91e2-6db50233171d",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:14:01.159Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 351,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "8f3a4843-7028-4184-a66c-b5689bead0d5",
          "parent_uuid": "1e78dd81-559c-4134-a3ac-f6ad5f99cd83",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:14:01.190Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 10,
          "output_tokens": 351,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 1
        },
        {
          "uuid": "db0c3f9b-cda7-49ea-ab7b-70afe79beac8",
          "parent_uuid": "8f3a4843-7028-4184-a66c-b5689bead0d5",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:14:06.541Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "cc17866c-581d-47ea-9788-f154f5601df5",
          "parent_uuid": "db0c3f9b-cda7-49ea-ab7b-70afe79beac8",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:14:06.544Z",
          "type": "user",
          "role": "user",
          "model": null,
          "input_tokens": 0,
          "output_tokens": 0,
          "cache_read_tokens": 0,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        },
        {
          "uuid": "cb6e991d-c30e-420a-b696-6870da86913c",
          "parent_uuid": "cc17866c-581d-47ea-9788-f154f5601df5",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:14:41.945Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 19713,
          "output_tokens": 1,
          "cache_read_tokens": 11371,
          "cost_usd": 0,
          "has_thinking": true,
          "thinking_length": 6221,
          "tool_call_count": 0
        },
        {
          "uuid": "ef82a323-40d2-42dc-934d-5a06eb02182e",
          "parent_uuid": "cb6e991d-c30e-420a-b696-6870da86913c",
          "session_id": "agent-a6a49bc",
          "timestamp": "2025-12-13T22:15:19.990Z",
          "type": "assistant",
          "role": "assistant",
          "model": "claude-haiku-4-5-20251001",
          "input_tokens": 19713,
          "output_tokens": 8319,
          "cache_read_tokens": 11371,
          "cost_usd": 0,
          "has_thinking": false,
          "thinking_length": 0,
          "tool_call_count": 0
        }
      ],
      "tool_calls": [
        {
          "id": "toolu_0179bhdojT13U1JGQg9NFGyN",
          "tool_name": "Read",
          "message_uuid": "1e78dd81-559c-4134-a3ac-f6ad5f99cd83",
          "session_id": "agent-a6a49bc"
        },
        {
          "id": "toolu_01XYNiRP2ESJN7Ft6aYbfEdc",
          "tool_name": "Read",
          "message_uuid": "8f3a4843-7028-4184-a66c-b5689bead0d5",
          "session_id": "agent-a6a49bc"
        }
      ]
    }
  ],
  "_sessions_total": 4477,
  "by_project": {
    "/mnt/c/python/gemini/cli": [
      "agent-ba912b75",
      "82a0d6c9-4f00-4912-abe3-0dfacc4e1097"
    ],
    "/mnt/c/python/claude/repo/xray": [
      "agent-adb692e",
      "agent-a3bad14",
      "agent-aab4342",
      "agent-a3c3057",
      "agent-a103bea",
      "agent-a6490e7",
      "agent-ac63a26",
      "agent-a6a49bc",
      "agent-abf37b0",
      "agent-a5b47f7"
    ],
    "_/mnt/c/python/claude/repo/xray_total": 14,
    "/mnt/c/python/claude/metrics": [
      "agent-ac0cd1d",
      "agent-a2c1e8e",
      "agent-a224d7c",
      "agent-a13835e",
      "agent-a8499c4",
      "agent-a24a9f7",
      "24190deb-471d-413c-a185-ba048413da7c",
      "agent-aab66cc"
    ],
    "/mnt/c/python/column/mapper": [
      "agent-43c4500e",
      "agent-8c7f2df8",
      "5a7bd008-1149-444b-b6b3-5a241a98057a",
      "agent-2492ad60"
    ],
    "/mnt/c/python/claudecode/swebench": [
      "agent-243aadff",
      "agent-ed3ed422",
      "6f62e28b-2cbc-40b1-b1b2-2b420bc496f8",
      "agent-03b8e252",
      "agent-a7ae14b2",
      "6edfe635-6bb2-4ac6-87d5-6ee94ffaf4c8"
    ],
    "/mnt/c/python/claude/hooks/manager/worktrees/task/1/core": [
      "agent-a4a831b",
      "agent-a4f88f1",
      "f41b99ab-1f04-4eaf-a39a-7ceb6267501d"
    ],
    "/mnt/c/python/onefilellm": [
      "5095cd99-da0c-44b9-bde2-3201336e8470",
      "agent-80ba354f",
      "agent-3a44d0c9",
      "agent-01ca4a08",
      "agent-5c0334d4",
      "agent-11275393",
      "agent-11e9e63c",
      "7a951406-d7d1-4572-92bc-5b443aeca741",
      "a8a046f6-f3ae-46bc-b5e0-2befefef11cc",
      "agent-33b356fc"
    ],
    "_/mnt/c/python/onefilellm_total": 12,
    "/mnt/c/python": [
      "agent-a99165e",
      "agent-a6a3d05",
      "agent-a11e96f",
      "agent-ada1e7f",
      "0bbfa92c-3595-429e-bd92-da3af5fb060b",
      "agent-a14cde7",
      "agent-aaf8951",
      "agent-a5f5994",
      "agent-a1c9683",
      "335f8a35-9a1c-42f3-858a-5eb62a0748be"
    ],
    "_/mnt/c/python_total": 14,
    "/mnt/c/python/data/formulator/claude/code/proxy": [
      "cbac83be-cd7d-4ab3-b3d3-0a68806f85d9",
      "e37f41c7-8ce3-43c2-a89c-adf5ece7dcac",
      "33ec1846-22d7-42e0-942f-b6c62228a149",
      "agent-5e15b754",
      "agent-99483960",
      "agent-9b20b95f",
      "agent-c9ef7ae6",
      "agent-1f024de0",
      "agent-a3965226",
      "agent-ee3f18b1"
    ],
    "_/mnt/c/python/data/formulator/claude/code/proxy_total": 31,
    "/mnt/c/python/gigamoon": [
      "agent-1e02e08b",
      "agent-7f645018",
      "e61da86f-bae2-45d0-b456-e32f8ec0d95c"
    ],
    "/mnt/c/python/judgment/import": [
      "agent-a65b61a",
      "agent-5cc6b6b3",
      "60c8284e-092d-41c7-ae2d-654be4bacde3",
      "87a30258-cdf8-41d3-8a1a-31207af748e4",
      "3d922612-507d-4a6b-9a68-c772ac8824a2",
      "agent-cef35b1d",
      "agent-b531e0be",
      "agent-7a75dff9",
      "agent-ad827ec",
      "agent-fb6bccdf"
    ],
    "/mnt/c/python/Kosmos": [
      "agent-e5c0430c",
      "agent-8ab2a960",
      "agent-c4e3add3",
      "agent-07f3258a",
      "75fda0ff-60da-42a2-ae51-d077f9081fab",
      "agent-48286496",
      "04f9cd7b-0c2a-43d8-a91e-338c19d399fa",
      "agent-db6dc94c",
      "5b242a6f-75e4-4d15-b669-2f8667a32720",
      "agent-16de3a4e"
    ],
    "_/mnt/c/python/Kosmos_total": 233,
    "/mnt/c/python/local/model": [
      "agent-d767ead5",
      "agent-563e85c4",
      "agent-5a314f16",
      "44cf592f-efa3-44cd-82cd-7854f2e4147e",
      "45d11933-82ae-48df-9727-4543695c884f",
      "agent-784a6a1d",
      "agent-599a0f94",
      "agent-38c0a1ad"
    ],
    "/mnt/c/python/kosmos": [
      "agent-e6cef621",
      "21c10e5b-1ff7-4dc4-b91a-367023ac6a9b",
      "agent-4b67af01",
      "agent-1429e6db",
      "agent-4222571e",
      "agent-b06a6c1b",
      "76dbc95e-6f5e-488e-a901-7a869e6f979f",
      "agent-097711ce",
      "agent-507e0517",
      "agent-0acb71a7"
    ],
    "_/mnt/c/python/kosmos_total": 144,
    "/mnt/c/python/claude/hooks/manager/worktrees/task/1/scanner/terminal": [
      "de2ccaa7-06eb-420d-b3f6-5fa87dd2f47b",
      "agent-a6cc044",
      "0aa7bc63-8767-475f-9317-747fc30f6124",
      "agent-a585853",
      "agent-a29c9ac",
      "agent-a991046"
    ],
    "/mnt/c/python/outlook/mcp": [
      "4e3abece-15b9-4313-b06a-b8bb49b899a9",
      "agent-9258bdd6",
      "agent-9563a429",
      "agent-1f81c2fe",
      "agent-eb52c989",
      "7b98234c-b8a3-4773-af6e-279c0145fb7c"
    ],
    "/mnt/c/python/claude/hooks/manager/worktrees/task/2/html": [
      "agent-a4435cc",
      "agent-ae91df2",
      "agent-acf7718",
      "agent-a6f9732",
      "agent-a8e089c",
      "23bd7690-8ea1-47d0-9ddf-4de9ea878525",
      "115e24a7-d7d9-40fb-b25b-a537c66aa440",
      "9cd002dd-35f6-415a-8b48-7ca3ef39e371",
      "agent-aba9861"
    ],
    "/mnt/c/python/llm/mastermind/benchmark": [
      "agent-bb1e53b3",
      "agent-bbe9e0e7",
      "d7caaea7-1a35-4cc0-b2db-22ec7c643286",
      "23519825-2175-42d5-9776-004838c37e31",
      "381976a7-db06-46d7-a55d-502f680f5104",
      "agent-d278ecca",
      "agent-d5351520",
      "901c0a3c-18e3-470e-9c2f-b562782ea3cc",
      "agent-df1f73fd",
      "bb0841dd-a653-486f-b1e5-c9773561af93"
    ],
    "_/mnt/c/python/llm/mastermind/benchmark_total": 3692,
    "/mnt/c/python/claude/hooks/manager": [
      "agent-a27b7ab",
      "agent-a88a41d",
      "agent-a54d943",
      "7d5732c3-d7a1-4f97-b17d-f2239f3472d4",
      "53d4e423-809b-4ba3-ad1c-b0e047171b3f",
      "e122f003-0df4-4c8a-832f-fe4df8300d3f",
      "agent-a36d63b",
      "agent-af45ef0",
      "agent-af1e9a0",
      "agent-ad3d968"
    ],
    "_/mnt/c/python/claude/hooks/manager_total": 54,
    "/mnt/c/python/security/questionnaire": [
      "a46eeb19-cf06-42ca-a2fc-a8071bf72d45",
      "a8d36c80-5060-4c87-b34f-a245d0d91a01",
      "91858e7d-b904-42d9-8c12-45752493fa37",
      "agent-5524d464",
      "8319d031-a885-4313-9e86-e33b74da4166",
      "agent-a88c738b",
      "agent-ae891bc",
      "c7c2a55d-a451-45ef-960b-3df6d8d77cc3",
      "cac7077b-7d9d-40a9-a59b-b0821ba3619a",
      "agent-3a208ddd"
    ],
    "_/mnt/c/python/security/questionnaire_total": 64,
    "/mnt/c/python/claude/code/plugin/marketplace": [
      "c0db16bd-062f-49d8-b5ab-abc789e6062b",
      "agent-ae43220",
      "agent-ac25f01",
      "5722316d-7dd4-45a3-9656-e9da966b7b1a",
      "agent-a553210",
      "agent-ac1631f"
    ],
    "/mnt/c/python/kosmos/research/R/D": [
      "agent-6966b331",
      "agent-658d36ef",
      "agent-b1cea798",
      "61bdf30a-b056-44a1-8f0f-a768d535e7ed"
    ],
    "/mnt/c/python/cp/reporting": [
      "b87cd330-53f9-4817-b180-89d726d98320",
      "agent-49825482",
      "ee1fd636-a79e-45cc-8ffb-cdc78ae29d27",
      "agent-1197e238",
      "agent-343420d4",
      "agent-2fc12835",
      "agent-86d132c5",
      "agent-4548f5b5",
      "6a4d68bc-0660-4a18-9467-3db3cb20c4c9",
      "agent-a8512f5"
    ],
    "_/mnt/c/python/cp/reporting_total": 27,
    "/mnt/c/python/data/formulator": [
      "3a831b68-e581-4a3b-8f64-2f6856b9402b",
      "agent-d570fc0b",
      "agent-dd1602e5",
      "agent-d47257d2",
      "agent-e1b852f6",
      "agent-65b0671d",
      "agent-1a43d7eb",
      "agent-a019a0e0",
      "ae5602dd-2f1a-42a8-afaa-70fb8f18901e",
      "agent-a25ed7af"
    ],
    "_/mnt/c/python/data/formulator_total": 14,
    "/mnt/c/python/claude/adversarial/tester": [
      "agent-ab8d727",
      "dea43e83-5b2b-47a9-9090-75ed2ca07ca4",
      "agent-aa16e6e",
      "agent-a0d3b09",
      "agent-aa17da1"
    ],
    "/mnt/c/python/claude/code/orchestrator/skill/builder": [
      "1ebe7d0a-526e-4168-925c-46304eb73ded",
      "agent-3aeb8f31",
      "agent-9ed01fa0",
      "agent-c1692067",
      "agent-27ca9276",
      "agent-65f6c802",
      "agent-18052b86",
      "agent-3ba4fd84",
      "f9dc238a-f21e-4a9f-944e-bcccc2c0f245",
      "agent-55ad1a86"
    ],
    "_/mnt/c/python/claude/code/orchestrator/skill/builder_total": 12,
    "/mnt/c/python/claude/hooks/manager/worktrees/task/4/tui": [
      "fad562df-8a39-4c1b-95a4-9b89b67bff10",
      "agent-ae2dd76",
      "agent-ac7f0f5",
      "d3974794-4abb-49b5-a3b5-4f8b50868d50",
      "agent-a57ac06",
      "agent-ad20312"
    ],
    "/mnt/c/python/claude/document/dependency/tracker": [
      "agent-3a69c8e5",
      "262ecdb1-b989-4970-a721-09c586ada7c5",
      "agent-5519d699",
      "agent-e368d36e",
      "agent-708ddd9a",
      "agent-e8bdcc03",
      "agent-a869d0a7",
      "agent-119f1d51",
      "3b1a8eee-7f4c-4687-8e46-c7e174205141",
      "agent-15381e9c"
    ],
    "_/mnt/c/python/claude/document/dependency/tracker_total": 57,
    "/mnt/c/python/claude/skills/reference/library": [
      "agent-05d1641a",
      "agent-557a6993",
      "agent-13d0a7c8",
      "6dcd33fb-de5c-4a80-b3e0-8cb53ae37ce1",
      "agent-54f78d01"
    ],
    "/mnt/c/python/skill/creator": [
      "fdcca94b-0593-41ac-80a8-3bc0bfd09581",
      "agent-710984a0",
      "agent-6c757802"
    ],
    "/mnt/c/python/kosmos/research": [
      "agent-5bcbc35c",
      "agent-12158b64",
      "agent-ce83b7cb",
      "agent-8a409adc",
      "agent-0e78b4ed",
      "7cb96bb3-70ae-4f2e-b250-a9a18d8c6c26",
      "agent-012ac703",
      "agent-59474c62",
      "agent-2947ed8d"
    ],
    "/mnt/c/python/claude/hooks/manager/worktrees/task/3/markdown": [
      "d1769f54-cccf-4bfb-b83b-c3a5038309d1",
      "agent-a108755",
      "agent-ab87f62",
      "0a495e09-924c-4433-9b05-ebaa3e93bad7",
      "agent-a2e220a",
      "agent-a266b6d"
    ]
  }
}
```

---

## 7. Todos

**Path:** `~/.claude/todos/*.json`

**Description:** Task lists created during sessions

### Sample Data

```json
{
  "path": "/home/jim/.claude/todos",
  "total_files": 1766,
  "total_todos": 192,
  "by_status": {
    "completed": 101,
    "pending": 78,
    "in_progress": 13
  },
  "session_count": 21,
  "todos": [
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #59: h5ad/Parquet Data Format Support",
      "status": "completed",
      "priority": null,
      "active_form": "Implementing h5ad/Parquet data format support"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #69: R Language Execution Support",
      "status": "completed",
      "priority": null,
      "active_form": "Implementing R language execution support"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #60: Figure Generation",
      "status": "completed",
      "priority": null,
      "active_form": "Implementing figure generation"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #61: Jupyter Notebook Generation",
      "status": "completed",
      "priority": null,
      "active_form": "Implementing Jupyter notebook generation"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #70: Null Model Statistical Validation",
      "status": "completed",
      "priority": null,
      "active_form": "Implementing null model statistical validation"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #63: Failure Mode Detection",
      "status": "pending",
      "priority": null,
      "active_form": "Implementing failure mode detection"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #62: Code Line Provenance",
      "status": "pending",
      "priority": null,
      "active_form": "Implementing code line provenance"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #64: Multi-Run Convergence Framework",
      "status": "pending",
      "priority": null,
      "active_form": "Implementing multi-run convergence framework"
    },
    {
      "id": null,
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "content": "Implement #65: Paper Accuracy Validation",
      "status": "pending",
      "priority": null,
      "active_form": "Implementing paper accuracy validation"
    },
    {
      "id": null,
      "session_id": "23bd7690-8ea1-47d0-9ddf-4de9ea878525-agent-23bd7690-8ea1-47d0-9ddf-4de9ea878525",
      "content": "Add HTMLRenderer class with render(data: ExtensionsData) -> str",
      "status": "completed",
      "priority": null,
      "active_form": "Adding HTMLRenderer class"
    }
  ],
  "_todos_total": 192,
  "by_session": {
    "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c-agent-0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c": {
      "count": 9,
      "completed": 5,
      "pending": 4,
      "in_progress": 0
    },
    "23bd7690-8ea1-47d0-9ddf-4de9ea878525-agent-23bd7690-8ea1-47d0-9ddf-4de9ea878525": {
      "count": 5,
      "completed": 1,
      "pending": 3,
      "in_progress": 1
    },
    "46e5d89c-9ce4-479c-a67f-afbe929a1049-agent-46e5d89c-9ce4-479c-a67f-afbe929a1049": {
      "count": 12,
      "completed": 0,
      "pending": 11,
      "in_progress": 1
    },
    "a889539c-9bb7-433c-bfae-e40e6f608261-agent-a889539c-9bb7-433c-bfae-e40e6f608261": {
      "count": 5,
      "completed": 1,
      "pending": 3,
      "in_progress": 1
    },
    "9a39d64b-55cb-4531-aa71-1aa4782198cf-agent-9a39d64b-55cb-4531-aa71-1aa4782198cf": {
      "count": 11,
      "completed": 7,
      "pending": 3,
      "in_progress": 1
    },
    "02983657-215a-4982-a7e4-c4e3481c66e6-agent-02983657-215a-4982-a7e4-c4e3481c66e6": {
      "count": 11,
      "completed": 9,
      "pending": 2,
      "in_progress": 0
    },
    "c19fc436-6769-4890-8777-f5193342ffe3-agent-c19fc436-6769-4890-8777-f5193342ffe3": {
      "count": 5,
      "completed": 1,
      "pending": 3,
      "in_progress": 1
    },
    "48aa21c0-57fa-4d4c-a13c-6364fd9b1c8e-agent-48aa21c0-57fa-4d4c-a13c-6364fd9b1c8e": {
      "count": 11,
      "completed": 7,
      "pending": 3,
      "in_progress": 1
    },
    "14bedb35-3a33-45d2-a431-41874a9707ba-agent-14bedb35-3a33-45d2-a431-41874a9707ba": {
      "count": 12,
      "completed": 0,
      "pending": 11,
      "in_progress": 1
    },
    "6a4d68bc-0660-4a18-9467-3db3cb20c4c9-agent-6a4d68bc-0660-4a18-9467-3db3cb20c4c9": {
      "count": 3,
      "completed": 2,
      "pending": 1,
      "in_progress": 0
    },
    "10ea09e8-eabf-4043-ad7e-d5b6cd9216f5-agent-10ea09e8-eabf-4043-ad7e-d5b6cd9216f5": {
      "count": 6,
      "completed": 5,
      "pending": 0,
      "in_progress": 1
    },
    "dced9bb5-2cbf-4594-96a1-091fb4ed10f1-agent-dced9bb5-2cbf-4594-96a1-091fb4ed10f1": {
      "count": 12,
      "completed": 10,
      "pending": 1,
      "in_progress": 1
    },
    "43a8913b-bc2d-499c-986b-e8eba7dbf3da-agent-43a8913b-bc2d-499c-986b-e8eba7dbf3da": {
      "count": 18,
      "completed": 12,
      "pending": 6,
      "in_progress": 0
    },
    "5efc9061-6a88-47aa-847b-bba4e40731b9-agent-5efc9061-6a88-47aa-847b-bba4e40731b9": {
      "count": 11,
      "completed": 7,
      "pending": 3,
      "in_progress": 1
    },
    "451b2810-9539-4dcc-be53-291f90110a59": {
      "count": 7,
      "completed": 7,
      "pending": 0,
      "in_progress": 0
    },
    "01505466-39cc-4f61-b2b2-cc83419a41b9": {
      "count": 4,
      "completed": 3,
      "pending": 0,
      "in_progress": 1
    },
    "b8421125-9602-4f2c-969e-cb47e6e47599-agent-b8421125-9602-4f2c-969e-cb47e6e47599": {
      "count": 12,
      "completed": 7,
      "pending": 5,
      "in_progress": 0
    },
    "6e5686a0-274a-4c34-b8cb-65b57a7d2ae5-agent-6e5686a0-274a-4c34-b8cb-65b57a7d2ae5": {
      "count": 3,
      "completed": 2,
      "pending": 1,
      "in_progress": 0
    },
    "3455223c-fe8d-4a48-b35f-ee5584f41b55-agent-3455223c-fe8d-4a48-b35f-ee5584f41b55": {
      "count": 11,
      "completed": 1,
      "pending": 9,
      "in_progress": 1
    },
    "1278e667-d9e3-4061-9c97-d3b6dea3792a-agent-1278e667-d9e3-4061-9c97-d3b6dea3792a": {
      "count": 6,
      "completed": 2,
      "pending": 3,
      "in_progress": 1
    },
    "ab8b0c3b-b4cc-49a9-b7d4-687a4f833af4-agent-ab8b0c3b-b4cc-49a9-b7d4-687a4f833af4": {
      "count": 18,
      "completed": 12,
      "pending": 6,
      "in_progress": 0
    }
  }
}
```

---

## 8. Plans

**Path:** `~/.claude/plans/*.md`

**Description:** Implementation plan documents created during plan mode

### Sample Data

```json
{
  "path": "/home/jim/.claude/plans",
  "total_plans": 46,
  "total_lines": 14533,
  "total_code_blocks": 387,
  "plans": [
    {
      "filename": "deep-leaping-fern.md",
      "file_path": "/home/jim/.claude/plans/deep-leaping-fern.md",
      "size_bytes": 28478,
      "created_at": "2025-12-14T00:04:05.400237",
      "modified_at": "2025-12-14T00:04:05.380237",
      "title": "Repo-Xray Unified Architecture Refactor Plan",
      "line_count": 926,
      "char_count": 27082,
      "headers": {
        "h1": 9,
        "h2": 24,
        "h3": 39,
        "h4": 0
      },
      "total_headers": 72,
      "code_block_count": 18,
      "checklist_total": 18,
      "checklist_checked": 0,
      "bullet_points": 55
    },
    {
      "filename": "fuzzy-snacking-turing.md",
      "file_path": "/home/jim/.claude/plans/fuzzy-snacking-turing.md",
      "size_bytes": 30273,
      "created_at": "2025-12-14T00:00:31.300612",
      "modified_at": "2025-12-14T00:00:31.290612",
      "title": "Implementation Plan: New Data Source Extractors",
      "line_count": 1036,
      "char_count": 30125,
      "headers": {
        "h1": 3,
        "h2": 35,
        "h3": 40,
        "h4": 8
      },
      "total_headers": 86,
      "code_block_count": 40,
      "checklist_total": 7,
      "checklist_checked": 7,
      "bullet_points": 93
    },
    {
      "filename": "clever-gliding-aho.md",
      "file_path": "/home/jim/.claude/plans/clever-gliding-aho.md",
      "size_bytes": 2549,
      "created_at": "2025-12-13T21:16:43.978240",
      "modified_at": "2025-12-13T21:16:43.978240",
      "title": "Fix GitHub Actions Publish Catalog Workflow",
      "line_count": 112,
      "char_count": 2549,
      "headers": {
        "h1": 1,
        "h2": 6,
        "h3": 0,
        "h4": 0
      },
      "total_headers": 7,
      "code_block_count": 4,
      "checklist_total": 0,
      "checklist_checked": 0,
      "bullet_points": 10
    },
    {
      "filename": "precious-cuddling-blanket.md",
      "file_path": "/home/jim/.claude/plans/precious-cuddling-blanket.md",
      "size_bytes": 30205,
      "created_at": "2025-12-13T21:13:45.178452",
      "modified_at": "2025-12-13T21:13:45.168452",
      "title": "Create Claude Code Data Sources Reference",
      "line_count": 852,
      "char_count": 27402,
      "headers": {
        "h1": 7,
        "h2": 33,
        "h3": 49,
        "h4": 0
      },
      "total_headers": 89,
      "code_block_count": 21,
      "checklist_total": 101,
      "checklist_checked": 0,
      "bullet_points": 8
    },
    {
      "filename": "HOT_START_old.md",
      "file_path": "/home/jim/.claude/plans/HOT_START_old.md",
      "size_bytes": 15097,
      "created_at": "2025-12-13T15:13:01.739235",
      "modified_at": "2025-12-13T14:13:19.963260",
      "title": "skills: Semantic Hot Start (Pass 2: Behavioral Analysis)",
      "line_count": 550,
      "char_count": 15097,
      "headers": {
        "h1": 1,
        "h2": 7,
        "h3": 19,
        "h4": 10
      },
      "total_headers": 37,
      "code_block_count": 22,
      "checklist_total": 0,
      "checklist_checked": 0,
      "bullet_points": 75
    },
    {
      "filename": "nifty-prancing-mountain.md",
      "file_path": "/home/jim/.claude/plans/nifty-prancing-mountain.md",
      "size_bytes": 1436,
      "created_at": "2025-12-13T01:09:22.557640",
      "modified_at": "2025-12-13T01:09:22.547640",
      "title": "Execution Plan: Adversarial Test Generator Implementation",
      "line_count": 44,
      "char_count": 1436,
      "headers": {
        "h1": 1,
        "h2": 6,
        "h3": 3,
        "h4": 0
      },
      "total_headers": 10,
      "code_block_count": 1,
      "checklist_total": 0,
      "checklist_checked": 0,
      "bullet_points": 3
    },
    {
      "filename": "wild-meandering-sonnet.md",
      "file_path": "/home/jim/.claude/plans/wild-meandering-sonnet.md",
      "size_bytes": 4353,
      "created_at": "2025-12-12T15:24:47.125398",
      "modified_at": "2025-12-12T15:24:47.125398",
      "title": "Plan: Restructure repo-xray to Root and Update Documentation",
      "line_count": 173,
      "char_count": 4233,
      "headers": {
        "h1": 12,
        "h2": 7,
        "h3": 12,
        "h4": 0
      },
      "total_headers": 31,
      "code_block_count": 8,
      "checklist_total": 0,
      "checklist_checked": 0,
      "bullet_points": 7
    },
    {
      "filename": "dreamy-floating-newell.md",
      "file_path": "/home/jim/.claude/plans/dreamy-floating-newell.md",
      "size_bytes": 7623,
      "created_at": "2025-12-12T01:40:05.910481",
      "modified_at": "2025-12-12T01:40:05.890481",
      "title": "Plan: Build kosmos-xray Skill and KosmosArchitect Agent",
      "line_count": 231,
      "char_count": 7491,
      "headers": {
        "h1": 2,
        "h2": 13,
        "h3": 5,
        "h4": 8
      },
      "total_headers": 28,
      "code_block_count": 6,
      "checklist_total": 0,
      "checklist_checked": 0,
      "bullet_points": 35
    },
    {
      "filename": "shiny-sniffing-zephyr.md",
      "file_path": "/home/jim/.claude/plans/shiny-sniffing-zephyr.md",
      "size_bytes": 2952,
      "created_at": "2025-12-11T21:53:59.067693",
      "modified_at": "2025-12-11T21:53:59.067693",
      "title": "Plan: Claude Extensions Visualizer",
      "line_count": 91,
      "char_count": 2946,
      "headers": {
        "h1": 1,
        "h2": 7,
        "h3": 7,
        "h4": 0
      },
      "total_headers": 15,
      "code_block_count": 3,
      "checklist_total": 0,
      "checklist_checked": 0,
      "bullet_points": 24
    },
    {
      "filename": "snuggly-frolicking-puzzle.md",
      "file_path": "/home/jim/.claude/plans/snuggly-frolicking-puzzle.md",
      "size_bytes": 15723,
      "created_at": "2025-12-11T17:00:13.587615",
      "modified_at": "2025-12-11T17:00:13.577615",
      "title": "Claude Hooks Manager - Final Implementation Plan",
      "line_count": 487,
      "char_count": 15153,
      "headers": {
        "h1": 15,
        "h2": 13,
        "h3": 27,
        "h4": 3
      },
      "total_headers": 58,
      "code_block_count": 19,
      "checklist_total": 0,
      "checklist_checked": 0,
      "bullet_points": 42
    }
  ],
  "_plans_total": 46
}
```

---

## 9. Extensions

**Path:** `~/.claude/{agents,commands,skills,plugins,statsig}/`

**Description:** Custom agents, commands, skills, plugins, and feature flag cache

### Sample Data

```json
{
  "agents": [
    {
      "type": "agent",
      "name": "adversarial-generator",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/agents/adversarial-generator.md",
      "size_bytes": 2842,
      "line_count": 76,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "adversarial-orchestrator",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/agents/adversarial-orchestrator.md",
      "size_bytes": 2592,
      "line_count": 84,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "Detect framework and run",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/agents/adversarial-validator.md",
      "size_bytes": 4221,
      "line_count": 106,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "Error Message Therapist",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/agents/therapist.md",
      "size_bytes": 7176,
      "line_count": 272,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "New Hire Documentation Validator",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/agents/new-hire.md",
      "size_bytes": 4607,
      "line_count": 174,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "Parallel Workflow Integration Agent",
      "description": "---",
      "triggers": [
        "integrate",
        "merge workers",
        "combine branches",
        "finish parallel."
      ],
      "file_path": "/home/jim/.claude/agents/parallel-integrate.md",
      "size_bytes": 4649,
      "line_count": 171,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "Parallel Workflow Monitor Agent",
      "description": "---",
      "triggers": [
        "check progress",
        "worker status",
        "monitor workers",
        "who is done",
        "any blocks."
      ],
      "file_path": "/home/jim/.claude/agents/parallel-monitor.md",
      "size_bytes": 2689,
      "line_count": 99,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "Parallel Workflow Setup Agent",
      "description": "---",
      "triggers": [
        "parallel setup",
        "create worktrees",
        "split work",
        "prepare workers."
      ],
      "file_path": "/home/jim/.claude/agents/parallel-setup.md",
      "size_bytes": 3771,
      "line_count": 126,
      "scope": "global"
    },
    {
      "type": "agent",
      "name": "Repo Architect",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/agents/repo_architect.md",
      "size_bytes": 5786,
      "line_count": 164,
      "scope": "global"
    }
  ],
  "agent_count": 9,
  "commands": [
    {
      "type": "command",
      "name": "backup",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/backup.md",
      "size_bytes": 1032,
      "line_count": 21,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "describe",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/describe.md",
      "size_bytes": 256,
      "line_count": 8,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "github",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/github.md",
      "size_bytes": 585,
      "line_count": 23,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "github-private",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/github-private.md",
      "size_bytes": 213,
      "line_count": 11,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "Global Claude Code Commands",
      "description": "These commands are available in any project when using Claude Code.",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/README.md",
      "size_bytes": 1844,
      "line_count": 68,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "plancompact",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/plancompact.md",
      "size_bytes": 211,
      "line_count": 5,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "pull",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/pull.md",
      "size_bytes": 312,
      "line_count": 17,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "push",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/push.md",
      "size_bytes": 366,
      "line_count": 15,
      "scope": "global"
    },
    {
      "type": "command",
      "name": "sync",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/commands/sync.md",
      "size_bytes": 338,
      "line_count": 14,
      "scope": "global"
    }
  ],
  "command_count": 9,
  "skills": [
    {
      "type": "skill",
      "name": "Adversarial Code Analysis",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/skills/adversarial-analysis/SKILL.md",
      "size_bytes": 3667,
      "line_count": 110,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/adversarial-analysis",
      "has_cheatsheet": false,
      "has_reference": false,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Adversarial Pattern Library",
      "description": "---",
      "triggers": [],
      "file_path": "/home/jim/.claude/skills/adversarial-patterns/SKILL.md",
      "size_bytes": 5690,
      "line_count": 119,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/adversarial-patterns",
      "has_cheatsheet": false,
      "has_reference": false,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Documentation Testing Skill",
      "description": "---",
      "triggers": [
        "docs",
        "readme",
        "onboarding",
        "setup validation",
        "documentation audit."
      ],
      "file_path": "/home/jim/.claude/skills/documentation-testing/SKILL.md",
      "size_bytes": 5618,
      "line_count": 175,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/documentation-testing",
      "has_cheatsheet": false,
      "has_reference": false,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Error UX Skill",
      "description": "---",
      "triggers": [
        "error messages",
        "user experience",
        "error handling",
        "exception messages",
        "validation errors."
      ],
      "file_path": "/home/jim/.claude/skills/error-ux/SKILL.md",
      "size_bytes": 7920,
      "line_count": 271,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/error-ux",
      "has_cheatsheet": false,
      "has_reference": false,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Local LLM Management",
      "description": "---",
      "triggers": [
        "ollama",
        "local model",
        "local LLM",
        "VRAM",
        "GPU memory",
        "model speed",
        "inference",
        "Modelfile",
        "llama.cpp",
        "quantization.\""
      ],
      "file_path": "/home/jim/.claude/skills/local-llm/SKILL.md",
      "size_bytes": 6890,
      "line_count": 264,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/local-llm",
      "has_cheatsheet": true,
      "has_reference": true,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Parallel Workflow Orchestrator",
      "description": "---",
      "triggers": [
        "parallel",
        "orchestrator",
        "worktrees",
        "workers",
        "coordinate",
        "integrate",
        "split work",
        "multiple sessions",
        "code review",
        "work items.\""
      ],
      "file_path": "/home/jim/.claude/skills/parallel-orchestrator/SKILL.md",
      "size_bytes": 18189,
      "line_count": 644,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/parallel-orchestrator",
      "has_cheatsheet": false,
      "has_reference": false,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Parallel Workflow Retrospective",
      "description": "---",
      "triggers": [
        "retrospective",
        "review",
        "post-mortem",
        "lessons learned",
        "workflow analysis",
        "evaluate parallel",
        "workflow quality",
        "planning assessment.\""
      ],
      "file_path": "/home/jim/.claude/skills/parallel-retrospective/SKILL.md",
      "size_bytes": 18334,
      "line_count": 653,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/parallel-retrospective",
      "has_cheatsheet": false,
      "has_reference": false,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Parallel Workflow Worker",
      "description": "---",
      "triggers": [
        "worker",
        "checkpoint",
        "worktree",
        "assigned scope",
        "commit prefix",
        "parallel task.\""
      ],
      "file_path": "/home/jim/.claude/skills/parallel-worker/SKILL.md",
      "size_bytes": 10359,
      "line_count": 451,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/parallel-worker",
      "has_cheatsheet": false,
      "has_reference": false,
      "has_configs": false,
      "has_scripts": false
    },
    {
      "type": "skill",
      "name": "Repo X-Ray Skill",
      "description": "---",
      "triggers": [
        "xray",
        "map structure",
        "skeleton",
        "interface",
        "architecture",
        "explore",
        "warm start",
        "token budget",
        "context compression."
      ],
      "file_path": "/home/jim/.claude/skills/repo-xray/SKILL.md",
      "size_bytes": 7118,
      "line_count": 186,
      "scope": "global",
      "skill_dir": "/home/jim/.claude/skills/repo-xray",
      "has_cheatsheet": true,
      "has_reference": true,
      "has_configs": true,
      "has_scripts": true
    }
  ],
  "skill_count": 9,
  "plugins": {
    "exists": true,
    "path": "/home/jim/.claude/plugins",
    "installed_plugins": {
      "version": 2,
      "plugins": {}
    },
    "known_marketplaces": {
      "community-claude-plugins": {
        "source": {
          "source": "github",
          "repo": "jimmc414/claude-code-plugin-marketplace"
        },
        "installLocation": "/home/jim/.claude/plugins/marketplaces/community-claude-plugins",
        "lastUpdated": "2025-12-14T02:45:47.050Z"
      }
    },
    "config": {
      "repositories": {}
    }
  },
  "statsig": {
    "exists": true,
    "path": "/home/jim/.claude/statsig",
    "cache_file_count": 14,
    "cache_files": [
      "statsig.cached.evaluations.2637556285",
      "statsig.session_id.2656274335",
      "statsig.cached.evaluations.3051566175",
      "statsig.cached.evaluations.2858433809",
      "statsig.stable_id.2656274335",
      "statsig.cached.evaluations.686696739",
      "statsig.cached.evaluations.1797776468",
      "statsig.cached.evaluations.929717271",
      "statsig.failed_logs.658916400",
      "statsig.last_modified_time.evaluations"
    ],
    "_cache_files_total": 14
  },
  "total_extensions": 27
}
```

---

## 10. Sqlite Store

**Path:** `~/.claude/__store.db`

**Description:** Structured message storage in SQLite format

### Sample Data

```json
{
  "database_exists": true,
  "path": "/home/jim/.claude/__store.db",
  "size_bytes": 2236416,
  "size_human": "2.1 MB",
  "tables": {
    "__drizzle_migrations": {
      "row_count": 3,
      "columns": [
        {
          "name": "id",
          "type": "SERIAL",
          "notnull": false,
          "pk": true
        },
        {
          "name": "hash",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "created_at",
          "type": "numeric",
          "notnull": false,
          "pk": false
        }
      ]
    },
    "assistant_messages": {
      "row_count": 124,
      "columns": [
        {
          "name": "uuid",
          "type": "TEXT",
          "notnull": true,
          "pk": true
        },
        {
          "name": "cost_usd",
          "type": "REAL",
          "notnull": true,
          "pk": false
        },
        {
          "name": "duration_ms",
          "type": "INTEGER",
          "notnull": true,
          "pk": false
        },
        {
          "name": "message",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "is_api_error_message",
          "type": "INTEGER",
          "notnull": true,
          "pk": false
        },
        {
          "name": "timestamp",
          "type": "INTEGER",
          "notnull": true,
          "pk": false
        },
        {
          "name": "model",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        }
      ]
    },
    "base_messages": {
      "row_count": 255,
      "columns": [
        {
          "name": "uuid",
          "type": "TEXT",
          "notnull": true,
          "pk": true
        },
        {
          "name": "parent_uuid",
          "type": "TEXT",
          "notnull": false,
          "pk": false
        },
        {
          "name": "session_id",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "timestamp",
          "type": "INTEGER",
          "notnull": true,
          "pk": false
        },
        {
          "name": "message_type",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "cwd",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "user_type",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "version",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "isSidechain",
          "type": "INTEGER",
          "notnull": true,
          "pk": false
        }
      ]
    },
    "conversation_summaries": {
      "row_count": 2,
      "columns": [
        {
          "name": "leaf_uuid",
          "type": "TEXT",
          "notnull": true,
          "pk": true
        },
        {
          "name": "summary",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "updated_at",
          "type": "INTEGER",
          "notnull": true,
          "pk": false
        }
      ]
    },
    "user_messages": {
      "row_count": 131,
      "columns": [
        {
          "name": "uuid",
          "type": "TEXT",
          "notnull": true,
          "pk": true
        },
        {
          "name": "message",
          "type": "TEXT",
          "notnull": true,
          "pk": false
        },
        {
          "name": "tool_use_result",
          "type": "TEXT",
          "notnull": false,
          "pk": false
        },
        {
          "name": "timestamp",
          "type": "INTEGER",
          "notnull": true,
          "pk": false
        }
      ]
    }
  },
  "assistant_stats": {
    "total_messages": 0,
    "total_cost_usd": 0.0,
    "models_used": [],
    "sessions_count": 0,
    "date_range": {
      "first": null,
      "last": null
    }
  },
  "model_usage": [
    {
      "model": "claude-3-7-sonnet-20250219",
      "message_count": 124,
      "total_cost_usd": 5.7689
    }
  ]
}
```

---

## 11. Debug Logs

**Path:** `~/.claude/debug/*.txt`

**Description:** Timestamped diagnostic logs per session

### Sample Data

```json
{
  "directory_exists": true,
  "path": "/home/jim/.claude/debug",
  "total_files": 1708,
  "total_size_bytes": 70411689,
  "total_size_human": "67.1 MB",
  "total_lines": 850580,
  "total_errors": 24955,
  "total_warnings": 328,
  "logs": [
    {
      "session_id": "24190deb-471d-413c-a185-ba048413da7c",
      "filename": "24190deb-471d-413c-a185-ba048413da7c.txt",
      "size_bytes": 607000,
      "size_human": "592.8 KB",
      "line_count": 6708,
      "error_count": 19,
      "warning_count": 8,
      "debug_count": 6609,
      "first_timestamp": "2025-12-14T02:45:46.445Z",
      "last_timestamp": "2025-12-14T06:47:41.665Z",
      "modified_at": "2025-12-14T00:47:42.605520"
    },
    {
      "session_id": "dced9bb5-2cbf-4594-96a1-091fb4ed10f1",
      "filename": "dced9bb5-2cbf-4594-96a1-091fb4ed10f1.txt",
      "size_bytes": 3268350,
      "size_human": "3.1 MB",
      "line_count": 34399,
      "error_count": 60,
      "warning_count": 97,
      "debug_count": 33906,
      "first_timestamp": "2025-12-12T17:46:33.316Z",
      "last_timestamp": "2025-12-14T06:47:40.848Z",
      "modified_at": "2025-12-14T00:47:41.845521"
    },
    {
      "session_id": "7712103f-beca-4ddd-9de8-b1004867c0ae",
      "filename": "7712103f-beca-4ddd-9de8-b1004867c0ae.txt",
      "size_bytes": 6908159,
      "size_human": "6.6 MB",
      "line_count": 71671,
      "error_count": 748,
      "warning_count": 9,
      "debug_count": 69247,
      "first_timestamp": "2025-12-06T01:00:57.054Z",
      "last_timestamp": "2025-12-14T06:47:02.278Z",
      "modified_at": "2025-12-14T00:47:03.275594"
    },
    {
      "session_id": "c0db16bd-062f-49d8-b5ab-abc789e6062b",
      "filename": "c0db16bd-062f-49d8-b5ab-abc789e6062b.txt",
      "size_bytes": 6011,
      "size_human": "5.9 KB",
      "line_count": 68,
      "error_count": 0,
      "warning_count": 0,
      "debug_count": 68,
      "first_timestamp": "2025-12-14T06:29:28.603Z",
      "last_timestamp": "2025-12-14T06:39:00.471Z",
      "modified_at": "2025-12-14T00:39:01.456464"
    },
    {
      "session_id": "dea43e83-5b2b-47a9-9090-75ed2ca07ca4",
      "filename": "dea43e83-5b2b-47a9-9090-75ed2ca07ca4.txt",
      "size_bytes": 154095,
      "size_human": "150.5 KB",
      "line_count": 1678,
      "error_count": 5,
      "warning_count": 10,
      "debug_count": 1654,
      "first_timestamp": "2025-12-13T05:50:14.696Z",
      "last_timestamp": "2025-12-14T06:36:40.641Z",
      "modified_at": "2025-12-14T00:36:41.626718"
    },
    {
      "session_id": "60c8284e-092d-41c7-ae2d-654be4bacde3",
      "filename": "60c8284e-092d-41c7-ae2d-654be4bacde3.txt",
      "size_bytes": 54032,
      "size_human": "52.8 KB",
      "line_count": 701,
      "error_count": 60,
      "warning_count": 0,
      "debug_count": 284,
      "first_timestamp": "2025-12-12T18:30:51.781Z",
      "last_timestamp": "2025-12-14T06:31:13.913Z",
      "modified_at": "2025-12-14T00:31:14.907298"
    },
    {
      "session_id": "2496bf3b-a7a4-4a69-948e-e9859541610a",
      "filename": "2496bf3b-a7a4-4a69-948e-e9859541610a.txt",
      "size_bytes": 469877,
      "size_human": "458.9 KB",
      "line_count": 5121,
      "error_count": 19,
      "warning_count": 38,
      "debug_count": 5022,
      "first_timestamp": "2025-12-13T08:10:53.186Z",
      "last_timestamp": "2025-12-14T06:26:59.869Z",
      "modified_at": "2025-12-14T00:27:00.867753"
    },
    {
      "session_id": "dc5255a1-f0a4-4195-a136-9c4659c37555",
      "filename": "dc5255a1-f0a4-4195-a136-9c4659c37555.txt",
      "size_bytes": 78091,
      "size_human": "76.3 KB",
      "line_count": 1043,
      "error_count": 102,
      "warning_count": 0,
      "debug_count": 338,
      "first_timestamp": "2025-12-12T04:55:07.383Z",
      "last_timestamp": "2025-12-14T06:25:15.235Z",
      "modified_at": "2025-12-14T00:25:16.217945"
    },
    {
      "session_id": "5722316d-7dd4-45a3-9656-e9da966b7b1a",
      "filename": "5722316d-7dd4-45a3-9656-e9da966b7b1a.txt",
      "size_bytes": 534623,
      "size_human": "522.1 KB",
      "line_count": 5827,
      "error_count": 24,
      "warning_count": 24,
      "debug_count": 5768,
      "first_timestamp": "2025-12-13T05:31:30.968Z",
      "last_timestamp": "2025-12-14T06:18:25.326Z",
      "modified_at": "2025-12-14T00:18:26.318676"
    },
    {
      "session_id": "8a19dd8c-4b2e-4521-9a13-7e1b87e2d00c",
      "filename": "8a19dd8c-4b2e-4521-9a13-7e1b87e2d00c.txt",
      "size_bytes": 247227,
      "size_human": "241.4 KB",
      "line_count": 2689,
      "error_count": 17,
      "warning_count": 8,
      "debug_count": 2457,
      "first_timestamp": "2025-12-12T06:34:10.572Z",
      "last_timestamp": "2025-12-13T08:10:49.807Z",
      "modified_at": "2025-12-13T02:10:49.800906"
    }
  ],
  "_logs_total": 1708
}
```

---

## 12. File History

**Path:** `~/.claude/file-history/`

**Description:** File backup/versioning system that preserves file states before edits

### Sample Data

```json
{
  "directory_exists": true,
  "path": "/home/jim/.claude/file-history",
  "total_sessions": 124,
  "total_files": 2276,
  "total_versions": 3633,
  "total_size_bytes": 46254839,
  "total_size_human": "44.1 MB",
  "sessions": [
    {
      "session_id": "009036d7-1c9a-41f6-940d-41293b09431e",
      "file_count": 18,
      "version_count": 64,
      "total_size_bytes": 493683,
      "files": [
        {
          "hash": "692cdade29d0c3bf",
          "version_count": 5,
          "max_version": 6,
          "total_size_bytes": 37786
        },
        {
          "hash": "83b146328933b674",
          "version_count": 2,
          "max_version": 2,
          "total_size_bytes": 14515
        },
        {
          "hash": "78b6cd9040260dcf",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 3537
        },
        {
          "hash": "a530191800f3f108",
          "version_count": 13,
          "max_version": 14,
          "total_size_bytes": 91741
        },
        {
          "hash": "86969c9c37415d81",
          "version_count": 3,
          "max_version": 4,
          "total_size_bytes": 33007
        },
        {
          "hash": "c99f5e23be3d9f8f",
          "version_count": 3,
          "max_version": 3,
          "total_size_bytes": 27194
        },
        {
          "hash": "7dc0af35ec4f6c27",
          "version_count": 10,
          "max_version": 11,
          "total_size_bytes": 56574
        },
        {
          "hash": "4dfeea06a55066d1",
          "version_count": 5,
          "max_version": 6,
          "total_size_bytes": 38819
        },
        {
          "hash": "4db25a39ae0a3c3f",
          "version_count": 3,
          "max_version": 4,
          "total_size_bytes": 23680
        },
        {
          "hash": "9c581f9a4118b0ca",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 9003
        }
      ],
      "_files_total": 18
    },
    {
      "session_id": "01f6a57e-ecc5-44bd-8963-67afc93513f2",
      "file_count": 126,
      "version_count": 133,
      "total_size_bytes": 2120001,
      "files": [
        {
          "hash": "9eba78babf54adb4",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 20042
        },
        {
          "hash": "9ff679aaab4895fe",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 16821
        },
        {
          "hash": "3e6467eec2e61003",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 8056
        },
        {
          "hash": "e920dd586983a90a",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 14805
        },
        {
          "hash": "d046821ba80ff55c",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 14678
        },
        {
          "hash": "92766ea11e291d63",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 3243
        },
        {
          "hash": "097896fb4df53c61",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 15652
        },
        {
          "hash": "14d4d02db03c292f",
          "version_count": 2,
          "max_version": 4,
          "total_size_bytes": 18197
        },
        {
          "hash": "57e811ff3176211a",
          "version_count": 1,
          "max_version": 6,
          "total_size_bytes": 4874
        },
        {
          "hash": "b6459dea91fd984b",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 26350
        }
      ],
      "_files_total": 126
    },
    {
      "session_id": "0450821c-8803-46b6-9a8c-1b5d536ff7c4",
      "file_count": 8,
      "version_count": 8,
      "total_size_bytes": 55311,
      "files": [
        {
          "hash": "922fdd51f2e54c7a",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 2804
        },
        {
          "hash": "2c671e0ee483a095",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 3950
        },
        {
          "hash": "db32b5d50e8fb0ca",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 26286
        },
        {
          "hash": "bf26c38378318b67",
          "version_count": 1,
          "max_version": 3,
          "total_size_bytes": 6194
        },
        {
          "hash": "bce70a1776ec2d36",
          "version_count": 1,
          "max_version": 14,
          "total_size_bytes": 5105
        },
        {
          "hash": "145f8837d722bc6e",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 5105
        },
        {
          "hash": "8eae6ae2a7131200",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 1514
        },
        {
          "hash": "5715b99dc2b11f25",
          "version_count": 1,
          "max_version": 5,
          "total_size_bytes": 4353
        }
      ]
    },
    {
      "session_id": "04e0e655-f31a-4976-9bc5-3953c98c8f08",
      "file_count": 6,
      "version_count": 11,
      "total_size_bytes": 157799,
      "files": [
        {
          "hash": "19037118051cade7",
          "version_count": 3,
          "max_version": 3,
          "total_size_bytes": 109287
        },
        {
          "hash": "aa7486bce82678dd",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 1379
        },
        {
          "hash": "5a19e0e0754b601a",
          "version_count": 4,
          "max_version": 4,
          "total_size_bytes": 28625
        },
        {
          "hash": "397a736f197945b4",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 15723
        },
        {
          "hash": "a1879fbd196a87b6",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 1729
        },
        {
          "hash": "11767b4ba27b000e",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 1056
        }
      ]
    },
    {
      "session_id": "04f9cd7b-0c2a-43d8-a91e-338c19d399fa",
      "file_count": 1,
      "version_count": 2,
      "total_size_bytes": 22396,
      "files": [
        {
          "hash": "978376e2560fe527",
          "version_count": 2,
          "max_version": 2,
          "total_size_bytes": 22396
        }
      ]
    },
    {
      "session_id": "0a495e09-924c-4433-9b05-ebaa3e93bad7",
      "file_count": 1,
      "version_count": 1,
      "total_size_bytes": 234,
      "files": [
        {
          "hash": "7c04514f994e10ba",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 234
        }
      ]
    },
    {
      "session_id": "0a64e446-fdd3-4ac8-86c2-8229af2bd84d",
      "file_count": 23,
      "version_count": 91,
      "total_size_bytes": 1568047,
      "files": [
        {
          "hash": "6ae73c38fe93dbfa",
          "version_count": 5,
          "max_version": 5,
          "total_size_bytes": 95787
        },
        {
          "hash": "99dd5d6ece4d4de0",
          "version_count": 2,
          "max_version": 2,
          "total_size_bytes": 9231
        },
        {
          "hash": "176d1b648627a842",
          "version_count": 3,
          "max_version": 3,
          "total_size_bytes": 44479
        },
        {
          "hash": "4d299a51355b837f",
          "version_count": 5,
          "max_version": 5,
          "total_size_bytes": 86799
        },
        {
          "hash": "cdff4ebd2e32ba40",
          "version_count": 4,
          "max_version": 4,
          "total_size_bytes": 56174
        },
        {
          "hash": "a12a35170013c7b6",
          "version_count": 4,
          "max_version": 4,
          "total_size_bytes": 42716
        },
        {
          "hash": "58259c1dc0862e45",
          "version_count": 3,
          "max_version": 3,
          "total_size_bytes": 52531
        },
        {
          "hash": "8d5e4642dda651c3",
          "version_count": 4,
          "max_version": 4,
          "total_size_bytes": 32826
        },
        {
          "hash": "41a4ef661d1faa74",
          "version_count": 5,
          "max_version": 5,
          "total_size_bytes": 84762
        },
        {
          "hash": "83f71ce671c95800",
          "version_count": 3,
          "max_version": 3,
          "total_size_bytes": 36817
        }
      ],
      "_files_total": 23
    },
    {
      "session_id": "0ba915ff-e7b5-4bf6-a5d8-a9532eadbe3c",
      "file_count": 88,
      "version_count": 88,
      "total_size_bytes": 1407553,
      "files": [
        {
          "hash": "9ff679aaab4895fe",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 16821
        },
        {
          "hash": "e920dd586983a90a",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 14805
        },
        {
          "hash": "d046821ba80ff55c",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 14678
        },
        {
          "hash": "097896fb4df53c61",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 15652
        },
        {
          "hash": "14d4d02db03c292f",
          "version_count": 1,
          "max_version": 3,
          "total_size_bytes": 9039
        },
        {
          "hash": "57e811ff3176211a",
          "version_count": 1,
          "max_version": 6,
          "total_size_bytes": 4874
        },
        {
          "hash": "2d2c1348d831626c",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 18232
        },
        {
          "hash": "ddd5b5d5b8142a99",
          "version_count": 1,
          "max_version": 10,
          "total_size_bytes": 6502
        },
        {
          "hash": "1b320d7200a95094",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 12745
        },
        {
          "hash": "607c73631331c6ea",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 2352
        }
      ],
      "_files_total": 88
    },
    {
      "session_id": "0ce7947f-0308-4202-a5f4-8cb09ba7aace",
      "file_count": 5,
      "version_count": 7,
      "total_size_bytes": 66899,
      "files": [
        {
          "hash": "033b35c2c10d3458",
          "version_count": 2,
          "max_version": 2,
          "total_size_bytes": 21953
        },
        {
          "hash": "4659ae19319dde91",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 4163
        },
        {
          "hash": "1c68c41061e4bab1",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 1390
        },
        {
          "hash": "6510241d27306da5",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 4626
        },
        {
          "hash": "2aa2a4b852c67e53",
          "version_count": 2,
          "max_version": 2,
          "total_size_bytes": 34767
        }
      ]
    },
    {
      "session_id": "0f234921-3ecf-4aaa-ace4-bcbbf63a57af",
      "file_count": 7,
      "version_count": 13,
      "total_size_bytes": 89762,
      "files": [
        {
          "hash": "c99f5e23be3d9f8f",
          "version_count": 5,
          "max_version": 5,
          "total_size_bytes": 40570
        },
        {
          "hash": "bf58d20dd5a9574e",
          "version_count": 1,
          "max_version": 1,
          "total_size_bytes": 9524
        },
        {
          "hash": "8c8f86d30adf836a",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 13067
        },
        {
          "hash": "df5e6407336c8b3d",
          "version_count": 2,
          "max_version": 2,
          "total_size_bytes": 2744
        },
        {
          "hash": "739329f5e67efa99",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 6000
        },
        {
          "hash": "107b0f1e650911f8",
          "version_count": 2,
          "max_version": 2,
          "total_size_bytes": 182
        },
        {
          "hash": "38284aca53e38a87",
          "version_count": 1,
          "max_version": 2,
          "total_size_bytes": 17675
        }
      ]
    }
  ],
  "_sessions_total": 124
}
```

---

## 13. Shell Snapshots

**Path:** `~/.claude/shell-snapshots/`

**Description:** Shell environment captures for session restoration

### Sample Data

```json
{
  "directory_exists": true,
  "path": "/home/jim/.claude/shell-snapshots",
  "total_snapshots": 82,
  "total_size_bytes": 268711,
  "total_size_human": "262.4 KB",
  "by_shell": {
    "bash": 82
  },
  "snapshots": [
    {
      "filename": "snapshot-bash-1765680346565-b7ecy3.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-13T20:45:46.591301",
      "shell": "bash",
      "timestamp": "1765680346565",
      "random_id": "b7ecy3"
    },
    {
      "filename": "snapshot-bash-1765613453279-u879hw.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-13T02:10:53.290898",
      "shell": "bash",
      "timestamp": "1765613453279",
      "random_id": "u879hw"
    },
    {
      "filename": "snapshot-bash-1765605014791-9yu0kx.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-12T23:50:14.805213",
      "shell": "bash",
      "timestamp": "1765605014791",
      "random_id": "9yu0kx"
    },
    {
      "filename": "snapshot-bash-1765603891082-df2v2b.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-12T23:31:31.096850",
      "shell": "bash",
      "timestamp": "1765603891082",
      "random_id": "df2v2b"
    },
    {
      "filename": "snapshot-bash-1765587846363-fj6box.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-12T19:04:06.369602",
      "shell": "bash",
      "timestamp": "1765587846363",
      "random_id": "fj6box"
    },
    {
      "filename": "snapshot-bash-1765564251939-8kchz4.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-12T12:30:51.956199",
      "shell": "bash",
      "timestamp": "1765564251939",
      "random_id": "8kchz4"
    },
    {
      "filename": "snapshot-bash-1765559809800-cyezex.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-12T11:16:49.835094",
      "shell": "bash",
      "timestamp": "1765559809800",
      "random_id": "cyezex"
    },
    {
      "filename": "snapshot-bash-1765519433382-ojrgq2.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-12T00:03:53.401955",
      "shell": "bash",
      "timestamp": "1765519433382",
      "random_id": "ojrgq2"
    },
    {
      "filename": "snapshot-bash-1765519416294-d9vkxd.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-12T00:03:36.311982",
      "shell": "bash",
      "timestamp": "1765519416294",
      "random_id": "d9vkxd"
    },
    {
      "filename": "snapshot-bash-1765515739031-9rjyg8.sh",
      "size_bytes": 3246,
      "size_human": "3.2 KB",
      "modified_at": "2025-12-11T23:02:19.039317",
      "shell": "bash",
      "timestamp": "1765515739031",
      "random_id": "9rjyg8"
    }
  ],
  "_snapshots_total": 82
}
```

---

## 14. Session Env

**Path:** `~/.claude/session-env/`

**Description:** Per-session environment data

### Sample Data

```json
{
  "directory_exists": true,
  "path": "/home/jim/.claude/session-env",
  "total_sessions": 104,
  "sessions_with_data": 0,
  "total_size_bytes": 0,
  "total_size_human": "0.0 B",
  "sessions": [
    {
      "session_id": "009036d7-1c9a-41f6-940d-41293b09431e",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "011e7271-678e-4ed1-95e3-defc20f767b6",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "04f9cd7b-0c2a-43d8-a91e-338c19d399fa",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "0a495e09-924c-4433-9b05-ebaa3e93bad7",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "0a64e446-fdd3-4ac8-86c2-8229af2bd84d",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "0bee98d3-b9fd-46b9-b8be-9c776f3b5411",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "0ce7947f-0308-4202-a5f4-8cb09ba7aace",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "0de190e0-e613-4466-a1c9-92c27fb1baa7",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "10ea09e8-eabf-4043-ad7e-d5b6cd9216f5",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    },
    {
      "session_id": "115e24a7-d7d9-40fb-b25b-a537c66aa440",
      "files": [],
      "file_count": 0,
      "size_bytes": 0,
      "size_human": "0.0 B"
    }
  ],
  "_sessions_total": 104
}
```

---

## 15. Versions

**Path:** `~/.local/share/claude/versions/`

**Description:** Installed Claude Code binary versions

### Sample Data

```json
{
  "directory_exists": true,
  "path": "/home/jim/.local/share/claude/versions",
  "total_versions": 0,
  "total_size_bytes": 0,
  "total_size_human": "0.0 B",
  "current_version": "2.0.67",
  "versions": []
}
```

---

## 16. Project Config

**Path:** `<project>/.claude/`

**Description:** Project-specific customizations that override global settings

### Sample Data

```json
{
  "projects_scanned": 55,
  "projects_with_config": 27,
  "total_agents": 21,
  "total_commands": 36,
  "total_skills": 25,
  "adoption_rate": 0.4909090909090909,
  "projects": [
    {
      "path": "/home/jim",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": false,
        "allow_rules": 0,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [
        "adversarial-generator",
        "adversarial-orchestrator",
        "adversarial-validator",
        "new-hire",
        "parallel-integrate",
        "parallel-monitor",
        "parallel-setup",
        "repo_architect",
        "therapist"
      ],
      "agent_count": 9,
      "commands": [
        "README",
        "backup",
        "describe",
        "github",
        "github-private",
        "plancompact",
        "pull",
        "push",
        "sync"
      ],
      "command_count": 9,
      "skills": [
        "adversarial-analysis",
        "adversarial-patterns",
        "documentation-testing",
        "error-ux",
        "local-llm",
        "parallel-orchestrator",
        "parallel-retrospective",
        "parallel-worker",
        "repo-xray"
      ],
      "skill_count": 9,
      "customization_score": 28
    },
    {
      "path": "/mnt/c/python/claude-document-dependency-tracker",
      "has_claude_dir": true,
      "has_settings": false,
      "agents": [
        "architect",
        "code-reviewer",
        "codebase-analyst",
        "explorer",
        "historian",
        "scout",
        "translator",
        "warm-start-engineer"
      ],
      "agent_count": 8,
      "commands": [
        "createspec",
        "hooks"
      ],
      "command_count": 2,
      "skills": [
        "analysis-interpreter",
        "codebase-analyzer",
        "context-awareness",
        "dependency-discovery",
        "directory-mapping",
        "domain-dictionary",
        "git-forensics",
        "impact-analysis",
        "python-best-practices",
        "security-patterns"
      ],
      "_skills_total": 11,
      "skill_count": 11,
      "customization_score": 21
    },
    {
      "path": "/mnt/c/python/data-formulator-claude-code-proxy",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": true,
        "allow_rules": 16,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [],
      "agent_count": 0,
      "commands": [
        "blockers",
        "checkpoint",
        "current",
        "docs",
        "files",
        "help",
        "history",
        "logs",
        "next-task",
        "phases"
      ],
      "_commands_total": 16,
      "command_count": 16,
      "skills": [],
      "skill_count": 0,
      "customization_score": 17
    },
    {
      "path": "/mnt/c/python/Kosmos",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": true,
        "allow_rules": 50,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [
        "kosmos_architect"
      ],
      "agent_count": 1,
      "commands": [
        "README",
        "hn-rewrite"
      ],
      "command_count": 2,
      "skills": [
        "kosmos-e2e-testing"
      ],
      "skill_count": 1,
      "customization_score": 5
    },
    {
      "path": "/mnt/c/python/kosmos",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": true,
        "allow_rules": 50,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [
        "kosmos_architect"
      ],
      "agent_count": 1,
      "commands": [
        "README",
        "hn-rewrite"
      ],
      "command_count": 2,
      "skills": [
        "kosmos-e2e-testing"
      ],
      "skill_count": 1,
      "customization_score": 5
    },
    {
      "path": "/mnt/c/python",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": true,
        "allow_rules": 6,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [],
      "agent_count": 0,
      "commands": [
        "describe",
        "github",
        "github-private"
      ],
      "command_count": 3,
      "skills": [],
      "skill_count": 0,
      "customization_score": 4
    },
    {
      "path": "/mnt/c/python/claude-repo-xray",
      "has_claude_dir": true,
      "has_settings": false,
      "agents": [
        "repo_architect",
        "repo_investigator"
      ],
      "agent_count": 2,
      "commands": [],
      "command_count": 0,
      "skills": [
        "repo-investigator",
        "repo-xray"
      ],
      "skill_count": 2,
      "customization_score": 4
    },
    {
      "path": "/home/jim/code_install",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": true,
        "allow_rules": 2,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [],
      "agent_count": 0,
      "commands": [],
      "command_count": 0,
      "skills": [],
      "skill_count": 0,
      "customization_score": 1
    },
    {
      "path": "/mnt/c/python/jack_page",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": true,
        "allow_rules": 2,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [],
      "agent_count": 0,
      "commands": [],
      "command_count": 0,
      "skills": [],
      "skill_count": 0,
      "customization_score": 1
    },
    {
      "path": "/mnt/c/python/onefilellm",
      "has_claude_dir": true,
      "settings": {
        "has_permissions": true,
        "allow_rules": 1,
        "deny_rules": 0
      },
      "has_settings": true,
      "agents": [],
      "agent_count": 0,
      "commands": [],
      "command_count": 0,
      "skills": [],
      "skill_count": 0,
      "customization_score": 1
    }
  ],
  "_projects_total": 55
}
```

---

## 17. Claude Md

**Path:** `<project>/CLAUDE.md`

**Description:** Project instructions (CLAUDE.md) read by Claude at session start

### Sample Data

```json
{
  "projects_scanned": 55,
  "projects_with_claude_md": 9,
  "adoption_rate": 0.16363636363636364,
  "files": [
    {
      "project": "/mnt/c/python/Kosmos",
      "path": "/mnt/c/python/Kosmos/CLAUDE.md",
      "size_bytes": 216,
      "size_human": "216.0 B",
      "line_count": 7,
      "word_count": 33,
      "sections": [
        {
          "level": 1,
          "title": "Claude Code Instructions"
        },
        {
          "level": 2,
          "title": "Commit Guidelines"
        }
      ],
      "section_count": 2,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/claude-code-plugin-marketplace",
      "path": "/mnt/c/python/claude-code-plugin-marketplace/CLAUDE.md",
      "size_bytes": 10397,
      "size_human": "10.2 KB",
      "line_count": 437,
      "word_count": 1256,
      "sections": [
        {
          "level": 1,
          "title": "Claude Code Plugin Marketplace - Operator Cheatsheet"
        },
        {
          "level": 2,
          "title": "Overview"
        },
        {
          "level": 2,
          "title": "Directory Structure"
        },
        {
          "level": 2,
          "title": "Python Tools Reference"
        },
        {
          "level": 3,
          "title": "scaffold.py - Create New Components"
        },
        {
          "level": 1,
          "title": "Create a new plugin"
        },
        {
          "level": 1,
          "title": "Add components to existing plugin"
        },
        {
          "level": 1,
          "title": "With description"
        },
        {
          "level": 3,
          "title": "validate.py - Validate Plugins"
        },
        {
          "level": 1,
          "title": "Validate single plugin"
        }
      ],
      "_sections_total": 82,
      "section_count": 82,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/claude-document-dependency-tracker",
      "path": "/mnt/c/python/claude-document-dependency-tracker/CLAUDE.md",
      "size_bytes": 1469,
      "size_human": "1.4 KB",
      "line_count": 49,
      "word_count": 189,
      "sections": [
        {
          "level": 1,
          "title": "Claude Code Project Configuration"
        },
        {
          "level": 2,
          "title": "Project Overview"
        },
        {
          "level": 2,
          "title": "MCP Servers"
        },
        {
          "level": 3,
          "title": "SpecBuilder (`mcp__specbuilder__*`)"
        },
        {
          "level": 2,
          "title": "Custom Commands"
        },
        {
          "level": 3,
          "title": "`/createspec <description>`"
        },
        {
          "level": 2,
          "title": "Tool Routing"
        },
        {
          "level": 2,
          "title": "Dependencies"
        },
        {
          "level": 2,
          "title": "Key Files"
        }
      ],
      "section_count": 9,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/column_mapper",
      "path": "/mnt/c/python/column_mapper/CLAUDE.md",
      "size_bytes": 2182,
      "size_human": "2.1 KB",
      "line_count": 55,
      "word_count": 287,
      "sections": [
        {
          "level": 1,
          "title": "CLAUDE.md"
        },
        {
          "level": 2,
          "title": "Project Overview"
        },
        {
          "level": 2,
          "title": "Commands"
        },
        {
          "level": 2,
          "title": "Usage Examples"
        },
        {
          "level": 1,
          "title": "Basic usage - outputs imhsipl.dat and <input>_IMHSIPL.xlsx"
        },
        {
          "level": 1,
          "title": "With custom output prefix - outputs prefix.dat and prefix.xlsx"
        },
        {
          "level": 2,
          "title": "Architecture"
        },
        {
          "level": 2,
          "title": "Utilities"
        },
        {
          "level": 2,
          "title": "Code Style Guidelines"
        },
        {
          "level": 2,
          "title": "Dependencies"
        }
      ],
      "section_count": 10,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/cp",
      "path": "/mnt/c/python/cp/CLAUDE.md",
      "size_bytes": 6134,
      "size_human": "6.0 KB",
      "line_count": 199,
      "word_count": 796,
      "sections": [
        {
          "level": 1,
          "title": "Collection Partner Integration Project"
        },
        {
          "level": 2,
          "title": "Claude Session Guide - START HERE! 👋"
        },
        {
          "level": 2,
          "title": "🎯 Quick Orientation"
        },
        {
          "level": 3,
          "title": "What You're Working With"
        },
        {
          "level": 3,
          "title": "Your Current Location"
        },
        {
          "level": 2,
          "title": "📚 Essential Documentation"
        },
        {
          "level": 2,
          "title": "⚡ Quick Commands"
        },
        {
          "level": 3,
          "title": "Test Database Connection"
        },
        {
          "level": 3,
          "title": "Process Legal Placement File"
        },
        {
          "level": 3,
          "title": "🆕 Launch/Close Collection Partner"
        }
      ],
      "_sections_total": 31,
      "section_count": 31,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/jack_page",
      "path": "/mnt/c/python/jack_page/CLAUDE.md",
      "size_bytes": 858,
      "size_human": "858.0 B",
      "line_count": 21,
      "word_count": 128,
      "sections": [
        {
          "level": 1,
          "title": "CLAUDE.md"
        },
        {
          "level": 2,
          "title": "Build/Test Commands"
        },
        {
          "level": 2,
          "title": "Code Style Guidelines"
        }
      ],
      "section_count": 3,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/kosmos",
      "path": "/mnt/c/python/kosmos/CLAUDE.md",
      "size_bytes": 216,
      "size_human": "216.0 B",
      "line_count": 7,
      "word_count": 33,
      "sections": [
        {
          "level": 1,
          "title": "Claude Code Instructions"
        },
        {
          "level": 2,
          "title": "Commit Guidelines"
        }
      ],
      "section_count": 2,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/prompt_ambiguity_analyzer",
      "path": "/mnt/c/python/prompt_ambiguity_analyzer/CLAUDE.md",
      "size_bytes": 7099,
      "size_human": "6.9 KB",
      "line_count": 173,
      "word_count": 942,
      "sections": [
        {
          "level": 1,
          "title": "CLAUDE.md"
        },
        {
          "level": 2,
          "title": "Project Purpose"
        },
        {
          "level": 2,
          "title": "Primary Workflow: Automated Prompt Analysis"
        },
        {
          "level": 3,
          "title": "Stage 1: Conflict Detection"
        },
        {
          "level": 3,
          "title": "Stage 2: Automatic Disambiguation"
        },
        {
          "level": 3,
          "title": "Critical Requirements"
        },
        {
          "level": 2,
          "title": "Architecture"
        },
        {
          "level": 2,
          "title": "Key Insight: Why This Matters"
        },
        {
          "level": 2,
          "title": "Output Format Example"
        },
        {
          "level": 2,
          "title": "Conflict Analysis"
        }
      ],
      "_sections_total": 22,
      "section_count": 22,
      "includes": [],
      "has_includes": false
    },
    {
      "project": "/mnt/c/python/security_questionnaire",
      "path": "/mnt/c/python/security_questionnaire/CLAUDE.md",
      "size_bytes": 5390,
      "size_human": "5.3 KB",
      "line_count": 148,
      "word_count": 875,
      "sections": [
        {
          "level": 1,
          "title": "Security Questionnaire - Firm Context"
        },
        {
          "level": 2,
          "title": "Organization Details"
        },
        {
          "level": 2,
          "title": "Infrastructure Summary"
        },
        {
          "level": 2,
          "title": "Existing Certifications"
        },
        {
          "level": 2,
          "title": "MSP Relationship"
        },
        {
          "level": 2,
          "title": "Security Stack"
        },
        {
          "level": 2,
          "title": "Discover Relationship Scope"
        },
        {
          "level": 2,
          "title": "Application Environment"
        },
        {
          "level": 2,
          "title": "Key Policies Status"
        },
        {
          "level": 2,
          "title": "Maturity Level Legend"
        }
      ],
      "_sections_total": 12,
      "section_count": 12,
      "includes": [],
      "has_includes": false
    }
  ]
}
```

---

## 18. Mcp Config

**Path:** `<project>/.mcp.json`

**Description:** Model Context Protocol server configuration

### Sample Data

```json
{
  "projects_scanned": 55,
  "projects_with_mcp": 1,
  "total_servers": 2,
  "adoption_rate": 0.01818181818181818,
  "configs": [
    {
      "project": "/mnt/c/python/claude-document-dependency-tracker",
      "config_file": ".mcp.json",
      "servers": [
        {
          "name": "specbuilder",
          "type": "stdio",
          "command": "python3",
          "args": [
            "./mcp_servers/specbuilder/server.py"
          ],
          "env": {},
          "has_env": false
        },
        {
          "name": "cortex",
          "type": "stdio",
          "command": "python3",
          "args": [
            "./.claude/mcp_servers/cortex/server.py"
          ],
          "env": {},
          "has_env": false
        }
      ],
      "server_count": 2
    }
  ]
}
```

---

## 19. Environment

**Path:** Process environment

**Description:** Claude Code environment variables

### Sample Data

```json
{
  "CLAUDECODE": "1",
  "CLAUDE_CODE_ENTRYPOINT": "cli",
  "CLAUDE_PROJECT_DIR": null,
  "CLAUDE_CONFIG_DIR": null,
  "CLAUDE_CODE_ENABLE_TELEMETRY": null,
  "OTEL_METRICS_EXPORTER": null,
  "OTEL_LOGS_EXPORTER": null,
  "OTEL_LOG_USER_PROMPTS": null,
  "MAX_MCP_OUTPUT_TOKENS": null,
  "has_ANTHROPIC_API_KEY": false,
  "has_CLAUDE_CODE_OAUTH_TOKEN": false,
  "_total_vars_set": 2
}
```

---

## 20. Cache

**Path:** `~/.cache/claude/`

**Description:** General cache and staging area

### Sample Data

```json
{
  "cache_exists": true,
  "path": "/home/jim/.cache/claude",
  "total_size_bytes": 0,
  "total_size_human": "0.0 B",
  "file_count": 0,
  "subdirectories": [
    {
      "name": "staging",
      "size_bytes": 0,
      "size_human": "0.0 B",
      "file_count": 0
    }
  ]
}
```

---

## 21. Mcp Logs

**Path:** `~/.cache/claude-cli-nodejs/`

**Description:** MCP server logs with timestamps

### Sample Data

```json
{
  "directory_exists": true,
  "path": "/home/jim/.cache/claude-cli-nodejs",
  "total_projects": 2,
  "total_servers": 3,
  "total_log_files": 13,
  "total_size_bytes": 358948,
  "total_size_human": "350.5 KB",
  "total_errors": 6,
  "projects": [
    {
      "project": "-mnt-c-python-claude-document-dependency-tracker",
      "servers": [
        {
          "server": "specbuilder",
          "log_count": 5,
          "total_size_bytes": 7794,
          "total_size_human": "7.6 KB",
          "total_lines": 196,
          "error_count": 0,
          "log_files": [
            {
              "filename": "2025-12-10T16-23-20-062Z.txt",
              "size_bytes": 1524,
              "line_count": 38,
              "error_count": 0
            },
            {
              "filename": "2025-12-10T03-32-13-040Z.txt",
              "size_bytes": 1283,
              "line_count": 32,
              "error_count": 0
            },
            {
              "filename": "2025-12-10T00-21-52-365Z.txt",
              "size_bytes": 1971,
              "line_count": 50,
              "error_count": 0
            },
            {
              "filename": "2025-12-10T00-19-03-807Z.txt",
              "size_bytes": 1508,
              "line_count": 38,
              "error_count": 0
            },
            {
              "filename": "2025-12-10T00-13-49-730Z.txt",
              "size_bytes": 1508,
              "line_count": 38,
              "error_count": 0
            }
          ]
        },
        {
          "server": "cortex",
          "log_count": 2,
          "total_size_bytes": 1470,
          "total_size_human": "1.4 KB",
          "total_lines": 40,
          "error_count": 4,
          "log_files": [
            {
              "filename": "2025-12-10T16-23-20-062Z.txt",
              "size_bytes": 735,
              "line_count": 20,
              "error_count": 2
            },
            {
              "filename": "2025-12-10T03-32-13-040Z.txt",
              "size_bytes": 735,
              "line_count": 20,
              "error_count": 2
            }
          ]
        }
      ],
      "server_count": 2,
      "total_log_count": 7,
      "total_size_bytes": 9264,
      "total_errors": 4
    },
    {
      "project": "-mnt-c-python-agent-ui",
      "servers": [
        {
          "server": "playwright",
          "log_count": 6,
          "total_size_bytes": 349684,
          "total_size_human": "341.5 KB",
          "total_lines": 9684,
          "error_count": 2,
          "log_files": [
            {
              "filename": "2025-10-09T18-08-33-076Z.txt",
              "size_bytes": 12352,
              "line_count": 344,
              "error_count": 0
            },
            {
              "filename": "2025-10-09T14-15-42-770Z.txt",
              "size_bytes": 101258,
              "line_count": 2810,
              "error_count": 0
            },
            {
              "filename": "2025-10-09T05-17-02-135Z.txt",
              "size_bytes": 232579,
              "line_count": 6434,
              "error_count": 2
            },
            {
              "filename": "2025-10-09T05-08-59-876Z.txt",
              "size_bytes": 1369,
              "line_count": 38,
              "error_count": 0
            },
            {
              "filename": "2025-10-09T05-08-41-037Z.txt",
              "size_bytes": 1369,
              "line_count": 38,
              "error_count": 0
            },
            {
              "filename": "2025-10-09T05-07-42-543Z.txt",
              "size_bytes": 757,
              "line_count": 20,
              "error_count": 0
            }
          ]
        }
      ],
      "server_count": 1,
      "total_log_count": 6,
      "total_size_bytes": 349684,
      "total_errors": 2
    }
  ]
}
```

---

## 22. Statusline

**Path:** Runtime stdin

**Description:** Real-time session data (schema documentation only)

### Sample Data

```json
{
  "source_type": "runtime",
  "availability": "Only available during active Claude Code session",
  "capture_method": "Via custom statusline command configured in settings.json",
  "configuration": {
    "setting": "statusLine.command",
    "example": "~/.claude/statusline-command.sh"
  },
  "schema": {
    "model": {
      "type": "object",
      "properties": {
        "display_name": {
          "type": "string",
          "example": "claude-opus-4-5"
        },
        "id": {
          "type": "string",
          "example": "claude-opus-4-5-20250514"
        }
      }
    },
    "workspace": {
      "type": "object",
      "properties": {
        "current_dir": {
          "type": "string",
          "example": "/home/user/project"
        },
        "project_dir": {
          "type": "string",
          "example": "/home/user/project"
        }
      }
    },
    "version": {
      "type": "string",
      "example": "2.0.69"
    },
    "cost": {
      "type": "object",
      "properties": {
        "total_cost_usd": {
          "type": "float",
          "example": 0.15
        },
        "total_lines_added": {
          "type": "int",
          "example": 150
        },
        "total_lines_removed": {
          "type": "int",
          "example": 45
        }
      }
    },
    "exceeds_200k_tokens": {
      "type": "bool",
      "example": false
    }
  },
  "sample_data": {
    "model": {
      "display_name": "claude-opus-4-5"
    },
    "workspace": {
      "current_dir": "/home/user/project",
      "project_dir": "/home/user/project"
    },
    "version": "2.0.69",
    "cost": {
      "total_cost_usd": 0.15,
      "total_lines_added": 150,
      "total_lines_removed": 45
    },
    "exceeds_200k_tokens": false
  },
  "note": "This is a runtime-only data source. No historical data is stored."
}
```

---

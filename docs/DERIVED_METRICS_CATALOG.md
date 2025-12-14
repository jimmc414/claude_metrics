# Claude Code Derived Metrics Catalog

A comprehensive catalog of 592 derived metrics (D001-D592) that can be computed from Claude Code's raw data.

**Related Documents:**
- [Data Sources](CLAUDE_CODE_DATA_SOURCES.md) - Raw data locations and formats
- [Metrics Catalog](CLAUDE_CODE_METRICS_CATALOG.md) - Raw data schemas and extractable fields

---

## Data Types Reference

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integer count | `42` |
| `float` | Decimal number | `3.14` |
| `ratio` | Proportion (typically 0-1) | `0.75` |
| `percentage` | Percentage (0-100) | `75.0` |
| `duration` | Time measurement | `3600` (seconds) |
| `rate` | Per-time measurement | `5.2` (per hour) |
| `trend` | Directional change over time | `+0.15` (slope) |
| `category` | Classification label | `"Night Owl"` |
| `compound` | Multi-factor composite score | `0.82` |
| `distribution` | Breakdown/histogram | `{"morning": 30, "afternoon": 50}` |
| `correlation` | Statistical relationship (-1 to 1) | `0.67` |
| `probability` | Likelihood (0-1) | `0.85` |
| `binary` | Boolean indicator | `true` |
| `timestamp` | Point in time | `"2024-11-15T10:00:00Z"` |
| `sequence` | Pattern count | `15` |
| `delta` | Change amount | `-5` |
| `inverse` | Inverted ratio | `0.25` |
| `lag` | Time delay | `3` (days) |

---

# Category A: Time & Productivity Metrics (D001-D028)

## A1. Active Time Calculations

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D001 | Active coding hours (daily) | `duration` | Gap-based session detection from timestamps; gaps >15min = new session | Daily time tracking |
| D002 | Active coding hours (weekly) | `duration` | Sum of daily active hours for 7-day window | Weekly reports |
| D003 | Active coding hours (monthly) | `duration` | Sum of daily active hours for 30-day window | Monthly reports |
| D004 | User thinking time | `duration` | Time between user messages within session | Implementation time estimate |
| D005 | Claude response time | `duration` | Time from user message to assistant response | Latency tracking |
| D006 | Session duration | `duration` | Last timestamp - first timestamp per session | Session length analysis |
| D007 | Average session duration | `duration` | Mean of all session durations | Typical work session length |
| D008 | Median session duration | `duration` | Median of session durations | Robust session length |
| D009 | Session duration variance | `float` | Standard deviation of session durations | Consistency measure |
| D010 | Time to first tool use | `duration` | Time from session start to first tool call | Warm-up time |

## A2. Temporal Patterns

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D011 | Peak productivity hour | `int` | Hour with highest message count | Optimal work time |
| D012 | Peak productivity day | `category` | Day of week with highest activity | Weekly patterns |
| D013 | Morning activity ratio | `ratio` | Messages 6am-12pm / total | Work schedule analysis |
| D014 | Afternoon activity ratio | `ratio` | Messages 12pm-6pm / total | Work schedule analysis |
| D015 | Evening activity ratio | `ratio` | Messages 6pm-12am / total | Work schedule analysis |
| D016 | Night activity ratio | `ratio` | Messages 12am-6am / total | Night owl detection |
| D017 | Weekend vs weekday ratio | `ratio` | Weekend messages / weekday messages | Work-life balance |
| D018 | Work style classification | `category` | "Night Owl" vs "Early Bird" based on hourCounts | Personal pattern |
| D019 | Session start time distribution | `distribution` | Histogram of session start hours | When work begins |
| D020 | Session end time distribution | `distribution` | Histogram of session end hours | When work ends |

## A3. Streaks & Consistency

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D021 | Current activity streak | `int` | Consecutive days with activity ending today | Motivation tracking |
| D022 | Longest activity streak | `int` | Maximum consecutive active days | Achievement tracking |
| D023 | Average streak length | `float` | Mean of all streak lengths | Consistency measure |
| D024 | Days since last activity | `int` | Today - last active date | Gap detection |
| D025 | Activity consistency score | `ratio` | 1 - (std dev of daily activity / mean) | Regularity measure |
| D026 | Weekly active days | `int` | Days with activity in past 7 days | Weekly engagement |
| D027 | Monthly active days | `int` | Days with activity in past 30 days | Monthly engagement |
| D028 | Activity density | `rate` | Messages per active day | Intensity measure |

---

# Category B: Tool Usage Metrics (D029-D048)

## B1. Tool Frequency Analysis

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D029 | Tool usage distribution | `distribution` | Percentage of each tool type | Tool preferences |
| D030 | Tool calls per session | `float` | Total tool calls / session count | Automation level |
| D031 | Tool calls per message | `float` | Tool calls / message count | Tool density |
| D032 | Tool calls per hour | `rate` | Tool calls / active hours | Productivity rate |
| D033 | Most used tool | `category` | Tool with highest count | Primary workflow |
| D034 | Least used tool | `category` | Tool with lowest count | Underutilized features |
| D035 | Tool diversity score | `ratio` | Unique tools used / total tools available | Feature adoption |
| D036 | Daily tool call trend | `trend` | Tool calls over time (slope) | Usage trajectory |

## B2. Tool Efficiency Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D037 | Tool success rate | `ratio` | Successful calls / total calls | Reliability |
| D038 | Tool error rate | `ratio` | Failed calls / total calls | Problem areas |
| D039 | Tool success rate by type | `distribution` | Success rate per tool | Per-tool reliability |
| D040 | Average tool execution time | `duration` | Mean of durationMs | Performance |
| D041 | Median tool execution time | `duration` | Median of durationMs | Robust performance |
| D042 | Slowest tool type | `category` | Tool with highest avg durationMs | Bottleneck ID |
| D043 | Tool timeout rate | `ratio` | Timeouts / total calls | Reliability issues |
| D044 | Tool retry rate | `ratio` | Repeated calls / total calls | Error recovery |

## B3. Tool Co-occurrence

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D045 | Read-before-Edit ratio | `ratio` | Read calls preceding Edit / total Edits | Best practice adherence |
| D046 | Grep-then-Read pattern | `int` | Grep followed by Read count | Search workflow |
| D047 | Tool sequence patterns | `distribution` | Common tool call sequences | Workflow analysis |
| D048 | Tool clustering | `distribution` | Tools frequently used together | Feature grouping |

---

# Category C: File Operation Metrics (D049-D073)

## C1. File Access Patterns

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D049 | Unique files touched | `int` | Count of distinct file paths | Project scope |
| D050 | Files per session | `float` | Unique files / session count | Session complexity |
| D051 | Most read files | `distribution` | Top N by read count | Reference hotspots |
| D052 | Most edited files | `distribution` | Top N by edit count | Change hotspots |
| D053 | Most written files | `distribution` | Top N by write count | Creation hotspots |
| D054 | File read/write ratio | `ratio` | Read count / (Edit + Write count) | Read vs modify |
| D055 | Edit vs Write ratio | `ratio` | Edit count / Write count | Modify vs create |
| D056 | Files read but never edited | `int` | Read-only files | Reference-only files |
| D057 | Files edited without reading | `int` | Edits without prior Read | Risky edits |

## C2. File Type Analysis

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D058 | File type distribution | `distribution` | Count by file extension | Language focus |
| D059 | Python file ratio | `ratio` | .py files / total | Python focus |
| D060 | JavaScript file ratio | `ratio` | .js/.ts files / total | JS/TS focus |
| D061 | Markdown file ratio | `ratio` | .md files / total | Documentation focus |
| D062 | Config file ratio | `ratio` | .json/.yaml/.toml / total | Configuration work |
| D063 | Code vs config ratio | `ratio` | Code files / config files | Work type |
| D064 | Test file ratio | `ratio` | *test*.py, *spec*.js / total | Testing focus |

## C3. File Revision Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D065 | Average versions per file | `float` | Mean of version numbers | Iteration intensity |
| D066 | Max versions for any file | `int` | Highest version number | Most iterated file |
| D067 | Files with 5+ revisions | `int` | Count of highly revised files | Refinement areas |
| D068 | Files with 10+ revisions | `int` | Count of very highly revised | Iteration hotspots |
| D069 | Revision rate over time | `rate` | Versions created per day | Editing velocity |
| D070 | File churn rate | `rate` | (Creates + Edits) / time period | Change velocity |

## C4. File Co-modification

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D071 | Files modified together | `distribution` | Files changed in same session | Coupling detection |
| D072 | File dependency graph | `distribution` | Co-modification network | Architecture insight |
| D073 | Module coupling score | `float` | Cross-module co-modifications | Design quality |

---

# Category D: Model & Token Metrics (D074-D109)

## D1. Model Usage Patterns

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D074 | Model usage distribution | `distribution` | Percentage by model | Model preferences |
| D075 | Opus usage ratio | `ratio` | Opus calls / total | Premium model usage |
| D076 | Sonnet usage ratio | `ratio` | Sonnet calls / total | Standard model usage |
| D077 | Haiku usage ratio | `ratio` | Haiku calls / total | Fast model usage |
| D078 | Model switching frequency | `rate` | Model changes per session | Flexibility |
| D079 | Model preference trend | `trend` | Model usage over time | Preference shifts |
| D080 | Agent model distribution | `distribution` | Model usage by subagent type | Agent optimization |

## D2. Token Economics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D081 | Tokens per message | `float` | Output tokens / message count | Verbosity |
| D082 | Tokens per session | `float` | Total tokens / session count | Session cost |
| D083 | Tokens per hour | `rate` | Total tokens / active hours | Hourly consumption |
| D084 | Tokens per tool call | `float` | Tokens / tool calls | Tool token cost |
| D085 | Input/output token ratio | `ratio` | Input tokens / output tokens | Prompt efficiency |
| D086 | Daily token consumption | `int` | Sum of tokens per day | Daily spend |
| D087 | Weekly token consumption | `int` | 7-day rolling token sum | Weekly spend |
| D088 | Token growth rate | `trend` | Daily token trend (slope) | Consumption trajectory |

## D3. Cache Efficiency

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D089 | Cache hit ratio | `ratio` | Cache read / (cache read + input) | Cache effectiveness |
| D090 | Cache creation ratio | `ratio` | Cache creation / total tokens | Cache investment |
| D091 | Cache efficiency score | `ratio` | Cache read / cache creation | ROI on caching |
| D092 | Ephemeral cache usage | `ratio` | Ephemeral tokens / total cache | Short-term caching |
| D093 | Cache savings estimate | `float` | Cache read tokens * price differential | Cost savings |

## D4. Cost Estimation

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D094 | Estimated Opus cost | `float` | Opus output * $75/M | Opus spending |
| D095 | Estimated Sonnet cost | `float` | Sonnet output * $15/M | Sonnet spending |
| D096 | Estimated Haiku cost | `float` | Haiku output * $1.25/M | Haiku spending |
| D097 | Total estimated cost | `float` | Sum of model costs | Total spending |
| D098 | Cost per session | `float` | Total cost / sessions | Per-session cost |
| D099 | Cost per hour | `float` | Total cost / active hours | Hourly rate |
| D100 | Cost per day | `float` | Daily token costs | Daily spending |
| D101 | Projected monthly cost | `float` | Daily avg * 30 | Budget projection |
| D102 | Cost trend | `trend` | Cost over time (slope) | Spending trajectory |

## D5. Additional Token Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D103 | User/assistant message ratio | `ratio` | User messages / assistant messages | Conversation balance |
| D104 | Average user message length | `float` | Mean chars of user messages | User verbosity |
| D105 | Average assistant response length | `float` | Mean chars of assistant text | Response verbosity |
| D106 | User message length variance | `float` | Std dev of user message lengths | Consistency |
| D107 | Longest user message | `int` | Max user message length | Complex requests |
| D108 | Shortest user message | `int` | Min user message length (>0) | Quick commands |
| D109 | Messages per session | `float` | Total messages / sessions | Session depth |

---

# Category E: Conversation Analysis Metrics (D110-D136)

## E1. Message Patterns

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D110 | Conversation depth | `int` | Max message chain length | Thread complexity |
| D111 | Questions asked by user | `int` | Messages containing "?" | Inquiry rate |
| D112 | Question ratio | `ratio` | Questions / total user messages | Exploration mode |
| D113 | Commands given | `int` | Imperative messages ("do X") | Directive mode |
| D114 | Code pastes by user | `int` | Messages with ``` or len > 500 | Context provision |
| D115 | Error reports by user | `int` | Messages with "error", "traceback" | Debugging frequency |
| D116 | Frustration indicators | `int` | "wrong", "still not", "doesn't work" | Pain points |
| D117 | Gratitude expressions | `int` | "thanks", "perfect", "great" | Satisfaction |
| D118 | Frustration/gratitude ratio | `ratio` | Frustration / gratitude count | Sentiment balance |

## E2. Topic Analysis

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D119 | Bug-related messages | `int` | Messages with bug/error/fix keywords | Debugging work |
| D120 | Feature-related messages | `int` | Messages with add/create/implement keywords | Feature work |
| D121 | Refactor-related messages | `int` | Messages with refactor/clean/improve | Maintenance work |
| D122 | Test-related messages | `int` | Messages with test/pytest/coverage | Testing work |
| D123 | Docs-related messages | `int` | Messages with document/readme/comment | Documentation work |
| D124 | Debug-related messages | `int` | Messages with debug/why/trace | Investigation work |
| D125 | Review-related messages | `int` | Messages with review/check/examine | Review work |
| D126 | Topic distribution | `distribution` | Percentage by topic category | Work focus |
| D127 | Topic trend over time | `trend` | Topic frequency over sessions | Focus shifts |

## E3. Extended Thinking Analysis

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D128 | Sessions with thinking | `ratio` | Sessions containing thinking blocks / total | Thinking usage |
| D129 | Thinking blocks per session | `float` | Thinking block count / sessions | Thinking intensity |
| D130 | Average thinking length | `float` | Mean chars of thinking content | Reasoning depth |
| D131 | Median thinking length | `float` | Median of thinking lengths | Typical reasoning |
| D132 | Max thinking length | `int` | Longest thinking block | Deepest reasoning |
| D133 | Thinking token percentage | `ratio` | Thinking tokens / total output | Reasoning investment |
| D134 | ULTRATHINK trigger count | `int` | Triggers with text="ULTRATHINK" | Deep thinking requests |
| D135 | Thinking level distribution | `distribution` | Count by thinkingMetadata.level | Thinking modes |
| D136 | Thinking disabled rate | `ratio` | disabled=true / total | Thinking opt-out |

---

# Category F: Thinking & Complexity Metrics (D137-D142)

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D137 | Thinking length trend | `trend` | Thinking length over time | Complexity trend |
| D138 | Sidechain exploration rate | `ratio` | isSidechain=true / total | Alternative exploration |
| D139 | Conversation compaction rate | `ratio` | Compaction events / sessions | Long conversation rate |
| D140 | Context clearing frequency | `rate` | Context management events / sessions | Context pressure |
| D141 | Tokens cleared per compaction | `float` | Mean cleared_input_tokens | Context savings |
| D142 | Multi-turn problem rate | `ratio` | Sessions with >20 messages | Complex problems |

---

# Category G: Task Management Metrics (D143-D158)

## G1. Todo Completion

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D143 | Total todos created | `int` | Sum of all todo items | Task volume |
| D144 | Completed todos | `int` | status="completed" count | Completion volume |
| D145 | Overall completion rate | `ratio` | Completed / total todos | Success rate |
| D146 | In-progress (abandoned) | `int` | status="in_progress" never completed | Abandonment |
| D147 | Pending (never started) | `int` | status="pending" count | Unstarted work |
| D148 | Abandonment rate | `ratio` | In-progress / (completed + in-progress) | Follow-through |
| D149 | Average tasks per session | `float` | Todos / sessions with todos | Task granularity |
| D150 | Max tasks in session | `int` | Highest todo count in one session | Most complex session |
| D151 | High priority ratio | `ratio` | High priority / total | Urgency level |

## G2. Planning Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D152 | Plans created | `int` | Count of plan files | Planning frequency |
| D153 | Average plan size | `float` | Mean plan file size | Plan complexity |
| D154 | Plan complexity score | `compound` | Headers * code blocks * size | Overall complexity |
| D155 | Technologies per plan | `int` | Unique tech keywords per plan | Tech breadth |
| D156 | Action words per plan | `int` | Implementation verbs count | Action density |
| D157 | Plan approval rate | `ratio` | ExitPlanMode / EnterPlanMode | Plan acceptance |
| D158 | Planning to execution ratio | `ratio` | Plans / features implemented | Planning overhead |

---

# Category H: Agent & Delegation Metrics (D159-D172)

## H1. Subagent Usage

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D159 | Agent sessions | `int` | Count of agent-*.jsonl files | Agent usage |
| D160 | Main vs agent ratio | `ratio` | Main sessions / agent sessions | Delegation level |
| D161 | Agent usage percentage | `percentage` | Agent sessions / total * 100 | Delegation rate |
| D162 | Subagent type distribution | `distribution` | Count by subagent_type | Agent preferences |
| D163 | Most used subagent | `category` | Highest subagent_type count | Primary agent |
| D164 | Explore agent usage | `int` | Explore type count | Research delegation |
| D165 | Plan agent usage | `int` | Plan type count | Planning delegation |
| D166 | Custom agent usage | `int` | Non-built-in agent count | Custom agent adoption |

## H2. Agent Efficiency

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D167 | Tokens per agent task | `float` | Agent totalTokens / agent calls | Agent token cost |
| D168 | Tools per agent task | `float` | Agent totalToolUseCount / agent calls | Agent tool usage |
| D169 | Agent success rate | `ratio` | Successful agent completions / total | Agent reliability |
| D170 | Agent resume rate | `ratio` | Resume parameter usage / total agents | Continuation rate |
| D171 | Parallel agent frequency | `int` | Multiple Task calls in one message | Parallelization |
| D172 | Agent depth | `int` | Nested agent spawns | Delegation depth |

---

# Category I: Project Metrics (D173-D188)

## I1. Project Activity

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D173 | Total projects | `int` | Unique cwd values | Project count |
| D174 | Sessions per project | `distribution` | Session count by cwd | Project activity |
| D175 | Most active project | `category` | Highest session count | Primary project |
| D176 | Messages per project | `distribution` | Message count by cwd | Project engagement |
| D177 | Time per project | `distribution` | Active hours by cwd | Project investment |
| D178 | Tools per project | `distribution` | Tool calls by cwd | Project complexity |

## I2. Git Activity

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D179 | Branches worked on | `int` | Unique gitBranch values | Branch diversity |
| D180 | Main/master activity | `int` | Activity on main branches | Core work |
| D181 | Feature branch activity | `int` | Activity on non-main branches | Feature work |
| D182 | Branch switching frequency | `rate` | Branch changes per session | Context switching |
| D183 | Empty branch sessions | `int` | gitBranch="" count | Untracked work |

## I3. Project Complexity

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D184 | Files per project | `distribution` | Unique files by project | Project scope |
| D185 | Tool diversity per project | `distribution` | Unique tools by project | Work variety |
| D186 | Session depth per project | `distribution` | Avg messages per session by project | Engagement depth |
| D187 | Multi-project sessions | `int` | Sessions spanning multiple cwd | Cross-project work |
| D188 | Project switching frequency | `rate` | cwd changes per day | Project juggling |

---

# Category J: Error & Recovery Metrics (D189-D203)

## J1. Error Rates

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D189 | Overall error rate | `ratio` | Errors / total tool calls | Reliability |
| D190 | Bash error rate | `ratio` | Bash errors / Bash calls | Command reliability |
| D191 | Edit conflict rate | `ratio` | Edit errors / Edit calls | Edit reliability |
| D192 | Read failure rate | `ratio` | Read errors / Read calls | File access issues |
| D193 | Permission error rate | `ratio` | Permission errors / total | Access issues |
| D194 | API error rate | `ratio` | isApiErrorMessage / total | API reliability |

## J2. Recovery Patterns

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D195 | Error recovery rate | `ratio` | Errors followed by success / errors | Recovery ability |
| D196 | Retry success rate | `ratio` | Successful retries / total retries | Retry effectiveness |
| D197 | Errors per session | `float` | Total errors / sessions | Session reliability |
| D198 | Error clustering | `int` | Sessions with multiple errors | Problem sessions |
| D199 | Time to recovery | `duration` | Time from error to success | Recovery speed |

## J3. Interruption Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D200 | Interrupted operations | `int` | interrupted=true count | Interruption rate |
| D201 | Truncated outputs | `int` | truncated=true count | Output limits hit |
| D202 | Killed shells | `int` | KillShell count | Manual interrupts |
| D203 | Hook prevention rate | `ratio` | preventedContinuation / hook executions | Hook blocking |

---

# Category K: Code Generation Metrics (D204-D228)

## K1. Code Volume

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D204 | Total code generated (KB) | `float` | Sum of code block sizes | Code volume |
| D205 | Code blocks generated | `int` | Count of ``` blocks | Code frequency |
| D206 | Average code block size | `float` | Mean block size | Typical code size |
| D207 | Largest code block | `int` | Max block size | Biggest generation |
| D208 | Code per session | `float` | Code KB / sessions | Session output |
| D209 | Code per hour | `rate` | Code KB / active hours | Code velocity |

## K2. Language Distribution

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D210 | Python code ratio | `ratio` | Python blocks / total | Python focus |
| D211 | JavaScript code ratio | `ratio` | JS blocks / total | JS focus |
| D212 | TypeScript code ratio | `ratio` | TS blocks / total | TS focus |
| D213 | Bash code ratio | `ratio` | Bash blocks / total | Scripting focus |
| D214 | JSON code ratio | `ratio` | JSON blocks / total | Data focus |
| D215 | Markdown code ratio | `ratio` | MD blocks / total | Docs focus |
| D216 | Language diversity | `int` | Unique languages used | Language breadth |

## K3. Code Quality Proxies

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D217 | Functions defined | `int` | def/function pattern matches | Function creation |
| D218 | Classes defined | `int` | class pattern matches | Class creation |
| D219 | Functions per session | `float` | Functions / sessions | Session complexity |
| D220 | Classes per session | `float` | Classes / sessions | OOP usage |
| D221 | Import statements | `int` | import/require matches | Dependency usage |
| D222 | Comment density | `ratio` | Comment lines / code lines | Documentation |
| D223 | Docstring presence | `ratio` | Docstring patterns / functions | Documentation rate |

## K4. Edit Analysis

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D224 | Net lines added | `int` | Lines in new_string - old_string | Code growth |
| D225 | Net lines removed | `int` | Lines in old_string - new_string | Code reduction |
| D226 | Code churn | `int` | Added + removed lines | Change volume |
| D227 | Replace all usage | `int` | replace_all=true count | Bulk changes |
| D228 | Average edit size | `float` | Mean (new_string - old_string) size | Edit granularity |

---

# Category L: Web Research Metrics (D229-D238)

## L1. Search Patterns

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D229 | Web searches per session | `float` | WebSearch / sessions | Research intensity |
| D230 | Web fetches per session | `float` | WebFetch / sessions | Documentation access |
| D231 | Research intensity | `float` | (Search + Fetch) / session | Overall research |
| D232 | External dependency | `ratio` | Web tools / total tools | External reliance |
| D233 | Search topics | `distribution` | Query keyword extraction | Research areas |

## L2. Domain Analysis

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D234 | Documentation site ratio | `ratio` | docs.* fetches / total | Official docs usage |
| D235 | GitHub ratio | `ratio` | github.com fetches / total | GitHub reliance |
| D236 | Stack Overflow ratio | `ratio` | stackoverflow.com / total | Community help |
| D237 | Domain diversity | `int` | Unique domains fetched | Source variety |
| D238 | Most accessed domain | `category` | Highest fetch count domain | Primary source |

---

# Category M: Hook & Customization Metrics (D239-D252)

## M1. Hook Usage

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D239 | Sessions with hooks | `int` | hookCount > 0 sessions | Hook adoption |
| D240 | Average hooks per session | `float` | Mean hookCount | Hook intensity |
| D241 | Hook error rate | `ratio` | hookErrors count / total hooks | Hook reliability |
| D242 | Hook prevention rate | `ratio` | preventedContinuation / hooks | Blocking hooks |
| D243 | Unique hook commands | `int` | Distinct hookInfos.command | Hook variety |

## M2. Customization Level

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D244 | Custom agents defined | `int` | Count of agents/*.md | Agent customization |
| D245 | Custom commands defined | `int` | Count of commands/*.md | Command customization |
| D246 | Custom skills defined | `int` | Count of skills/*/ | Skill customization |
| D247 | Total customizations | `int` | Agents + commands + skills | Customization level |
| D248 | Permission rules defined | `int` | Count of allow/deny rules | Security config |
| D249 | Auto-allow rules | `int` | Allow rules count | Automation level |

## M3. Additional Hook Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D250 | Questions asked by Claude | `int` | AskUserQuestion count | Clarification needs |
| D251 | Questions per session | `float` | AskUserQuestion / sessions | Interaction rate |
| D252 | Multi-select questions | `int` | multiSelect=true count | Complex choices |

---

# Category N: User Interaction Metrics (D253-D259)

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D253 | Unique question topics | `int` | Distinct question headers | Decision areas |
| D254 | Most common decisions | `distribution` | Frequent question patterns | Key decision points |
| D255 | Answer capture rate | `ratio` | Questions with answers / total | Response rate |
| D256 | "Yes" response rate | `ratio` | Affirmative answers / total | Approval rate |
| D257 | "Other" response rate | `ratio` | Custom answers / total | Custom choices |
| D258 | First option selection rate | `ratio` | First option chosen / total | Default acceptance |
| D259 | Decision time estimate | `duration` | Time before answer / questions | Decision speed |

---

# Category O: Advanced Derived Metrics (D260-D300)

## O1. Productivity Scores

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D260 | Focus score | `ratio` | Deep sessions (>30min) / total | Deep work ratio |
| D261 | Iteration index | `float` | Avg file versions per task | Perfectionism measure |
| D262 | Self-sufficiency ratio | `ratio` | Tasks without errors / total | Independence |
| D263 | Code velocity | `rate` | KB generated per active hour | Output speed |
| D264 | Pair programming score | `float` | Message density per session | Interaction intensity |
| D265 | Context efficiency | `ratio` | Cache hits / total context | Memory efficiency |

## O2. Quality Indicators

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D266 | Documentation debt ratio | `ratio` | Code generated / docs generated | Docs balance |
| D267 | Test coverage proxy | `ratio` | Test file touches / code file touches | Testing culture |
| D268 | Refactoring frequency | `ratio` | Refactor messages / total | Maintenance habit |
| D269 | Code review engagement | `ratio` | Review messages / total | Review culture |
| D270 | Error learning curve | `trend` | Error rate trend over time | Skill improvement |

## O3. Behavioral Patterns

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D271 | Consistency score | `ratio` | 1 - (std dev daily activity / mean) | Regularity |
| D272 | Deep work ratio | `ratio` | Sessions >1hr / total sessions | Focus time |
| D273 | Context switching rate | `rate` | Project changes per hour | Multitasking |
| D274 | Burnout indicators | `compound` | Late night + high activity + declining | Health warning |
| D275 | Flow state indicator | `compound` | Long sessions + low errors + high output | Optimal state |

## O4. Comparative Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D276 | Week-over-week message change | `percentage` | (This week - last week) / last week | Trend |
| D277 | Week-over-week session change | `percentage` | Session count comparison | Trend |
| D278 | Week-over-week tool change | `percentage` | Tool usage comparison | Trend |
| D279 | Week-over-week cost change | `percentage` | Cost comparison | Trend |
| D280 | Month-over-month growth | `percentage` | Monthly activity comparison | Growth |

## O5. Predictive Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D281 | Projected monthly tokens | `int` | Daily avg * 30 | Budget forecast |
| D282 | Projected monthly cost | `float` | Daily cost avg * 30 | Cost forecast |
| D283 | Session completion likelihood | `probability` | Historical completion rate | Success prediction |
| D284 | Error probability | `probability` | Error rate trends | Risk assessment |
| D285 | Feature adoption score | `ratio` | New tools used / available | Adoption prediction |

## O6. Cross-Reference Metrics

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D286 | Search-to-implementation ratio | `ratio` | Code after WebSearch / searches | Research effectiveness |
| D287 | Plan-to-completion ratio | `ratio` | Completed plans / created plans | Planning effectiveness |
| D288 | Agent-to-outcome ratio | `ratio` | Successful agent results / spawns | Agent effectiveness |
| D289 | Read-to-edit ratio | `ratio` | Edits after reads / reads | Read utilization |
| D290 | Error-to-recovery time | `duration` | Avg time from error to success | Recovery efficiency |

## O7. Session Classification

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D291 | Debugging sessions | `int` | Sessions with high error messages | Session typing |
| D292 | Feature sessions | `int` | Sessions with create/implement | Session typing |
| D293 | Research sessions | `int` | Sessions with high WebSearch | Session typing |
| D294 | Refactoring sessions | `int` | Sessions with refactor keywords | Session typing |
| D295 | Documentation sessions | `int` | Sessions with high .md touches | Session typing |

## O8. Efficiency Correlations

| ID | Metric | Type | Calculation | Use Case |
|----|--------|------|-------------|----------|
| D296 | Thinking-to-success correlation | `correlation` | Success rate vs thinking usage | Thinking value |
| D297 | Planning-to-completion correlation | `correlation` | Completion vs planning usage | Planning value |
| D298 | Agent-to-speed correlation | `correlation` | Time saved with agents | Agent value |
| D299 | Cache-to-cost correlation | `correlation` | Cost reduction vs cache usage | Cache value |
| D300 | Error-to-time correlation | `correlation` | Time impact of errors | Error cost |

---

# Category P: Global State & Project Metrics (D301-D343)

## P1. Startup & Usage (D301-D304)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D301 | Total startups | `int` | numStartups | ~/.claude.json | Overall usage |
| D302 | Prompt queue usage | `int` | promptQueueUseCount | ~/.claude.json | Feature adoption |
| D303 | Memory feature usage | `int` | memoryUsageCount | ~/.claude.json | Feature adoption |
| D304 | Onboarding completion | `binary` | hasCompletedOnboarding | ~/.claude.json | Setup completion |

## P2. Feature Discovery (D305-D308)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D305 | Tips seen | `int` | Count of tipsHistory keys | ~/.claude.json | Feature awareness |
| D306 | Feature discovery rate | `ratio` | Tips seen / available tips | ~/.claude.json | Discovery % |
| D307 | Most shown tip | `category` | Max value in tipsHistory | ~/.claude.json | Reinforced feature |
| D308 | Tip exposure ratio | `ratio` | Total tip shows / startups | ~/.claude.json | Engagement |

## P3. Feature Flags (D309-D310)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D309 | Enabled feature flags | `int` | Count true in cachedStatsigGates | ~/.claude.json | Feature access |
| D310 | Feature flag ratio | `ratio` | Enabled / total flags | ~/.claude.json | Access level |

## P4. Per-Project Analytics (D311-D320)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D311 | Total projects tracked | `int` | Count of projects keys | ~/.claude.json | Project count |
| D312 | Projects with MCP | `int` | Projects with mcpServers defined | ~/.claude.json | MCP adoption |
| D313 | Trusted projects | `int` | hasTrustDialogAccepted = true | ~/.claude.json | Trust level |
| D314 | Project-level cost | `float` | lastCost per project | ~/.claude.json | Per-project spend |
| D315 | Total cost across projects | `float` | Sum of all lastCost | ~/.claude.json | Total spend |
| D316 | Most expensive project | `float` | Max lastCost | ~/.claude.json | Cost hotspot |
| D317 | Project lines impact | `int` | lastLinesAdded + lastLinesRemoved | ~/.claude.json | Code impact |
| D318 | Project code velocity | `rate` | Lines / duration per project | ~/.claude.json | Productivity |
| D319 | Project API efficiency | `ratio` | Tokens / cost per project | ~/.claude.json | Efficiency |
| D320 | React vulnerability exposure | `int` | Projects with detected=true | ~/.claude.json | Security risk |

## P5. Subscription & Rate Limits (D321-D323)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D321 | Subscription type | `category` | subscriptionType | credentials.json | Plan level |
| D322 | Rate limit tier | `category` | rateLimitTier | credentials.json | Limit level |
| D323 | Token expiration | `duration` | expiresAt - now | credentials.json | Time to refresh |

## P6. Versions (D324-D327)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D324 | Installed versions | `int` | Count of version files | versions/ | Version count |
| D325 | Version disk usage | `int` | Total size of versions | versions/ | Storage used |
| D326 | Version update frequency | `rate` | Version timestamps | versions/ | Update rate |
| D327 | Current version | `category` | lastOnboardingVersion | ~/.claude.json | Active version |

## P7. CLAUDE.md Metrics (D328-D330)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D328 | Projects with CLAUDE.md | `int` | Count of CLAUDE.md files | File scan | Instruction adoption |
| D329 | CLAUDE.md size | `int` | File sizes | File scan | Instruction depth |
| D330 | Instruction complexity | `int` | Line/word count | File scan | Complexity |

## P8. Project Customization (D331-D337)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D331 | Projects with custom agents | `int` | Count of .claude/agents/ dirs | File scan | Agent adoption |
| D332 | Projects with custom commands | `int` | Count of .claude/commands/ dirs | File scan | Command adoption |
| D333 | Projects with custom skills | `int` | Count of .claude/skills/ dirs | File scan | Skill adoption |
| D334 | Projects with MCP servers | `int` | Count of .mcp.json files | File scan | MCP adoption |
| D335 | Custom permission rules | `int` | Count per project | settings.local | Security config |
| D336 | MCP servers defined | `int` | Total across projects | .mcp.json | MCP scale |
| D337 | Project customization score | `compound` | Agents + commands + skills + CLAUDE.md | Multiple | Customization depth |

## P9. MCP Server Logs (D338-D340)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D338 | MCP server log count | `int` | Count of log files per server | cache logs | MCP activity |
| D339 | MCP server usage frequency | `rate` | Logs per server per day | cache logs | MCP intensity |
| D340 | MCP errors | `int` | Error patterns in logs | cache logs | MCP reliability |

## P10. Statusline Real-Time Data (D341-D343)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D341 | Real-time session cost | `float` | cost.total_cost_usd | statusline JSON | Live cost |
| D342 | Real-time lines changed | `int` | lines_added + lines_removed | statusline JSON | Live impact |
| D343 | Context overflow indicator | `binary` | exceeds_200k_tokens | statusline JSON | Context limit |

---

# Category Q: Startup & Usage Metrics (D344-D348)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D344 | Total startups | `int` | numStartups | ~/.claude.json | Overall usage |
| D345 | Startups per day | `rate` | numStartups / days since first | ~/.claude.json | Usage frequency |
| D346 | Startup trend | `trend` | numStartups change over time | ~/.claude.json | Adoption curve |
| D347 | Prompt queue adoption | `ratio` | promptQueueUseCount / numStartups | ~/.claude.json | Feature adoption |
| D348 | Memory feature adoption | `ratio` | memoryUsageCount / numStartups | ~/.claude.json | Feature adoption |

---

# Category R: Feature Discovery Metrics (D349-D357)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D349 | Tips seen count | `int` | len(tipsHistory) | ~/.claude.json | Feature awareness |
| D350 | Tips available | `int` | Total known tips (~30) | ~/.claude.json | Potential discovery |
| D351 | Feature discovery rate | `ratio` | Tips seen / tips available | ~/.claude.json | % features discovered |
| D352 | Most shown tip | `category` | max(tipsHistory values) | ~/.claude.json | What's reinforced |
| D353 | Least engaged tip | `int` | Tips with count=1 | ~/.claude.json | Ignored features |
| D354 | Tip engagement score | `float` | avg(tipsHistory values) | ~/.claude.json | Engagement depth |
| D355 | Advanced feature discovery | `int` | Custom agents + commands tips | ~/.claude.json | Power user indicator |
| D356 | Shortcut awareness | `int` | double-esc + shift-tab tips | ~/.claude.json | Efficiency potential |
| D357 | Feature category adoption | `distribution` | Tips grouped by category | ~/.claude.json | Feature area focus |

---

# Category S: Feature Flag Metrics (D358-D362)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D358 | Enabled flags count | `int` | Count true in cachedStatsigGates | ~/.claude.json | Feature access |
| D359 | Disabled flags count | `int` | Count false in cachedStatsigGates | ~/.claude.json | Restricted features |
| D360 | Feature flag ratio | `ratio` | enabled / total | ~/.claude.json | Access level |
| D361 | Beta feature access | `int` | Specific beta flags enabled | ~/.claude.json | Early adopter status |
| D362 | Security flags enabled | `int` | Security-related flags | ~/.claude.json | Security posture |

---

# Category T: Per-Project Analytics (D363-D395)

## T1. Cost Analysis

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D363 | Total cost all projects | `float` | sum(projects.*.lastCost) | ~/.claude.json | Overall spending |
| D364 | Most expensive project | `float` | max(projects.*.lastCost) | ~/.claude.json | Cost hotspot |
| D365 | Least expensive project | `float` | min(projects.*.lastCost) | ~/.claude.json | Efficient projects |
| D366 | Cost per project | `distribution` | lastCost per project | ~/.claude.json | Project spending |
| D367 | Cost variance | `float` | std dev of lastCost | ~/.claude.json | Spending consistency |
| D368 | Cost percentile rank | `distribution` | Project cost percentile | ~/.claude.json | Relative spending |

## T2. Code Impact Analysis

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D369 | Total lines added all projects | `int` | sum(lastLinesAdded) | ~/.claude.json | Total code generated |
| D370 | Total lines removed all projects | `int` | sum(lastLinesRemoved) | ~/.claude.json | Total code removed |
| D371 | Net code impact | `int` | Added - removed | ~/.claude.json | Code growth |
| D372 | Code churn by project | `distribution` | Added + removed per project | ~/.claude.json | Change intensity |
| D373 | Lines per dollar | `ratio` | Lines / cost per project | ~/.claude.json | Cost efficiency |
| D374 | Most productive project | `category` | Highest lines/cost ratio | ~/.claude.json | Best ROI |

## T3. Time Analysis

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D375 | Longest session project | `category` | max(lastDuration) | ~/.claude.json | Deep work location |
| D376 | API time ratio | `ratio` | lastAPIDuration / lastDuration | ~/.claude.json | API vs thinking |
| D377 | Tool time ratio | `ratio` | lastToolDuration / lastDuration | ~/.claude.json | Automation level |
| D378 | Retry overhead | `duration` | APIDuration - APIDurationWithoutRetries | ~/.claude.json | Retry cost |
| D379 | Time efficiency | `ratio` | Lines / duration per project | ~/.claude.json | Productivity rate |

## T4. Token Analysis by Project

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D380 | Input/output ratio by project | `distribution` | Input / output tokens | ~/.claude.json | Prompt efficiency |
| D381 | Cache efficiency by project | `distribution` | CacheRead / (CacheRead + Input) | ~/.claude.json | Cache hits |
| D382 | Token density | `rate` | Tokens / duration | ~/.claude.json | Token rate |
| D383 | Model mix by project | `distribution` | lastModelUsage breakdown | ~/.claude.json | Model preferences |
| D384 | Opus vs Sonnet ratio by project | `distribution` | Model token comparison | ~/.claude.json | Quality vs speed |

## T5. Security & Trust

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D385 | Trusted projects count | `int` | Count hasTrustDialogAccepted=true | ~/.claude.json | Trust adoption |
| D386 | Untrusted projects | `int` | Count hasTrustDialogAccepted=false | ~/.claude.json | Trust resistance |
| D387 | Projects with vulnerabilities | `int` | reactVulnerabilityCache.detected=true | ~/.claude.json | Security issues |
| D388 | Crawl-disabled projects | `int` | dontCrawlDirectory=true count | ~/.claude.json | Privacy-sensitive |

## T6. MCP Adoption

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D389 | Projects with MCP servers | `int` | Count with mcpServers defined | ~/.claude.json | MCP adoption |
| D390 | Total MCP servers | `int` | Sum of mcpServers across projects | ~/.claude.json | MCP scale |
| D391 | MCP servers per project | `float` | Avg mcpServers count | ~/.claude.json | MCP intensity |
| D392 | Most MCP-heavy project | `category` | Max mcpServers count | ~/.claude.json | Integration hub |

## T7. Onboarding Analysis

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D393 | Onboarding completion rate | `ratio` | Completed / total projects | ~/.claude.json | Adoption success |
| D394 | Onboarding friction score | `float` | Avg onboardingSeenCount | ~/.claude.json | Adoption difficulty |
| D395 | High-friction projects | `int` | onboardingSeenCount > 3 | ~/.claude.json | Problem projects |

---

# Category U: Subscription & Rate Limit Metrics (D396-D399)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D396 | Subscription tier | `category` | subscriptionType | credentials.json | Plan level |
| D397 | Rate limit tier | `category` | rateLimitTier | credentials.json | Rate limit level |
| D398 | Token freshness | `duration` | expiresAt - now | credentials.json | Time until refresh |
| D399 | Scope count | `int` | len(scopes) | credentials.json | Permission breadth |

---

# Category V: Project Customization Metrics (D400-D411)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D400 | Projects with CLAUDE.md | `int` | Count of CLAUDE.md files | File scan | Instruction adoption |
| D401 | CLAUDE.md total size | `int` | Sum of file sizes | File scan | Instruction depth |
| D402 | Avg CLAUDE.md size | `float` | Mean file size | File scan | Typical complexity |
| D403 | Projects with custom agents | `int` | Count with agent dirs | .claude/agents/ | Agent adoption |
| D404 | Custom agents defined | `int` | Total agent count | .claude/agents/*.md | Agent scale |
| D405 | Projects with custom commands | `int` | Count with command dirs | .claude/commands/ | Command adoption |
| D406 | Custom commands defined | `int` | Total command count | .claude/commands/*.md | Command scale |
| D407 | Projects with custom skills | `int` | Count with skill dirs | .claude/skills/ | Skill adoption |
| D408 | Custom skills defined | `int` | Total skill count | .claude/skills/*/ | Skill scale |
| D409 | Projects with .mcp.json | `int` | Count of .mcp.json files | File scan | MCP config adoption |
| D410 | Project customization score | `compound` | Agents + commands + skills + CLAUDE.md | Multiple | Customization depth |
| D411 | Permission rules per project | `distribution` | Count of allow/deny rules | settings.local.json | Security granularity |

---

# Category W: MCP Server Log Metrics (D412-D417)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D412 | MCP log files count | `int` | Total log files | cache logs | MCP activity |
| D413 | MCP servers used | `int` | Unique server names | cache logs | MCP diversity |
| D414 | MCP logs per day | `rate` | Log files by date | cache logs | MCP intensity |
| D415 | MCP error rate | `ratio` | Error patterns / total | cache logs | MCP reliability |
| D416 | Longest MCP session | `duration` | Max log file size | cache logs | Deep MCP usage |
| D417 | MCP server popularity | `distribution` | Logs per server | cache logs | Server preferences |

---

# Category X: Real-Time Session Metrics (D418-D423)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D418 | Live session cost | `float` | cost.total_cost_usd | statusline JSON | Current spend |
| D419 | Live lines changed | `int` | lines_added + lines_removed | statusline JSON | Current impact |
| D420 | Context overflow events | `int` | exceeds_200k_tokens occurrences | statusline JSON | Context pressure |
| D421 | Model in use | `category` | model.display_name | statusline JSON | Current model |
| D422 | Session cost velocity | `rate` | Cost / session time | statusline JSON | Spend rate |
| D423 | Lines per minute | `rate` | Lines / session time | statusline JSON | Output rate |

---

# Category Y: Cross-Source Correlation Metrics (D424-D430)

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D424 | Tip-to-feature correlation | `correlation` | Tip shown → feature used | tips + sessions | Tip effectiveness |
| D425 | Customization-to-cost | `correlation` | Cost for customized vs not | customization + cost | Customization ROI |
| D426 | Trust-to-productivity | `correlation` | Lines for trusted vs not | trust + output | Trust impact |
| D427 | MCP-to-efficiency | `correlation` | Output with MCP vs without | MCP + metrics | MCP value |
| D428 | Subscription-to-usage | `correlation` | Usage patterns by tier | subscription + usage | Tier utilization |
| D429 | Onboarding-to-retention | `correlation` | Sessions after onboarding | onboarding + sessions | Onboarding quality |
| D430 | Flag-to-behavior | `correlation` | Behavior with flags on/off | flags + sessions | Flag impact |

---

# Category Z: Behavioral Pattern Metrics (D431-D442)

## Z1. Learning & Growth

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D431 | Feature adoption velocity | `rate` | Tips discovered per week | tips over time | Learning rate |
| D432 | Customization growth | `rate` | New agents/commands per week | customization over time | Sophistication growth |
| D433 | Efficiency improvement | `trend` | lines/cost over time | Trend in productivity | Skill development |
| D434 | Error rate decline | `trend` | Error trend | errors over time | Mastery curve |

## Z2. Engagement Patterns

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D435 | Project diversity index | `ratio` | Unique projects / sessions | projects visited | Focus vs variety |
| D436 | Project loyalty | `float` | Sessions per project concentration | sessions per project | Project commitment |
| D437 | New project rate | `rate` | New projects per week | new projects over time | Exploration rate |
| D438 | Return rate | `ratio` | Returns / unique projects | return visits | Project stickiness |

## Z3. Cost Behavior

| ID | Metric | Type | Calculation | Source | Insight |
|----|--------|------|-------------|--------|---------|
| D439 | Cost consciousness | `trend` | Haiku vs Opus ratio over time | model choices | Cost awareness |
| D440 | Spending trajectory | `trend` | Cost trend | cost over time | Budget trajectory |
| D441 | Cost per feature | `distribution` | Cost by task type | cost by activity | Feature economics |
| D442 | Peak spend timing | `distribution` | When most is spent | cost by hour/day | Spend patterns |

---

# Category AA: Behavioral Psychology (D443-D447)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D443 | Hesitation Index | `ratio` | median(time_delta(AskUserQuestion→tool_result)) / question_char_count | session.jsonl | Cognitive depletion indicator |
| D444 | Blind Faith Ratio | `ratio` | (next_user_action_time - assistant_msg_end) / output_tokens for code blocks >10 lines | session.jsonl | Skim vs verify behavior |
| D445 | Decision Fatigue Slope | `trend` | P(option_0_selected) ~ session_duration regression | session.jsonl | Rising Option 0 selection |
| D446 | Frustration Typing Signature | `compound` | After tool_error: (msg_length_decrease) + (capitalization_ratio) + (punctuation_density) | session.jsonl | Session abandonment predictor |
| D447 | Panic Spiral Probability | `ratio` | count(tool_error → user_msg<10s containing "fix"/"error"/"no") / tool_errors | session.jsonl | Panic coding indicator |

---

# Category AB: Learning & Mastery (D448-D452)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D448 | Feature Stubbornness Score | `ratio` | tipsHistory[tip].count / (actual_usage_count + 1) | ~/.claude.json, session.jsonl | UX friction indicator |
| D449 | Tip Conversion Velocity | `lag` | days_between(tip_first_shown, feature_first_used) | ~/.claude.json, session.jsonl | Teachability measure |
| D450 | Native Feature Adoption Velocity | `lag` | days_between(firstSessionDate, first_advanced_feature_use) | stats-cache.json, session.jsonl | Power user differentiation |
| D451 | Command Sophistication Curve | `trend` | (Task+EnterPlanMode+Glob) / (Read+Edit+Bash) over 30-day windows | session.jsonl | Skill evolution |
| D452 | Manual Compactor Rate | `ratio` | count(compactMetadata.trigger="manual") / count(compactMetadata) | session.jsonl | Meta-cognition indicator |

---

# Category AC: Collaboration Quality (D453-D457)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D453 | Micromanagement Index | `ratio` | user_input_tokens / tool_call_count per session | session.jsonl | Trust level indicator |
| D454 | Hook Dependency Score | `ratio` | sessions_with_hookCount>0 / total_sessions | session.jsonl | Workflow maturity |
| D455 | Hook Friction Coefficient | `ratio` | count(preventedContinuation=true) / count(hookCount>0) | session.jsonl | Governance friction |
| D456 | Skepticism Loop Intensity | `sequence` | count(Edit→Bash(test/lint)→Edit same_file) | session.jsonl | Trust but verify behavior |
| D457 | Ghost Session Rate | `ratio` | sessions(duration>10min AND user_msgs=0 AND cost=0) / total_sessions | session.jsonl | Anomaly detection |

---

# Category AD: Code Quality/Architecture (D458-D462)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D458 | AI Technical Debt | `int` | count(files_only_modified_by_Edit AND never_in_history.jsonl) | session.jsonl, history.jsonl | Bus factor risk |
| D459 | Zombie Code Index | `int` | count(files_Read>3_times AND Edited=0_times) | session.jsonl | Confusing but fragile code |
| D460 | Spaghetti Coupling Factor | `float` | avg(distinct_files_modified_per_assistant_turn) | session.jsonl | Architectural coherence |
| D461 | TDD Adherence Score | `probability` | P(test_file_edited_before_impl_file) per session | session.jsonl | Test-driven development |
| D462 | Vulnerability Ignorance Window | `duration` | sessions_elapsed_while(reactVulnerabilityCache.detected=true) | ~/.claude.json, session.jsonl | Security risk |

---

# Category AE: Economic Efficiency (D463-D467)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D463 | Haiku Optimization Opportunity | `float` | sum(opus_sonnet_cost WHERE session_tools ⊆ {Read, WebSearch}) | session.jsonl | Model inefficiency |
| D464 | Context Bankruptcy Rate | `rate` | count(exceeds_200k_tokens OR large_cleared_input) / active_hours | session.jsonl, statusline | Resource management |
| D465 | Ephemeral Cache Waste | `float` | sum(cache_creation.ephemeral_5m WHERE next_msg_delay > 5min) | session.jsonl | Cache efficiency |
| D466 | Cost of Correction | `float` | sum(cost WHERE next_action = git_checkout OR revert_Edit) | session.jsonl | Undo tax |
| D467 | Project Sunk Cost | `float` | lastCost WHERE no_successful_git_commit | ~/.claude.json, session.jsonl | Spending without resolution |

---

# Category AF: Problem-Solving (D468-D471)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D468 | Rabbit Hole Depth | `sequence` | max(consecutive WebSearch→Read WITHOUT Edit/Task) | session.jsonl | Research stuck indicator |
| D469 | Plan Adherence Ratio | `ratio` | count(plan_steps_marked_[x]) / total_plan_steps per EnterPlanMode session | plans/*.md, session.jsonl | Planning effectiveness |
| D470 | YOLO Coding Rate | `ratio` | count(Write/Edit WITHOUT preceding Read of same file) / total_writes | session.jsonl | Hallucination risk |
| D471 | Echo Chamber Effect | `sequence` | count(consecutive WebSearch with Levenshtein(query_i, query_i+1) < threshold) | session.jsonl | Stuck pattern |

---

# Category AG: Meta-Cognitive (D472-D475)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D472 | Paste Dump Ratio | `ratio` | user_tokens_that_are_code / total_user_tokens | session.jsonl | Manual context management |
| D473 | Instruction Entropy | `float` | vocabulary_diversity(user_messages) | session.jsonl | Communication quality |
| D474 | Screenshot Development Rate | `sequence` | count(image/* messages → frontend_edits) | session.jsonl | Visual-driven development |
| D475 | Prompt Correction Density | `ratio` | count(user_msgs containing "no"/"stop"/"wrong") / total_user_msgs | session.jsonl | Misalignment indicator |

---

# Category AH: Network/Graph (D476-D478)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D476 | Knowledge Silo Index | `int` | count(disconnected_clusters in file_co-modification_graph) | session.jsonl | Knowledge silos |
| D477 | Agent Fan-Out Factor | `float` | avg(unique_subagents_per_parent_session) | session.jsonl | Architect vs lone wolf |
| D478 | Agent Recursion Risk | `int` | max(Task_call_nesting_depth) | session.jsonl, agent-*.jsonl | Complex autonomous reasoning |

---

# Category AI: Security/Permissions (D479-D481)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D479 | Permission Creep Rate | `rate` | d(allowedTools.length) / d(sessions) | ~/.claude.json | Progressive safety disabling |
| D480 | Click-Through Rate | `ratio` | count(permission_approval < 1s) for dangerous tools | session.jsonl | Permission fatigue |
| D481 | Shadow IT Detector | `int` | count(WebFetch to non-whitelisted domains or unusual ports) | session.jsonl | Exfiltration risk |

---

# Category AJ: Temporal Dynamics (D482-D484)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D482 | Monday Morning Cold Start | `ratio` | error_rate[first_session_of_week] / avg(error_rate[mid_week]) | stats-cache.json, session.jsonl | Context loading cost |
| D483 | Session Momentum Curve | `trend` | d(lines_generated) / d(time) over session | session.jsonl | Flow vs fatigue |
| D484 | Circadian Error Vulnerability | `correlation` | correlation(hour_24, tool_error_rate) | stats-cache.json, session.jsonl | Fatigue-driven errors |

---

# Category AK: Customization ROI (D485-D488)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D485 | Customization ROI | `ratio` | (lastLinesAdded/lastCost)[with_custom] / (lastLinesAdded/lastCost)[without] | ~/.claude.json, .claude/ | Custom agent payoff |
| D486 | Slow Machine Frustration Index | `correlation` | correlation([SLOW OPERATION] logs, user_cancel_commands) | debug/*.txt, session.jsonl | Hardware limitations |
| D487 | MCP Value-Add | `ratio` | success_rate(mcp__*) / success_rate(WebSearch+Bash) for similar queries | session.jsonl | MCP setup justification |
| D488 | Instruction Adherence Impact | `correlation` | correlation(CLAUDE.md_size, correction_loop_intensity) | CLAUDE.md, session.jsonl | Project instruction value |

---

# Category AL: Counterfactual (D489-D492)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D489 | Road Not Taken | `int` | count(plans/*.md never Read in subsequent sessions) | plans/, session.jsonl | Wasted planning |
| D490 | Ghost Tool Rate | `ratio` | count(tool_result="interrupted"/"error" AND never retried) | session.jsonl | Abandoned actions |
| D491 | Undo Reflex | `ratio` | count(Edit WHERE next_Edit_same_file restores old_string) | session.jsonl | False starts |
| D492 | Tip Ignorance Score | `int` | count(tips WHERE shown>3 AND feature_unused) | ~/.claude.json | Active ignorance |

---

# Category AM: Biological Proxies (D493-D497)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D493 | Fatigue Fingerprint | `float` | variance(response_times) within session | session.jsonl | Physical fatigue |
| D494 | Circadian Alignment Score | `ratio` | productivity(current_hour) / avg(productivity[typical_active_hours]) | stats-cache.json, session.jsonl | Optimal hours |
| D495 | Second Wind Detection | `binary` | productivity_spike > 1.5x avg AFTER gap > 30min | session.jsonl | Recovery pattern |
| D496 | Attention Span Proxy | `duration` | avg(time_before_context_switch_or_new_topic) | session.jsonl | Sustained focus |
| D497 | Typing Cadence Regularity | `float` | coefficient_of_variation(inter_message_time) | session.jsonl | Focus vs distraction |

---

# Category AN: Information Theory (D498-D502)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D498 | Prompt Compression Ratio | `ratio` | output_tokens / input_tokens per exchange | session.jsonl | Communication efficiency |
| D499 | Context Entropy | `float` | Shannon_entropy(topics_per_session) | session.jsonl | Topic diversity |
| D500 | Information Gain per Dollar | `ratio` | novel_outputs / cost | session.jsonl | Economic value |
| D501 | Redundancy Index | `int` | count(repeated_Read_same_file + repeated_similar_WebSearch) | session.jsonl | Waste detection |
| D502 | Compression Efficiency | `ratio` | useful_context_preserved / total_context_before_compact | session.jsonl | Compaction quality |

---

# Category AO: Predictive (D503-D507)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D503 | Churn Risk Score | `probability` | P(no_session_next_7d) based on (declining_frequency + rising_errors + stale_project) | session.jsonl, ~/.claude.json | Project abandonment |
| D504 | Success Predictor | `probability` | Features from first 5 min that predict git_commit in session | session.jsonl | Productive session signals |
| D505 | Blocker Detection | `compound` | count(WebSearch→WebSearch→WebSearch) + count(same_file_edited>5x) | session.jsonl | Roadblock warning |
| D506 | Scope Creep Predictor | `trend` | variance(files_touched_per_session) increasing over project lifetime | session.jsonl | Early scope creep |
| D507 | Burnout Risk Score | `compound` | (session_length_increasing) + (error_rate_increasing) + (night_work_increasing) | session.jsonl, stats-cache.json | Health warning |

---

# Category AP: Game Theory (D508-D511)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D508 | Bargaining Efficiency | `int` | iterations_to_reach_approach_agreement in EnterPlanMode | session.jsonl | Agreement speed |
| D509 | Trust Calibration Accuracy | `correlation` | correlation(user_trust_level, actual_AI_reliability) | session.jsonl | Trust appropriateness |
| D510 | Delegation Optimality | `ratio` | success_rate(delegated_tasks) vs success_rate(direct_tasks) | session.jsonl | Task assignment quality |
| D511 | Strategic Patience Score | `ratio` | count(explicit_planning_before_action) / count(immediate_action) | session.jsonl | Long-term thinking |

---

# Category AQ: Developmental Psychology (D512-D515)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D512 | Maturity Stage Classification | `category` | Feature-based classification into Novice/Intermediate/Expert | session.jsonl, ~/.claude.json | Skill tier |
| D513 | Growth Velocity | `rate` | d(sophistication_score) / d(time) | session.jsonl | Skill acquisition rate |
| D514 | Plateau Detection | `duration` | sessions_since(last_new_feature_adopted) | session.jsonl | Growth stall |
| D515 | Regression Risk | `trend` | sophisticated_feature_usage_declining over time | session.jsonl | Skill decay |

---

# Category AR: Systems Theory (D516-D519)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D516 | Feedback Loop Intensity | `ratio` | count(Edit→Error→Edit cycles) / session | session.jsonl | Correction patterns |
| D517 | Emergent Behavior Detection | `float` | distance(current_patterns, historical_patterns) | session.jsonl | Unusual patterns |
| D518 | System Stability Index | `inverse` | 1 / variance(session_characteristics) over time | session.jsonl | Predictability |
| D519 | Positive Feedback Spiral | `binary` | productivity → more_usage → more_productivity detection | session.jsonl | Virtuous cycle |

---

# Category AS: Comparative/Benchmark (D520-D524)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D520 | Efficiency Percentile | `percentile` | percentile(current_efficiency, historical_efficiency) | session.jsonl | Self-benchmark |
| D521 | Cost Percentile | `percentile` | percentile(current_cost, historical_cost) | session.jsonl | Spending benchmark |
| D522 | Optimal Session Length | `duration` | session_length WHERE efficiency is maximized | session.jsonl | Sweet spot |
| D523 | Best Practice Adherence | `ratio` | count(TDD + Planning + Testing) / possible_opportunities | session.jsonl | Engineering compliance |
| D524 | Peak Performance Baseline | `float` | 95th_percentile(productivity_score) | session.jsonl | Personal best |

---

# Category AT: Ecosystem/Meta-System (D525-D529)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D525 | Ecosystem Diversity Score | `int` | count(MCP_servers + hooks + agents + commands + skills) | All config sources | Customization breadth |
| D526 | Ecosystem Growth Rate | `rate` | d(Ecosystem_Diversity_Score) / d(time) | All config sources | Evolution speed |
| D527 | Ecosystem Health Index | `ratio` | customizations_actively_used / total_customizations | Config + session.jsonl | Maintenance health |
| D528 | Integration Depth | `int` | count(cross-tool_dependencies) | All config sources | Setup interconnection |
| D529 | Configuration Debt | `int` | count(configured_but_unused_for_30d) | All config sources | Stale configurations |

---

# Category AU: Quality Assurance (D530-D534)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D530 | Test Coverage Delta | `delta` | test_coverage_after - test_coverage_before per session | session.jsonl, git data | AI test contribution |
| D531 | Linting Score Delta | `delta` | lint_score_after - lint_score_before per session | session.jsonl, hook results | AI quality contribution |
| D532 | Type Safety Delta | `delta` | typed_lines_after - typed_lines_before per session | session.jsonl | AI type contribution |
| D533 | Documentation Delta | `delta` | doc_coverage_after - doc_coverage_before per session | session.jsonl | AI docs contribution |
| D534 | Bug Introduction Rate | `ratio` | bugs_introduced / lines_generated (inferred from quick fixes) | session.jsonl | AI defect density |

---

# Category AV: Workflow Optimization (D535-D539)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D535 | Bottleneck Detection | `category` | tool/step with highest wait_time / iteration_count | session.jsonl | Workflow slowdown |
| D536 | Parallelization Potential | `int` | count(independent_tasks_run_sequentially) | session.jsonl | Parallel opportunity |
| D537 | Automation Candidates | `int` | count(repeated_identical_sequences > 3x) | session.jsonl | Automation targets |
| D538 | Context Loading Overhead | `duration` | time(first_productive_action) - session_start | session.jsonl | Wasted context time |
| D539 | Tool Selection Optimality | `ratio` | count(tool_switched_after_failure) / count(first_tool_success) | session.jsonl | First attempt accuracy |

---

# Category AW: Communication Dynamics (D540-D542)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D540 | Clarification Burden | `ratio` | count(AskUserQuestion) / total_tool_calls | session.jsonl | Clarification frequency |
| D541 | Instruction Precision | `ratio` | successful_outcomes / total_instructions without revision | session.jsonl | First-attempt clarity |
| D542 | Conversation Convergence Rate | `inverse` | 1 / iterations_to_acceptable_output | session.jsonl | Agreement speed |

---

# Category AX: Hybrid Cross-Category (D543-D552)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D543 | Cognitive-Economic Efficiency | `compound` | (lines_generated / thinking_time) × (1 - cost_per_line) | session.jsonl | Mental effort vs output vs cost |
| D544 | Trust-Performance Calibration Gap | `delta` | abs(expected_reliability - actual_reliability) | session.jsonl | Trust mismatch |
| D545 | Learning Efficiency Ratio | `ratio` | skill_gain / (time + cost + cognitive_effort) | session.jsonl, ~/.claude.json | Skill development ROI |
| D546 | Resilience Index | `compound` | (recovery_rate × recovery_quality) / (error_frequency × error_severity) | session.jsonl | Bounce-back ability |
| D547 | Flow-Cost Tradeoff | `ratio` | flow_state_duration × productivity / cost | session.jsonl | Flow vs spending balance |
| D548 | Autonomy-Quality Ratio | `ratio` | (tasks_completed_autonomously × quality_score) / total_tasks | session.jsonl | Autonomy impact |
| D549 | Context-Efficiency Tradeoff | `ratio` | output_quality / context_tokens_used | session.jsonl | Lean context benefit |
| D550 | Velocity-Stability Score | `compound` | development_speed × (1 - regression_rate) | session.jsonl | Fast without breaking |
| D551 | Exploration-Exploitation Balance | `ratio` | time_researching / time_implementing per session | session.jsonl | Learning vs doing |
| D552 | Mastery-Complexity Alignment | `correlation` | correlation(user_skill_level, task_complexity) | session.jsonl | Task matching |

---

# Category AY: Meta-Metrics (D553-D562)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D553 | Metric Stability Index | `inverse` | 1 / variance(key_metrics) over time | session.jsonl | Pattern consistency |
| D554 | Self-Awareness Score | `correlation` | correlation(user_perceived_patterns, actual_patterns) | session.jsonl | Behavioral self-awareness |
| D555 | Prediction Accuracy | `ratio` | correct_predictions / total_predictions from early signals | session.jsonl | Signal validity |
| D556 | Dimension Coverage | `ratio` | count(active_metric_categories) / total_categories | session.jsonl | Metric breadth |
| D557 | Data Richness Score | `ratio` | count(non-null_fields) / total_possible_fields per session | session.jsonl | Data completeness |
| D558 | Metric Correlation Entropy | `float` | Shannon_entropy(correlation_matrix) | All metrics | Information independence |
| D559 | Outlier Concentration | `ratio` | count(metrics > 2σ) / total_metric_values | All metrics | Extreme value frequency |
| D560 | Metric Trend Consistency | `ratio` | count(metrics_trending_same_direction) / total_trending_metrics | All metrics | Indicator alignment |
| D561 | Signal-to-Noise Ratio | `ratio` | variance(meaningful_patterns) / variance(random_fluctuations) | session.jsonl | Signal clarity |
| D562 | Metric Actionability Score | `ratio` | count(metrics_with_clear_action) / total_metrics | All metrics | Practical utility |

---

# Category AZ: Epistemological (D563-D572)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D563 | First Principles Ratio | `ratio` | explanatory_requests / directive_requests | session.jsonl | Understanding vs doing |
| D564 | Abstraction Preference | `ratio` | abstract_queries / concrete_example_requests | session.jsonl | Learning style |
| D565 | Certainty Calibration | `correlation` | correlation(expressed_certainty, actual_correctness) | session.jsonl | Confidence accuracy |
| D566 | Knowledge Source Preference | `distribution` | Distribution of docs : examples : explanations | session.jsonl | Preferred learning mode |
| D567 | Verification Depth | `ratio` | count(secondary_verification_attempts) / count(initial_outputs) | session.jsonl | Output checking |
| D568 | Hypothesis Testing Behavior | `int` | count(test→observe→revise cycles) | session.jsonl | Scientific method |
| D569 | Mental Model Alignment | `float` | prediction_accuracy(user_about_AI_behavior) | session.jsonl | AI understanding |
| D570 | Knowledge Integration Rate | `ratio` | count(new_concepts_applied_in_context) / concepts_introduced | session.jsonl | Learning transfer |
| D571 | Uncertainty Tolerance | `ratio` | count(proceed_despite_ambiguity) / count(ambiguous_situations) | session.jsonl | Ambiguity comfort |
| D572 | Belief Update Velocity | `rate` | d(expressed_opinions_about_tool) / d(evidence_encountered) | session.jsonl | Belief change speed |

---

# Category BA: Narrative/Story (D573-D582)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D573 | Session Arc Coherence | `float` | topic_continuity_score throughout session | session.jsonl | Clear through-line |
| D574 | Plot Twist Detection | `int` | count(major_direction_changes_mid_session) | session.jsonl | Unexpected pivots |
| D575 | Climax Identification | `timestamp` | timestamp(peak_effort_or_complexity_point) | session.jsonl | Session peak |
| D576 | Resolution Completeness | `inverse` | count(open_threads_at_end) / count(threads_started) | session.jsonl | Thread resolution |
| D577 | Character Development Score | `delta` | skill_level_end - skill_level_start per session | session.jsonl | Per-session growth |
| D578 | Conflict Intensity | `float` | max(error_rate × correction_density) per session | session.jsonl | Most challenging moment |
| D579 | Pacing Consistency | `float` | variance(activity_intensity) throughout session | session.jsonl | Even vs dramatic pace |
| D580 | Theme Coherence | `float` | semantic_similarity(start_topic, end_topic) | session.jsonl | Topic consistency |
| D581 | Subplot Detection | `int` | count(parallel_threads_active) per session | session.jsonl | Multiple concerns |
| D582 | Denouement Quality | `ratio` | productivity(last_15min) / avg(productivity) | session.jsonl | Ending quality |

---

# Category BB: Phenomenological (D583-D592)

| ID | Metric | Type | Calculation | Sources | Insight |
|----|--------|------|-------------|---------|---------|
| D583 | Flow State Probability | `probability` | P(flow) from (low_errors AND consistent_pace AND low_interruptions) | session.jsonl | Flow likelihood |
| D584 | Frustration Accumulation | `float` | integral(frustration_signals) over session | session.jsonl | Total frustration |
| D585 | Satisfaction Proxy | `ratio` | (completed_tasks × quality) / (effort + errors) | session.jsonl | Inferred satisfaction |
| D586 | Engagement Intensity | `compound` | (activity_rate × session_duration) / context_switches | session.jsonl | Deep vs distracted |
| D587 | Curiosity Index | `ratio` | count(exploratory_queries + voluntary_learning) / total_queries | session.jsonl | Intrinsic motivation |
| D588 | Boredom Detection | `compound` | (repetitive_patterns + declining_complexity + increasing_breaks) | session.jsonl | Disengagement signs |
| D589 | Accomplishment Markers | `int` | count(task_completions + positive_language + session_closures) | session.jsonl | Achievement signals |
| D590 | Overwhelm Indicators | `compound` | (context_overflow + error_clustering + retreat_to_simpler_tasks) | session.jsonl | Cognitive overload |
| D591 | Intrinsic Motivation Score | `ratio` | voluntary_exploration / required_work | session.jsonl | Self-directed work |
| D592 | Presence Quality | `inverse` | 1 / (avg_response_time × distraction_frequency) | session.jsonl | User presence |

---

# Summary

## Metric Counts by Category

| Category | Range | Count | Focus Area |
|----------|-------|-------|------------|
| A | D001-D028 | 28 | Time & Activity |
| B | D029-D048 | 20 | Tool Usage |
| C | D049-D073 | 25 | File Operations |
| D | D074-D109 | 36 | Model & Tokens |
| E | D110-D136 | 27 | Conversation |
| F | D137-D142 | 6 | Thinking & Complexity |
| G | D143-D158 | 16 | Task Management |
| H | D159-D172 | 14 | Agent & Delegation |
| I | D173-D188 | 16 | Project Activity |
| J | D189-D203 | 15 | Error & Recovery |
| K | D204-D228 | 25 | Code Generation |
| L | D229-D238 | 10 | Web Research |
| M | D239-D252 | 14 | Hooks & Customization |
| N | D253-D259 | 7 | User Interaction |
| O | D260-D300 | 41 | Advanced Derived |
| P | D301-D343 | 43 | Global State & Project |
| Q | D344-D348 | 5 | Startup & Usage |
| R | D349-D357 | 9 | Feature Discovery |
| S | D358-D362 | 5 | Feature Flags |
| T | D363-D395 | 33 | Per-Project Analytics |
| U | D396-D399 | 4 | Subscription |
| V | D400-D411 | 12 | Project Customization |
| W | D412-D417 | 6 | MCP Server Logs |
| X | D418-D423 | 6 | Real-Time Session |
| Y | D424-D430 | 7 | Cross-Source Correlation |
| Z | D431-D442 | 12 | Behavioral Patterns |
| AA | D443-D447 | 5 | Behavioral Psychology |
| AB | D448-D452 | 5 | Learning & Mastery |
| AC | D453-D457 | 5 | Collaboration Quality |
| AD | D458-D462 | 5 | Code Quality/Architecture |
| AE | D463-D467 | 5 | Economic Efficiency |
| AF | D468-D471 | 4 | Problem-Solving |
| AG | D472-D475 | 4 | Meta-Cognitive |
| AH | D476-D478 | 3 | Network/Graph |
| AI | D479-D481 | 3 | Security/Permissions |
| AJ | D482-D484 | 3 | Temporal Dynamics |
| AK | D485-D488 | 4 | Customization ROI |
| AL | D489-D492 | 4 | Counterfactual |
| AM | D493-D497 | 5 | Biological Proxies |
| AN | D498-D502 | 5 | Information Theory |
| AO | D503-D507 | 5 | Predictive |
| AP | D508-D511 | 4 | Game Theory |
| AQ | D512-D515 | 4 | Developmental Psychology |
| AR | D516-D519 | 4 | Systems Theory |
| AS | D520-D524 | 5 | Comparative/Benchmark |
| AT | D525-D529 | 5 | Ecosystem/Meta-System |
| AU | D530-D534 | 5 | Quality Assurance |
| AV | D535-D539 | 5 | Workflow Optimization |
| AW | D540-D542 | 3 | Communication Dynamics |
| AX | D543-D552 | 10 | Hybrid Cross-Category |
| AY | D553-D562 | 10 | Meta-Metrics |
| AZ | D563-D572 | 10 | Epistemological |
| BA | D573-D582 | 10 | Narrative/Story |
| BB | D583-D592 | 10 | Phenomenological |
| **TOTAL** | | **592** | |

## Type Distribution

| Type | Count | Description |
|------|-------|-------------|
| `ratio` | ~180 | Proportions and normalized values |
| `int` | ~120 | Integer counts |
| `float` | ~80 | Decimal measurements |
| `distribution` | ~50 | Breakdowns and histograms |
| `duration` | ~40 | Time measurements |
| `rate` | ~30 | Per-time values |
| `trend` | ~25 | Directional changes |
| `compound` | ~25 | Multi-factor scores |
| `correlation` | ~15 | Statistical relationships |
| `category` | ~15 | Classification labels |
| `probability` | ~10 | Likelihood values |
| `other` | ~22 | Various specialized types |

---

## Related Documentation

- **[CLAUDE_CODE_DATA_SOURCES.md](CLAUDE_CODE_DATA_SOURCES.md)** - Raw data locations and formats
- **[CLAUDE_CODE_METRICS_CATALOG.md](CLAUDE_CODE_METRICS_CATALOG.md)** - Raw data schemas and field definitions
- **[IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md)** - Project implementation roadmap

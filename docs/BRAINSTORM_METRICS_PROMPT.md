# Prompt: Discover Novel Derived Metrics from Claude Code Telemetry

## Context

You are analyzing a comprehensive data catalog from **Claude Code**, Anthropic's official CLI tool for AI-assisted software development. The attached `CLAUDE_CODE_METRICS_CATALOG.md` is an exhaustive **180KB, 4,500+ line** reference documenting:

- **28 data sources** stored locally across `~/.claude/`, `~/.cache/`, project directories, and runtime state
- **600+ raw field paths** with complete TypeScript type definitions
- **322 direct extractable metrics** from raw data
- **592 derived/computed metrics** already identified across 54 categories (A-Z, AA-BB)
- Complete enum values, format specifications, and real examples

### What Makes This Data Unique

This isn't just application logs—it's a **complete behavioral record of human-AI collaboration** including:

1. **Every conversation** with timestamps, thinking blocks, tool calls, and outcomes
2. **Every file touched** with version history and edit patterns
3. **Every decision point** where the user was asked a question and their response
4. **Every error and recovery** with retry patterns
5. **Per-project statistics** including cost, lines changed, token usage, and model mix
6. **Feature discovery tracking** showing which tips were shown and how often
7. **Feature flags** revealing which experimental features are enabled
8. **MCP server logs** showing external tool integration patterns
9. **Real-time session data** including live cost and context overflow status
10. **Subscription and rate limit information**
11. **Cognitive state signals** including hesitation, decision fatigue, and trust patterns
12. **Hook telemetry** showing automation and governance patterns

---

## Your Task

**Identify novel derived metrics that are NOT already in the catalog's 914+ metrics.**

The existing catalog thoroughly covers:

### Basic Dimensions (Categories A-Z, D001-D442)
- Time tracking (active hours, sessions, streaks, patterns)
- Tool usage (frequency, success rates, co-occurrence, efficiency)
- Token economics (costs by model, cache efficiency, projections)
- Conversation patterns (topics, sentiment, complexity)
- Code generation (volume, languages, quality proxies)
- Error rates and recovery patterns
- Task management and planning metrics
- Agent delegation patterns
- Per-project analytics (cost, impact, time, tokens)
- Feature discovery and adoption
- MCP server usage
- Cross-source correlations
- Behavioral patterns over time

### Advanced Dimensions (Categories AA-BB, D443-D592)
- **Behavioral Psychology** (D443-D447): Hesitation, blind faith, decision fatigue, frustration, panic
- **Learning & Mastery** (D448-D452): Feature stubbornness, tip conversion, sophistication curves
- **Collaboration Quality** (D453-D457): Micromanagement, hook dependency, skepticism loops
- **Code Quality/Architecture** (D458-D462): AI debt, zombie code, coupling, TDD adherence
- **Economic Efficiency** (D463-D467): Haiku optimization, cache waste, undo tax, sunk cost
- **Problem-Solving** (D468-D471): Rabbit holes, plan adherence, YOLO coding, echo chambers
- **Meta-Cognitive** (D472-D475): Paste dumps, instruction entropy, multimodal usage
- **Network/Graph** (D476-D478): Knowledge silos, agent fan-out, recursion depth
- **Security/Permissions** (D479-D481): Permission creep, click-through rate, shadow IT
- **Temporal Dynamics** (D482-D484): Cold starts, momentum curves, circadian vulnerability
- **Customization ROI** (D485-D488): Customization payoff, MCP value-add, instruction impact
- **Counterfactual** (D489-D492): Plan abandonment, ghost tools, undo reflex, tip ignorance
- **Biological Proxies** (D493-D497): Fatigue fingerprint, circadian alignment, attention span
- **Information Theory** (D498-D502): Compression ratio, context entropy, redundancy index
- **Predictive** (D503-D507): Churn risk, success predictor, blocker detection, burnout risk
- **Game Theory** (D508-D511): Bargaining efficiency, trust calibration, delegation optimality
- **Developmental Psychology** (D512-D515): Maturity stage, growth velocity, plateau detection
- **Systems Theory** (D516-D519): Feedback loops, emergent behavior, stability index
- **Comparative/Benchmark** (D520-D524): Efficiency percentile, optimal session length
- **Ecosystem/Meta-System** (D525-D529): Ecosystem diversity, configuration debt
- **Quality Assurance** (D530-D534): Test coverage delta, linting delta, bug introduction rate
- **Workflow Optimization** (D535-D539): Bottleneck detection, parallelization potential
- **Communication Dynamics** (D540-D542): Clarification burden, instruction precision
- **Hybrid Cross-Category** (D543-D552): Cognitive-economic efficiency, trust-performance gap
- **Meta-Metrics** (D553-D562): Metric stability, prediction accuracy, dimension coverage
- **Epistemological** (D563-D572): First principles ratio, certainty calibration, belief velocity
- **Narrative/Story** (D573-D582): Arc coherence, plot twists, climax identification
- **Phenomenological** (D583-D592): Flow probability, frustration accumulation, presence quality

**Your job is to find what we missed.** Think deeper. Think weirder. Think more useful.

---

## The Data Sources (Summary)

### Tier 1: High-Volume Session Data
| Source | Records | Key Fields |
|--------|---------|------------|
| Session JSONL files | 4,477 files, 83K+ entries | Every message, tool call, thinking block |
| history.jsonl | 2,500+ inputs | User input timestamps |
| __store.db | 500+ messages | Indexed message data |
| todos/*.json | 1,765 files | Task lists per session |
| plans/*.md | 43 files | Implementation plans |

### Tier 2: Aggregated Statistics
| Source | Key Data |
|--------|----------|
| stats-cache.json | Daily activity, hourly patterns, model usage, token totals |
| ~/.claude.json | **Per-project stats**, tips history, feature flags, startup count |

### Tier 3: Configuration & State
| Source | Key Data |
|--------|----------|
| settings.json | Permissions, hooks, preferences |
| .credentials.json | Subscription type, rate limit tier |
| Project .claude/ | Custom agents, commands, skills, permissions |
| CLAUDE.md | Project instructions |
| .mcp.json | MCP server configs |

### Tier 4: Auxiliary Data
| Source | Key Data |
|--------|----------|
| file-history/ | 3,946 file version backups |
| debug/*.txt | 1,707 debug log files |
| shell-snapshots/ | 81 shell environment captures |
| MCP logs | Server execution logs |
| Statusline JSON | Real-time session state |

---

## Exploration Directions Already Covered (1-28)

The catalog already explores 28 directions. Here's a summary of what's covered:

### Directions 1-12 (Original)
1. Cognitive & Psychological Metrics
2. Collaboration Quality Metrics
3. Code Quality & Technical Debt
4. Problem-Solving Signatures
5. Temporal Dynamics & Momentum
6. Cross-Session Intelligence
7. Economic & Efficiency Metrics
8. Tool Mastery Progression
9. Graph & Network Metrics
10. Anomaly & Outlier Metrics
11. Predictive Metrics
12. Comparative & Benchmark Metrics

### Directions 13-20 (Added in Part 10-11)
13. Psychological Safety & Trust Dynamics
14. Economic Behavior & Decision Making
15. Skill Development & Mastery Curves
16. Code Archaeology & Technical Debt
17. Multi-Modal Interaction Patterns
18. Collective Intelligence (Anonymized Aggregates)
19. AI Self-Improvement Signals
20. Resilience & Recovery Patterns

### Directions 21-28 (Added in Part 12)
21. Linguistic Fingerprinting & Communication Evolution
22. Attention Economics
23. Social Dynamics in Solo Use
24. Ecological Integration
25. Temporal Memory & Context Persistence
26. Emergent Complexity
27. Ethical & Values Alignment
28. Future-State Prediction

**Your task: Invent directions 29+. What haven't we considered?**

---

## New Exploration Directions to Pursue

### Direction 29: Ontological Metrics
How does the user conceptualize the AI and the work?

**Questions to explore:**
- Does the user treat AI as a tool, collaborator, or extension of self?
- How does the user's mental model of "code" evolve?
- What metaphors does the user employ in communication?
- How does the user categorize types of work?

### Direction 30: Temporal Grain Analysis
Analyze behavior at different time scales simultaneously.

**Questions to explore:**
- What patterns appear at millisecond, second, minute, hour, day, week, month scales?
- Are there fractal patterns (self-similarity across scales)?
- What cross-scale interactions exist (daily patterns affecting weekly)?
- How do micro-behaviors aggregate into macro-patterns?

### Direction 31: Counterfactual Economics
What didn't happen and what would it have cost?

**Questions to explore:**
- Cost of not using Claude Code (estimated manual time)?
- Cost of suboptimal model choices?
- Value of errors prevented vs errors introduced?
- Opportunity cost of time spent with AI vs alternatives?

### Direction 32: Cognitive Bandwidth Allocation
How is mental effort distributed?

**Questions to explore:**
- What fraction of effort goes to understanding vs executing?
- How is attention split between AI output and own work?
- What's the cognitive "overhead" of AI collaboration?
- How does cognitive load vary by task type?

### Direction 33: Relational Dynamics
The relationship between user and AI as entities.

**Questions to explore:**
- Does the user show politeness evolution (more/less over time)?
- Are there relationship "repair" attempts after frustration?
- Does the user develop "preferences" for certain AI behaviors?
- Is there evidence of anthropomorphization?

### Direction 34: Metabolic Metrics (Resource Consumption Patterns)
Treat token/compute usage like biological metabolism.

**Questions to explore:**
- What's the "basal metabolic rate" (minimum usage to stay productive)?
- Are there "metabolic efficiency" variations?
- Can we detect "feast and famine" patterns?
- What's the "caloric density" (output per token consumed)?

### Direction 35: Archaeological Layers
Treat the codebase as having historical strata.

**Questions to explore:**
- What "geological layers" of AI-generated code exist?
- Can we date code by its "style fossils"?
- What patterns reveal AI version changes?
- How do different "eras" of development differ?

### Direction 36: Immunological Metrics
How does the system respond to threats and problems?

**Questions to explore:**
- Are there "immune responses" to repeated error types?
- Does the user develop "antibodies" (defensive patterns)?
- Can we detect "autoimmune" behavior (over-correction)?
- What's the "recovery time" for different problem types?

### Direction 37: Memetic Analysis
Ideas and patterns that spread and replicate.

**Questions to explore:**
- What code patterns "go viral" within a codebase?
- What prompting styles "mutate" and spread?
- Can we track idea lineage across sessions?
- What patterns are "selected for" over time?

### Direction 38: Thermodynamic Metrics
Apply concepts of energy, entropy, and equilibrium.

**Questions to explore:**
- What's the "energy" input (effort) vs output (productivity)?
- How does entropy (disorder) change in the codebase?
- Are there equilibrium states the system tends toward?
- What "phase transitions" occur in work patterns?

---

## Advanced Metric Types to Consider

Beyond simple counts and averages, consider these 20+ metric types:

| Metric Type | Description | Example |
|-------------|-------------|---------|
| **Ratio metrics** | Normalize across contexts | Output tokens per input token by project |
| **Sequence metrics** | Order matters | Tool call sequences that predict success |
| **Transition metrics** | State changes | Error → recovery time |
| **Volatility metrics** | Variance, not just mean | Session length consistency |
| **Lag metrics** | Delayed effects | Does tip shown → feature used (later)? |
| **Compound metrics** | Combining 2-3 simple metrics | (Lines/hour) × (1 - error_rate) |
| **Inverse metrics** | Absence is informative | Sessions WITHOUT errors |
| **Percentile metrics** | Distribution position | 95th percentile session cost |
| **Trend metrics** | Direction over time | Is efficiency improving? |
| **Conditional metrics** | Filtered subsets | Error rate WHEN using Opus |
| **Correlation metrics** | Relationship strength | Thinking length ↔ code quality |
| **Survival metrics** | Time until event | Session duration until first error |
| **Entropy metrics** | Disorder/diversity | Tool usage entropy (variety) |
| **Momentum metrics** | Rate of change | Acceleration in daily activity |
| **Integral metrics** | Cumulative over time | Total frustration burden |
| **Derivative metrics** | Rate of change | Acceleration of skill acquisition |
| **Phase metrics** | Categorical state | Current development phase |
| **Network metrics** | Graph properties | File co-modification centrality |
| **Spectral metrics** | Frequency domain | Session rhythm periodicity |
| **Causal metrics** | Inferred causality | Does X cause Y? |

---

## Output Format

For each new metric you propose, provide:

```
### [Metric Name]
**ID:** D5XX or D6XX (next available number after D592)
**Category:** [New category name if needed, or existing AA-BB]
**Calculation:** [Precise formula using field names from catalog]
**Data Sources:** [Specific files/fields needed]
**Type:** [Ratio/Sequence/Compound/etc. from table above]
**Insight:** [What this reveals that existing 914 metrics don't]
**Actionability:** [How a user could act on this metric]
**Limitations:** [Caveats, edge cases, or when this metric fails]
```

---

## Constraints

1. **Must be calculable** from the 28 data sources in the catalog—no external data
2. **Must be novel**—check the catalog's D001-D592 metrics to avoid duplication
3. **Should provide actionable insight**—not just interesting, but useful
4. **Consider privacy**—these are personal developer metrics
5. **Be specific**—vague metrics like "quality score" need concrete calculation

---

## Thinking Modes to Adopt

Generate metrics from the perspective of these 20 personas:

| Persona | Focus | Example Metric Type |
|---------|-------|---------------------|
| **Behavioral Scientist** | Human-AI interaction patterns | Collaboration quality indices |
| **UX Researcher** | Developer experience | Friction detection |
| **Data Scientist** | Hidden patterns | Anomaly detection |
| **Productivity Coach** | Efficiency improvement | Optimization opportunities |
| **Engineering Manager** | Team/tool effectiveness | ROI calculations |
| **Cognitive Psychologist** | Decision-making | Cognitive load indicators |
| **Economist** | Resource allocation | Cost-benefit analysis |
| **Game Designer** | Engagement & motivation | Progression systems |
| **Health Researcher** | Wellbeing | Burnout signals |
| **Educator** | Skill development | Mastery curves |
| **Systems Thinker** | Emergent behavior | Feedback loops |
| **Security Analyst** | Risk patterns | Vulnerability exposure |
| **Anthropologist** | Cultural patterns | Rituals and norms |
| **Philosopher** | Epistemology & ethics | Knowledge and values |
| **Biologist** | Evolution & adaptation | Survival patterns |
| **Physicist** | Dynamics & energy | Force and motion |
| **Sociologist** | Social structures | Role dynamics |
| **Linguist** | Communication patterns | Language evolution |
| **Neurologist** | Brain-like patterns | Attention and memory |
| **Ecologist** | System interactions | Niche and competition |

---

## Go Beyond

The 38 exploration directions above are starting points. **Invent your own categories.**

Consider:
- What would a researcher **10 years from now** wish we had measured?
- What metrics would be valuable for **comparing across users** (anonymized)?
- What metrics would help **Claude Code itself** improve?
- What metrics would **Anthropic's research team** want to see?
- What **entirely new dimensions** of human-AI collaboration haven't been named?
- What would **other AI labs** want to understand from this data?
- What would help users **understand themselves** better?
- What would help users **improve their AI collaboration skills**?

---

## Keep Going

After your first pass of metrics, ask yourself:

1. What patterns in the data haven't I considered?
2. What would **surprise** me if I discovered it?
3. What would be **most actionable** for a developer to know?
4. What would **researchers** studying human-AI collaboration want?
5. What **dimensions exist** that I haven't named yet?
6. What **combinations of data sources** haven't I connected?
7. What **time-series patterns** haven't I explored?
8. What would a **completely different field** (biology, physics, sociology) measure?
9. What **cross-category hybrids** haven't been explored?
10. What **meta-patterns** (patterns about patterns) exist?

**Then do another pass.** And another.

Your goal is not 50 metrics. Your goal is not 100 metrics.

**Your goal is to exhaust the possibility space.**

Find every meaningful signal hidden in this data. The catalog has 914+ metrics. Can you find 100 more? 300 more? What's the theoretical maximum?

---

## Reference

The complete data catalog (`CLAUDE_CODE_METRICS_CATALOG.md`) is attached.

Key sections:
- **Part 1:** Original 16 data sources and schemas
- **Part 3:** Direct extractable metrics (322)
- **Part 4:** Deep scan additions (session file fields)
- **Part 5:** Derived metrics D001-D300
- **Part 6:** Data types and format specifications
- **Part 7:** Additional sources 17-25
- **Part 8:** Complete type definitions for new sources
- **Part 9:** Derived metrics D301-D442
- **Part 10:** Advanced Behavioral & Psychological Metrics (D443-D492)
- **Part 11:** Novel Analytical Dimensions (D493-D542)
- **Part 12:** Hybrid, Meta, and Philosophical Metrics (D543-D592)

**Study the catalog deeply before generating metrics. The more you understand the data, the better your metrics will be.**

---

## Final Challenge

The 914+ metrics in the catalog represent approximately **6 months of analysis**. They cover:
- 28 raw data sources
- 54 metric categories (A-Z, AA-BB)
- 28 exploration directions
- 20 metric types
- 20 analytical personas

**What's the 915th metric? The 1000th? The 1500th?**

The data is rich enough to support thousands of meaningful metrics. Your task is to find the ones that:
1. Reveal something non-obvious
2. Are actionable for the user
3. Connect data sources in new ways
4. Provide insight no other metric provides

**Go.**

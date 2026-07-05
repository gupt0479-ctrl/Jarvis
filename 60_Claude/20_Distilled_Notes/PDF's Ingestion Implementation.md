---
type: evergreen
status: sprout
created: 2026-07-05
tags:
  - implementation
  - ingestion
  - mcp
  - claude-code
notes:
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/5 Best Claude Code MCPs (PDF)]]"
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/Claude Code Free with Ollama (PDF)]]"
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/Claude Code Status Bar (PDF)]]"
  - "[[60_Claude/10_Source_Summaries/PDF Ingestion/Obsidian + Claude Code Codebook — 12 Commands (PDF)]]"
  - "[[Web Ingestion Implementation]]"
  - "[[GitHub Ingestion Implementation]]"
---

# PDF Ingestion Implementation

Extract actionable requirements from PDF source summaries to guide Claude Code MCP setup, tool configuration, and vault integration.

---

## MCP Setup & Installation

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/5 Best Claude Code MCPs (PDF)]]

### Installed & Verified
- **Context7** — Already in deferred tools. Pulls live, version-specific docs to prevent API hallucination.
- **Firecrawl** — Already integrated via MCP server. Replaces Playwright for web scraping.

### To Install (Priority)
- **Sequential Thinking** — Install now. Provides step-by-step planning with branching/revision; aligns with [[Jarvis OS — North Star]] "plan before build" discipline.
  - Command: `claude mcp add sequential-thinking -- npx -y @modelcontextprotocol/server-sequential-thinking`

### To Evaluate (Decision Gate)
- **Knowledge Graph Memory** — Determine if redundant with jarvis-memory before adopting.
  - Does it improve Claude session visualization better than jarvis-memory?
  - Would it integrate with Obsidian graph or benefit graphify?
  - Likely: jarvis-memory's cross-vault scope supersedes project-scoped memory MCP.

- **Codex Plugin** (OpenAI) — Explore as adversarial second-opinion loop (reinforces existing Codex pattern in [[10_Areas/AI/Codex|Codex]]).
  - Commands: `/codex:review`, `/codex:adversarial-review`, `/codex:rescue`

### Not Adopting
- **Playwright** — Firecrawl handles this use case.

---

## Claude Code Configuration

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/Claude Code Status Bar (PDF)]]

- **Status bar** — Run `/statusline show folder, git branch, model name, and context percentage with a progress bar`. Sets context-fill awareness cue for token-economy discipline.
  - Set color warning at 70%+ to trigger preemptive `/compact`.

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/Claude Code Free with Ollama (PDF)]]

- **Local fallback** — Decide: is Ollama (GLM 4.7 Flash) worth setting up for low-stakes bulk coding when Claude quota exhausted?
  - Tradeoff: Free with no limits, but weaker model — unsuitable for planning or quality writing.
  - Implementation: Set `ANTHROPIC_BASE_URL=http://localhost:11434` only when needed, not globally.

---

## Vault Integration & Skills

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/Obsidian + Claude Code Codebook — 12 Commands (PDF)]]

### Principle
Context quality caps agent usefulness. Jarvis context-pack discipline is validated by independent sources (Vin's codebook, claudekit).

### Confirmed Gaps (Missing Skills)
Vin's 12-command set converges on Jarvis's skill roster and confirms these gaps:
- **/challenge** — Pressure-test beliefs; surface contradictions and weak assumptions.
- **/ideas** — Generate grounded idea report (tools to build, people to meet, topics to investigate).
- **/drift** — Surface loosely-connected recurring themes without clear thread (requires semantic search via jarvis-memory).
- **/emerge** — Identify clusters coalescing into projects/products (requires semantic search via jarvis-memory).

### Existing Equivalents (Validated)
- /context, /today (→ /startday), /closeday, /trace (→ /trace-topic), /connect (→ /connect-notes), /graduate (→ /distill-note) already implemented in Jarvis.

### Build Priority
1. **/challenge** and **/ideas** — buildable now without semantic search.
2. **/drift** and **/emerge** — dependent on jarvis-memory semantic-search completion (North Star 5.4).

---

## Certifications Strategy (Career Signal + ATS Insurance)

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/20 Free AI Certifications (PDF)]]

### Core Principle
Certifications are **concrete, verifiable ATS-filter insurance** — not a substitute for deployed projects. Use them strategically: 5-6 recognized certs stacked across vendors + 3 deployed projects = differentiated resume signal. Secondary to project work (only 6% of AI/ML postings explicitly require certs per [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]]), but cheap resume leverage for screening automation.

### Tier 1: Doing Now (5-6 Certifications)

**High-Signal Tier (recognized by recruiters):**
1. **GitHub Foundations Certificate** — Verifiable GitHub credential; shows on profile.
2. **LinkedIn Learning: Anthropic Claude Certified Architect Foundations (CCA-F) Cert Prep** — Direct Claude/LLM focus (rare on resumes); requires LinkedIn Premium (~3 months to complete multiple courses).
3. **Microsoft AI Fundamentals (AI-900)** — High-recruiter recognition (~10-15h); free virtual training days include exam voucher.
   - **Decision:** Find better Azure course (current curriculum too generic; need Anthropic-Claude or hands-on focus).
4. **Google AI Essentials** — Gold-standard AI fundamentals starter (~5h, free); high recognition.
   - **Decision:** Find better Google course (current too basic; want ML/RAG depth or specific vertical like LLMs).
5. **AWS Cloud Practitioner Essentials** — Currently doing.
6. **AWS AI & ML Scholars Program** — Mentorship + structured prep for AWS Certified AI Practitioner; higher substance than badge-only certs.
   - **Decision:** Clarify: is this done *alongside* Cloud Practitioner or as a prerequisite?

**Domain-Specific Add-On (if determined high-value):**
- **NVIDIA AI Certification** — GPU/CUDA focus (good for BOOM observability); need to identify better course than generic options.

### Tier 2: Future Certifications (Dependent on Tier 1 Completion)

After completing the 5-6 above, pursue these in priority order:

1. **AWS Certified AI Practitioner** — Natural progression after AWS AI & ML Scholars Program; validates applied AI skills.
2. **IBM AI Fundamentals** (IBM SkillsBuild) — Official Credly badge; vendor diversity; ~10h investment.
3. **Google Cloud Professional Data Engineer** — BigQuery + ML; pairs with Google AI Essentials; deeper than basics.
4. **Anthropic Certified AI Engineer** (if released) — Follows CCA-F; deep Claude-specific patterns and best practices.
5. **DeepLearning.AI Specialization** (TensorFlow, LLM, or RAG-specific) — Project-backed, more substantial than one-off certs; depends on portfolio direction (trading vs. BOOM vs. Jarvis).

### Decision Gate: Full Vault Certification Review

**Action:** Before finalizing 5-6, review **all certification resources scattered across the vault** (not just this one PDF):
- Check `10_Areas/Career/` for internship cert tracking.
- Check `60_Claude/05_Clippings/` for other ingested cert resources.
- Check `20_Progress/` for any half-started cert work.
- Reconcile with [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] (project-first data).

**Scope clarification needed:**
- How many hours/week available for cert work vs. project work (BOOM, portfolio, Jarvis)?
- Are these 5-6 certs *in parallel* or *sequential*?
- LinkedIn Premium cost/timing: when to enable for CCA-F prep?

### Anti-Output-Illusion Guardrail

Per [[The Output Audit (web)]], cert-stacking can become busywork. The rule: **2 recognized certs (Google + Microsoft AI-900) are ATS insurance; anything beyond that serves the portfolio project directly** (e.g., AWS certs for trading infrastructure, Anthropic CCA-F for Jarvis agent work). If a cert doesn't feed into active shipped work, skip it.

---

## Portfolio Projects: Pick 1-2, Build Deep

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/BASWE 15 AI Engineering Projects That Land Jobs (PDF)]]

### Core Principle
Build 2–3 exceptionally well, not all 15. Ship to "deployed + evaluated + tested + Loom video + case-study-with-a-number" standard. The recurring winning pattern across all projects: **hand-built golden dataset → multi-dimensional scoring → regression diff → feedback loop that grows dataset from failures** (because eval quality is bounded by data quality).

### Priority: Leverage Existing Vault Work

**Option A: Project 6 (RAG + Hybrid Search)**
- **Why:** Feeds directly into [[Jarvis OS — North Star]] jarvis-memory semantic-search roadmap.
- **Scope:** Production RAG with dense + sparse (BM25) hybrid retrieval, reranker, grounded generation with citations.
- **Differentiator:** Citation verification + chunking-strategy A/B testing (fixed+overlap vs. header-recursive vs. semantic).
- **Stack:** Python, text-embedding-3-small, ChromaDB/Qdrant, rank_bm25, Claude/GPT-4o, FastAPI, Docker.
- **Deliverable:** API + dashboard showing hybrid-vs-dense toggle; eval framework (50+ golden Q&A with faithfulness/accuracy metrics).
- **Timeline:** 12–14 days at 2–3 h/day.

**Option B: Project 15 (Agent Orchestration + MCP)**
- **Why:** Aligns with [[Claude OS]] CausalOps and Jarvis agent layer; demonstrates multi-agent + MCP + tool use + memory.
- **Scope:** Supervisor agent decomposes tasks, delegates to specialized agents, maintains persistent memory, escalates with low confidence.
- **Differentiator:** Full decision observability; human-in-the-loop for edge cases; MCP integration (real tools, not toy).
- **Stack:** Python, LangGraph, Claude/Anthropic, MCP tools, PostgreSQL + ChromaDB (short/long-term memory), Redis, React/Streamlit, Docker.
- **Deliverable:** Autonomous system with fallback to human; decision explorer UI; metrics on task success + human escalation rate.
- **Timeline:** 12–14 days at 2–3 h/day.

### Portfolio Proof Requirements
Every project needs:
1. **Loom walkthrough** (3 min max): show problem → solution → live demo → metrics.
2. **Case study with a number:** lead with impact ("reduced cost by X%", "Y% accuracy uplift", "Z% safety: 100% blocked dangerous queries").
3. **Eval dataset:** hand-built, at least 50 test cases including edge cases.
4. **Reproducible pipeline:** Docker-compose or clear setup; results deterministic.

### Anti-Advice
- **Not:** "I called an LLM API and built a chatbot."
- **Not:** Sampling 5 projects shallowly.
- **Not:** Eval-less demos (Project 1 on regression detection can be adapted as your own skills' missing eval layer).

---

## Knowledge Gathering & Intelligence Automation System (10% of Work Needed)

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/Find Startup Ideas with Reddit & AI (PDF)]]

**Status:** FRAMEWORK DEFINED — This is the Reddit pattern expanded into multi-platform knowledge aggregation. **Not a content-generation tool; not a posting tool. This is research + reporting automation.**

### Concept: "Search Like a Superior Human"

Automated research agent that monitors multiple platforms for:
- What people actually want (pain points, requests, solutions)
- What's emerging (trending topics, early signals)
- What's happening now (breaking news, market moves, job demand)
- What people are building (GitHub trends, engineering patterns)

Then: **aggregate, synthesize, report.**

### Six Automation Channels (MVP)

| Channel | Source | What to Extract | Platform Tools |
|---------|--------|-----------------|-----------------|
| **Reddit** | Trending communities (10k–100k, growing) | Pain points, advice requests, solution requests, recurring problems | Gummy Search or native Reddit API |
| **LinkedIn** | Job postings, industry discussions | Job requirements, skills demand, emerging roles, industry sentiment | LinkedIn API or Firecrawl |
| **GitHub** | Trending repos, releases, stars | Emerging libraries, engineering patterns, tech adoption | GitHub API or Firecrawl |
| **Job Postings** | AngelList, LinkedIn Jobs, Wellfound | Skill gaps, market signals, hiring demand | Job API aggregators (RapidAPI) |
| **Trading News** | Financial RSS (Reuters, Bloomberg, CNBC) | Market sentiment, price drivers, opportunity signals | RSS aggregators + Firecrawl |
| **Email Newsletters** | gupta.21.anant@gmail.com (AI-curated inbox) | AI research updates, trend summaries, expert signals | Gmail API + Claude analysis |

### Automation Pattern (Reddit Model → Scaled)

**Step 1: Ingest** (automated, daily/weekly)
- Scrape Reddit subreddits (10k–100k, fast-growing)
- Scrape LinkedIn jobs (filter by role/location)
- Pull GitHub trending (languages/tags of interest)
- Parse job postings (extract requirements, compensation)
- Fetch trading news RSS (filter by keywords)
- Read email newsletters (extract summaries)

**Step 2: Parse & Categorize** (LLM-assisted)
- Identify pain points ("users frustrated with X")
- Flag solution requests ("looking for Y tool")
- Extract signals ("company hiring for Z" = market move)
- Classify sentiment (bullish/bearish/neutral on topic)
- Tag by domain (AI, fintech, infrastructure, etc.)

**Step 3: Aggregate & Synthesize** (report generation)
- Daily/weekly reports per channel
- Cross-platform insights ("Reddit pain point matches job demand matches GitHub trend")
- Trending topics (what's moving across multiple sources)
- Opportunity detection (unmet needs + job demand + emerging repos)

**Step 4: Output & Action**
- Markdown reports to vault (auto-file by domain)
- Slack summaries (daily digest)
- Task creation (high-signal opportunities for research)
- Jarvis integration (feed into [[Claude OS]] knowledge layer)

### Platform Selection: Orchestration for All Six Channels

**Key requirement:** Single platform that handles:
- Multiple data source integrations (API, RSS, scraping)
- Scheduled runs (daily/weekly/event-based)
- LLM-powered processing (Claude API calls)
- Error handling and retry logic
- Output automation (write to vault, Slack, email)

**Recommended platforms (ranked by fit):**

1. **n8n (self-hosted or cloud)**
   - ✅ Open-source, free self-hosted option
   - ✅ 1,000+ integrations (Reddit API, LinkedIn, Gmail, GitHub, RSS)
   - ✅ Native LLM node (Claude API support)
   - ✅ Can write directly to vault via MCP or webhook
   - ✅ Complexity: Medium (visual workflow builder)
   - Cost: Free (self-hosted) or $20–100/mo (cloud)

2. **Make.com (formerly Integromat)**
   - ✅ Visual workflow, very user-friendly
   - ✅ All integrations available
   - ✅ LLM support (Claude, GPT-4)
   - ❌ Paid-first: ~$10/mo minimum
   - ❌ Execution time limited on free tier
   - Cost: $10–600+/mo depending on scenario complexity

3. **Zapier**
   - ✅ Most integrations (2,000+)
   - ✅ Claude Action available
   - ❌ Most expensive option
   - ❌ Limited execution time per action
   - Cost: $20–600+/mo

4. **Custom: Airflow + Claude API**
   - ✅ Full control, no platform limits
   - ✅ Scales to any complexity
   - ❌ Requires DevOps; self-hosted infrastructure
   - ❌ Steeper learning curve
   - Cost: $0–50/mo (cloud compute) + development time

5. **Custom: GitHub Actions + Claude API**
   - ✅ Free for public repos
   - ✅ Good for simple daily/weekly runs
   - ❌ Limited to cron scheduling
   - ❌ Workflow YAML complexity
   - Cost: $0 (free tier)

**Recommendation for your context:**
- **Near-term (MVP):** GitHub Actions + Claude API (free, no infrastructure)
  - Daily cron jobs per channel
  - Python scripts (Reddit, LinkedIn scrape, etc.)
  - Claude API for analysis
  - Write results to vault via git push
- **Medium-term (scale):** n8n self-hosted
  - Visual workflows reduce maintenance
  - All integrations handled by platform
  - Direct vault integration via MCP
  - Easy to add new channels

### Scope: 10% of Total Automation Work

**This section captures the framework.** Full implementation involves:

1. **Data source setup** (Reddit API OAuth, LinkedIn scraping auth, Gmail API token, GitHub API key, RSS feed parsing)
2. **Channel-specific scrapers** (Reddit posts → pain/solution/advice categories; LinkedIn jobs → regex for skills; GitHub → trending detection; trading news → sentiment analysis)
3. **LLM prompts** (analyze Reddit thread for emerging problems; classify GitHub repo significance; extract job requirements; rate-score trading news impact)
4. **Vault integration** (auto-file reports by domain; link to existing notes; create tasks from opportunities)
5. **Error handling** (API limits, auth failures, duplicate detection, data validation)
6. **Performance tuning** (caching, batch processing, cost optimization on Claude API calls)

Each channel alone is 2–3 weeks of work. Total estimated effort: **8–12 weeks for full system with error handling and Jarvis integration.**

### Data Flow Diagram (Conceptual)

```
Reddit API → Parse pain/solution/advice → Categorize
LinkedIn API → Scrape jobs → Extract skills/demand
GitHub API → Trending repos → Classify patterns
Job APIs → Parse requirements → Tag skills
RSS feeds → Filter trading news → Sentiment score
Gmail API → Read newsletters → Extract summaries
         ↓
    Claude API (analysis layer)
         ↓
    Aggregate & Synthesize
         ↓
    Reports → Vault (auto-file by domain)
    Reports → Slack (daily digest)
    Reports → Tasks (high-signal opportunities)
```

### Open Questions for Implementation

- [ ] Which channel should be built first (Reddit → LinkedIn → GitHub → jobs → news → email)?
- [ ] Should reports go to Jarvis vault, or separate "Research" vault, or both?
- [ ] Frequency: daily or weekly per channel? Real-time alerts for high-signal items?
- [ ] LLM cost: how many Claude API calls per day for all channels? (budget constraint?)
- [ ] GitHub Actions + Python vs. n8n self-hosted vs. Make.com? (trade-off: cost vs. maintenance)
- [ ] How to detect duplicates across channels (same signal in Reddit + LinkedIn + GitHub)?

### Integration with Jarvis

Once built, this feeds into [[Claude OS]] as:
- **Knowledge layer input:** research reports auto-file into vault
- **Signal detection:** high-opportunity items create tasks
- **Trend analysis:** jarvis-memory queries ("what's moving in fintech right now?") pull from aggregated reports
- **Decision support:** when working on TradingView or portfolio projects, research automation surfaces relevant market moves

---

## Orby (Portfolio): Model Regression Detection for Eval

**From BASWE 15 Project 1 — Implement for Portfolio**

Use **deepeval + GitHub Actions** as the eval/testing layer for portfolio AI Lab.

**Setup:**
- `deepeval eval` runs on every model/prompt change in CI/CD.
- Multi-dimensional scoring (faithfulness, relevance, correctness).
- HTML diff report + pass/fail gate before deploy.
- Catches AI-generated hallucinations before shipping to recruiter.

**Implementation:**
1. Hand-build 30–50 golden Q&A pairs from portfolio materials (resume, projects, experience).
2. Set evaluation thresholds (e.g., must pass faithfulness >0.8 to merge).
3. GitHub Actions: runs deepeval on every push to `portfolio` branch.
4. Loom video: show eval framework catching a hallucination, then fix.

This is the **eval gap backstop** for Orby's AI Lab agent.

---

## Claude Code Skills & Repos: Implement vs. Knowledge Matrix

**Sources:**
- [[60_Claude/10_Source_Summaries/PDF Ingestion/Free Claude Code Skill Libraries (PDF)]]
- [[40_Resources/CS/Repos.md]]

**Status:** CRITICAL DECISION GATE — 380+ skills exist. Most are **reference/knowledge only**. This section distinguishes what to **actually install** vs. what to **check before building**.

### The Implementation Problem

Your Repos.md file has 100+ starred repos with annotations:
- `(*INSTALL: GLOBALLY)` — means install now
- `(*COPY)` — means copy and customize
- `(*COPY GLOBALLY*)` — copy and make universal
- `(*MATERIAL*)` — read before building, but don't install
- `(*HOW USEFUL?*)` — uncertain; needs research before deciding
- `(*not useful*)` — skip

**But most repos are marked with questions, not decisions.** This session needs to resolve: what gets installed vs. what stays as reference?

### The Skill Library Landscape

**What exists (too much to use all):**
- **Awesome Agent Skills** — 380+ community skills (too broad; mine for specific gaps only)
- **Claude Command Suite** — 148 commands + 54 agents (reference directory)
- **Production-Ready Commands** — 57 vetted commands (curated; higher quality)
- **Awesome Claude Code** — index of skills/hooks/commands (reference, not install all)
- **gstack** (Garry Tan) — 13 proven skills (creator: YC, Initialized; **INSTALL**)
- **mattpocock-skills** — 18 skills fixing agent failure modes (battle-tested; **INSTALL GLOBALLY**)
- **ECC** (affaan-m) — one-shot agent harness + memory + security (FORK or INSTALL)
- **Agency Agents** — 105K stars, complete AI agency template (should study, maybe fork)

### Implementation Decision Matrix

**Tier 1: INSTALL NOW (Proven, High-Value)**

| Repo | What | Install How | Priority | Status |
|------|------|---|---|---|
| **ECC** | Agent harness + skills + memory + security | Fork or `npx ecc install` | CRITICAL | ✅ In your setup |
| **mattpocock-skills** | 4 skills: verbose-thinking, entropy-check, feedback-loop, surface-level fix | `npx skills add mattpocock/skills` | HIGH | ❓ Do you have this? |
| **gstack** | 13 proven skills: founder-review, eng-manager, release-manager | Copy `.md` files to `.claude/commands/` | HIGH | ❓ Which ones? |
| **cpr-compress-preserve-resume** | Session persistence: `/preserve`, `/compress`, `/resume` | Install as skill or MCP | HIGH | ✅ Mentioned in setup |
| **context-sync** | SQLite-backed memory MCP | `claude mcp add context-sync` | MEDIUM | ❓ Do you have this? |
| **spec-kit** | Spec-driven dev: constitution → spec → plan → tasks | `npx spec-kit specify` | HIGH | ❓ GitHub or local? |

**Tier 2: EVALUATE THEN DECIDE (High-Star, Uncertain Fit)**

| Repo | What | Fit for Your Work? | Decision Needed |
|------|------|---|---|
| **Hermes Agent** | 171K-star Nous Research agent | ACP/MCP support; alternative if Claude Code hits limits | Worth trying as fallback? Or Cursor/Kiro enough? |
| **Browser Use** | 96K-star web automation for agents | Useful for Orby (portfolio) AI Lab scraping? | Install only if needed for portfolio research |
| **Goose** | 50K-star autonomous agent (Rust) | ACP/MCP native; mechanical tasks | Do you need autonomous agent, or is Claude Code enough? |
| **Agency Agents** | 105K-star complete agency template | Study for patterns; consider forking | Copy patterns to CLAUDE.md or skip? |
| **OpenCode** | 166K-star open-source coding agent | Fallback if Claude Code unavailable | Install only if you hit Claude rate limits badly |
| **Multica** | 34K-star task dispatch across agents | Useful for parallel Cursor + Claude work? | Do you need this, or git-based workflow sufficient? |
| **AgentScope** | 25K-star Alibaba agent framework | MCP-native, multi-modal | Compare to existing stack; duplicate? |

**Tier 3: KNOWLEDGE/REFERENCE (Don't Install; Check Before Building)**

| Repo | Purpose | When to Consult |
|------|---------|---|
| **Awesome MCP Servers** | 1,000+ MCP index | Before building any new integration |
| **Claude Code Best Practice** | 55K-star best practices | Read once; reference on CLAUDE.md patterns |
| **System Prompts Collection** | Extracted system prompts | When writing agent instructions |
| **Awesome Claude Skills** | Skill index | Mining for /challenge, /emerge, /drift implementations |
| **awesomeclaude.ai** | Skill directory | Browse; don't bulk-install |

**Tier 4: NOT USEFUL (Skip)**

| Repo | Why Skip |
|------|---|
| Claude Code Templates | Duplicate of other tools; `npx aitmpl` not useful |
| Dify | Self-hosted platform; not solo agentic tooling |
| React Three Fiber | Frontend library; not part of core stack |
| Modern JS Cheatsheet | Reference; not actionable |
| Ghostty Blackhole | Terminal config; distraction |

### What You're Actually Missing (Implementation Gaps)

Looking at your Repos.md annotations, these need **decisions before next session:**

**Marked `(*HOW USEFUL?*)` or `(*INSTALL?*)` :**
1. **TradingView MCP** — "free?" — Does it work? Is it worth integrating?
2. **Polymarket MCP** — "how to use on laptop?" — Worth trying for prediction markets?
3. **Claude Context** — "over use of context?" — Should you use this for BOOM?
4. **CL4R1T4S** — "best resource for guard-railed models" — What does this actually do?
5. **GSD Core** — "how to work with other installations?" — Conflicts with existing setup?
6. **Obsidian Mind** — "workflow needs to be studied" — Extract patterns or fork?
7. **memsearch** — "how realistic to use?" — Alternative to jarvis-memory?
8. **MiroFish** — "how to use for my cases?" — Useful for trading + prediction markets?
9. **Autoresearch** (Karpathy) — "karpathy needs to be used" — Should you fork this?
10. **Scrapling** — "worth learning?" — Better than BeautifulSoup for trading data?

### Recommended Action: Implementation Audit

**Before you implement any new skill or repo:**

1. **Is it solving a named gap?** (e.g., `/challenge` skill closes a gap in Jarvis)
2. **Does it conflict with existing tools?** (e.g., memsearch vs. jarvis-memory)
3. **What's the install cost vs. benefit?** (15 min to copy skill vs. 1 hour to debug integration)
4. **Who maintains it?** (Anthropic/YC-backed vs. hobby project vs. dead?)
5. **Can you test it in one session?** (MVP first; don't commit without testing)

### Implementation Queue (Proposed Priority Order)

**This Week:**
- ✅ mattpocock-skills (if not installed): 4 skills, 15 min
- ✅ Verify gstack is copied + customized: founder-review, eng-manager for shipping
- ⚠️ TradingView MCP: test on real TradingView chart (1 hour; report whether it works)
- ⚠️ Polymarket MCP: read docs; decide if worth setup (30 min research)

**Next Week:**
- ⚠️ Obsidian Mind: extract 5 lifecycle hooks; implement in CLAUDE.md
- ⚠️ MiroFish: evaluate for trading bot (1 hour proof test)
- ⚠️ Hermes Agent: try as Claude Code fallback if hitting limits

**Later (Batch Review):**
- Audit CL4R1T4S, GSD Core, Autoresearch, Scrapling, memsearch
- Resolve all `(*HOW USEFUL?*)` marks in Repos.md

---

### Principle: **Implement > Knowledge**

Your Repos.md has excellent discovery, but it's become an archive. The rule going forward:

- **Install only what closes a named gap** or unlocks a blocked project
- **Reference everything else** via Awesome indexes before building from scratch
- **Test before committing** (can you use it in one session?)
- **Mark decisions** in Repos.md: `(*INSTALLED*)`, `(*SKIP*)`, or `(*EVAL: DATE*)`

This session captured the framework. Next session should resolve the `(*HOW USEFUL?*)` queue and commit to Tier 1 installs.

---

## Code Review & Eval Gap: Pre-Commit AI Backstop

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/CodeRabbit CLI Code Review (PDF)]]

### Problem
Claude/Cursor-generated code ships with systematic errors: hallucinated function calls, off-by-one errors, missing tests, hardcoded secrets, race conditions. The eval/observability gap is flagged across [[15 AI Engineering Projects]], [[Jarvis OS — North Star]], and vault skills.

### CodeRabbit CLI: NOT VIABLE ❌

**Tested in production and rejected:**
- Claims "free to start" but effectively paid service (rate limits after <2 PRs)
- Unreliable: doesn't work ~50% of the time in actual PR workflow
- CLI and PR integration hit same limits (same backend service)
- Cost/benefit: not worth the time vs. free alternatives

**Status:** FIND AN ALTERNATIVE

### Recommended: Free Stack Instead

**For AI-generated code review:**
1. **Semgrep** (free, open-source) — Catches real bugs (logic errors, SQL injection, secrets, race conditions)
   - Runs pre-commit locally
   - No rate limits, no API costs
   - Integrates with GitHub Actions
2. **PyLint** + **ESLint** (free) — Syntax and style errors
3. **Pylance/Copilot** (free in VS Code) — Real-time type checking during coding

**For AI output validation:**
1. **deepeval** (free) — Already captured in [[#Orby (Portfolio): Model Regression Detection for Eval]]
   - Multi-dimensional scoring (faithfulness, correctness, relevance)
   - Runs in CI/CD; no rate limits
2. **Local LLM-as-judge** (once distilled 3B model is built) — Confidence-scored validation, zero running cost

### Adoption Pattern
1. **Immediate:** Set up Semgrep + GitHub Actions for portfolio pre-deploy gate
2. **Parallel:** Implement deepeval for Orby AI Lab output validation
3. **Scale:** Add local LLM-as-judge once distilled model is ready

### Anti-Drift
Focus on free, reliable tools (Semgrep, deepeval, PyLint) instead of paying services with unreliable rate limits.

---

## Model Distillation: Distill 70B into 3B for Task-Specific Offline Inference

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/Clone — Distill a 70B into a 3B (PDF)]]

**Status:** MUST BE IMPLEMENTED using Unsloth (but requires deep research on use case first)

### Core Concept
Task-specific model distillation: a 70B teacher generates thousands of labeled examples for a *narrow* task → fine-tune a 3B student on them → the 3B replicates the 70B's behavior on that task without needing the 70B's weights or any internet.

**Benefits:**
- Runs locally at ~60 tokens/sec on Apple Silicon or consumer GPU
- Zero API costs after training (~$12 one-time build cost)
- Offline: no internet, no API keys, data never leaves the machine
- Ideal for health/legal/finance/proprietary data use cases

### Three-Step Pipeline

**Step 1: Generate Training Data (distilabel)**
- 70B teacher model (Together AI: Meta-Llama-3.1-70B-Instruct-Turbo)
- Load 100–200 seed examples from Hub
- `TextGeneration` step with system prompt defining the task
- `UltraFeedback` judge (same 70B scores each generation)
- **Always dry-run first** (`pipeline.dry_run()`) to validate DAG before spending
- Cost: ~$4.40 to generate 3,000 examples

**Step 2: Fine-Tune (Unsloth + LoRA)**
- Load Llama-3.2-3B-Instruct in 4-bit quantization
- Add LoRA adapters (r=16, target q/k/v/o_proj)
- `SFTTrainer`: batch 4, grad-accum 4, 3 epochs, lr 2e-4
- **Critical:** Verify correct chat template (EOS token between examples; without it, context leaks and model hallucinates)
- Export as GGUF (Q4_K_M quantization)
- Runtime: ~90 min on A100 (RunPod/Colab)
- Cost: ~$4.50 for A100 time

**Step 3: Deploy Offline (Ollama)**
- Write `Modelfile` with GGUF path, temperature, system prompt
- `ollama create your-model`
- Serve via OpenAI-compatible endpoint: `http://localhost:11434/api/generate`
- Zero running cost

### Total Cost: ~$11.50 per distilled model

- Data generation + judging: ~$7
- Fine-tuning: ~$4.50
- Deployment: $0

### Open Research Questions: What Task Should You Distill?

This is the gap to resolve before building. Candidates:

**Option 1: Trading-Specific Model**
- Task: Predict market direction from news/sentiment/technicals
- Train on: Trading bot's research → prediction pipeline outputs
- Deploy: Fast, offline market analysis for prediction markets or stocks
- Use case: High-frequency classification (bullish/bearish/neutral) without hitting Claude API limits
- Related: Companion to Kronos time-series model or standalone for market sentiment
- **Question:** Would a distilled 3B sentiment classifier beat Kronos for speed? Or is it orthogonal?

**Option 2: Jarvis Skill Distillation**
- Task: Specific Jarvis workflow (e.g., `/challenge` pressure-testing, `/ideas` idea-generation)
- Train on: Successful vault examples + generated counter-examples
- Deploy: Run /challenge offline on vault notes without API cost
- Use case: Daily async skill runs when Claude API is rate-limited or expensive
- **Question:** Which Jarvis skill is repetitive enough to justify distillation?

**Option 3: Portfolio/Orby Distillation**
- Task: Extract structured info from resume/projects/experience
- Train on: Your actual portfolio materials → structured schema
- Deploy: Fast, offline parsing for the AI Lab agent
- Use case: Reduce API calls in portfolio AI Lab; recruiter privacy (no Claude API calls for their interactions)
- **Question:** Is this redundant with deepeval/GPT-4o-vision, or complementary?

**Option 4: Repetitive Task Extraction**
- Task: JSON extraction from documents (e.g., parsing financial reports, research summaries)
- Train on: 100–200 examples of unstructured → structured JSON
- Deploy: Ultra-fast document processing pipeline
- Use case: BOOM alert enrichment, trading research pipeline, Jarvis ingestion
- **Question:** Which ingestion pipeline (BOOM, trading research, Jarvis) would benefit most?

### Red Flags & Gotchas

1. **EOS token:** The model's end-of-sequence token (e.g., `<|eot_id|>`) must appear between training examples. Without it, examples leak context and the model hallucinates. Unsloth's `SFTTrainer` handles it only if the **correct chat template** is applied. **Verify this before training or the 90 min is wasted.**

2. **Dry-run discipline:** Always run `pipeline.dry_run()` first (free, validates DAG). A misconfigured full run of 3,000 examples costs ~$7 and produces unusable data.

3. **Eval story missing:** The PDF doesn't specify how to measure whether the 3B actually matches the 70B on your task. You need:
   - Held-out test set (10% of data)
   - Brier score or task-specific metric
   - Benchmark against the 70B teacher on the same set

4. **Quantization matters:** Q4_K_M GGUF is a safe default, but you may need Q5_K_M or F16 if the 3B undershoots on your task (size/quality trade-off).

### Implementation Path (Once Task is Clear)

1. **Identify the narrow task** — One specific workflow, not "all of Jarvis" or "all trading"
2. **Collect 100–200 seed examples** of input → desired output (manually or mined from your vault)
3. **Run distilabel dry-run** to validate pipeline
4. **Generate 3,000 training examples** (distilabel + Together AI)
5. **Fine-tune 3B on Colab/RunPod** (90 min, Unsloth)
6. **Eval on held-out set** (Brier, accuracy, or task-specific metric)
7. **Deploy to Ollama** (Modelfile + local inference)
8. **Integrate into project** (replace API calls for this specific task with local 3B)

### Recommended Starting Point

Given your projects, **Option 1 (Trading-Specific Model)** seems highest-leverage:
- Your trading bot needs fast, repetitive sentiment/direction classification
- A distilled 3B runs offline (good for Bangalore week with spotty internet)
- Cost ($12) is negligible vs. trading upside
- Pairs well with existing Kronos time-series model
- **But:** need to clarify whether it's a sentiment classifier or direction predictor, and how it fits with Kronos

**Next step:** Dive deeper into one task option (probably trading) before committing to the build.

---

## DeepThinksFinance: Competitive Analysis & Proof Testing (Not Primary Source)

**Sources:** 
- [[60_Claude/10_Source_Summaries/PDF Ingestion/DeepThinksFinance AI Portfolio Optimizer (PDF)]]
- [[60_Claude/10_Source_Summaries/PDF Ingestion/DeepThinksFinance Master Quant Prompt Guide v2 (PDF)]]

**Status:** INFORMATIONAL BUT REQUIRES VERIFICATION — Treat as case studies, not blueprints. Both PDFs exhibit signs of AI-generated content ("too good to be true"; India-specific hardcoding; retail signal over-confidence).

### What These PDFs Cover

**Portfolio Optimizer (31 pages, full-stack app):**
- React 18 + Tailwind + Plotly frontend
- FastAPI + Python backend
- Modern Portfolio Theory (MPT) with Monte Carlo (10,000 portfolios)
- Claude API as analyst layer (turns optimization output into prose)
- Complete with Docker, pytest suite, deployment guide

**Master Quant Prompt Guide v2 (188 pages, 10 models + 50+ prompts):**
- Copy-paste prompt → Claude generates Python → run on Colab → interactive charts
- 10 models: Monte Carlo, Black-Scholes, Market Timing, ML Direction, Macro Prediction, Mean Reversion, Pairs Trading, Factor Attribution, VaR & Stress, Portfolio Optimization
- All free stack: yfinance + pandas + numpy + scipy + plotly
- India-specific (NIFTY 50, NSE, ₹, RBI rates) but adaptable

### Useful Architectural Patterns to Extract

**From Portfolio Optimizer:**
1. **Three-layer system:** data pipeline (yfinance) → quantitative engine (scipy optimize) → LLM explanation layer
   - Claude's role: analyst *over* deterministic math, **not inside the decision loop** (safer than prediction market bot)
2. **Risk profile → constraints mapping:**
   - Conservative: 25% max position, min-volatility objective
   - Moderate: 35% max position, max-Sharpe objective
   - Aggressive: 50% max position, max-return objective
3. **Unit test invariants:** All 10,000 weight vectors sum to 1 within 10^-10
4. **Deployment pattern:** Separate backend/frontend, Docker-compose, GitHub Actions for CI/CD

**From Master Quant Guide:**
1. **Blended volatility:** `0.6 * (VIX/100) + 0.4 * (90-day historical)` — flagged as institutional approach over pure historical
2. **Cholesky decomposition** for correlated multi-asset Monte Carlo (preserves correlation structure)
3. **Four VaR methods side-by-side comparison:**
   - Historical (percentile of returns)
   - Parametric ($-z\sigma P$, assumes normal distribution)
   - CVaR / Expected Shortfall (average loss beyond VaR)
   - Monte Carlo (GBM-simulated distributions)
4. **Fama-French factor attribution:** Separate factor beta from true alpha via rolling OLS
5. **Signal engineering:** Z-Score, Bollinger Bands, RSI divergence (but flagged as descriptive, not validated)

### What Needs Verification Before Building

**Red flags requiring testing:**

| Component | Claim | Verification Needed |
|-----------|-------|---|
| **Retail Signals (RSI/Bollinger)** | "Powerful in sideways markets" | Walk-forward validation on real universe; MIT Quant Bible warns these are descriptive, not edge factors |
| **Pairs Trading Z-Score** | "LTCM used this" | Does cointegration survive out-of-sample? Are spreads mean-reverting in live data? |
| **Mean Reversion Entry** | "Z < −1.5 AND RSI < 40" | Win rate overstated if not tested on holdout period. What was the backtest universe (tickers, years)? |
| **NIFTY Macro Model** | 43 indicators, "18 yrs data" | Survivorship bias? Data leakage in feature engineering? Does it work on S&P 500 or only NIFTY? |
| **Blended Vol** | "Institutional approach" | vs. pure realized vol — is the 0.6/0.4 split evidence-based or arbitrary? |
| **Black-Scholes Pricing** | Standard formula | Holds for liquid instruments; does NSE F&O data match assumptions? What about vol smile? |

### Implementation Strategy: "Proof Testing"

**Step 1: Extract Patterns (Don't Copy Code)**
- Use the portfolio optimizer's three-layer architecture (data → quantitative → explanation)
- Use Cholesky + blended vol for your Monte Carlo
- Use factor attribution to measure alpha vs. beta
- Use four VaR methods for risk validation

**Step 2: Test Components Independently**
- Implement Efficient Frontier (portfolio optimizer) first — it's the most stable (known math, easy to validate)
- Backtest mean reversion signals on your data (NIFTY or S&P 500) with walk-forward validation
- Validate cointegration on real pairs before pairs trading
- Compare four VaR methods on your portfolio; which matches live drawdowns best?

**Step 3: Validate Before Shipping**
- **Brier score:** Do predicted probabilities match real outcomes? (from ML Direction model)
- **Out-of-sample testing:** Holdout 20% of data; does model trained on 80% backtest generalize?
- **Deflated Sharpe:** Is the Sharpe ratio statistically significant or just lucky? (MIT Quant Bible framework)
- **Walk-forward window:** Retrain monthly; how stable are the factor loadings or signal strengths?

### TradingView Build Integration: What to Use, What to Skip

**Use:**
- Three-layer architecture (data → engine → Claude analyst)
- MPT + Monte Carlo + Efficient Frontier (foundational, well-understood)
- Cholesky for correlated simulations
- Blended vol for forward-looking risk estimates
- Four VaR methods (choose one, or compare all)
- Factor attribution for alpha decomposition

**Skip or heavily test:**
- Retail signals (RSI/Bollinger) as standalone trading rules
- NIFTY-specific code/assumptions (retarget to your data)
- Prompt-to-Python pattern (useful for rapid prototyping, but generated Python needs code review)
- Any backtest without out-of-sample validation

**Conditional:**
- Mean Reversion + Z-Score: test on your universe first (could work, or could be data-snooped)
- Pairs Trading: only if you find stable cointegrated pairs in your target universe
- Macro prediction: do the 43 indicators apply to your market and time horizon?

### Proof-Testing Roadmap

1. **Week 1:** Implement Efficient Frontier from Portfolio Optimizer (fastest path to a working system; most defensible)
2. **Week 2:** Add Cholesky + blended vol to Monte Carlo; validate VaR estimates vs. live portfolio history
3. **Week 3:** Build factor attribution; measure how much is alpha vs. market beta
4. **Week 4:** Test *one* signal (mean reversion OR pairs trading) on out-of-sample data; publish walk-forward stats
5. **Week 5+:** Integrate proven signals into TradingView bot; skip unvalidated ones

### Open Questions for Deep Dive

- [ ] Which of the 10 models is worth building: Efficient Frontier (low risk, high confidence) or Pairs Trading (higher edge, higher risk)?
- [ ] Do the retail signals (RSI/Bollinger/Z-Score) survive walk-forward validation on US equities or crypto?
- [ ] Is the "prompt → generated Python" pattern useful for your workflow, or does it waste time on code review?
- [ ] Can you adapt NIFTY-specific code (tickers, RBI rates, India VIX) to your market without revalidation?

### What NOT to Do

- ❌ Copy the prompt guide's Python directly; validate it first
- ❌ Deploy unvalidated signals (mean reversion, pairs trading) without walk-forward testing
- ❌ Assume retail indicator rules (RSI < 40, Z < −1.5) are edge factors; they're descriptive context
- ❌ Trust backtest results without out-of-sample verification or Deflated Sharpe calculation
- ❌ Use India-specific parameters (5.25% RBI rate, ^INDIAVIX) for US markets without adjustment

---

## Trading Bot Architecture: Five-Stage Pipeline

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/AI Prediction Market Trading Bot (PDF)]]

### Pattern Overview
A production trading bot scans for opportunities → researches → estimates probability → validates risk → learns from outcomes. This exact five-stage architecture (scan/research/predict/risk/compound) maps from prediction markets (Polymarket, Kalshi) directly to your stocks/ETFs TradingView build, with the same Claude skills structure and math.

### Stage 1: Scan (Find Tradeable Opportunities)
**Goal:** Filter noise; identify markets/tickers worth trading.

**For Stocks/ETFs (your build):**
- Connect to your data source (Alpha Vantage, TradingView API, or IEX Cloud).
- Filter by: volume ≥200k shares, price move >2%, volatility spike vs 20-day MA, bid-ask spread <0.5%.
- Anomaly detection: unusual volume, price correlation breaks (if you're monitoring pairs).
- Run every **15–30 minutes** during market hours.
- Output: ranked opportunity list by estimated edge potential.

**Skill structure:** `scan-stocks-skill.md` — Market filters, live data polling, opportunity ranking logic.

### Stage 2: Research (Gather Intelligence)
**Goal:** Build information edge; understand "why" the market moved.

**For Stocks/ETFs:**
- Parallel scraping: financial news (Reuters, Bloomberg RSS), Twitter/X sentiment on ticker/CEO, earnings announcements, sector momentum.
- Sentiment classification: bullish/bearish/neutral per source.
- Cross-reference to cut noise (one tweet ≠ signal, but unanimous sentiment + news + technical break = signal).
- Research brief: what sources say vs. what price action shows, and where the edge might be.

**Real-world example:** Bot processes earnings surprise, reprices within 90 seconds, captures spread → $896 profit on $2,000 position in <10 min. Edge is **faster processing at scale**, not smarter predictions.

**Skill structure:** `research-stocks-skill.md` — News scrapers, sentiment aggregation, research brief generation.

### Stage 3: Predict (Estimate True Probability/Direction)
**Goal:** Generate trade signal only when confidence exceeds threshold. **This is your edge.**

**Core Formulas:**

**Edge Calculation:**
```
edge = p_model - p_market  (trade only if edge > 0.04, i.e., 4%)
```
For stocks: $p_{model}$ = your model's probability of move >X% in Y days; $p_{market}$ = implied move from options (IV).

**Expected Value:**
```
EV = p · b - (1 - p)
```
where $b$ = profit/loss ratio (e.g., risk 1, win 2 = b = 1).

**Mispricing Score (Z-score):**
```
δ = (p_model - p_market) / σ  (how many std devs does model diverge from market?)
```

**Calibration Tracking (Brier Score):**
```
BS = (1/n) Σ(p_pred - outcome)²
```
Lower is better; **target <0.25** for a well-calibrated model.

**Multi-Model Ensemble (Real-World Winning Pattern):**
- Grok primary forecaster (30% weight)
- Claude Sonnet technical analyst (20%)
- GPT-4o bull advocate (20%)
- Gemini Flash bear advocate (15%)
- DeepSeek risk manager (15%)

Each votes independently; **consensus signals the trade**. This beats any single model.

**For your build:**
- Use Claude for news analysis + fundamental score.
- Use a lightweight local model or API for technical pattern recognition.
- Use options-implied volatility as market consensus.
- Log **every prediction** with its confidence; track Brier to verify you're actually better than the market.

**Skill structure:** `predict-stocks-skill.md` — Model scoring, ensemble voting, edge calculation, prediction logging.

### Stage 4: Risk Management & Execution
**Goal:** Ensure position sizing doesn't destroy you even with a 60% win rate.

**Risk Checks (All Must Pass):**
1. Edge > 0.04 (4%)
2. Position size ≤ Kelly calculation
3. New bet + existing exposure ≤ max portfolio exposure
4. **Value at Risk (VaR)** at 95% within daily limit
5. Drawdown >8% → block all new trades
6. Daily loss over threshold → stop for the day

**Position Sizing: Kelly Criterion**

Full Kelly formula:
```
f* = (p · b - q) / b
```
where $p$ = win probability, $q = 1-p$, $b$ = net odds (profit/loss ratio).

**Example:** $10,000 bankroll, 70% win prob, 2:1 reward/risk
- Full Kelly = 12% = $1,200 (too aggressive; violent swings)
- **Quarter-Kelly = 3% = $300** (professional standard; lower ruin risk)
- **Half-Kelly = 6% = $600** (middle ground)

**Use fractional Kelly (0.25–0.5×) in practice.** Full Kelly is mathematically optimal but destroys accounts.

**Execution Rules:**
- Limit orders only (never market order).
- Abort if slippage >2% between signal and actual fill.
- Kill switch: create a `STOP` file to halt all new orders immediately.
- Auto-hedge on new information (if you entered long and breaking news changes the thesis).

**Risk Validation:** Put all deterministic risk checks in Python scripts, not markdown. Code is deterministic; prose instructions can be interpreted differently each run.

**Skill structure:** `risk-stocks-skill.md` — Edge validation, Kelly calculator (calls Python script), execution rules, kill switch.

**Python scripts:**
```
scripts/
  validate_risk.py      (deterministic risk checks)
  kelly_size.py         (position calculator: f* = (p·b - q) / b)
```

### Stage 5: Compound (Learn & Improve)
**Goal:** A bot that doesn't learn from failures is gambling with extra steps.

**What to Track:**
- Full trade logs: entry/exit, predicted probability, actual outcome, P/L, time held, market conditions.
- Loss classification: bad prediction / bad timing / bad execution / external shock.
- Nightly consolidation: update knowledge-base file (scan and research agents read this before next day).

**Metrics to Monitor:**
| Metric | Target | Why |
|--------|--------|-----|
| Win Rate | 60%+ | Baseline signal quality |
| Sharpe Ratio | >2.0 | Risk-adjusted returns |
| Max Drawdown | <8% | Don't blow up |
| Profit Factor | >1.5 | Avg win / avg loss |
| Brier Score | <0.25 | Calibration quality |

**Reference backtest (Anthropic's prediction-market bot):**
- 68.4% win rate
- 2.14 Sharpe
- −4.2% max drawdown
- 312 trades / 90 days

This is a **backtest, not live trading** — expect live results to be messier.

**Implementation:**
- Trade log database (SQLite): entry/exit/conditions/outcome.
- Nightly job: aggregate losses by type, update `failure_log.md`.
- Knowledge base: what markets/tickers worked, what didn't, why.
- Brier tracker: am I getting better at probability estimates, or just lucky?

**Skill structure:** `compound-stocks-skill.md` — Trade log parser, loss classification, knowledge-base updater.

---

### Prediction Market Bot → Stocks/ETFs Translation

| Element | Prediction Market (Polymarket) | Your Stocks Build |
|---------|--------------------------------|-------------------|
| **Scan** | Polymarket CLOB API, find high-volume markets | Alpha Vantage/TradingView, volume >200k, price moves |
| **Research** | Twitter sentiment on event, news RSS | Earnings, sector news, options IV, CEO tweets |
| **Predict** | Estimate event probability vs market price | Estimate move probability vs options-implied move |
| **Risk** | Kelly on yes/no contracts | Kelly on long/short positions; position size in $ |
| **Compound** | Trade log + loss classification | Win/loss stats, Brier tracker, strategy journal |
| **API** | Polymarket REST + WebSocket | Alpha Vantage (free tier limited) or paid provider |
| **Skills** | SKILL.md structure (5 files) | Same: scan, research, predict, risk, compound |

---

### Implementation Roadmap for Your Build

**Week 1:** Set up live data feeds (Alpha Vantage or broker API); manual trades to learn mechanics.

**Week 2:** Build scan skill; log opportunity data; **don't trade yet**.

**Week 3:** Build research + predict skills; backtest predictions against outcomes; track Brier — *are you better than the market?*

**Week 4:** Risk skill + Kelly calculator; **paper trade ≥2 weeks** before live money.

**Week 5+:** Live trading at **$100–500 max exposure** (per position or total?); scale only after **50+ trades** with verified positive results.

---

### Anti-Patterns to Avoid

1. **Bad calibration** — Model says 80% up, reality is 55% → oversized positions, fast losses. Track Brier religiously.
2. **Overfitting** — Great backtest, fails live. Always test out-of-sample (hold-out period).
3. **Liquidity traps** — Good on paper, can't actually fill at wanted price. Check orderbook depth first.
4. **API failures** — Data providers have downtime. Handle disconnects; never leave orphaned positions.
5. **Runaway costs** — 5-min heartbeat checks alone cost $50+/day. Budget API spend explicitly (e.g., $50/day max).
6. **Position abandonment** — Forgetting that you're in a trade because the bot lost connection.

---

### Decision Points for Your TradingView Build

1. **Data source priority:** Alpha Vantage (free, limited), paid broker API (better), or IEX Cloud (fast)?
2. **Multi-model ensemble:** Will you use Claude for all stages, or split (Claude for research + predict, local model for scan)?
3. **Edge threshold:** 4% (from prediction markets) or different for stocks? (Consider bid-ask spread, commissions.)
4. **Kelly fraction:** Start at quarter-Kelly, half-Kelly, or full Kelly for your risk tolerance?
5. **Kalshi demo first?** The PDF recommends learning on Kalshi's mock-money environment first; is there a stocks paper-trading equivalent?
6. **Time horizon:** Are you trading day trades, swings (1–5 days), or longer positions? Changes the scan frequency and research depth.

---


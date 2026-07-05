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

## Claude Code Skills: Targeted Mining vs. Bulk Installing

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/Free Claude Code Skill Libraries (PDF)]]

### Principle
Skills are `.md` files in `~/.claude/commands/` (global) or `.your-project/.claude/commands/` (project). 380+ free skills exist (Awesome Agent Skills, Claude Command Suite, Production-Ready Commands), but **width is the disease, not the cure** — targeted mining against named gaps beats bulk-installing.

### High-Value Mining Targets

**Confirmed Gaps to Mine Against:**
1. **/challenge** — Pressure-test beliefs; surface contradictions (Awesome Claude Skills).
2. **/emerge** — Identify clusters coalescing into projects (custom build or adapt from awesomeclaude.ai).
3. **/drift** — Surface loosely-threaded recurring themes (custom or library adapt).
4. **/security-review** — Pre-commit/pre-deploy code audit (Claude Command Suite has these).
5. **/eval-suite** — Catch AI agent generation failures (adapt Project 1 regression-detection logic).

### Implementation
- Use **awesomeclaude.ai** as a browse-before-adopt directory.
- Copy only `.md` files that close a named gap.
- Review before installing (skills run with full project access).
- Anti-drift: skill shopping is weekly-slot work, not daily operations.

---

## Code Review & Eval Gap: Pre-Commit AI Backstop

**Source:** [[60_Claude/10_Source_Summaries/PDF Ingestion/CodeRabbit CLI Code Review (PDF)]]

### Problem
Claude/Cursor-generated code ships with systematic errors: hallucinated function calls, off-by-one errors, missing tests, hardcoded secrets, race conditions. The eval/observability gap is flagged across [[15 AI Engineering Projects]], [[Jarvis OS — North Star]], and vault skills.

### Solution: CodeRabbit CLI
- Runs locally, pre-commit.
- Free to start; catches what the agent missed.
- Positioned as a backstop for AI-generated code.

### Adoption Pattern
1. **Trial:** Set up on Portfolio pre-deploy gate (cheapest backstop).
2. **Parallel:** Implement `/eval-suite` skill to close the Jarvis skills' eval gap (same pattern as BASWE Project 1).
3. **Scale:** Consider integrating into GitHub Actions for CausalOps/BOOM CI/CD.

### Anti-Drift
This is **not** a tool to adopt immediately. It's a named gap to trial when shipping a portfolio project (Option A or B above).

---


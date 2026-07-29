---
type: evergreen
status: sprout
created: 2026-07-05
tags:
  - implementation
  - ingestion
  - github
  - tools
notes:
  - "[[60_Claude/10_Source_Summaries/GitHub Ingestion/How Anant Uses Each Repo]]"
  - "[[PDF's Ingestion Implementation]]"
  - "[[Web Ingestion Implementation]]"
---

# GitHub Ingestion Implementation

Actionable repo adoption priorities from the comprehensive GitHub guide: VS Code + Claude setup, project-specific tooling, and infrastructure decisions.

---

## VS Code + Claude Setup (Priority 1 — Install Today)

**Source:** [[60_Claude/10_Source_Summaries/GitHub Ingestion/How Anant Uses Each Repo]] → "Today's Goal: VS Code + Claude Setup"

### Install Immediately (< 10 min each)
1. **ECC** (affaan-m) — Drops CLAUDE.md, skills, memory, and security hooks in one shot. Wires all four agents (Claude, Cursor, Kiro, Copilot) to shared context.
2. **mattpocock-skills** — Four skills fixing common Claude failures (verbose-thinking, entropy-check, feedback-loop, surface-level answers).
3. **cpr-compress-preserve-resume** — Session persistence: `/preserve`, `/compress`, `/resume`. Critical for long Jarvis ingestion sessions.
4. **context-sync** — SQLite-backed memory MCP. Lightweight alternative to memsearch for immediate adoption.

### Read Before Writing (15 min)
- **get-shit-done templates** — Context-dump template for priming Claude Code sessions (saves 20 min per session).
- **claude-code-best-practice** (shanraisshan) — 55K stars; community consensus on working patterns. Copy CLAUDE.md template, agent patterns, hooks section.
- **system-prompts-and-models-of-ai-tools** — Understand default system prompts of Cursor/Kiro so CLAUDE.md overrides actually stick.

### Secondary Installs This Week
- **gstack** (garrytan) — Battle-tested skills: founder-review, eng-manager, release-manager for shipping code.
- **addyosmani/agent-skills** — Spec-first, test-before-ship, observability-check (for BOOM).
- **spec-kit** — Before writing any code: `npx spec-kit specify "feature"` → constitution → spec → plan → tasks.
- **claude-code-templates** (davila7) — 100+ agent/MCP/hook scaffolds via `npx aitmpl`.

### Memory & Persistence (Week 2)
- **memsearch** (Zilliz) — Auto-index all Claude Code sessions to Milvus. Use weekly once adopted.
- **PageIndex** — Vectorless RAG over Jarvis vault using document reasoning instead of embeddings.
- **graphify** — Post-ingestion: run on full Jarvis vault; exports NetworkX graph to show dense/orphaned areas.
- **obsidian-mind** — Extract 5 lifecycle hooks (session-start, task-complete, context-full, vault-write, session-end); implement in Jarvis CLAUDE.md.

---

## Project-Specific Tooling

### BOOM (Rust / Observability / Distributed Systems)
- **promptfoo** — Test BOOM's alert pipeline with edge cases; run before merging.
- **ASI-Evolve** — Curriculum-based training for BOOM's rare-event classifiers (generalization without massive datasets).
- **dots.ocr** — Enrich astronomical image cutouts if BOOM pipeline needs text extraction.
- **airllm** — Run large models locally on GPU for testing enrichment classifiers.
- **claude-context** — Semantic code search over BOOM's Rust sprawl (~40% token reduction on large codebase).

### Portfolio (Next.js / Three.js / AI Lab)
- **browser-use** — Dynamic AI Lab agent that can browse GitHub, pull live commit activity, present to recruiters.
- **semantic-search-nextjs-pinecone-langchain-chatgpt** — Template for AI Lab: embed materials → semantic search → Claude answers.
- **react-three-fiber** — Refactor Three.js spaghetti into declarative R3F components (particle sphere, floating cards).
- **pocketbase** — Replace Sanity: one Go binary (auth, DB, storage, realtime) for profile/projects/experience/blog. Free, self-hosted.
- **dify** — Study workflow builder UI for portfolio's "proof pack" generator (retrieve materials → summarize → format for recruiter).
- **jarvis** (ethanplusai) — Voice interface pattern for AI Lab: talk → Three.js visualizes → Claude acts.

### Trading / Finance
- **TradingAgents** — Architecture: analyst/researcher/trader/risk-manager agents. Replace data source, keep communication pattern.
- **Kronos** — Foundation model trained on financial language. Better than scikit-learn classifiers for Alpha Vantage time-series.
- **MiroFish** — Swarm intelligence for decision layer. Ensemble > single model for signal quality.
- **tradingview-mcp** — Chart analysis MCP: send ticker → Claude interprets chart pattern → route to analyst agent.
- **Scrapegraph-ai** — Natural language scraping for financial news/earnings. Hook into researcher agent.
- **Scrapling** — Adaptive DOM tracking so trading scraper survives HTML changes.

### Jarvis / Knowledge System
- **n8n-workflows** — Automate ingestion pipeline steps: GitHub → Obsidian sync, email digest → vault note, web scrape → clipping.

---

## Agent Frameworks (Multi-Agent Coordination)

**Decision:** Pick one for parallel agent work on BOOM/portfolio.

- **beads** (gastownhall) — Atomic task claiming prevents agent stomping. Use for multi-agent BOOM subsystem work.
- **goose** — Autonomous agent for mechanical tasks (test writing); runs while you work on something else.
- **multica** — Task dispatch across multiple agents. Use when frontend (Cursor) + backend (Claude) work in parallel.
- **agentscope** (Alibaba) — Multi-agent runtime for TradingAgents. MCP-native, built for analyst-researcher-trader pattern.

### Anti-Drift: Only explore weekly
- **ruflo** (ruvnet) — Swarm behavior with Q-Learning routing (trading project later).
- **opencode** (anomalyco) — Fallback CLI when Claude Code rate-limited; shares same CLAUDE.md.
- **hermes-agent** — Understand architecture (171K stars = community consensus). Persistent skill accumulation pattern.

### Research finding (2026-07-29): does ECC actually solve this?
**No, not yet, and the earlier assumption that it was already installed was wrong.** Went looking for the real ECC install in WSL to answer this properly: `~/projects/ai/claude/everything-claude-code/ecc2` turned out to be an *unrelated* Rust project (its own session/comms/tui/worktree/observability modules — coincidental naming, not affaan-m/ECC), and a direct check of `~/.claude/plugins/marketplaces/everything-claude-code` came back empty on one pass and populated on another — genuinely inconsistent, not confirmed either way. `~/tools/ecc-setup.sh` exists and *targets* enabling `everything-claude-code@everything-claude-code` as a project-scoped plugin for Portfolio specifically, but there's no evidence it was ever actually run. **Correct status: undecided, not installed** — see [[Immediate Action]]. Until ECC is actually cloned and run for real, it can't be credited with solving agent-framework coordination; right now Claude Code's native subagent/Task tooling is the only coordination mechanism actually in use, same conclusion as [[00_Execution#Github|00_Execution]] reached independently.

---

## Security & Auditing

- **bumblebee** (Perplexity) — Scan installed packages/extensions for supply-chain compromises before adding MCPs.
- **keyhacks** — Verify leaked API keys; audit repos for accidentally-committed credentials.
- **cai** (aliasrobotics) — Run on portfolio's auth/API for security testing and documentation.
- **promptfoo** (red team mode) — Test portfolio AI Lab for jailbreak vulnerabilities before recruiter reaches it.

### Research finding (2026-07-29): is bumblebee enough?
**No — correctly identified as a thin layer.** Bumblebee is a one-time, read-only, on-disk scanner (checks installed packages/extensions against a known-compromise database) — it does exactly that one job well, but it's a point-in-time check, not continuous monitoring, and it doesn't touch npm-specific behavioral threats (typosquatting, compromised-maintainer takeovers) the way a dedicated supply-chain tool does. Checked against real 2026 incidents (Socket.dev's own blog: the Nx npm compromise and the TrapDoor crypto-stealer campaign across npm/PyPI/Crates.io) — both were caught by **behavioral** analysis, which bumblebee doesn't do.
**Verdict:** keep bumblebee for its actual designed purpose (run once before adding any new MCP/package, per the existing plan) — it's free and does that job fine. But it is not sufficient as the whole security layer, especially for **Portfolio**, which is exactly Socket's strongest use case (npm/Next.js-heavy). Add continuous supply-chain monitoring on top:
- **Socket.dev** — free tier for open-source projects, paid Pro per-contributor; the stronger choice if a small ongoing cost is fine, given Portfolio's real npm dependency surface.
- **OSV-Scanner** (Google) — the free, vendor-neutral equivalent if avoiding a paid tool matters more than Socket's extra behavioral-detection depth; CVE-based rather than behavioral, but zero cost and no vendor lock-in.
**Action:** wire one of these two into Portfolio's CI (GitHub Actions) as the actual continuous layer; bumblebee stays as the pre-install spot-check, not the whole answer. Not yet done — this is a decision, not an install, this session.

---

## Learning Curriculum (Next Month)
- **DataTalksClub zoomcamps** — data-engineering-zoomcamp (BOOM Kafka/MongoDB), mlops-zoomcamp (trading deployment), llm-zoomcamp (Jarvis eval framework), ai-dev-tools-zoomcamp (Claude/MCP structured path).
- **applied-ml** (Eugene Yan) — Production ML baselines from Google/Spotify/Netflix; use before implementing Jarvis semantic index or portfolio AI Lab.
- **system-design-primer** — Map BOOM to "distributed message queue" + "search with ranking" patterns for interview language.
- **coding-interview-university** — Checklist; align with coursework, not all-or-nothing.
- **tech-interview-handbook** — System design: use BOOM as your distributed systems answer.

---

## Install Order (This Session)

1. **Security first:** bumblebee
2. **VS Code foundation:** ECC, mattpocock-skills, cpr-compress-preserve-resume, context-sync
3. **Reading/setup:** get-shit-done templates, claude-code-best-practice, system-prompts
4. **Scanning/setup:** claude-code-templates (`npx aitmpl`), whichllm, spec-kit
5. **Reference tabs open:** TradingAgents, PageIndex, semantic-search-nextjs, obsidian-mind

---

## Major Decisions to Make

1. **Memory architecture:** memsearch (Milvus + full session search) or context-sync (SQLite + fast recall) or both?
2. **Code search for BOOM:** Adopt claude-context (semantic search) or rely on existing Glob/Grep?
3. **Portfolio backend:** Pocketbase (free, self-hosted) vs. existing Sanity setup?
4. **Agent coordination:** beads (BOOM), goose (autonomous tasks), or multica (parallel agents)?
5. **Portfolio AI Lab template:** Adapt semantic-search-nextjs or build custom?

---

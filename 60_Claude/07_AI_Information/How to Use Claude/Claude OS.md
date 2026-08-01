---
type: dashboard
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - claude-os
  - ai-infrastructure
  - dashboard
notes:
  - "[[Jarvis OS — North Star]]"
  - "[[AI_CONTEXT]]"
next: "Act on the High rows of the marketplace evaluation; adopt /emerge and /challenge from second-brain-claudekit"
---
# Claude OS — Agentic Setup Registry

All skills, agents, hooks, and MCP servers across every project. Source material lives in `20_Progress/AI/`. This note is the strategy/registry layer; the operational queryable view is [[20_Progress/AI/Claude OS Dashboard|Claude OS Dashboard]], and the visual layer blueprint is [[10_Areas/Excalidraw/Claude OS Map]]. Per-platform operating guides: [[10_Areas/AI/Claude Code|Claude Code]] · [[10_Areas/AI/Cursor|Cursor]] · [[10_Areas/AI/Kiro|Kiro]] · [[10_Areas/AI/Codex|Codex]].

---

## Jarvis (this vault)

**Path:** `D:\Users\_Anant\10_Areas\Documents\Jarvis\.claude\`

### Agents (5 — all with name/description/tools/model frontmatter as of 2026-07-03)

| Agent | Trigger | Tools beyond Read/Glob/Grep/Edit/Write |
|-------|---------|-----------------------------------------|
| research-distiller | Deep ingestion: PDFs, web, transcripts, GitHub repos | Bash, WebFetch |
| anti-slop-editor | De-slopping any note per HUMAN_WRITING | — |
| vault-curator | Vault-wide health: links, duplicates, frontmatter, Write Contract | — |
| learning-agent | Overdue drills, enrichment, spaced repetition | — |
| career-operator | Internship/resume/portfolio/mentorship briefs | — |

### Skills / Commands (14)

| Command | Shape | Notes |
|---------|-------|-------|
| /startday | directory (SKILL.md + reference.md) | patches dashboard focus fields (Step 3b) |
| /closeday | directory (SKILL.md + reference.md) | writes lc_count/study_today/wins_done/habits_done, resets dashboard |
| /ingest-clipping | directory (+ examples.md + scripts/extract_pdf.py) | the gold-standard skill shape |
| /distill-note, /remove-ai-slop, /context, /trace-topic, /connect-notes, /weekly-review, /lint-claude-layer, /ops, /organize-csci2033, /tag-month, mcp-hub | flat .md | convert most-used first per North Star 5.1 |

### Hooks

| Hook | Event | Script |
|------|-------|--------|
| jarvis-session-continuity | SessionStart + SessionEnd | `30_Order/System/claude-workflow/hooks/jarvis-session-continuity.ps1` |
| jarvis-write-guard | PreToolUse (Write\|Edit\|MultiEdit) | `30_Order/System/claude-workflow/hooks/jarvis-write-guard.ps1` |

### MCP Servers

| Server | Command | Purpose |
|--------|---------|---------|
| obsidian | `uvx mcp-obsidian` | Read/write vault via Obsidian REST API |
| filesystem | `npx @modelcontextprotocol/server-filesystem` | Direct vault file access |
| git | `uvx mcp-server-git` | Git operations on vault |
| fetch | `uvx mcp-server-fetch` | Web fetch |
| jarvis-memory | `python server.py` | Vault registry + keyword search — ✅ verified 2026-07-03: server connects, `jarvis_reindex` built the index (8,124 notes), `jarvis_status` and `jarvis_search` return correct results. Semantic search still TODO (schema has `chunks`/`embeddings` tables, unpopulated). |

---

## CausalOps

**Path:** `20_Progress/AI/Claude Code/CausalOps/`
**Repo:** [gupta-builds/CausalOps](https://github.com/gupta-builds/CausalOps)

### Agents

| Agent | Purpose |
|-------|---------|
| causal-safeguard-reviewer | Reviews causal claims for safety / validity |
| coordinator-expert | Multi-agent coordination |
| memory-layer-specialist | Memory layer implementation |

### Commands

| Command | Purpose |
|---------|---------|
| lint | Code lint |
| memory-test | Memory layer testing |
| smoke | Smoke tests |
| unit-test | Unit tests |

---

## Windows Home `.claude`

**Path:** `20_Progress/AI/Claude Code/Windows Home/`
**What:** Global home directory `.claude` with all installed plugins/marketplaces

### Installed Skill Marketplaces

| Marketplace | Skills count | Location |
|-------------|-------------|---------|
| claude-plugins-official | 7 | `Windows Home/plugins/marketplaces/claude-plugins-official/plugins/` |
| addy-agent-skills | multiple | `Windows Home/plugins/marketplaces/addy-agent-skills/` |
| everything-claude-code | ~240 | `WSL Home/plugins/marketplaces/everything-claude-code/skills/` (not Windows Home — corrected 2026-07-03) |

### Firecrawl Skills (active in Windows Home)

```dataview
TABLE file.mtime AS "Updated"
FROM "20_Progress/AI/Claude Code/Windows Home/skills"
WHERE contains(file.name, "firecrawl")
SORT file.name ASC
```

---

## second-brain-claudekit — overlap vs gap (fetched from gupta-builds/second-brain-claudekit, 2026-07-03)

The kit ships 11 vault-specific + 10 global commands, 3 agents, 2 hooks, and the CPR (Compress → Preserve → Resume) session pattern.

| claudekit command | Jarvis equivalent | Verdict |
|-------------------|-------------------|---------|
| /context | /context | Overlap — Jarvis version reads the richer manifest |
| /today | /startday | Overlap — Jarvis version is stronger (plans + history + dashboard patch) |
| /closeday | /closeday | Overlap — Jarvis adds metrics frontmatter + dashboard reset |
| /trace | /trace-topic | Overlap |
| /graduate | /distill-note + promotion flow | Overlap (promotion lives in AGENTS.md routing) |
| /drift | /ops + vault-curator | Overlap |
| /review (global) | /weekly-review | Overlap |
| /connect (global) | /connect-notes | Overlap |
| /research (global) | research-distiller agent | Overlap |
| /summarize, /inbox-process, /capture (global) | /ingest-clipping + 00_Inbox flow | Overlap |
| **/emerge** | none | **Gap** — surface latent patterns from recent notes; nothing in Jarvis does cross-note pattern surfacing |
| **/challenge** | none | **Gap** — steelman/stress-test an idea; would pair well with brainstorm-type notes |
| **/ghost** | none | **Gap** (low priority) — judgment-free free-writing mode |
| **/ideas**, /brainstorm (global) | none | **Gap** (low priority) — timed ideation sprints saving atomic notes |
| **/schedule** | none | **Gap** — builds a schedule from Tasks across the vault; /startday covers the daily case, nothing covers multi-day |
| /preserve + /compress + /resume (CPR) | session log + SessionStart hook | Partial — Jarvis logs sessions but has no /resume that reloads the last log deliberately, and no /preserve that promotes a session rule into CLAUDE.md |

Agents (vault-curator, research-distiller, weekly-reviewer) and hooks (after-edit-log, session-wrapup) are already covered by Jarvis equivalents or superseded by the write guard + continuity hook.

**Adopt next:** /emerge and /challenge (genuinely new capabilities), then a /preserve-style rule-promotion step in the session-end protocol.

---

## everything-claude-code Marketplace — relevance triage

**Path (corrected):** `20_Progress/AI/Claude Code/WSL Home/plugins/marketplaces/everything-claude-code/skills/` — ~240 skills installed, near-zero adopted.

### High — adopt or trial deliberately

| Skill | Why |
|-------|-----|
| agentic-os | Maps an entire .claude setup — directly feeds this registry and the dashboard |
| agent-architecture-audit | Audits agent rosters for gaps/overlap — run it against the 5 Jarvis agents |
| mcp-server-patterns | Patterns for growing jarvis-memory (semantic search is the next build) |
| deep-research | Structured research complement to research-distiller |
| context-budget / token-budget-advisor | Direct support for North Star Part 6 token economics |
| continuous-learning / continuous-learning-v2 | Same loop the learning-agent runs — mine for drill mechanics |
| knowledge-ops | Knowledge-base operations — closest to vault-curator's lane |
| verification-loop | Red-green verification for writing skills (North Star 5.1 checklist rule) |

### Medium — useful for specific projects, not the vault

| Skill | Where |
|-------|-------|
| tdd-workflow, python-testing, python-patterns | jarvis-memory / jarvis-cli development |
| benchmark, eval-harness, agent-eval | CausalOps agent evaluation |
| mle-workflow, pytorch-patterns | CSCI 2033 ML work + Trading models |
| fastapi-patterns, postgres-patterns, docker-patterns | Resq/Assisto backends |
| security-review, security-scan | pre-deploy gates (Portfolio, Assisto) |
| github-ops, git-workflow | repo automation |
| prompt-optimizer, iterative-retrieval | prompt/RAG work in Trading + UROP |
| dashboard-builder | could inform 00_Dashboard iterations |
| article-writing, brand-voice | content output, filtered through HUMAN_WRITING |

### Low — ignore (bulk of the ~240)

Language/framework packs unrelated to the current stack (kotlin-*, swift-*, laravel-*, quarkus-*, springboot-*, dotnet-*, perl-*, angular-*, flutter-*…), domain verticals with no matching project (healthcare-*, homelab-*, logistics-*, customs-*, energy-*, carrier-*, defi-*, prediction-market-*…), and platform one-offs (blender-*, manim-video, remotion-*, ios-icon-gen, x-api…). Rule: a skill earns Enable only when a named project note needs it — width was the original disease (North Star Part 2).

---

## Cursor Setup

**Path:** `20_Progress/AI/Cursor/`

### Rules (`.cursor/rules/`)

| File | Scope | Purpose |
|------|-------|---------|
| workspace-context.mdc | alwaysApply | Vault routing, folder structure, write contract |
| human-writing.mdc | alwaysApply | Voice standard, anti-slop rules |
| vault-behavior.mdc | alwaysApply | Pre-flight, frontmatter schema, placement, quality gate |
| note-creation.mdc | `**/*.md` | Per-note formatting, plugin integration |
| plugin-rules.mdc | alwaysApply | When to use each plugin |

---

## Kiro Setup

**Path:** `20_Progress/AI/Kiro/`
**Steering files:** `.kiro/steering/workspace-context.md`

---

## Codex Setup

**Path:** `20_Progress/AI/Codex/`

---

## What Needs Work

```dataview
TABLE notes, next
FROM "60_Claude/07_AI_Information"
WHERE contains(tags, "claude-os") AND status != "tree"
SORT file.mtime DESC
```

### Known gaps

- [x] jarvis-memory MCP: verified 2026-07-03 — server runs, index built (8,124 notes), all 3 tools respond
- [ ] Jarvis skills: 11 commands still single `.md` files (startday/closeday/ingesting-clipping converted) — convert most-used next
- [x] Jarvis agents: all 5 have proper frontmatter (name, description, tools, model) as of 2026-07-03
- [x] Claude OS map blueprint: [[10_Areas/Excalidraw/Claude OS Map]] (text blueprint; hand-drawn Excalidraw still optional)
- [x] second-brain-claudekit: overlap/gap table above — adopt /emerge, /challenge, /preserve-style rule promotion
- [ ] Portfolio + SafeReach `.claude` setups: Portfolio dump folder is empty, SafeReach has no Claude Code dump — re-export both
- [x] everything-claude-code: triaged High/Medium/Low above — act on the High rows
- [ ] jarvis-memory semantic search: `chunks`/`embeddings` tables exist but are unpopulated — the next real build (North Star 5.4)

---
type: project
status: active
created: 2026-05-29
updated: 2026-05-29
tags:
  - audit
  - jarvis
  - mcp-hub
  - roadmap
  - 3-month-plan
notes:
  - "[[Jarvis]]"
  - "[[CLAUDE.md]]"
  - "[[AGENTS]]"
  - "[[HUMAN_WRITING]]"
  - "[[AI_CONTEXT]]"
  - "[[00_Dashboard]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/Obsidian/Claude Pro Workflow]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
  - "[[60_Claude/40_Project_Briefs/Claude Optimization Master Setup]]"
  - "[[60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis — 2026-W22]]"
horizon: 2026-09-01
next: Create conversation capture folders, then patch AGENTS.md and CLAUDE.md per Phase 4.
---

# Vault Audit — 2026-05-29

> **If you're reading this in a new session, read this first.**
>
> This audit is the orientation pack for any future Claude session working on the Jarvis vault meta-system. Read it before touching anything else.
>
> Phase order: (1) read the spine pack — `AGENTS.md`, `HUMAN_WRITING.md`, `60_Claude/7_AI_Information/AI_CONTEXT.md`, `00_Dashboard.md`, last 100 lines of `60_Claude/10_Session_Logs/log.md`, [[40_Resources/Obsidian/Vault Operating System]], [[40_Resources/Obsidian/Claude Pro Workflow]]. (2) read this audit. (3) read [[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan|the Master Plan]] and [[60_Claude/40_Project_Briefs/Claude Optimization Master Setup|the Claude Optimization brief]] for execution context. Then act.
>
> Anchor dates: Master Plan runs 2026-04-24 → 2026-07-17. This audit's horizon runs 2026-05-29 → 2026-09-01. The first month of this audit overlaps with Master Plan Month 2; the third month extends past the Master Plan and into hardening + integration.
>
> Verify before recommending: the master plan names files and CLI commands that may not exist yet (registry SQLite, `jarvis status`, embeddings, conversation capture folders). Check the filesystem, not the plan.

## Why this audit exists

Anant asked for a vault intelligence audit and a 3-month setup plan to September 1, 2026. The vault is to operate as (a) a PKM that drives real expertise via read→internalize→test→apply, (b) an MCP hub that any external agent (Claude Code, Cursor, Kiro, Codex, Cowork, ChatGPT, future agents) can read for context, and (c) a self-improving instruction system that future cold-start Claude sessions can pick up in five minutes.

The vault already has most of the structural pieces. The audit's job is to find the gaps between what the spine claims and what actually exists on disk, then prescribe the cheapest fix order.

---

## Spine Health

| File | Status | Diagnosis |
|------|--------|-----------|
| `CLAUDE.md` | Good | Skills table matches `.claude/skills/` 1:1 (12 skills). Agents table matches `.claude/agents/` 1:1 (4 agents). Folder roles correct. Frontmatter `status: sprout` is understated — this file is load-bearing for every Claude session and behaves like `tree`. Inline body uses `[[AI_CONTEXT]]` (resolves via Obsidian) and the path `AI_CONTEXT.md` (ambiguous to non-Obsidian tools — actual path is `60_Claude/7_AI_Information/AI_CONTEXT.md`). |
| `AGENTS.md` | Good with gaps | Solid folder roles, working rules, retrieval rules, safety. Missing: explicit per-agent invocation pointers (currently delegates to `.claude/agents/`, fine for Claude Code, opaque to other agents). Missing: folder roles for `60_Claude/45_Outputs/` and `60_Claude/7_AI_Information/`, both active in vault. |
| `HUMAN_WRITING.md` | Excellent | Single source of truth, concrete contrasts, named anti-patterns. Do not change. |
| `60_Claude/7_AI_Information/AI_CONTEXT.md` | Good | Manifest layout correct: shared sources, live state, domain entry points, continuity protocol, tool-specific notes. The "Canonical Shared Sources" list does not include `CLAUDE.md` — minor inconsistency given CLAUDE.md is treated as canonical everywhere else. |
| `00_Dashboard.md` | Good | Status `tree`, last updated 2026-05-26. Dataview queries for active projects, AI staging, raw clippings, classes, recent outputs, tasks, flashcards, orphans, metadata cleanup, recent reviews — comprehensive. Capability Engine block is wired to Field OS boards. |
| `60_Claude/10_Session_Logs/log.md` | Healthy | 26+ entries from 2026-04-08 to 2026-05-29. Has one duplicate 2026-05-28 entry (Claude Optimization Master Setup section appears twice, near-identical). Recent activity dominated by ingestion + audit work, not the Master Plan build spine. |
| `40_Resources/Obsidian/Vault Operating System.md` | Excellent | Status `tree`. Full property schema including the Capability Engine extension. Enrichment rules explicit. |
| `40_Resources/Obsidian/Claude Pro Workflow.md` | Good | Status `sprout`, created 2026-05-26. Strong on surface roles (Code/Desktop/mobile), MCP rules, rate-limit discipline, verification checklist. This is the operating contract for Claude Pro usage and should be the first file every Claude session reads after `AGENTS.md`. |

**Verdict:** the spine is structurally sound. The single load-bearing issue is the `AI_CONTEXT.md` path ambiguity for tools that interpret references as filesystem paths, not Obsidian wikilinks (Cursor, Kiro, Codex). Fix in Phase 4 by normalizing all references to the full path `60_Claude/7_AI_Information/AI_CONTEXT.md`.

---

## Instruction Files — What Exists

### `.claude/skills/` (12 files)

| File | Purpose | Quality (1-5) | Key Gap | Action Needed |
|------|---------|---------------|---------|---------------|
| `ops.md` | Daily ops dispatcher (`morning-start`, `health-check`, `triage`, etc.) | 5 | Depends on `jarvis-cli` whose runtime status is unverified in recent logs. Long (742 lines) — at the edge of legibility for cold-start Claude. | Verify CLI commands still work. No edit needed. |
| `weekly-review.md` | Plan-aware weekly review with milestone audit | 5 | None. Already enriched with pre-flight reads, milestone tables, cold-start orientation. Reference model for other skills. | None. |
| `remove-ai-slop.md` | Rewrite AI-sounding prose into human writing | 4 | None major. Reads HUMAN_WRITING + AGENTS + Vault Operating System before editing. | None. |
| `ingest-clipping.md` | Convert raw clip into source summary + entity/concept stubs | 4 | Does not route to `60_Claude/05_Clippings/AI Conversations/` for conversation imports (folder doesn't exist yet). Does not handle GitHub repo clippings (which is what recent ingestions actually were). | Add conversation + repo subroutes after folders exist. |
| `organize-csci2033.md` | Merge CSCI 2033 linear algebra notes | 4 | Folder path uses `50_Archive/Previous Classes/CSCI 2033/` — verify still exists. Course-specific, lower priority. | Verify path; otherwise none. |
| `distill-note.md` | Convert messy capture into evergreen note | 3 | Generic distillation template. No integration with the Capability Engine fields (`track`, `mastery_level`, `enrichment_status`) or the Jarvis Enrichment Template at `30_Order/Templates/Capability/Jarvis Enrichment Template.md`. | Add Capability Engine field hooks. |
| `context.md` | Summarize current vault state | 3 | Does not read the Capability Dashboard, Field OS boards, or enrichment queue. The Three-Month Master Plan defines a richer context-pack format — this skill is the older, thinner version. | Patch to read Capability Engine surfaces and accept `--mode {live,project,topic,agent}` like the planned `jarvis context-pack`. |
| `today.md` | Build today's plan | 3 | No drill-queue integration (Capability Engine has `next_drill` field). No reference to the three-month plan's current phase. | Add drill queue + master plan phase awareness. |
| `trace-topic.md` | Map a topic across the vault | 3 | Generic. Doesn't call semantic search (which doesn't exist yet) or graph queries. | Stub the semantic + graph hooks now; activate when Master Plan Month 2 deliverables land. |
| `connect-notes.md` | Suggest backlinks between notes | 3 | Generic. No use of frontmatter `notes:` field as primary surface. No integration with the Capability Engine `prerequisites` / `used_in` / `evidence` fields. | Patch to leverage Capability Engine relationship fields. |
| `closeday.md` | End-of-day summary | 3 | Doesn't run the Capability Audit (the `/ops evening-close` does, but `/closeday` alone doesn't). Creates `60_Claude/50_Reviews/Closeday - YYYY-MM-DD.md` independent of the Weekly Synthesis chain. | Add capability audit summary section; cross-link the day's morning briefing. |
| `lint-claude-layer.md` | Health check `60_Claude/` | 3 | Generic. No reference to the Vault Health Dashboard which already surfaces most of this via Dataview. Risk of redundancy. | Patch to consume Vault Health Dashboard counts; only flag what dashboards miss. |

### `.claude/agents/` (4 files)

| File | Purpose | Quality (1-5) | Key Gap | Action Needed |
|------|---------|---------------|---------|---------------|
| `research-distiller.md` | Deep distillation of source material | 4 | Strong file. Reads AI_CONTEXT + HUMAN_WRITING + Vault Operating System. Output template covers exec summary, claims, quotes, entities, concepts, contradictions, actions. | None. |
| `vault-curator.md` | Vault-wide lint and structure | 4 | Reads latest Ops Report before scanning to avoid duplicating daily ops work. Includes Capability Engine maintenance section. | None. |
| `anti-slop-editor.md` | Rewrite slop-heavy prose | 4 | Minimal but focused. Reads HUMAN_WRITING. | None. |
| `career-operator.md` | Career, internship, portfolio, mentorship work | 3 | Reads AI_CONTEXT + HUMAN_WRITING + 00_Dashboard. Generic action item lists. No integration with Capability Engine `evidence` field or the 9 output notes already in `60_Claude/45_Outputs/`. | Patch to pull from outputs layer when generating resume bullets. |

### `.claude/rules/` and `.claude/context/`

| File | Purpose | Quality (1-5) | Key Gap | Action Needed |
|------|---------|---------------|---------|---------------|
| `rules/human-writing.md` | Steering wrapper around HUMAN_WRITING | 4 | Minimal pointer file with Kiro-style frontmatter. Correct. | None. |
| `context/workspace-context.md` | Cross-tool steering wrapper | 4 | Uses `#[[file:AI_CONTEXT.md]]` syntax pointing at vault root, but actual file is at `60_Claude/7_AI_Information/AI_CONTEXT.md`. | Fix path to full location. |

### `30_Order/Templates/` (33 templates)

Templates exist for: Classes (Class Board, Concept, Discussion, Exam Sheet, Homework, Lab, Project, Textbook, Week), Capability (Field OS, Jarvis Enrichment, Clipping Distill, Deep Dive, Depth Ladder, Output, Question Bank, Synthesis, Weekly Synthesis), Metadata (For Brainstorm, Classes, Evergreen, Everything, Inputs, Progress, Thoughts), Headway (Better Today/Week/Month/Year), MOC. Coverage is comprehensive. Not audited individually — no evidence they are stale or broken.

---

## Plan Files Found

| File | Status | Diagnosis |
|------|--------|-----------|
| `20_Progress/Projects/Jarvis.md` | Active | Project hub. `next:` points at Master Plan Week 1 deliverables — overdue by 4+ weeks. Updated 2026-04-24. |
| `60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan.md` | Active (overdue) | The canonical 3-month roadmap, 2026-04-24 → 2026-07-17. Per W22 review: ~30% complete. Week 1 (registry hardening) and Week 2 (conversation capture spine) deliverables missing. Now in calendar Week 5 (Month 2 start). |
| `60_Claude/40_Project_Briefs/Jarvis Multi-Agent PKM Plan.md` | Sprout (superseded) | Earlier multi-agent design (2026-04-24). The conversation registry schema, context pack design, and promotion manifest from this note were folded into the Master Plan. Status should likely be `archived` or `complete` with a note pointing at the Master Plan. |
| `60_Claude/40_Project_Briefs/Claude Optimization Master Setup.md` | Active | 2026-05-28 audit + action list. Concrete next actions still pending: install mattpocock/skills, create AI Conversations folders, set up Sunday 7 PM weekly review. |
| `60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis — 2026-W22.md` | Reference | W22 review surfaced: spine ~30% complete, capture folders missing, 223-note enrichment queue idle, AI Workflow.md + MCPs.md outdated, duplicate log entry. Still all true 7 days later. |
| `10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/CSCI 2041 Note Production Plan.md` | Course-specific | Source-grounded note production contract for CSCI 2041. Out of scope for vault-meta-system work. |

**Orphan plan files:** none found beyond the above. No competing roadmap that contradicts the Master Plan.

---

## Conflicts & Contradictions

1. **`AI_CONTEXT.md` path is ambiguous.** Used as `[[AI_CONTEXT]]` (Obsidian wikilink, resolves correctly) and as `AI_CONTEXT.md` (path-style, looks for vault root — file does not exist there). Tools that parse paths as filesystem paths will fail. Affected files: `CLAUDE.md` body, `.claude/context/workspace-context.md`, frontmatter `notes:` in multiple project briefs. Fix: standardize all path-style references to `60_Claude/7_AI_Information/AI_CONTEXT.md`.

2. **Master Plan timeline vs. actual progress.** Master Plan says "Month 1 ends ~May 22 with conversation capture spine working." On 2026-05-29, the two capture folders still do not exist. The plan and reality diverge by one full month. Either reset the plan dates or compress Month 1 into Weeks 5–6.

3. **CLAUDE.md skills/agents tables vs. actual filesystem.** Match exactly (12 skills, 4 agents). No conflict here — note this as confirmation, not a bug.

4. **AGENTS.md folder roles miss two active folders.** `60_Claude/45_Outputs/` and `60_Claude/7_AI_Information/` exist and contain working material. Neither appears in the AGENTS.md folder role table. Result: agents don't know how to treat them.

5. **`Jarvis Multi-Agent PKM Plan` and `Jarvis Three-Month Research Engine Master Plan` overlap.** Both are status-active, both describe a conversation registry + context pack builder + promotion manifest. The Master Plan supersedes. Status conflict.

6. **`AI Workflow.md` and `MCPs.md` predate the current setup.** Created March 2026, written before Claude Pro became primary. Still indexed as active reference notes — agents reading `40_Resources/CS/AI/` get outdated guidance. Both should either be archived or rewritten with a "superseded by Claude Pro Workflow + Claude Optimization Master Setup" banner.

7. **Duplicate session log entry on 2026-05-28.** Two near-identical "audit | Claude Optimization Master Setup" entries. Cosmetic but breaks any future Dataview query that counts sessions per day.

8. **`/closeday` skill creates Closeday notes, `/ops evening-close` appends to the same Closeday note.** Composition is intentional but undocumented — a Claude reading only `/closeday.md` will not know about the evening-close append behavior. Cross-reference in both files.

---

## Missing Files (Critical)

These don't exist yet and the vault is acting as if they do:

1. **`60_Claude/05_Clippings/AI Conversations/`** — conversation raw archive. Master Plan Week 2 deliverable. Five weeks overdue. Blocks the entire conversation memory workstream.

2. **`60_Claude/30_Source_Summaries/AI Conversations/`** — distilled conversation summaries. Same status as above.

3. **`.claude/agents/learning-agent.md`** — read→test→apply learning loop agent. Should be able to: pick a concept from a Field OS, generate drill questions from the note's content, grade answers, update `mastery_score` and `next_drill` with user approval, suggest the next note to drill or enrich. Not yet built.

4. **`.claude/skills/mcp-hub.md`** — skill that defines which files to send to which external tool as context, and how to keep those files current. Should also expose `mcp-hub list-tools`, `mcp-hub context-pack <tool>`, `mcp-hub sync` operations.

5. **`40_Resources/Obsidian/MCP-Hub-Index.md`** — single-page orientation note any new agent reads first. Should cover vault folder roles in one table, active project list with one-liners, naming conventions, where to find the canonical plan, what NOT to touch.

6. **`30_Order/System/jarvis-memory/`** — registry tooling folder referenced by Master Plan Week 1. Not yet created. No `registry.sqlite`, no `conversations.jsonl`, no schema file.

7. **Conversation registry schema file** — should live at `30_Order/System/jarvis-memory/schemas/conversation.json`. Master Plan documents the shape; no file commits the contract.

8. **Benchmark question set** — Master Plan calls for 75 questions across 5 categories. None captured yet.

9. **CONTEXT.md files in active project repos** — Claude Optimization brief flags this as a high-leverage missing file for repos (IssueDesk, OpsPilot, BOOM work). Not a vault file but a vault-policy gap.

---

## 3-Month Roadmap to September 1

The roadmap is structured around the user's three stated goals: PKM that builds expertise, MCP hub for external agents, self-improving instruction system. Each month has a single focus. Estimated effort assumes Claude-pair sessions of 1–2 hours, not solo coding hours.

### Month 1 — Foundation and MCP Hub (2026-05-29 → 2026-06-26)

The cheapest, highest-leverage work. Builds the missing instruction layer and unblocks Month 2.

| Item | Why it matters | Effort |
|------|----------------|--------|
| Create `60_Claude/05_Clippings/AI Conversations/` and `60_Claude/30_Source_Summaries/AI Conversations/` | Unblocks Master Plan Week 2. Five weeks overdue. Zero code required. | 5 min |
| Patch `AGENTS.md` to include `60_Claude/45_Outputs/` and `60_Claude/7_AI_Information/` in folder roles | Agents currently have no rules for two active folders | 15 min |
| Patch `CLAUDE.md` to standardize the `AI_CONTEXT.md` reference to full path | Non-Obsidian tools fail on the wikilink form | 10 min |
| Fix `.claude/context/workspace-context.md` to point at `60_Claude/7_AI_Information/AI_CONTEXT.md` | Same path bug as above, separate file | 5 min |
| Create `.claude/skills/mcp-hub.md` (new skill) | Defines context-pack-per-tool. Replaces ad-hoc prompts in `Claude Pro Workflow.md`. | 1.5 hr |
| Create `40_Resources/Obsidian/MCP-Hub-Index.md` (new note) | Single-page orientation for any external agent. The "read me first" file. | 1 hr |
| Create `.claude/agents/learning-agent.md` (new agent) | Drives the read→drill→update cycle. Activates the 223-note enrichment queue and the Capability Engine drill schedule. | 1.5 hr |
| Archive or banner `40_Resources/CS/AI/AI Workflow.md` and `40_Resources/CS/AI/MCPs.md` | Both are outdated and misleading | 20 min |
| Resolve `Jarvis Multi-Agent PKM Plan.md` status (mark superseded by Master Plan) | Cleans plan-file inventory | 5 min |
| Clean duplicate 2026-05-28 session log entries | Cosmetic but blocks Dataview counts | 5 min |
| Install `mattpocock/skills` in one active repo and add CONTEXT.md | Tested workflow from Claude Optimization brief, still pending | 30 min |
| Enrich 25 notes from the queue (5/week × 5 weeks of catch-up, compressed) | The queue has been idle since 2026-04-27 | 5 hr |

**Month 1 deliverable:** the MCP hub is real, the instruction layer is consistent, and the conversation capture spine exists.

### Month 2 — Brain (2026-06-26 → 2026-07-24)

This aligns with Master Plan Month 2. The audit's role here is to keep the build honest: prefer thin, working slices over heavy infrastructure.

| Item | Why it matters | Effort |
|------|----------------|--------|
| Build `jarvis-memory/registry.sqlite` with notes/headings/chunks/conversations tables | Foundation for retrieval and conversation memory | 3 hr |
| Add `jarvis status` command | Self-reflection: file count, indexed count, queue size, stale projects | 1 hr |
| Build chunk index over approved folders (40_Resources, 20_Progress, 60_Claude/20+30+40+45) | Required for semantic search | 3 hr |
| Build local embeddings via Ollama (`embeddinggemma`) | Cheap, local-first, no cloud dependency | 2 hr |
| Add `jarvis semantic-search` command + 30-query benchmark | Per Master Plan Week 5 | 3 hr |
| Build conversation import command + first 2 adapters (Claude Code, ChatGPT export) | Per Master Plan Week 2 (rescheduled) | 4 hr |
| Distill 5 conversations as proof of pipeline | First real use of the conversation spine | 1.5 hr |
| Run weekly review every Sunday | Already automated via Cowork scheduled task | 30 min/wk |

**Month 2 deliverable:** the registry, semantic search, and conversation capture all work end-to-end on a small corpus.

### Month 3 — Research Engine and Learning Loop (2026-07-24 → 2026-09-01)

The 6-week stretch goal: turn Jarvis from a memory layer into an answering and teaching system. This phase extends past the Master Plan's July 17 finish.

| Item | Why it matters | Effort |
|------|----------------|--------|
| Build `jarvis ask` v1 with citation contract | The first answer engine. Every answer must cite notes, declare confidence, and admit gaps. | 5 hr |
| Build 75-question benchmark, run weekly, track pass rate | Prevents Jarvis from becoming vibes | 4 hr |
| Build knowledge graph v1 (links, prerequisites, evidence edges) | Required for `prerequisites`, `evidence`, `gaps` queries | 4 hr |
| Wire learning-agent into the drill loop: ask Jarvis → grade → update mastery | Activates the read→test→apply spine | 3 hr |
| Build `jarvis research <topic>` brief generator | Used for picking the next AI/ML deep dive | 3 hr |
| Build validation layer: confidence labels (`vault-grounded`, `inferred`, `uncertain`, `missing`) | Required by the Master Plan's truthfulness rule | 2 hr |
| Generate 3 research briefs to test the pipeline | First real Jarvis-as-research-engine use | 2 hr |
| Final demo: import a conversation → answer a question → identify gap → enrich note → generate path → log everything | Master Plan Week 12 demo, ported to Sept 1 horizon | 3 hr |
| Final audit and roadmap to Month 4–6 | Sets up the post-Sept-1 direction | 2 hr |

**Month 3 deliverable:** Jarvis can answer questions from the vault with citations, teach concepts, generate research briefs, and admit what it does not know. The full read→test→apply loop runs end-to-end on at least one Field OS track.

**Month 1 priorities (highest leverage, lowest effort):**
1. Create the two AI Conversations folders.
2. Patch AGENTS.md and CLAUDE.md (paths + missing folder roles).
3. Build mcp-hub skill, MCP-Hub-Index note, learning-agent.

These three unblock the rest. Phase 4 of this audit executes the first two.

---

## MCP Hub Gap Analysis

External tools that talk to this vault, ranked by importance:

### Claude Code CLI

- **Context it needs:** project root context, current task, vault folder roles, writing rules, active project's `next:`.
- **File it should read first:** `CLAUDE.md` (already does, via Claude Code's memory hierarchy).
- **Status:** functional. CLAUDE.md is well-structured for Claude Code. Folder roles, frontmatter conventions, output destinations, skills/agents tables all present.
- **Gap:** none for normal use.

### Cursor

- **Context it needs:** codebase rules, file naming, what not to rewrite.
- **File it should read first:** `.cursor/rules/` files (Cursor convention).
- **Status:** `.cursor/rules/workspace-context.mdc` exists (mentioned in session log 2026-04-24) and points at AI_CONTEXT.
- **Gap:** the path inside the rule wrapper likely points at vault root `AI_CONTEXT.md`, not the actual location. Verify and fix during Phase 4.

### Kiro

- **Context it needs:** steering files + spec folder.
- **File it should read first:** `.kiro/steering/workspace-context.md`.
- **Status:** exists per session log 2026-04-24.
- **Gap:** same path issue likely. Verify.

### Codex

- **Context it needs:** `AGENTS.md` + project files.
- **File it should read first:** `AGENTS.md`.
- **Status:** AGENTS.md is comprehensive and Codex-compatible.
- **Gap:** none.

### Cowork (this session)

- **Context it needs:** project instructions + CLAUDE.md.
- **File it should read first:** project instructions auto-loaded; CLAUDE.md loaded at session start.
- **Status:** working — this audit was produced via Cowork.
- **Gap:** Cowork reads CLAUDE.md but not all the spine files automatically. Recommend a short orientation prompt at top of CLAUDE.md ("read these N files in order before responding") — partially exists, can be sharpened.

### ChatGPT / Claude web

- **Context it needs:** project knowledge upload + compressed summary.
- **File it should read first:** a small context pack, not the whole vault.
- **Status:** no context-pack builder exists yet.
- **Gap:** until `jarvis context-pack` is built (Master Plan Week 3), web tools require manual file selection. The `mcp-hub` skill in Phase 4 can produce one of these for ChatGPT/Claude web manually.

### Future external agents

- **Context they need:** a single canonical entry point that orients them in five minutes.
- **File they should read first:** does not exist yet. Should be `40_Resources/Obsidian/MCP-Hub-Index.md`.
- **Status:** missing.
- **Gap:** the critical missing file. Built in Phase 4.

### Obsidian Local REST API MCP server

- **Status:** active, used by this very audit (`mcp__jarvis__vault_read`, `mcp__jarvis__vault_list`, etc.).
- **Gap:** none functional. `.mcp.json` at vault root configures it. Configuration should not be touched.

---

## What this audit changed

Phase 4 of the original mission executes the highest-leverage fixes. Tracked separately in this audit's `next:` action and in the session log entry for 2026-05-29.

Key follow-ups for the next session:
- Verify Cursor/Kiro steering files actually point to the correct AI_CONTEXT path.
- Run `/ops health-check` to baseline vault health before Month 1 begins.
- Run the 2026-W23 weekly review (Cowork scheduled task is set for Mondays at 9 AM).
- Begin enrichment catch-up — pick 5 notes from the 223-candidate queue and drill them.

---

*Built by Claude (Cowork session) 2026-05-29. Replace timestamps and progress numbers when refreshing in future audits.*

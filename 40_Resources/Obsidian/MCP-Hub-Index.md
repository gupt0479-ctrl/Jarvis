---
type: evergreen
status: sprout
created: 2026-05-29
updated: 2026-05-29
tags:
  - evergreen
  - mcp-hub
  - orientation
  - agent-entry-point
notes:
  - "[[CLAUDE.md]]"
  - "[[AGENTS]]"
  - "[[HUMAN_WRITING]]"
  - "[[AI_CONTEXT]]"
  - "[[00_Dashboard]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/Obsidian/Claude Pro Workflow]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
  - "[[60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29]]"
---

# MCP Hub Index

**This is the orientation page for any external agent reading the Jarvis vault.** If you can read this file, you can become productive in five minutes. Read it before doing anything else.

## What This Vault Is

Jarvis is Anant Gupta's AI-powered second brain: a CS-student-and-future-engineer's PKM that doubles as the shared memory layer for every AI tool he uses. CS at University of Minnesota, learning agentic AI workflows, ML/AI pipelines, full-stack apps, automation, trading systems. Building toward genuine technical expertise and eventually running a multinational company.

The vault is an Obsidian vault with a Local REST API MCP server. Every AI tool (Claude Code, Cursor, Kiro, Codex, Cowork, ChatGPT/Claude web) reads vault content the same way: through the MCP server, through hardcoded file reads, or through tool-specific wrappers.

## Read These Files First (In Order)

1. `AGENTS.md` — vault-wide behavioral rules. Folder roles, working rules, retrieval rules, safety.
2. `CLAUDE.md` — vault operating contract. Skills, agents, output destinations.
3. `HUMAN_WRITING.md` — writing standard. **Non-negotiable.** Read before drafting any prose.
4. `60_Claude/7_AI_Information/AI_CONTEXT.md` — the cross-tool manifest. Tells you what's live and where to find it.
5. `00_Dashboard.md` — current control panel. Active projects, open tasks, Dataview queries.
6. The tail of `60_Claude/10_Session_Logs/log.md` — last 30 lines tell you what just happened.

For deeper context after the spine:
- `40_Resources/Obsidian/Vault Operating System.md` — full schema (frontmatter properties, folder logic, enrichment rules).
- `40_Resources/Obsidian/Claude Pro Workflow.md` — how Claude Pro surfaces (Code, Desktop, mobile) divide labor.
- `60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan.md` — the canonical 3-month build plan.
- `60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29.md` — current state diagnosis + roadmap to Sept 1, 2026.

## Folder Map (Compressed)

| Folder | What's In It | Agent Behavior |
|--------|--------------|----------------|
| `10_UMN/` | Active and previous coursework | Read for context. Don't restructure. Create distilled mirrors in `60_Claude/` instead. |
| `20_Progress/` | Active projects, career, mentorship, UROP/BOOM | Read for context. Update with user approval. Every project should have a `next:` action. |
| `30_Order/` | Templates and system structure | Read for conventions. Don't modify templates unless asked. |
| `40_Resources/` | Stable reference knowledge, system docs | Read for context. Add backlinks. Long-lived; respect `status: tree` notes. |
| `50_Archive/` | Past courses, completed work | Read-only. Historical reference. |
| `00_Inbox/` | Anant's quick capture | Read for context. Don't modify unless asked. |
| `60_Claude/00_Inbox/` | AI outputs awaiting review | Write here for pending AI work. |
| `60_Claude/05_Clippings/` | Raw source captures, imports | **Never modify.** Read as input only. |
| `60_Claude/10_Session_Logs/` | Append-only session continuity log | Append entries after meaningful work. |
| `60_Claude/20_Distilled_Notes/` | Durable AI-generated knowledge | Write durable concept notes here. |
| `60_Claude/30_Source_Summaries/` | Source-grounded summaries from clippings | Write source summaries here. |
| `60_Claude/40_Project_Briefs/` | Synthesized project plans + audits | Write project briefs here. |
| `60_Claude/45_Outputs/` | Proof artifacts: interview stories, portfolio bullets, reusable prompts | Write with `source_concepts:` provenance. |
| `60_Claude/50_Reviews/` | Daily / weekly / monthly reviews and ops reports | Daily and weekly reviews land here. |
| `60_Claude/60_Indexes/` | Dashboards, indexes, Field OS boards | Dataview-powered. Update when adding new note classes. |
| `60_Claude/7_AI_Information/` | Agent-facing operating docs + AI_CONTEXT manifest | The shared context layer for agents. |
| `.claude/skills/` | Claude Code skill definitions | Read to know what skills exist. Edit only to enrich or create new skills. |
| `.claude/agents/` | Claude Code subagent definitions | Read to know what agents exist. |
| `.claude/rules/` | Steering rules for Claude Code | Minimal pointers. |
| `.cursor/rules/` | Cursor steering | External-tool wrappers. |
| `.kiro/steering/` | Kiro steering | External-tool wrappers. |
| `.kiro/specs/` | Kiro spec folders | Planning artifacts. Not part of normal vault scans. |
| `30_Order/System/jarvis-cli/` | The Jarvis Ops CLI (`jarvis.ps1`, `jarvis_ops.py`) | Deterministic vault scans. CLI-first for baseline checks. |

## Active Projects (Snapshot)

The canonical list lives in `00_Dashboard.md` via Dataview. As of 2026-05-29:

- **Jarvis** (`20_Progress/Projects/Jarvis.md`) — the meta-system. Building this vault into a research engine. Master plan: `60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan.md`. Currently in Master Plan Month 2 (semantic search + ask engine), with Month 1 spine (registry, conversation capture) still incomplete.
- **UROP / BOOM** (`20_Progress/UROP/`) — systems engineering, Kafka/Redis pipelines, observability, Rust.
- **Mentorship Program** (`20_Progress/Mentorship Program/`) — active mentorship relationships and tracking.
- **Career / Internships** (`20_Progress/Internship/`, `20_Progress/Career/`) — application tracking, portfolio, resume.

When in doubt about a project's status, read its frontmatter `next:` field and most recent `updated:`.

## Naming Conventions

- Frontmatter `type` values: `evergreen`, `concept`, `input`, `project`, `thought`, `brainstorm`, `class`, `plan`, `review`, `dashboard`, `index`, `output`, `log`.
- Frontmatter `status` values: `seed` (idea), `sprout` (growing), `tree` (mature — don't modify without approval), `active`, `paused`, `complete`, `archived`.
- Dates are ISO format: `YYYY-MM-DD`.
- Internal references use `[[wikilinks]]`. Path-style references use full vault-root paths (not bare filenames — `AI_CONTEXT.md` is ambiguous; `60_Claude/7_AI_Information/AI_CONTEXT.md` is not).
- New notes use the convention in [[40_Resources/Obsidian/Vault Operating System]] including the Capability Engine extension fields for any concept tracked under a Field OS.

## What NOT to Touch

- `60_Claude/05_Clippings/` — raw source material. Read-only.
- `50_Archive/` — historical. Read-only unless archival cleanup is the task.
- `.obsidian/` — plugin config, settings. Off-limits.
- `.mcp.json` and `.claude/settings.local.json` — credential and config files. Don't read or write secrets to vault notes.
- Notes with `status: tree` — propose changes, wait for approval, then apply.

## How to Navigate

- **For project context:** start at `00_Dashboard.md` → click into the relevant project under `20_Progress/`.
- **For concept knowledge:** search `40_Resources/CS/` first, then `60_Claude/20_Distilled_Notes/`. Field OS boards under `60_Claude/60_Indexes/Field OS/` are the curated entry points by track (AI, Systems, Algorithms, Career, Trading).
- **For recent decisions:** read the tail of `60_Claude/10_Session_Logs/log.md`.
- **For raw sources:** browse `60_Claude/05_Clippings/`. For distilled versions: `60_Claude/30_Source_Summaries/`.
- **For active questions:** `60_Claude/60_Indexes/Question Dashboard.md`.
- **For overdue drills and enrichment candidates:** `60_Claude/60_Indexes/Capability Dashboard.md` and `Knowledge Enrichment Dashboard.md`.

## What This Vault Is Building Toward (Sept 1, 2026)

By September 1, 2026, the vault should be able to:

1. Capture every meaningful AI conversation into a distilled, searchable summary.
2. Answer questions about any concept in the vault with citations and uncertainty labels.
3. Drive a read → drill → apply learning loop using the Capability Engine fields.
4. Generate research briefs that pick the next AI/ML deep dive direction.
5. Serve as the MCP hub for every AI tool Anant uses — each tool reads only what it needs.

The roadmap to get there is in `60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29.md`.

## How to Be Helpful Here

- Read the spine before answering. Path-style references in files are vault-root-relative.
- Use wikilinks for internal references.
- Preserve frontmatter. Update `updated:` when notes change meaningfully.
- Patch under existing headings; do not rewrite whole files.
- Follow `HUMAN_WRITING.md`. Concrete mechanisms over vague praise. Compression over repetition.
- After meaningful work, append a one-paragraph entry to `60_Claude/10_Session_Logs/log.md`.
- When unsure, ask. When the task is clear, do it completely.

## Companion Files

- The `/mcp-hub` skill (`.claude/skills/mcp-hub.md`) operationalizes this index — it lists tools, builds context packs, and verifies wrappers don't drift.
- This file should be updated whenever folder roles change, new tools are added, or the spine evolves. Pair this file's `updated:` field with the `mcp-hub sync` operation.

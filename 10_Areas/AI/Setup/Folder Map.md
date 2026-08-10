---
type: index
status: sprout
created: 2026-08-09
updated: 2026-08-09
tags:
  - moc
  - ai
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
  - "[[20_Progress/AI/Claude OS Dashboard]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/AI/Claude Code/Management]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Log]]"
  - "[[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution]]"
  - "[[60_Claude/20_Distilled_Notes/Sources - Plan/GitHub Ingestion Implementation]]"
  - "[[60_Claude/05_Clippings/AI Conversations/README]]"
  - "[[60_Claude/07_AI_Information/AI Conversation - Summaries/README]]"
  - "[[60_Claude/30_Reviews/Weekly Synthesis/Weekly Synthesis Index]]"
  - "[[40_Resources/CS/AI/Token Optimization/Claude Pro Workflow]]"
  - "[[10_Areas/AI/Claude Code]]"
next: Decide whether 10_Areas/AI, 20_Progress/AI, and 20_Progress/Projects/AI Use stay three separate trees or get merged now that their jobs are written down here
---
# Folder Map
==Every AI-related folder in this vault does one of nine distinct jobs — sync infrastructure, per-tool registry, hub, ingestion pipeline, conversation capture, review, project briefs, source-of-truth resources, or this meta-map — and most of them are real, working infrastructure rather than aspirational scaffolding.==
## Purpose
This note answers one question: for any AI-related folder in Jarvis, what is it actually for, and which other folders does it depend on or duplicate? It exists because the AI tooling layer grew across three parallel top-level trees (`10_Areas/AI`, `20_Progress/AI`, `20_Progress/Projects/AI Use`) plus `60_Claude` and `40_Resources/CS/AI`, and nothing tied them together until this pass. Read this before creating any new AI-related folder or note — check whether the job already exists somewhere below.
## Map
### Claude Kit sync layer
`.claude/` at the vault root is Jarvis's own live Claude Code config (agents, commands, skills, hooks) — the thing actually executing when a skill runs in this repo. `20_Progress/AI/Claude Code/second-brain-claudekit/` is the vault-side mirror of a separate coding project (`second-brain-claudekit`, WSL) that builds and tests Claude Code tooling before it gets promoted anywhere else. That mirror is the one genuinely live-synced folder in the whole vault: a Unison script, triggered by a 15-minute Windows Scheduled Task, has run successfully roughly 280 times since 2026-07-30 per [[20_Progress/AI/Claude Code/second-brain-claudekit/Sync-Log|its Sync-Log]], including one real conflict that was skipped rather than silently overwritten. [[20_Progress/AI/Claude Code/Sync - Unison]] is the rollout plan for extending that same sync to the other eight tracked repos — it has verified real WSL paths and `.claude/` shapes for each, but nothing beyond second-brain-claudekit has been switched live; that requires a per-project go-ahead that has not been given yet. A stale, undocumented duplicate of second-brain-claudekit's own config sits at `second-brain-claudekit/Da Shit/` (frozen 2026-07-30) — no vault note references it, and the live sync bypassed it entirely; treat it as dead unless a future session revives the "Da Shit" naming decision on purpose. `.claude_windows/` and `.claude_wsl/` are raw mirrors of the real global `~/.claude` home directories (credentials, session history, plugin caches) — deliberately excluded from tracking and sync per [[20_Progress/AI/Claude Code/MOC]], because syncing them would turn a one-time credential leak into a continuous one.
### Per-tool operational registry
`20_Progress/AI/Claude Code/`, `20_Progress/AI/Codex/`, `20_Progress/AI/Cursor/`, and `20_Progress/AI/Kiro/` each hold one subfolder per real coding project, a snapshot of that project's actual tool config, and their own `MOC.md`. Only `second-brain-claudekit` (above) is live; the other eight Claude Code project folders, and everything under Codex/Cursor/Kiro, are frozen one-time exports from 2026-07-05 — real content, not placeholders, but static unless someone re-exports them. `20_Progress/AI/Claude OS Dashboard.md` is a health-check dashboard over this registry (MCP status, platform inventory, open actions) but it has drifted: it is over a month stale against today and its `.canvas` twin disagrees with the `.md` version on which project folders are populated. The excalidraw diagram that documents this registry visually is not stored here — see the meta-map section below.
### AI Use hub
`20_Progress/Projects/AI Use/` is meant to be the entry point for AI-tooling work in progress. `Cursor AI.md` and the `Gen AI/` course notes are real and current; `Jan.md` and `Ollama.md` mix one substantive section with unfinished template scaffolding; `The AI Hub.md`, despite its name, is an empty stub with no actual index content. `Builds & Resources/` holds five real distilled decision notes (LLM council skill install, a code-review/eval gap, a corrected Hermes agent framing, a Maverick-skills-to-repo mapping, a deferred model-distillation plan) — moved here from `20_Progress/AI/Builds & Resources/` this session, byte-identical, just not yet committed. `Claude Kit/` is the tool-qualification pipeline tracker for second-brain-claudekit's sandbox: [[20_Progress/Projects/AI Use/Claude Kit/Log|Log.md]] is a real append-only build log and [[20_Progress/Projects/AI Use/Claude Kit/Tool Map|Tool Map.md]] tracks named tools (GBrain, gstack, mattpocock-skills, graphify, and 13 others) through sandbox → tested-skills → promoted stages — but `Overview.md`, `Build Map.md`, and `Claude Code/Prompts.md` inside it are still empty files. `Toolkit/` itself is no longer empty (2026-08-10): [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Claude Code|Claude Code.md]] is now a real MOC over five category pairs (`What {Category}.md` / `How to Use {Category}.md` for Agents, Commands, Hooks, MCPs, Skills) plus a shared set of use-case notes ([[Research & Distillation]], [[Vault Curation]], [[Writing Quality]], [[Decision & Planning]], [[Learning & Mastery]], [[Career Ops]], [[Daily Operations]], and two honestly-flagged not-yet-served placeholders, [[Code Review]] and [[Frontend]]).
### GitHub ingestion pipeline
`60_Claude/20_Distilled_Notes/Sources - Plan/` holds the working files for ingesting external repos into the vault: [[60_Claude/20_Distilled_Notes/Sources - Plan/GitHub Ingestion Implementation|GitHub Ingestion Implementation.md]] is a prioritized shortlist of ~50 repos, not a procedure; [[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution|00_Execution.md]] is a prose verdict log across three passes (PDF, Web, GitHub) whose frontmatter says the passes are done while its own body admits the resulting install queue was "planned twice, executed zero times"; `_Notes Created From Ingestion.md` is a 47-row index of notes the passes actually produced, and its own text names the method as a manual read-and-write-down pass across sessions, not yet turned into a repeatable skill. `60_Claude/10_Source_Summaries/Github Ingestion/Claude Kit Implementation.md` is the one real hands-on ingestion session on record — a partial, honestly-incomplete install log for second-brain-claudekit's sandbox tools, blocked on a Chromium dependency and an embedding-provider decision.
### Conversation capture
`60_Claude/05_Clippings/AI Conversations/` is the raw-capture layer, split into `Windows/` and `WSL/`, each further split by source app (Claude Code, Cowork, Cursor). Windows Claude Code capture is live and current. WSL Claude Code capture and Windows Cowork capture both went silent shortly after being wired (WSL stalled 2026-07-30, Cowork stalled 2026-07-24) — the cause is not visible from vault files alone and needs a live check of the WSL and Cowork hook wiring. `60_Claude/07_AI_Information/AI Conversation - Summaries/` is the distillation layer the `export-ai-session` skill writes to; it has four empty scaffold subfolders (`Claude Code/`, `Cowork/`, `Cursor/`, `Kiro/`) that were apparently built for per-source organization but have never been used — the four summaries that actually exist sit flat at the top level, and all four are Cursor-sourced. No Claude Code or Cowork session has ever been distilled into a summary. `60_Claude/07_AI_Information/Session Logs/log.md` is the real, actively-written general session log; its `Claude Kit/` subfolder is a same-day-created, empty, untracked scaffold, distinct from the genuinely active Claude-Kit build log at `20_Progress/Projects/AI Use/Claude Kit/Log.md`.
### Review system
`60_Claude/30_Reviews/AI/` (`Conversations/`, `Scheduled/Weekly/`, `Scheduled/Monthly/`, `Tools/`) is a completely empty shell, with the `Scheduled` subfolders created the same day as this note — nothing writes to it yet. Real review activity in the vault happens at a different path entirely: [[60_Claude/30_Reviews/Weekly Synthesis/Weekly Synthesis Index|Weekly Synthesis Index]] and `60_Claude/30_Reviews/Monthly/` hold two weekly syntheses (five weeks apart) and one monthly review, all produced manually by the existing `/weekly-review` skill. No cron job, tool-use metric, or automated-fix gate exists anywhere in the vault today.
### Project briefs
`60_Claude/40_Project_Briefs/Claude Kit/` is empty — zero files. The idea it's meant to hold, running graphify inside second-brain-claudekit and syncing its output into Jarvis the way `.claude/` already syncs, has real ingredients elsewhere (graphify is installed and has already produced real output against TradingView, see `60_Claude/40_Project_Briefs/TradingView/`; the Unison sync mechanism is proven) but the combination has never been written down as a brief.
### Source-of-truth resources
`40_Resources/CS/AI/` is meant to hold durable, manually-curated knowledge on using each AI platform correctly. `Agent Orchistration/` and `Memory/` are fully empty folders. `Prompts/`, `Token Optimization/`, and `Workflows/` have real content, but it's misfiled against the folder's own stated intent: `Prompts/Chat Gpt Prompts.md` mixes ChatGPT and Cursor prompts with no per-model organization; the best Claude-specific workflow note in the vault, [[40_Resources/CS/AI/Token Optimization/Claude Pro Workflow]], sits under `Token Optimization/` instead of `Workflows/`; `Workflows/AI Workflow.md` is ChatGPT-era content already flagged stale by a sibling note. `Toolkit/` was fully moved out this session into `20_Progress/Projects/AI Use/Claude Kit/Toolkit/`, leaving one note (`Claude Optimization Master Setup.md`) with internal links that now point at a folder that no longer exists.
### This meta-map
`10_Areas/AI/` holds four rich tool-usage guides (`Claude Code.md`, `Codex.md`, `Cursor.md`, `Kiro.md` — comparison-and-setup notes, not folder maps), the actual `Claude OS Map.excalidraw` diagram (embedded in `Claude Code.md`, not stored under `20_Progress/AI` where the operational dashboard lives), an empty and currently-undocumented `Setup/` subfolder, and this file plus [[Notes Map]] and [[Gaps]] — the three notes that now do the job the folder was always meant to do: map every AI-related folder and note in the vault to its purpose, in one place.
## Status
| Cluster | Health |
|---|---|
| Claude Kit sync (second-brain-claudekit) | live — ~280 successful syncs since 2026-07-30 |
| Claude Kit sync (other 8 tracked repos) | static snapshots from 2026-07-05, rollout planned but not started |
| Per-tool registry dashboard | stale — over a month behind, `.canvas` and `.md` disagree |
| AI Use hub | mixed — Cursor AI.md and Gen AI/ current, The AI Hub.md empty |
| GitHub ingestion pipeline | analysis done, execution queue never run |
| Conversation capture (Windows Claude Code) | live |
| Conversation capture (WSL Claude Code, Cowork) | stalled 10–16 days, cause unconfirmed |
| Conversation distillation | never produced a Claude Code or Cowork summary |
| Review system (30_Reviews/AI) | empty shell, unwired |
| Claude Kit project briefs | empty |
| 40_Resources/CS/AI | 2 of 6 subfolders empty, rest real but misfiled |
| 10_Areas/AI meta-map | being built now (this note) |
## Dataview
```dataview
TABLE type, status, updated
FROM "10_Areas/AI" OR "20_Progress/AI" OR "20_Progress/Projects/AI Use" OR "40_Resources/CS/AI" OR "60_Claude/30_Reviews/AI"
SORT updated DESC
```
## Links
[[Notes Map]] lists what each individual note in these folders actually does. [[Gaps]] turns every drift, stall, and empty folder named above into a concrete action statement. [[20_Progress/AI/Claude Code/MOC]] is the detailed per-project registry this note summarizes at the cluster level.

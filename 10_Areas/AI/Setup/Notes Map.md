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
  - "[[20_Progress/AI/Claude Code/Management]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Log]]"
  - "[[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution]]"
  - "[[60_Claude/20_Distilled_Notes/Sources - Plan/_Notes Created From Ingestion]]"
  - "[[60_Claude/10_Source_Summaries/Github Ingestion/Claude Kit Implementation]]"
  - "[[60_Claude/07_AI_Information/AI Conversation - Summaries/WSL Claude Code — Wiring Gap]]"
  - "[[60_Claude/30_Reviews/Weekly Synthesis/Weekly Synthesis Index]]"
  - "[[40_Resources/CS/AI/Token Optimization/Claude Pro Workflow]]"
  - "[[10_Areas/AI/Claude Code]]"
next: Write the missing per-project Setup.md and MOC coverage this note surfaces as absent, starting with Codex/Cursor/Kiro MOCs
---
# Notes Map
==A note earns a link here if another note actually depends on reading it first; everything else gets one sentence saying what job it does for its folder.==
## Purpose
[[Folder Map]] says what each AI folder is for. This note goes one level deeper: what does each real note inside those folders actually do, and which ones are load-bearing enough that other notes should link to them. Read this when deciding whether a new note duplicates something that already exists.
## Map
### Claude Kit sync layer
[[20_Progress/AI/Claude Code/MOC]] is the one note to open first — it inventories every project's `.claude/` state in a table and links out to everything else in this cluster. [[20_Progress/AI/Claude Code/Management]] is the live snapshot of sync health and active blockers; [[20_Progress/AI/Claude Code/Write Log]] is the append-only chronological record of the same layer — read Management for current state, Write Log for how it got there. [[20_Progress/AI/Claude Code/Sync - Unison]] is the verified rollout plan (real WSL paths, real `.claude/` shapes, a draft sync manifest) for extending live sync beyond second-brain-claudekit — nothing in it has shipped yet. [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]] documents the sync script itself (`sync-jarvis.sh`, the 15-minute Scheduled Task, the exact files it touches); its sibling `Sync-Log.md` is the raw run history and `CLAUDE.md` is that repo's own standing-rules file (ingestion pipeline stages, do-not-touch list). The `Da Shit/` folder inside second-brain-claudekit has no corresponding note anywhere — it is genuinely undocumented, which is itself evidence nothing currently depends on it.
### Per-tool operational registry
Each of `20_Progress/AI/{Claude Code,Codex,Cursor,Kiro}/` has its own `MOC.md` in the same Purpose→Map→Status shape as [[20_Progress/AI/Claude Code/MOC]] — Codex's and Cursor's and Kiro's are real but were not read in full this pass; they are the right place to check per-project detail before assuming a project's tool config doesn't exist. `20_Progress/AI/Claude OS Dashboard.md` and its `.canvas` twin are the cross-tool health view — use the `.md`, not the `.canvas`, since the canvas has drifted further out of date.
### AI Use hub
`20_Progress/Projects/AI Use/Cursor AI.md` is a dense, current Cursor workflow guide (Plan Mode, Bugbot, subagents, cloud agents) — the strongest single note in this folder. [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] is the live tracker for every tool moving through second-brain-claudekit's qualification sandbox (stage: sandbox/tested-skills/promoted); [[20_Progress/Projects/AI Use/Claude Kit/Log]] is the append-only build log behind it — Tool Map for current state, Log for the history. `The AI Hub.md` and `Claude Kit/Overview.md` and `Claude Kit/Build Map.md` are named like they should be entry points but are empty — nothing links to them because there is nothing in them yet.
### GitHub ingestion pipeline
[[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution]] is the master verdict log across the PDF, Web, and GitHub ingestion passes — the single note that says what got decided and what's still open, even though its own frontmatter overstates completion relative to its body. [[60_Claude/20_Distilled_Notes/Sources - Plan/GitHub Ingestion Implementation]] is the input to that log: a prioritized shortlist of repos, not a process. [[60_Claude/20_Distilled_Notes/Sources - Plan/_Notes Created From Ingestion]] is the retrospective index of every note the three passes produced (47 rows) — check it before assuming a topic hasn't been ingested yet; it has one broken link (`[[Immediate Action]]`, which should point at Claude Kit Implementation.md but doesn't resolve). [[60_Claude/10_Source_Summaries/Github Ingestion/Claude Kit Implementation]] is the only real hands-on ingestion session on record, and it says plainly what it didn't finish.
### Conversation capture
`60_Claude/05_Clippings/AI Conversations/README.md` documents the capture mechanism (SessionEnd hooks, long-path-safe enumeration for Cowork, the Windows/WSL split) — read it before touching the capture pipeline, but note it also describes two folders (`Claude App/`, `OpenCode/`) that don't exist on disk. [[60_Claude/07_AI_Information/AI Conversation - Summaries/WSL Claude Code — Wiring Gap]] is the note that explains why WSL capture exists at all — it proposed the hook that was added 2026-07-30, right before WSL capture went silent again, which makes it the first note to reopen if that gap gets investigated. `60_Claude/07_AI_Information/AI Conversation - Summaries/README.md` documents the summary-note naming convention but says nothing about the four empty per-source subfolders sitting next to it — that's the ambiguity, written down nowhere else. `60_Claude/07_AI_Information/Session Logs/log.md` is the real general session log; `Session Logs Board.md` is a thin dataview pointer to it, not a separate source of information.
### Review system
[[60_Claude/30_Reviews/Weekly Synthesis/Weekly Synthesis Index]] tracks the two weekly syntheses that exist; `60_Claude/30_Reviews/Monthly/Monthly Review — 2026-06.md` is the one monthly review. Both are produced by the `/weekly-review` skill (`.claude/skills/weekly-review.md`), which writes to these paths, not to `60_Claude/30_Reviews/AI/`. Nothing in `30_Reviews/AI/` has a note yet because nothing has ever been written there.
### Project briefs
`60_Claude/40_Project_Briefs/Claude Kit/` has no notes. `60_Claude/40_Project_Briefs/TradingView/00 Overview.md` is worth reading as a model for what a graphify-backed brief could look like — it already documents re-running graphify (`graphify query`, `/graphify --update`) against a real repo with 2,213 nodes and 142 communities.
### Source-of-truth resources
[[40_Resources/CS/AI/Token Optimization/Claude Pro Workflow]] is the single best-formed note in this folder — a real operating contract for Claude Pro usage (rate limits, surface roles, context-pack prompts, failure modes) — and the closest thing to what `Workflows/` is supposed to hold, despite sitting one folder over. `Token Optimization/Claude Optimization Master Setup.md` is a 2026-05-28 vault audit that already flagged some of what this pass re-confirms (stale `AI Workflow.md`, a since-moved `MCPs.md`) — read it as prior art before repeating the audit. `Prompts/Chat Gpt Prompts.md` and `Workflows/AI Workflow.md` and `Workflows/UMN Workflow.md` each do one narrow job (prompting technique, a stale ChatGPT-era plan, one course's Gemini Gem config) — none of them is the per-platform reference the folder's purpose calls for.
### This meta-map
[[10_Areas/AI/Claude Code]], `Codex.md`, `Cursor.md`, and `Kiro.md` are rich tool-comparison guides — read them for "which tool for which job," not for "where does this folder's content live," which is what [[Folder Map]] and this note are for instead. `Setup/` has no notes in it at all.
## Links
[[Folder Map]] is the folder-level companion to this note. [[Gaps]] turns the absences named here (Codex/Cursor/Kiro MOCs not reviewed, empty hub notes, the broken `[[Immediate Action]]` link) into concrete next actions.

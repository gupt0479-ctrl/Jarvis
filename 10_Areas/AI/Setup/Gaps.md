---
type: action
status: active
created: 2026-08-09
updated: 2026-08-19
tags:
  - action
  - ai
source_note: "[[Folder Map]]"
related_progress:
  - "[[20_Progress/AI/Claude Code/MOC]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution]]"
next: Decide whether/how to reconcile the two home directories' still-disjoint agents/commands/skills content, per [[20_Progress/AI/Claude Code/Sync - Unison]]
---
# Gaps
Derived from [[Folder Map]] and [[Notes Map]], both built from a full read-through of every AI-related folder in the vault on 2026-08-09. Statements only — no checkboxes, no prose paragraphs. Every statement links to the thing it concerns.
## Claude Kit sync layer
**Fully resolved 2026-08-10.** Every real project under `20_Progress/AI/Claude Code/` (`second-brain-claudekit`, `CausalOps`, `Jarvis`, `Portfolio`, `Trading View`, `Resq`, `OpsPilot`, `The Plan`) plus both home directories (`.claude_windows`, `.claude_wsl`) is now live-synced via the manifest-driven [[20_Progress/AI/Claude Code/Sync - Unison]] driver (`sync-all.sh`), each wiped clean and rebuilt, each verified in both directions plus a real conflict test. `Da Shit/` is deleted. `The Plan` turned out to be a real Windows-side sibling vault, not dead as earlier research concluded — found and onboarded the same pass. `Github ReadMe` re-checked and confirmed to still have no real source. Remaining open question, not a gap: whether to reconcile the two home directories' still largely disjoint `agents/`/`commands/`/`skills/` content — see [[20_Progress/AI/Claude Code/Sync - Unison]].
Both pending folder-move commits from the original pass are long since resolved by the vault's own auto-commit bot — no action needed.
## Per-tool operational registry
Refresh [[20_Progress/AI/Claude OS Dashboard]] — it is over a month stale and its `.canvas` twin still claims Portfolio and Trading View are empty when both were re-exported 2026-07-05.
Reconcile or delete the stale `.canvas` fork of [[20_Progress/AI/Claude OS Dashboard]] so the two stop disagreeing.
Re-export `20_Progress/AI/Claude Code/Jarvis/` — [[20_Progress/AI/Claude Code/MOC]] already marks it `stale`, missing `tools:`/`model:` frontmatter on all five agents and the `excalidraw-diagram` command entirely.
## AI Use hub
Write real content into `20_Progress/Projects/AI Use/The AI Hub.md` or delete it — an empty note named "hub" is actively misleading.
Fill or remove `20_Progress/Projects/AI Use/Claude Kit/Overview.md`, `Build Map.md`, and `Claude Code/Prompts.md` — still 0-byte files sitting where real content is expected. (`Toolkit/` itself, previously the same complaint, was filled 2026-08-10 — see [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Claude Code|Toolkit/Claude Code.md]].)
Resolve gstack's missing-Chromium blocker and gbrain's embedding-provider choice, both logged as open in [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]].
## GitHub ingestion pipeline
Fix the broken `[[Immediate Action]]` link in `_Notes Created From Ingestion.md` — it should resolve to [[60_Claude/10_Source_Summaries/Github Ingestion/Claude Kit Implementation]], either by renaming the file or adding an `aliases:` entry.
Correct [[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution]]'s frontmatter, which claims the GitHub pass is done while its own body says the install queue was "planned twice, executed zero times."
Turn the manual read-and-write-down ingestion method, named as unbuilt in `_Notes Created From Ingestion.md`'s own text, into an actual skill instead of repeating it by hand next time.
Delete or fill the 0-byte `60_Claude/20_Distilled_Notes/Sources - Plan/Video Ingestion Implementation.md` placeholder.
## Conversation capture
**Resolved 2026-08-19** — the WSL `SessionEnd`-hook-reliability question below is closed by a separate, parallel effort (a `pwsh`/.NET assembly-load crash in every Stop/SessionEnd hook, root-caused and fixed by wrapping hook commands with `2>/dev/null; exit 0` at the settings.json layer; native scheduled-task retry added; a real scheduled backfill safety net built for both platforms). Not taken on that effort's own word — independently verified here by reading `60_Claude/05_Clippings/AI Conversations/00 - Capture Health.md` directly: both the Windows and WSL backfill tables show consecutive `OK (exit 0)` runs through 2026-08-19T10:30 (Windows) / 10:15 (WSL), "No current failure streak" on both. The original symptom (WSL capture producing nothing since 2026-07-30) is fixed by the backfill mechanism itself, which now catches whatever the event hooks miss — checked, not assumed.
~~Check whether the WSL `SessionEnd` hook is still registered — WSL Claude Code capture under `60_Claude/05_Clippings/AI Conversations/WSL/` has produced nothing since 2026-07-30, the day [[60_Claude/07_AI_Information/AI Conversation - Summaries/WSL Claude Code — Wiring Gap]] says it was wired.~~
Check whether the Cowork sweep is still firing on Windows `SessionEnd` — `60_Claude/05_Clippings/AI Conversations/Windows/Cowork/` has produced nothing since 2026-07-24 despite Windows Claude Code sessions ending on Aug 3, 7, and 8. **Not verified this pass** — the Capture Health dashboard tracks Windows/WSL Claude Code backfill only, not Cowork; left open.
Wire the `export-ai-session` skill to actually write into the four existing empty subfolders (`Claude Code/`, `Cowork/`, `Cursor/`, `Kiro/`) under `60_Claude/07_AI_Information/AI Conversation - Summaries/`, or delete the subfolders and confirm summaries stay flat — right now neither the code nor the docs say which.
Run `export-ai-session` at least once against the Windows Claude Code and Cowork raw transcripts sitting in `60_Claude/05_Clippings/AI Conversations/` — zero distilled summaries exist for either source despite weeks of raw capture.
Update `60_Claude/05_Clippings/AI Conversations/README.md`, which documents `Claude App/` and `OpenCode/` folders that don't exist on disk.
## Review system
Build the automated review pipeline the user wants (tool-use metrics, skill-use metrics, a written review, a separate automation log, a 100%-clarity gate before auto-fixes) from scratch — nothing in `60_Claude/30_Reviews/AI/` is wired to any skill or cron job today.
Point that future pipeline's output at `60_Claude/30_Reviews/AI/Conversations/`, `Tools/`, and `Scheduled/{Weekly,Monthly}/` specifically, since those folders exist but are empty and disconnected from the working `/weekly-review` skill, which writes to [[60_Claude/30_Reviews/Weekly Synthesis/Weekly Synthesis Index]] instead.
Schedule the weekly/monthly cadence via `CronCreate` or the `schedule` skill once the review-writing logic exists — `CronList` currently returns no scheduled jobs at all.
Close the five-week gap between [[60_Claude/30_Reviews/Weekly Synthesis/Weekly Synthesis Index]]'s two entries (W17, W22) if a real weekly cadence is the goal rather than an occasional manual trigger.
## Project briefs
Write the graphify-plus-Unison brief into `60_Claude/40_Project_Briefs/Claude Kit/` — the ingredients (graphify installed and proven against `60_Claude/40_Project_Briefs/TradingView/`, Unison sync proven in [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]) exist separately but the combination has never been written down.
Run graphify inside `second-brain-claudekit/sandbox/graphify/` for real — [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]] shows it as clone-only, never executed there.
Decide whether the graphify-sync brief should use the `type: input` Brief Standard shape or a different one — that standard is scoped to transcript-derived briefs, which this isn't.
## Source-of-truth resources
Populate `40_Resources/CS/AI/Agent Orchistration/` and `40_Resources/CS/AI/Memory/` — both are fully empty despite being named as source-of-truth folders.
Move [[40_Resources/CS/AI/Token Optimization/Claude Pro Workflow]] into `40_Resources/CS/AI/Workflows/` — it is already the best Claude workflow note in the vault, just filed under the wrong subfolder.
Reorganize `40_Resources/CS/AI/Prompts/Chat Gpt Prompts.md` into per-model sections, or split it, so Claude-specific prompting guidance has its own home the way `Prompts/` is supposed to provide.
Replace or archive `40_Resources/CS/AI/Workflows/AI Workflow.md` — it is ChatGPT-era content already flagged stale by `Token Optimization/Claude Optimization Master Setup.md`.
Fix `Claude Optimization Master Setup.md`'s internal links to `Skills/Github Skills.md` and `MCPs.md` — both moved to `20_Progress/Projects/AI Use/Claude Kit/Toolkit/` and the old paths no longer resolve.
Fill or delete the empty `40_Resources/CS/AI/Workflows/Claude Code/` subfolder.
## This meta-map
Review Codex, Cursor, and Kiro's own `MOC.md` files in full — this pass confirmed they exist and are real but did not read them end to end the way `20_Progress/AI/Claude Code/MOC` was read.
`10_Areas/AI/Setup/` is no longer empty — [[Folder Map]], [[Notes Map]], and this note were relocated into it 2026-08-10; its purpose is now this meta-map itself, not open anymore.
Turn the plain-code-formatted folder paths in [[10_Areas/AI/Claude Code]], `Codex.md`, `Cursor.md`, and `Kiro.md` into real wikilinks where the target folders have MOCs, so this meta-map layer and the per-tool registry actually connect.
## Open Threads
Whether `10_Areas/AI`, `20_Progress/AI`, and `20_Progress/Projects/AI Use` should be merged into fewer trees now that [[Folder Map]] has written down what each one does — flagged, not decided, in this pass.
Decided 2026-08-10: the automated review system builds out under `60_Claude/30_Reviews/AI/` as its own tree, kept separate from `Weekly Synthesis/`/`Monthly/` since that structure is concept-mastery review (Capability Engine), a different subject — not yet built, but no longer an open question.

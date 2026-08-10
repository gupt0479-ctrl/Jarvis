---
type: action
status: active
created: 2026-08-09
updated: 2026-08-09
tags:
  - action
  - ai
source_note: "[[Folder Map]]"
related_progress:
  - "[[20_Progress/AI/Claude Code/MOC]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution]]"
next: Decide the "Da Shit" folder's fate in [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]] before it gets rediscovered and mistaken for the live config
---
# Gaps
Derived from [[Folder Map]] and [[Notes Map]], both built from a full read-through of every AI-related folder in the vault on 2026-08-09. Statements only — no checkboxes, no prose paragraphs. Every statement links to the thing it concerns.
## Claude Kit sync layer
Restructure Portfolio, Trading View, Resq, and OpsPilot's flat mirror folders into the nested `.claude/` + sibling-docs (`CLAUDE.md`, `AGENTS.md`, `Setup.md`) shape and onboard them into live sync — CausalOps and Jarvis already went through this 2026-08-10 via the new manifest-driven [[20_Progress/AI/Claude Code/Sync - Unison]] driver (`sync-all.sh`), same steps apply to the rest.
Delete the orphaned `second-brain-claudekit/Da Shit/` folder — confirmed dead, safe to remove, just not yet done.
Wire `.claude_wsl` the same way `.claude_windows` was done 2026-08-10 (wiped clean, curated live sync — `agents/`, `commands/`, `skills/`, `hooks/`, `CLAUDE.md`, secrets/session-state hard-excluded) — see [[20_Progress/AI/Claude Code/.claude_windows/Setup]] for the pattern to repeat.
Commit the in-flight uncommitted move of `20_Progress/AI/Builds & Resources/` to `20_Progress/Projects/AI Use/Builds & Resources/` — content is verified byte-identical, only the git commit is missing.
Commit the in-flight uncommitted move of `40_Resources/CS/AI/Toolkit/` to `20_Progress/Projects/AI Use/Claude Kit/Toolkit/` for the same reason.
## Per-tool operational registry
Refresh [[20_Progress/AI/Claude OS Dashboard]] — it is over a month stale and its `.canvas` twin still claims Portfolio and Trading View are empty when both were re-exported 2026-07-05.
Reconcile or delete the stale `.canvas` fork of [[20_Progress/AI/Claude OS Dashboard]] so the two stop disagreeing.
Re-export `20_Progress/AI/Claude Code/Jarvis/` — [[20_Progress/AI/Claude Code/MOC]] already marks it `stale`, missing `tools:`/`model:` frontmatter on all five agents and the `excalidraw-diagram` command entirely.
## AI Use hub
Write real content into `20_Progress/Projects/AI Use/The AI Hub.md` or delete it — an empty note named "hub" is actively misleading.
Fill or remove `20_Progress/Projects/AI Use/Claude Kit/Overview.md`, `Build Map.md`, and `Claude Code/Prompts.md` — all three are 0-byte files sitting where real content is expected.
Resolve gstack's missing-Chromium blocker and gbrain's embedding-provider choice, both logged as open in [[20_Progress/Projects/AI Use/Claude Kit/Tool Map]].
## GitHub ingestion pipeline
Fix the broken `[[Immediate Action]]` link in `_Notes Created From Ingestion.md` — it should resolve to [[60_Claude/10_Source_Summaries/Github Ingestion/Claude Kit Implementation]], either by renaming the file or adding an `aliases:` entry.
Correct [[60_Claude/20_Distilled_Notes/Sources - Plan/00_Execution]]'s frontmatter, which claims the GitHub pass is done while its own body says the install queue was "planned twice, executed zero times."
Turn the manual read-and-write-down ingestion method, named as unbuilt in `_Notes Created From Ingestion.md`'s own text, into an actual skill instead of repeating it by hand next time.
Delete or fill the 0-byte `60_Claude/20_Distilled_Notes/Sources - Plan/Video Ingestion Implementation.md` placeholder.
## Conversation capture
Check whether the WSL `SessionEnd` hook is still registered — WSL Claude Code capture under `60_Claude/05_Clippings/AI Conversations/WSL/` has produced nothing since 2026-07-30, the day [[60_Claude/07_AI_Information/AI Conversation - Summaries/WSL Claude Code — Wiring Gap]] says it was wired.
Check whether the Cowork sweep is still firing on Windows `SessionEnd` — `60_Claude/05_Clippings/AI Conversations/Windows/Cowork/` has produced nothing since 2026-07-24 despite Windows Claude Code sessions ending on Aug 3, 7, and 8.
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
Whether the automated review system described by the user should live under `60_Claude/30_Reviews/AI/` as scaffolded, or fold into the existing `Weekly Synthesis/`/`Monthly/` structure that already works — needs a decision before any build work starts.

---
type: input
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - claude-code
  - sync
  - claude-kit
notes:
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: Watch the first few scheduled runs after cutover, especially any that land while a live session is mid-edit on the source .claude/
---
# Jarvis — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is
The live-synced mirror of this vault's own root `.claude/` — the config actually executing whenever a Claude Code session runs inside Jarvis, including the one that built this sync. Rebuilt clean 2026-08-10 — the folder previously held a flat, hand-copied, drifted snapshot that [[20_Progress/AI/Claude Code/MOC]] had already flagged `stale`: missing `challenge`, `excalidraw-diagram`, `ideas`, `llm-council`, `note-to-actions`, `strategy`, `transcript-to-brief`, and `mcp-hub` entirely, among other gaps. That snapshot was wiped and replaced with a fresh sync.
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `Jarvis`, `needs_fat: true` (both replicas are DrvFs from the executing WSL process's point of view, even though both are Windows-side paths on the same drive — confirmed empirically rather than assumed, since the first run needed it same as every other entry). Synced paths: `.claude/agents`, `.claude/commands`, `.claude/skills`, `.claude/context`, `.claude/rules`, `.claude/settings.json`, root `CLAUDE.md`, root `AGENTS.md`. Not synced: `.claude/settings.local.json`, `.claude/README.md`, `.claude/GITHUB_WORKFLOW.md`, `.claude/scheduled_tasks.lock` — the first is machine-local, the rest are repo-facing docs and runtime state that don't need a Jarvis-side copy.
## What's actually here
`.claude/agents/` (5), `.claude/commands/` (19), `.claude/skills/` (21, including the `closeday/`, `ingesting-clipping/`, `startday/` subfolder-shaped skills), `.claude/context/workspace-context.md`, `.claude/rules/human-writing.md`, `.claude/settings.json`, root `CLAUDE.md`, root `AGENTS.md` — verified byte-identical against the live source immediately after the first sync (`diff` on every list and every doc file, zero differences).
## Verification performed
Extra care taken here specifically because the source is the live config of the very session that built this sync — not treated as routine just because the mechanism was already proven twice on other targets:
1. First sync populated the (wiped) mirror entirely from the live source — confirmed every file and folder count matches exactly (19 commands, 21 skills, both root docs).
2. Created a new, inert test file (`_sync_test.md`, not a real command) on the Jarvis-mirror side, synced, confirmed it landed in the real live `.claude/commands/` — mirror-to-source direction proven without touching any file this session actually reads.
3. Deleted the test file from both the real source and the mirror immediately after confirming, synced once more, confirmed a clean no-op and zero leftover files.
4. Deliberately did **not** run the "edit the same file on both sides to trigger a conflict" leg of the test here, unlike `.claude_windows` and CausalOps — that leg was already proven twice with the identical Unison invocation and binary, and repeating it against this session's own live config for marginal additional confidence wasn't worth the risk of touching a file this session might read mid-edit.
## Trigger
Manual only as of 2026-08-10 — runs when `sync-all.sh Jarvis` (or a full `sync-all.sh` run) is invoked by hand. Cutover to the 15-minute Windows Scheduled Task happens once all three of this session's targets are confirmed (see [[20_Progress/AI/Claude Code/Sync - Unison]]) — worth watching the first few scheduled runs specifically for what happens if one lands while a live session has an uncommitted edit to a synced file (e.g. `settings.json`) open.

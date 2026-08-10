---
type: project
status: active
created: 2026-07-30
updated: 2026-08-10
tags:
  - claude-code
  - setup
  - second-brain-claudekit
  - sync
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
  - "[[Tool Map]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
next: None — 15-min hidden Task Scheduler sync is live (ClaudeKit-Sync-All), now driving 4 projects, not just this one
---
# second-brain-claudekit — Claude Code Setup

Unlike the remaining candidate folders in `20_Progress/AI/Claude Code/` (Portfolio, Trading View, Resq, OpsPilot — still hand-copied snapshots that drift over time), **this folder is kept live by a script**, not a manual copy — and as of 2026-08-10, so are `CausalOps/`, `Jarvis/`, and `.claude_windows/`, all driven by the same script. Run `60_Claude/scripts/sync-all.sh` from the `second-brain-claudekit` repo (WSL: `~/projects/ai/claude/second-brain-claudekit`) — with no arguments it syncs every manifest entry marked `live`; pass a name (e.g. `sync-all.sh second-brain-claudekit`) to sync just this one. This folder's `.claude/agents`, `.claude/commands`, `.claude/hooks`, `.claude/settings.json`, and `CLAUDE.md` are brought to exact parity with the repo's live versions, in either direction — edits made here flow back to the repo too. `sync-jarvis.sh` (the old single-project script) still exists in this same folder for reference but is not wired to anything — do not point new work at it. Full research, tool choice (Unison over `rclone bisync`), and real test results (including a genuine conflict test) live in the repo's `_docs/Sync.md`.

The `Da Shit/` folder that used to sit alongside `.claude/` here is gone — deleted 2026-08-10 after the naming-rename idea it represented was explicitly reversed (every project mirror now keeps the literal `.claude/` name; see `_docs/Sync.md`'s 2026-08-10 amendment). If you see `Da Shit/` referenced anywhere else in older notes, that reference is stale.

Editing files in this folder directly is safe and intentional — that's the point of the bidirectional sync — but a genuine conflict (same file changed on both sides between syncs) is **skipped, not resolved**. Check `Sync-Log.md` in this folder after a sync if something doesn't look like it propagated.

## What's synced here

- `.claude/agents/` — the live sub-agents this repo's own Claude Code session uses
- `.claude/commands/` — vault-specific slash commands
- `.claude/hooks/` — automation hooks
- `.claude/settings.json` — Claude Code settings for this repo
- `CLAUDE.md` — the repo's own standing-rules file (qualification workflow, do-not-touch list)

## What's deliberately NOT synced

- `.claude/settings.local.json` — machine-local overrides, not committed in the repo either
- `Docs/`, `50_Claude/`, `sandbox/`, `tested-skills/`, `.git/` — everything else in the repo; this folder mirrors the behavioral config layer only, not the whole repo

## Trigger status

Windows Scheduled Task `ClaudeKit-Sync-All` runs `sync-all.sh` every 15 minutes, invoking `wsl.exe` directly — no VBS/wscript wrapper (the old launcher's fire-and-forget bug is exactly why it's gone; see `_docs/Sync.md`'s incident writeups). This one task now drives `second-brain-claudekit`, `CausalOps`, `Jarvis`, and `.claude_windows` in a single run. The old task, `SecondBrainClaudekit-JarvisSync`, is disabled (not deleted) as a rollback reference. Manual runs: `60_Claude/scripts/sync-all.sh [name]` from the repo. Re-register the task (if needed): `60_Claude/scripts/register-sync-task.ps1`.

## Links
[[20_Progress/AI/Claude Code/MOC]] · [[Tool Map]] · [[20_Progress/Projects/AI Use/Claude Kit/Log]] · [[20_Progress/AI/Claude Code/Sync - Unison]]

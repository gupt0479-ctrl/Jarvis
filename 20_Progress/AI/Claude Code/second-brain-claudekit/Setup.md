---
type: project
status: active
created: 2026-07-30
updated: 2026-07-30
tags:
  - claude-code
  - setup
  - second-brain-claudekit
  - sync
notes:
  - "[[20_Progress/AI/Claude Code/MOC]]"
  - "[[Tool Map]]"
next: None — 15-min hidden Task Scheduler sync is live (SecondBrainClaudekit-JarvisSync)
---
# second-brain-claudekit — Claude Code Setup

Unlike the other folders in `20_Progress/AI/Claude Code/` (Jarvis, Portfolio, CausalOps, etc. — all hand-copied snapshots that drift behind their live `.claude/` over time, as `Jarvis/Setup.md` documents about itself), **this folder is kept live by a script**, not a manual copy. Run `50_Claude/scripts/sync-jarvis.sh` from the `second-brain-claudekit` repo (WSL: `~/projects/ai/claude/second-brain-claudekit`) and this folder's `.claude/agents`, `.claude/commands`, `.claude/hooks`, `.claude/settings.json`, and `CLAUDE.md` are brought to exact parity with the repo's live versions, in either direction — edits made here flow back to the repo too. Full research, tool choice (Unison over `rclone bisync`), and real test results (including a genuine conflict test) live in the repo's `Docs/Sync.md`.

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

Windows Scheduled Task `SecondBrainClaudekit-JarvisSync` runs `sync-jarvis.sh` every 15 minutes through a hidden `wscript` launcher (no console popup). Manual runs still work: `50_Claude/scripts/sync-jarvis.sh` from the repo. Re-register (if needed): `30_Order/System/claude-workflow/scripts/register-jarvis-sync-task.ps1`.

## Links
[[20_Progress/AI/Claude Code/MOC]] · [[Tool Map]] · [[20_Progress/Projects/AI Use/Claude Kit/Log]]

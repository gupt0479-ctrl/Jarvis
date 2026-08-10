---
type: evergreen
status: sprout
created: 2026-08-10
updated: 2026-08-10
tags:
  - evergreen
  - claude-kit
  - hooks
notes:
  - "[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/How to Use Hooks]]"
  - "[[10_Areas/AI/Setup/Gaps]]"
next: Register jarvis-session-continuity.ps1 in .claude/settings.json, or correct the notes that currently claim it is already wired
---
# What Hooks
==Only one of Jarvis's two documented hooks is actually registered right now — verified by reading .claude/settings.json directly, not by trusting the note that describes it.==
## Promoted in claudekit
second-brain-claudekit's `.claude/hooks/`, both wired in its `settings.json`, both confirmed present as `.ps1` files with `.md` companion docs.
- **after-edit-log.ps1** — `PostToolUse` (`Write|Edit|MultiEdit`) — appends a log line to `60_Claude/Sessions/_today-edits.md` on every edit.
- **session-wrapup.ps1** — `Stop` — reminds to run `/compress` if no session log was written that session.
Both were the source of a real incident (`_docs/Repo-Map.md`'s "50_Claude recreation bug") — hardcoded a pre-rename path, silently recreated a deleted folder the moment the hook re-armed after a git restore. Fixed 2026-08-08. Worth remembering when writing any hook here: a hardcoded path survives a folder rename as a silent bug, not a loud one.
## Live in Jarvis
Verified directly against `.claude/settings.json` and `.claude/settings.local.json` at the vault root, not against `10_Areas/AI/Claude Code.md`'s table, which claims two wired hooks — that claim is only half true right now.
- **jarvis-write-guard.ps1** — `PreToolUse` (`Write|Edit|MultiEdit`) — **actually registered**, confirmed in `.claude/settings.json`. Enforces the Write Contract: denies vault-root files, `50_Archive/`, `.obsidian/`, `05_Clippings/`, `.cursor/`, `.kiro/`, `.git/`; allowlists daily-ops paths. Fails open on a JSON parse error.
- **jarvis-session-continuity.ps1** — exists on disk at `30_Order/System/claude-workflow/hooks/jarvis-session-continuity.ps1`, documented as injecting context at `SessionStart` and continuity at `SessionEnd` — **not present in either settings file**, so it does not currently run. This is a real, current gap, not a documentation nitpick — the "morning context assembly" behavior several notes describe as automatic is not happening via this mechanism today.
## Links
[[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Hooks/How to Use Hooks]] for lifecycle-event guidance. [[10_Areas/AI/Setup/Gaps]] already names the broader "nothing runs on a schedule" gap this connects to.

---
type: index
status: active
created: 2026-07-05
updated: 2026-08-10
tags:
  - claude-code
  - moc
  - index
notes:
  - "[[20_Progress/AI/Claude OS Dashboard]]"
  - "[[20_Progress/AI/Claude Code/Jarvis/Setup]]"
  - "[[20_Progress/AI/Claude Code/CausalOps/Setup]]"
  - "[[20_Progress/AI/Claude Code/.claude_windows/Setup]]"
  - "[[20_Progress/AI/Claude Code/OpsPilot/Setup]]"
  - "[[20_Progress/AI/Claude Code/Resq/Setup]]"
  - "[[20_Progress/AI/Claude Code/The Plan/Setup]]"
  - "[[20_Progress/AI/Claude Code/Github ReadMe/Setup]]"
  - "[[20_Progress/AI/Claude Code/Portfolio/Setup]]"
  - "[[20_Progress/AI/Claude Code/Trading View/Setup]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/Management]]"
  - "[[20_Progress/AI/Claude Code/Write Log]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
next: Onboard Portfolio, Trading View, Resq, and OpsPilot into live sync next, then .claude_wsl
---
# Claude Code — Content Map
Every project folder under `20_Progress/AI/Claude Code/` now has a `Setup.md` that inventories its files and tags each markdown note with a `setup_status`. This MOC is the one place to see all of them at once and find what needs work, without opening every folder.

**Upstream of this map:** tools land in a real project's `.claude/` (and therefore in this map) only after clearing the qualification pipeline run in `gupta-builds/second-brain-claudekit` (`~/projects/ai/claude/second-brain-claudekit`, WSL). That pipeline's own current state — GBrain (sandbox, tested, pending an embedding-key decision), gstack (sandbox, blocked on missing Chromium libs), mattpocock-skills (tested-skills, partial review) — is tracked separately at [[Tool Map|Claude Kit/Tool Map]], not duplicated here. None of the three have reached any project's real `.claude/` yet, so no row below reflects them.

**Four rows below are live, not static snapshots, as of 2026-08-10:** `second-brain-claudekit`, `CausalOps`, `Jarvis`, and `.claude_windows`. All four are kept at parity with their real source by the same manifest-driven driver, `second-brain-claudekit/60_Claude/scripts/sync-all.sh` (superseding the old single-project `sync-jarvis.sh`) — see each project's own `Setup.md` and the repo's `_docs/Sync.md` for the full research, incident history, and real test results (every direction and a genuine conflict tested for real on each of the three newly-onboarded entries, not just assumed from the mechanism working elsewhere). The driver runs every 15 minutes via the Windows Scheduled Task `ClaudeKit-Sync-All`, which invokes `wsl.exe` directly — no VBS wrapper, so `LastTaskResult` is now an honest signal instead of always reporting 0.
`.claude_windows/` is no longer a raw unmanaged mirror — rebuilt clean 2026-08-10 as a curated, live-synced mirror of the real Windows home `.claude` (see its own `Setup.md`). `.claude_wsl/` remains a raw, untracked one-time dump of `~/.claude` (thousands of files: credentials, backups, cache, daemon state) — still excluded from this map on purpose, still noted here for completeness only, pending the same clean-rebuild treatment `.claude_windows/` just got.

**Current status and sync health**: [[20_Progress/AI/Claude Code/Management|Management.md]] (live snapshot: sync status, active blockers, recent findings) and [[20_Progress/AI/Claude Code/Write Log|Write Log.md]] (append-only chronological record of every change to this layer) are the two files to check first, before opening any individual project's Setup.md. The multi-project sync rollout plan (which projects are mapped vs. actually live-synced) lives in [[20_Progress/AI/Claude Code/Sync - Unison]].
## Projects
| Project | Status | Last Updated | Setup |
|---|---|---|---|
| Jarvis | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/Jarvis/Setup\|Setup]] |
| CausalOps | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/CausalOps/Setup\|Setup]] |
| OpsPilot | static | 2026-07-05 | [[20_Progress/AI/Claude Code/OpsPilot/Setup\|Setup]] |
| Resq | static | 2026-07-05 | [[20_Progress/AI/Claude Code/Resq/Setup\|Setup]] |
| The Plan | draft | 2026-07-05 | [[20_Progress/AI/Claude Code/The Plan/Setup\|Setup]] |
| Github ReadMe | dead | 2026-07-05 | [[20_Progress/AI/Claude Code/Github ReadMe/Setup\|Setup]] |
| Portfolio | static | 2026-07-05 | [[20_Progress/AI/Claude Code/Portfolio/Setup\|Setup]] |
| Trading View | static | 2026-07-05 | [[20_Progress/AI/Claude Code/Trading View/Setup\|Setup]] |
| second-brain-claudekit | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup\|Setup]] |
| .claude_windows | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/.claude_windows/Setup\|Setup]] |
| .claude_wsl | unmanaged mirror | — | not tracked (raw `~/.claude` backup) |
## Needs Work
```dataview
TABLE setup_status, updated, file.folder AS Project
FROM "20_Progress/AI/Claude Code"
WHERE setup_status AND setup_status != "current"
SORT setup_status ASC, file.folder ASC
```
## All Tracked Files
```dataview
TABLE setup_status, updated
FROM "20_Progress/AI/Claude Code"
WHERE setup_status
SORT file.folder ASC, file.name ASC
```
## Links
[[20_Progress/AI/Claude OS Dashboard]]

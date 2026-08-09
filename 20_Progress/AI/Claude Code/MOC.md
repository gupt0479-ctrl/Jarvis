---
type: index
status: active
created: 2026-07-05
updated: 2026-07-30
tags:
  - claude-code
  - moc
  - index
notes: '["[[20_Progress/AI/Claude OS Dashboard]]", "[[20_Progress/AI/Claude
  Code/Jarvis/Setup]]", "[[20_Progress/AI/Claude Code/CausalOps/Setup]]",
  "[[20_Progress/AI/Claude Code/OpsPilot/Setup]]", "[[20_Progress/AI/Claude
  Code/Resq/Setup]]", "[[20_Progress/AI/Claude Code/The Plan/Setup]]",
  "[[20_Progress/AI/Claude Code/Github ReadMe/Setup]]", "[[20_Progress/AI/Claude
  Code/Portfolio/Setup]]", "[[20_Progress/AI/Claude Code/Trading View/Setup]]",
  "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]",
  "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]",
  "[[20_Progress/AI/Claude Code/Management]]", "[[20_Progress/AI/Claude
  Code/Write Log]]", "[[20_Progress/AI/Claude Code/Sync - Unison]]"]'
next: Get Anant's per-project go-ahead on [[20_Progress/AI/Claude Code/Sync -
  Unison]]'s candidate list, then onboard the first additional project beyond
  second-brain-claudekit
---
# Claude Code — Content Map
Every project folder under `20_Progress/AI/Claude Code/` now has a `Setup.md` that inventories its files and tags each markdown note with a `setup_status`. This MOC is the one place to see all of them at once and find what needs work, without opening every folder.

**Upstream of this map:** tools land in a real project's `.claude/` (and therefore in this map) only after clearing the qualification pipeline run in `gupta-builds/second-brain-claudekit` (`~/projects/ai/claude/second-brain-claudekit`, WSL). That pipeline's own current state — GBrain (sandbox, tested, pending an embedding-key decision), gstack (sandbox, blocked on missing Chromium libs), mattpocock-skills (tested-skills, partial review) — is tracked separately at [[Tool Map|Claude Kit/Tool Map]], not duplicated here. None of the three have reached any project's real `.claude/` yet, so no row below reflects them.

**`second-brain-claudekit` is the one row below that isn't a static snapshot.** It's kept at parity with the repo's live `.claude/` by a tested Unison sync script (`50_Claude/scripts/sync-jarvis.sh` in that repo), not a manual copy — see [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup|its Setup.md]] and the repo's `Docs/Sync.md` for the research and real test results (install, first sync, reverse-direction sync, and a genuine conflict all tested for real this session). The sync runs on-demand only; no automatic scheduler trigger is wired up yet.
`.claude_windows/` and `.claude_wsl/` (formerly `Windows Home/`/`WSL Home/`) are excluded from this map on purpose — they're raw mirrors of `~/.claude` (thousands of files each: credentials, backups, cache, daemon state), not hand-authored project configs. They're noted here for completeness, not tracked.

**Current status and sync health**: [[20_Progress/AI/Claude Code/Management|Management.md]] (live snapshot: sync status, active blockers, recent findings) and [[20_Progress/AI/Claude Code/Write Log|Write Log.md]] (append-only chronological record of every change to this layer) are the two files to check first, before opening any individual project's Setup.md. The multi-project sync rollout plan (which projects are mapped vs. actually live-synced) lives in [[20_Progress/AI/Claude Code/Sync - Unison]].
## Projects
| Project | Status | Last Updated | Setup |
|---|---|---|---|
| Jarvis | stale | 2026-07-05 | [[20_Progress/AI/Claude Code/Jarvis/Setup\|Setup]] |
| CausalOps | static | 2026-07-05 | [[20_Progress/AI/Claude Code/CausalOps/Setup\|Setup]] |
| OpsPilot | static | 2026-07-05 | [[20_Progress/AI/Claude Code/OpsPilot/Setup\|Setup]] |
| Resq | static | 2026-07-05 | [[20_Progress/AI/Claude Code/Resq/Setup\|Setup]] |
| The Plan | draft | 2026-07-05 | [[20_Progress/AI/Claude Code/The Plan/Setup\|Setup]] |
| Github ReadMe | dead | 2026-07-05 | [[20_Progress/AI/Claude Code/Github ReadMe/Setup\|Setup]] |
| Portfolio | static | 2026-07-05 | [[20_Progress/AI/Claude Code/Portfolio/Setup\|Setup]] |
| Trading View | static | 2026-07-05 | [[20_Progress/AI/Claude Code/Trading View/Setup\|Setup]] |
| second-brain-claudekit | live-synced | 2026-07-30 | [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup\|Setup]] |
| .claude_windows | unmanaged mirror | — | not tracked (raw `~/.claude` backup, ~7,300 files) |
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

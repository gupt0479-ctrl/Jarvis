---
type: index
status: active
created: 2026-07-05
updated: 2026-08-20
tags:
  - claude-code
  - moc
  - index
notes:
  - "[[20_Progress/AI/Claude OS Dashboard]]"
  - "[[20_Progress/AI/Claude Code/Jarvis/Setup]]"
  - "[[20_Progress/AI/Claude Code/CausalOps/Setup]]"
  - "[[20_Progress/AI/Claude Code/.claude_windows/Setup]]"
  - "[[20_Progress/AI/Claude Code/.claude_wsl/Setup]]"
  - "[[20_Progress/AI/Claude Code/OpsPilot/Setup]]"
  - "[[20_Progress/AI/Claude Code/Resq/Setup]]"
  - "[[20_Progress/AI/Claude Code/The Plan/Setup]]"
  - "[[20_Progress/AI/Claude Code/Github ReadMe/Setup]]"
  - "[[20_Progress/AI/Claude Code/Portfolio/Setup]]"
  - "[[20_Progress/AI/Claude Code/Trading View/Setup]]"
  - "[[20_Progress/AI/Claude Code/second-brain-claudekit/Setup]]"
  - "[[20_Progress/AI/Claude Code/internship-research-loop/Setup]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Tool Map]]"
  - "[[20_Progress/AI/Claude Code/Management]]"
  - "[[20_Progress/Projects/AI Use/Claude Kit/Log]]"
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
next: internship-research-loop onboarded 2026-09-05 (11th live entry) - decide whether it joins the 15-minute Scheduled Task or stays manual; deferred settings.json/settings.local.json portability question still open
---
# Claude Code — Content Map
Every project folder under `20_Progress/AI/Claude Code/` now has a `Setup.md` that inventories its files and tags each markdown note with a `setup_status`. This MOC is the one place to see all of them at once and find what needs work, without opening every folder.

**Upstream of this map:** tools land in a real project's `.claude/` (and therefore in this map) only after clearing the qualification pipeline run in `gupta-builds/second-brain-claudekit` (`~/projects/ai/claude/second-brain-claudekit`, WSL). That pipeline's own current state — GBrain (sandbox, tested, pending an embedding-key decision), gstack (sandbox, blocked on missing Chromium libs), mattpocock-skills (tested-skills, partial review) — is tracked separately at [[Tool Map|Claude Kit/Tool Map]], not duplicated here. None of the three have reached any project's real `.claude/` yet, so no row below reflects them.

**Every project row below except Github ReadMe is now live, not a static snapshot, as of 2026-08-10.** All nine are kept at parity with their real source by the same manifest-driven driver, `second-brain-claudekit/60_Claude/scripts/sync-all.sh` (superseding the old single-project `sync-jarvis.sh`) — see each project's own `Setup.md` and the repo's `_docs/Sync.md` for the full research, incident history, and real test results (every direction, plus a genuine conflict, tested for real on every entry before it was trusted). The driver runs every 15 minutes via the Windows Scheduled Task `ClaudeKit-Sync-All`, which invokes `wsl.exe` directly — no VBS wrapper, so `LastTaskResult` is now an honest signal instead of always reporting 0.
`.claude_windows/` and `.claude_wsl/` are no longer raw unmanaged mirrors — both rebuilt clean 2026-08-10 as curated, live-synced mirrors of the real Windows and WSL home directories (see their own `Setup.md`s), replacing raw one-time dumps that had accumulated thousands of files each, including live credentials and (on the WSL side) a plaintext GitHub token.
**`The Plan` was a real correction, not a re-run of an old plan.** Earlier research (2026-07-30, and again earlier in this same session) concluded no repo backed it, because that research only checked `~/projects` on WSL. Direct inspection 2026-08-10 found it's a genuine Windows-side sibling Obsidian vault (`D:\Users\_Anant\10_Areas\Documents\The Plan`, git remote `gupta-builds/Obsidian-SecondBrain`) with its own real `.claude/` — now onboarded the same way as every other project. `Github ReadMe` got the same re-check and stayed `dead` — confirmed, not assumed, that no matching repo exists anywhere.

**Current status and sync health**: [[20_Progress/AI/Claude Code/Management|Management.md]] (live snapshot: sync status, active blockers, recent findings) is the file to check first, before opening any individual project's Setup.md. The append-only chronological record of changes to this layer now lives in [[20_Progress/Projects/AI Use/Claude Kit/Log|Claude Kit/Log.md]] — [[20_Progress/AI/Claude Code/Write Log|Write Log.md]] carried that role until 2026-08-20, when it was retired and folded in after 21 days of unmaintained silence (kept for historical reference, not deleted). The multi-project sync rollout plan (which projects are mapped vs. actually live-synced) lives in [[20_Progress/AI/Claude Code/Sync - Unison]].
**2026-08-20 audit, recorded in [[20_Progress/Projects/AI Use/Claude Kit/Log|Log.md]]'s dated "correction" entry:** all ten rows below re-verified real and current. A same-day sync-task failure (16:36:56 attempt, non-zero result) turned out transient — re-checked 2026-08-21, the task has been running clean since, and second-brain-claudekit's manifest fix (`README.md`/`_docs` added, `settings.json` dropped) has fully propagated. Stray `.claude/settings.json` copies removed from the `Jarvis`, `Resq`, `second-brain-claudekit`, `The Plan`, and `Trading View` mirrors, matching the source manifest's own removal of that path — re-confirmed absent everywhere 2026-08-21. `.claude_windows/` and `.claude_wsl/` now have real Toolkit-level depth documentation at [[20_Progress/Projects/AI Use/Claude Kit/Toolkit/Global/What Global|Toolkit/Global]], distinguishing global (home-directory) tooling from the project-scoped tooling this MOC otherwise tracks.
## Projects
| Project | Status | Last Updated | Setup |
|---|---|---|---|
| Jarvis | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/Jarvis/Setup\|Setup]] |
| CausalOps | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/CausalOps/Setup\|Setup]] |
| OpsPilot | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/OpsPilot/Setup\|Setup]] |
| Resq | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/Resq/Setup\|Setup]] |
| The Plan | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/The Plan/Setup\|Setup]] |
| Github ReadMe | dead | 2026-08-10 | [[20_Progress/AI/Claude Code/Github ReadMe/Setup\|Setup]] |
| Portfolio | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/Portfolio/Setup\|Setup]] |
| Trading View | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/Trading View/Setup\|Setup]] |
| second-brain-claudekit | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/second-brain-claudekit/Setup\|Setup]] |
| internship-research-loop | live-synced | 2026-09-05 | [[20_Progress/AI/Claude Code/internship-research-loop/Setup\|Setup]] |
| .claude_windows | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/.claude_windows/Setup\|Setup]] |
| .claude_wsl | live-synced | 2026-08-10 | [[20_Progress/AI/Claude Code/.claude_wsl/Setup\|Setup]] |
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

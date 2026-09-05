---
type: input
status: sprout
created: 2026-09-05
updated: 2026-09-05
tags:
  - claude-code
  - sync
  - claude-kit
notes:
  - "[[20_Progress/AI/Claude Code/Sync - Unison]]"
  - "[[20_Progress/AI/Claude Code/MOC]]"
next: Confirm whether internship-research-loop should move onto the 15-minute Windows Scheduled Task alongside the other live entries, or stay manual-trigger for now.
---
# internship-research-loop — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is
The live-synced mirror of `~/projects/work/internship-research-loop` (WSL, git remote `gupta-builds/internship-research-loop`), Anant's internship-search automation repo (contact research, program-writer, application tracking, promotion, testing-tools). This project's `.claude/` was built out directly in a vault session the week of 2026-09-01 — 7 agents, 8 skills, 3 rules, a hook — entirely outside this sync pipeline. This is the first time it's been onboarded: manifest entry added 2026-09-05, first sync run same day.
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `internship-research-loop`, `needs_fat: true` (source is native ext4 WSL, mirror is DrvFs Windows). Synced paths: `.claude/agents`, `.claude/hooks`, `.claude/skills`, `.claude/rules`, `.claude/context`, root `CLAUDE.md`, root `README.md`. Not synced: `.claude/settings.json` / `.claude/settings.local.json` (project config, not reference content — same exclusion CausalOps uses) and `.claude/context` had no files at sync time (folder exists, empty).
## What's actually here
- `.claude/agents/` — 7 files: `applying.md`, `contact-researcher.md`, `loop-verifier.md`, `program-writer.md`, `promotion.md`, `testing-tools.md`, `tracking.md`.
- `.claude/hooks/` — 1 file: `review-reminder.sh` (registered on `PostToolUse` for `Write|Edit|MultiEdit` in the real `.claude/settings.json`).
- `.claude/skills/` — 8 folders: `applying-rn`, `program-write`, `promote-dossier`, `promoting-manual-find`, `review-loop-change`, `tailoring-application`, `testing`, `tracking`.
- `.claude/rules/` — 3 files: `autonomous.md`, `internship-loop.md`, `jarvis.md`.
- `CLAUDE.md` — the project's real operating instructions (15716 bytes as of 2026-09-05).
- `README.md` — 1515 bytes.
## Verification performed
First run only, 2026-09-05: `sync-all.sh internship-research-loop` exited `OK`, populated this mirror folder from empty, and simultaneously populated `second-brain-claudekit/{agents,hooks,skills,instructions}/internship-research-loop/` via the same run's one-way reference-copy step. File counts cross-checked directly against the real WSL source (agents: 7, skills: 8, hooks: 1, rules: 3) — no full bidirectional conflict test run yet (mirror was empty, so this first run was effectively one-directional; the real round-trip/conflict battery CausalOps ran on 2026-08-10 hasn't been repeated here yet).
## Trigger
Manual only as of 2026-09-05 — runs when `sync-all.sh internship-research-loop` (or a full `sync-all.sh` run) is invoked by hand. Not yet on the 15-minute Windows Scheduled Task.

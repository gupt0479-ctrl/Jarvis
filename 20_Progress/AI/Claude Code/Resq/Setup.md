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
next: Watch the first few scheduled runs, then apply the same shape to OpsPilot
---
# Resq — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is
The live-synced mirror of `~/projects/hackathon/Resq` (WSL, git remote `gupta-builds/Resq`), a hackathon project. Rebuilt clean 2026-08-10, replacing an old flat, hand-copied dump. Shape note: this repo has **no `agents/`/`commands/`/`hooks/` at all** — its `.claude/` is an agent-handoff documentation set instead (PRD, context, playbooks, decisions, checklists), the same pattern as OpsPilot.
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `Resq`, `needs_fat: true`. Synced paths: `.claude/PRD.md`, `.claude/README.md`, `.claude/context`, `.claude/playbooks`, `.claude/decisions`, `.claude/checklists`, `.claude/settings.json`, root `AGENTS.md`. **`.claude/settings.json` added 2026-08-10** — present in the real repo but missing from the original manifest draft, caught during the fresh pre-sync check rather than after. No root `CLAUDE.md` exists in this repo — confirmed, not a gap.
## What's actually here
- `.claude/PRD.md`, `.claude/README.md` — the project's product spec and handoff readme.
- `.claude/context/` — 5 files: `12hour-execution.md`, `architecture.md`, `collections-action-implementation.md`, `current-state.md`, `product-vision.md`.
- `.claude/playbooks/` — 4 files: `backend-and-api.md`, `supabase-and-data.md`, `tinyfish-and-agent.md`, `ui-and-demo.md`.
- `.claude/decisions/decision-log.md` — the running decision record.
- `.claude/checklists/` — `change-gate.md`, `demo-readiness.md`.
- `.claude/settings.json` — Claude Code config.
- `AGENTS.md` — present at repo root.
## Verification performed
Both directions and the conflict path tested for real with a throwaway file (`.claude/decisions/_sync_test.md`):
1. Created on the Jarvis-mirror side, synced, confirmed it landed in the real WSL repo.
2. Edited on the WSL repo side, synced, confirmed the edit landed back in the mirror.
3. Edited differently on both sides without syncing in between, synced: Unison reported the conflict and **both edits stayed intact**.
4. Deleted from both sides, synced once more, confirmed a clean no-op.
## Trigger
Live on the 15-minute Windows Scheduled Task `ClaudeKit-Sync-All` as of 2026-08-10.

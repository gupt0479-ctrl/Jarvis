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
next: Watch the first few scheduled runs; this was the last of the four project candidates onboarded 2026-08-10
---
# OpsPilot — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is
The live-synced mirror of `~/projects/hackathon/opspilot` (WSL, git remote `gupta-builds/opspilot`), a hackathon submission project — a reservation → invoice → payment → finance → feedback → recovery pipeline. Rebuilt clean 2026-08-10, replacing an old flat, hand-copied dump. Same doc-only `.claude/` shape as Resq (no `agents/`/`commands/`/`hooks/`), plus a `workflows/` subfolder Resq doesn't have.
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `OpsPilot`, `needs_fat: true`. Synced paths: `.claude/PRD.md`, `.claude/README.md`, `.claude/context`, `.claude/playbooks`, `.claude/workflows`, `.claude/decisions`, `.claude/checklists`, root `CLAUDE.md`, root `AGENTS.md`. Double-checked before this sync ran that `.claude/` genuinely has no top-level `settings.json`/`settings.local.json` here (confirmed via direct listing — unlike Resq, which did have one the manifest was initially missing).
## What's actually here
- `.claude/PRD.md`, `.claude/README.md`.
- `.claude/context/` — 6 files: `6hour-status.md`, `architecture.md`, `current-state.md`, `external-review-codex-2026-04.md`, `keyword-map.md`, `remote-main-and-merge.md`.
- `.claude/playbooks/` — 6 files: `ai-features.md`, `backend-and-api.md`, `integrations-and-webhooks.md`, `invoice-and-finance.md`, `supabase-and-data.md`, `ui-and-read-models.md`.
- `.claude/workflows/restaurant-core-demo.md`.
- `.claude/decisions/decision-log.md`.
- `.claude/checklists/` — `ai-change-checklist.md`, `change-planning.md`, `demo-readiness.md`, `mutation-checklist.md`.
- `CLAUDE.md` — hackathon-mode agent brief: explicit demo-critical read order, a "what's already done, don't rebuild" list, a hard boundary between deterministic services (own mutations) and AI (classify/summarize/draft only, never owns invoice totals or ledger writes), key file map, verification commands, and a step-by-step demo script.
- `AGENTS.md` — present alongside `CLAUDE.md`.
## Verification performed
Both directions and the conflict path tested for real with a throwaway file (`.claude/decisions/_sync_test.md`):
1. Created on the Jarvis-mirror side, synced, confirmed it landed in the real WSL repo.
2. Edited on the WSL repo side, synced, confirmed the edit landed back in the mirror.
3. Edited differently on both sides without syncing in between, synced: Unison reported the conflict and **both edits stayed intact**.
4. Deleted from both sides, synced once more, confirmed a clean no-op.
## Trigger
Live on the 15-minute Windows Scheduled Task `ClaudeKit-Sync-All` as of 2026-08-10 — the fourth and last of this session's project onboardings.

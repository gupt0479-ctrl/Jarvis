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
next: Watch the first few scheduled runs, then apply the same shape to Trading View/Resq/OpsPilot
---
# Portfolio — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is
The live-synced mirror of `~/projects/hub/portfolio` (WSL, git remote `gupta-builds/Portfolio`), Anant's personal portfolio site. Rebuilt clean 2026-08-10 — everything except this Setup.md was deleted and the folder was fully repopulated by a fresh sync, replacing an old flat, hand-copied dump.
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `Portfolio`, `needs_fat: true`. Synced paths: `.claude/agents`, `.claude/commands`, `.claude/docs`, `.claude/CLAUDE.md`, `.claude/cosmic-frontend.mdc`. **Shape note:** unlike every other project here, Portfolio keeps `CLAUDE.md` *inside* `.claude/`, not at repo root — there is no root-level `CLAUDE.md` or `AGENTS.md` in this repo at all, confirmed directly, not assumed from the earlier draft. Not synced: `.claude/settings.local.json` (machine-local) and `.claude/scheduled_tasks.lock` (runtime state, not configuration).
## What's actually here
- `.claude/agents/` — 7 files: `ai-engineer.md`, `eval-runner.md`, `frontend-builder.md`, `sanity-schema.md`, `security-reviewer.md`, `test-runner.md`, `three-artist.md`.
- `.claude/commands/` — 10 files: `add-project.md`, `build-fix.md`, `deploy.md`, `e2e.md`, `eval.md`, `performance.md`, `review.md`, `sanity-push.md`, `ship-check.md`, `typecheck.md`. **This was missing from the original manifest draft** (dropped by mistake when the manifest was first written) — caught and fixed before the first sync ran, not after.
- `.claude/docs/` — `ORBY.md`, `ecc-setup-guide.md`.
- `.claude/CLAUDE.md` — the repo's real operating instructions: exact stack (Next.js 16, Tailwind v4 CSS-first, shadcn/Radix, React Three Fiber, Sanity CMS, Clerk, Biome, pnpm), a full visual-identity spec (color tokens, `.cosmic-card`/`.float-btn` CSS contracts), R3F performance rules, and an explicit forbidden-actions list.
- `.claude/cosmic-frontend.mdc` — a Cursor-style rule file living alongside the Claude config.
## Verification performed
Both directions and the conflict path tested for real with a throwaway file (`.claude/commands/_sync_test.md`):
1. Created on the Jarvis-mirror side, synced, confirmed it landed in the real WSL repo.
2. Edited on the WSL repo side, synced, confirmed the edit landed back in the mirror.
3. Edited differently on both sides without syncing in between, synced: Unison reported the conflict (`CONFLICTS`, exit 1) and **both edits were still intact afterward** — nothing overwritten.
4. Deleted from both sides, synced once more, confirmed a clean no-op.
## Trigger
Live on the 15-minute Windows Scheduled Task `ClaudeKit-Sync-All` as of 2026-08-10 — added to the manifest with `status: live` in the same pass this Setup.md was written, no separate manual-only period like the first three targets had.

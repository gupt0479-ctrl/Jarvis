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
next: Watch the first few scheduled runs after cutover, then apply the same shape to Portfolio/Trading View/Resq/OpsPilot
---
# CausalOps — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is
The live-synced mirror of `~/projects/hub/CausalOps` (WSL, git remote `gupta-builds/CausalOps`), an evidence-backed causal reasoning engine for cyber SOC operations. Rebuilt clean 2026-08-10 — everything except this Setup.md was deleted and the folder was fully repopulated by a fresh sync, replacing an old flat, hand-copied dump (`agents/`, `commands/`, `hooks/` sitting directly in this folder, no nested `.claude/`, plus a stray `scheduled_tasks.lock` and `settings.local.json` that were never meant to be here).
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `CausalOps`, `needs_fat: true` (this pairing genuinely crosses the WSL↔Windows boundary — source is native ext4, mirror is DrvFs). Synced paths: `.claude/agents`, `.claude/commands`, `.claude/hooks`, root `CLAUDE.md`, root `AGENTS.md`. Not synced: `.claude/settings.local.json` (machine-local) and anything outside `.claude/` besides the two root docs.
## What's actually here
- `.claude/agents/` — 3 files: `causal-safeguard-reviewer.md`, `coordinator-expert.md`, `memory-layer-specialist.md`.
- `.claude/commands/` — 4 files: `lint.md`, `memory-test.md`, `smoke.md`, `unit-test.md`.
- `.claude/hooks/` — 3 files: `guard-sacred-files.sh`, `lint-on-edit.sh`, `test-memory-on-edit.sh`.
- `CLAUDE.md` — the project's real operating instructions: an evidence-backed causal reasoning engine (LLM proposes hypotheses, deterministic code falsifies them via DoWhy), currently mid-implementation of a persistent semantic memory layer (Supabase pgvector, temporal decay, a standalone FastMCP server) — status noted in the file itself as complete, 21/21 integration tests passing against a live Supabase project.
- `AGENTS.md` — present, synced alongside `CLAUDE.md` for the first time this session (the earlier manifest draft only carried `CLAUDE.md`).
## Verification performed
Both directions and the conflict path tested for real with a throwaway file (`.claude/commands/_sync_test.md`), matching the same battery already proven on `second-brain-claudekit`:
1. Created a test file on the Jarvis-mirror side, synced, confirmed it landed in the real WSL repo.
2. Edited that file on the WSL repo side, synced, confirmed the edit landed back in the mirror.
3. Edited the same file differently on both sides without syncing in between, then synced: Unison reported `changed <-?-> changed`, exit 1 (`CONFLICTS`), and **both edits were still intact afterward on their respective sides** — nothing silently overwritten.
4. Deleted the test file from both sides, synced once more, confirmed a clean no-op (`OK exit=0`) and a folder containing exactly the 10 real config files plus this Setup.md and `Sync-Log.md`.
## Trigger
Manual only as of 2026-08-10 — runs when `sync-all.sh CausalOps` (or a full `sync-all.sh` run) is invoked by hand. Cutover to the 15-minute Windows Scheduled Task happens once all three of this session's targets are confirmed (see [[20_Progress/AI/Claude Code/Sync - Unison]]).

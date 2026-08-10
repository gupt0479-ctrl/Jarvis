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
next: Watch the first few scheduled runs, then apply the same shape to Resq/OpsPilot
---
# Trading View — Setup
This note is Jarvis-only. It is never read or written by the sync itself — `sync-all.sh` never touches it, it carries no `paths` entry in the manifest. It exists purely to tell a Jarvis reader what's actually in this folder and how it got that way.
## What this is
The live-synced mirror of `~/projects/hub/tradingview` (WSL, git remote `gupta-builds/TradingView`) — despite the folder name, confirmed **not affiliated with TradingView**: a beginner-safe AI market-research desk for learning and disciplined investment reasoning, currently in its Month-1 data-ingestion-foundation phase. Rebuilt clean 2026-08-10, replacing an old flat, hand-copied dump.
## Sync scope
Bidirectional, via `second-brain-claudekit/60_Claude/scripts/sync-all.sh`, manifest entry `Trading View`, `needs_fat: true`. Synced paths: `.claude/agents`, `.claude/hooks`, `.claude/skills`, `.claude/settings.json`, root `CLAUDE.md`, root `AGENTS.md`. No `.claude/commands/` here — confirmed this repo genuinely has none, not a sync gap. Not synced: `.claude/settings.local.json` (machine-local).
## What's actually here
- `.claude/agents/` — 2 files: `guardrail-auditor.md` (reviews diffs against the repo's non-negotiable guardrails: no execution language like BUY/SELL, no fabricated data, confidence always capped by data quality, no LLM calls inside the ingestion path, no secrets, no broker/order-routing code), `spec-implementer.md` (implements the next open `tasks.md` item, flags drift between spec and code).
- `.claude/hooks/block-secrets.sh` — a real guardrail hook.
- `.claude/skills/` — `guardrail-check/SKILL.md` (grep-based sweep for guardrail violations), `kiro-status/SKILL.md` (reconciles `tasks.md` against actual implementation).
- `.claude/settings.json` — Claude Code config for this repo.
- `CLAUDE.md` — the repo's real operating instructions: module map for the `research_data` Python package (OHLCV data fetch → DuckDB storage → quality auditing → AI-consumable evidence packets), explicit non-negotiable guardrails carried over from a `.kiro/specs/` design doc, and the phase roadmap.
- `AGENTS.md` — present alongside `CLAUDE.md`.
## Verification performed
Both directions and the conflict path tested for real with a throwaway file (`.claude/agents/_sync_test.md`):
1. Created on the Jarvis-mirror side, synced, confirmed it landed in the real WSL repo.
2. Edited on the WSL repo side, synced, confirmed the edit landed back in the mirror.
3. Edited differently on both sides without syncing in between, synced: Unison reported the conflict and **both edits stayed intact**, nothing overwritten.
4. Deleted from both sides, synced once more, confirmed a clean no-op.
## Trigger
Live on the 15-minute Windows Scheduled Task `ClaudeKit-Sync-All` as of 2026-08-10.

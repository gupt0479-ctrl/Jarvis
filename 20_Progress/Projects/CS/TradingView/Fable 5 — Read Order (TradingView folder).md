---
type: project
status: active
created: 2026-07-10
updated: '"2026-07-12"'
related_progress: '["[[Phase 3 — AI Brain Hub Landed (2026-07-12)]]", "[[Session
  Findings — AI Brain Hub (2026-07-12)]]", "[[Session Findings — Post Base
  (2026-07-11)]]", "[[Year-Ahead Base — Fable 5 Architecture Contract]]",
  "[[Math-First Map — Existing Code to Factor Brain]]"]'
tags:
  - trading
  - fable-5
track:
  - trading
  - ai
next: '"V1.1 parked (proposer, DuckDB evidence_cards); re-sync 60_Claude
  graphify vault mirror in smaller batches"'
---
# Fable 5 — Read Order (TradingView folder)
==Read these vault notes in order before writing code. Newer Session Findings beat older notes on conflict.==
## Goal
Give Fable 5 a two-minute path into the current base and the AI-hub design pass, without re-deriving either.
## Folder map
`20_Progress/Projects/CS/TradingView/` now holds five subfolders, plain names, no numeric prefixes: **Canon/** (settled architecture and law), **Session Findings/** (dated decision logs, newest wins), **Phases/** (landed-work records), **Research/** (pre-Canon research and product vision), **Archive/** (resolved or superseded, kept for audit trail — never deleted).
## Read order
0. [[Phase 3 — AI Brain Hub Landed (2026-07-12)]] — **current SoT, as-built**; LLM seam merged to `main` (PR #4, `c754f00`); architecture, real NVDA card/critic artifacts, test results, guardrail check, and a found-not-fixed `created_at` provenance gap
1. [[Session Findings — AI Brain Hub (2026-07-12)]] — **current SoT**; AI hub locks A1–G3 + Cursor prereqs landed
2. [[Session Recap — AI Brain Hub Questionnaire (2026-07-12)]] — full Q&A transcript for this session
3. [[Session Findings — Post Base (2026-07-11)]] — prior SoT for ingestion/Phase 2b facts; still valid where AI Brain Hub doesn't override
4. [[Session Findings — Cursor Alignment Pass (2026-07-10)]] — settled law Q&A
5. [[Year-Ahead Base — Fable 5 Architecture Contract]] — base modules (Canon/)
6. [[Phase 2 — Strategy Pack Landed (2026-07-11)]] — pack that Fable shipped (Phases/)
7. [[Math-First Map — Existing Code to Factor Brain]] — keep ingestion clean (Canon/)
8. [[Postmortem - Stocks-ETFs First, Prediction Markets Second]] — PM vertical parked (Canon/)
9. [[Research - Kronos Foundation Model Deep Dive (2026-06-25)]] — reserved only (Research/)
> [!NOTE] Archived, not deleted
> [[History Depth Blocker — Massive Starter Required]] (resolved via Tiingo) and [[Phase 2b — Promotion Study (Draft)]] (superseded) → Archive/ 2026-07-12.
> Fable implementer prompt (repo): `Docs/FABLE5_PHASE3_AI_BRAIN_PROMPT.md`
## Repo
`/home/anant_gupta/projects/hub/tradingview` — `src/research_data/`, `config/`, `.kiro/specs/data-ingestion-foundation/`, `CLAUDE.md`. Mirror architecture into `Docs/YEAR_AHEAD_BASE.md`; mirror the AI-hub design into `Docs/PHASE3_AI_BRAIN_*.md` once F2 closes.
## Next Action
Phase 3 LLM seam is landed and merged (`c754f00`, 2026-07-12) — see [[Phase 3 — AI Brain Hub Landed (2026-07-12)]]. Parked for V1.1: StrategySpec proposer, DuckDB `evidence_cards` (`cards/store.py` build #2). The `60_Claude/40_Project_Briefs/TradingView` graphify vault mirror is stale (a 2026-07-12 bulk-copy attempt was abandoned mid-way after hitting the session usage limit) — re-sync it in a smaller-batch pass before relying on it; the repo copy at `graphify-out/jarvis_curated/` (141 communities / 1,747 nodes) is current.

---
type: project
status: active
created: 2026-07-10
updated: 2026-07-12
related_progress:
  - "[[Session Findings — AI Brain Hub (2026-07-12)]]"
  - "[[Session Findings — Post Base (2026-07-11)]]"
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Math-First Map — Existing Code to Factor Brain]]"
tags:
  - trading
  - fable-5
track:
  - trading
  - ai
next: "Cursor: close G1-G3, then write the Fable 5 AI-hub implementer prompt"
---
# Fable 5 — Read Order (TradingView folder)
==Read these vault notes in order before writing code. Newer Session Findings beat older notes on conflict.==
## Goal
Give Fable 5 a two-minute path into the current base and the AI-hub design pass, without re-deriving either.
## Folder map
`20_Progress/Projects/CS/TradingView/` now holds five subfolders, plain names, no numeric prefixes: **Canon/** (settled architecture and law), **Session Findings/** (dated decision logs, newest wins), **Phases/** (landed-work records), **Research/** (pre-Canon research and product vision), **Archive/** (resolved or superseded, kept for audit trail — never deleted).
## Read order
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
G1–G3 (Cursor vs Fable split, Fable one-shot scope, explicit non-goals) are still open in [[Session Findings — AI Brain Hub (2026-07-12)]]. Once closed, write the Fable 5 implementer prompt for the AI hub (`cards/` + `agents/` packages, per that note's Block F module map).
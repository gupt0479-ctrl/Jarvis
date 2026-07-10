---
type: project
status: active
created: 2026-07-10
updated: 2026-07-10
related_progress:
  - "[[Session Findings — Cursor Alignment Pass (2026-07-10)]]"
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Math-First Map — Existing Code to Factor Brain]]"
tags:
  - trading
  - fable-5
track:
  - trading
  - ai
next: "Fable 5: read this list in order, then execute Year-Ahead Base contract"
---
# Fable 5 — Read Order (TradingView folder)

==Read these vault notes in order before writing code. Cursor session findings beat older notes on conflict.==

## Goal
Give Fable 5 a two-minute path into the year-ahead base without re-deriving the alignment pass.

## Read order
1. [[Session Findings — Cursor Alignment Pass (2026-07-10)]] — every Q&A, ambition raise, how we avoid the student-toy failure, confidence gate
2. [[Year-Ahead Base — Fable 5 Architecture Contract]] — in-scope build, out-of-scope Cursor leftovers, Definition of Done
3. [[Math-First Map — Existing Code to Factor Brain]] — do not pollute ingestion modules; package layout; math inventory; leftover ordered list
4. [[Postmortem - Stocks-ETFs First, Prediction Markets Second]] — sequencing + failure modes (zero PM code now)
5. [[AI Market Analyzer - Strategy Engine]] — factor modules + score packet shape
6. [[Research - Systematic Equity Strategy Edge (2026-06-25)]] — why factors beat checklist folklore
7. [[Research - Kronos Foundation Model Deep Dive (2026-06-25)]] — deferral / RankIC gate only
8. [[RESEARCH]] — product thesis, autonomy ladder, journal contracts (patched 2026-07-10)

*Optional context:* [[Trading Resources Integration — TradingView Architecture Roadmap]] — borrow process ideas; **ignore** any pressure to build Polymarket/Kalshi in this phase.

## Repo
`/home/anant_gupta/projects/hub/tradingview` — `src/research_data/`, `config/`, `.kiro/specs/data-ingestion-foundation/`, `CLAUDE.md`. Mirror architecture into `Docs/YEAR_AHEAD_BASE.md`.

## Next Action
Execute [[Year-Ahead Base — Fable 5 Architecture Contract]] end-to-end.

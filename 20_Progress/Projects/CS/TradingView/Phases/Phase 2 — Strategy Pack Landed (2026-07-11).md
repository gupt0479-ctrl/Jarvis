---
type: project
status: active
created: 2026-07-11
updated: 2026-07-11
related_progress:
  - "[[Session Findings — Post Base (2026-07-11)]]"
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Phase 2b — Promotion Study (Draft)]]"
tags:
  - trading
  - phase2
  - strategy
track:
  - trading
  - ai
next: "Unblock history depth → Phase 2b promotion study"
---
# Phase 2 — Strategy Pack Landed (2026-07-11)

==Fable 5 completed the Phase 2 one-shot: first production strategy pack through the four gates (offline proof + live study runner).==

## What landed
- Package: `src/research_data/strategies/quality_momentum.py`
- Hook: `research_data.strategies.quality_momentum:quality_momentum_tilt_hook`
- Formula: 50/50 momentum 12-1 percentile + quality_fcf composite; top-K=3; rebalance every 21 sessions; 90d fundamentals lag; ETFs never selectable
- Citations: Jegadeesh-Titman 1993, Novy-Marx 2013, AFP 2019; gates cite Pardo / Bailey-LdP (unchanged defaults)
- Runner: `scripts/run_quality_momentum_study.py` (no network; reads DuckDB; records brain gates + paper journal)
- Docs: `Docs/PHASE2_STRATEGY_PACK.md`; lessons in `Docs/fable5_run_memory.md`
- Tests: production closed-loop + strategy tests (CI offline)

## Live study result (Basic depth — expected fail-closed)
- ~274→501 sessions available; after warm-up only ~21–248 strategy sessions depending on window
- OOS gate failed closed on thin data; later gates not run
- Not demo-eligible
- Journal wrote honest vs-VOO figures (strategy lagged VOO in the short window)
- **This is correct behavior** — proof over narrative

## What Phase 2 did *not* claim
- Demo-eligibility on live data
- Walk-forward pass on free-tier history
- Kronos, UI, multi-agent, orchestration CLI

## Graphify (post-land)
Rebuilt 2026-07-11 against current repo. God nodes include `OHLCVRecord`, `BrainStore`, `PriceReadAPI`, `FactorEngine`, brain loop. Phase 2 pack + four gates appear in doc communities. Full report: repo `graphify-out/GRAPH_REPORT.md`.

## Next
[[History Depth Blocker — Massive Starter Required]] then [[Phase 2b — Promotion Study (Draft)]].

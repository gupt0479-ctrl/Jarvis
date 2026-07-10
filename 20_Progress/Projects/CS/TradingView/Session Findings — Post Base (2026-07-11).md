---
type: decision-log
status: active
created: 2026-07-11
updated: 2026-07-11
related_progress:
  - "[[Session Findings — Cursor Alignment Pass (2026-07-10)]]"
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Phase 2 — Strategy Pack Landed (2026-07-11)]]"
  - "[[History Depth Blocker — Massive Starter Required]]"
  - "[[Phase 2b — Promotion Study (Draft)]]"
tags:
  - trading
  - architecture
  - decision
  - session
track:
  - trading
  - ai
next: "Upgrade Massive to Starter+ → deepen DuckDB ≥1135 sessions → Phase 2b promotion study one-shot"
---
# Session Findings — Post Base (2026-07-11)

==This note is the source of truth after the year-ahead base + Phase 2 strategy pack landed.== When it conflicts with [[Session Findings — Cursor Alignment Pass (2026-07-10)]], **this file wins** for current state. Older alignment Q&A remains valid settled law unless explicitly superseded here.

## Goal
Capture what is actually true in the repo after Fable 5 Phase 2 and the Cursor history/graphify/vault pass — so the next agent does not treat pre-shakeout checkboxes as current.

## Current repo truth (measured)

| Layer | State |
|---|---|
| Year-ahead base | On `main` (CI green). Brain, factors, fundamentals, gates, paper, Kronos reserved. |
| Phase 2 strategy pack | Branch `feat/quality-momentum-strategy-pack` commit `f6f26c6`. Production hook `research_data.strategies.quality_momentum:quality_momentum_tilt_hook`. Offline four-gate capability proven on synthetic 1300 sessions. |
| Live study (Basic history) | Ran: ~21 strategy sessions after 253 warm-up; OOS fail-closed; not demo-eligible; journal wrote honest vs-VOO numbers. |
| DuckDB OHLCV after max Basic deepen | **501 sessions/symbol** (2024-07-10 → 2026-07-09). Still below default WF floor. |
| Massive plan on current key | **Basic** — probes requesting 2021+ silently truncate to first bar 2024-07-10. |
| Graphify | Rebuilt 2026-07-11: ~1844 nodes, 3631 edges, 124 communities. See repo `graphify-out/GRAPH_REPORT.md`. |
| Cursor tooling | `.cursor/rules/`, `.cursor/agents/`, root `AGENTS.md` added (was empty). |

## Settled law (unchanged)
Personal desk; stocks/ETFs only; Python owns facts; action vocab; four gates literature defaults; Kronos reserved until RankIC; approver `anant`; universe 14; no PM; no execution language.

## New locks from 2026-07-11 questionnaire + Fable land
1. Desk-is-real bar = **gated historical replay + journal vs VOO**, not "module exists" and not UI.
2. Kronos = permanent optional evidence slot; RankIC only after a factor path is proven through gates on real data.
3. Next hardest Fable one-shot = **Phase 2b**: same production pack, deep history, all four gates, demo-eligible, replay journal vs VOO.
4. Do **not** loosen gate constants to fit free-tier depth.
5. Cursor owns keys/ingest/plumbing; Fable reserved for the hard promotion-study one-shot after deepen.
6. Composite = momentum + quality 50/50 (Fable chose; safety not a hard filter) — leave unless Phase 2b evidence says otherwise.

## Math that blocks Phase 2b until paid history
Default WF: train 504 / test 126 / step 126 / min_windows 3 → ≥882 strategy-return sessions. Plus momentum warm-up 253 → **≥ ~1135 OHLCV sessions** (~4.5y). Target window `2021-01-01 → today`. Massive **Starter $29/mo (5y)** is the minimum plan; Basic is insufficient.

## Open (actionable)
- [ ] Upgrade Massive to Starter+ and put key in `.env` (`POLYGON_API_KEY`)
- [ ] `python scripts/deepen_history.py --start-date 2021-01-01` until DuckDB VOO n ≥ 1135
- [ ] Refresh fundamentals for the longer window (one source per symbol)
- [ ] Phase 2b promotion study one-shot (Fable 5) — see [[Phase 2b — Promotion Study (Draft)]]
- [ ] Merge `feat/quality-momentum-strategy-pack` to `main` via PR when ready
- [ ] Vault folder hygiene: Canon / Research / Phases banners (incremental; do not delete unsure notes)

## Explicitly deferred
Kronos RankIC; analyst/critic agents; UI/charting; full orchestration CLI; real-money; PM vertical.

## Related
- [[Phase 2 — Strategy Pack Landed (2026-07-11)]]
- [[History Depth Blocker — Massive Starter Required]]
- [[Phase 2b — Promotion Study (Draft)]]
- Repo: `Docs/PHASE2_STRATEGY_PACK.md`, `Docs/HISTORY_DEPTH.md`, `AGENTS.md`

---
type: project
status: active
created: 2026-07-11
updated: 2026-07-11
related_progress:
  - "[[Session Findings — Post Base (2026-07-11)]]"
  - "[[Phase 2b — Promotion Study (Draft)]]"
tags:
  - trading
  - data
  - blocker
track:
  - trading
  - ai
next: "Upgrade Massive Starter → run scripts/deepen_history.py --start-date 2021-01-01"
---
# History Depth Blocker — Massive Starter Required

==Phase 2b cannot start until DuckDB has enough sessions for default walk-forward. Gate constants stay frozen.==

## Requirement (do not change gates)
| Item | Value |
|---|---|
| WF train / test / step / min_windows | 504 / 126 / 126 / 3 |
| Min strategy-return length | 882 sessions |
| Momentum warm-up | 253 sessions |
| Min OHLCV sessions/symbol | **≥ ~1135** (~4.5 trading years) |
| Target ingest start | `2021-01-01` |

## Measured 2026-07-11
| Step | Result |
|---|---|
| Pre-deepen | 274 sessions (2025-06-05 → 2026-07-09) |
| Max Basic ingest | **501 sessions** (2024-07-10 → 2026-07-09) |
| Probe 2021-01-01 → today | Truncates to first bar **2024-07-10** |
| Plan on current `POLYGON_API_KEY` | Massive **Basic** (2y) |

## Fix
1. Upgrade to [Massive Stocks Starter](https://massive.com/pricing) ($29/mo, 5y history) or higher.
2. Keep using `POLYGON_API_KEY` in `.env` (or `MASSIVE_API_KEY`).
3. From repo:
```bash
source .venv/bin/activate
python scripts/deepen_history.py --probe-only --start-date 2021-01-01
# expect: VERDICT: depth sufficient
python scripts/deepen_history.py --start-date 2021-01-01
```
4. Confirm DuckDB: `SELECT COUNT(*) FROM daily_ohlcv WHERE symbol='VOO'` ≥ 1135.
5. Refresh fundamentals for the longer window (SEC preferred for depth; one source per symbol).

## Anti-patterns
- Loosening `WalkForwardParams` / `OOSParams` to pass on 501 bars
- Fabricating history
- Burning Fable 5 quota on the deepen chore — this is a Cursor/ops task

Repo mirror: `Docs/HISTORY_DEPTH.md`, `scripts/deepen_history.py`.

---
type: concept
status: sprout
created: 2026-07-10
updated: 2026-07-10
related_progress:
  - "[[Year-Ahead Base — Fable 5 Architecture Contract]]"
  - "[[Session Findings — Cursor Alignment Pass (2026-07-10)]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
tags:
  - trading
  - architecture
  - math-first
track:
  - trading
  - ai
---
# Math-First Map — Existing Code to Factor Brain

==Math-first means every new trading claim in this repo is a typed computation with provenance and a test that can kill it — existing `research_data` files stay the data spine, not a junk drawer for strategy logic.==

*Reader:* Fable 5 and Cursor agents touching `src/research_data/`.

## Goal
Map what already exists, what must not be polluted, what Fable 5 adds, and what remains — so the codebase stays the easiest professional tree to navigate a year from now.

## Principle
```text
providers / raw / normalize / quality / read_api
        → factor scorers (deterministic math)
        → four-gate harness (kill tests)
        → brain (citations, specs, promote/demote, journal links)
        → paper contracts
        → (later) agents explain packets only
```
AI never writes numbers into `daily_ohlcv`. Strategy code never lives inside `storage.py` or `quality.py`.

## Existing Modules — Keep Clean
| File | Responsibility today | Math-first rule |
|---|---|---|
| `models.py` | OHLCV, quality enums, `DataEvidencePacket` shape | Add strategy/brain models in **new** modules or clearly named model files — do not turn `OHLCVRecord` into a strategy bag |
| `config.py` | TOML load, API key env validation | New fundamentals providers get toml entries + `*_API_KEY` / `SEC_USER_AGENT`; no hardcoded secrets |
| `storage.py` | DuckDB schema, raw payloads, upserts, redaction | New tables for brain/tests/journal — separate from `daily_ohlcv` PK |
| `normalization.py` | Provider → OHLCVRecord | Prices only; no factor scores here |
| `calendar.py` | NYSE/NASDAQ sessions | Shared by quality, factors (trading-day math), gates |
| `quality.py` | MISSING>…>USABLE, confidence_cap | Caps **all** downstream confidence; do not overload CONTRADICTORY for PM spreads (PM deferred) |
| `read_api.py` | `get_price_frame` | Sole read path for factor inputs from prices; `require_usable` before scoring |
| `providers/base.py` | Registry + protocol | New FMP/SEC clients implement protocol; csv_fixture remains offline default |
| `providers/csv_fixture.py` | Deterministic tests | Keep as CI backbone when live keys fail |

> [!WARNING]
> Do not “just add a column” to `daily_ohlcv` for momentum or FCF. Scores are derived artifacts with their own as_of and inputs.

## What Fable 5 Adds (new packages, navigable names)
Suggested layout (adjust only if clearer — document in `Docs/YEAR_AHEAD_BASE.md`):
```text
src/research_data/
  brain/           # citations, specs, test runs, promote/demote, journal links
  factors/         # momentum, safety, quality_fcf, valuation, etf_baseline, ta_context
  fundamentals/    # FMP + SEC fetch/normalize for statements/ratios
  gates/           # oos, monte_carlo, walk_forward, deflated_sharpe, eligibility
  paper/           # thesis approval, timed entry, replay journal, live book hooks
```
Each package: `README` or module docstring stating inputs/outputs; tests under `tests/` mirroring package names (`test_factors_momentum.py`, etc.).

## Math Inventory (must be explicit in code + docs)
| Signal | Formula intent | Inputs | Kill condition |
|---|---|---|---|
| Momentum | 12-1 month total return rank in universe | usable daily closes | insufficient history → no rank / INSUFFICIENT_DATA |
| Safety | inverse rank of 12m realized vol | usable daily returns | same |
| Quality/FCF | composite incl. FCF/EV, FCF margin, margin stability, debt | fundamentals + prices | missing FCF/EV → cap confidence; no fabricated FCF |
| Valuation | FCF/EV primary; sector caveats | fundamentals | no cross-sector raw P/E as sole driver |
| ETF baseline | compare idea vs VOO overlapping sessions | prices | refuse if stale/missing per quality |
| TA context | MA/RSI/Bollinger descriptive | prices | never sole action driver |
| Gate: OOS | holdout performance | strategy returns | fail → not demo-eligible |
| Gate: Monte Carlo | path/resampling stress | returns | fail → not demo-eligible |
| Gate: Walk-forward | rolling train/test | returns + params | fail → not demo-eligible |
| Gate: Deflated Sharpe | selection-bias-aware Sharpe | returns + trial count | fail → not demo-eligible |

Kronos: **schema reservation only** — see Session Findings.

## Still Left and Necessary (ordered)

### A — Fable 5 hard slice (now)
==Done 2026-07-10 (Fable 5).== All seven items landed with tests:
1. [x] Brain persistence + closed-loop APIs (`brain/models|store|loop`) — human-gated approve/promote, gate-order enforcement
2. [x] Factor scorers + `ScorePacket`s (`factors/`) — formulas, windows, INSUFFICIENT_DATA kill-paths
3. [x] Minimal FMP/SEC fundamentals path (`fundamentals/`) — pure parsers, fail-closed live clients, DuckDB store
4. [x] Four-gate harness + eligibility (`gates/`) — OOS/MC/WF/DSR, short-circuit, recorded to brain
5. [x] Paper-test contracts (`paper/`) — approve → timed entry; replay journal-as-if-time-passed; live-book review hooks
6. [x] Vault + `Docs/YEAR_AHEAD_BASE.md` mirror
7. [x] Kronos reserved fields/docs only (`kronos_reserved.py`)

### B — Cursor next (plumbing, not the hard product problem)
==Done 2026-07-10 (Cursor).== All `.kiro` data-ingestion-foundation tasks are checked (60/60):
1. [x] Quality tests 7.2–7.4
2. [x] `evidence.py` builder (`DataEvidencePacket` for downstream agents)
3. [x] `benchmark.py` reporter (refuses execution language)
4. [x] `providers/polygon.py` with rate limiting + retry/backoff
5. [x] CLI (`init-db`, `ingest-prices`, `audit-prices`, `benchmark`) + property tests
6. [x] Scope/security checks (task 13, `tests/test_security_scope.py`)

Full offline suite after both slices: **420 tests passing**. Section C below remains the future queue.

### C — After base proves itself (not this handoff)
1. Multi-agent debate layer consuming packets only
2. Streamlit (or chosen) UI: watchlist, evidence feed, approve queue, charts/indicators
3. Kronos RankIC validation → optional evidence input
4. Autonomy ladder level-3 experiments only with journal evidence
5. Real-money instructions surface + TradingView.com as execution record
6. Kalshi/Polymarket vertical — **only** after stocks paper readiness (Postmortem)

## Professionalism Checklist (every PR / Fable commit)
- [ ] New code in the right package — no strategy logic in ingestion files
- [ ] Types + provenance fields on derived artifacts
- [ ] Offline test path green without network
- [ ] No secrets in fixtures/logs
- [ ] No BUY/SELL/guaranteed language
- [ ] Module map in Docs updated if files added
- [ ] Promote/demote or gate failure is representable (not silent)

## Related Notes
- [[Year-Ahead Base — Fable 5 Architecture Contract]]
- [[Session Findings — Cursor Alignment Pass (2026-07-10)]]
- [[Postmortem - Stocks-ETFs First, Prediction Markets Second]]

---
type: project
status: active
created: 2026-07-10
updated: 2026-07-10
related_progress:
  - "[[Session Findings — Cursor Alignment Pass (2026-07-10)]]"
  - "[[Math-First Map — Existing Code to Factor Brain]]"
  - "[[RESEARCH]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[Postmortem - Stocks-ETFs First, Prediction Markets Second]]"
tags:
  - trading
  - architecture
  - fable-5
track:
  - trading
  - ai
next: "Fable 5 implements this contract; mirror into Docs/YEAR_AHEAD_BASE.md in-repo"
---
# Year-Ahead Base — Fable 5 Architecture Contract

==One-sentence goal: leave a durable base for TradingView a year from now — brain loop, factor(+fundamentals) math, four-gate promotion, paper-test contracts, Kronos reserved — not a disposable demo.==

*Primary reader:* Fable 5 executing the hard slice. *Secondary:* future-Anant auditing whether the base still matches intent.

## Goal
Ship the **year-ahead structural base** of the personal stocks/ETFs desk: real persistence, real formulas, real kill-tests, navigable modules — so later UI/agents/PM vertical sit on rock, not on student scaffolding.

## Current State
- ==Base executed (2026-07-10)==: Fable 5 landed the hard slice; Cursor completed the `.kiro` ingestion plumbing (all 60 spec tasks checked). Full offline suite: **420 tests passing**.
- In repo now: `brain/` (closed loop — citations, specs, human-gated approve, test runs, promote/demote, journal links), `factors/` (momentum 12-1, safety/vol, quality_fcf, valuation FCF/EV, ETF baseline vs VOO, TA context-only → `ScorePacket`), `fundamentals/` (FMP + SEC EDGAR parsers/clients/store, provenance on every field, offline fixtures), `gates/` (OOS → Monte Carlo → walk-forward → deflated Sharpe; costs, drawdown, trade count, vs-VOO; fail-closed on thin data), `paper/` (pre-approved theses, timed auto-entry in windows, replay journal-as-if-time-passed, live-book review jump-ahead hooks, `voo_return_same_period` required on exits), `kronos_reserved.py` (schema + USABLE/RankIC≥0.03 admission gates, zero inference).
- Cursor's `.kiro` completions: `evidence.py`, `benchmark.py` (refuses execution language), `cli.py` (`init-db`, `ingest-prices`, `audit-prices`, `benchmark`), `providers/polygon.py`, quality/property tests, scope/security checks.
- Universe expanded to 14 symbols; canonical letters-only `BRKB` stands for BRK.B (providers map their own punctuation).
- Contract mirrored in-repo at `Docs/YEAR_AHEAD_BASE.md`; build lessons in `Docs/fable5_run_memory.md`.
- `.env` (gitignored) holds `POLYGON_API_KEY`, `FMP_API_KEY`, `SEC_USER_AGENT`; `research_data.env.load_dotenv()` loads it without echoing values.

## What Fable 5 Builds (in scope)

### 1. Design notes (vault + repo mirror)
*Vault:* patch/extend under `20_Progress/Projects/CS/TradingView/` (preserve frontmatter keys).
*Repo mirror:* `Docs/YEAR_AHEAD_BASE.md` so the codebase carries the contract without vault access.
*Forbidden:* edits under `60_Claude/40_Project_Briefs/TradingView/` (graphify output).

### 2. Brain module (x-factor = closed loop)
Implement under something like `src/research_data/brain/` with clear public APIs and tests:
- **citation / research items** — source, retrieved_at, claims, links
- **strategy specs** — `proposed` | `approved`; human gate required to advance
- **test-run records** — gate name, inputs, outputs, pass/fail, as_of
- **promote / demote decisions** — what changed, why, evidence refs
- **links to paper-journal entries**
==Closed loop (non-negotiable):== citation → proposed spec → human approve → Python implementation hook → four gates → promote/demote → journal lesson → next proposal.
AI may propose specs; Python implements only approved specs. Fixed factors improve via promote/demote from tests.

### 3. Factor engine (primary math)
Deterministic scorers → structured score packets (see [[AI Market Analyzer - Strategy Engine]] + [[Research - Systematic Equity Strategy Edge (2026-06-25)]]):
- `momentum_score` — 12-1 month return rank in universe
- `safety_score` — inverse rank of 12m realized vol
- `quality_fcf_score` / valuation — FCF/EV weighted; margins; debt
- ETF baseline vs **VOO**
- TA (MA/RSI/Bollinger) as **context fields only** — never sole `action_hint` drivers
Universe: expand `config/assets.toml` to RESEARCH 14 if needed (VOO VTI SPY QQQ AAPL MSFT NVDA AMZN GOOGL META BRK.B JPM COST TSLA).

### 4. Minimal fundamentals path
FMP + SEC EDGAR sufficient for FCF, margins, debt, EV.
- Provenance on every field; no fabrication; secrets redacted.
- `SEC_USER_AGENT` on every SEC request; respect fair-access rate limits.
- Fixtures for offline tests; live clients when keys work.

### 5. Four-gate promotion harness
Order fixed; all must pass before demo-paper eligibility:
1. Out-of-sample screening
2. Monte Carlo
3. Walk-forward
4. Deflated Sharpe
Always vs VOO/buy-and-hold; include costs, drawdown, trade count; no lookahead; literature defaults over curve-fit.

### 6. Paper-test contracts
- Pre-approve thesis → timed auto paper entry in test windows
- Accelerated historical replay writing journal-as-if-time-passed (research verification)
- Live calendar paper book with review jump-ahead hooks
UI may be thin; storage/APIs must be real and navigable.

### 7. Kronos (architecture only)
Reserve evidence fields + gates (`USABLE` only, RankIC threshold, no action from forecast alone). **No inference** in this handoff.

## Out of Scope (Cursor next — do not burn Fable quota)
- Quality property/unit tests 7.2–7.4
- `evidence.py` builder, `benchmark.py`, full `cli.py` wiring, leftover task-9–13 cosmetics
- Kalshi/Polymarket anything
- Real-money brokers, auth, multi-tenancy
- Kronos model download/inference
Use existing `PriceReadAPI` / DuckDB / `csv_fixture`; implement live Polygon only if required to unblock and kept small.

## Navigation / professionalism rules (codebase must stay clean)
> [!TIP]
> A year from now, a cold reader should find any concern in under two minutes: package map → one module → one test file.

1. **One responsibility per module** — brain ≠ factors ≠ gates ≠ providers.
2. **No god-objects** — do not extend `OHLCVRecord` with strategy or PM fields.
3. **Public API surface thin** — `__init__.py` exports only stable types/functions.
4. **Tests beside behavior** — every new scorer/gate/brain write path has unit or property coverage; offline by default.
5. **Docs mirror code** — `Docs/YEAR_AHEAD_BASE.md` module map stays accurate when files move.
6. **No secrets in repo** — `.env` gitignored; redact stored request metadata.
7. **Graphify later** — regenerate briefs after the base lands; do not hand-edit graphify trees.

## How This Avoids the Student-Toy Failure
| Student-toy pattern | Year-ahead base response |
|---|---|
| Dashboard before math | Factors + gates before polish UI |
| AI chat as “strategy” | AI proposes; Python + tests decide eligibility |
| Untested indicators as edge | Factor filter + four gates |
| Messy catch-all packages | Explicit `brain/`, factors, gates, fundamentals |
| “It backtested once” | Deflated Sharpe + OOS + walk-forward + Monte Carlo |
| Premature multi-asset | Stocks/ETFs only until paper proven |

## Definition of Done (Fable 5)
All met 2026-07-10 (verified against `pytest` output, 420 passing):
- [x] Vault notes under this folder updated to match what was built
- [x] `Docs/YEAR_AHEAD_BASE.md` exists and matches code
- [x] Brain loop persists and is tested (incl. full closed-loop integration test `tests/test_closed_loop.py`)
- [x] Factor(+fundamentals) path produces score packets on fixture data (live keys pending shakeout)
- [x] Four gates runnable with pass/fail records (fail-closed, recorded in brain, never silent)
- [x] Paper-test contracts stored (thesis gate, timed entry, replay + live modes; UI intentionally absent)
- [x] Kronos reserved only (no inference imports — enforced by test)
- [x] Honest report delivered: what passed, leftovers, risks

## Next Action
Contract executed end-to-end (2026-07-10). Next phase (new handoff, not this contract): live-data shakeout with real keys (polygon prices, FMP/SEC fundamentals into the stores), first real replay studies on the 14-symbol universe, then charting/UI choice and the agent layer consuming `ScorePacket`s. Kronos stays reserved until a RankIC validation pass on this universe.

## Open Questions
- [ ] Confirm charting library for in-app indicators after base APIs exist
- [ ] When to expand beyond 14 symbols (only after RankIC/journal evidence, not before)
- [ ] LLM provider for live “propose spec” calls vs human-authored proposals stored in brain

## Related Notes
- [[Session Findings — Cursor Alignment Pass (2026-07-10)]]
- [[Math-First Map — Existing Code to Factor Brain]]
- [[Research - Systematic Equity Strategy Edge (2026-06-25)]]
- [[Research - Kronos Foundation Model Deep Dive (2026-06-25)]]

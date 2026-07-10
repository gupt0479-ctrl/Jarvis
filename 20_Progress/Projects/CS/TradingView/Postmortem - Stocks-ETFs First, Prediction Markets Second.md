---
type: decision-log
status: active
created: 2026-06-25
updated: 2026-07-10
related_progress:
  - "[[RESEARCH]]"
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[AI Market Analyzer - 4 Month Build Plan]]"
tags:
  - trading
  - architecture
  - postmortem
  - decision
track:
  - trading
  - ai
---

# Postmortem — Stocks/ETFs First, Prediction Markets Second

This note is the single source of truth for the sequencing decision made on 2026-06-25, after a two-session review: one pass by Claude (desktop/cowork session, with vault access) auditing drift across this project's notes and the `research_data` codebase, and a second pass (Claude Code, WSL session, with direct repo access) giving a critical second opinion focused on failure modes of merging stocks/ETFs and prediction markets into one product. Treat this as the decision record that future sessions should read before re-opening the "should we merge these" question.

## Verified Repo State (as of 2026-06-25, read directly from `/home/anant_gupta/projects/hub/tradingview`)
Earlier notes in this vault (`RESEARCH.md`) were written from a Windows-side session that could not reach the WSL path and so could not verify the actual codebase. This section corrects that — verified directly against `.kiro/specs/data-ingestion-foundation/tasks.md` and the `src/research_data/` tree:

- **Done (tasks 1–6):** project structure, config loading, Pydantic models (`OHLCVRecord`, `QualityStatus`, `PriceAdjustment`), DuckDB schema + storage layer, provider registry, CSV fixture provider, raw payload writer with hashing/redaction, normalizer, market calendar. All with property tests.
- **Partial (task 7):** `quality.py` (the `DataQualityAuditor`) is implemented, but its property tests and unit tests (7.2–7.4) are not written yet.
- **Drifted checkbox state:** `read_api.py` already exists on disk, but `tasks.md` still marks task 9.1 as not started. The task list is stale relative to the code — needs reconciliation (see `kiro-status` skill in this repo) before more building happens.
- **Not started at all:** evidence packet builder (`evidence.py`), benchmark reporter (`benchmark.py`), Polygon provider (`polygon.py`), CLI (`cli.py`). No strategy engine, no agent layer, no journal, no UI exist anywhere in code.
- **Net assessment:** roughly the bottom third of the stocks/ETFs vertical (data plumbing) is solid. The part that actually produces a trading decision — strategy engine, evidence cards, agent debate, paper-trade journal — is 0% built. Nothing for prediction markets exists in code, by design.

**2026-07-10 re-check (Cursor alignment session):** same shape confirmed — `quality.py` + `read_api.py` present; still no `evidence.py` / `benchmark.py` / `polygon.py` / `cli.py`; strategy/brain/gates still absent. Session SoT: [[Session Findings — Cursor Alignment Pass (2026-07-10)]]. Year-ahead hard slice handed to Fable 5 per [[Year-Ahead Base — Fable 5 Architecture Contract]]; leftover `.kiro` plumbing stays Cursor-next, not Fable.

## Decision
1. **Build the stocks/ETFs vertical completely first.** Finish `.kiro` tasks 7–13 (Cursor owns easy leftovers), then build the strategy engine → evidence card → agent debate → staged paper trade → journal loop described in `[[RESEARCH]]`. Hard slice for 2026-07-10: brain + factor math + fundamentals + four-gate harness + paper contracts — see [[Year-Ahead Base — Fable 5 Architecture Contract]].
2. **Prediction markets become a second, separate vertical later — not a parallel build from day one.** In the final product it should feel like a separate page/division of the same app (own nav, own data, own risk model), not a feature bolted into the stock engine.
3. **Refinement on timing (confirmed 2026-07-10):** **no vertical-2 code at all** until stocks/ETFs paper trading is online, being tested, and verified ready for real-use readiness. **Zero shared-core / PM schema placeholders** until then. Paper-testing downtime may fund vertical-2 *design reading* only — not PM tables in the stocks engine.
4. **Residual risk to track, not ignore:** starting vertical 2's architecture before vertical 1's paper-trading loop has produced real feedback means the "shared core" (provenance pattern, evidence-packet contract, agent orchestration) gets generalized from theory, not from lived experience. Re-check the shared core's shape after the first few weeks of real paper-trade journal entries exist, and be willing to refactor it.
5. **Current focus stays on stocks/ETFs research depth, not prediction markets.** Prediction markets and Kronos are noted and deferred, not forgotten — Kronos is architecture-reserved only until RankIC validation (Session Findings).

## Why Sequencing, Not One Unified Engine

The instinct to build "one product" is right at the company/app level, wrong at the engine level. Multi-asset platforms share a thin platform core and run separate engines per asset class — they don't run one undifferentiated model across asset classes. Concretely:

**Genuinely shared (build once, reuse):**
- Provenance discipline: raw-payload-before-normalized, hash-keyed storage, secret redaction, "missing data surfaces as MISSING, never fabricated."
- Evidence-packet contract: agents only consume timestamped evidence, never invent numbers.
- Agent/critic orchestration pattern (data auditor → analysts → bull/bear debate → risk manager → trader).
- Ledger/journal *infrastructure* (schema, UI) — but not the same ledger/bankroll, see failure mode 5 below.

**Not shared — forcing it breaks correctness, not just style:**
- Quality semantics: `quality.py`'s precedence (`MISSING > CONTRADICTORY > STALE > INSUFFICIENT_DATA > PARTIAL > USABLE`) was built around provider disagreement on one objective price. Two prediction-market venues quoting different odds on the same event isn't a data defect — it's the actual signal (spread/arbitrage). Reusing `CONTRADICTORY` here mislabels a real edge as a data error.
- Risk model: drawdown/Sharpe/position-sizing (continuous returns) vs. Kelly criterion/bankroll management (binary, resolves, all-or-nothing). No honest shared abstraction exists without crippling one side.
- Action vocabulary: `ACCUMULATE`/`REDUCE` imply scaling a position gradually. A binary contract near resolution doesn't "reduce" the way a stock position does. Reusing the enum literally produces output that sounds coherent but means something subtly wrong about applicability — a fabrication-adjacent failure even with no invented number.
- Provider config shape: `providers.toml` fields (`rate_limit`, `adjustment_policy`, `license_note`) assume a stable, regulated price vendor. Prediction-market providers have a risk category with no field anywhere in the current schema: **resolution-criteria ambiguity** — arguably the single biggest real-world risk in event markets.
- Regulatory posture: securities (SEC-adjacent) vs. event contracts (CFTC-adjacent for Kalshi; contested/offshore for Polymarket with US persons). One app touching both raises the compliance bar non-linearly the moment it's shared with anyone else, demoed, or monetized.

## Failure Modes (the ones we are explicitly designing against)

| # | Failure mode | What it looks like | Mitigation |
|---|---|---|---|
| 1 | God-object schema | One `Asset`/`OHLCVRecord`-like table grows nullable fields (`resolution_date`, `implied_probability`, `binary_outcome`) empty 90% of the time depending on asset class | Separate tables/models per vertical; share only the provenance/evidence-packet base contract |
| 2 | Mislabeled signal as noise | Quality auditor reused naively flags healthy cross-venue spread as `CONTRADICTORY`, confidence-capping a real edge into invisibility | Write a dedicated prediction-market quality auditor when that vertical starts; do not extend `quality.py`'s enum to mean two things |
| 3 | Guardrail erosion by side door | Event markets resolving in hours, with all-or-nothing payoffs, quietly reintroduce the intraday/leverage-like exposure this project's guardrails exclude | Write an explicit guardrails addendum for the prediction-market vertical before any code starts there; do not assume the stocks guardrails cover it |
| 4 | Testing combinatorics doubled too early | OHLC invariants (`high >= low`) don't transfer to market invariants (probability ∈ [0,1], no-arbitrage across outcomes) — two full property-test suites maintained before either vertical ships | Don't start prediction-market property tests until that vertical's data model is even drafted |
| 5 | Ledger cross-contamination | Shared bankroll/journal lets a losing streak in fast-resolving prediction markets bleed into slower stock conviction (panic overrides, revenge sizing) | Separate books/ledgers by construction even when both verticals live in one app and share UI chrome |
| 6 | Sunk-cost retrofitting | "DuckDB already works, just add a table" used as if it were evidence the schema fits prediction markets | Convenience of what exists is not validation for a new domain — design the prediction-market schema from its own requirements |
| 7 | Scope-creep recurrence | This project's own vault history already shows four generations of drift before anything past ingestion got built; adding a second asset class before vertical 1's loop is proven repeats this at larger scale | Hold the line: vertical 1 (`.kiro` tasks 7–13 → strategy engine → evidence cards → paper journal) ships completely before vertical 2 gets active dev time |
| 8 | Attention split with no team | Solo builder, two asset classes, different decision cadences, competing for the same hours | Mitigated by the sequencing decision above (vertical 2 dev time comes from vertical 1's paper-testing downtime, not from splitting active build time) — re-evaluate if paper-testing turns out to require more active tending than expected |
| 9 | Vendor instability asymmetry | Stock data providers are mature/stable; Polymarket/Kalshi APIs are newer and less stable; a shared provider abstraction tuned for the stable case will silently underserve the fragile one | Don't generalize `providers.toml`'s schema to prediction markets until that vertical's actual provider quirks are known |
| 10 | False sense of completeness | A unified-looking app with both verticals half-built reads as "far along" when it's actually two unfinished things | Track and report vertical completion separately, not as one blended percentage |

## Open Research Questions (next phase)
These stay in scope for research — several were closed or redirected in [[Session Findings — Cursor Alignment Pass (2026-07-10)]]:

1. ~~What does a genuinely differentiated stocks/ETFs strategy edge look like?~~ → **Addressed:** factor stack (momentum 12-1, quality/FCF, safety/vol, valuation FCF-EV, ETF baseline) + four-gate promotion; TA demoted to context. See [[Research - Systematic Equity Strategy Edge (2026-06-25)]] and Strategy Engine.
2. ~~What is Kronos actually capable of?~~ → **Researched** in [[Research - Kronos Foundation Model Deep Dive (2026-06-25)]]. **Build decision 2026-07-10:** reserved evidence slot only; no inference until RankIC validation on V1 universe.
3. What deeper trading/investing literature should still feed the brain's citation layer before expanding the universe past 14 names?
4. Prediction markets stay parked — **no code, no schema placeholders** until stocks paper readiness (confirmed 2026-07-10).
5. **New:** in-app charting/indicator library choice after paper APIs exist.
6. **New:** live LLM "propose spec" vs human-authored proposals stored in brain — decide after brain persistence lands.

## Related Notes
- [[RESEARCH]] — full product blueprint, autonomy ladder, agent design, evidence/thesis/journal contracts
- [[AI Market Analyzer - Product Spec]] — screens, non-goals, success criteria
- [[AI Market Analyzer - Strategy Engine]] — current strategy module drafts
- [[AI Market Analyzer - 4 Month Build Plan]] — build sequencing
- [[Session Findings — Cursor Alignment Pass (2026-07-10)]] — 2026-07-09/10 Q&A SoT before Fable 5
- [[Year-Ahead Base — Fable 5 Architecture Contract]] — hard-slice contract
- [[Math-First Map — Existing Code to Factor Brain]] — keep ingestion clean under math-first

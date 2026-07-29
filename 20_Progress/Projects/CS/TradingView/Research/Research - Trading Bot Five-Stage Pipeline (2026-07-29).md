---
type: research
status: sprout
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[Phase 2 — Strategy Pack Landed (2026-07-11)]]"
  - "[[Hermes Agent — Trading & Alert System (Distilled)]]"
tags:
  - trading
  - research
  - architecture
track:
  - trading
---
# Research — Trading Bot Five-Stage Pipeline (2026-07-29)
**Purpose:** [[PDF's Ingestion Implementation#Trading Bot Architecture: Five-Stage Pipeline - USEFUL?|AI Prediction Market Trading Bot's five-stage architecture]] (Scan → Research → Predict → Risk → Compound) is not a new decision — [[00_Execution]] confirmed it **restates** the human-review-gate design [[AI Market Analyzer - Product Spec]] already committed to, and independently matches a pattern [[Hermes Agent — Trading & Alert System (Distilled)]] distilled from a completely different source. Three convergent sources, one architecture. This note is the **implementation reference for later** — Kelly sizing, edge formula, Brier calibration — not a spec to build against yet, since the Product Spec hasn't reached paper trading.
---
## Confirmed: Same Shape as the Product Spec, Not a New Direction
[[AI Market Analyzer - Product Spec]]'s Non-Goals explicitly rule out auto-trading and broker execution for v1. Its Evidence Card Feed uses `ACCUMULATE`/`HOLD`/`WATCH`/`REDUCE`/`AVOID`/`INSUFFICIENT_DATA`, never `BUY`/`SELL` — a human-review gate by design. That's identical to what this five-stage architecture recommends: Predict generates a signal, a human decides, Risk/Compound stay deterministic. Nothing here overrides that design; it confirms it.
## The Five Stages (Prediction Market → Stocks/ETFs Translation)
| Stage | Prediction Market (Polymarket) | This Project's Translation |
|---|---|---|
| **Scan** | Polymarket CLOB API, high-volume markets | Alpha Vantage/TradingView data, volume ≥200k, price move >2%, volatility spike vs. 20-day MA |
| **Research** | Twitter sentiment on event, news RSS | Earnings, sector news, options IV, CEO sentiment |
| **Predict** | Estimate event probability vs. market price | Estimate move probability vs. options-implied move |
| **Risk** | Kelly on yes/no contracts | Kelly on long/short position size, $ terms |
| **Compound** | Trade log + loss classification | Win/loss stats, Brier tracker, strategy journal |
## Implementation Reference (For When Paper Trading Starts)
**Edge calculation:** trade only if `edge = p_model - p_market > 0.04` (4%). For stocks: $p_{model}$ is the model's probability of a move >X% in Y days; $p_{market}$ is the options-implied move.
**Kelly-criterion sizing:** full Kelly `f* = (p·b - q) / b` is mathematically optimal but destroys accounts on variance — use **quarter-Kelly (0.25×)** as the professional-standard default, half-Kelly (0.5×) as the aggressive ceiling. Example: $10,000 bankroll, 70% win probability, 2:1 reward/risk → full Kelly = 12% ($1,200, too aggressive) vs. quarter-Kelly = 3% ($300).
**Brier-score calibration:** $BS = \frac{1}{n}\sum(p_{pred} - outcome)^2$ — target <0.25. This is how the Product Spec's Portfolio Tracker screen would answer "is this model actually better than the market, or just lucky?"
**Risk checks (all must pass before a trade fires):** edge > 4%, position size ≤ Kelly calculation, new bet + existing exposure ≤ max portfolio exposure, VaR at 95% within daily limit, drawdown >8% blocks all new trades.
## Where This Plugs Into the Product Spec
- **Portfolio Tracker screen** — trade log, Brier tracker, win/loss stats (the Compound stage).
- **Alerts screen** — Scan + Research stage output, the trigger for a new Evidence Card.
- **Strategy Lab** — where Predict's edge calculation and Risk's Kelly sizing get backtested, using the VaR methods from [[Research - DeepThinksFinance Architecture Transfer (2026-07-29)]].
## Not Needed Yet
The Product Spec is still in build-out, not at the paper-trading stage. This is a reference to implement when that stage arrives — not a redesign to reconcile with [[Phase 2 — Strategy Pack Landed (2026-07-11)]]'s already-shipped strategy pack. Phase 2's four-gate system (OOS → Monte Carlo → walk-forward → deflated Sharpe, per [[Year-Ahead Base — Fable 5 Architecture Contract]]) already exceeds this architecture's rigor bar; nothing here should be re-decided when paper trading actually starts.
## Evidence
- [[PDF's Ingestion Implementation#Trading Bot Architecture: Five-Stage Pipeline - USEFUL?|Trading Bot Architecture]] — full stage-by-stage breakdown and formulas
- [[60_Claude/10_Source_Summaries/PDF Ingestion/Read/AI Prediction Market Trading Bot (PDF)]]
- [[AI Market Analyzer - Product Spec]] — the Non-Goals and Evidence Card design this confirms
- [[Phase 2 — Strategy Pack Landed (2026-07-11)]] — confirms current build state, not contradicted by this note
- [[Hermes Agent — Trading & Alert System (Distilled)]] — the independent second source converging on the same architecture
- [[00_Execution]] — the resolved verdict this note executes

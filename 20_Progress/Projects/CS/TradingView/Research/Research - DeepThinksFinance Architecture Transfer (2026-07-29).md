---
type: research
status: sprout
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[Phase 2 — Strategy Pack Landed (2026-07-11)]]"
tags:
  - trading
  - research
  - deepthinksfinance
track:
  - trading
---
# Research — DeepThinksFinance Architecture Transfer (2026-07-29)
**Purpose:** [[PDF's Ingestion Implementation#DeepThinksFinance: Competitive Analysis & Proof Testing (Not Primary Source) - USEFUL?|DeepThinksFinance's two PDFs]] (Portfolio Optimizer, Master Quant Prompt Guide) show signs of AI-generated content — "too good to be true" claims, India-specific hardcoding, retail-signal over-confidence. [[00_Execution]] resolved what actually transfers: the **architecture**, not the numbers. This note carries that resolved split forward as the concrete build reference for [[AI Market Analyzer - Product Spec]]'s Strategy Lab screen.
---
## What Transfers: The Three-Layer Split
DeepThinksFinance's Portfolio Optimizer uses: data pipeline (yfinance) → quantitative engine (scipy optimize) → LLM explanation layer, with Claude strictly *outside* the decision loop — analyst over deterministic math, never inside it. **This is the same shape [[AI Market Analyzer - Product Spec]] already commits to** in its own AI Behavior design (Evidence Card Feed uses `ACCUMULATE`/`HOLD`/`WATCH`/`REDUCE`/`AVOID`/`INSUFFICIENT_DATA`, never `BUY`/`SELL` — a human-review gate by design). DeepThinksFinance **confirms** the Product Spec's existing direction; it doesn't change it.
## Concrete Techniques Worth Adopting
- **Cholesky decomposition** for correlated multi-asset Monte Carlo — preserves the correlation structure across assets instead of simulating each independently.
- **Four VaR methods side by side:** historical (percentile of returns), parametric ($-z\sigma P$, assumes normal distribution), CVaR/Expected Shortfall (average loss beyond VaR), Monte Carlo (GBM-simulated). Compare all four rather than picking one blind.
- **Fama-French factor attribution** — separate factor beta from true alpha via rolling OLS. Maps directly onto [[AI Market Analyzer - Product Spec]]'s Strategy Lab backtest fields (Sharpe, drawdown) as the "how much of this return is skill vs. market exposure" check.
- **Unit test invariant:** all Monte Carlo weight vectors must sum to 1 within 10^-10 — a cheap correctness check worth copying verbatim.
## What Does NOT Transfer — The Proof-Testing Roadmap
Per [[PDF's Ingestion Implementation#DeepThinksFinance: Competitive Analysis & Proof Testing (Not Primary Source) - USEFUL?|the same section]], these need walk-forward validation before any use, and the source PDFs never ran that validation themselves:
- **Retail signals** (RSI, Bollinger Bands, Z-score) — descriptive context, not proven edge factors. [[Trading Resources Integration — TradingView Architecture Roadmap]]'s own MIT Bible source warns the same thing independently.
- **NIFTY-specific numbers** — ₹, RBI rate, India VIX — hardcoded to a market [[AI Market Analyzer - Product Spec]] doesn't trade. Adapt the *method*, never copy the constant.
## The Correct Build Order (Proof-Testing Roadmap)
1. **Week 1 — Efficient Frontier** from the Portfolio Optimizer's MPT + Monte Carlo. Most stable, most defensible — known math, easy to validate.
2. **Week 2 — Cholesky + blended vol** (`0.6 * (VIX/100) + 0.4 * (90-day historical)`) added to the Monte Carlo; validate VaR estimates against real portfolio drawdown history.
3. **Week 3 — Factor attribution** — measure how much of any strategy's return is alpha vs. market beta.
4. **Week 4 — One signal tested out-of-sample** (mean reversion or pairs trading, not both) with walk-forward stats published, not assumed.
## Confirmed Against Real Build State
[[Phase 2 — Strategy Pack Landed (2026-07-11)]] shows the actual TradingView codebase is already **ahead** of this roadmap on rigor: `quality_momentum.py` passed through four gates including an out-of-sample check that **failed closed correctly on thin data** — deterministic Python computing, AI only explaining, citation-backed signal selection (Jegadeesh-Titman 1993, Novy-Marx 2013). Nothing here should be used to second-guess that approach; this note is the reference for the *next* layer (Strategy Lab's VaR/Monte Carlo build), not a correction to what's shipped.
## Evidence
- [[PDF's Ingestion Implementation#DeepThinksFinance: Competitive Analysis & Proof Testing (Not Primary Source) - USEFUL?|DeepThinksFinance section]] — full red-flag table and proof-testing roadmap
- [[60_Claude/10_Source_Summaries/PDF Ingestion/Read/DeepThinksFinance AI Portfolio Optimizer (PDF)]]
- [[60_Claude/10_Source_Summaries/PDF Ingestion/Read/DeepThinksFinance Master Quant Prompt Guide v2 (PDF)]]
- [[AI Market Analyzer - Product Spec]] — Strategy Lab screen, the build target
- [[Phase 2 — Strategy Pack Landed (2026-07-11)]] — confirms current build already exceeds this roadmap's rigor bar
- [[00_Execution]] — the resolved verdict this note executes

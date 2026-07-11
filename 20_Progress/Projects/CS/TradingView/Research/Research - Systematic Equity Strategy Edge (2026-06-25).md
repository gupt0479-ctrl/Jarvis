---
type: research
status: sprout
created: 2026-06-25
updated: 2026-06-25
related_progress:
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[Postmortem - Stocks-ETFs First, Prediction Markets Second]]"
  - "[[RESEARCH]]"
tags:
  - trading
  - strategy
  - factor-investing
  - research
track:
  - trading
  - ai
---

# Research — Systematic Equity Strategy Edge (2026-06-25)

**Purpose:** Close the gap between the current strategy module notes (`[[AI Market Analyzer - Strategy Engine]]`), which are a generic TA/valuation checklist, and what primary academic and practitioner sources say about systematic edges that actually survive out-of-sample testing.

---

## The Core Problem with the Current Strategy Notes

The current modules (trend following → mean reversion → quality compounder → valuation sanity) are all reasonable things to *check*, but none of them are *differentiated edge*. The distinction matters:

- A **checklist** says: is price above the 200-day MA? Is RSI under 70? Is FCF positive?
- An **edge** is a systematic rule, applied to a cross-section of assets or over time, that has produced positive risk-adjusted returns *out-of-sample* after costs, with a plausible economic explanation that's unlikely to be pure data mining.

The gap: moving averages, RSI, and Bollinger Bands are technical folklore with weak or mixed evidence. Factor premiums (momentum, quality, value) have thirty-plus years of evidence across multiple countries and time periods.

---

## What Actually Has Primary-Source Evidence

### 1. Cross-Sectional Momentum (Jegadeesh-Titman 1993)

**The finding:** Stocks that outperformed over the prior 12 months (skipping the most recent month to avoid short-term reversal) continue to outperform over the next 3–12 months. Long winners, short losers.

**Signal construction:** For each stock, compute the 12-1 month total return (month −12 to month −2). Rank all stocks by this return. Buy top decile, avoid/short bottom decile.

**Evidence quality:** Originally published 1993 in the *Journal of Finance*, replicated across 30+ years, 40+ countries, multiple asset classes. Arguably the most robustly replicated anomaly in all of empirical finance.

**Decay pattern:** Signal is significant for 7–9 months post-formation. After 12–18 months, momentum *reverses* (long-term mean reversion). This implies momentum is not a set-and-forget strategy.

**Implementation challenges for V1:**
- With a 10-stock universe, true cross-sectional ranking is noisy (you're ranking 10 names, not 500). Momentum works better with larger universes.
- Short-selling is excluded from our guardrails. So the signal becomes a tilt (overweight recent winners, underweight recent losers in watchlist priority) rather than a long-short portfolio.
- Transaction costs eat momentum alpha aggressively if you're rebalancing monthly with small capital. Monthly rebalancing on a 10-stock list is still feasible.

**What to add to the strategy engine:** A 12-1 month return score for each symbol in the universe. Call it `momentum_score`. Use it to rank the watchlist. This is more evidence-based than price vs. 200-day MA alone.

**⚠️ Guardrail check:** Momentum signal ranks assets — it does not say "buy." Output must be: "This symbol ranks 2nd of 10 on 12-month relative return. Combined with other signals, this influences the evidence card." Never output "buy because momentum is high."

---

### 2. Quality Factor — QMJ (Asness, Frazzini, Pedersen — AQR 2014 / SSRN 2312432)

**The finding:** High-quality stocks (profitable, safe, growing, well-managed) earn higher risk-adjusted returns than low-quality "junk" stocks. The premium exists across 24 countries.

**Quality dimensions (the full QMJ definition):**
- **Profitability:** gross profit / assets (Novy-Marx), ROE, ROA, cash flow / assets, gross margin, fraction of earnings accruals
- **Growth:** 5-year growth in the above profitability metrics
- **Safety:** low beta, low idiosyncratic volatility, low leverage, low bankruptcy risk (Altman Z-score)
- **Payout:** high dividend + buyback yield, low dilution

**Key insight:** QMJ has *negative* market beta — quality stocks hold up better in downturns. It has low correlation to value (HML), which means quality and value are complementary factors, not redundant.

**What our current "quality compounder" module captures:** Revenue growth ✓, margins ✓, FCF ✓, debt ✓. Missing: beta/volatility safety dimension, accrual quality, dilution check.

**What to add:** A safety sub-score based on 12-month realized volatility (standard deviation of daily returns). Lower-volatility stocks get a higher safety component in the quality score. This also overlaps with the BAB anomaly (see below).

**⚠️ Guardrail check:** Quality score is an *evidence input*, not a rating. "This symbol scores 72/100 on quality composite" is acceptable. "This is a buy because quality is high" is not.

---

### 3. Low-Volatility Anomaly / Betting Against Beta (Frazzini, Pedersen 2014)

**The finding:** Low-beta, low-volatility stocks outperform high-beta stocks on a *risk-adjusted basis*. This contradicts CAPM, which predicts higher beta = higher return.

**Why it exists:** Leverage-constrained investors (pension funds, mutual funds that can't lever) reach for return by overweighting high-beta names. This creates overpricing for high-beta stocks and underpricing for low-beta stocks.

**2024 update (BABB — Betting Against Bad Beta):** The BABB variant — which isolates stocks with high beta but low fundamental quality ("bad beta") — produces a gross annualized return of 15.0% with 13.8% vol (Sharpe 1.09 vs BAB's 1.01 in the same sample).

**What to add to the strategy engine:** A 12-month realized volatility metric per symbol. Flag high-volatility symbols as carrying more risk than their apparent trend suggests. Low-volatility within the universe gets a slight quality bump.

---

### 4. Value / Free Cash Flow Yield (Multiple sources)

**The finding:** Stocks with high earnings yield (earnings/price = 1/P/E) and especially high free cash flow yield (FCF/enterprise value) have historically outperformed in large-cap US equities. FCF yield outperforms simple P/E because it is harder to manipulate and captures real cash generation.

**Evidence:** FCF yield (FCF/EV) produced the highest return and fewest negative-return periods vs. other valuation metrics since 1991 in Pacer ETFs' research. Stocks in the top decile by FCF yield outperformed the broader market by 3–5% annually.

**Combination effect:** When FCF yield is combined with 12-month price momentum, total return more than doubles vs. either signal alone (+755% total return vs. single-factor implementations). This cross-factor combination is the strongest signal available at our universe size.

**What this means for the strategy engine:** Valuation sanity check should weight FCF yield more heavily than raw P/E. P/E is useful but easily gamed; P/FCF is closer to what QMJ's profitability dimension actually measures.

---

### 5. Fama-French Five-Factor Model — What It Explains and Doesn't

**The five factors:** Market (MKT-RF), Size (SMB), Value (HML), Profitability (RMW), Investment (CMA).

**What it handles:** The model explains a significant fraction of the cross-section of US equity returns. RMW (robust minus weak profitability) is closely related to QMJ's profitability dimension. CMA (conservative minus aggressive investment) captures firms that grow assets slowly — often correlated with quality.

**What it misses:** Momentum is not included in FF5 and represents its biggest gap. The model also doesn't explain the low-volatility anomaly (BAB). COVID-era evidence (2024): size gained, value was volatile, profitability and investment factors declined in significance.

**Practical implication for us:** The FF5 factors are a useful benchmark to check whether a strategy's backtest alpha is just factor exposure in disguise. A backtest that looks impressive but is just long RMW/CMA exposure isn't an edge — it's a known factor tilt. Use the Fama-French data library (Dartmouth) to audit this. Free download via `getFamaFrenchFactors` Python package.

---

## The Factor Zoo Problem — What This Means for Us

Harvey, Liu, and Zhu (2016) reviewed 296 published significant factors. After adjusting for multiple testing, the majority are likely false discoveries. The key implication: do not add signals just because they sound reasonable or produce a good backtest on the V1 universe of 10 stocks.

**Our filter:** Only add a signal to the strategy engine if at least one of the following is true:
1. It maps to one of the four well-documented factors (momentum, quality/profitability, value/FCF, low-volatility).
2. It has a published, replicated paper that survives multiple-testing adjustment.
3. It has an economic explanation that's independent of historical mining.

**Signals that fail this filter (and are already in our current notes):**
- RSI overbought/oversold: no robust long-term academic evidence as a standalone signal. Useful as a *description* of price action, not as a reliable predictive edge.
- Bollinger Band touch: similar to RSI — useful for visualizing volatility, not a well-documented systematic edge.
- Price vs. 200-day MA (used in isolation): no robust factor evidence. Correlates with momentum, but is a much cruder version. Keep as a *trend context check*, not as an evidence-generating signal.

**These signals are not being removed.** They stay as contextual checks and evidence-card descriptions. They just don't get to drive the action label independently.

---

## What Walk-Forward Validation Means for Our Backtests

The current backtesting rules in the strategy engine notes cover: no lookahead bias, buy-and-hold comparison, transaction costs, drawdown. What's missing:

**Walk-forward validation:** Instead of one train/test split, you optimize strategy parameters on a rolling 2-4 year window, then test on the next 3-6 months, advance the window forward, and repeat. This is what Pardo (1992) formalized as the gold standard for strategy validation.

**Deflated Sharpe Ratio (López de Prado 2018):** When you've tested many strategy configurations, the best backtest Sharpe is inflated by selection bias. The Deflated Sharpe Ratio corrects for this. SSRN paper: 3073799.

**Probability of Backtest Overfitting (Bailey, Borwein, López de Prado, Zhu 2014):** Uses combinatorial cross-validation to estimate the probability that a backtest result is an overfit. Available in Python as `mlfinlab`.

**Practical implication for V1:** Our 10-symbol universe is too small for true walk-forward parameter optimization (you need at minimum 5 years of daily data and a universe large enough to form portfolios). Instead:
1. Fix strategy parameters to values from the academic literature (12-1 month for momentum, well-established quality metrics) rather than optimizing them on our data.
2. Report backtests honestly with the actual parameter choices and the note "parameters not optimized on this data."
3. Run walk-forward once the universe expands past 20-30 symbols.

---

## Proposed Strategy Engine Revision (What to Change)

| Current module | Issue | Change |
|---|---|---|
| Trend following (price vs. 50/200-day MA) | Contextual check, not a factor edge | Keep as context. Add 12-1 month return score (`momentum_score`) as the primary ranking signal. |
| Mean reversion (RSI, Bollinger) | No robust factor evidence in isolation | Demote to "technical context" in the evidence card. Do not use as a primary action driver. |
| Quality compounder | Good start. Missing safety/volatility dimension. | Add realized volatility (12-month) as a safety sub-score. Weight FCF margin over raw revenue growth. |
| Valuation sanity (P/E, P/S, P/FCF) | P/FCF closest to evidence-based value signal. | Weight FCF/EV most heavily. Add note: P/E differs substantially across sectors; flag sector context. |
| ETF baseline | Correct and important. | No change. This is the right primary benchmark. |

**New additions:**
- `momentum_score`: 12-1 month return rank within the universe (1 = lowest return, 10 = highest return for a 10-symbol universe). Used to rank watchlist priority.
- `safety_score`: inverse of 12-month realized daily return volatility. Higher score = lower volatility = less risk within the universe.
- `quality_fcf_score`: composite of FCF margin, FCF/EV, operating margin stability, debt-to-equity.

These three scores combine with the existing quality and valuation checks to form the evidence packet that feeds agents.

---

## Source Index

| Source | URL | Supports |
|---|---|---|
| Jegadeesh & Titman (1993) — Returns to Buying Winners and Selling Losers | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=227214 | 12-1 month momentum is the seminal evidence. Signal significant 7–9 months, reverses after 12–18. |
| Momentum: what do we know 30 years after J&T (2022, Springer) | https://link.springer.com/article/10.1007/s11408-022-00417-8 | Review of 30 years of momentum evidence across asset classes and countries. |
| AQR — Quality Minus Junk (Asness, Frazzini, Pedersen) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2312432 | Full QMJ definition: profitability, growth, safety, payout. Evidence across 24 countries. |
| AQR QMJ Factor Data | https://www.aqr.com/Insights/Datasets/Quality-Minus-Junk-Factors-Monthly | Free monthly factor data download from AQR. |
| Betting Against (Bad) Beta (2024, arXiv 2409.00416) | https://arxiv.org/pdf/2409.00416 | BABB extension of BAB: high-beta + low-quality stocks are the overpriced ones. Gross return 15.0% / vol 13.8%. |
| Harvey, Liu, Zhu — ...and the Cross-Section of Expected Returns (2016) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2249314 | The factor zoo problem: majority of 296 published factors are likely false discoveries. Multiple-testing threshold required. |
| Fama-French Data Library (Dartmouth) | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Free download of FF3, FF5, momentum factor returns. Ground truth for factor exposure audit. |
| FCF Yield evidence (Pacer ETFs) | https://www.paceretfs.com/resources/resource-library/the-power-of-free-cash-flow-yield | FCF/EV produced highest return and fewest negative-return periods since 1991. FCF + momentum: >2x single-factor return. |
| Walk-Forward Analysis vs. Backtesting (Surmount) | https://surmount.ai/blogs/walk-forward-analysis-vs-backtesting-pros-cons-best-practices | Walk-forward: 2-4 year optimization window, 3-6 month OOS. Gold standard for strategy validation. |
| Walk-Forward Optimization (QuantInsti) | https://blog.quantinsti.com/walk-forward-optimization-introduction/ | Implementation guide for walk-forward with rolling windows. |
| Fama-French Five-Factor Model systematic review (HRMARS) | https://hrmars.com/papers_submitted/21632/how-well-has-fama-french-five-factor-model-explained-asset-returns-a-systematic-literature-review.pdf | FF5 global evidence review; model fails on momentum and low-volatility. |

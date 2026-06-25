---
type: research
status: sprout
created: 2026-06-25
updated: 2026-06-25
related_progress:
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[Research - Systematic Equity Strategy Edge (2026-06-25)]]"
  - "[[Research - Kronos Foundation Model Deep Dive (2026-06-25)]]"
tags:
  - trading
  - fundamentals
  - risk-management
  - backtesting
  - research
track:
  - trading
---

# Research — Trading Fundamentals Gap Fill (2026-06-25)

**Purpose:** Document the specific investing/trading concepts that were blocking a real strategy decision. These are the vocabulary and mental models that need to be internalized before the strategy engine notes make sense — and before we can evaluate whether our backtests are any good.

Written for a beginner who already understands: price charts, basic P/E ratios, what a stock is, what an ETF is.

---

## Alpha and Beta

**Beta** is how much a stock moves relative to the overall market. A beta of 1.0 means: if the S&P 500 drops 3%, this stock typically drops 3% too. A beta of 1.5 means: if the market drops 3%, this stock typically drops 4.5%. A beta of 0.7 means it drops only 2.1%.

- High beta stocks (>1.0): more volatile, more upside in bull markets, more downside in crashes. Examples: NVDA, speculative growth stocks.
- Low beta stocks (<1.0): steadier, but cap your upside. Examples: consumer staples, utility companies.
- ETFs like VOO have beta ≈ 1.0 by construction (they *are* the market benchmark).

**Alpha** is the return above what you'd expect given your beta exposure. If the S&P 500 returns 10% and your strategy returns 10%, your alpha is 0 — you just had market exposure. If the same strategy returns 13% while the market returned 10%, alpha = 3%. Alpha is the measure of skill (or luck) that goes beyond simply riding market returns.

**Why this matters for our product:** Every stock idea must explain whether it's earning alpha or just leveraged market exposure. The ETF baseline check exists specifically to call out "this looks good but is actually just high-beta market exposure, not skill."

---

## Systematic Risk vs. Idiosyncratic Risk

**Systematic risk** (also called market risk) affects all stocks at once. Interest rate changes, recessions, geopolitical events, pandemic shocks — these are systematic. You cannot eliminate systematic risk by holding more stocks. Even a perfectly diversified portfolio still falls in a market crash.

**Idiosyncratic risk** (also called company-specific or unsystematic risk) is unique to one company: a bad earnings report, a CEO departure, a product recall, a competitive threat. This risk *can* be diversified away. If you hold 30-50 uncorrelated stocks, individual company disasters don't sink the whole portfolio.

**For our V1 10-symbol universe:** We have almost no diversification benefit — our universe is 10 of the largest US tech/growth names. They are all highly correlated. AAPL, MSFT, NVDA, AMZN, GOOGL, META all move together in a tech-sector rotation. This means idiosyncratic risk across the universe is actually low (the universe is highly concentrated in systematic/sector risk), but we have no real diversification buffer against a tech sell-off. This is a known limitation of V1 and should be flagged in every evidence card.

---

## Risk-On / Risk-Off Market Regimes

Markets cycle between **risk-on** and **risk-off** environments. Understanding which regime you're in determines which signals matter and which are likely to produce false positives.

**Risk-on:** Investors are comfortable taking risk. Money flows into stocks, high-yield bonds, emerging markets, crypto. Tech and growth stocks typically outperform. Momentum strategies work well in risk-on environments.

**Risk-off:** Investors want safety. Money flows out of stocks into US Treasuries, gold, Swiss francs, Japanese yen. Growth stocks sell off disproportionately. Momentum strategies tend to break down (they're long the prior winners, which are often the first to be sold).

**Why this matters for our strategy engine:** The current strategy notes don't account for market regime at all. A trend-following signal saying "NVDA is above its 200-day MA" means something different in a risk-on bull market vs. a risk-off environment where the 200-day MA is collapsing. The Risk Manager agent (in the multi-agent design) should assess current regime as part of the confidence cap.

**Simple regime proxy for V1:** VIX level (volatility index). VIX < 15: stable/risk-on. VIX 15-25: caution. VIX > 25: risk-off / elevated uncertainty. When VIX > 25, evidence card confidence should be capped lower for trend-following signals, because trends break faster in high-volatility regimes.

---

## Risk-Adjusted Return Metrics

Raw return numbers are meaningless without knowing how much risk was taken to earn them. These three metrics are the standard tools for comparing strategies that might have very different volatility profiles.

### Sharpe Ratio

```
Sharpe = (Strategy Return − Risk-Free Rate) / Strategy Volatility
```

Measures return per unit of *total* volatility (upside and downside alike).

| Sharpe | Interpretation |
|---|---|
| < 0 | Worse than simply holding cash |
| 0–0.5 | Marginal. Barely justifies the risk. |
| 0.5–1.0 | Respectable. Worth examining further. |
| 1.0–2.0 | Genuinely good. Rare in practice. |
| > 2.0 | Exceptional, but be very skeptical — likely overfit or survivorship bias. |

**Risk-free rate:** The return you'd get with no risk at all (US Treasury bills, currently ~4-5%). The subtraction matters: earning 8% with 20% volatility when T-bills yield 5% only gives a Sharpe of (8-5)/20 = 0.15, which is poor.

### Sortino Ratio

```
Sortino = (Strategy Return − Risk-Free Rate) / Downside Deviation
```

Same as Sharpe but only penalizes *negative* volatility. A strategy that goes up sharply and then flat has lots of upside volatility — Sharpe punishes this. Sortino doesn't. For strategies with asymmetric return distributions (hold for big winners, cut losses fast), Sortino is a more honest metric.

**Use Sortino alongside Sharpe.** If Sortino >> Sharpe, the strategy has lots of upside volatility (good). If Sortino ≈ Sharpe, the volatility is mostly symmetric (neutral). If Sortino < Sharpe, something is wrong (asymmetry is in the wrong direction — more downside spikes than upside).

### Calmar Ratio

```
Calmar = Annualized Return / Maximum Drawdown
```

Maximum drawdown = the largest peak-to-trough decline during the backtest period. Calmar measures how much annual return you earn per unit of worst-case loss.

- Calmar = 0.5: earn 0.5% annualized for every 1% of worst-case drawdown. Poor.
- Calmar = 1.0: earn 1% per 1% of worst drawdown. Acceptable.
- Calmar > 2.0: earn 2%+ per 1% of worst drawdown. Good.

**Why Calmar matters:** Buy-and-hold VOO has had drawdowns of 35-50% in major crashes (2008, 2020). A strategy with identical annualized returns but half the max drawdown has a Calmar ratio twice as good. Calmar is the metric that catches strategies that look good on average returns but blow up periodically.

**Practical note:** All three ratios must be computed for the *out-of-sample* period, not the period used to develop the strategy. An overfit backtest will produce Sharpe > 2.0 in-sample and Sharpe < 0 out-of-sample.

---

## Walk-Forward Validation — The Key Backtest Standard

Standard backtests have a fatal flaw: you pick parameters (lookback periods, thresholds) that looked good on the historical data, then test on that same historical data. This is circular — you're measuring how well you've memorized the past, not how well your strategy will work on new data.

**Walk-forward validation** solves this by mimicking how you'd actually use the strategy:

1. Take the full historical data, say 5 years.
2. Use the first 2 years (the "optimization window") to pick parameters.
3. Test those exact parameters on the next 6 months (the "out-of-sample window") — data the model never saw.
4. Record the OOS performance.
5. Advance both windows forward by 6 months.
6. Repeat until you've tested the full data range.
7. Report average OOS performance across all windows.

The optimization window should be 2-4 years of daily data. The OOS window should be 3-6 months. Each step advances by one OOS period.

**For V1 limitations:** Our 10-symbol universe is too small and our parameter space should be kept fixed (use academically-published parameters, not optimized parameters). But we must still hold out the most recent 12 months as a true OOS test period that is never touched during strategy development.

**Deflated Sharpe Ratio:** When you've run many strategy variants and picked the best one, the winner's Sharpe is inflated by selection bias — you chose the best of many noisy outcomes. The Deflated Sharpe Ratio (López de Prado & Bailey, 2014, SSRN 3073799) corrects for this. It deflates the observed Sharpe based on the number of strategies tested, the trial correlation structure, and the distribution of outcomes.

Rule of thumb: if you've tested 20+ strategy configurations, divide your best Sharpe by √(log(20)) ≈ 1.73 as a rough deflation. The actual Deflated Sharpe formula is more precise.

---

## Position Sizing — Kelly Criterion

**Kelly criterion** answers: what fraction of your portfolio should you risk on a trade with known win rate and win/loss ratio?

```
Kelly fraction = (edge) / (odds)
              = (P(win) × Win_pct − P(loss) × Loss_pct) / Win_pct
```

Or equivalently: `f = W − (1−W)/R` where W = win rate, R = win/loss ratio.

**Example:** Strategy wins 55% of the time, average win +4%, average loss -3%.
- R = 4/3 = 1.33
- Kelly = 0.55 − 0.45/1.33 = 0.55 − 0.34 = 0.21 = 21%

Kelly says risk 21% of portfolio per trade. In practice, **fractional Kelly** (half-Kelly or quarter-Kelly) is standard because:
1. Kelly requires exact knowledge of win rate and win/loss ratio, which we don't have — they're estimated from a backtest, so they're noisy.
2. Full Kelly maximizes long-run geometric return but causes extremely large drawdowns in the short run.
3. Half-Kelly gives about 75% of the long-run growth rate but with much smaller drawdowns — this is almost universally preferred.

**For V1:** We're paper trading with a fixed simulated account size. Kelly or half-Kelly gives a principled way to size simulated positions rather than using arbitrary percentages. This is important to implement in the paper journal.

---

## Benchmark Comparison — Why VOO Is the Bar

Every strategy must beat a simple alternative: buy VOO, hold it forever, ignore everything else.

| Metric | What to compare |
|---|---|
| Annualized return | Must beat VOO's average annual return (historically ~10-11%) after costs |
| Sharpe | Must beat VOO's Sharpe (historically ~0.5–0.8 over 30-year periods) |
| Max drawdown | Can be worse than VOO only if returns are proportionally better (i.e., Calmar must stay competitive) |
| Transaction costs | Must be included — momentum strategies with monthly rebalancing on 10 stocks accumulate real costs |

If a strategy doesn't consistently beat VOO buy-and-hold across multiple OOS windows on a risk-adjusted basis, it's not worth implementing over simply holding VOO. This is the product's core behavioral guardrail.

---

## Fama-French Data — Free Research Resource

The Fama-French factor return data is freely available from Kenneth French's Dartmouth data library. This is academically maintained, updated monthly, and includes:

- 3-Factor monthly returns (Mkt-RF, SMB, HML) back to 1926
- 5-Factor monthly returns (Mkt-RF, SMB, HML, RMW, CMA)
- Momentum factor (Mom)
- Portfolio returns sorted by size, value, profitability, investment

**How to use in Python:**

```python
pip install getFamaFrenchFactors
import getFamaFrenchFactors as gff

# Download 5-factor monthly returns
ff5 = gff.famaFrench5Factor(frequency='m')
```

**Use in the project for:** Auditing whether a strategy's backtest return is just factor exposure. If a strategy that claims to have found "alpha" has high correlation with FF5 factor returns, it's not alpha — it's just a known factor tilt without the diversification benefits of holding the actual factor portfolio.

---

## What the Current Strategy Notes Still Lack

After this research pass, three gaps remain in the current `AI Market Analyzer - Strategy Engine.md`:

1. **No RankIC computation.** The strategy engine produces strategy scores but doesn't evaluate how well those scores *rank* the 10 symbols in terms of forward returns. Cross-sectional ranking ability is what determines whether the strategy adds value over holding all 10 equally.

2. **No confidence decay from regime.** VIX or realized-volatility regime flag is missing. High-VIX periods should automatically reduce evidence card confidence.

3. **No benchmark-relative return tracking in paper journal.** The paper journal should record, for every paper position, what VOO returned over the same holding period. Without this comparison, we can't evaluate strategy performance honestly.

These three additions should be part of the strategy engine revision (see `[[Research - Systematic Equity Strategy Edge (2026-06-25)]]`).

---

## Source Index

| Source | URL | Supports |
|---|---|---|
| Alpha (finance) — Wikipedia | https://en.wikipedia.org/wiki/Alpha_(finance) | Definition of alpha as excess return above benchmark expectation. |
| Beta (finance) — Wikipedia | https://en.wikipedia.org/wiki/Beta_(finance) | Beta definition, baseline = 1.0, interpretation for high/low beta stocks. |
| Risk-on vs Risk-off (Britannica Money) | https://www.britannica.com/money/risk-on-vs-risk-off | Clear explanation of regime dynamics and asset flow patterns. |
| Risk-on vs Risk-off (Capital.com) | https://capital.com/en-int/learn/glossary/risk-on-risk-off-definition | Practical implications for equity strategy. |
| Walk-Forward Analysis vs. Backtesting (Surmount) | https://surmount.ai/blogs/walk-forward-analysis-vs-backtesting-pros-cons-best-practices | Walk-forward: gold standard for strategy validation, 2-4yr optimization window, 3-6mo OOS. |
| Walk-Forward Optimization (QuantInsti) | https://blog.quantinsti.com/walk-forward-optimization-introduction/ | Implementation guide with rolling windows. |
| Deflated Sharpe Ratio (López de Prado, SSRN 3073799) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3073799 | Corrects for selection bias when testing many strategy configurations. |
| Probability of Backtest Overfitting (Bailey et al., SSRN 2326253) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253 | CSCV method for computing probability of backtest overfitting. |
| Kenneth French Data Library (Dartmouth) | https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html | Free FF3/FF5/momentum factor data. Ground truth for factor attribution. |
| Fama-French Python package (getFamaFrenchFactors) | https://github.com/vashOnGitHub/getFamaFrenchFactors | Python wrapper for downloading FF factor returns as pandas DataFrames. |
| Risk Metrics Explained (ICF Specialists) | https://icfs.com/specialists-desk/risk-metrics-explained | Sharpe, Sortino, alpha, beta definitions with numerical examples. |
| MTUM momentum ETF large-cap performance 2024 | https://www.investing.com/analysis/momentum-largecap-growth-set-to-top-factors-returns-in-2024-200654933 | Large-cap momentum topped factor returns in 2024 with 32.0% gain. Context for current-regime evidence. |

---
type: concept
status: sprout
created: 2026-04-26
updated: 2026-06-25
related_progress:
  - "[[Trading with Ai]]"
  - "[[AI Market Analyzer - AI Engine Architecture]]"
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[AI Market Analyzer - Data Sources]]"
  - "[[Research - Systematic Equity Strategy Edge (2026-06-25)]]"
  - "[[Research - Kronos Foundation Model Deep Dive (2026-06-25)]]"
  - "[[Research - Trading Fundamentals Gap Fill (2026-06-25)]]"
tags:
  - trading
  - strategy
  - ai
  - backtesting
track:
  - trading
  - ai
next: "[[AI Market Analyzer - 4 Month Build Plan]]"
---

# AI Market Analyzer - Strategy Engine

## Core Rule

Strategies must be deterministic first. AI can explain and combine evidence, but Python code must compute the signals.

Bad:

```text
Ask AI: "Should I buy AAPL?"
```

Good:

```text
Fetch verified data
Compute indicators
Run strategy checks
Run risk checks
Build evidence packet
Ask AI to produce structured evidence card
```

## Signal Filter

Only add a signal to the engine if at least one of these is true:
1. It maps to one of the four academically documented factor premiums: momentum, quality/profitability, value/FCF yield, low-volatility.
2. It has a published, replicated paper that survives multiple-testing adjustment.
3. It has an economic explanation independent of historical data mining.

Moving averages, RSI, and Bollinger Bands do not pass this filter as standalone signals. They remain in the engine as **trend and volatility context** — useful descriptions of price action that agents can reference, but they do not drive action hints on their own. See `[[Research - Systematic Equity Strategy Edge (2026-06-25)]]`.

---

## V1 Strategy Types

### 1. ETF Baseline Strategy

Purpose:

- Keep me grounded.
- Compare individual stock picks against a broad market alternative.

Example assets:

- VOO
- VTI
- QQQ
- SCHD

Rules:

- Long-term default is broad ETF accumulation.
- Individual stocks must justify why they deserve attention over ETF baseline.
- Evidence cards should compare expected risk against broad ETF exposure.

---

### 2. Trend Following Strategy

Purpose:

- Identify assets already moving in a healthy direction, using cross-sectional ranking rather than raw price-level checks.

**Primary signal — `momentum_score`:**

Compute the 12-1 month total return for each symbol in the V1 universe: the cumulative return from 12 months ago to 1 month ago (skipping the most recent month to avoid the known short-term reversal effect documented by Jegadeesh-Titman 1993). Rank all 10 symbols from 1 (lowest return) to 10 (highest return).

This is the primary watchlist-priority signal for the Trend Following module. A symbol ranked 9 or 10 of 10 on 12-month relative return has demonstrated sustained relative strength across the universe. A symbol ranked 1 or 2 has underperformed peers over the same window.

Signal significance window: 7–9 months post-formation. After 12–18 months, momentum tends to reverse. Re-rank monthly.

**Trend context (not independent action drivers):**

The following describe price structure and support the Technical Analyst agent's narrative, but do not independently produce an `action_hint`:
- Price vs. 50-day moving average
- Price vs. 200-day moving average
- 50-day MA vs. 200-day MA (golden cross / death cross)
- Relative strength vs. SPY or VOO
- Volume confirmation on breakouts

Possible actions:

- `WATCH`: momentum_score is mid-range (4–7), trend context is neutral.
- `ACCUMULATE`: momentum_score ranks in the top 2–3 of the universe, trend context is constructive, quality and risk checks pass.
- `REDUCE`: momentum_score has fallen sharply month-over-month and price has broken key trend context levels.

Guardrail: the evidence card must say "ranks Nth of 10 on 12-month relative return" — not "accumulate because momentum is high." The score ranks; agents interpret. Never use momentum_score alone to produce an action label.

Beginner warning:

- Momentum strategies buy recent winners, which can mean high valuations.
- Cross-sectional ranking on 10 symbols is noisier than on a 500-stock universe. Treat rankings as a tiebreaker, not a certainty.
- Signal decays after 9 months — re-rank monthly, not annually.

---

### 3. Mean Reversion Strategy

Purpose:

- Flag when price has moved unusually far from its recent range. This is contextual information for agents, not a standalone strategy with independent action authority.

**Technical context (descriptive only — do not drive action_hint alone):**

RSI and Bollinger Band signals describe the current price position relative to recent history. They are useful for the Technical Analyst agent to note as context. They do not independently produce an `action_hint` because neither has robust out-of-sample evidence as a standalone predictive edge (see Factor Zoo filter above).

Context fields to compute and expose:
- RSI (14-day): flags whether price is statistically extended (below 30 or above 70) — report the value, not a directive.
- Bollinger Band position: how many standard deviations current price sits from the 20-day mean — report the value.
- Short-term drawdown: percentage decline from the 52-week high — report the magnitude.

When these context fields show extreme readings *and* the quality_fcf_score and safety_score are strong, the combination may support a cautious `WATCH` or `ACCUMULATE` hint. Neither RSI nor Bollinger alone justifies anything beyond `WATCH`.

Possible actions:

- `WATCH`: price is extended (high RSI / outside Bollinger) but fundamentals and thesis are intact — worth monitoring for re-entry.
- `ACCUMULATE`: significant pullback in a symbol with a strong quality_fcf_score and a high momentum_score over the prior 12-month window — evidence supports a cautious position.
- `AVOID`: price is falling but fundamentals are also deteriorating — no rebound basis.

Beginner warning:

- Cheap can get cheaper.
- Mean reversion without quality filters is dangerous.
- RSI and Bollinger do not predict direction — they describe the current state.

---

### 4. Quality Compounder Strategy

Purpose:

- Find companies worth holding for longer periods, using a composite quality score that covers the four QMJ dimensions: profitability, growth, safety, and payout.

**`quality_fcf_score` — primary quality composite:**

Composite of four sub-signals, each scored and weighted:
- **FCF/EV (FCF yield):** primary weight. Higher FCF/EV = more cash generated per dollar of enterprise value. Hardest valuation metric to manipulate; strongest documented large-cap equity factor (Pacer ETFs 1991–present; FCF + momentum combination doubles standalone returns).
- **FCF margin:** FCF / revenue. Captures how efficiently the business converts revenue to real cash.
- **Operating margin stability:** consistency of operating margin over trailing 4–8 quarters. Volatile margins flag earnings quality risk.
- **Debt-to-equity:** lower is better within the universe. Excessive leverage raises bankruptcy risk and amplifies drawdowns.

The `quality_fcf_score` ranges 0–100 across the V1 universe. Report it as "scores Nth of 10 on quality composite" — not as a standalone buy/avoid signal.

**`safety_score` — new sub-score filling the QMJ safety dimension:**

Compute the 12-month realized daily return volatility (standard deviation of daily returns over the trailing 252 trading days) for each symbol. The `safety_score` is the inverse rank: the symbol with the lowest realized volatility in the universe ranks 10 (safest); the symbol with the highest volatility ranks 1 (most volatile).

This fills the missing safety dimension of QMJ (Asness, Frazzini, Pedersen 2014). High-volatility, high-beta names are structurally overpriced relative to their fundamentals (the Betting Against Beta anomaly). A low safety_score is a flag, not a disqualifier — but it must be surfaced in the evidence card's `risk_flags`.

**Existing profitability signals (retained):**

- Revenue growth (year-over-year)
- Gross/operating margin strength
- Positive free cash flow
- Consistent profitability over trailing 4 quarters
- Durable sector/industry position

Possible actions:

- `ACCUMULATE`: quality_fcf_score ranks high in the universe, safety_score is not at the bottom, momentum_score is above mid-range.
- `HOLD`: business quality remains strong but either price is stretched relative to FCF/EV or momentum_score has faded.
- `WATCH`: quality signals are promising but one or more fields are incomplete or inconsistent.

Beginner warning:

- Great companies can be bad buys at extreme prices.
- A high quality_fcf_score does not override a very low safety_score — volatility risk is real.
- Revenue growth alone is not the same as quality. Weight FCF margin and FCF/EV more heavily than top-line growth.

---

### 5. Valuation Sanity Strategy

Purpose:

- Prevent buying hype blindly. Anchors the evidence card to cash-based valuation, not narrative valuation.

**Primary weight — FCF/EV (FCF yield):**

FCF/EV is the primary valuation signal, not raw P/E. Reasons: P/E is easily manipulated through accounting choices and varies widely across sectors; FCF/EV measures real cash returned per dollar of enterprise value and has the strongest documented large-cap evidence base.

**Secondary signals (contextual, sector-dependent):**

- P/FCF: directionally aligned with FCF/EV; include for cross-check.
- Forward P/E if available: useful for growth-expectation context; flag if it implies >25% annualized growth (extreme assumptions).
- P/S: useful for pre-profit companies only; note the limitation explicitly.
- EV/EBITDA: good for capital-intensive businesses; note sector applicability.
- Comparison to symbol's own historical range: is current valuation stretched vs. the prior 5 years?

**`quality_fcf_score` bridges quality and valuation:**

The FCF/EV and FCF margin sub-components of `quality_fcf_score` (computed in the Quality module) are the primary valuation inputs here. Do not compute a separate valuation score disconnected from the quality composite — valuation and quality should reinforce each other, not be independent axes.

Possible actions:

- `HOLD`: valuation is stretched on FCF/EV but business quality supports patience.
- `WATCH`: wait for a better FCF/EV entry point or stronger quality evidence.
- `AVOID`: FCF/EV implies the market is pricing in unrealistic growth; quality signals do not support the premium.

Guardrail: P/E differences across sectors make raw P/E comparisons misleading. NVDA and SCHD should never be compared on raw P/E. Always flag the sector when surfacing valuation context.

Beginner warning:

- Valuation metrics differ by sector.
- Early-growth companies may look expensive on FCF/EV for years while compounding. Context matters.
- A low FCF/EV is a signal to investigate, not a mechanical buy trigger.

---

## Strategy Score Packet

Each strategy run produces a structured packet. The AI receives this packet — it does not recompute signals from scratch.

```yaml
symbol: MSFT
as_of: "2026-06-25"
universe_size: 10

# Factor-based scores (new additions — primary ranking signals)
momentum_score:
  value: 8                          # rank 8 of 10 in universe on 12-1 month return
  twelve_month_minus_one_return: 0.31   # raw 12-1 month total return
  context: "Ranks 8th of 10 on 12-month relative return within V1 universe."

safety_score:
  value: 7                          # rank 7 of 10 (lower volatility = higher rank)
  realized_vol_12m: 0.22            # 12-month daily return std dev (annualized)
  context: "Ranks 7th of 10 on realized volatility. Moderate safety within universe."

quality_fcf_score:
  value: 81                         # composite 0-100
  fcf_ev: 0.035                     # FCF / enterprise value
  fcf_margin: 0.28                  # FCF / revenue
  op_margin_stability: "high"       # consistent across trailing 8 quarters
  debt_to_equity: 0.41
  context: "Ranks 2nd of 10 on quality composite. FCF yield and margin both strong."

# Module scores (existing — retained)
trend_following:
  action_hint: HOLD
  confidence_hint: 0.68
  trend_context:
    price_vs_50d: "above"
    price_vs_200d: "above"
    ma_cross: "golden"
    note: "Trend context is constructive. momentum_score (rank 8) is the primary signal."
  signals:
    positive:
      - "Ranks 8th of 10 on 12-month relative return."
      - "Price above both moving averages."
    negative:
      - "Volume confirmation is weak on recent price move."

mean_reversion:
  action_hint: null                 # No independent action hint from mean reversion this pass
  technical_context:
    rsi_14: 58
    bollinger_position: "mid-band"
    drawdown_from_52w_high: -0.04
    note: "RSI and Bollinger describe current position only. No extreme readings — no mean reversion context to flag."

quality_compounder:
  action_hint: ACCUMULATE
  confidence_hint: 0.74
  signals:
    positive:
      - "quality_fcf_score ranks 2nd of 10."
      - "FCF margin 28% — among the strongest in the universe."
      - "Operating margin has been stable for 8 consecutive quarters."
    negative:
      - "Debt-to-equity is moderate but not best-in-class within universe."

valuation_sanity:
  action_hint: HOLD
  confidence_hint: 0.65
  signals:
    positive:
      - "FCF/EV of 3.5% is above the universe median."
    negative:
      - "Forward P/E implies 18% annualized growth — achievable but not certain."
    caveats:
      - "Sector: large-cap software. Raw P/E not comparable to SCHD or VOO."

risk_flags:
  - "safety_score rank 7: moderate realized volatility — not a top safety concern but not a low-beta name."
  - "Earnings date within next 30 days — event risk is elevated."

data_quality:
  status: usable
  max_confidence: 0.80
  missing_fields: []
  stale_fields: []
```

The AI receives this packet. It does not compute the packet from scratch. It must cite the evidence fields above when producing the evidence card — not invent numbers, ratings, or analyst claims.

---

## Evidence Card Schema

The AI must return structured output matching this shape:

```json
{
  "symbol": "MSFT",
  "action": "HOLD",
  "confidence": 0.71,
  "time_horizon": "weeks_to_months",
  "strategy_used": ["quality_compounder", "trend_following"],
  "summary": "Business quality is strong, but the current setup is better for holding than aggressive buying.",
  "evidence": [
    {
      "source": "fundamentals",
      "claim": "Operating margin remains strong.",
      "as_of": "2026-04-26"
    }
  ],
  "risks": [
    "Valuation risk if growth slows."
  ],
  "opposing_evidence": [
    "Momentum is not strong enough for a high-conviction entry."
  ],
  "invalidation_conditions": [
    "Revenue growth deteriorates in the next filing.",
    "Price closes below the 200-day moving average."
  ],
  "next_review_date": "2026-05-03",
  "data_quality": {
    "status": "usable",
    "missing_fields": [],
    "stale_fields": []
  }
}
```

---

## Backtesting Rules

Backtests must be honest.

Rules:

- No future data leakage.
- Train/test split must respect time order.
- Compare every strategy to buy-and-hold.
- Include transaction costs.
- Include max drawdown.
- Include number of trades.
- Do not optimize parameters until the chart looks good.
- Use walk-forward validation once basic backtests work.

Minimum backtest output:

```yaml
strategy: trend_following
symbol: AAPL
period: 2018-01-01_to_2026-04-26
return_strategy: 0.82
return_buy_hold: 1.10
max_drawdown_strategy: -0.22
max_drawdown_buy_hold: -0.31
trades: 18
win_rate: 0.50
sharpe_estimate: 0.74
conclusion: "Did not beat buy-and-hold, but reduced drawdown."
```

---

## Notification Rules

Alerts should be review prompts, not commands.

Good:

```text
Review NVDA: price broke below 50-day average on high volume. Momentum score fell from rank 8 to rank 4 of 10. No sell action was taken.
```

Bad:

```text
Sell NVDA now.
```

Alert severity:

- `info`: useful update.
- `review`: meaningful signal changed.
- `urgent_review`: portfolio risk or major news changed.

---

## AI Prompt Contract

The system prompt should say:

```text
You are an investing research assistant for a beginner investor.
You are not a financial advisor and you do not execute trades.
Use only the evidence packet provided by the application.
Do not invent metrics, prices, dates, filings, analyst ratings, or news.
If data is stale, missing, or contradictory, lower confidence or return INSUFFICIENT_DATA.
Return only structured JSON matching the evidence card schema.
```

---

## TODO — Follow-Up Gaps (Next Pass)

Three gaps identified in `[[Research - Trading Fundamentals Gap Fill (2026-06-25)]]` are not yet implemented. Flag them for the strategy engine revision that follows Kiro task completion:

1. **RankIC tracking:** The strategy engine currently computes strategy scores but does not track how well those scores *rank* the 10 symbols by forward return. Cross-sectional ranking ability (RankIC) is the actual measure of whether the strategy adds value over equal-weight holding. Add a RankIC audit after enough paper-trade history accumulates (minimum: 6 months of monthly rankings + realized 1-month returns).

2. **VIX-based confidence decay:** High-volatility market regimes (VIX > 25) break trend-following signals faster and make mean-reversion signals more dangerous. The Risk Manager agent should apply a confidence cap multiplier based on current VIX level. Not yet implemented.

3. **Benchmark-relative tracking in paper journal:** Every paper position entry should record what VOO returned over the same holding period. Without this comparison, it is impossible to honestly evaluate whether the strategy earned alpha or just rode market returns. Add `voo_return_same_period` as a required field in the paper journal schema.

**Also deferred:** Kronos model integration (`kronos_score`). Gated on the Phase A RankIC validation pass described in `[[Research - Kronos Foundation Model Deep Dive (2026-06-25)]]`. Do not add Kronos to the evidence packet until that validation confirms RankIC > 0.03 on the V1 universe.

---

## What I Learn From This Project

Technology:

- Python data pipelines.
- API integration.
- SQL/DuckDB.
- Feature engineering.
- Backtesting.
- Structured AI outputs.
- Dashboard design.
- Scheduling and alerts.

Markets:

- ETFs vs individual stocks.
- Trend vs value vs quality.
- Risk management.
- Earnings and filings.
- Market data limitations.
- Why prediction is hard.

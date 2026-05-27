---
type: concept
status: sprout
created: 2026-04-26
updated: 2026-04-26
related_progress:
  - "[[Trading with Ai]]"
  - "[[AI Market Analyzer - AI Engine Architecture]]"
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[AI Market Analyzer - Data Sources]]"
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

### 2. Trend Following Strategy

Purpose:

- Identify assets already moving in a healthy direction.

Signals:

- Price above 50-day moving average.
- Price above 200-day moving average.
- 50-day moving average above 200-day moving average.
- Relative strength vs SPY or VOO.
- Volume confirmation on breakouts.

Possible actions:

- `WATCH`: trend is forming but not confirmed.
- `ACCUMULATE`: trend is healthy and valuation/risk is acceptable.
- `REDUCE`: trend breaks key moving averages.

Beginner warning:

- Trend following can buy late.
- It needs risk rules.

### 3. Mean Reversion Strategy

Purpose:

- Identify temporary overreaction or pullback setups.

Signals:

- RSI below 30 or above 70.
- Price stretched below/above moving average.
- Bollinger band touch.
- Short-term drawdown relative to normal volatility.

Possible actions:

- `WATCH`: stock is oversold but fundamentals/news need review.
- `ACCUMULATE`: pullback in a high-quality asset with no major thesis break.
- `AVOID`: falling stock with deteriorating fundamentals.

Beginner warning:

- Cheap can get cheaper.
- Mean reversion without quality filters is dangerous.

### 4. Quality Compounder Strategy

Purpose:

- Find companies worth holding for longer periods.

Signals:

- Revenue growth.
- Gross/operating margin strength.
- Positive free cash flow.
- Reasonable debt.
- Consistent profitability.
- Durable sector/industry position.

Possible actions:

- `ACCUMULATE`: quality is strong and price/risk is acceptable.
- `HOLD`: business remains strong but valuation is not attractive.
- `WATCH`: quality is promising but evidence is incomplete.

Beginner warning:

- Great companies can be bad buys at extreme prices.

### 5. Valuation Sanity Strategy

Purpose:

- Prevent buying hype blindly.

Signals:

- P/E.
- Forward P/E if available.
- P/S.
- P/FCF.
- EV/EBITDA if available.
- Comparison to sector or own historical range.

Possible actions:

- `HOLD`: valuation is stretched but business quality supports patience.
- `WATCH`: wait for better price or stronger evidence.
- `AVOID`: valuation requires unrealistic growth.

Beginner warning:

- Valuation metrics differ by sector.
- Early-growth companies may look expensive for years.

## Strategy Score Packet

Each strategy should produce a structured packet:

```yaml
symbol: MSFT
strategy: quality_compounder
score: 78
action_hint: HOLD
confidence_hint: 0.71
signals:
  positive:
    - "Revenue growth remains positive."
    - "Operating margin is strong."
  negative:
    - "Valuation is above broad market average."
  neutral:
    - "Momentum is stable but not accelerating."
risk_flags:
  - "Upcoming earnings can reprice the stock."
data_quality:
  status: usable
  max_confidence: 0.75
```

The AI receives this packet. It does not compute the packet from scratch.

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

## Notification Rules

Alerts should be review prompts, not commands.

Good:

```text
Review NVDA: price broke below 50-day average on high volume. Momentum score fell from 82 to 61. No sell action was taken.
```

Bad:

```text
Sell NVDA now.
```

Alert severity:

- `info`: useful update.
- `review`: meaningful signal changed.
- `urgent_review`: portfolio risk or major news changed.

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

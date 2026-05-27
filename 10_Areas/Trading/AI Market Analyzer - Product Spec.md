---
type: project
status: sprout
created: 2026-04-26
updated: 2026-04-26
related_progress:
  - "[[Trading with Ai]]"
  - "[[AI Market Analyzer - Data Sources]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[AI Market Analyzer - 4 Month Build Plan]]"
tags:
  - trading
  - ai
  - product-spec
track:
  - trading
  - ai
next: "[[AI Market Analyzer - Data Sources]]"
---

# AI Market Analyzer - Product Spec

## Product Thesis

Build a personal investing app that helps me make smarter decisions by combining verified company data, market data, strategy checks, portfolio context, and AI-generated explanations.

The app should not say "buy this because AI thinks so." It should say:

> Here is the evidence, here is the strategy being applied, here is the risk, here is what would invalidate the idea, and here is what you should review next.

## Audience

Primary user: me.

Current level:

- Beginner investor.
- Beginner trader.
- CS student trying to learn AI/data systems professionally.
- Low budget.
- Wants to build something useful and portfolio-worthy.

This means the app must be practical, educational, and honest.

## Non-Goals

Do not build these in v1:

- Auto-trading.
- Broker execution.
- Options strategies.
- Crypto.
- Social trading.
- Public financial advice.
- Day-trading scalping tools.
- Paid institutional-style terminal clone.
- Complex real-time streaming infrastructure.

## Core Screens

### 1. Dashboard

Shows:

- Portfolio summary.
- Watchlist summary.
- Market overview.
- Today's alerts.
- Latest AI evidence cards.
- Stocks needing review.
- Data freshness status.

Dashboard cards:

- Portfolio value.
- Unrealized gain/loss.
- Watchlist count.
- High-risk positions.
- New review signals.
- Data pipeline last successful run.

### 2. Portfolio Tracker

Tracks real or manual positions:

```yaml
symbol: VOO
asset_type: ETF
shares: 3.25
average_cost: 428.10
account: Fidelity
thesis: "Long-term broad market exposure."
time_horizon: years
risk_level: low
opened_at: 2026-04-26
review_frequency: monthly
```

V1 can use manual input. Broker sync is deferred.

### 3. Watchlist

Tracks stocks/ETFs I am researching.

Fields:

- Symbol.
- Company/name.
- Reason for watching.
- Strategy tags.
- Target review price.
- Alert rules.
- Last evidence card.
- Data status.

Example watchlist reasons:

- "Long-term ETF baseline."
- "Strong trend, waiting for pullback."
- "AI infrastructure company."
- "High-quality business, valuation too high."

### 4. Stock Detail Page

Shows:

- Price chart.
- Technical indicators.
- Fundamentals.
- Valuation metrics.
- News.
- Earnings/filing events.
- Strategy scores.
- AI evidence card.
- Backtest result for relevant strategy.

The app from the transcript is useful here: TradingView widgets can provide charts and market visuals, but backend decisions should use our own stored data and explicit source timestamps.

### 5. Strategy Lab

Lets me test strategies before trusting them.

V1 strategies:

- ETF baseline.
- Trend following.
- Mean reversion.
- Quality compounder.
- Value sanity check.

Each strategy should show:

- Entry logic.
- Exit logic.
- Time horizon.
- Backtest period.
- Win rate.
- Max drawdown.
- Sharpe ratio if available.
- Compared-to-buy-and-hold result.

### 6. Evidence Card Feed

The main AI output.

Possible actions:

- `ACCUMULATE`
- `HOLD`
- `WATCH`
- `REDUCE`
- `AVOID`
- `INSUFFICIENT_DATA`

For v1, avoid direct `BUY` and `SELL` wording in the UI. Use softer decision language until the system is more mature.

### 7. Alerts

V1 alert types:

- Price crosses moving average.
- RSI overbought/oversold.
- Large one-day move.
- Earnings/filing detected.
- News sentiment shock.
- Watchlist stock needs review.
- Portfolio position violates risk rule.

Alerts should not say "sell now." They should say "review this because X changed."

## AI Behavior

The AI should answer:

- What changed?
- Why does it matter?
- Which strategy does this affect?
- What is the evidence?
- What is the opposing evidence?
- What should I review next?

The AI should not answer from memory when live data is required. It must use retrieved/stored facts from the data engine.

## Success Criteria

V1 is successful when:

- I can track 5-10 portfolio/watchlist assets.
- I can generate evidence cards for each asset.
- Each evidence card has source timestamps.
- I can run at least 3 backtests.
- The AI refuses or downgrades confidence when data is weak.
- The dashboard is useful enough to review weekly.
- The README explains the architecture and limitations honestly.


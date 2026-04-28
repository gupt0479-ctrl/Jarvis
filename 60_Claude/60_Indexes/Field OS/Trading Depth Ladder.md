---
type: evergreen
status: tree
tags:
  - dashboard
  - capability
  - depth-ladder
created: 2026-04-25
updated: 2026-04-25
notes:
  - "[[Trading Field OS]]"
  - "[[Trading Question Bank]]"
  - "[[BOOM Board]]"
---
# Trading Depth Ladder

Modeled after the [[BOOM Board]]. Trading track covers technical analysis, risk management, backtesting, order flow, and trading automation.

## Core Concepts

- [[Trading with Ai]]
- [[Reddit|Trading Reddit Resources]]
- [[10_Areas/Trading/Links|Trading Links]]

Placeholder concepts to seed as enriched notes:

- Technical Analysis (support/resistance, candlestick patterns, indicators)
- Risk Management (position sizing, stop losses, risk/reward ratios)
- Backtesting (strategy validation, overfitting, walk-forward analysis)
- Order Flow (bid/ask dynamics, volume profile, market microstructure)

## Compare and Discriminate

| Concept A | Concept B | What to clarify |
|---|---|---|
| Technical analysis | Fundamental analysis | Technical reads price and volume patterns. Fundamental reads earnings, balance sheets, and macro data. Technical works on shorter timeframes; fundamental works on longer ones. Most retail traders blend both badly. |
| Backtesting | Paper trading | Backtesting runs a strategy against historical data. Paper trading runs it forward in real time with fake money. Backtesting is faster but prone to overfitting; paper trading is slower but tests execution and psychology. |
| Risk management | Position sizing | Risk management is the whole framework (max drawdown, correlation limits, stop rules). Position sizing is one tool within it — how much capital per trade. You can have good position sizing and still blow up if you ignore correlated positions. |

## 30-Minute Refresher

1. [[Trading with Ai]]
2. Review risk management fundamentals
3. Review one recent trade setup

## 2-Hour Technical Refresher

1. [[Trading with Ai]]
2. [[10_Areas/Trading/Links|Trading Links]] — review current tool stack
3. Walk through a backtesting example
4. Review position sizing rules
5. Analyze one real trade with entry/exit reasoning

## Deep Relearning Pass

Start at [[10_Areas/Trading/Links|Trading Links]] and work through each resource. Then review clippings tagged with trading for recent captures.

## Overdue Drills

```dataview
TABLE mastery_level, difficulty, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND contains(track, "trading") AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## All Tracked Trading Concepts

```dataview
TABLE mastery_level, difficulty, status, next_drill
FROM ""
WHERE type = "concept" AND contains(track, "trading")
SORT file.name ASC
```

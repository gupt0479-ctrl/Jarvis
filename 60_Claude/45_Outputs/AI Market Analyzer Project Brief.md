---
type: output
status: seed
created: 2026-04-25
updated: 2026-04-25
tags:
  - output
track:
  - ai
  - trading
output_kind: project-brief
source_concepts:
  - "[[60_Claude/20_Distilled_Notes/AI-Assisted Trading]]"
  - "[[60_Claude/20_Distilled_Notes/Trading Tools and Platforms]]"
  - "[[40_Resources/CS/AI/AI Workflow]]"
---

# AI Market Analyzer Project Brief

## Problem

Most retail AI trading tools are black boxes that provide pre-built analysis. Building your own gives you a portfolio project that demonstrates data pipeline engineering, ML model evaluation, and API integration — even if the strategy doesn't beat the market.

## Scope

Build a market analysis dashboard that pulls daily price data, computes technical indicators, runs a simple classifier for next-day direction, and displays signals with historical performance.

## Architecture

1. **Data pipeline**: Alpha Vantage or Yahoo Finance API → daily price data → local storage (SQLite or Postgres)
2. **Feature engineering**: moving averages, RSI, volume changes, Bollinger bands
3. **Model**: random forest or gradient boosting classifier for next-day direction
4. **Backtesting**: train/test split on historical data, measure accuracy and Sharpe ratio
5. **Dashboard**: Next.js frontend showing signals, performance charts, and model confidence

## Stack

- Python (pandas, scikit-learn) for data pipeline and model
- Next.js + Tailwind for dashboard
- SQLite for local storage
- Alpha Vantage API for market data

## Success Criteria

- Pipeline runs daily and stores 1+ year of historical data
- Model accuracy on held-out data is measurable (even if barely above random)
- Dashboard shows current signals and historical performance
- README documents architecture decisions and honest performance assessment

## Honest Assessment

Most simple models barely beat random on out-of-sample data. The engineering value is in the pipeline, not the predictions. Document this honestly — it shows maturity.

## Timeline

- Week 1: Data pipeline + storage
- Week 2: Feature engineering + model training
- Week 3: Backtesting framework + evaluation
- Week 4: Dashboard + documentation

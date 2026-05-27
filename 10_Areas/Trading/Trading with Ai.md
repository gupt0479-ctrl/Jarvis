---
type: project
status: sprout
created: 2026-04-26
updated: 2026-04-26
related_progress:
  - "[[Stocks Trading AI Hub]]"
  - "[[Trading Tools and Platforms]]"
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[AI Market Analyzer - Data Sources]]"
  - "[[AI Market Analyzer - AI Engine Architecture]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[AI Market Analyzer - 4 Month Build Plan]]"
tags:
  - trading
  - ai
  - investing
  - project
track:
  - trading
  - ai
next: "[[AI Market Analyzer - 4 Month Build Plan]]"
---

# Trading With AI

## Source Of Truth

This project is not a get-rich-quick trading bot. It is a personal investing intelligence system that helps me learn markets, track my investments, evaluate companies, test strategies, and make more disciplined decisions.

The app should be built as an **advisor-only system** first. It can explain what looks attractive, risky, overextended, undervalued, or worth watching, but it must not place trades automatically. Any real buy/sell decision stays with me.

The first version focuses on:

- US stocks and ETFs.
- Weeks-to-months investing decisions.
- Evidence cards instead of vague chat answers.
- Low-budget data sources.
- Python-first analysis before a polished web app.

## The Core Problem

I want to invest money more intelligently, but I am a beginner in both investing and AI. That creates three risks:

1. I may trust weak signals because they look technical.
2. I may confuse AI confidence with factual correctness.
3. I may overbuild a flashy dashboard before I understand markets.

The app should solve this by forcing every recommendation through a structured process:

```text
portfolio/watchlist
-> verified market and company data
-> deterministic strategy checks
-> risk and freshness checks
-> AI synthesis
-> evidence card
-> human decision
```

The AI is the final explainer, not the source of truth.

## What The App Should Become

Working name: **MarketLens AI** or **SignalLab**.

The product should help me answer:

- What do I own?
- What am I watching?
- Why did a stock move?
- Is this company fundamentally strong?
- Is the chart trend healthy or breaking down?
- Is the current price attractive, stretched, or too risky?
- What strategy is being applied here?
- What evidence supports this suggestion?
- What would make the suggestion wrong?
- When should I review this again?

The best version of this app feels like a personal research desk:

- Portfolio tracker.
- Watchlist.
- Stock/ETF detail page.
- Strategy lab.
- Daily digest.
- Alert engine.
- AI evidence card.
- Learning journal.

## What The AI Is Allowed To Do

The AI can:

- Summarize verified data.
- Explain technical indicators in beginner language.
- Compare strategy signals.
- Point out risks and contradictions.
- Generate an evidence card.
- Help me learn why an investment might be good or bad.
- Ask for more data when the evidence is weak.

The AI cannot:

- Invent numbers.
- Provide a recommendation without source timestamps.
- Claim real-time accuracy if the data is delayed.
- Recommend a trade when data quality is poor.
- Execute trades.
- Hide uncertainty.
- Present backtest results as future guarantees.

If data is stale, missing, contradictory, or low quality, the AI must return:

```text
WATCH
INSUFFICIENT_DATA
NEEDS_REVIEW
```

not a confident buy or sell.

## V1 Recommendation Format

Every AI output should become an evidence card with this shape:

```yaml
symbol: AAPL
as_of: 2026-04-26T16:00:00-05:00
action: WATCH
confidence: 0.62
time_horizon: weeks_to_months
thesis: "Strong quality business, but current momentum is mixed and valuation needs comparison."
evidence:
  - source: price_history
    point: "Price remains above the 200-day moving average."
  - source: fundamentals
    point: "Margins remain strong relative to many large-cap peers."
  - source: news
    point: "Recent headlines do not show an obvious company-specific shock."
risks:
  - "Valuation may already price in optimistic growth."
  - "Upcoming earnings can invalidate the signal."
invalidation:
  - "Close below 200-day moving average with rising volume."
  - "Revenue or margin deterioration in next filing."
next_review: 2026-05-03
data_quality:
  status: usable
  stale_fields: []
  missing_fields: []
```

The output should be structured JSON in the actual application, then rendered as a card in the UI.

## Beginner Investing Rules

These rules must shape the app:

- Emergency savings comes before investing.
- High-interest debt comes before stock picking.
- Broad ETFs are the default baseline.
- Individual stocks should be treated as higher-risk research positions.
- Never risk money needed within the next few years.
- A good investment process can still lose money.
- A profitable backtest can still fail live.
- More trades does not mean more intelligence.

The app should teach these rules while I build it.

## Target V1

V1 should be useful even before it has a full Next.js interface.

Build order:

1. Python data engine.
2. Local database.
3. Watchlist and portfolio tracker.
4. Strategy scoring engine.
5. Backtesting notebook or CLI.
6. AI evidence card generator.
7. Streamlit dashboard.
8. Optional Next.js web app after the engine works.

## Reference Notes

- [[AI Market Analyzer - Product Spec]]
- [[AI Market Analyzer - Data Sources]]
- [[AI Market Analyzer - AI Engine Architecture]]
- [[AI Market Analyzer - Strategy Engine]]
- [[AI Market Analyzer - 4 Month Build Plan]]
- [[Trading Tools and Platforms]]
- [[Links]]

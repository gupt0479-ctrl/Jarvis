---
type: concept
status: sprout
created: 2026-04-26
updated: 2026-04-26
related_progress:
  - "[[Trading with Ai]]"
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
tags:
  - trading
  - data
  - api
  - source-of-truth
track:
  - trading
  - ai
next: "[[AI Market Analyzer - Strategy Engine]]"
---

# AI Market Analyzer - Data Sources

## Data Principle

The app is only as good as its data. The AI must not be allowed to invent or silently correct missing data. Every evidence card must know:

- Source.
- Timestamp.
- Whether the data is delayed, end-of-day, or near real-time.
- Whether a field is missing.
- Whether sources disagree.

If data quality is poor, the app should block confident recommendations.

## Primary Data Sources

### Financial Modeling Prep

Use for:

- Price history.
- Company profile.
- Financial statements.
- Ratios.
- Market news.
- Basic fundamentals.

Why:

- Low-cost API.
- Useful financial endpoints.
- Free plan is enough for experimentation.
- Starter plan is close to the chosen budget if needed.

Current pricing note from official FMP pricing page:

- Basic/free: 250 calls/day.
- Starter: listed at $22/month billed annually, with more API capacity and US coverage.

Source:

- https://site.financialmodelingprep.com/pricing-plans
- https://site.financialmodelingprep.com/developer/docs

V1 rule:

- Start on free plan.
- Upgrade only if the daily pipeline hits limits during real usage.

### SEC EDGAR

Use for:

- Official company filings.
- Submissions history.
- XBRL company facts.
- Cross-checking fundamentals for important decisions.

Why:

- Official source.
- No API key required.
- Useful for validating financial statement data.

Important details from SEC docs:

- `data.sec.gov` hosts RESTful JSON APIs.
- APIs include submissions history and XBRL data.
- SEC says the JSON structures are updated throughout the day as submissions are disseminated.
- Bulk ZIP files are republished nightly.
- CORS is not supported, so the app should fetch SEC data from backend/server code, not directly from browser UI.

Source:

- https://www.sec.gov/edgar/sec-api-documentation

V1 rule:

- Use SEC as a validation and learning source, not the only source for every dashboard field.

### TradingView Widgets

Use for:

- Charts.
- Market overview.
- Symbol overview.
- Watchlist-style display.
- Heatmap.

Why:

- Excellent UI.
- Free embeddable widgets.
- Good enough for visual market context.

Important limitation:

- TradingView widgets are display widgets. Do not treat widget-rendered data as backend strategy input unless the terms and technical API support that use.

Sources:

- https://www.tradingview.com/widget-docs/widgets/charts/advanced-chart
- https://www.tradingview.com/widget-docs/widgets/charts/advanced-chart/demos

V1 rule:

- Use TradingView for visual charting only.
- Use stored API data for strategy calculations and AI evidence.

### Alpha Vantage

Use for:

- Backup market data.
- Indicator experiments.
- Learning API integration.

Current official pricing note:

- Alpha Vantage says many endpoints are free.
- The standard free usage limit is 25 API requests/day.
- Premium removes daily limits and unlocks additional features.

Source:

- https://www.alphavantage.co/premium/

V1 rule:

- Use as fallback, not primary, unless FMP is insufficient.

## Optional Sources Later

### Finnhub

Useful for:

- Quotes.
- Company news.
- Basic financials.
- Analyst/recommendation style data depending on plan.

Use if FMP is weak for news or if a Next.js app needs a simple API.

### Yahoo Finance

Useful for:

- Prototyping with unofficial libraries.
- Quick local experiments.

Risk:

- Unofficial packages can break.
- Licensing and reliability may be unclear.

Use only for local learning, not as the durable production data source.

## Data Freshness Rules

Every stored data table should include:

```yaml
source: fmp
source_url: "..."
retrieved_at: 2026-04-26T17:00:00-05:00
data_as_of: 2026-04-26
freshness: end_of_day
quality_status: usable
```

Freshness statuses:

- `real_time`
- `delayed`
- `end_of_day`
- `filing_based`
- `stale`
- `unknown`

Quality statuses:

- `usable`
- `partial`
- `conflicting`
- `missing`
- `stale`

## Data Model V1

Tables or DuckDB relations:

### assets

```yaml
symbol: string
name: string
asset_type: stock | etf
exchange: string
sector: string
industry: string
source: string
last_updated_at: datetime
```

### prices_daily

```yaml
symbol: string
date: date
open: float
high: float
low: float
close: float
adjusted_close: float
volume: int
source: string
retrieved_at: datetime
```

### fundamentals

```yaml
symbol: string
period: annual | quarterly
fiscal_date: date
revenue: float
gross_margin: float
operating_margin: float
net_income: float
free_cash_flow: float
debt: float
cash: float
shares_outstanding: float
source: string
retrieved_at: datetime
```

### portfolio_positions

```yaml
symbol: string
shares: float
average_cost: float
opened_at: date
thesis: string
risk_level: low | medium | high
review_frequency: weekly | monthly | quarterly
```

### watchlist

```yaml
symbol: string
reason: string
strategy_tags: list
created_at: datetime
review_after: date
```

### evidence_cards

```yaml
symbol: string
created_at: datetime
action: string
confidence: float
strategy: string
data_quality_status: string
json_payload: object
```

## Source Reliability Policy

Recommendation confidence should be capped by data quality:

| Data condition | Max confidence |
|---|---:|
| Fresh price + fundamentals + no conflicts | 0.85 |
| Fresh price but stale fundamentals | 0.70 |
| Price only, no fundamentals | 0.55 |
| Conflicting source data | 0.45 |
| Missing or stale critical data | 0.30 |

The app should explain this cap in the evidence card.


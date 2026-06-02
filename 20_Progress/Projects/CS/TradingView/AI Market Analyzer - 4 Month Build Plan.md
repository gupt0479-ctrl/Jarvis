---
type: project
status: sprout
created: 2026-04-26
updated: 2026-04-26
deadline: 2026-08-31
related_progress:
  - "[[Trading with Ai]]"
  - "[[AI Market Analyzer - Product Spec]]"
  - "[[AI Market Analyzer - Data Sources]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
tags:
  - trading
  - ai
  - roadmap
  - project
track:
  - trading
  - ai
next: "Week 1: set up Python repo, data source keys, and local asset database"
---
# AI Market Analyzer - 4 Month Build Plan

## Goal

By August 31, 2026, build a personal AI market analyzer that I can actually use weekly to track investments, research US stocks/ETFs, run strategy checks, and generate evidence-based AI recommendations.

The project should produce:

- Working Python analysis engine.
- Local database.
- Watchlist and portfolio tracker.
- Strategy scoring system.
- Backtests.
- AI evidence cards.
- Streamlit dashboard.
- Portfolio-ready README and demo.

## Month 1 - Data Foundation

Theme: make data reliable before making AI impressive.

### Week 1: Project Setup

Deliverables:

- Python repo created.
- `README.md` with project thesis and non-goals.
- `.env.example` with expected API keys.
- Basic folder structure:

```text
market-analyzer/
  app/
  data/
  notebooks/
  src/
    ingestion/
    storage/
    indicators/
    strategies/
    ai/
    dashboard/
  tests/
```

Tasks:

- Set up Python environment.
- Choose DuckDB or SQLite. Default: DuckDB for analytics.
- Create symbols seed list: VOO, VTI, SPY, QQQ, AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA.
- Get FMP API key.
- Test SEC EDGAR request for one company.

Done when:

- One command fetches and stores basic data for 3 symbols.

### Week 2: Price Data Pipeline

Deliverables:

- Daily price ingestion.
- `prices_daily` table.
- Data freshness metadata.
- Basic CLI command:

```bash
python -m src.ingestion.prices --symbols AAPL MSFT VOO
```

Tasks:

- Fetch 1-5 years of daily OHLCV data.
- Store adjusted close.
- Prevent duplicate rows.
- Log source and retrieval time.
- Add failure handling for missing API key and rate limits.

Done when:

- 10 symbols have daily prices stored locally.

### Week 3: Fundamentals And Company Profiles

Deliverables:

- Company profile ingestion.
- Basic financial metrics ingestion.
- SEC cross-check for one company.

Tasks:

- Store sector, industry, exchange, market cap.
- Store revenue, margins, income, debt, cash, free cash flow where available.
- Add `quality_status` to each dataset.
- Document which fields come from FMP vs SEC.

Done when:

- AAPL and MSFT have both API fundamentals and at least one SEC validation path documented.

### Week 4: Portfolio And Watchlist

Deliverables:

- Manual portfolio tracker.
- Watchlist tracker.
- First text-based review report.

Tasks:

- Add positions manually.
- Add watchlist reasons and strategy tags.
- Compute current unrealized gain/loss.
- Generate a plain Markdown daily/weekly report.

Done when:

- I can enter my holdings/watchlist and generate a readable report.

## Month 2 - Strategy Engine

Theme: make strategy logic explicit and testable.

### Week 5: Technical Indicators

Deliverables:

- Indicator calculations.
- Indicator table per symbol.

Tasks:

- Moving averages: 20, 50, 200.
- RSI.
- Bollinger bands.
- Volatility.
- Drawdown.
- Relative strength vs VOO or SPY.

Done when:

- Each watchlist symbol has a technical summary.

### Week 6: Strategy Scores

Deliverables:

- Trend following score.
- Mean reversion score.
- Quality score.
- Valuation sanity score.

Tasks:

- Produce strategy score packets.
- Add positive/negative/neutral signal lists.
- Add risk flags.
- Cap confidence by data quality.

Done when:

- Each symbol has a deterministic strategy packet before AI touches it.

### Week 7: Backtesting V1

Deliverables:

- Backtest runner.
- Buy-and-hold comparison.
- Performance summary.

Tasks:

- Backtest trend following.
- Backtest mean reversion.
- Include transaction cost assumption.
- Report return, drawdown, trades, win rate, and Sharpe estimate.

Done when:

- At least 3 symbols have honest backtest reports.

### Week 8: Risk Rules

Deliverables:

- Risk scoring.
- Portfolio concentration checks.
- Alert severity policy.

Tasks:

- Detect oversized positions.
- Detect high volatility.
- Detect major drawdown.
- Detect earnings/filing review windows if data exists.
- Generate review alerts.

Done when:

- The app can say what needs review without saying what to trade.

## Month 3 - AI Evidence And Dashboard

Theme: AI explains verified evidence.

### Week 9: Evidence Card Schema

Deliverables:

- JSON schema for evidence cards.
- Local evidence card generator.
- Validation tests.

Tasks:

- Define structured output schema.
- Build evidence packet from deterministic strategy outputs.
- Add refusal rules for weak data.
- Store evidence cards locally.

Done when:

- Evidence cards validate against schema and include source timestamps.

### Week 10: OpenAI Integration

Deliverables:

- AI synthesis function.
- Prompt contract.
- Cost logging.

Tasks:

- Use OpenAI structured outputs.
- Send only evidence packets, not raw uncontrolled prompts.
- Log model, latency, input size, and estimated cost.
- Retry only on schema failure, not bad investment conclusions.

Done when:

- AI creates evidence cards for all watchlist symbols without inventing data.

### Week 11: Streamlit Dashboard

Deliverables:

- Working dashboard.

Screens:

- Portfolio.
- Watchlist.
- Stock detail.
- Strategy scores.
- Evidence cards.
- Backtest results.
- Data freshness.

Done when:

- I can use the dashboard for a weekly review.

### Week 12: Alerts And Digest

Deliverables:

- Daily or weekly digest.
- Local alert feed.

Tasks:

- Generate digest from new evidence cards.
- Add alert severity.
- Add "review by" dates.
- Optional email later; local dashboard first.

Done when:

- The app tells me what changed since the last review.

## Month 4 - Polish, Evaluation, Portfolio

Theme: make it trustworthy and explainable.

### Week 13: Reliability Pass

Deliverables:

- Tests for ingestion and indicators.
- Error handling.
- Data quality dashboard.

Tasks:

- Missing API key test.
- Stale data test.
- Duplicate row test.
- Schema validation test.
- Backtest no-lookahead checklist.

Done when:

- Failures are visible and understandable.

### Week 14: Strategy Review

Deliverables:

- Strategy documentation.
- Backtest write-up.
- Lessons learned note.

Tasks:

- Compare strategies to ETF baseline.
- Write what worked and what failed.
- Document overfitting risks.

Done when:

- The project sounds mature instead of hype-driven.

### Week 15: Optional Web Layer

Decision:

- If Streamlit is enough, polish Streamlit.
- If portfolio presentation needs stronger UI, build a thin Next.js frontend that reads from exported JSON/API.

Do not rebuild the engine in Next.js. Keep Python as the source of truth.

Deliverables if Next.js is chosen:

- Landing dashboard.
- Stock detail page.
- Evidence card UI.
- TradingView widget embeds.

### Week 16: Final Packaging

Deliverables:

- Demo video.
- README.
- Architecture diagram.
- Portfolio bullet.
- Technical blog post.
- Future roadmap.

README must include:

- What the app does.
- What it does not do.
- Data sources.
- AI safety boundaries.
- Backtesting honesty.
- Setup instructions.
- Screenshots.

## Weekly Operating Rhythm

Monday:

- Pick one workflow.
- Define acceptance criteria.

Tuesday-Thursday:

- Build and commit daily.

Friday:

- Write a short technical note.
- Update README or dashboard screenshot.

Saturday:

- Run backtest or failure test.

Sunday:

- Review evidence cards.
- Decide next week scope.

## Scoreboard

Track weekly:

| Metric | Target |
|---|---:|
| Commits | 5/week |
| Symbols tracked | +2/week until 20 |
| Evidence cards generated | 5/week |
| Backtests run | 1/week after Week 7 |
| Bugs/failures documented | 1/week |
| README/demo updates | 1/week |

## First Concrete Next Action

Create the Python repo and implement:

```text
fetch prices -> store prices -> compute moving averages -> print one report for AAPL, MSFT, VOO
```

Do not start with AI. Start with data.


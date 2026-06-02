# Personal AI Trading Desk Research And Product Blueprint

## WSL Preflight Note

This document is intended to refine the research artifact originally requested at:

```text
/home/anant_gupta/projects/hub/tradingview/RESEARCH.md
```

The current Windows shell cannot access that WSL path. `wsl -l -v` reports that no WSL distributions are installed, and `\\wsl$` is not available from this session. Because of that, this implementation creates the refined artifact in the accessible workspace at:

```text
D:\Users\_Anant\10_Areas\Documents\The Plan\tradingview\RESEARCH.md
```

Before reconciling this with the Linux project folder, verify:

```bash
wsl -l -v
test -d /home/anant_gupta/projects/hub
test -d /home/anant_gupta/projects/hub/tradingview
test -f /home/anant_gupta/projects/hub/tradingview/RESEARCH.md
```

Do not overwrite the Linux file without reading it first.

## What Changed From The Earlier Plan

The earlier plan centered too much on TradingView as the product reference. That is not the real target.

The stronger target is a Barebone-like personal AI finance research desk, but with a more disciplined operating system for trading decisions:

- Barebone-style AI financial research.
- TradingView-style visual context where useful.
- TradingAgents-style multi-agent debate.
- Deterministic strategy and risk checks before AI synthesis.
- Paper-trade staging before any real execution.
- A personal journal that records what the system believed, what I approved, what happened, and what I learned.

The product is not being built for sale. It is a private tool for learning markets, improving research quality, and eventually testing whether AI agents can help make disciplined trades.

## Product Thesis

Build a private AI trading operating system that helps me research US stocks and ETFs, generate evidence-backed trade theses, stage paper trades for my approval, and learn from every outcome.

The app should bridge manual trading and future autonomy. V1 should not trade real money and should not autonomously place orders. It should let AI agents research, debate, score, and propose paper trades. I approve or reject every staged trade.

The goal is not to create a magic prediction bot. The goal is to create a repeatable decision process:

```text
market universe
-> free trusted data
-> deterministic strategy checks
-> multi-agent research debate
-> risk manager review
-> paper trade proposal
-> human approval
-> journaled outcome
-> lessons fed back into future research
```

## Barebone Deep Dive

Barebone is the closest product reference discovered so far. Public app listings describe Barebone as an AI finance research app that gives users a team of AI Wall Street analysts, personalized financial research agents, real-time market trends and sentiment, fundamental analysis, technical analysis, financial data analysis, breaking news, investment insights, and asset or industry comparisons.

Its App Store listing also mentions newer research features:

- Earnings transcript summaries.
- Pre-earnings checklists.
- Polymarket earnings odds.
- Enhanced market brief.
- Enhanced news reports.
- Smart investor activity tracking across top fund managers such as Buffett, Soros, and Ackman.

Barebone explicitly says it is not an investment advisory tool and does not execute trades. The app listing frames it as informational research software, not a broker.

### What Barebone Appears To Be Good At

Barebone appears to compress financial research into a mobile-first AI experience:

- Fast stock and market summaries.
- AI-generated explanations.
- Technical and fundamental analysis in one place.
- News and sentiment context.
- Comparative research across assets and industries.
- Earnings event support.
- Tracking prominent investors and fund managers.

This is useful because a beginner does not yet know which sources to inspect, which metrics matter, or how to synthesize a large amount of market information quickly.

### Barebone Gaps To Solve Personally

The opportunity is not to make a prettier Barebone clone. The opportunity is to build the version that is useful for one serious personal workflow.

Gaps to solve:

| Gap | Personal App Response |
|---|---|
| Research output can feel like polished AI prose without enough audit trail. | Every evidence card must show source, timestamp, and missing data. |
| It is unclear whether strategy logic is deterministic or mostly AI-generated. | Python computes signals first; AI only explains and debates the evidence. |
| No personal research memory owned locally. | Store theses, rejected trades, paper trades, results, and lessons in a local journal. |
| No transparent backtest layer. | Every strategy module must show historical behavior versus buy-and-hold. |
| No staged autonomy ladder. | Move from research-only to approved paper trades before autonomous paper testing. |
| Subscription and privacy tradeoffs. | Zero-cost-first local system using public data where possible. |
| No direct control over agent roles. | Define agents, deliverables, failure modes, and success metrics explicitly. |

### Product Lesson From Barebone

Barebone shows that the winning user experience is not raw charts or raw chat. The useful shape is a structured finance research assistant that turns scattered data into decision-ready insight.

Our app should go further in one direction: decision accountability. Every card should answer:

- What is the trade or watch thesis?
- What evidence supports it?
- What evidence disagrees?
- What would invalidate it?
- What data is stale, missing, or weak?
- What happened when similar setups were tested historically?
- Would this beat simply buying a broad ETF?
- What did I decide, and what happened next?

## What Are We Actually Building?

Working name: `Personal AI Trading Desk`.

This is a private web app and Python research engine for supervised AI-assisted trading research. It is not a public SaaS, not a broker, not financial advice, and not an autonomous real-money trading bot.

V1 focuses on US-listed stocks and ETFs because they give the best balance of:

- Free and trusted public data.
- SEC filings.
- Insider transaction forms.
- Institutional 13F filings.
- Broad ETF benchmarks.
- Paper-trading support.
- Beginner-friendly risk controls.
- Real companies with fundamentals that can be studied.

The product should help answer:

- What should I study this week?
- Which stocks or ETFs are worth watching?
- What changed since the last review?
- Is this setup trend, mean-reversion, quality, valuation, or event-driven?
- What are the strongest arguments for and against the trade?
- What would prove the thesis wrong?
- Should I stage a paper trade?
- What did I learn from the last trade?

## Non-Negotiable Constraints

- Zero cost first. Use free data, local storage, free paper-trading tools, and no paid market data unless explicitly justified later.
- Personal use only. Do not design for multiple users, billing, or public recommendations.
- US stocks and ETFs only in V1.
- No options, futures, margin, leverage, forex, or crypto in V1.
- No autonomous real-money execution.
- No AI-generated numbers unless they are present in the evidence packet.
- No hidden confidence. Data quality must cap recommendation confidence.
- No direct `BUY NOW` or `SELL NOW` language.
- No claim that the system can consistently beat the market.

## Trading Universe Decision

We are analyzing many tradable markets, but choosing one for V1.

| Market | V1 Decision | Reason |
|---|---|---|
| US ETFs | Include | Best beginner baseline, diversified, low minimums, useful benchmark. |
| US large-cap stocks | Include | Strong data availability, SEC filings, liquidity, fundamentals. |
| Crypto | Defer | High volatility, weaker fundamental anchors, fraud risk, 24/7 noise. |
| Options | Defer | Leverage, Greeks, expiry risk, assignment risk, beginner complexity. |
| Futures | Defer | High leverage, specialized risk, not beginner-safe. |
| Forex | Defer | Macro-driven, leverage-heavy, harder edge for beginner. |
| Prediction markets | Defer | Interesting for event research, but not the first long-term investing lane. |
| Day trading | Defer | Requires speed, discipline, pattern-day-trader constraints, and higher failure risk. |

### V1 Universe

Start with a small universe that can be researched deeply:

- `VOO`
- `VTI`
- `SPY`
- `QQQ`
- `AAPL`
- `MSFT`
- `NVDA`
- `AMZN`
- `GOOGL`
- `META`
- `BRK.B`
- `JPM`
- `COST`
- `TSLA`

The broad ETF baseline is the default benchmark. Every individual stock idea must explain why it deserves attention over simply accumulating a broad ETF.

## Autonomy Ladder

The product should be designed for future autonomy, but earn it slowly.

| Level | Name | Behavior | Status |
|---:|---|---|---|
| 0 | Research only | Agents generate notes and evidence cards. | Supported as base layer. |
| 1 | Evidence cards | App produces structured labels such as `WATCH` or `ACCUMULATE`. | Supported in V1. |
| 2 | Approved paper trades | Agents stage paper trades; I approve or reject. | V1 target. |
| 3 | Autonomous paper loop | Agents place paper trades without approval, with daily review. | Later, after journal evidence. |
| 4 | Tiny supervised real-money trades | Very small real trades with manual approval. | Out of MVP. |
| 5 | Autonomous real-money trading | Agent trades real money independently. | Explicit non-goal until long-term proof exists. |

V1 target is Level 2.

## Strategy Philosophy

The app should not start by trying to predict tomorrow's price. That is the wrong problem for a beginner.

The better strategy is:

- Build a research process.
- Use broad ETFs as the baseline.
- Find high-quality setups.
- Control risk.
- Paper trade before real trading.
- Journal every decision.
- Learn from wrong calls.

AI is useful for synthesis, contradiction finding, and research workflow. Python is responsible for facts, calculations, and tests.

## Actual Strategy V1

V1 is an advisor and supervised paper-trading strategy, not an auto-trader.

Allowed labels:

- `WATCH`
- `HOLD`
- `ACCUMULATE`
- `REDUCE`
- `AVOID`
- `INSUFFICIENT_DATA`

Avoid `BUY`, `SELL`, `GUARANTEED`, `RISK_FREE`, or `CAN'T_LOSE`.

### Strategy Modules

#### 1. ETF Baseline

Purpose:

- Keep the system honest.
- Compare individual ideas against broad market accumulation.
- Teach that doing nothing fancy can be a strong strategy.

Checks:

- VOO/VTI/SPY trend.
- Broad market drawdown.
- QQQ relative strength.
- Whether an individual stock idea adds risk without clear evidence.

#### 2. Trend Following

Purpose:

- Identify assets already moving in a healthy direction.

Signals:

- Price above 50-day moving average.
- Price above 200-day moving average.
- 50-day moving average above 200-day moving average.
- Relative strength versus SPY or VOO.
- Volume confirmation on breakouts.

Failure mode:

- Trend following can buy late and get whipsawed.

#### 3. Mean Reversion

Purpose:

- Identify temporary pullbacks or overreactions.

Signals:

- RSI below 30 or above 70.
- Bollinger Band touch.
- Short-term drawdown relative to volatility.
- Pullback into support while long-term trend remains intact.

Failure mode:

- Cheap can get cheaper if fundamentals are deteriorating.

#### 4. Quality Compounder

Purpose:

- Identify businesses worth studying for longer-term ownership.

Signals:

- Revenue growth.
- Gross and operating margin strength.
- Positive free cash flow.
- Reasonable debt.
- Consistent profitability.
- Durable competitive position.

Failure mode:

- Great companies can be bad trades at extreme valuations.

#### 5. Valuation Sanity

Purpose:

- Prevent hype buying.

Signals:

- P/E.
- P/S.
- P/FCF where available.
- Historical valuation range.
- Sector comparison.
- Growth required to justify valuation.

Failure mode:

- Simple valuation multiples can mislead across sectors and growth stages.

#### 6. Risk Manager

Purpose:

- Prevent one bad idea from damaging the learning process.

Checks:

- Position size.
- Total portfolio concentration.
- Earnings within review window.
- Recent filing or news event.
- Stale or missing data.
- Max loss plan.
- Thesis invalidation condition.

## Multi-Agent Research Design

Use the role-based idea from TradingAgents, but make it stricter and more personal.

| Agent | Responsibility | Inputs | Output | Failure Mode | Success Metric |
|---|---|---|---|---|---|
| Data Auditor | Check freshness and completeness. | Stored prices, filings, fundamentals, news metadata. | Data quality report and confidence cap. | Lets stale data through. | Blocks weak analysis with `INSUFFICIENT_DATA`. |
| Technical Analyst | Score trend, mean reversion, volatility, and volume. | OHLCV, indicators, benchmark data. | Technical score packet. | Overweights chart patterns. | Explains signals without pretending certainty. |
| Fundamentals Analyst | Evaluate business quality. | SEC facts, financial statements, ratios. | Quality and valuation packet. | Ignores sector context. | Identifies business strength and weakness. |
| Sentiment/News Analyst | Summarize current market narrative. | RSS/news metadata, earnings dates, headlines. | Event and sentiment packet. | Treats noise as signal. | Flags meaningful catalysts only. |
| Smart Money Analyst | Track institutional and insider signals. | 13F, Form 4, public fund holdings. | Ownership activity packet. | Blindly copies famous investors. | Uses filings as context, not commands. |
| Bull Case Analyst | Make strongest positive case. | All evidence packets. | Bull thesis with assumptions. | Cherry-picks positives. | States what must be true for upside. |
| Bear Case Analyst | Make strongest negative case. | All evidence packets. | Bear thesis with invalidation risks. | Excessive pessimism. | Finds thesis-breaking risks. |
| Trader | Converts research into a staged paper plan. | Scores, risk report, debate. | Paper trade proposal or no-trade decision. | Overtrades. | Proposes only when evidence is sufficient. |
| Risk Manager | Final review before paper trade. | Proposed trade, portfolio context. | Approve/reject for staging. | Allows oversized or unclear trades. | Enforces position size and invalidation rules. |
| Student Tutor | Explains the decision in beginner language. | Final card and evidence. | Learning note. | Oversimplifies. | Improves my understanding. |

The AI agents should cite only the evidence packet. If a claim is not in the packet, the agent must ask for more data or label it uncertain.

## Evidence Packet Contract

The deterministic engine builds the packet. The LLM does not invent it.

```yaml
symbol: MSFT
as_of: 2026-05-11T16:00:00-05:00
asset_type: stock
portfolio_context:
  owned: false
  target_role: watchlist
data_quality:
  status: usable
  max_confidence: 0.75
  missing_fields: []
  stale_fields: []
source_timestamps:
  prices: 2026-05-10
  fundamentals: 2026-04-30
  filings: 2026-04-25
  news: 2026-05-11
strategy_scores:
  trend_following:
    score: 72
    action_hint: WATCH
  mean_reversion:
    score: 41
    action_hint: HOLD
  quality:
    score: 83
    action_hint: ACCUMULATE
  valuation:
    score: 58
    action_hint: WATCH
risks:
  - "Earnings within 14 days."
  - "Valuation above broad market average."
benchmark:
  symbol: VOO
  comparison_summary: "Stock has higher concentration and company-specific risk than ETF baseline."
```

## Trade Thesis Contract

Every proposed paper trade needs a written thesis.

```yaml
symbol: MSFT
label: WATCH
setup_type: quality_pullback
time_horizon: weeks_to_months
thesis: "High-quality business, but valuation and earnings risk make this a watchlist setup rather than an immediate staged trade."
supporting_evidence:
  - source: fundamentals
    claim: "Operating margin remains strong."
    as_of: 2026-04-30
opposing_evidence:
  - source: valuation
    claim: "Valuation is not clearly cheap versus broad market baseline."
    as_of: 2026-05-10
invalidation:
  - "Close below 200-day moving average with high volume."
  - "Revenue growth or margin quality deteriorates in the next filing."
paper_order_plan:
  enabled: false
  reason: "Watchlist only until stronger risk/reward."
next_review_date: 2026-05-18
```

## Paper Trade Journal Contract

The journal is the core product moat for personal use.

```yaml
trade_id: 2026-05-11-MSFT-001
symbol: MSFT
created_at: 2026-05-11T16:20:00-05:00
proposed_by: trader_agent
approval_status: rejected
approved_by_user: false
reason_for_decision: "Evidence was useful, but earnings risk was too close."
entry_plan:
  side: buy
  order_type: paper_limit
  planned_price: null
  size_percent_of_paper_portfolio: 2.0
exit_plan:
  invalidation: "Close below 200-day moving average."
  review_after_days: 7
outcome:
  status: not_entered
lesson:
  - "Good business does not automatically mean good setup."
```

## No-Money Testing Plan

### Phase 1: Historical Backtests

Use Python and local data.

Minimum metrics:

- Strategy return.
- Buy-and-hold return.
- Max drawdown.
- Number of trades.
- Win rate.
- Sharpe estimate.
- Transaction cost assumption.
- Performance by market regime where possible.

Rules:

- Preserve time order.
- No lookahead bias.
- No future fundamentals in past decisions.
- No repeated parameter tuning until a chart looks good.
- Show losing examples.
- Compare every strategy to broad ETF accumulation.

### Phase 2: Manual Paper Trading

Use TradingView Paper Trading or a local simulated journal to practice without real money.

The goal is not to prove profitability quickly. The goal is to test:

- Whether the thesis was clear.
- Whether the invalidation rule was clear.
- Whether I followed the plan.
- Whether the agents missed important risks.
- Whether the trade was better than waiting.

### Phase 3: Approved API Paper Trading

Use Alpaca paper trading later if the engine is stable. Alpaca documents paper trading as a free simulation environment for testing algorithms, but also states that paper trading is only a simulation and differs from live trading in market impact, slippage, queue position, fees, dividends, and other real-world effects.

V1 should not depend on Alpaca. It should first support local staged paper trades and journal entries.

## Learning From Great Investors And Traders

This app should study successful investors without turning them into signals to copy blindly.

### Warren Buffett / Berkshire Hathaway

Useful principles:

- Think like a business owner, not a ticker watcher.
- Focus on intrinsic business value.
- Use debt sparingly.
- Compare performance to the S&P 500.
- Be candid about mistakes.
- Long-term ownership matters more than short-term price movement.

Implementation:

- Add a `business_owner_check` to every stock thesis.
- Add a `benchmark_vs_sp500` field to every strategy report.
- Add a `leverage_allowed: false` guardrail.

### Ray Dalio / Bridgewater

Useful principles:

- Market regimes matter.
- Diversification should be based on different economic environments, not just many tickers.
- Humility is necessary because markets are hard to predict.

Implementation:

- Add market regime context: risk-on, neutral, risk-off.
- Track inflation/rates context later if free sources are reliable.
- Lower confidence when regime context conflicts with the setup.

### Jim Simons / Renaissance

Useful principles:

- Systematic research beats casual pattern matching.
- Data quality and testing discipline matter.
- Humans are prone to seeing patterns that are not real.

Implementation:

- Keep strategy calculations deterministic.
- Store backtest assumptions.
- Treat ML as post-MVP.
- Do not pretend to copy Renaissance methods.

### Institutional And Insider Tracking

Barebone's "smart investor activity" idea is worth borrowing, but it must be used carefully.

Useful data:

- SEC Form 13F for institutional investment manager holdings.
- SEC Forms 3, 4, and 5 for insider ownership and transaction reports.

Implementation:

- Use these filings as context only.
- Never copy a fund manager because they bought something.
- Track filing lag.
- Explain that 13F data can be delayed and incomplete for real-time trade decisions.

## Repo Reverse Engineering

### TradingAgents

What it appears to do:

- Implements a multi-agent trading research workflow with analyst roles, debate, trader, risk manager, and portfolio manager.

What to borrow:

- Role separation.
- Bull/bear debate.
- Risk manager before decision.
- Structured analyst handoffs.

What not to copy:

- Do not blindly trust agent conclusions.
- Do not start with real trade execution.
- Do not use AI as the source of market facts.

MVP relevance:

- High. This is the strongest architecture inspiration for agent roles.

### MiroFish

What it appears to suggest:

- Swarm or simulation-style thinking where multiple agents explore possible scenarios.

What to borrow:

- Scenario rooms.
- Narrative simulation.
- Multiple competing interpretations of the same market event.

What not to copy:

- Do not make swarm complexity part of MVP.

MVP relevance:

- Low for V1. Keep as post-MVP research.

### agency-agents

What it appears to provide:

- Agent design discipline: clear roles, deliverables, success metrics, and repeatable workflows.

What to borrow:

- Explicit agent contracts.
- Repeatable task loops.
- Success metrics for each role.

What not to copy:

- Do not over-engineer an agency framework before the trading workflow is proven.

MVP relevance:

- Medium. Useful for discipline, not necessarily implementation dependency.

### OpenTradex / Paperclip Pattern

Your vault also contains notes on OpenTradex, a dashboard-first agent harness for AI-assisted trading workflows.

What to borrow:

- Local coding agent as the research runner.
- Persistent memory files like `SOUL.md` and `strategy_notes.md`.
- A dashboard that streams agent reasoning.
- A thesis submission workflow.
- A risk policy the agent cannot override.

What not to copy:

- Do not start with live execution.
- Do not rely on unconstrained agent reasoning without deterministic checks.
- Do not make prediction-market execution the V1 lane.

MVP relevance:

- Medium. The architecture is useful, but V1 should stay with US stocks/ETFs and approved paper trades.

## System Architecture

Python is the source of truth. The UI displays results; it does not compute them.

```text
free data sources
-> ingestion jobs
-> DuckDB or SQLite
-> deterministic indicators
-> strategy modules
-> risk checks
-> evidence packet
-> agent debate
-> validated evidence card
-> staged paper trade
-> human approval
-> journal and lessons
```

### Suggested Repo Shape

```text
tradingview/
  RESEARCH.md
  README.md
  SOUL.md
  strategy_notes.md
  data/
    raw/
    processed/
  notebooks/
  src/
    data/
    indicators/
    strategies/
    backtesting/
    agents/
    risk/
    journal/
    reports/
    dashboard/
  tests/
```

### Data Sources

V1 should prioritize:

- SEC EDGAR APIs for official filings and XBRL company facts.
- Free end-of-day price data source for daily OHLCV.
- TradingView widgets for visual charts only.
- Manually maintained watchlist and portfolio.
- Optional RSS/news later.
- Optional Alpaca paper trading only after local paper journal works.

Every stored dataset should include:

```yaml
source: sec_edgar
source_url: "https://data.sec.gov/..."
retrieved_at: 2026-05-11T16:00:00-05:00
data_as_of: 2026-05-10
freshness: filing_based
quality_status: usable
```

## 4-Week MVP Plan

### Week 1: Research And Data Foundation

Deliverables:

- Refined `RESEARCH.md`.
- `README.md` with thesis and non-goals.
- Local Python environment.
- DuckDB or SQLite selected. Default: DuckDB.
- Seed universe file.
- One script that fetches and stores daily prices for 3-5 symbols.
- One SEC EDGAR experiment for AAPL or MSFT.

Done when:

- The app can produce a plain text data freshness report.

### Week 2: Strategy And Backtest Engine

Deliverables:

- Moving averages.
- RSI.
- Bollinger Bands.
- Relative strength versus VOO or SPY.
- ETF baseline comparison.
- Trend-following backtest.
- Mean-reversion backtest.
- Transaction cost assumption.

Done when:

- At least three symbols have backtest reports showing return, buy-and-hold return, drawdown, trades, win rate, and Sharpe estimate.

### Week 3: Evidence Cards And Agent Debate

Deliverables:

- Evidence packet schema.
- Evidence card schema.
- Data auditor.
- Technical analyst.
- Fundamentals analyst.
- Bull case.
- Bear case.
- Risk manager.
- Trader agent that can stage but not execute paper trades.

Done when:

- `analyze_symbol("AAPL")` produces a validated evidence card and either a staged paper trade or a clear no-trade reason.

### Week 4: Personal Dashboard And Journal

Deliverables:

- Streamlit dashboard.
- Watchlist page.
- Symbol detail page.
- Evidence card feed.
- Staged paper trade queue.
- Approval/rejection workflow.
- Paper trade journal.
- Weekly review report.

Done when:

- I can run a weekly review, approve or reject staged paper trades, and review previous outcomes.

## Risk Guardrails

### Product Risks

- AI hallucinated facts.
- Overconfidence from polished writing.
- Overfitted backtests.
- Lookahead bias.
- Survivorship bias.
- Stale data.
- Confusing paper profits with live trading skill.
- Overtrading.
- Copying famous investors without understanding filing delays.
- Treating social/news sentiment as truth.

### Hard Rules

- Missing critical data returns `INSUFFICIENT_DATA`.
- Confidence cannot exceed the data quality cap.
- Every trade thesis needs opposing evidence.
- Every staged paper trade needs an invalidation rule.
- Every strategy report compares against ETF baseline.
- Every backtest shows trade count and drawdown.
- No direct real-money execution in V1.
- No leverage, margin, options, futures, forex, or crypto in V1.
- No hidden prompt-only strategy logic.

### Beginner Personal Finance Guardrails

Before real money is ever considered:

- Emergency savings should exist.
- High-interest debt should be handled.
- The journal should show at least several months of paper-trade discipline.
- The system should be tested across different market regimes.
- A written maximum loss limit should exist.
- Broad ETF accumulation remains the default benchmark.

## What The First Useful Demo Should Do

Do not start with a polished AI chatbot.

Start with:

```text
analyze_symbol("AAPL")
```

Expected output:

- Data freshness report.
- Technical score.
- Fundamental score.
- Valuation sanity score.
- Risk flags.
- Bull case.
- Bear case.
- Final evidence card.
- Paper trade proposal or no-trade decision.
- Journal entry.

The first UI can be Streamlit. The first database can be DuckDB. The first "AI" can be a structured evidence card generated from deterministic packets, with LLM synthesis added after the packet is reliable.

## Source Index

| Source | URL | What It Supports |
|---|---|---|
| Barebone App Store | https://apps.apple.com/us/app/barebone-ai-finance-research/id6737490098 | Barebone feature set, positioning, disclaimer, earnings summaries, Polymarket odds, smart investor activity. |
| Barebone Google Play | https://play.google.com/store/apps/details?id=com.briiantam.bareboneai | Cross-check that Barebone is positioned as AI finance research. |
| Barebone LinkedIn | https://www.linkedin.com/company/barebone-ai | Company identity and public positioning. |
| TradingView Paper Trading | https://www.tradingview.com/support/solutions/43000516466-paper-trading-main-functionality/ | Manual simulated trading without real money. |
| Alpaca Paper Trading | https://docs.alpaca.markets/docs/paper-trading | API-based paper trading and simulation limitations. |
| SEC EDGAR APIs | https://www.sec.gov/search-filings/edgar-application-programming-interfaces | Official company submissions and XBRL API access. |
| Investor.gov Form 13F | https://www.investor.gov/introduction-investing/investing-basics/glossary/form-13f-reports-filed-institutional-investment | Institutional holdings reports and smart-money tracking context. |
| Investor.gov Forms 3, 4, 5 | https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-69 | Insider ownership and transaction filing context. |
| Investor.gov ETFs | https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-2 | ETF baseline, diversification, costs, and risks. |
| FINRA Day Trading | https://www.finra.org/investors/investing/investment-products/stocks/day-trading | Why day trading is deferred for V1. |
| Investor.gov Margin Accounts | https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins-29 | Margin risk rationale. |
| CFTC Digital Asset Fraud Alert | https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/watch_out_for_digital_fraud.html | Crypto fraud and digital asset risk rationale. |
| CFTC Futures Basics | https://www.cftc.gov/LearnAndProtect/EducationCenter/FuturesMarketBasics/index2.htm | Futures risk and complexity context. |
| Berkshire Owner's Manual | https://www.berkshirehathaway.com/ownman.pdf | Buffett/Berkshire principles: owner mindset, intrinsic value, debt discipline, candor, S&P comparison. |
| Bridgewater All Weather Story | https://www.bridgewater.com/research-and-insights/the-all-weather-story | Regime thinking and diversification inspiration. |
| Backtest Overfitting Paper | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253 | Anti-overfitting guardrails. |


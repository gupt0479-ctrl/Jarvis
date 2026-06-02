---
type: concept
status: sprout
created: 2026-04-26
updated: 2026-04-26
related_progress:
  - "[[Trading with Ai]]"
  - "[[AI Market Analyzer - Strategy Engine]]"
  - "[[AI Market Analyzer - Data Sources]]"
  - "[[AI Market Analyzer - 4 Month Build Plan]]"
tags:
  - trading
  - ai
  - architecture
  - strategy-engine
track:
  - trading
  - ai
next: "Build the deterministic evidence engine before adding LLM synthesis"
---

# AI Market Analyzer - AI Engine Architecture

## Core Conclusion

The AI should not be a freeform chatbot that guesses whether to buy or sell.

The strongest architecture is:

```text
verified data
-> deterministic indicators and strategy modules
-> backtest and risk checks
-> evidence packet
-> structured AI analyst
-> AI risk critic
-> validated evidence card
-> human decision
```

The AI is an analyst and explanation layer. The strategy engine is the source of truth.

## Why This Pattern

Financial prediction is noisy, non-stationary, and easy to overfit. A model can look amazing in historical tests and fail when market regimes change. Backtesting research repeatedly warns that selecting strategies from many historical experiments can produce overfit results that do not survive out-of-sample.

This means the app should optimize for:

- repeatable process
- evidence quality
- uncertainty handling
- risk controls
- source timestamps
- honest backtesting
- human review

not for magical prediction.

## The AI System Roles

### 1. Data Auditor

Checks whether the app has enough valid data to analyze a symbol.

Responsibilities:

- Verify latest price date.
- Verify fundamentals date.
- Verify whether news exists.
- Detect missing fields.
- Detect source conflicts.
- Cap confidence when data quality is weak.

Output:

```yaml
data_quality_status: usable | partial | stale | conflicting | missing
max_confidence: 0.70
blocked_reasons:
  - "Fundamentals older than accepted window."
```

This can be deterministic Python first. AI can explain the result later.

### 2. Pattern Detector

Computes technical indicators and chart patterns.

Use indicators as features, not as decisions.

Useful v1 indicators:

- Simple moving averages: 20, 50, 200.
- Exponential moving averages.
- RSI.
- MACD.
- Bollinger bands.
- ATR.
- Volume change.
- Relative strength vs SPY or VOO.
- 52-week high/low position.

Candlestick patterns can be added later through TA-Lib, but they should never drive a decision alone. They are weak signals unless confirmed by trend, volume, and risk context.

### 3. Strategy Modules

Each strategy is a deterministic module that returns a score packet.

V1 modules:

- ETF baseline.
- Trend following.
- Mean reversion.
- Quality compounder.
- Valuation sanity.
- Risk control.

Each module returns:

```yaml
strategy: trend_following
score: 72
action_hint: WATCH
confidence_hint: 0.64
positive_signals: []
negative_signals: []
neutral_signals: []
risk_flags: []
required_data: []
missing_data: []
```

### 4. Regime Context

The same strategy behaves differently depending on the broader market.

V1 regime checks:

- SPY above or below 200-day moving average.
- QQQ relative strength.
- VIX level if available.
- Sector strength if available.
- Broad market drawdown.

Example:

```yaml
market_regime:
  label: risk_on | neutral | risk_off
  evidence:
    - "SPY above 200-day moving average."
    - "QQQ outperforming SPY over 3 months."
```

The AI should use regime context to lower confidence during unstable markets.

### 5. Evidence Builder

Combines data quality, indicators, strategies, risk, and portfolio context into one packet.

This packet is the only thing the LLM should see.

Example:

```yaml
symbol: MSFT
portfolio_context:
  owned: true
  position_weight: 0.12
  average_cost: 310.25
data_quality:
  status: usable
  max_confidence: 0.75
strategies:
  - strategy: quality_compounder
    score: 82
    action_hint: HOLD
  - strategy: trend_following
    score: 68
    action_hint: WATCH
risks:
  - "Position concentration above target."
  - "Earnings within 14 days."
source_timestamps:
  prices: 2026-04-26
  fundamentals: 2026-04-20
  news: 2026-04-26
```

### 6. AI Analyst

The analyst turns the evidence packet into a structured evidence card.

Rules:

- Use only supplied evidence.
- Do not invent prices, financials, ratings, or news.
- Return structured JSON.
- Explain both supporting and opposing evidence.
- Include invalidation conditions.
- Include next review date.
- Respect the data quality confidence cap.

The analyst should use OpenAI Structured Outputs so the app receives schema-valid JSON instead of loose prose.

### 7. AI Risk Critic

The critic reviews the analyst output before the user sees it.

Checks:

- Did the analyst cite evidence that exists in the packet?
- Is confidence above the allowed cap?
- Did it ignore a major risk flag?
- Did it use forbidden language like guaranteed, certain, risk-free?
- Did it produce a direct trade command instead of a review suggestion?
- Did it produce a recommendation despite missing data?

If the critic fails the card, the app should either:

- lower confidence,
- return `NEEDS_REVIEW`,
- or regenerate once with the critic feedback.

### 8. Alert Decider

Converts evidence cards into notifications.

Alert types:

- `info`: useful but not urgent.
- `review`: meaningful signal changed.
- `urgent_review`: risk or thesis changed materially.

Alerts should say:

```text
Review MSFT because trend score dropped below threshold and earnings are within 14 days.
```

not:

```text
Sell MSFT now.
```

## The Most Successful Build Pattern

The winning pattern is a **hybrid rule-based + AI analyst system**:

1. Deterministic Python calculates facts.
2. Strategy modules produce scores.
3. Backtests evaluate strategy behavior.
4. AI summarizes and reasons over the evidence.
5. A critic validates the output.
6. The user makes the decision.

This is stronger than:

- pure chatbot
- pure technical indicator dashboard
- raw ML price prediction
- auto-trading bot
- overfit backtest optimizer

## AI Recommendation Workflow

```text
1. User asks for analysis or scheduled job runs.
2. System fetches latest stored data for symbol.
3. Data auditor checks freshness and completeness.
4. Feature engine computes indicators.
5. Strategy modules score the symbol.
6. Backtest engine attaches relevant historical behavior.
7. Evidence builder creates the evidence packet.
8. AI analyst creates evidence card as strict JSON.
9. AI critic validates card against packet and policy.
10. App stores final card and shows it to user.
```

## What The AI Should Do

The AI should:

- summarize stock/company context
- explain why a strategy fired
- explain uncertainty
- compare signals against each other
- detect contradictions
- explain market regime
- produce beginner-friendly reasoning
- generate invalidation conditions
- generate review questions
- produce a digest of watchlist changes

The AI should not:

- fetch random web facts itself in v1
- make ungrounded predictions
- claim to know future prices
- execute trades
- optimize strategies by itself
- modify backtest assumptions silently

## ML Model Roadmap

### V1: No Predictive ML Required

Start with deterministic strategy modules. This is enough to learn and build something useful.

### V2: Simple Supervised Models

Possible targets:

- Probability stock beats SPY over next 20 trading days.
- Probability of 10% drawdown over next 60 trading days.
- Risk regime label.
- Alert prioritization.

Use models like:

- logistic regression
- random forest
- gradient boosting

Do not start with deep learning.

### V3: Advanced Research

Only after v1/v2 work:

- walk-forward validation
- purged/combinatorial cross-validation
- model calibration
- feature importance
- ensemble of strategy signals
- regime-aware models

## Evaluation Plan

Evaluate the AI separately from the trading strategies.

### Strategy Evaluation

Metrics:

- return vs buy-and-hold
- max drawdown
- Sharpe estimate
- number of trades
- win rate
- transaction cost sensitivity
- performance by market regime

### AI Output Evaluation

Tests:

- JSON schema validity.
- No invented facts.
- Confidence never exceeds data quality cap.
- Refuses when required fields are missing.
- Mentions major risk flags.
- Includes opposing evidence.
- Uses allowed action labels only.

Create test cases:

```yaml
case: stale_price_data
expected_action: INSUFFICIENT_DATA
expected_max_confidence: 0.30
```

```yaml
case: strong_trend_but_bad_fundamentals
expected_behavior: mention contradiction and lower confidence
```

```yaml
case: earnings_tomorrow
expected_behavior: flag event risk and avoid high-confidence action
```

## Implementation Stack

Python engine:

- `pandas`
- `numpy`
- `duckdb`
- `scikit-learn`
- `ta-lib` or `pandas-ta-classic`
- `vectorbt` later for faster backtests
- `pydantic` for evidence schemas

AI:

- OpenAI Responses API
- Structured Outputs with JSON schema
- optional function/tool calling later
- eval graders for testing AI output quality

Storage:

- DuckDB first
- Postgres later if web app needs multi-user backend

Dashboard:

- Streamlit first
- Next.js later

## First AI Milestone

Do not start with a chatbot.

Build this first:

```text
analyze_symbol("AAPL")
-> loads price/fundamental data
-> computes indicators
-> scores strategies
-> builds evidence packet
-> produces JSON evidence card
-> validates card
-> saves card
```

The first demo should be a terminal or notebook output, not UI.

## Source Anchors

- OpenAI Structured Outputs: https://platform.openai.com/docs/guides/structured-outputs
- OpenAI function calling: https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api
- OpenAI graders/evals: https://platform.openai.com/docs/guides/graders/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- SEC AI investment fraud alert: https://www.investor.gov/index.php/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/artificial-intelligence-fraud
- SEC AI washing enforcement example: https://www.sec.gov/newsroom/press-releases/2024-36
- TA-Lib: https://ta-lib.org/index.html
- vectorbt: https://vectorbt.dev/
- Backtest overfitting paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253


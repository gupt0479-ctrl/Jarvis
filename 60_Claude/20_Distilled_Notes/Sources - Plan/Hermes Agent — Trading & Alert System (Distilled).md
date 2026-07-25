---
type: input
status: sprout
created: 2026-07-09
tags:
  - trading
  - agents
  - alert-systems
  - operationalization
notes:
  - "[[AI Prediction Market Trading Bot (PDF)]]"
  - "[[trading-bot five-stage architecture]]"
  - "[[MIT Quant Bible (PDF)]]"
  - "[[TradingView Project Scope]]"
source_url: https://zachdoesai.com/guides/hermes-money-playbook (Play 4: Markets)
source_note: "[[4 Ways to Make Money With the Hermes Agent (web).md]]"
track: trading
input_kind: web
---

# Hermes Agent — Trading & Alert System (Distilled)

**Source:** Zach's "4 Ways to Make Money With the Hermes Agent" (Play 4: Markets section)  
**Extracted:** 2026-07-09  
**Relevance:** **HIGH — directly applicable to TradingView bot architecture**  

---

## Core Insight: Agent as Research Operator, Not Autonomous Trader

### The Reframe (Critical)

> "The most dangerous one if you position it wrong. So position it right. Do not let an AI agent trade real money on autopilot."

**What fails:**
- ❌ Agent autonomously places trades (you hand your bankroll to a bot with no judgment)
- ❌ "Watch the markets and trade for me when something looks good" prompt (too vague, too risky)

**What works:**
- ✅ Agent monitors for anomalies, researches cause, sends **research brief** to human
- ✅ Human reviews brief and decides whether to act
- ✅ Agent **removes repetition** (finding signal in noise), not decision-making

**Money model:** Paid alert system, research feed, or consulting workflow for existing traders (not "let me trade your money")

---

## The Trading Agent Prompt (Good Version)

```
Monitor these market categories for unusual movement: [your categories]. 
Do not place trades. 

When a market moves more than [8%] in 24 hours or volume spikes unusually, 
send me a brief with:
  1. Market link
  2. Current price
  3. Possible reason for the move
  4. Related news
  5. What I should verify before taking any action
```

**Key constraints:**
- No autonomous trading
- Specific threshold (8% or unusual volume)
- Research brief, not a recommendation
- Human verification step required

---

## Mapping to Your Five-Stage Trading Bot Architecture

This Hermes pattern maps cleanly to [[AI Prediction Market Trading Bot (PDF)]] five-stage pipeline:

| Stage | TradingView Design | Hermes Parallel | Implementation |
|---|---|---|---|
| **Scan** | Find tradeable opportunities (volume, price moves, volatility spikes) | "Monitor market categories for unusual movement" | Automated polling (15–30 min intervals); flag >8% moves or anomalies |
| **Research** | Gather intelligence (news, sentiment, earnings, sector momentum) | "Possible reason for the move, related news" | Scrape Reuters/Bloomberg RSS, Twitter sentiment, financial calendars; aggregate sources |
| **Predict** | Estimate probability/direction (confidence + edge) | "What I should verify before taking action" | Model scores; human decides if edge >threshold; tracks Brier score |
| **Risk** | Validate position sizing, Kelly fraction, VaR checks | [Human approval gate] | All risk checks Python-deterministic; agent enforces constraints |
| **Compound** | Learn from outcomes; update knowledge base | Alert log becomes training data | Track which alerts led to profitable trades; refine alert thresholds monthly |

---

## Why This Matters for TradingView

### 1. **Operational Risk Reduction**
- Instead of: "Build a bot that makes trades automatically" → Ship a complex, fragile system
- Swap to: "Build a bot that alerts on opportunities" → Ship a research tool, humans decide
- **Reality:** Alert system is 80% of the alpha with 20% of the risk

### 2. **Portfolio Value Signal**
Winning hackathon projects (from Hall of Hacks) that use AI are NOT autonomous traders; they're:
- Trading research tools (TradingView, Polymarket alert systems)
- Portfolio analysis agents (backtesting, Sharpe scoring)
- Research pipelines (news → sentiment → trade idea)

**Pattern:** Agents do repetitive research better than humans; humans do risk management better than agents.

### 3. **Immediate MVP Scope** (24–48 hour build)
If TradingView project enters a hackathon, this is your scoped MVP:

```
Stage 1: Scan (automated, runs every 30 min)
  - Monitor S&P 500 stocks for >5% 24h moves
  - Flag unusual volume (2x average)
  
Stage 2: Research (automated, triggered by scan)
  - Fetch latest news on flagged ticker
  - Sentiment analysis (bullish/bearish/neutral)
  - Options implied volatility (market's view)
  
Stage 3: Predict (human, triggered by research)
  - User sees alert brief (price, reason, news, IV)
  - User decides: "Worth a look?" or "Pass"
  
Stages 4–5 are manual (out of scope for MVP hackathon)
```

**Time to build:** 18–20 hours with Claude + v0  
**Demo:** User gets 3 market alerts with research briefs; shows one being acted on profitably

---

## The Hermes Anti-Pattern You Must Avoid

**Temptation (what will get you wrecked):**
```
"Let me build a bot that:
  - Monitors markets 24/7
  - Places trades autonomously
  - Compounds profits without human approval
  - Learns and scales position size over time"
```

**Why this fails:**
1. Complexity explodes (state management, connection reliability, drift)
2. One bug = full account loss (no circuit breaker)
3. Judges will ask "What's your risk management?" and you'll have none
4. You'll lose money before launch

**What wins:**
```
"I built a research system that:
  - Identifies market anomalies (systematic, not lucky)
  - Summarizes research (saves trader 2h/day)
  - Lets traders decide (they own the risk)
  - Improves over time (tracks which alerts converted to profits)"
```

**Why this wins:**
1. Scope is defensible (you control complexity)
2. Risk is transparent (human always in the loop)
3. Judges ask "How do you find anomalies?" — you have a real answer
4. You can demo it risk-free with backtested alerts

---

## Concrete Implementation Path (For TradingView Build)

### Phase 1: Scan Stage (Hours 0–6)
**Goal:** Detect anomalies reliably

```python
# Pseudocode
while True:
  for ticker in WATCHLIST:
    price_24h_ago = get_price(ticker, days_ago=1)
    price_now = get_price(ticker, now=True)
    pct_move = (price_now - price_24h_ago) / price_24h_ago
    
    volume_avg_20d = get_volume_average(ticker, days=20)
    volume_now = get_volume(ticker, now=True)
    volume_spike = volume_now / volume_avg_20d
    
    if pct_move > 0.05 or volume_spike > 2:
      alert_threshold_crossed(ticker, pct_move, volume_spike)
  
  sleep(1800)  # Check every 30 min
```

**Data source:** Alpha Vantage (free tier limited) or paid API (Polygon.io, IEX Cloud)

### Phase 2: Research Stage (Hours 6–12)
**Goal:** Brief human with context

```python
def research_brief(ticker, price_move, volume_spike):
  # Fetch in parallel
  news = scrape_ticker_news(ticker)  # Reuters, Bloomberg RSS
  sentiment = analyze_sentiment(news)  # Bullish/bearish/neutral
  
  iv_now = get_options_iv(ticker)  # Implied volatility
  iv_avg_30d = get_options_iv_historical(ticker, days=30)
  iv_signal = "market expected move" if iv_now > iv_avg_30d else "move surprised market"
  
  return {
    'ticker': ticker,
    'current_price': get_price(ticker),
    'move_24h': price_move,
    'volume_spike': volume_spike,
    'top_news': news[:3],  # 3 most recent
    'sentiment': sentiment,
    'iv_signal': iv_signal,
    'verify_before_trading': [
      'Is the news genuine (not bot-generated)?',
      'Does the IV back up the move?',
      'What sector effect (is it broad or stock-specific)?',
      'When was the earnings/event that triggered this?'
    ]
  }
```

**Deploy:** Render as Markdown alert → email/Slack to user

### Phase 3: Predict Stage (Hours 12–18)
**Goal:** Human reviews; tracks decision quality

```python
# User reviews alert
alert_log = {
  'timestamp': '2026-07-09 14:32',
  'ticker': 'TSLA',
  'user_action': 'TRADED' | 'SKIPPED',
  'reasoning': 'News about Giga Berlin restart seemed credible',
  'entry_price': 245.30,
  'exit_price': 248.50,
  'pnl': '+1.28%',
  'alert_outcome': 'PROFITABLE'
}

# Track Brier score: are alerts calibrated?
brier = measure_calibration(alert_log)
# If 50% of alerts led to profitable trades, you have real signal
```

### Phase 4 & 5: Risk + Compound (Post-MVP)
- Risk: Implement Kelly fraction; auto-reject alerts when portfolio drawdown >5%
- Compound: Monthly audit of which alert types converted best; refine thresholds

---

## MVP Hackathon Checklist (From This Framework)

### Pre-Hackathon (2 weeks before)
- [ ] Choose 50–100 stock watchlist (tech + finance + energy for diversity)
- [ ] Integrate data API (Alpha Vantage free or paid provider)
- [ ] Test 3 anomaly detectors: price move %, volume spike, options IV
- [ ] Prepare 5 sample alerts to demo

### During Hackathon (Hours 0–12)
- [ ] Build scan + research stages (don't touch trading)
- [ ] Connect to email/Slack alert dispatch
- [ ] Create demo alerts for 3 stocks (backtested, not live)
- [ ] Design alert dashboard (ticker, move, news, IV, verify-steps)

### Demo (Hour 20–24)
- [ ] Show 3 backtested alerts that would have been profitable
- [ ] Walk through one alert: "Here's what the system saw, here's what a trader should verify"
- [ ] Explain risk philosophy: "Alert is research; trading decision is always human"

### Post-Hackathon (Portfolio Integration)
- **Resume bullet:** "Built anomaly-detection trading alert system; 65% of backtested alerts led to profitable trades"
- **GitHub:** Source code + alert_log.csv (proof of track record)
- **Case study:** Problem (traders spend 2h/day scanning news) → Solution (system does it) → Result (65% alert accuracy)

---

## Key Learnings from Hermes Framework

| Learning | Application |
|---|---|
| **Agent as junior operator** | Your bot handles routine monitoring; you handle trading decisions |
| **Attach to real workflow** | Traders actually spend 2h/day on research — you're automating that, not replacing human judgment |
| **Sell the outcome, not the method** | "2 hours saved per day on research" sells better than "I used Claude + Python" |
| **No autonomous risk** | Every alert requires human verification before trade; no auto-execution |
| **One good result, then scale** | Build one alert type (price anomalies) perfectly; add volume/sector/news later |

---

## Integration with TradingView Architecture

This distilled note plugs into:
- **Scan stage:** Hermes shows you how to frame monitoring (anomaly thresholds, not vague "looks interesting")
- **Research stage:** Hermes prompt is exactly the research brief structure (link, price, reason, news, verify)
- **Risk stage:** Hermes anti-pattern (no auto-trading) is your guardrail
- **Compound stage:** Hermes money model (research feed for traders) is how you monetize long-term

---

## Open Questions for Implementation

- [ ] **Data source:** Alpha Vantage free tier (~5 calls/min) vs. paid provider ($20–100/mo)? Trade-off: cost vs. reliability
- [ ] **Watchlist:** S&P 500 (500 stocks = heavy computation) vs. curated 50 (faster, more focused)?
- [ ] **Thresholds:** Start with 8% move (Hermes example) or 5% (lower barrier for MVPs)?
- [ ] **Alert dispatch:** Email, Slack, or web dashboard? (Email is simplest for MVP; can add others post-hackathon)
- [ ] **Backtesting:** Use past 2 years of data to validate alert accuracy before deploying live?

---

## Related Vault Notes

- [[AI Prediction Market Trading Bot (PDF)]] — Five-stage architecture this maps to
- [[trading-bot five-stage architecture]] — Your detailed design doc
- [[MIT Quant Bible (PDF)]] — Market-making context (if you add options IV as signal)
- [[Hall of Hacks — Winning Hackathon Patterns Analysis]] — Real hackathon winners (none are autonomous traders)
- [[TradingView Project Scope]] — Main project doc (link once created)

---

## Flashcards

#cards/trading  
**What's the Hermes trading anti-pattern you must avoid?**::Letting an agent trade autonomously ("trade for me when something looks good"). Instead: agent monitors for signal, sends research brief to human, human decides.

**How does Hermes trading map to the five-stage bot architecture?**::Scan (anomaly detection) + Research (news/IV/sentiment brief) → Human decision gate → Risk/Compound (manual). No agent decision-making on executions.

**What's the money model for trading alerts (Hermes frame)?**::Not "I predict the market"; but "I save traders 2h/day on research" = paid research feed or alert subscription for existing traders.

**What makes a hackathon trading project win (per Hermes + Hall of Hacks)?**::Research tool that demonstrates signal reliably (65%+ alert accuracy on backtested data) + explains why + proves human can use it safely = judges like it. Autonomous trading bot = judges don't.

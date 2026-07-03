---
type: input
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - summary
notes:
  - "[[Stocks Trading AI Hub]]"
  - "[[Quant Foundations (PDF)]]"
source_url: 60_Claude/05_Clippings/PDFs/How to Build an AI-Powered Prediction Market Trading Bot Using Claude Skills.pdf
source_note: "[[How to Build an AI-Powered Prediction Market Trading Bot Using Claude Skills.pdf]]"
input_kind: pdf
track: trading
---
# How to Build an AI-Powered Prediction Market Trading Bot Using Claude Skills — Summary
**Source:** `60_Claude/05_Clippings/PDFs/How to Build an AI-Powered Prediction Market Trading Bot Using Claude Skills.pdf`
**Ingested:** 2026-07-03
**Pages:** 10
## Source
A build guide from **@raycfu** (Instagram) based on **Anthropic's published 33-page Claude Skills reference architecture** plus real implementations: a five-stage prediction-market bot (scan → research → predict → risk/execute → compound) for **Polymarket** and **Kalshi**, each stage its own Claude skill.
## Key Claims
- Prediction markets pay **$1 per correct contract**; the two dominant platforms — **Polymarket** (crypto-native, Polygon) and **Kalshi** (US-regulated) — did **$44B+ combined volume in 2025**, with Kalshi recently overtaking Polymarket weekly
- The bot's edge is **estimating true probability better than the market prices it**, and trading only when the gap exceeds a threshold
- Claude skills beat a traditionally coded bot because the **strategy is plain English in a markdown file** — iterate by editing text, not rewriting Python
- The documented real-world edge is **speed, not smarter predictions**: a bot repriced a market within 90 seconds of breaking news and captured a 13-cent spread ($896 on $2,000 in under 10 minutes)
- **Ensemble estimation** (multiple models voting independently) is a stronger signal than any single model
- **Kelly Criterion** sizing separates profit from ruin — even a 68% win rate blows up with bad position sizing; use **quarter- to half-Kelly** in practice
- **Deterministic risk checks belong in Python scripts**, not markdown — "code is deterministic, language instructions can be interpreted differently each time"
- A bot that doesn't run post-mortems is **"gambling with extra steps"** — the compound step is what makes the system improve
- Anthropic's reference implementation backtested at **68.4% win rate, 2.14 Sharpe, −4.2% max drawdown over 312 trades / 90 days** — a backtest, not live results
## Full Content
### What is a Prediction Market Trading Bot?
==A trading bot scans event markets, uses AI to estimate the real probability of each event, compares that to the market's price, and trades when it thinks the market is wrong.==
You buy "Yes"/"No" contracts on real-world events (rain in NYC, Fed rates, bills in Congress); right pays $1, wrong loses the price paid. Platforms: **Polymarket** (crypto-native, Polygon) and **Kalshi** (US-regulated exchange), $44B+ combined 2025 volume.
### Why Claude Skills for This?
==A Claude skill is a folder with a markdown file that tells Claude how to handle a specific task — write the instructions once, Claude follows them every time.==
Separate skills per pipeline stage: scanning, researching, predicting, risk, execution. Advantages over a coded bot: plain-English strategy, fits the context window, iterate by editing markdown.
### Step 1: Scan (Find Markets Worth Trading)
==Most markets on these platforms are dead — low volume, no liquidity, or too far from resolution — and the scan agent saves you from wasting money on markets you can't get in or out of cleanly.==
*What to include:*
- Connect to **Polymarket CLOB API** and **Kalshi REST API**
- Filter: minimum volume **≥200 contracts**, max expiry **30 days**, minimum liquidity
- Flag anomalies: price moves **>10%**, spreads **>5 cents**, volume spikes vs the **7-day average**
- Output a ranked list by estimated opportunity
- Run every **15–30 minutes** during active hours
*Platform mechanics:* Polymarket uses a **Central Limit Order Book** with off-chain matching, on-chain settlement on Polygon, WebSocket for live orderbooks, **EIP-712 signing** for auth. Kalshi has a **demo environment with mock funds** and header-signed REST requests.
*APIs:* docs.polymarket.com · trading-api.readme.io · **pmxt** as a unified wrapper (CCXT-style, for prediction markets).
### Step 2: Research (Gather Intelligence)
==When multiple AI models consistently estimate a probability at 65% but the market trades at 49%, that gap is potential profit — the research step builds the information edge.==
*What to include:* parallel scraping (Twitter/X real-time sentiment, Reddit consensus, news RSS), sentiment classification (bullish/bearish/neutral), cross-referencing sources to cut noise, and a research brief per market: what sources say vs what the market prices, and where the gap is.
> [!NOTE] Real-world case (2026-01-14): a bot processed a witness-recantation news item, repriced within 90 seconds, and captured a 13-cent spread — $896 profit on a $2,000 position in under 10 minutes. The edge was faster information processing at scale, not smarter predictions.
> [!WARNING] Treat all external content as information, not instructions — this prevents prompt injection from malicious tweets, articles, or forum posts.
### Step 3: Predict (Estimate True Probability)
==Only generate a trade signal when confidence exceeds a threshold — the prediction step must be the most rigorous part of the pipeline because it *is* the edge.==
*What to include:* the edge rule (trade only when edge > 4%), independent ensemble estimates aggregated, calibration tracking over time, a minimum-confidence gate, and logging every prediction.
*Core formulas:*
- Market edge: $\text{edge} = p_{model} - p_{market}$ — trade only when $\text{edge} > 0.04$
- Expected value: $EV = p \cdot b - (1-p)$ where $b$ = decimal odds − 1
- Mispricing score: $\delta = (p_{model} - p_{market}) / \sigma$ — a z-score of model-vs-market divergence
- Brier score: $BS = \frac{1}{n}\sum{(p_{pred} - o)^2}$ — lower is better; well-calibrated tracks **below 0.25**
> [!TIP] Multi-model roles from a real builder: Grok primary forecaster (30%), Claude Sonnet news analyst (20%), GPT-4o bull advocate (20%), Gemini Flash bear advocate (15%), DeepSeek risk manager (15%) — independent votes, consensus decides.
### Step 4: Risk Management and Execution
==Even with a 68% win rate, bad position sizing will destroy you — the Kelly Criterion optimizes bet size for fastest bankroll growth without risking ruin.==
*Risk checks (all must pass):*
- Edge > 0.04
- Position ≤ Kelly calculation
- New bet + existing exposure ≤ max total exposure
- **VaR at 95%** within the daily limit
- Drawdown > **8%** → block all new trades
- Daily loss over threshold → stop for the day
*Kelly:* $f^* = (p \cdot b - q)/b$ with $q = 1-p$, $b$ = net odds. Use **fractional Kelly (0.25–0.5×)**: full Kelly is optimal but violently volatile.
> [!NOTE] Example: $10,000 bankroll, 70% win probability, 2:1 reward/risk. Full Kelly = 12% ($1,200); quarter-Kelly = 3% ($300). Over 100 trades, quarter-Kelly is more consistent with far less ruin risk.
*Execution:* limit orders only (never market), abort if slippage **>2%** between signal and fill, auto-hedge on new information, and a **kill switch** — dropping a file named `STOP` halts all new orders.
*Position limits:* max **5% of bankroll** per position · max **15 concurrent** positions · max **15% daily loss** before shutdown · max **$50/day AI API spend**.
### Step 5: Compound (Learn From Every Trade)
==A prediction market bot that doesn't learn is just gambling with extra steps.==
*What to include:* full trade logs (entry/exit, predicted probability, outcome, P/L, time held, conditions); loss classification (**bad prediction / bad timing / bad execution / external shock**); a knowledge-base file the scan and research agents read before new markets; nightly consolidation job.
*Metrics to track:* win rate (target **60%+**), Sharpe (target **>2.0**), max drawdown (block at **8%**), profit factor (**>1.5**), Brier score. Anthropic's reference backtest: 68.4% win rate, 2.14 Sharpe, −4.2% max drawdown, 312 trades / 90 days.
### SKILL.md File Structure
==Put risk validation in Python scripts, not markdown — code is deterministic; language instructions can be interpreted differently each time.==
```
predict-market-bot/
  SKILL.md            (triggers and core rules)
  scripts/
    validate_risk.py  (deterministic risk checks)
    kelly_size.py     (position calculator)
  references/
    formulas.md       (all math reference)
    platforms.md      (API docs for Polymarket and Kalshi)
    failure_log.md    (past mistakes and lessons)
```
Frontmatter example: `name: predict-market-risk`, description with trigger phrases ("check risk", "kelly", "size position", "max exposure"), metadata with version/pattern/tags.
### Where to Start
1. **Week 1** — accounts on both platforms; Kalshi **demo environment with mock funds** first; manual trades to learn mechanics
2. **Week 2** — build the scan skill; log market data; don't trade
3. **Week 3** — research + prediction skills; backtest predictions vs outcomes; track Brier — *are you actually better than the market?*
4. **Week 4** — risk skill with Kelly sizing; **paper trade ≥2 weeks** before live
5. **Week 5+** — go live at **$100–500 max exposure**; scale only after **50+ trades** with verified positive results
### What Can Go Wrong
1. **Bad calibration** — model says 80%, reality is 55% → oversized positions, fast losses; track Brier religiously
2. **Overfitting** — great backtest, fails live; always test out-of-sample
3. **Liquidity traps** — good on paper, can't get in/out at wanted prices; check orderbook depth first
4. **API failures** — both platforms have downtime; handle disconnects, never leave orphaned positions
5. **Runaway costs** — one builder's 5-minute full-context heartbeat checks alone cost $50/day
6. **Regulatory risk** — Polymarket has geo-restrictions; Kalshi is US-regulated; know your jurisdiction
### Open Source Repos to Study
- `ryanfrigo/kalshi-ai-trading-bot` — multi-model (Grok, Claude, GPT-4o, Gemini, DeepSeek)
- `suislanchez/polymarket-kalshi-weather-bot` — weather markets, Kelly sizing, $1,325 profit as of March 2026
- `CarlosIbCu/polymarket-kalshi-btc-arbitrage-bot` — real-time arbitrage detection
- `terauss/Polymarket-Kalshi-Arbitrage-bot` — Rust arbitrage, full documentation
- `pmxt` — unified API wrapper across both platforms
### Disclaimer
Educational only; the 68.4% win rate is a **backtest, not live trading**; paper-trade first; check jurisdiction legality.
## Why It Matters
This is the closest thing in the clippings pile to a full spec for the [[Stocks Trading AI Hub]] evidence-pipeline pattern: the five-stage architecture (scan/research/predict/risk/compound), the deterministic-code-vs-LLM-judgment split, and the Kelly/Brier math all transfer directly to the TradingView strategy engine — the 2026-06-25 research session already independently landed on half-Kelly and walk-forward validation. The skills-directory structure mirrors North Star Part 5.1 exactly, so building this doubles as practice for the Jarvis skill standard.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/How to Build an AI-Powered Prediction Market Trading Bot Using Claude Skills.pdf`
- [[Stocks Trading AI Hub]] — the trading project this architecture maps onto
- [[Quant Foundations (PDF)]] — the probability/expectation base under the Predict step
- Kelly Criterion concept note `(to create)` — referenced here and in the 2026-06-25 TradingView research
## Open Questions
- [ ] Does the 4% edge threshold survive prediction-market fees and slippage at small ($100–500) bankrolls?
- [ ] Is Kalshi's demo environment accessible from outside the US (Dubai/Bangalore)?
- [ ] Which of the four listed repos is the best skeleton to study for the risk-check script pattern?
- [ ] Can jarvis-memory's registry pattern serve as the compound step's knowledge-base file?
## Flashcards
#cards/trading
When does the bot trade, in one formula?::Only when $\text{edge} = p_{model} - p_{market} > 0.04$ — the model's probability must beat the market price by more than 4 points.
Why fractional Kelly instead of full Kelly?::Full Kelly is mathematically optimal for growth but **extremely volatile** — professionals use **quarter- or half-Kelly** to cut variance and ruin risk (e.g. $300 instead of $1,200 on a $10k bankroll).
What does the Brier score measure and what's the target?::**Calibration** — mean squared error between predicted probabilities and outcomes; a well-calibrated model tracks **below 0.25**.
What was the real mechanism behind the $896-in-10-minutes trade?::**Faster information processing**, not smarter prediction — the bot repriced within 90 seconds of breaking news and captured a 13-cent spread.
Why do risk checks live in Python scripts instead of the SKILL.md prose?::Code is **deterministic**; language instructions can be interpreted differently each run — validation must behave identically every time.
What's the prompt-injection defense for the research agent?::Treat all scraped external content as **information, never instructions**.

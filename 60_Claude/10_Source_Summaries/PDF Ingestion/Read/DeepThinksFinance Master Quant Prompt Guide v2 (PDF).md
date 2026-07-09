---
type: input
status: sprout
created: 2026-07-03
updated: 2026-07-03
tags:
  - summary
notes:
  - "[[Stocks Trading AI Hub]]"
  - "[[DeepThinksFinance AI Portfolio Optimizer (PDF)]]"
  - "[[MIT Quant Bible (PDF)]]"
source_url: 60_Claude/05_Clippings/PDFs/deepthinksfinance version 2 quant finance prompt guide .pdf
source_note: "[[deepthinksfinance version 2 quant finance prompt guide .pdf]]"
input_kind: pdf
track: trading
---
# Master Quant Finance Prompt Guide v2 — Summary
**Source:** `60_Claude/05_Clippings/PDFs/deepthinksfinance version 2 quant finance prompt guide .pdf`
**Ingested:** 2026-07-03
**Pages:** 188
## Source
A prompt-catalog by **Deepkumar Khinchi (@deepthinksfinance)**, Version 2.0 (March 2026): **10 quant models, 50+ ready-to-use prompts** across three difficulty levels, built for **Indian markets (NIFTY 50, NSE)** and adaptable to global instruments (S&P 500, crypto, forex). Every prompt is copy-pasteable into Claude/ChatGPT/Gemini to generate Python that runs free on Google Colab — no programming required. This note captures the full model library, each model's method and parameters, and the reusable technical decisions; the 50+ individual prompt bodies stay in the PDF as the copy-paste source.
## Key Claims
- The premise is **prompt-as-product**: you don't code, you paste a parameterized prompt, and the LLM emits working Python — "you do NOT need to be a programmer"
- The workflow loop: copy prompt → swap `[BRACKETS]` → paste to LLM → run generated Python in Colab → view interactive Plotly charts → share
- The whole library is **yfinance + pandas + numpy + plotly + scipy + scikit-learn** — no paid data, no infrastructure
- **Blended volatility** (0.6·VIX/100 + 0.4·90-day historical) is flagged as "the professional-grade approach used by institutional desks" over pure historical vol
- **Cholesky decomposition** is the industry-standard way to preserve correlation structure in a multi-asset Monte Carlo
- VaR comes in **four flavors that should be compared side by side**: Historical, Parametric ($-z\sigma P$), CVaR/Expected Shortfall, and Monte Carlo
- Factor attribution separates **factor beta from true alpha** — "tells you exactly WHERE your returns come from"
- The models are consistently India-specific: RBI rate 5.25%, India VIX (`^INDIAVIX`), NIFTY (`^NSEI`), SEBI daily-VaR reporting, ₹ capital sizing
## Full Content
### The 10-model library (Section 02)
| Model | Category | Method | Key outputs |
| --- | --- | --- | --- |
| **Monte Carlo Simulation** | Probabilistic | GBM price paths | probability distributions, confidence bands, VaR, 3D path surfaces (20 prompts) |
| **Black-Scholes Options Lab** | Derivatives | BS pricing + all 5 Greeks | option chains, vol smile, 8-strategy builder, 3D payoff surfaces (15 prompts) |
| **Market Timing Optimization** | Systematic | composite Entry Score (0–1) from momentum/volatility/drawdown | entry zones, backtest vs Buy&Hold, CAGR (10 prompts) |
| **ML Direction Probability** | Machine learning | Logistic Regression + Random Forest + Gradient Boosting run together | next-day UP/DOWN probability, 3D surfaces, walk-forward accuracy (12 prompts) |
| **NIFTY50 Macro Prediction** | Macro/AI | 43 macro indicators, GB + RF + Bayesian (Student-t), 18 yrs / 218 points | monthly close prediction (8 prompts) |
| **Mean Reversion Signal** | Statistical | Z-Score + Bollinger + RSI divergence | buy/sell reversion signals (6 prompts) |
| **Pairs Trading Cointegration** | Market-neutral | ADF/Engle-Granger + OLS hedge ratio + spread Z-Score | market-neutral stat-arb (6 prompts) |
| **Risk Factor Attribution** | Risk | Fama-French-style rolling OLS on 4 factors | alpha/beta, R², factor loadings (5 prompts) |
| **VaR & Stress Dashboard** | Risk/compliance | Historical + Parametric + CVaR + Monte Carlo VaR | 99% VaR, stress tests (5 prompts) |
| **Portfolio Optimization** | Portfolio theory | MPT / random-weight Efficient Frontier | max-Sharpe & min-variance allocation (5 prompts) |
### Monte Carlo Engine (Section 03)
==Monte Carlo answers "what is the range of possible outcomes?" not "what is the price" — thousands of GBM paths from historical drift and volatility.==
Prompt tiers: basic (10k paths / 252 days / percentile bands / VaR-95 histogram) → dashboard (probability table P(above/below target), 50/75/90/95% CIs) → **blended volatility** (0.6·India_VIX/100 + 0.4·90-day historical, side-by-side vs pure) → 3D path surface (X=time, Y=sim number, Z=price + density heatmap) → **correlated portfolio MC via Cholesky decomposition** (3 assets, preserves historical correlation, efficient-frontier overlay + portfolio-vs-individual VaR).
### Black-Scholes Options Lab (Section 04)
==A live NIFTY options engine: Black-Scholes pricing, all 5 Greeks (Delta, Gamma, Theta, Vega, Rho), option chains, and 3D payoff/vol surfaces on real NSE weekly F&O.==
Inputs: spot, strike, T=days/365, risk-free = 0.0525 (RBI rate), vol = India VIX/100. Progression: basic pricer with **Put-Call parity check** → live 21-strike chain (ATM±10 at ₹50 intervals) with per-strike Greeks → **3D implied-volatility surface** (strike × expiry × IV, realistic vol smile: higher IV for deep OTM/ITM) → strategy builder (8 strategies) with 3D payoff surfaces.
### Market Timing Optimization (Section 05)
==Answers WHEN to invest via a composite Entry Score built from momentum, volatility, and drawdown signals, backtested against Buy & Hold.==
Downloads ~8 years, computes the three sub-signals into a 0–1 Entry Score, marks optimal entry zones, and reports CAGR vs Buy&Hold.
### ML Direction Probability (Section 06)
==Runs Logistic Regression, Random Forest, and Gradient Boosting simultaneously to predict tomorrow's UP/DOWN with probability scores, plus 3D probability surfaces and walk-forward accuracy.==
The three-model ensemble is the point — comparing their agreement, with a Bloomberg-style UI.
### NIFTY50 Macro Prediction (Section 07)
==Predicts monthly NIFTY close from 43 global macro indicators (Dow, Gold, Oil, INR/USD, VIX, …), trained on 18 years / 218 monthly points spanning the 2008 crash and COVID.==
Models: Gradient Boosting, Random Forest, and a Bayesian **Student-t** model (fat tails); input is a 218-row × 44-column dataset.
### 5 New Models (Section 08 — exclusive)
1. **Mean Reversion Signal Engine** — ==prices statistically tend to return to their average after extreme moves.== Rolling Z-Score = (price − 20-mean)/20-std, Bollinger-band position, RSI(14) divergence from 50. BUY when Z < −1.5 AND RSI < 40 AND near lower band; SELL/EXIT when Z > 0 OR RSI > 60. Reports win rate, avg holding period, Sharpe. "Especially powerful in index instruments during sideways markets."
2. **Pairs Trading Cointegration** — ==market-neutral stat-arb on the divergence of two historically correlated stocks, no directional bet.== Engle-Granger cointegration test → OLS hedge ratio → 60-day rolling spread Z-Score. LONG spread when Z < −2, SHORT when Z > +2, EXIT when |Z| < 0.5. "This is the strategy LTCM used — learn the mechanics."
3. **Risk Factor Attribution (Fama-French style)** — ==decompose returns into systematic factors to separate factor beta from true alpha.== 4 factors: Market (NIFTY returns), Momentum (12m − 1m return), Volatility (inverse 30-day realized vol), Quality (return-consistency score); rolling 90-day OLS of portfolio returns on the factors → rolling loadings, factor contributions, **residual = alpha**, R² over time.
4. **VaR & Stress Testing Dashboard** — ==VaR = maximum expected loss over a horizon at a confidence level; regulators require it.== Four methods at 95%/99%, 1-day: **Historical** (percentile), **Parametric** ($-z\sigma P$, assumes normal), **CVaR/Expected Shortfall** (average loss beyond VaR), **Monte Carlo** (50k GBM). Stress scenarios: 2008 (−60%), COVID Mar-2020 (−38%), custom. "SEBI requires institutional managers to report VaR daily."
5. **Efficient Frontier Portfolio Optimizer** — ==MPT: the allocation maximizing return per unit of risk.== 50,000 random weight sets → expected return / annual vol / Sharpe (rf=5.25%) → efficient-frontier scatter colored by Sharpe, marking **max-Sharpe (star), min-variance (diamond), equal-weight (circle)**, plus the Capital Market Line and an optimal-weights pie.
### Quick Reference (Section 09)
Library map: `yfinance` (data), `pandas` (manipulation), `numpy` (GBM), `plotly` (3D charts), `scipy` (ADF, cointegration), `scikit-learn` (RF, logistic, GB). Consistent conventions across all models: dark Bloomberg theme, gold accent, ₹ sizing, `^NSEI`/`^INDIAVIX` tickers, RBI 5.25% rate.
## Why It Matters
This is a **menu of buildable trading models** that maps directly onto [[Stocks Trading AI Hub]] and overlaps heavily with two already-ingested sources: the [[DeepThinksFinance AI Portfolio Optimizer (PDF)]] (same author, the Efficient-Frontier model built out to a full app) and the [[AI Prediction Market Trading Bot (PDF)]] (Monte Carlo, VaR, Kelly). The honest read: these are **educational/retail prompt templates, not validated strategies** — the [[MIT Quant Bible (PDF)]] and the 2026-06-25 TradingView research both warn that indicators like RSI/Bollinger are descriptive context, not documented-edge factors, and that any model needs walk-forward validation and a Deflated Sharpe before it's evidence. The real value here is (a) the **model inventory** as a build checklist, (b) the reusable engineering decisions (blended vol, Cholesky for correlated MC, the four VaR methods, Fama-French factor construction), and (c) confirmation that the whole stack is free (yfinance + Colab). Treat the prompts as scaffolding to generate a first Python draft, then replace the retail signals with the academically-supported factors from the TradingView research.
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/PDFs/deepthinksfinance version 2 quant finance prompt guide .pdf`
- [[Stocks Trading AI Hub]] — the trading project this model menu feeds
- [[DeepThinksFinance AI Portfolio Optimizer (PDF)]] — the same author's Efficient-Frontier model as a full-stack app
- [[AI Prediction Market Trading Bot (PDF)]] — overlapping Monte Carlo / VaR / risk-management methods
- [[MIT Quant Bible (PDF)]] — the rigorous version of the probability/regression/VaR math underneath these prompts
- Fama-French / VaR / cointegration concept notes `(to create)`
## Open Questions
- [ ] Which of these 10 models is worth actually building as a Bangalore flagship — Pairs Trading (market-neutral, testable) or the Efficient Frontier (already 80% done in the optimizer guide)?
- [ ] Do the retail signals (RSI/Bollinger/Z-Score) survive walk-forward validation on a real universe, per the TradingView research's warning?
- [ ] Are the NIFTY/NSE specifics (`^NSEI`, India VIX, RBI rate) a blocker, or trivially swappable to S&P 500 for a US-facing portfolio piece?
- [ ] Can the "generate Python from a parameterized prompt" pattern itself become a Jarvis skill (a quant-model scaffolder)?
## Flashcards
#cards/trading
What does blended volatility mean in this guide, and why use it?::$0.6 \times \text{VIX}/100 + 0.4 \times \text{90-day historical vol}$ — flagged as the institutional-desk approach because it weights forward-looking implied vol with realized vol instead of using either alone.
What are the four VaR methods this guide compares side by side?::**Historical** (percentile of returns), **Parametric** ($-z\sigma P$, assumes normal), **CVaR / Expected Shortfall** (average loss beyond the VaR threshold), and **Monte Carlo** (GBM-simulated).
Why is Cholesky decomposition used in the portfolio Monte Carlo?::It **preserves the historical correlation structure** between assets when generating correlated random price paths — the industry-standard method for multi-asset MC.
What defines the entry and exit rules in the pairs-trading model?::Trade the spread Z-Score: **LONG when Z < −2, SHORT when Z > +2, EXIT when |Z| < 0.5**, after confirming cointegration (Engle-Granger) and computing the OLS hedge ratio.
In factor attribution, what is "alpha"?::The **residual of the portfolio's returns after the systematic factors (market/momentum/volatility/quality) are regressed out** — true skill-driven return, separated from factor beta.
What's the honest limitation of this guide's models?::They're **retail educational prompt templates, not validated strategies** — the indicators (RSI/Bollinger/Z-Score) are descriptive context, and any model needs walk-forward validation before it's trustworthy as evidence.

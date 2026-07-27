---
type: research
status: sprout
created: 2026-07-26
updated: 2026-07-26
related_progress:
  - "[[Frontend Build Plan — V1 UI Spec]]"
  - "[[Session Findings — Frontend UX Questionnaire (2026-07-26)]]"
  - "[[Math-First Map — Existing Code to Factor Brain]]"
  - "[[Session Findings — AI Brain Hub (2026-07-12)]]"
tags:
  - trading
  - research
  - open-source
  - shortcut
track:
  - trading
  - ui
---
# Research — Reference Repositories for Shortcut Build (2026-07-26)
==No single repo is this desk already built — the exact combination (deterministic factor scores → Analyst/Critic evidence cards → four immutable gates → human-gated promotion → paper trading) is a specific synthesis nobody else has assembled. But five real, actively-maintained repos each cover one slice well enough to borrow code or structure from directly, and two low-star repos are worth reading for the math but not depending on.==
## What to actually clone and mine for code
### 1. microsoft/qlib — factor engine + RankIC, closest match to the brain's math layer
`https://github.com/microsoft/qlib` — 46.6k stars, 7.4k forks, actively maintained (commits within the last week, ongoing RD-Agent integration). MIT-style Microsoft open source license.
Qlib is an AI-oriented quant research platform with a real factor library (Alpha158, Alpha360), RankIC-based factor evaluation, and rolling/walk-forward retraining workflows — the same **RankIC** metric your own Kronos-gating note already names as the bar (`RankIC ≥ 0.03`). This is the strongest single match to `src/research_data`'s factor-scorer layer. Mine it for: factor definition patterns (how Alpha158 expresses momentum/volatility/valuation-style factors as vectorized expressions), the RankIC evaluation code, and the rolling-window backtest harness — your WF gate is doing roughly the same job as Qlib's rolling retraining module. It has no user-facing dashboard (headless research platform; a separate `qlib-server` project exists for web visualization but is thin and lightly maintained — don't expect a UI here).
### 2. freqtrade/freqtrade + freqtrade/frequi — closest match to the dashboard's page taxonomy
`https://github.com/freqtrade/freqtrade` — 52.6k stars, actively maintained, crypto-only but architecturally close: strategy backtesting, hyperopt, dry-run (paper) mode, live/paper split.
`https://github.com/freqtrade/frequi` — 1k stars (small because it's a companion, not standalone), Vue + TypeScript, actively maintained alongside the main bot. This is the single closest UI precedent to what you're building: it has a bot-status dashboard, an open-trades list, a performance/backtest-results view, and a strategy list — map that almost directly onto your Bots-Hub / My Stocks / Tests / Strategies pages. It's Vue, not Streamlit, so don't fork the code directly — clone it locally, run it, and screenshot/trace its page layout and component breakdown (trade table columns, chart placement, status badges) as the concrete UI reference Cursor should mimic in Streamlit. This is more useful as a *design reference* than a *code source* given the framework mismatch.
### 3. TauricResearch/TradingAgents — analyst-report structure, NOT the trader topology
`https://github.com/TauricResearch/TradingAgents` — 94.5k stars, the real repo behind arXiv 2412.20138, very actively maintained (this is the framework your own vault's graphify Nodes already reference by name — `Bull Case Analyst Agent` / `Bear Case Analyst Agent` node stubs under `60_Claude/40_Project_Briefs/TradingView/Nodes/` are almost certainly auto-extracted from prior research into this exact repo).
==Important: this repo's core topology — a Trader agent and a Portfolio Manager agent that use an LLM to approve/execute trades — is the exact pattern your own Session Recap (AI Brain Hub, Block C1) explicitly rejected: "TradingAgents Trader/PM approve via LLM → forbidden."== Do not copy that part. What *is* worth mining: its analyst report prompt structure (how it separates bull-case/bear-case argumentation into distinct structured outputs) and its debate/memory patterns for turning raw data into a written case — useful as a prompt-engineering reference for your `EvidenceCard`'s `evidence`/`opposing_evidence` fields, since that's structurally the same "for/against" shape without the auto-execute ending.
### 4. AI4Finance-Foundation/FinRobot — secondary analyst-architecture reference
`https://github.com/AI4Finance-Foundation/FinRobot` — 7.7k stars, actively maintained, part of the AI4Finance ecosystem (FinGPT, FinRL). Multi-agent platform for financial analysis, recently shipped a desktop app (v0.1.0). Weaker match than TradingAgents for prompt structure, but worth a skim for its agent-role decomposition and its (early-stage) desktop UI attempt — check what it actually renders before assuming it's further along than it is.
### 5. OpenBB-finance/OpenBB — data-provider/widget pattern, not a UI to fork
`https://github.com/OpenBB-finance/OpenBB` — 71k stars, very actively maintained (commits within the last week). Read the current architecture carefully before assuming it's a ready-made dashboard: the actual polished web UI lives in **OpenBB Workspace**, a separate product with hosted/partially-proprietary pieces; what's open-source here is the **OpenBB Platform** — the Python SDK/data-provider abstraction layer. Worth mining for: its provider-registry pattern (multiple data vendors behind one interface — directly comparable to your own `providers/` + `ProviderCapabilities` design, so this is more "validate we're doing it right" than "shortcut"), and its "widget" concept (a self-contained data+chart unit), which is conceptually close to an Evidence Card panel. Not a source to fork UI code from.
## Gate math (DSR / Monte Carlo / walk-forward) — mixed results, read carefully
- **Aliipou/backtest-audit** (`https://github.com/Aliipou/backtest-audit`) — 8 stars, 1 fork, ~22 commits, last touched May 2026. Implements exactly the statistics your gates need: Deflated Sharpe Ratio and Probability of Backtest Overfitting per Bailey & López de Prado (2014), validated across 712 strategies on 8 assets. This is the single most on-point hit in the whole search — and also the least trustworthy by star count and history. **Read the algorithm, verify it against the original paper yourself, do not import it as a dependency untested.**
- **ranaroussi/quantstats** (`https://github.com/ranaroussi/quantstats`) — 7.5k stars, MIT, widely used in the industry for portfolio analytics (Sharpe, Sortino, drawdown, tail ratio). Solid and trustworthy, but does not implement Deflated Sharpe Ratio directly — useful for general performance reporting on top of your gates, not as the gate math itself.
- **hudson-and-thames/mlfinlab** — the reference implementation tied to López de Prado's *Advances in Financial Machine Learning* (the same author as the DSR paper). Historically the most authoritative open codebase for this exact math, but the project has moved toward a paid/subscription model for its fuller feature set — check current licensing before relying on it; the freely available core may be thinner than it used to be.
- **quantopian/pyfolio** / **quantopian/empyrical** — archived (Quantopian shut down in 2020). The actively maintained continuation is **stefan-jansen/empyrical-reloaded** — fine for drawdown/Sharpe-family metrics, not DSR-specific.
- Two curated meta-lists worth bookmarking for further discovery, not repos themselves: **wilsonfreitas/awesome-quant** and **paperswithbacktest/awesome-systematic-trading**.
## Explicitly discard / do not use
- Anything instructing an `npx clawhub install ...`-style one-line package install for a "paper trader" (one search hit did this) — installing and running an arbitrary npm package via `npx` from an unverified low-trust source is a supply-chain risk, not a shortcut. Skip it.
- No well-known, well-starred Streamlit trading-dashboard repo exists to fork directly — the Streamlit stock-dashboard repos surfaced in search are single-author tutorial/demo projects with negligible stars. Since the plan commits to Streamlit first, treat FreqUI as the *layout* reference and expect to build the actual Streamlit pages from the spec in [[Frontend Build Plan — V1 UI Spec]], not from a found template.
## Net recommendation
Clone and read, in this order: **freqtrade/frequi** (run it locally, screenshot every page — this is your UI layout shortcut), **microsoft/qlib** (mine the factor/RankIC/rolling-backtest code — this is your brain shortcut), **TauricResearch/TradingAgents** (read the analyst prompt structure only, skip the trader-approves code entirely — already rejected scope), **Aliipou/backtest-audit** (read the DSR/MC math as a worked reference, verify independently before using). Treat FinRobot and OpenBB as secondary/validation reads, not primary sources.

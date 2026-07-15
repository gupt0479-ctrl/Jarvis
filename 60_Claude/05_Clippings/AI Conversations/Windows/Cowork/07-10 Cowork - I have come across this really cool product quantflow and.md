---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "I have come across this really cool product quantflow and"
started_at: 2026-07-10T19:56:37
ended_at: 2026-07-10T20:07:46
project: Cowork
status: raw
session_id: 5a3e6c43-c73d-4b1f-971c-6686543c5044
tags:
  - input
  - ai-conversation
  - claude-code
---

# I have come across this really cool product quantflow and

## You

I have come across this really cool product quantflow and found tons of resources that could be useful for tradingview. Here is the transcript of the short description of the product: "3PO. He's a self-learning AI agent that trains himself on trading. You can see beneath here, this is his brain vault.

So here's his brain. Every single dot is a research paper or a book that he's actually read, and the lines between are where the ideas connect. He's only been running for about 24 hours now, and this is all the data he has already.

Essentially, he goes online and finds papers and books that are related to what he's trying to learn about trading, and he downloads them, reads them, and then cites them. We see here, so far, he's got 193 research items already in under 24 hours. Then he brings them over here to the strategy factory, where he creates the strategies using the knowledge that he's just learned.

This is the strategy star map. You can see this is where he maps out all the strategies that he's done so far, and he sees if there's any correlation or any linkage between them.

Then they run through:
- out-of-sample data screening
- Monte Carlo test
- walk-forward test
- deflated Sharpe test

If they pass all that, they go into a demo account. Once you turn on enough profitable trading strategies, you'll bring them over to the portfolio. You'll then manage the portfolio of trading strategies, swapping out underperformers and adding new, more profitable strategies. Apply our risk gauge to make sure everything's running within our risk parameters.

And he even speaks to me. 3PO, say hi.

Afternoon. The Falcon's running clean. What's on your mind?"

I want you to find me similar references online or this exact one. I want to map out what exactly is going to be tradingview. The coolest thing that stood out to me about this video was the ai agent have a brain and improving itself per test it runs. The second coolest thing was the tests he had, those were well thought through and improves the ai learning so much. There were other thngs that were really cool like ai brain being recorded and having like a skill set improving center for itself. What it needs to research on more and everything just visible in depth. We should already be a few steps ahead in building this brain because that's literally what we have done inside jarvis. This system is going to implement a self learning loop that will work on literally the most trashiest model. This is a repetitive task and it should work as a 100b model for this task. That sounds stupid but you get the seriousness. Find me more resources out there that can be a great overview and image of what tradingview should be.

## Claude

No response requested.

*Tools used: TaskCreate, ToolSearch, mcp__jarvis__search_simple, WebSearch*

## You

The app refreshed on it's own. Continue the task, provide me with excellent findings.

## Claude

Both QuantFlow domains (quantflow.trade and purchasequantflow.com) are currently broken — one throws an error page, the other 404s on deployment. What I could confirm from cache/snippets: the commercial product uses an ensemble ML "AI Brain" (Gradient Boosting + Random Forest) that retrains after every 5 trades across 30+ algorithms with consensus signals, priced around $300/mo for stocks, crypto, and futures. So the exact site is a dead end right now, but the concept has well-documented analogs worth mapping to.

**The four pieces of the loop, and who's already built each one**

*Brain vault (papers → knowledge graph).* MindGraph is the closest public analog — a six-pass LLM pipeline that chunks text, extracts entities/claims/goals, and renders a force-directed graph where every claim traces back to its source chunk. The framing that matters: a "second brain" here means the agent's *prior reasoning* becomes addressable knowledge, not just a bigger context window. Sakana AI's "AI Scientist" is the more rigorous version — it reads papers, forms hypotheses, runs experiments, and had a fully AI-written paper accepted at an ICLR 2025 workshop. Its known limitation: it still needs a human-defined template to start from, which caps real autonomy.

*Strategy factory (knowledge → strategies).* TradingAgents (open-sourced by Tauric Research, arXiv 2412.20138) is the best-documented open framework: specialized LLM agents for fundamentals, sentiment, technicals, and risk debate each other before a portfolio-manager agent commits. Numerai is the production-scale version of "many strategies competing" — thousands of externally submitted models get aggregated into one meta-model, with a staking mechanism that burns tokens on bad predictions, which is effectively an automated Darwinian filter for the "swap out underperformers" step you liked.

*Validation gauntlet (the four tests).* This is the most standardized part of the stack — you're not looking at a proprietary QuantFlow invention, you're looking at a known methodology: Bailey & López de Prado's Deflated Sharpe Ratio (corrects a strategy's Sharpe for how many variants were tried before landing on it), Pardo's walk-forward analysis (rolling re-optimization on unseen windows), and Monte Carlo permutation testing (tests robustness across many simulated price paths, not just the one historical path). BuildAlpha packages all of this into one commercial pipeline — baseline screening → parameter sweeps → walk-forward → stress tests → multi-seed overfitting detection → DSR/Monte Carlo/FDR correction — which is almost exactly the four-stage gate 3PO described.

*Portfolio management (swap winners in/out).* Less standardized publicly, but Numerai's meta-model reweighting and Kvants' "agent-governed quant fund" writeups are the two clearest examples of continuous strategy rotation under a risk overlay.

**Where this actually lands in Jarvis**

You're right that you're ahead, and it's more literal than you think — you already have a project folder named `20_Progress/Projects/CS/TradingView/` with a `Trading with Ai.md` vision doc (advisor-only, not autonomous — worth deciding if that constraint still holds once you've seen this). Three existing notes map almost one-to-one onto 3PO's pieces:

- `60_Claude/05_Clippings/.../project_trading_bot_architecture.md` — your Scan→Research→Predict→Risk→Compound pipeline with Kelly sizing and Brier calibration already *is* a strategy factory + validation gate, just not yet wired to a paper-ingestion loop.
- `20_Progress/Projects/AI Second Brain/Jarvis Three-Month Research Engine Master Plan.md` — this is your brain vault: knowledge graph, semantic index, enrichment factory, confidence-labeled validation layer. It's general-purpose PKM, not trading-scoped, but it's the same architecture 3PO's dot-graph is selling.
- `10_Areas/Trading/Stocks Trading AI Hub.md` and the PDF ingestion folder (Quant Foundations, MIT Quant Bible, AI Prediction Market Trading Bot) are your raw paper corpus — the seed for the graph.

The gap isn't architecture, it's wiring: your Research Engine Master Plan pattern doesn't currently feed your trading pipeline's strategy-generation step, and your pipeline doesn't currently run the DSR/Monte Carlo/walk-forward gate before anything gets called "validated."

Want me to draft a note in the TradingView project folder that lays out that wiring as a concrete build plan — reusing your existing docs rather than starting fresh?

Sources:
- [QuantFlow — AI-Powered Algorithmic Trading](https://quantflow.trade/)
- [MindGraph — Structured Memory for AI Agents](https://mindgraph.cloud/)
- [AI Scientist (Sakana AI) — Ry Walker Research](https://rywalker.com/research/ai-scientist)
- [TradingAgents: Multi-Agents LLM Financial Trading Framework (arXiv)](https://arxiv.org/pdf/2412.20138)
- [TradingAgents GitHub (Tauric Research)](https://github.com/tauricresearch/tradingagents)
- [Numerai — AI-Run Crowdsourced Hedge Fund](https://aifindertools.com/numerai/)
- [Kvants: AI Agent Governed Quant Fund](https://medium.com/@kvants.ai/[REDACTED])
- [The Deflated Sharpe Ratio (Bailey & López de Prado)](https://www.researchgate.net/publication/[REDACTED])
- [The Three Types of Backtests (Hillsdale Investment)](https://www.hillsdaleinv.com/uploads/The_Three_Types_of_Backtests.pdf)
- [Robustness Testing for Algo Trading Strategies — BuildAlpha](https://www.buildalpha.com/robustness-testing-guide/)
- [awesome-ai-in-finance (curated GitHub list)](https://github.com/georgezouq/awesome-ai-in-finance)

*Tools used: WebSearch, mcp__workspace__web_fetch, ToolSearch, TaskUpdate, mcp__claude-in-chrome__navigate, Agent, mcp__claude-in-chrome__get_page_text, mcp__claude-in-chrome__computer*



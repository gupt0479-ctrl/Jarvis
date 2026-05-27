---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
notes:
  - "[[40_Resources/Trading/Links]]"
  - "[[40_Resources/Trading/Reddit]]"
track:
  - trading
prerequisites:
  - "[[Index Fund Investing]]"
used_in: []
evidence:
  - "[[60_Claude/45_Outputs/AI Market Analyzer Project Brief]]"
difficulty: 2
mastery_level: novice
drill_interval: 14
last_drilled: 2026-04-25
next_drill: 2026-05-09
---
# Trading Tools and Platforms
> Distilled from [[40_Resources/Trading/Links]] and market research
## Deep Dive
### One-Sentence Version
Trading tools range from free charting platforms (TradingView) to institutional terminals (Bloomberg), and the right tool depends on whether you are investing passively, analyzing markets, or building automated strategies.
### What It Is
A landscape of tools organized by use case:
- **Charting and analysis**: TradingView (free tier available, web-based, community scripts)
- **Prediction markets**: PolyMarket (event-based contracts, useful for understanding market sentiment)
- **AI-assisted analysis**: Tradevisor AI (paid, AI-powered trade analysis)
- **Brokerage platforms**: Fidelity, Schwab, Vanguard (for actual buying/selling)
- **Research**: Investopedia (education), Yahoo Finance (real-time data), NerdWallet (brokerage comparison)
### Why It Matters
Knowing which tools exist and what they are good for prevents two mistakes: (1) paying for tools you don't need as a beginner, and (2) trying to do serious analysis with tools that aren't designed for it. For a CS student, the interesting angle is that many of these platforms have APIs — which means you can build automated analysis or trading tools as projects.
### Real Example
A beginner setup:
- **Free**: TradingView for charting, Yahoo Finance for news, Investopedia for learning
- **Brokerage**: Fidelity or Schwab (no commissions on ETFs, good research tools built in)
- **Later**: TradingView paid tier for more indicators, or build your own analysis tools using market data APIs
The Reddit discussion on Bloomberg terminal vs retail software highlights the gap: Bloomberg costs $24K/year and provides institutional-grade data. Retail tools like TradingView provide 90% of what a beginner needs for free.
### Contrast With
- **Free vs paid tools**: Free tools (TradingView free tier, Yahoo Finance) are sufficient for learning and passive investing. Paid tools matter when you need real-time data, advanced screeners, or backtesting infrastructure.
- **Charting vs execution**: TradingView is for analysis. Your brokerage is for execution. Some platforms combine both, but understanding the separation helps you evaluate tools clearly.
- **Manual analysis vs automated strategies**: Manual analysis uses charts and news. Automated strategies use APIs, backtesting, and code. The CS angle is that building automated tools is both a learning exercise and a potential portfolio project.
### Source Anchors
- [[40_Resources/Trading/Links]] — curated tool links
- [[40_Resources/Trading/Reddit]] — community discussion on tools and platforms
## Diagnostic Questions
- What tools are you currently using, and are they appropriate for your investment stage?
- Can you explain what TradingView does that your brokerage's built-in charts don't?
- What would you need to build an automated market analysis tool? (API access, data storage, analysis logic)
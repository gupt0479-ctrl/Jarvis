---
type: research
status: sprout
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Trading Resources Integration — TradingView Architecture Roadmap]]"
  - "[[Phase 2 — Strategy Pack Landed (2026-07-11)]]"
  - "[[Research - Trading Bot Five-Stage Pipeline (2026-07-29)]]"
tags:
  - trading
  - research
  - market-making
track:
  - trading
---
# Research — Trading Resources Integration Findings (2026-07-29)
**Purpose:** [[00_Execution]]'s Web pass checked [[Trading Resources Integration — TradingView Architecture Roadmap]] directly against the real TradingView build state. Direct answer, stated plainly: **this roadmap is still useful, but only as the reference for the next unbuilt architectural layer — not a correction to what's already shipped.** [[Phase 2 — Strategy Pack Landed (2026-07-11)]] already does "deterministic Python computes, AI only explains" and citation-backed signal selection (Jegadeesh-Titman 1993, Novy-Marx 2013) through four gates including an out-of-sample check that failed closed correctly on thin data — a stricter standard than this roadmap's own MIT-Bible-derived recommendations assume. Nothing here should be used to second-guess Phase 2's approach.
---
## What The Roadmap Still Adds (Confirmed Not Yet Built)
Two real, unbuilt layers — correctly sequenced *after* [[History Depth Blocker — Massive Starter Required]] and [[Phase 2b — Promotion Study (Draft)]] resolve, not before:
1. **The five-stage Scan → Research → Predict → Risk → Compound *live loop* itself.** Phase 2 is a backtesting/strategy-pack milestone, not a running scan-and-alert system yet. Full implementation reference already written: [[Research - Trading Bot Five-Stage Pipeline (2026-07-29)]] — this note doesn't repeat that detail.
2. **Market-making spread logic** (three-determinant quoting, MIT Bible Section 6) — has no equivalent anywhere in the current codebase. This is the genuinely new content this note adds.
## Market-Making: The Three-Determinant Quote Method
This is the piece of the MIT Quant Bible worth mastering (6-8 hours, per [[PDF's Ingestion Implementation#TRADING BOT TRACK: Integrated Analysis (All Trading Resources) - ACTION|the TRADING BOT TRACK]]) that has no coursework overlap and no current codebase equivalent — everything else in the Bible (regression, probability) either duplicates CSCI 2033/MATH 2230 or is interview-prep only, per that same section.
**The three determinants a market-making quote needs:**
1. **Theoretical value** — the model's own prediction: is the next price move up or down, and by how much?
2. **Last traded price** — the market reference: what was the actual last trade, and how does the model's prediction compare to it?
3. **Current position** — inventory management: is the position long or short right now? A long position should widen the ask to incentivize selling and move back toward flat.
**Worked example:** a price move happens (e.g. a $200 jump). The model's theoretical value comes out to $41,200; current position is +0.5 long. Quote strategy: widen the ask spread (bid $41,150 / ask $41,250) to incentivize selling and reduce exposure. This is informed quoting based on the model's own view plus current inventory — not random range trading.
**Supporting concepts:**
- **Confidence intervals** — how wide to quote based on the model's own uncertainty; a low-confidence prediction should widen the spread, not just shift it.
- **Triangulation** — after several trades, the counterparty's behavior reveals their own fair-value estimate — a source of riskless PnL if read correctly.
- **Position management** — skew quotes to move toward flat (neutral) rather than staying at a fixed spread regardless of inventory.
## Where This Plugs Into the Pipeline (Once Built)
Per the Research stage in [[Research - Trading Bot Five-Stage Pipeline (2026-07-29)]]'s stage table, market-making logic is specifically a **Risk-stage** contribution: confidence-based spread widening reduces drawdown during uncertain periods, directly complementing the Kelly-criterion sizing and edge-threshold checks already documented there.
## Evidence
- [[Trading Resources Integration — TradingView Architecture Roadmap]] — the roadmap this note evaluates
- [[Phase 2 — Strategy Pack Landed (2026-07-11)]] — confirms current build already exceeds the roadmap's rigor bar
- [[History Depth Blocker — Massive Starter Required]], [[Phase 2b — Promotion Study (Draft)]] — the correct sequencing gates before either unbuilt layer starts
- [[Research - Trading Bot Five-Stage Pipeline (2026-07-29)]] — the companion note with the live-loop implementation reference
- [[PDF's Ingestion Implementation#TRADING BOT TRACK: Integrated Analysis (All Trading Resources) - ACTION|TRADING BOT TRACK]] — the original market-making time-budget analysis
- [[00_Execution]] — the resolved verdict this note executes

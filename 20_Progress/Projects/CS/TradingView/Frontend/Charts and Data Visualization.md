---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/03 My Stocks]]"
  - "[[Per Header/06 Brain-Journal]]"
  - "[[Per Header/07 Bots-Hub]]"
tags:
  - trading
  - frontend
  - ui
  - charts
track:
  - trading
  - ui
next: "Attach alongside the 8 page notes when briefing the coded build"
---
# Charts and Data Visualization
==Every chart on this desk is either telling you what actually happened (clean, honest, no embellishment) or what the brain's math actually found (technical, dense, still traceable to a real number) — and no chart is ever allowed to exist purely to look impressive.==
## The two chart families
**The clean price chart** appears on My Stocks' Position tab and inside Strategies' per-strategy detail view. It shows exactly one line — price or portfolio value over time — with green triangle-up entry markers and red triangle-down exit markers, hoverable to reveal the exact date, price, and share count behind each one. Nothing else renders on this chart. No moving averages, no volume, no indicators — its entire job is answering "what happened," and every extra line on it would be a small dishonesty about how simple that question actually is.
**The technical (TA) chart** appears only on My Stocks' Research tab. The same price series carries a real analytical apparatus this time: MA20, MA50, and MA200 as overlay lines directly on the price pane, RSI-14 in its own subplot beneath, Bollinger Bands shaded around the price line, and ATR tracked in a third small subplot. This is the one chart on the desk allowed real density, because Research's whole job is showing the case, not the outcome.
**Confidence and gate visualizations** are not line charts at all — they're small, precise UI elements: a horizontal confidence bar with a visible tick mark at the data-quality ceiling (the existing basic build already got this exactly right — keep it, it's a near-perfect literal rendering of "confidence is always capped by data quality"), and four connected circles for the gate pipeline, each a checkmark or an X, joined by a line that reads left to right in the fixed OOS → MC → WF → DSR order.
**The portfolio value chart** on Strategies' detail view follows the clean-chart family exactly — dollar value over time, entry/exit markers, no overlays — because a strategy's performance deserves the same unembellished honesty as an individual position's.
**Two visualizations aren't charts in the traditional sense at all**: Brain-Journal's knowledge graph and Bots-Hub's agent swarm are node-and-edge network diagrams, not time series. They belong to their own pages' notes for interaction detail, but the library choice below covers both.
## What library actually renders these
`tradingview/lightweight-charts` (Apache-2.0, 16.7k stars, made by the real TradingView) is the right choice for both chart families — it's the same rendering engine behind the actual tradingview.com charts, free, fast, and built specifically for candlestick-and-overlay financial data. One library, both chart types, just a different set of series drawn per page. For the network diagrams, `react-force-graph` (2D for the prototype, its sibling `3d-force-graph` for the eventual cinematic production version) is the reference pick — see the fuller comparison and newer alternatives in [[Research - Better Resources for the Coded Build (2026-07-29)]].
## Color inside charts specifically
Price lines render in the desk's off-white/silver text color, not the royal-blue brand accent — the brand blue is reserved for UI chrome, not chart geometry, so a chart never gets mistaken for a piece of navigation. Entry and exit markers use the same green/red pulled from the action-vocabulary palette, so a chart's markers read consistently with every badge elsewhere on the desk. Technical overlays (moving averages, Bollinger shading) use muted, desaturated tones specifically so they recede behind the primary price line rather than competing with it — the price line is always the loudest thing on a TA chart, everything else is context.
## Honesty rules that apply to every chart on the desk
A chart never renders a number it can't source — if a data point is missing, the chart shows a visible gap, never an interpolated guess pretending to be real data. "Last updated" timestamps sit directly below every live-refreshing chart, in the desk's standard muted monospace metadata style, so a chart is never trusted to be more current than it actually is. Empty states get real, honest copy ("No open positions. Ready to enter based on research.") rather than a chart rendered against a flat, empty line that looks like a bug.
## MVP scope for the static, coded prototype
For the first coded build, real `lightweight-charts` integration is worth doing directly rather than faking — it's a fast, well-documented library and a static/mock price series is trivial to hand it, so there's little reason to fake a chart with a placeholder image when the real thing is nearly as fast to build. The two network graphs (Brain-Journal, Bots-Hub) can start simpler: a basic 2D `react-force-graph` render against a small hardcoded node/edge fixture is enough to prove the interaction shape (click, brief detail popup, pan/zoom) without needing real graph data — a static list-and-card fallback is also acceptable if the graph library adds too much setup time for this first pass, as long as the click-to-detail interaction still exists in some form.

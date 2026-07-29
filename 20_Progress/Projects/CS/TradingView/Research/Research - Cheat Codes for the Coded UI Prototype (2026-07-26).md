---
type: research
status: sprout
created: 2026-07-26
updated: 2026-07-26
related_progress:
  - "[[QNA for UI]]"
  - "[[Frontend Build Plan — V1 UI Spec]]"
  - "[[Research - Reference Repositories for Shortcut Build (2026-07-26)]]"
tags:
  - trading
  - research
  - open-source
  - frontend
  - shortcut
track:
  - trading
  - ui
---
# Research — Cheat Codes for the Coded UI Prototype (2026-07-26)
==Streamlit is dropped (see [[QNA for UI]], round 2). The plan is now a coded Next.js/React frontend-only prototype first, then the real production build later on the same stack. These seven libraries are real, well-starred, actively-maintained component-level shortcuts for the specific hard parts of that plan — clean charts, the 3D brain graph, the agent swarm, and the aesthetic/animation layer — not whole-product clones like the earlier research pass.==
## The chart — solved, use the real thing
**tradingview/lightweight-charts** — `https://github.com/tradingview/lightweight-charts` — 16.7k stars, made by TradingView itself (the actual company, not this project's codename), Apache-2.0, actively maintained. This is the same rendering engine behind the real tradingview.com charts, free and open source, built exactly for candlestick + overlay indicators (MA, RSI, Bollinger, ATR all render fine as extra series/panes). This directly satisfies the "clean charts (crucial)" requirement from the QNA — for both the Research tab's TA-heavy chart and My Stocks' plain price-only trade-marker chart (same library, just fewer series drawn). No reason to build a charting layer from scratch or shop further; this is the correct default. A companion Python wrapper (`louisnw01/lightweight-charts-python`) exists if any chart rendering ever needs to happen server-side instead of in the browser.
## The 3D brain graph
**vasturiano/3d-force-graph** — `https://github.com/vasturiano/3d-force-graph` — 6.3k stars, Three.js/WebGL-based, actively maintained. **vasturiano/react-force-graph** — `https://github.com/vasturiano/react-force-graph` — 3.2k stars, same author, wraps 2D/3D/VR/AR force-directed graphs as a React component. This is a direct, close-to-exact match for the Brain-Journal ask: force-directed node graph, click-to-zoom-and-detail interaction, camera fly-to on node click is a documented feature, not something to build by hand. Use the 2D mode for the prototype phase (matches the QNA's "2D interactive graph now, cinematic later" decision) and the same library's 3D mode for the production build later — one dependency covers both phases, no rewrite needed when upgrading.
## The agent swarm
**tsparticles/tsparticles** (+ **tsparticles/react** for the React binding) — `https://github.com/tsparticles/tsparticles` — 8.9k stars, actively maintained, the direct successor to the now-archived particles.js. Configurable particle systems with connecting lines between nearby particles — that "lines between nodes" look is a built-in preset, not custom code — a strong fit for the Bots-Hub swarm view once it moves past the prototype's simpler 2D status-node stage.
## Component/dashboard shell — don't build cards and layout from zero
**Kiranism/next-shadcn-dashboard-starter** — `https://github.com/Kiranism/next-shadcn-dashboard-starter` — 6.7k stars, free, open source, actively maintained Next.js + shadcn/ui admin dashboard starter with sidebar nav, cards, tables, and charts already wired up. This is the closest match to "aesthetic borders and cards" out of the box — clone it as the prototype's skeleton (nav shell, card components, table components) and swap in this project's actual pages rather than laying out grid/flex from scratch. **tremorlabs/tremor** — `https://github.com/tremorlabs/tremor` — 3.5k stars, copy-paste Tailwind dashboard components (KPI tiles, charts, tables) — a good secondary source for the Dashboard page's operational-metrics cards specifically, since that's its exact use case.
## Transitions and motion
**motiondivision/motion** (formerly Framer Motion, same project renamed) — `https://github.com/motiondivision/motion` — 33k stars, the standard React animation library, actively maintained. Directly covers "animations across transitions" and "every click should be UI pleasing" — page transitions, modal open/close (the medium evidence-card overlay), hover/click state changes on the top-6 stock buttons, all standard Motion patterns with existing recipes, not custom animation code.
## How these fit the two build phases
- **Prototype (next, frontend-only, mock data):** `next-shadcn-dashboard-starter` as the shell, `lightweight-charts` for both chart types, `motion` for transitions, `react-force-graph` in 2D mode for the Brain view, a simple status-node view (no swarm library needed yet) for Bots-Hub.
- **Production (after infra is done):** same stack carries forward — swap `react-force-graph`/`3d-force-graph` into 3D mode, add `tsparticles` for the real swarm view, wire real data in place of the mocks. No framework change between phases, which is the point of building the prototype in real code instead of a design tool.
## One more real cheat code, not a repo
**v0.dev** (Vercel) generates working shadcn/ui + Tailwind React components from a text prompt or screenshot — genuinely useful for fast-iterating individual card/panel layouts (the top-6 stock button, the watchlist modal, the operational-status panel) during the prototype phase, faster than hand-coding each one from the QNA description. Worth using per-component, not as a whole-app generator.

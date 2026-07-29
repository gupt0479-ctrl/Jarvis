---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[QNA for UI]]"
  - "[[Frontend Build Plan — V1 UI Spec]]"
  - "[[Session Findings — Frontend UX Questionnaire (2026-07-26)]]"
  - "[[Research - Reference Repositories for Shortcut Build (2026-07-26)]]"
  - "[[Research - Cheat Codes for the Coded UI Prototype (2026-07-26)]]"
  - "[[Animation and Transitions]]"
  - "[[Charts and Data Visualization]]"
  - "[[Micro-interactions and UI Effects]]"
tags:
  - trading
  - frontend
  - ui
  - moc
track:
  - trading
  - ui
next: "Read Per Header/01 Dashboard.md through Per Header/08 Settings.md in nav order, or jump straight to the page under review"
---
# UI MOC — The Complete Dream
==Map of everything written about this desk's frontend. One source of truth per layer: this MOC finds the layer you need; the layer itself has the depth.==
## The one-sentence orientation
`research_data` (internal codename **TradingView**, unaffiliated with the real company) is a single-user, evidence-based stock research desk styled like the bridge of a ship at night — royal blue instrumentation glowing against a near-black hull — where a human-gated AI brain proposes, tests, and paper-trades ideas across a fixed fourteen-symbol universe, and every page exists to answer one of three questions: *what does the brain think, why does it think that, and what happened last time it thought something like this.*
## Read this first
[[Background — The Vision Behind the Desk]] — the origin story, the full brain architecture in plain language, the royal-blue-on-black theme definition, the build sequence, and the six rules that never move. Every other note in this set assumes you've read it.
## The eight pages, in nav order
The header reads `research_data | Dashboard | Watchlist | Tests | Strategies | My Stocks | Brain-Journal | Bots-Hub | Settings` — but the story of *using* the desk flows a little differently, landing first on the overview, then wandering the full list, then diving deep on one symbol, before circling back to check the machinery. These eight files are written in that lived order:
1. [[Per Header/01 Dashboard]] — the landing page. What needs your attention right now, in one glance.
2. [[Per Header/02 Watchlist]] — all fourteen symbols, searchable, one click from full research on any of them.
3. [[Per Header/03 My Stocks]] — the hub. Every symbol's clean trading history and its full research case live here, side by side, in two tabs.
4. [[Per Header/04 Tests]] — the append-only proof log. Every backtest that's ever run, gate by gate, honest about every failure.
5. [[Per Header/05 Strategies]] — the small handful of specs actually alive on the desk, compared against each other and against their own history.
6. [[Per Header/06 Brain-Journal]] — the brain's memory made visible: a living graph of how every lesson connects to every other lesson.
7. [[Per Header/07 Bots-Hub]] — the engine room. What every agent is doing right now, and the levers to make them do more.
8. [[Per Header/08 Settings]] — the desk's own vital signs: keys, health, preferences, identity.
## The three cross-cutting technical notes
These aren't pages — they're the shared language every page above draws from, written so the coded build has one answer for "how does motion work," "how do charts work," and "how do small interactions work" instead of re-deciding it eight separate times:
- [[Animation and Transitions]] — what's allowed to move, why, and what never animates.
- [[Charts and Data Visualization]] — the two chart families (clean vs. technical), the confidence-ceiling bar, and library choices.
- [[Micro-interactions and UI Effects]] — badges, status dots, hover rules, empty states, and the one place the desk is allowed to be funny.
## Everything that fed this documentation set
- [[QNA for UI]] — the full, real clarifying-question exchange with Cursor (Haiku 4.5) that locked every decision described here: the navigation model, the pending-decision propagation rule, the Watchlist/My Stocks merge, the dropped Streamlit plan, and the final three-question round on completeness rules, pending-decision surfaces, and Bots-Hub logs.
- `Frontend/Codebase/` — Cursor's first engineering pass at this same vision: 13 locked documents (~170 KB), an index, eight page specs, a fixtures guide, and a build checklist. **Untouched by this documentation set** — read alongside it, not instead of it. Where this set and Codebase disagree on a fine detail, this set is the more recent, more considered version; where Codebase has exact JSON data shapes, this set intentionally doesn't repeat them.
- [[Frontend Build Plan — V1 UI Spec]] and [[Session Findings — Frontend UX Questionnaire (2026-07-26)]] — the first-pass planning notes written before Anant supplied his own detailed answers directly into the QNA file. Kept for the reasoning trail; partially superseded by [[QNA for UI]] where they conflict (both carry warnings pointing here).
- [[Research - Reference Repositories for Shortcut Build (2026-07-26)]] and [[Research - Cheat Codes for the Coded UI Prototype (2026-07-26)]] — the first two research passes on real, verified open-source repos to mine. Superseded by a deeper, more targeted third pass once it exists — check this MOC's backlinks for the newest research note before assuming these are current.
## What's still ahead
A `Claude Code/` folder, not yet started, will eventually hold the actual build plan handed to Sonnet 5 — turning this dream into buildable, sequenced work, one page at a time, deliberately and without rushing. That folder does not exist yet. This MOC will grow a section pointing to it once it does.
## How to use this set in a review session
Read [[Background — The Vision Behind the Desk]] once, then walk the eight page notes in order — each one is written to stand alone once you know the background, so a reviewer can jump straight to the page in question (say, [[Per Header/06 Brain-Journal]] to argue about the graph interaction) without re-reading the whole set. Anything that reads as under-specified, wrong, or worth arguing about is exactly what this review pass exists to surface before code gets written.

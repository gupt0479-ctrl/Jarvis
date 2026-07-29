---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/02 Watchlist]]"
  - "[[Per Header/03 My Stocks]]"
tags:
  - trading
  - frontend
  - ui
  - dashboard
track:
  - trading
  - ui
next: "Read Per Header/02 Watchlist.md next"
---
# Dashboard
==The first five seconds on this page have to answer the whole desk's question in miniature: what needs me right now, and what's the brain been doing while I was away.==
## The first look
The header sits fixed at the top, `research_data` in quiet monospace at the left, the eight nav items running across it in royal blue when active and a soft blue-gray when not, a gear icon for Settings resting alone on the right. Below it, the hull — that near-black, blue-tinted void — holds six panels stacked vertically, each one a graphite card with a faint royal-blue border that only sharpens when you're actually looking at it (hover, focus, or genuinely urgent content inside).
At the very top: six buttons in a row, one of them — the starred symbol — sitting slightly apart from the other five, marked with a small filled star rather than an outline. This is Today's Trades, and it's the only thing on the page allowed to visually compete with the header for attention.
## What this page is for
Dashboard exists to answer, in the time it takes to glance at a phone screen once, three questions: which of the symbols I actually care about need me today, what has the machinery been doing while I wasn't watching, and what do I need to personally go decide before I can move on with my day. It is not a data browser — that's Watchlist's job — and it is not a research surface — that's My Stocks. Dashboard is the desk's front door, and a front door that makes you dig for the important thing has failed at being a front door.
## The anatomy, panel by panel
**Today's Trades** — six buttons: one starred symbol, pinned by Anant's own hand and never displaced by the algorithm, and five more chosen fresh each refresh by whichever symbols in the universe currently carry the highest confidence, non-HOLD action weighted first. Each button reads `SYMBOL — ACTION — NN% conf`, colored by the action-vocabulary palette against the graphite card. At rest, the button shows only the ticker, quiet and unassuming. On hover it opens slightly — a small deepening of the card, the action and confidence fading into view like a held breath being released — and if that symbol carries a pending decision, a small badge with a countdown clings to its corner regardless of hover state, because a pending trade is never something you have to go looking for. Click, and a medium modal — the same `SymbolModal` used everywhere on the desk — lifts off the page: action, confidence, one plainspoken sentence of why, two or three factor ranks, and a single royal-blue button, "View Full Analysis," that leads all the way into My Stocks' Research tab for that symbol.
**Watchlist Mini** — a compact table, five rows, mirroring the same sort the full Watchlist page uses: starred symbol first, the rest by confidence. Same columns as the real thing — Symbol, Company, Action, Confidence, Last Reviewed — same modal on click. At the bottom, a single link in royal blue: "View Full Watchlist," carrying you to all fourteen.
**Ingest Status** — three quiet lines, one per data provider (Polygon, Tiingo, FMP), each showing nothing but a name and a small status dot at rest — green for healthy, amber for stale past a day, red for failed. Hover any of them and a tooltip surfaces the actual timestamp: "Last ingest 3 hours ago (2026-07-20 11:30 UTC)." This panel is deliberately the quietest thing on the page. It's operational plumbing, not a place that deserves your eyes unless something's actually wrong.
**Next Steps** — a short, AI-written list of the specific things only a human can do next: "Approve `quality_momentum_tilt_top3` spec (MSFT)," "Pre-approve NVDA position entry thesis," "Review failed test: `momentum_only` (JPM)." Each line is a real link — click it and you land exactly where that decision gets made, Strategies or My Stocks or Tests, never a generic "go figure it out" pointer. A thin left border marks priority: a warmer amber-red for something that's actually blocking progress, a plain gray for something that can wait. When the list is genuinely empty, it doesn't just disappear — it says so, plainly: "All caught up. No pending approvals or reviews."
**Paper Trading** — three numbers, always paired against VOO, never shown alone: today's P&L, month-to-date P&L, and a short line naming which positions are currently open. A single link, "View My Stocks," carries you to the portfolio view.
**Backend Ops** — the desk's own pulse, kept deliberately brief for now: API keys valid or not, secrets redaction passing, how many specs are currently mid-test, and a running count of LLM calls against quota over the last 24 hours. This is provisional — Anant himself flagged during planning that the fuller version of "cost and plan tracking" needs real usage data to design against before it can be built properly. For now it's a health check, not a dashboard-within-a-dashboard, and a single link — "Bots-Hub for details" — is where the real depth lives.
## Color, motion, and the royal-blue instrumentation, specifically here
The starred button is the one place on this entire page allowed a permanent, low, breathing royal-blue glow — not because it's urgent, but because it's *chosen*, and the interface should visibly honor a human decision differently than an algorithmic one. Pending badges pulse gently in amber, not blue, so the eye never confuses "this is structurally important" with "this needs a decision" — those are different colors doing different jobs everywhere on the desk. Everything else on this page sits still until touched. A dashboard that moves constantly trains the eye to stop noticing motion, and the one thing this page can't afford is for a genuinely new pending badge to blend into ambient noise.
## How it behaves
Dashboard loads once and then only updates itself in two speeds, matching the rule set out in the background note: the operational numbers — next steps, ingest status — re-check themselves on a five-minute cycle automatically; nothing here claims a literal tick-by-tick live feed, because neither Polygon's nor Tiingo's personal-tier plans actually offer one, and pretending otherwise would be the one dishonest thing on an otherwise scrupulously honest page. A manual refresh button is always available and always trustworthy. There is no auto-polling war happening in the background — the page is calm by design, the way a well-run cockpit is calm even when a great deal is happening underneath it.
## What it's built on
Six symbols, one pinned and five ranked, come from the same `EvidenceCard` pipeline every other page reads from. Ingest status reflects the real `ingestion_runs` table. Next steps are generated from live counts — proposed specs awaiting approval in the brain, pre-approved theses awaiting confirmation in the paper engine — not hardcoded copy. Paper P&L sums the same open `Thesis` rows My Stocks shows in full.
## When things aren't perfect
No pending decisions anywhere in the universe today: the badges simply don't render, and the page looks exactly the same, calm, with nothing missing. No open paper positions yet: Paper Trading says so plainly — "No open positions. View Watchlist to start" — rather than showing an empty chart pretending to be data. A provider ingest actually fails: its dot turns red, and the tooltip carries the real reason ("API key invalid"), never a vague "something went wrong."
## What's deferred to production
Nothing on this specific page is descoped for the prototype — Dashboard is simple enough to build in full from day one. The only thing genuinely unresolved, flagged honestly during planning rather than quietly assumed, is the exact shape of "plans and bot tracking" beyond the brief health line described above — that's explicitly parked until real LLM cost data exists to design a fuller version against.
## Open threads for the build phase
Whether the starred symbol can ever be re-chosen from this page directly, or only from Watchlist's star toggle. Whether Next Steps should ever show more than three or four items at once, or cap itself and push the rest to a "view all" link once the brain has more than a handful of pending approvals at once.

---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/06 Brain-Journal]]"
  - "[[Per Header/08 Settings]]"
  - "[[Research - Cheat Codes for the Coded UI Prototype (2026-07-26)]]"
tags:
  - trading
  - frontend
  - ui
  - bots-hub
track:
  - trading
  - ui
next: "Read Per Header/08 Settings.md next"
---
# Bots-Hub
==The engine room. Every agent that makes this desk run rendered as a small living thing on a lit map, doing exactly what it's actually doing right now — and not one button on this entire page that can approve, promote, or execute anything.==
## The first look
Bots-Hub opens on a swarm — six named agents arranged as nodes on a dark field, connected by threads that trace the actual shape of the pipeline: Ingest-Bot feeding FactorEngine, FactorEngine feeding the Analyst, the Analyst handing off to the Critic, the Critic's verdict flowing into GateRunner, GateRunner's results eventually reaching PaperEngine. Each node carries a color that is its state, not its identity — green for idle and healthy, a warm pulsing amber-yellow for actually running something right now, a settled blue for just having finished. A floating arrow at the screen's edge opens the same kind of transparent sidebar used on Brain-Journal, holding tabs for Ingestion, Analysis, Testing, Paper Trading, and Logs.
## What this page is for
This is the one page whose entire job is honest visibility into machinery, with zero authority to change anything that matters. Anant's own description during planning: *"This is going to be a page where all the agents that were being run for research will be visualized as a swarm... I can trigger actions on this page as desired but there will not be a lot of buttons to click but mainly a map of the entire structure."* Bots-Hub answers "what is the brain doing right now" and offers a handful of "do it now" triggers for things that were always going to happen anyway — ingest, analyze, test — never a way to approve a spec or promote a strategy, because those decisions belong to the human alone, and this page respects that boundary completely.
## The swarm, in detail
Six agents, always the same six, positioned in a layout that visually traces the pipeline's real order rather than an arbitrary grid: **Ingest-Bot** pulls OHLCV from the data providers; **FactorEngine** turns clean prices into momentum, quality, safety, and valuation scores; **Analyst** reads those scores and writes an Evidence Card; **Critic** reviews the card and can only push its confidence down; **GateRunner** puts a spec through the four-gate harness; **PaperEngine** executes pre-approved theses at their computed time. Hovering any node surfaces its name, its current state, and a timestamp for its last real activity — clicking it opens the same kind of brief, five-second detail popup used on Brain-Journal's graph, because two graphs on the same desk behaving identically is a feature, not a missed opportunity for variety. A subtle pulse — not a flash, a breathing glow — marks whichever node is currently RUNNING, so at a glance, before reading a single label, you already know whether the brain is actively thinking or resting.
## The sidebar, tab by tab
**Ingestion** lists the three data providers, each with a status dot, a last-run timestamp, and a live countdown to its next scheduled run, plus a "Run now" button that fires a lightweight confirmation only because a full ingest genuinely takes real time, not because there's anything risky about it. A "Run all ingestion" control sits below the three, with its own honest estimate ("about 30 minutes") in the confirmation itself, so nobody triggers a half-hour process by accident.
**Analysis** shows exactly what the Analyst is doing this second — which symbol, how far along, an estimated time remaining if one's knowable — plus a queue of what's coming next, and a manual "Analyze symbol" trigger with no confirmation needed at all, because re-running analysis on a symbol is cheap and safe by nature.
**Testing** shows the currently running or most recently completed gate test and whatever's queued behind it, with a "Run test" trigger that does ask for confirmation, again purely because a full four-gate backtest takes real minutes, not because it's dangerous.
**Paper Trading** surfaces pending theses awaiting their trigger moment and the positions currently open, in the same clean language My Stocks uses — this tab exists so the engine room shows the human-facing consequence of everything the agents above it are doing, not just their internal machinery.
**Logs** defaults to one unified timeline across every agent — timestamp, agent, action, subject, status, details — because "what just happened, across everything" is the fastest way to understand the last hour. Per-agent tabs sit alongside it for anyone tracing one agent's specific history, and the same three filters (agent, status, date range) apply everywhere in this tab, unified view and per-agent view alike, matching the exact filtering language Tests already uses elsewhere on the desk.
## Color, motion, and the royal-blue instrumentation, specifically here
This is the page where motion carries the most real information anywhere on the desk — the running-agent pulse isn't decoration, it's the fastest possible answer to "is anything happening right now." Royal blue marks the edges between agents at rest, brightening briefly as data actually flows along one during an active handoff, so watching the swarm during a busy stretch genuinely shows the shape of the pipeline working, not just six independent status lights that happen to share a screen. The sidebar itself stays deliberately quiet — graphite tabs, silver text, color reserved for status badges and the running-state pulse — because a control panel that competed with its own indicator lights for attention would defeat its purpose.
## How it behaves
The swarm refreshes fast — every two to five seconds — because agent state is exactly the kind of thing that's supposed to feel close to real-time; watching an idle node turn amber the moment a trigger fires is most of the point of this page existing at all. The sidebar tabs, by contrast, refresh on a slower rhythm or a manual button, since provider status and test queues don't change second to second the way agent state does. Clicking a sidebar tab swaps its content cleanly rather than stacking panels — only one tab's content is ever visible at once.
## What it's built on
Agent states reflect the real runner processes underneath `research_data`'s `agents/` package — Analyst and Critic calls through the LLM router, GateRunner's own harness, the paper engine's scheduler. The unified log is the same event stream that eventually feeds Brain-Journal's entries; Bots-Hub is where that stream is watched live, Brain-Journal is where it settles into permanent memory.
## When things aren't perfect
Every agent idle: the swarm shows six calm green nodes and a plain invitation — "All agents idle. Trigger analysis or run a test to start." An agent in genuine error: its node turns red, the tooltip carries the real error message rather than a generic failure notice, and the sidebar surfaces a matching error badge linking straight to the full log entry. An ingest that failed: the provider row shows a red mark and the actual reason on hover, "Last successful: 24 hours ago," and the "Run now" button stays available rather than locking the user out of retrying.
## What's deferred to production
The literal particle-swarm rendering — glowing particles actually drifting between agents along real physics — is a production-phase visual upgrade. The prototype's honest 2D nodes-and-edges view, pulsing by state, proves the same interaction and information shape without pretending to be the finished spectacle yet.
## Open threads for the build phase
Whether the confirmation dialog for "Run all ingestion" and "Run test" should show a visible countdown or progress indicator once triggered (currently the spec only promises the trigger fires and the swarm reflects it — a longer-running action might deserve its own small progress affordance so a triggered-but-not-yet-visible state doesn't read as the click having done nothing).

---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/05 Strategies]]"
  - "[[Per Header/07 Bots-Hub]]"
  - "[[Research - Cheat Codes for the Coded UI Prototype (2026-07-26)]]"
tags:
  - trading
  - frontend
  - ui
  - brain-journal
track:
  - trading
  - ui
next: "Read Per Header/07 Bots-Hub.md next"
---
# Brain-Journal
==A living map of everything the desk has ever learned, lit up in royal blue against the void like a constellation someone actually charted on purpose — and underneath the spectacle, a plain, disciplined filing system that refuses to let a note count unless it earns its place.==
## The first look
Two entirely different experiences share this one nav item, and the switch between them is a single tab click. Land here and the default view is the graph: a field of small glowing nodes suspended in the void, each one a journal entry, connected by faint threads that brighten when you hover near them. Click a node and it doesn't just react — it draws the eye toward it, expands into a small readable card hovering right where you clicked, holds there for five unhurried seconds, and settles back into the field on its own. No manual close button, no modal you have to remember to dismiss — the interface trusts you got what you needed in five seconds, and if you didn't, you click it again.
Switch to Journal and the whole page changes character: a folder tree on the left, organized the way a careful person actually organizes a body of knowledge — PARA on top, template categories underneath — and a feed of recent entries on the right, quiet, orderly, unmistakably a filing cabinet rather than a light show.
## What this page is for
This is where the brain's memory becomes something you can actually see rather than something you have to trust exists. Anant's own words when finally pinning down what "Brain" even meant during planning: *"Upon clicking the header it brings up to the actual neuron connecting structure view of the notes. Shown how the brain actually operates and shows each and every single thing... upon clicking, it zooms up on the screen to show this detail — only for about 5 seconds."* Everything on this page exists in service of that image: a brain you can watch think, and beneath the spectacle, an honest record of what it actually learned, organized so nothing gets lost and nothing gets counted as real until it's actually complete.
## Mode one: the graph
Every journal entry the brain has ever produced becomes one node — colored by the kind of thing it is: a warm green for a test success, a controlled red for a failure, a gold for an evergreen concept the desk keeps coming back to, a cool blue for pure research. Edges connect an entry to whatever it caused or was caused by — a test failure connects to the critic review that predicted the weakness, a promotion connects forward to the paper trades it authorized. Drag to pan, scroll to zoom, double-click to reset the view back to its resting frame. Hovering an edge lights up both nodes it touches and surfaces the actual relationship in a small label — "leads to," "causes" — so the graph never asks you to guess why two things are connected.
A floating, semi-transparent sidebar — reached by an arrow at the edge of the screen, exactly the same interaction pattern used on Bots-Hub, because two floating sidebars that behave differently would be a small betrayal of trust — holds the page's four view tabs (Graph, Journal, Research, Test Viz) along with a short stat line: total nodes, total connections, time since the last entry landed. The sidebar never blocks the graph; it floats over the void like a HUD, and toggling it away leaves nothing but the constellation itself.
## Mode two: the journal
The left panel is a folder hierarchy built on PARA — Projects, Areas, Resources, Archives — with a fifth branch underneath specifically for Templates: Test Success, Test Failure, Ingestion, Paper Trading, Evergreen, MOC, each one expandable to show which entries were actually written against it. Click a folder and the right panel filters to show only what lives there. A "+ New entry" control at the bottom of the left panel opens a template picker rather than a blank page — every entry on this desk starts life as one of the named templates, never as freeform prose with no shape.
The right panel is a read-only feed, deliberately — Anant was explicit about this during planning: *"None of my edits reflect on the right — I just make them."* This is a passive activity stream, not a workspace; it shows what already exists and already passed muster, pinned entries first, then everything else newest-first, each card carrying its template-colored badge, title, date, tags, and a two-line excerpt that expands inline on click to the entry's full content and frontmatter.
A search bar spans the top of the whole journal view — genuinely smart, matching against tags, dates, and content all at once, real-time, the same instant-filter feeling as Watchlist's search box but reaching into far more text.
## The completeness gate, made visible
An entry doesn't earn its place in the feed for free. Each template carries its own required fields — a Test Success entry needs a spec name, confirmation all gates passed, and a demo-eligibility flag; a Test Failure entry needs the failed gate and a real, non-empty reason — and the system checks those fields automatically, the same way the rest of this desk automatically checks data quality before letting a number reach a screen. While an entry is being written, an expandable legend sits right there on the form: a small checklist of what this template actually requires, checkmarks filling in live as fields get completed, the submit button staying disabled until the required set is whole. An entry that's saved incomplete doesn't vanish — it sits in its folder, visibly marked as a draft, filterable via a "show drafts" toggle, honest about its own unfinished state rather than either hiding entirely or pretending to be done.
## Color, motion, and the royal-blue instrumentation, specifically here
This is the one page on the whole desk where royal blue gets to be genuinely beautiful rather than purely structural — the graph's ambient glow, the faint trailing light along an edge as it highlights, the ring that blooms around a node the instant it's clicked, all rendered in shades of the same royal blue that anchors the rest of the desk, so that even at its most cinematic this page never stops looking like it belongs to the same instrument panel as Dashboard and Watchlist. The journal side of the page, by contrast, deliberately calms back down — folders and cards in the same graphite-on-void language as everywhere else, template badges carrying the only real color, because a filing system dressed up like a light show would undermine its own credibility.
## How it behaves
The graph is static between sessions — new nodes appear when new entries are created, not on any timer, because a brain's memory doesn't need to pulse every few seconds to feel alive; it needs to actually grow when something real happens. The journal feed is similarly non-refreshing by default, with a manual refresh available for catching entries created elsewhere (say, from the Bots-Hub sidebar's own logging). Everything else — search, folder filtering, template filtering — is instant and client-side.
## What it's built on
Graph nodes and journal entries are the same underlying `JournalEntry` and `Citation` records the brain writes throughout its own operation — a test passing writes an entry here, a lesson learned from a closed paper position writes an entry here, a promotion decision writes an entry here. This page doesn't invent content; it's the one place all of that content finally becomes visible and navigable as a single connected body of knowledge, mirroring the same vault the rest of Anant's actual notes live in, one-way, database wins on any conflict.
## When things aren't perfect
No entries exist yet: the graph shows a quiet invitation rather than an empty void — "No entries yet. Create your first journal entry to start building the brain" — and the journal side offers the same, pointed straight at "create first entry." An entry links to something that no longer exists: the graph still shows the node, but the edge toward the missing target grays out and carries a plain question mark, with a warning surfaced on the entry itself rather than a silently broken connection. A search that matches nothing: "No entries found for '[term]'. Clear search."
## What's deferred to production
The true cinematic version of this page — a real 3D graph, camera flying toward a clicked node rather than a flat card appearing beside it, genuine depth and parallax as you pan — is explicitly a production-phase build, not part of the prototype. The prototype's job is to prove the *interaction shape* (click, brief detail, return) in an honest 2D network first; the spectacle comes once the shape is proven right.
## Open threads for the build phase
Whether pinned entries should visually distinguish themselves in the graph too (a slightly larger node, a steady glow instead of the resting dim state) so pinning has a consequence beyond just the journal feed. Whether the Research and Test Viz sidebar tabs need their own full write-ups before build, given they were named in passing during planning ("there is going to be a research page, a test visualisation phase... and something more maybe") without ever being fully specified — this is a genuine gap worth closing before Claude Code starts building against this page.

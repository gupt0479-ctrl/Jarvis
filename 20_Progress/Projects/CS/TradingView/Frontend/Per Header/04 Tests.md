---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/03 My Stocks]]"
  - "[[Per Header/05 Strategies]]"
tags:
  - trading
  - frontend
  - ui
  - tests
track:
  - trading
  - ui
next: "Read Per Header/05 Strategies.md next"
---
# Tests
==Every idea this desk has ever tested is written down here, forever, in the order it actually happened — the passes and the failures side by side, because a failure recorded honestly is worth more than a pass nobody can verify.==
## The first look
Tests opens on a filter bar — status, gate, symbol, date range — sitting above a long table that scrolls back through every backtest the desk has ever run, most recent first, twenty-five rows at a time. Passing rows carry the faintest wash of green behind their status badge; failing rows the faintest wash of red — not loud, not alarm-toned, just enough tint to let the eye sort pass from fail while scanning without reading a single word. Click any row and it opens downward, right where it sits, into the full gate-by-gate account of what actually happened.
## What this page is for
This is the desk's memory for a very specific kind of truth: *did this idea survive contact with history, and exactly where did it stop surviving if it didn't.* Nothing here is provisional or editable — a test run, once complete, is a historical fact, written once and never touched again. The page exists so that "we tried this before and it failed at Monte Carlo" is never a half-remembered feeling; it's a row you can click open six months later and see the exact 5th-percentile return that killed it.
## The anatomy
**The table** carries six columns — Date, Spec, Symbol, Status, Gate, Decision — compact enough that a week of testing activity fits on one screen without scrolling. Status is a clean pass or fail badge. Gate names which of the four gates actually stopped a failing run (blank, correctly, for anything that passed all four). Decision shows PROMOTED, REJECTED, or a plain dash for anything still awaiting a human call.
**The expanded row** is where the real density lives. Four gate panels, Out-of-Sample through Deflated Sharpe, each one showing its key numbers directly against the threshold that mattered — "OOS Net Sharpe: 0.72 (threshold: >0.5× in-sample)" — so a failure never reads as a bare X, it reads as a specific number that came up short against a specific bar. A gate that never ran because an earlier gate already failed shows plainly as `NOT_RUN`, not blank, not hidden — the fixed OOS→MC→WF→DSR order is a structural fact of this desk, and the UI should make that order visible even in failure. Below the four gates, an overall verdict banner — "ALL 4 GATES PASSED" or "FAILED AT GATE 2" — and beneath that, the linked journal entry this test run produced (a real excerpt, not a placeholder) and, if a human has already weighed in, the promotion or demotion decision with its reasoning and timestamp.
## Color, motion, and the royal-blue instrumentation, specifically here
Royal blue appears only as structural chrome — filter focus rings, the expand affordance, a link's underline color — because this page's entire job is to let pass/fail and gate-specific green/red carry the visual weight without competition. Nothing here animates beyond the row's own open/close transition, a simple, quick slide that never overstays its welcome. A test log that tried to look exciting would be lying about what it is: a ledger, not a highlight reel.
## How it behaves
Filters apply instantly and can stack — status and gate and symbol and date range together, narrowing the same twenty-five-per-page table in real time. Only one row expands at a time by default, so opening a second collapses the first — this keeps the page from becoming an accordion of half-remembered open panels, though an "expand all" affordance is a reasonable future addition once someone actually wants to compare several runs at once. New test runs don't magically appear mid-session — this is an append-only log, not a live feed, and a manual refresh is the honest way to see what's landed since the page loaded.
## What it's built on
Every row is one complete run of a `StrategySpec` through all four gates, exactly matching the brain's own `PromotionDecision` and journal records — this page is, in effect, a direct window onto the gate harness's own output tables, formatted for a human to actually read rather than grep.
## When things aren't perfect
No tests have run yet: the page says so plainly, "No test runs yet. Trigger a backtest from Bots-Hub to start," rather than showing an empty table pretending to be a feature. A test with no promotion decision yet: the panel reads "Pending human review," with a direct link into Strategies to go make that call. A failed test with genuinely sparse logging (an edge case that shouldn't happen, but the UI should survive it gracefully): the gate panel shows what it has and a small honest note pointing at Bots-Hub's logs for anything the structured record didn't capture.
## What's deferred to production
Re-running a test directly from this page. That trigger lives in Bots-Hub by design — Tests stays strictly read-only, a ledger rather than a control panel, and a fresh run always appends a new row rather than mutating an old one.
## Open threads for the build phase
Whether very old test runs (a threshold to be decided — six months felt reasonable in early planning) should archive out of the default view with a link to reveal them, once the log genuinely accumulates enough history that scrolling becomes the bottleneck rather than reading.

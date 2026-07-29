---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/04 Tests]]"
  - "[[Per Header/06 Brain-Journal]]"
tags:
  - trading
  - frontend
  - ui
  - strategies
track:
  - trading
  - ui
next: "Read Per Header/06 Brain-Journal.md next"
---
# Strategies
==A small, deliberately limited stage — never more than five specs at once, usually just two live and a couple of challengers arguing for their place — because a desk that lets strategies multiply without limit stops being able to actually know any of them well.==
## The first look
Strategies opens on a grid, never crowded, because it structurally can't be — a hard cap of five specs means this page will never scroll past a screen and a half. Each spec is a card: name, a status badge in a color that tells its whole story at a glance (amber for Proposed, blue for Approved, green with a checkmark for Promoted, red with an X for Demoted), creation date, current paper portfolio value against VOO, the outcome of its most recent gate run, and a small row of buttons that change depending on exactly where in its life this spec currently sits.
## What this page is for
This is the roster page — the small set of ideas the desk currently trusts enough to be running paper money against, or is actively arguing about whether it should. Anant's own framing during planning drew the boundary precisely: *"We are not planning on adding more than 5 strategies. We will mainly only be using 2 with one of them as backup. The rest two strategies are going to [be] ingested or suggested strategies that are being compared to the strategies currently used and fighting for their place."* The page is built around that exact shape — a primary, a backup, and up to two challengers actively contesting the incumbents, not an open-ended strategy library.
## The anatomy
**The grid** is the default view, filterable by status (All, Proposed, Approved, Promoted, Demoted) with Approved-and-Promoted showing by default, since those are the specs actually doing something today. Every card shows its four-gate result as a compact strip — pass marks or a clear indication of where it stopped — so you never have to click through just to see whether a challenger is even still alive.
**The per-strategy detail view**, reached by clicking a card's "View," is where a single spec gets the full room. A back arrow returns to the grid. Context-sensitive action buttons sit right under the header — Approve and Reject for something Proposed, Promote and Reject for something Approved, Demote alone for something already Promoted, nothing at all (rightly) for something already Demoted — because a button that can't legally do anything shouldn't be sitting there tempting a click. Below that, a portfolio chart in the same clean style as My Stocks' Position tab — price-equivalent value over time, entry and exit markers, no technical overlays, because this chart's job is honesty about performance, not analysis. Portfolio stats follow: total return, the outperformance-versus-VOO number specifically called out (never buried in a generic "return" figure), max drawdown, win rate, Sharpe. Then the latest test's gate results, compact, with a link into the full Tests row. Then the strategy's actual mechanics laid bare — universe, rebalance frequency, holding count, every parameter that defines what this spec actually does, because "why does this strategy hold what it holds" should never require reading source code to answer.
**The Compare view**, reached by toggling away from Grid, replaces the card layout with a single table — checkboxes at the top to choose which specs to line up, then rows for every metric worth comparing side by side: status, demo-eligibility, Sharpe, OOS Sharpe specifically, max drawdown, win rate, paper return, outperformance versus VOO, last test date, and a running tally of tests passed against tests attempted. This is where "which one is truly better" — Anant's own phrase for what this page needs to let the brain and the human decide together — actually gets decided, side by side, with nothing hidden in a separate tab.
## Color, motion, and the royal-blue instrumentation, specifically here
Status badges carry the only strong color on the grid — the cards themselves stay graphite-on-void like everywhere else, so five cards read as five distinct decisions rather than five identical containers. Royal blue marks the Approved status specifically (a deliberate choice — Approved is the "waiting on the brain, not waiting on you" state, and giving it the structural brand color rather than a semantic one underlines that it's a process state, not a verdict). The Compare table highlights the best value per metric with a subtle royal-blue-tinted cell background rather than bold text or an icon — quiet enough not to turn the comparison into a scoreboard, present enough to save a second of mental arithmetic.
## How it behaves
Grid and Compare are a simple toggle, no page reload, state preserved if you flip back and forth while deciding which specs to line up. Compare's checkbox selection updates the table live as you check and uncheck specs — there's no separate "apply" step, because a comparison you have to submit before seeing feels like friction on a page whose entire purpose is fast side-by-side thinking.
## What it's built on
Every card and every detail view reads directly from a real `StrategySpec` — its parameters, its citation history, its complete gate record (not just the latest run), and every `PromotionDecision` ever made on it, in order. The five-spec cap isn't a UI decoration; it reflects the actual discipline the brain's own citation-and-promotion loop is designed around.
## When things aren't perfect
No specs exist yet: the grid says so plainly and points at where new ones actually get proposed — Brain-Journal or Bots-Hub, not this page, since Strategies displays and decides, it doesn't originate ideas. A spec with no paper trades yet: portfolio value reads "Not yet trading" rather than a bare zero that could be mistaken for a loss. A spec proposed but not yet reviewed: only Approve and Reject are live; Promote and Demote simply don't exist yet for that card, because they're not real options until Approved happens first.
## What's deferred to production
Editing a spec's parameters directly from this page — the prototype shows the parameters, honestly, but doesn't pretend to let you change them; that's a real backend mutation, not a UI-only feature, and it waits for the production build. CSV export from the Compare table.
## Open threads for the build phase
Whether the five-spec cap should show visibly on the grid itself ("3 of 5 slots used") so the limit feels like a designed constraint rather than something you discover by trying to add a sixth. Whether the detailed decision log — every promote/demote/reject ever made on a spec, not just the latest — deserves its own expandable section on the detail view or a dedicated link out, given Anant's explicit preference that per-strategy logs stay light while the *full* decision trail lives somewhere separately detailed.

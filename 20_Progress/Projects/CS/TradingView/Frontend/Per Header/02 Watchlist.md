---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/01 Dashboard]]"
  - "[[Per Header/03 My Stocks]]"
tags:
  - trading
  - frontend
  - ui
  - watchlist
track:
  - trading
  - ui
next: "Read Per Header/03 My Stocks.md next — every row here leads there"
---
# Watchlist
==Fourteen symbols, the whole universe the brain is allowed to think about, laid bare in one table — nothing hidden, nothing paginated away, nothing more than one click from full research.==
## The first look
Where Dashboard is curated, Watchlist is complete. The page opens on a single search box sitting quietly under the page title, and beneath it, one long table — fourteen rows, no more, because the universe genuinely doesn't have a fifteenth symbol until real evidence earns one. The starred symbol sits at the top with its small filled star, the rest fall away by confidence, and the whole table reads like a manifest — every name accounted for, nothing left off the list because it wasn't interesting enough that day.
## What this page is for
This is the page for the question "what does the brain think about everything, not just the six things it decided to show me." It exists specifically because Dashboard's curation is a feature, not a complete picture — someone using only Dashboard could go weeks without ever seeing what the brain thinks of, say, COST or BRK.B, and Watchlist is the guarantee that nothing in the universe is actually hidden, only de-prioritized.
## The anatomy
**The search box** sits alone at the top, full width on mobile, comfortably narrow on desktop, placeholder text reading simply "Search by symbol or company." It filters in real time, case-insensitive, matching against both the ticker and the company name — type "micro" and Microsoft surfaces even though you never typed a letter of "MSFT."
**The table** carries seven columns: a star toggle, Symbol, Company, Action, Confidence, Data Quality, Last Reviewed. The star column is interactive everywhere else on this page is read-only — click it, and that symbol becomes the one pinned atom on Dashboard's Today's Trades, immediately, no confirmation needed, no save button. Action renders as a small solid badge in the action-vocabulary palette — WATCH gray, HOLD blue, ACCUMULATE green, REDUCE amber, AVOID red, INSUFFICIENT_DATA a dashed gray outline that visibly reads as *absence* rather than *opinion*. Data Quality carries its own smaller badge, the same green-to-red logic, independent of the action badge, because a stock can be a confident ACCUMULATE built on rock-solid data or a shaky one built on partial data, and those are two very different things to know at a glance.
**Every row is a door.** Click anywhere on it — not just the symbol — and the same medium `SymbolModal` from Dashboard rises over the page: action, confidence, a one-line summary pulled straight from that symbol's Evidence Card, the top two or three factor ranks, and the "View Full Analysis" button that walks straight into My Stocks' Research tab for that exact symbol. This is deliberate consistency, not laziness — one modal, one behavior, used everywhere a symbol can be previewed, so the desk never has to teach a second interaction pattern for the same fundamental action.
## Color, motion, and the royal-blue instrumentation, specifically here
The table itself stays almost entirely monochrome — graphite rows on the void hull, silver text — so that the action and quality badges are the only saturated color on the page and can't help but draw the eye first. Royal blue shows up exactly twice here: the active search box's focus ring, and a faint left-edge glow on whichever row the mouse currently rests over, just enough to say "this is the row you'd click" without turning the whole table into a light show. Nothing on this page pulses or breathes — Watchlist is a reference surface, not a live feed, and its stillness is the point.
## How it behaves
Default sort is fixed and non-negotiable: starred symbol first, then confidence descending, with symbol name as the tiebreaker when two rows land on the exact same confidence, so the order never visibly shuffles for no reason between refreshes. Sorting by clicking a column header is a real feature worth having eventually, but it isn't required for the row to already tell its whole story — everything you'd want to sort by is already visible without a click. The page refreshes its data on a five-minute cycle, same as Dashboard, and search is purely client-side, instant, with zero network round-trip, because filtering fourteen rows should never feel like it's waiting on anything.
## What it's built on
Every row is one symbol's latest `EvidenceCard` and its accompanying data-quality read, pulled from the exact same source Dashboard's mini-widget and My Stocks' Research tab read from — this is the same data at three different zoom levels, never three different versions of the truth.
## When things aren't perfect
A search with no matches doesn't just show a blank table — it says plainly, "No symbols found for '[term]'," with a one-click way to clear the search and see all fourteen again. A symbol the brain genuinely can't say anything useful about shows `INSUFFICIENT_DATA` in the action column and a flat `0.0` confidence rather than a stale or fabricated number — honesty about not knowing is itself information worth displaying clearly, not something to paper over.
## What's deferred to production
Column-header sorting beyond the fixed default order. Multi-symbol comparison directly from this table (that lives, if it ever exists, inside Strategies' Compare view, not here).
## Open threads for the build phase
Whether the Data Quality badge deserves a hover tooltip explaining *why* a symbol is STALE or PARTIAL (probably yes — a badge that raises a question it can't answer on hover is a small trust leak). Whether the search box should also match on factor descriptions ("momentum," "quality") for a more research-flavored search, or stay strictly symbol/company for simplicity.

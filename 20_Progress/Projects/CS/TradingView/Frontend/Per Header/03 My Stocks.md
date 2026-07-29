---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Per Header/02 Watchlist]]"
  - "[[Per Header/04 Tests]]"
  - "[[Per Header/05 Strategies]]"
tags:
  - trading
  - frontend
  - ui
  - my-stocks
track:
  - trading
  - ui
next: "Read Per Header/04 Tests.md next"
---
# My Stocks
==Every road on this desk ends here. This is where the brain's opinion and the brain's actual track record sit in the same room, one tab apart, so that learning to trade means watching both at once — not choosing between them.==
## The first look
My Stocks is the hub — the single page every deep link on the entire desk eventually points to, and it looks the part. A slim, semi-transparent sidebar hugs the left edge, a search box at its top and the full fourteen-symbol list beneath it, favorites pulled into their own small section above the rest. Whichever symbol is currently open sits highlighted in royal blue against the sidebar's graphite. The main pane takes the rest of the screen: a breadcrumb-style header naming the symbol and its full company name, a star to toggle favorite status, and two tabs — **Position** and **Research** — sitting side by side like two different instruments reading the same underlying reality.
If a decision is pending on this symbol, nothing about the page lets you forget it: a banner spans the top of the main pane, amber-toned against the void, carrying the exact entry logic and a live countdown — "Entry pending: NVDA, Monday 9:30 AM ET — 2 days 4 hours away" — and one button, "View thesis details," that jumps straight to the reasoning behind it. This banner is not dismissible. It doesn't hide when you scroll. It is the one place on the desk where the interface is allowed to insist.
## What this page is for
This is where "why did the brain think that" and "what actually happened" get to sit next to each other instead of living in two different apps. Position is the honest ledger — what was bought, what was sold, what it's worth right now, always measured against VOO so there's no way to quietly forget the benchmark. Research is the case file — the same evidence, factor scores, critic pushback, and gate history a symbol carried the moment the brain formed its opinion. Anant's own framing during planning was direct: *"This should be synced with the brain extremely because that's the knowledge we are implementing and going to learn from it. This is the main learning process. We learn by testing."* My Stocks is that learning process made visible.
## The sidebar
Search filters the fourteen symbols in real time, same behavior as Watchlist's search box. Above the full list, a small "Favorites" accordion holds whichever symbols have been starred — expanded by default, collapsible if it ever feels crowded. Click any symbol anywhere in the sidebar and the main pane swaps instantly, the URL updates to name that symbol, and the newly active row lights up in the same royal blue used for active nav state elsewhere on the desk — the sidebar and the header nav should feel like the same language, because structurally they're doing the same job at two different scales.
## Tab one: Position
This tab tells the truth about money, and nothing else. A clean price chart — no moving averages, no RSI, no Bollinger bands, none of the analytical apparatus Research carries — because the question this chart answers is simply "what happened," not "what should I think." Green triangles mark every entry, red triangles mark every exit, hoverable to reveal the exact date, price, and share count behind each one. Below the chart, current price and today's percent move sit in bold monospace, and beneath that, two tables: open positions first, each row showing entry date, entry price, shares, current value, and P&L; closed positions collapsed by default under a "show more history" toggle, because the open positions are the ones that matter today and the closed ones are reference material, not the headline. A small stats line closes the tab — average entry price, win rate, total P&L across every trade ever made in this symbol — the kind of summary that turns a wall of individual trades into a single sentence about whether this symbol has actually been good to Anant or not.
## Tab two: Research
This tab tells the truth about reasoning. The same price series renders again, but this time carrying the full technical apparatus — MA20, MA50, MA200, RSI-14 in its own subplot, Bollinger bands shaded around the price line, ATR tracked separately — because Research exists to answer "what should I think," and the technical context is part of that case, even though (per the brain's own rules) it never gets to drive an action on its own.
Below the chart, four stacked panels build the full case in the order a careful reader would want it:
- **The Evidence Card** — action, capped confidence, the strategy spec this reading came from, whether it's demo-eligible, a plain-language summary, then collapsible sections for supporting evidence, risks, and the exact invalidation conditions that would prove the thesis wrong. This card is the single most important piece of prose on the entire desk, and it's styled accordingly — the most legible surface on the page, generous line height, nothing crowding it.
- **The Critic Review**, directly beneath, deliberately smaller and quieter — a lighter background, a step down in visual weight — because the Critic's job is annotation, not a second equal opinion. It shows the Analyst's original confidence, the Critic's adjustment (which can only ever be negative or zero), the final number, whatever the Critic suggests instead, and the human decision that actually got recorded, with a timestamp proving a real person looked at this and chose.
- **The Gate Panel** — four boxes, Out-of-Sample, Monte Carlo, Walk-Forward, Deflated Sharpe, left to right, each carrying a clean pass or fail mark and, on expand, the two or three numbers that actually decided it against the threshold that mattered. A link out to the full row on Tests sits at the bottom for anyone who wants the complete diagnostic.
- **Data Quality**, the smallest panel, closing the tab with three or four short lines — price, fundamentals, technical indicators — each graded on the same quality ladder used everywhere else on the desk, so the reader's very last impression before leaving the page is an honest account of how much to trust everything they just read above it.
## Color, motion, and the royal-blue instrumentation, specifically here
The pending banner is the one piece of amber allowed real visual weight on this page — everything else uses royal blue for structure (the active sidebar row, the active tab underline, focus rings) and the action palette only where an actual action or quality value is being reported. The Critic Review panel's muted background is a deliberate, small act of color-as-hierarchy: it should read, before you've consciously registered why, as *quieter than the thing above it*. "Last updated" timestamps sit in the same muted blue-gray used everywhere on the desk for metadata, refreshing on their own five-to-fifteen-minute cycle with a small manual refresh icon beside them that never pretends to be faster than the underlying data actually is.
## How it behaves
Switching symbols in the sidebar never triggers a full page reload — it's a swap, instant, the URL updating underneath it for shareability and back-button sanity, but nothing about the experience should feel like leaving and re-arriving. Switching between Position and Research is the same instant swap. The pending banner, if present, persists across both tabs without re-rendering awkwardly between them — it's structurally part of the page header, not part of either tab's content.
## What it's built on
Position reads directly from the paper engine's `Thesis` records — every entry, every exit, every P&L figure reported against `voo_return_same_period`, the field the backend requires on every exit specifically so nobody can quietly stop comparing against the benchmark. Research reads the same `ScorePacket`, `EvidenceCard`, `CriticReview`, and gate results that feed the Evidence modal everywhere else on the desk — there is exactly one version of "what the brain thinks about NVDA," and this page is simply where its fullest form lives.
## When things aren't perfect
No open positions on a symbol yet: Position says so directly — "No open positions. Ready to enter based on research" — and points at Research rather than showing an empty chart apologizing for itself. Evidence gone stale past a day: the card itself carries a small note, "Evidence stale (analyzed 48h ago)," with a "re-analyze now" link into Bots-Hub rather than silently presenting old thinking as current. Data genuinely missing: action reads `INSUFFICIENT_DATA`, confidence reads `0.0`, and if a pending banner would have shown, it instead reads "Cannot show pending decision — insufficient data," because a confident-looking banner built on nothing would be a worse failure than an honest gap.
## What's deferred to production
Nothing about the two-tab structure, the sidebar, or the pending banner is descoped — this page is the hub precisely because it has to work fully from the first prototype. The one thing genuinely deferred is any notion of comparing two symbols side by side inside My Stocks itself; that instinct, if it's ever needed, belongs to Strategies' Compare view instead, which already exists for exactly that job.
## Open threads for the build phase
Whether "View thesis details" from the pending banner should open a modal or navigate into Brain-Journal directly to the relevant entry — both are defensible, and it's worth deciding once the journal's own navigation patterns are settled. Whether the closed-positions table needs its own filter (by date range, by win/loss) once a symbol accumulates real trading history, or whether "show more" pagination is enough for a desk with only fourteen symbols and a young track record.

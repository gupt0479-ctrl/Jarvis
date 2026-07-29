---
type: project
status: active
created: 2026-07-29
updated: 2026-07-29
related_progress:
  - "[[Background — The Vision Behind the Desk]]"
  - "[[UI MOC — The Complete Dream]]"
  - "[[Animation and Transitions]]"
  - "[[Charts and Data Visualization]]"
tags:
  - trading
  - frontend
  - ui
  - effects
track:
  - trading
  - ui
next: "Attach alongside the 8 page notes when briefing the coded build"
---
# Micro-interactions and UI Effects
==The small, repeated moments — a badge, a hover, a status dot — are what a desk you sit in front of for years actually feels like day to day, far more than any single dramatic page ever will.==
## Badges as a single, consistent object
Every badge on the desk — action (WATCH/HOLD/ACCUMULATE/REDUCE/AVOID/INSUFFICIENT_DATA), data quality (USABLE/PARTIAL/STALE/MISSING/CONTRADICTORY), strategy status (Proposed/Approved/Promoted/Demoted), pending-decision markers — should render from one shared component with a color prop, never as one-off styled elements per page. This isn't just a build-efficiency note: a user's eye learns a badge shape once and then trusts it everywhere, and a desk with three subtly different-looking "badge" treatments across its eight pages quietly erodes that trust every time.
## Status dots
The small colored dot pattern already present in the existing basic build's top strip (green/amber/red dots next to "usable / partial / stale / missing" counts) is worth keeping as the desk's standard for any compact health indicator — provider status on Dashboard and Bots-Hub, data quality inline in tables, agent state in the swarm view. A dot, not a badge, when space is tight and the surrounding text already carries the label; a full badge when the color needs to stand alone.
## The confidence bar with a ceiling tick
The existing basic build's MSFT page already does this exactly right: a horizontal bar filled to the actual confidence value, with a small separate tick mark at the data-quality ceiling and a caption underneath ("Max confidence allowed by data quality: 94%"). This single component is the clearest possible visual proof of the desk's most important rule — confidence can never exceed what the data actually supports — and it should be treated as a locked, reusable pattern, not redesigned from scratch on other pages that need to show a capped number.
## Hover reveals versus click reveals
A consistent rule worth holding across every page: hover shows *more information about what's already visible* (a tooltip naming an exact timestamp, a row highlighting to show it's clickable), while click shows *new content that wasn't there before* (a modal, an expanded row, a detail popup). Nothing on the desk should require a click just to see a tooltip, and nothing should fully reveal itself on hover alone if it's information dense enough to need a deliberate look — that boundary keeps touch devices (where hover doesn't really exist) from silently losing information sighted-mouse users would get for free.
## Empty and loading states have their own voice
An empty state is never a blank card — it's a short, plain sentence in the desk's own voice ("No open positions. Ready to enter based on research," "No entries yet. Create your first journal entry to start building the brain") paired with a single clear next action where one exists. A loading state is a quiet skeleton shape in the same graphite tone as a populated card, never a spinner floating in empty space — the skeleton's job is to promise "this exact shape of content is coming," which is a small honesty the desk's whole design language already insists on everywhere else.
## Focus and keyboard rings
Every interactive element gets a visible royal-blue focus ring on keyboard navigation, thicker and more saturated than the ambient hover glow, because this is the one piece of motion/color language that exists purely for accessibility rather than aesthetics, and it should never be sacrificed for visual quietness. Tab order follows reading order on every page — top to bottom, left to right — described explicitly in each page's own note.
## Toasts and confirmations
When a trigger fires from Bots-Hub (an ingest, an analysis run, a gate test), the feedback is a small, brief toast in the bottom corner — action confirmed, no modal, no page interruption — because these are routine operational actions, not consequential ones, and treating them as anything heavier would make the genuinely consequential actions (a spec approval, a promotion) feel less distinct by comparison. A gate-test or full-ingest trigger, which takes real time, gets a lightweight confirm dialog first (described in each relevant page's own note) — but even that confirm should read plainly, stating the real time estimate, never dramatizing a routine action into something that sounds risky.
## The one effect the desk earns the right to be a little playful about
Anant's own words on error handling during planning: *"Anything that doesn't work will have a pop up saying that this did not work, skill issue."* This is the single place on the entire desk where the tone is allowed to be genuinely light — a small, honest, slightly funny toast on a failed no-op action in the prototype, rather than a stern error banner. It fits because it's low-stakes by construction (nothing in the prototype can actually break anything real), and it's a nice, deliberate crack in an otherwise serious interface — exactly one crack, not a pattern to repeat everywhere.
## MVP scope for the static, coded prototype
Badges, status dots, the confidence-ceiling bar, and empty-state copy are cheap and high-value — build these for real from the start, since they're the components every other page leans on. Toasts and confirm dialogs are worth a simple, real implementation too (a basic toast library, a plain confirm modal) since Bots-Hub's whole point is showing these triggers exist. Skeleton loading states can be skipped entirely for the first static pass — a prototype built on hardcoded mock data never actually has a loading moment to show one during.

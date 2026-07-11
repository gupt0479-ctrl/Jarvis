---
type: concept
status: sprout
created: 2026-06-13
updated: 2026-06-13
tags:
  - portfolio
  - frontend
  - layout
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[BUILD-STATUS]]"
---
# Global Fixes — Header & Section Spacing
> Cross-cutting fixes that touch **every** section. Do these first in the refinement pass — they're cheap and they change how every other screenshot reads. Sourced from the user's two top-priority items (header + the "blank box after every section") plus the live DOM in the dev-tools screenshot.

## 1. The dark-mode pill must be STATIC in the header
The "Dark" pill currently **drifts/wobbles** in the header — `useSpaceFloat` (or an equivalent continuous-drift) was applied to it. A control in a fixed header must not wander; it reads as broken.
- **Remove `useSpaceFloat` / any continuous drift from the theme pill** in `HeaderScrolling.tsx`. It stays put.
- Keep the Phase-2 semantic fix ([[13 - Dark Mode Toggle]]): it's a `<button>` with `useTheme()`, a no-op `onClick`, aria-label, `cursor-default`. A `float-btn`-style *hover lift* is fine; **continuous idle motion is not.**
- While here: confirm no other header element (logo, nav links) has drift applied. The header is the one zone that stays still.

## 2. Kill the "blank box" / extra padding after every section
The DOM shows each section as `<section class="section-backdrop py-16 px-6">` (About), `py-18` (Experience), `py-24` (Projects) — **inconsistent vertical padding** — and `section-backdrop` paints a `::before` pseudo-element. The user sees a tall empty block + uneven gaps between sections.

Two things to fix, both in `src/app/globals.css` + the section wrappers:
- **The `.section-backdrop::before`** is almost certainly the culprit "blank box": a pseudo-element with its own height/min-height/large vertical padding or margin that injects dead space at the end of each section. Audit it — if it's a decorative backdrop it should be `position:absolute; inset:0; z-index:-1; pointer-events:none` and add **zero** layout height. It must not occupy flow space. Remove any `min-height`, top/bottom `margin`, or block sizing on it that creates the gap.
- **Unify section vertical padding.** Sections currently use ad-hoc `py-16 / py-18 / py-24`. Replace with ONE token/value so spacing between every section is uniform. Define a single `--section-pad-y` (or a shared `.section` utility / a `<Section>` wrapper) and apply it to every section wrapper. Pick one rhythm (e.g. `py-20` / ~5rem) and use it everywhere.

### Acceptance
- No empty block appears between any two sections.
- The vertical gap between every consecutive section is identical (one token), top to bottom of the page.
- `prefers-reduced-motion` and the existing scroll-backdrop visual are preserved — only the dead layout space is removed.

## 3. The Achievements exception (subsection of Certifications)
Achievements is a **subsection under Certifications**, not a top-level nav section (correctly absent from the header). It must NOT get the full uniform section padding:
- **Minimal top gap** between the Certifications section and Achievements — they read as one block. Use a much smaller top padding than `--section-pad-y` (e.g. a fraction of it).
- **Smaller header** for Achievements: reduce the h2 font-size and the kicker/description scale relative to a top-level section heading. Still centered, just visibly a sub-heading.
- Remove the same `section-backdrop::before` dead space here too.
- (Visual rebuild of the Achievements cards/rail is in [[07 - Certifications & Achievements]].)

## Order
Do this note's three fixes as the **first refinement phase** (call it Phase R0) before the per-section refinements — uniform spacing + a still header make every later visual change easier to judge.

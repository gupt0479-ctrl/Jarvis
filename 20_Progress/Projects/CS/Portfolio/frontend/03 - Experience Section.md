---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - frontend
  - experience
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[BUILD-STATUS]]"
---
# Experience Section
> **Refinement pass (2026-06-13).** The section is built and rendering from Sanity. Files: `sections/ExperienceSection.tsx`, `cards/ExperienceCard.tsx` (`CometCard variant="dark"`, `getCategoryColor()`, `CATEGORY_COLORS`, `EMPLOYMENT_LABELS`). Kicker `// trajectory`, header already centered. This note is now the **fix list**, not a rebuild.

## Fixes (from BUILD-STATUS UI Fixes #1–2)
1. **Move the employment-type chip to the location row.** It **currently renders next to the position title** (the "Contract" pill beside "Research Assistant") — move it so it sits **beside the location** (the MapPin row, next to "Minneapolis, MN, USA"). Same `EMPLOYMENT_LABELS` + chip styling, just relocated. The title row keeps only the title; the type chip lives with the location.
2. **Recolour achievements off gold/green.** The achievement `★` lines currently render in **yellow/gold** (confirmed in the live screenshot) — a hardcoded-looking status colour. Change to a **theme tone — blue/violet/cyan** drawn from the design tokens, matching the card. They must read as part of the card, not a traffic-light status.
3. **Description only on click + subtle "more" affordance.** The Portable Text `description` currently renders **always-open** below the chips — it must be **hidden by default** and revealed on click. Put a **very subtle "more" toggle at the bottom-right** of each card (low-opacity, gains presence on card hover; accessible name). Clicking the card OR the toggle opens a **small** dropdown with the description — it must **not** take the full screen. Compact, single-open, no sibling layout shift; the card keeps its gentle drift while open.
4. **Dial the comet DOWN.** The card tilts/moves too much on hover. Reduce `CometCard` tilt depth (e.g. lower `rotateDepth`/`translateDepth`, or use a gentler variant). Keep the hover feel, just less swing.
5. **Per-skill dot colour from Sanity.** The dot next to each skill chip must come from the new `skill.color` field ([[02 - Sanity as Single Source of Truth]]), not a hardcode and not only the category colour. Everything on the card stays Sanity-rendered. Fall back to category colour when `color` unset.

## Already correct — do NOT redo
- Header centered; logo, position, company link, location, date range, `responsibilities[]` (≤3), `technologies[]` chips (≤4) all render.
- The Portable Text `description` IS fetched — the only missing piece was rendering it (fix #3).
- `useSpaceFloat`/rail breathing from the motion pass — keep if applied; just ensure the card drift is subtle and hover doesn't add a big jump.

## Done conditions
- Type chip beside location; achievements in a blue/violet/cyan theme tone; description hidden until click via a subtle bottom-right "more"; small dropdown, no full-screen; comet swing reduced; skill dots use `skill.color` from Sanity.

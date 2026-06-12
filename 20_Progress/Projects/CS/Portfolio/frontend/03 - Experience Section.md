---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - experience
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[02 - Sanity as Single Source of Truth]]"
---
# Experience Section
Files: `ExperienceSection.tsx`, `ExperienceCard.tsx`, plus the shared `SpaceRail` and `CometCard` from [[01 - Motion System & Comet Cards]]. Kicker: `// trajectory`.

## The timeline rail (brief item 1)
Replace the patchy, static, hard-transition rail with the shared `SpaceRail`:
- One smooth vertical gradient stroke — no segmented glow, no abrupt on/off.
- Dot nodes aligned to each card's title row, each with an even, soft glow.
- A scroll-progress fill travels the rail as the section scrolls.
- The rail **breathes in space**: a slow sine on the path so it wiggles slightly, eye-pleasing while scrolling. Dots stay pinned to their cards.

## The cards (brief items 2, 6)
Use `CometCard` with **reduced tilt** (large card) + a small `useSpaceFloat`. The card must **not** occupy the full screen and must **not** drop on hover.

Layout / content, all from Sanity ([[02 - Sanity as Single Source of Truth]]):
- **Employment-type chip** (`contract`, `internship`, `freelance`, …) renders **next to the location**, not floating by the title. Style it as a small muted pill matching the theme.
- **Description** (long-form, from Sanity) is currently not rendered — wire it up, but it is **hidden by default** and revealed only on click (see drop-down below).
- **Achievements**: kill the green. Recolour to the site theme — use the card's accent / a muted success tone derived from the theme tokens, not raw green. They read as a subtle highlighted line, not a neon block.
- **Skill chips**: the shared `<SkillChip>` rendering only `color` + `name` from the `skill` references. Uniform with the rest of the site.

## The click-to-expand drop-down (brief item 2)
This is the signature interaction for the card.
- A **very subtle** toggle affordance at the **bottom-right** of each card — almost invisible until hovered (a small chevron that gains opacity/glow on card hover). Accessible name required ("Show details").
- Click expands a **small** drop-down inside the card showing the Sanity `description` (and any extra detail). It is compact — not a full-screen takeover.
- Expansion animates height without shifting siblings (reserve space / grid-rows trick from [[01 - Motion System & Comet Cards]]). The card keeps drifting while expanded.
- Collapsed by default; one card's expansion does not collapse others (or does — pick single-open for tidiness; single-open recommended).

## Done conditions
- Rail is smooth, glows evenly, has scroll fill, and breathes.
- Employment-type sits beside location; description renders only on click; achievements match theme; chips are uniform Sanity chips.
- Drop-down toggle is bottom-right, subtle, keyboard-operable; expansion is compact and shift-free.
- Nothing hardcoded; every field traces to Sanity.

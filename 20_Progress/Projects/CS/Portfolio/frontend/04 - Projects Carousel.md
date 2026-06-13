---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - frontend
  - projects
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[09 - Sanity Content Spec]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[BUILD-STATUS]]"
---
# Projects Carousel
> **Refinement pass (2026-06-13).** Built and rendering. **Correction to earlier notes: the carousel is now R3F, not Framer Motion.** Per the graphify map, `three/ProjectsSlider.tsx` is a 3D carousel inside an R3F `<Canvas>`, using **`Float` from `@react-three/drei`** for the gentle drift and **`@react-spring/web` elastic spring** for card physics. Header lives in `PortfolioContent.tsx`. The fixes below apply to that R3F implementation.

## Fixes (from BUILD-STATUS UI Fixes #3–4)
1. **Dial the centre-card comet DOWN.** The centre project's comet/tilt is too strong. Keep the same hover *intent* but reduce the magnitude (lower tilt + lighter `Float` amplitude). 
2. **Bound the drift to the card's padding.** The `Float` wander must stay within the card's own area — reduce `floatIntensity`/`rotationIntensity`/`speed` and the position range so it never drifts into neighbours.
3. **Side cards independent of the centre's hover.** Right now hovering the centre card makes the left/right cards move down with it. The side cards must be **decoupled from the centre hover** — they keep their own gentle `Float` wander and their current translucent opacity, unaffected by what the centre does. Comet only when a side card becomes the centre (already correct).
4. **Remove the "case note" box.** Show **only the project `summary`** in that inner box — nothing else. Keep the truncation (the summary cut-off is good; it got too long otherwise). Apply to every project uniformly.
5. **Cap skills at 4.** Render **no more than 4** `technologies[]` chips per project. Dots use `skill.color` ([[02 - Sanity as Single Source of Truth]]).
6. **Schema (Phase 0, [[09 - Sanity Content Spec]]):** `coverImage` is now **optional** (remove required); the `visibility` enum is **removed** (use `featured` + `order`). `summary` is the hover field; `githubUrl` is the source link; hide View-Live when `liveUrl` empty.

## Already correct — do NOT redo / keep as-is
- 3-card R3F carousel renders; nav works; centre card prominent, side cards translucent and dimmed.
- Side cards stay at their current opacity while wandering (correct).
- Side cards get comet only when centred (correct).
- `useIridescentEffect` shimmer on the View-Live pill — keep.
- Header centering (if already centered in the screenshots, leave it; the brief's centre requirement is satisfied).

## Done conditions
- Centre comet reduced and `Float` bounded to padding; side cards keep wandering and are **not** dragged by the centre's hover; case-note box gone (summary only, truncated); ≤4 skill chips with Sanity-coloured dots; `coverImage` optional; `visibility` removed.

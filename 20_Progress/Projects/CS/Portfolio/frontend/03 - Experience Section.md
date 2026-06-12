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
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Experience Section
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]].** Files: `src/components/sections/ExperienceSection.tsx`, `src/components/cards/ExperienceCard.tsx`. Kicker `// trajectory`.

## Corrections from note 10 (what the first draft got wrong)
- **Header is already `text-center`.** No change needed. (First draft said left-aligned — wrong.)
- **employmentType chip already renders** as an orbit-chip; location already renders with a MapPin icon. Keep.
- **`responsibilities[]` (≤3, prefixed `→`) and `achievements[]` (≤2, ★) already render.** Tech chips (`technologies[]`→skill refs, ≤4) already colour per category via `getCategoryColor()` — **this is the uniform colour system; keep it.**
- Card already uses `CometCard variant="dark"` with `rotateDepth={3} translateDepth={5}` and a hover sweeping-light effect.

## The one real content gap
**The Portable Text `description` is fetched by `EXPERIENCE_QUERY` but never rendered by `ExperienceCard.tsx`.** There is no `<PortableText>` in the card. This is the primary fix.

## What to actually build
1. **Render the description behind a click-to-expand drop-down.** Add a `<PortableText>` block (use `@portabletext/react`) that is collapsed by default and revealed by a **very subtle toggle at the bottom-right** of the card (a small chevron that gains opacity/glow on card hover; accessible name "Show details"). Expansion is compact — not full-screen — and animates height without shifting siblings (reserve space / grid-rows). Single-open across cards is cleaner. Card keeps drifting while expanded.
2. **Recolour achievements off green.** They're currently emerald `★` lines, which read as cheap. Map them to the theme accent / a muted highlight token from `globals.css`, not raw green.
3. **Motion polish (from [[01 - Motion System & Comet Cards]]):** add a small `useSpaceFloat` to each card (it already has CometCard tilt — compose float on the outer wrapper, tilt inner). Make the timeline rail breathe: the rail is currently static gradient `divs` with violet box-shadow dots — give it a slow sine wiggle and a scroll-progress fill so it's eye-pleasing while scrolling, dots staying pinned to card title rows. (Reuse the rail approach noted for Achievements in [[07 - Certifications & Achievements]] so both sections share one rail treatment.)
4. **No hover-drop.** Cards already drift; hover changes tilt/glow only, never position.

## Done conditions
- Portable Text `description` renders via a subtle bottom-right expand toggle, compact, shift-free, keyboard-operable.
- Achievements recoloured to theme (no green); chips stay category-coloured (already uniform).
- Cards float + comet (no hover-drop); rail breathes with scroll fill; header untouched (already centered).

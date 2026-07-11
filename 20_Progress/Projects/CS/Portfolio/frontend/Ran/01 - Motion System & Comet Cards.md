---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - motion
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Motion System & Comet Cards
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]].** `CometCard` already exists at `src/components/ui/comet-card.tsx` with **4 variants** — `default`, `dark`, `subtle`, `ghost` (the `ghost` variant was added on the `Chatbot` branch: no background class, no card shadow, tilt capped at 6°). So the only genuinely-new primitive to build is **`useSpaceFloat`**; `CometCard` is *standardise + reuse* (already applied across Experience/Certs/Achievements), and `SpaceRail` is *extract the existing Experience rail treatment so Achievements can share it*.

This is the **build-first** note. Almost every visual ask in the brief — "appears to be in space," "wiggles in its own padding," "comet-card effect," "lifts at the bottom on hover" — resolves to two reusable primitives plus one timeline component. Build these, get them feeling right once, then every section consumes them. Do not re-implement floating/tilt per section; that is how nine slightly-different janky animations happen.

## Primitive 1 — `useSpaceFloat` (the drift)
A hook that gives an element continuous, gentle, *bounded* zero-gravity drift inside its own padding box. This is the "floating in space, no gravity, wiggles in its own area" behaviour.

- **Motion:** sum of 2–3 low-frequency sines on translateX/translateY plus a tiny rotate, with per-instance random phase so no two cards drift in sync. Periods in the 4–9s range. Amplitude is a prop (`radius`), defaulting small (≈6–10px) and clamped so the element never leaves its padding.
- **Implementation:** drive with `requestAnimationFrame` and write to a CSS variable / transform, or use Framer Motion's `animate` with `repeat: Infinity, repeatType: "mirror"`. Prefer transform-only (GPU) — never animate layout properties.
- **Props:** `radius` (drift px), `rotate` (deg, default ~0.6), `speed`, `disabled`. Hover does **not** stop the drift — the card keeps wandering while expanded (explicit requirement for the Projects side cards and Blog cards).
- **Reduced motion:** if `prefers-reduced-motion`, the hook returns a static transform. One check, here, covers the whole site.

## Primitive 2 — `CometCard` (the hover surface)
A wrapper that gives a card the premium pointer-tracking tilt + light-sweep + glow that the brief keeps calling "comet card." **It already exists** at `src/components/ui/comet-card.tsx` with 4 variants (`default`, `dark`, `subtle`, `ghost`) and props `rotateDepth`/`translateDepth`. Do not rebuild it — reuse it as the single hover surface and only extend if a section needs a tilt it can't express.

- **Variants in use:** Experience/Certifications use `variant="dark"`; Achievements uses `variant="subtle"`. Use `ghost` for chip-level surfaces that shouldn't carry a card background.
- **Tilt:** pointer position → rotateX/rotateY, tuned via `rotateDepth`/`translateDepth`. **Reduce depth for large cards** (Experience `rotateDepth=3 translateDepth=5` is the existing baseline); fuller tilt for small chips/buttons.
- **Sheen:** a radial highlight that follows the cursor across the surface; a soft border glow on hover.
- **No vertical jump:** the old behaviour where "all cards move down on hover" is removed. Cards must not translate on hover now that they are already drifting — hover changes tilt/glow/elevation-shadow only, never position. (Brief item 7/Hover.)
- **Composition:** `CometCard` and `useSpaceFloat` compose — the float owns the base transform, the comet tilt is applied on an inner layer so the two transforms don't fight. Decide one ownership rule (float on outer wrapper, tilt on inner content) and keep it consistent.

### Where each applies (from the brief)
| Surface | `useSpaceFloat` | `CometCard` | Notes |
|---|---|---|---|
| Experience cards | yes (small radius) | yes (reduced tilt) | drop-down expands in place |
| Projects centre card | yes (in padding) | yes (reduced tilt) | only the centre card gets comet |
| Projects side cards | yes | **no comet until centred** | stay translucent, keep drifting on hover |
| Skills **category** buttons | yes | yes | the only skills elements that float+comet |
| Skills individual chips | no | no (own effects instead) | see the 7 effects in [[05 - Skills Capability Graph]] |
| Education shapes + cards | yes | yes | float together with the blob |
| Certification cards | optional small | yes | compact |
| Blog GitHub card | yes (wobble) | yes (bottom-lift) | keep the liked bottom-lift |
| Blog small resource cards | yes | yes | + more translucent bg |
| Contact card | subtle | yes | "frame not fill," see [[08 - Blog, Contact & Footer]] |
| Back-to-top button | no | yes | centred |

## Primitive 3 — the timeline rail (`SpaceRail`)
Used by Experience and reused by Achievements (the brief explicitly says Achievements' line should be "exactly like the experience section timeline," moved outside the box). One component, two mounts.

- **The problem today:** the rail glows in patches with hard, ugly transitions, and it is dead-static.
- **Fix:** render the rail as an SVG path with a single smooth vertical gradient (no segmented glow). Dot nodes sit at card-title centres, each with a soft, *even* glow. A scroll-progress fill travels the rail as the user scrolls the section.
- **In space:** apply a very small `useSpaceFloat` to the rail path control points (or a slow sine on the path's horizontal offset) so it breathes/wiggles slightly while scrolling — eye-pleasing, not distracting. Dots stay pinned to their cards even as the line breathes.

## Global guardrails
- **Transform-only animation.** No animating `top/left/width/height`. Everything is `transform`/`opacity` to avoid layout thrash on a heavy three.js page.
- **One rAF budget.** Many drifting elements = many rAF loops. Prefer a single shared ticker that updates all floaters, or Framer Motion's batched scheduler. Watch for jank against the existing background sphere.
- **`prefers-reduced-motion`** handled in the primitives only.
- **No layout shift on hover** (brief, accessibility section) — hover never changes box size for collapsed cards; expansion is an explicit click, and expansion animates height with `transform: scaleY`/grid-rows, reserving space so siblings don't jump.
- **Accessible names** on every interactive control (carousel arrows, drop-down toggles, category buttons, back-to-top). Keyboard operable.

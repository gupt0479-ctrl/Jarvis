---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, projects, gsap]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
---

# UI Fix 04 — Projects Section (Pinned Cinematic Lock)

> **Status:** open (carousel exists and is more capable than previously documented; no pin/emerge/edge effect)
> **Ledger:** [[UI Fixes]] §3 | **Tasks:** 4.1, 4.2
> **2026-09-05 correction pass:** re-verified line-by-line against `ProjectsSlider.tsx` (491 lines) and `PortfolioContent.tsx` on `post-frontend`. Several claims below were wrong or incomplete — corrected. Same correction applied to [[frontend-ui-fixes-design]] Fix 6 and [[frontend-ui-fixes-tasks]] Phase 4.

## Purpose

Projects becomes a **pinned cinematic beat**: cards **emerge from translucent space** into solid cards once when the section is scrolled into view, soothing **edge/border animation** during auto-scroll, and side-card drift — **without breaking the carousel's existing drag/keyboard/auto-play/chat-nav behavior**, all of which is more built-out than this note previously said.

## Current code (re-verified 2026-09-05)

| File | What exists today |
|---|---|
| `src/components/three/ProjectsSlider.tsx` (491 lines) | Full carousel: prev/next buttons, dot pagination, keyboard arrows, GSAP `Draggable`+`InertiaPlugin` swipe gesture, auto-play, ambient float on all three visible cards, `CometCard` tilt on the center card, chat-nav slug jump. |
| Section wrapper | `<section id="projects">` (kicker + `SplitHeading` + description) lives directly in `PortfolioContent.tsx` — **there is no separate `ProjectsSection.tsx` file.** `ProjectsSlider.tsx` renders its own nested `<section aria-label="Projects carousel">` inside that. Pin the outer `#projects` section. |
| Auto-play (~line 277–284) | `setInterval` every `AUTO_PLAY_INTERVAL_MS` (5000ms) advances `(prev + 1) % safeProjects.length`. **This cycles through every project, not just indices 0–2** — the "auto-play first 3 only" claim in the old note and in [[frontend-ui-fixes-requirements]] does not match the code. Pauses on any interaction via `pauseAutoPlay()` for `AUTO_PLAY_RESUME_DELAY_MS` (10000ms). |
| Slide transition (`slideVariants`, ~line 170) | Drives **every** index change — manual, drag, keyboard, and auto-play alike — via `AnimatePresence`: real ±200px horizontal `x` translate + opacity + scale (spring, stiffness 300 / damping 30). There is currently no separate "emerge-only" path distinct from this. |
| Side cards | Not just static/faded: `opacity-35 scale-[0.88] blur-[1px] pointer-events-none`, each individually wrapped in `useSpaceFloat({radius: 4, rotate: 0.3})` (`src/hooks/use-space-float.ts`) for ambient drift. **Drift already exists today** — the old note's "no side-card oscillation" gap claim is wrong. It's just not the specific "±8–12px, active only during auto-play, pauses on interaction" spec — it's always-on regardless of auto-play state. |
| Center card | `useSpaceFloat({radius: 2, rotate: 0.1})` + `CometCard rotateDepth={3} translateDepth={5}`. |
| Drag gesture (previously undocumented) | `Draggable.create` + `InertiaPlugin` on a wrapper ref: swipe past a distance/velocity threshold advances/retreats with an exit-then-snap animation; below threshold, elastic snap-back. Every advance (manual, drag, or auto-play) also fires a one-shot "tether flash" — a gradient line + `tether-flash` CSS keyframe — via `tetherActive` state. **This entire system must survive the pin/emerge work untouched.** |
| GSAP plugins registered in this file | `useGSAP`, `Draggable`, `InertiaPlugin` only. **`ScrollTrigger` is not registered here** — needs adding (it ships inside the already-installed `gsap` package, `gsap/ScrollTrigger` — not a new dependency). |
| `src/lib/gsap/projects-pin.ts` | Confirmed does not exist — genuinely new file, no naming collision. |
| Edge/border pulse CSS | Confirmed absent from `globals.css` (grepped for `edge-glow`, `edge-pulse`, `.edge-*`, `projects-edge` — nothing) — genuinely new work. |

## Target behavior

### 1. ScrollTrigger pin
- Pin `#projects` (the `PortfolioContent.tsx` section, not `ProjectsSlider.tsx`'s inner section) for ~1 viewport on entry, `scrub: 1`.
- Import `ScrollTrigger` from `gsap/ScrollTrigger` and register it — it isn't registered anywhere in this file yet.
- Unpin resumes normal scroll; carousel (drag/keyboard/auto-play/chat-nav) keeps working exactly as it does today, before and after the pin.

### 2. Card emerge — a ONE-TIME reveal, separate from the existing slide transition
The existing `slideVariants` opacity/scale shape (0→1 opacity, 0.92→1 scale) already looks like "emerge" — but it fires on every index change via `AnimatePresence`, which the pin-entry reveal must NOT hijack or duplicate. Build the pin-entry emerge as its own one-time animation on the three cards' **outer wrappers** (the `useSpaceFloat`-floated divs, not the inner `AnimatePresence`/`slideVariants` layer), gated to fire once per pin-entry:

| Property | From → To |
|---|---|
| opacity | 0 → 1 (center first, ~0.2 progress into the pin) |
| scale | 0.92 → 1 |
| filter | blur(8px) → blur(0) |
| horizontal position | unchanged — no added translateX |

- Side cards: opacity ramps from 0 to their existing resting `0.35`, not to 1 — don't change their resting opacity.
- After the emerge completes, existing carousel interactions (drag/keyboard/dots/auto-play) resume completely unchanged, including their own `slideVariants` transitions.

### 3. Edge / border background effect
- During auto-play, after the pin (progress past ~0.5, or simply "always while pinned and auto-playing" — your call): recurring gradient pulse on the section's screen periphery.
- New CSS on `globals.css` or a scoped `<style>` — violet/indigo ~15% opacity, 4–6s loop. No existing class to conflict with.
- Optional stretch: dispatch a `background:mode: projects-edge` CustomEvent for R3F ring sync — out of scope unless trivial; the hero-background note ([[ui-fix-01-hero-background]]) explicitly defers building the consumer side of this event.

### 4. Side card ambient drift — extend, don't duplicate
`useSpaceFloat` already drives side-card transforms. **Read `src/hooks/use-space-float.ts` before adding anything** — if it writes a CSS transform on the same element you'd target with a second Framer `repeat: Infinity` animation, the two will fight over the same `transform` property and one will silently win each render. Prefer: tune `useSpaceFloat`'s existing `radius`/`rotate` params (or add an optional bounded-mode param to the hook) over layering a second independent animation system on the same div.
- If a genuinely separate "auto-play-only, pauses on interaction" behavior is wanted (distinct from the always-on ambient float), gate it through `autoPlayPaused` (already tracked in `ProjectsSlider.tsx` state) rather than inventing new pause-tracking.

##### 5. Auto-play scope — RESOLVED 2026-09-05: keep current behavior

User confirmed: **keep cycling through all projects** (the live behavior). The "0–2 only" language in [[frontend-ui-fixes-requirements]] Fix Area 6 is stale — do not implement a cap. No code change is needed for the auto-play index range itself; this section is closed.

### 6. Document × card effects (brainstorm — pick 1–2, unchanged from before, still just a brainstorm)

| Option | Description |
|---|---|
| Edge chroma (recommended) | Border glow color shifts per project's Sanity accent |
| Tech tag pulse | Stack pills illuminate in sequence with active index |
| Live preview strip | Active project description scrolls in card border |
| Background constellation | R3F stars connect to project category |

## Files to modify

| File | Action |
|---|---|
| `src/lib/gsap/projects-pin.ts` | NEW — pin + one-time emerge timeline, registers `ScrollTrigger` |
| `src/components/three/ProjectsSlider.tsx` | Wire pin-entry emerge on outer card wrappers; do not touch `slideVariants`, `Draggable`/`InertiaPlugin` setup, or `tetherActive` logic |
| `src/components/PortfolioContent.tsx` | Pin trigger ref/id on the existing `#projects` section (no new wrapper component needed) |
| `src/hooks/use-space-float.ts` | Read first; extend only if needed for bounded auto-play drift |
| `globals.css` | New edge-pulse keyframes (no existing class to collide with) |

## Do NOT

- Do not modify `slideVariants`, its spring config, or how `AnimatePresence` drives per-index transitions.
- Do not touch the `Draggable`/`InertiaPlugin` setup, drag thresholds, or the `tetherActive`/tether-flash effect.
- Do not remove or fight `useSpaceFloat` on the center or side cards — extend it, don't shadow it with a second transform system on the same element.
- Do not cap or otherwise change auto-play's index range — confirmed to keep cycling all projects (§5, resolved).
- Do not add a new animation dependency — `ScrollTrigger` ships inside the already-installed `gsap` package.
- Do not touch `orby:navigate` chat-nav slug handling.

## Visual reference

- Projects screenshot: Resq center, side projects faded, position indicator dots below.
- Orby bubble text bottom-aligned — separate issue, Contact section, out of scope here.

## Accessibility

- WCAG 2.2.2: auto-play already pauses on interaction (`pauseAutoPlay`) — pin/emerge must not regress this.
- Existing `aria-label`s on nav buttons and `aria-current` on dots — preserve exactly.
- `prefers-reduced-motion` is already read into local state (`prefersReducedMotion`) and gates both auto-play and the Draggable setup — new pin/emerge/edge-pulse code must check the same flag, not add a second detection mechanism.

## Acceptance criteria

- [ ] Section pins on scroll entry
- [ ] Cards emerge once on pin-entry without disturbing per-index slide transitions
- [ ] Edge effect loops during auto-play
- [ ] Auto-play still cycles through all projects (confirmed, unchanged) — side-card drift stays always-on as it is today
- [ ] Drag-to-swipe, keyboard arrows, dot nav, and chat-nav slug jump all still work exactly as before
- [ ] `prefers-reduced-motion`: no pin animation, no edge pulse, existing static/no-autoplay fallback unchanged
- [ ] `pnpm typecheck && pnpm lint` pass

## Implementation prompt

> Written for a single autonomous coding session (Claude Sonnet 5 in Cursor). Read this whole file before editing anything — it corrects a prior version of this note that misdescribed current auto-play scope and missed the drag gesture, tether-flash effect, and existing ambient drift entirely.

```
Read ui-fix-04-projects-section.md in full first. It was rewritten 2026-09-05 after re-verifying against the live repo; a prior version of this note wrongly claimed auto-play was limited to indices 0-2 (it actually cycles through every project) and didn't mention the existing GSAP Draggable swipe gesture, the "tether flash" effect, or the useSpaceFloat ambient drift already on all three visible cards. Do not trust summaries of this task from anywhere else.

AUTO-PLAY SCOPE IS RESOLVED (confirmed by the user 2026-09-05): keep cycling through all projects — this is the current, correct behavior. Do not cap it to the first 3. No code change is needed for the auto-play index range itself.

TASK — implement exactly this, nothing else:

1. Create src/lib/gsap/projects-pin.ts: import ScrollTrigger from "gsap/ScrollTrigger" and register it (it's part of the already-installed gsap package — do not add a new dependency). Pin the #projects section (defined in PortfolioContent.tsx, not ProjectsSlider.tsx's own inner <section>) for ~1 viewport with scrub: 1.

2. Wire a ONE-TIME emerge animation that fires on pin-entry, on the three cards' OUTER wrapper divs (the ones already wrapped by useSpaceFloat in ProjectsSlider.tsx) — NOT by touching slideVariants or the AnimatePresence block, which must keep working exactly as today for every subsequent index change (manual, drag, keyboard, auto-play). Emerge: opacity 0→1 (center first), scale 0.92→1, blur(8px)→blur(0), no horizontal translate. Side cards animate opacity 0 → their existing resting 0.35, not to 1.

3. Add a new CSS edge-pulse effect (globals.css or a scoped style) — violet/indigo gradient pulse on the section's screen periphery, 4-6s loop, ~15% opacity, active during auto-play. No existing class to reuse or collide with — confirmed absent from globals.css.

4. Read src/hooks/use-space-float.ts before touching side-card drift. It already drives always-on ambient drift on both side cards regardless of auto-play state — that matches the resolved "keep all projects cycling" scope, so no gating change is required here. Only touch this hook if you need to tune radius/rotate for the emerge transition to look right, or if the emerge animation's opacity/scale conflicts with the transform it writes (see constraints below) — do not add a second independent Framer Motion repeat:Infinity transform animation on the same element it targets.

CONSTRAINTS:
- Do not modify slideVariants, its spring config (stiffness 300 / damping 30), or how AnimatePresence drives index-change transitions.
- Do not touch the Draggable/InertiaPlugin setup (drag bounds, thresholds, snap-back/exit animations) or the tetherActive "tether flash" effect — verify by manual swipe test after your changes that this still works identically.
- Do not cap or otherwise change auto-play's index range.
- Do not touch orby:navigate chat-nav slug handling.
- Respect prefers-reduced-motion exactly via the existing prefersReducedMotion state — do not add a second media-query check.

VERIFY before reporting done, and state the result of each explicitly:
(a) Scrolling into #projects pins it and the three cards visibly emerge once, without a horizontal slide.
(b) After the emerge, clicking prev/next still slides with the original x-translate spring animation.
(c) Drag-to-swipe left and right still works, including the tether-flash line on advance.
(d) Auto-play still advances through all projects at the same interval and still pauses on interaction for the same 10s.
(e) Keyboard arrows and dot-pagination nav both still work.
(f) Chat-nav (orby:navigate) slug jump still works.
(g) prefers-reduced-motion: no pin animation, no edge pulse.
Run pnpm typecheck && pnpm lint and paste the output. Do not deploy, do not commit.
```

## Dependencies

- Task 3.0 GSAP research (reuse ScrollTrigger patterns from About, once that exists)
- Optional: [[ui-fix-01-hero-background]]'s deferred `background:mode` event, if projects-edge R3F sync is attempted

## Risks

- Emerge animation and the existing `AnimatePresence`/`slideVariants` transition both touching opacity/scale on nested elements — keep them on clearly separate DOM layers (outer wrapper vs. inner `motion.div`) so they don't fight.
- A second transform-writing system layered onto `useSpaceFloat`'s target element will visibly stutter or freeze drift — read the hook first (see §4 above).
- Pin duration vs. carousel height on mobile — carousel side cards are already `hidden md:block`, so mobile only ever shows the center card; account for that when sizing the pin.

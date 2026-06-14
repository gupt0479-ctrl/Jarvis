---
type: concept
status: active
created: 2026-06-14
updated: 2026-06-14
tags:
  - portfolio
  - frontend
  - prompt
  - orby
  - codebase-audit
notes:
  - "[[BUILD-STATUS]]"
  - "[[12 - Orby Friction Fixes]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Orby Enhancement + Codebase Audit

> Claude Code prompt for Orby visual fixes and a structural audit of globals.css, layout.tsx files, and Clerk usage. Run in one session. Start at repo root. Run `pnpm typecheck` before closing.

---

## Context you must read first

Before touching anything, read these files in full:
- `src/components/orby/Orby.tsx` — the RAF loop, position logic, state transitions, `OrbyArrow` usage, portfolio button
- `src/components/orby/OrbyArrow.tsx` — how the arrow is rendered and positioned
- `src/components/orby/OrbyCanvas.tsx` — **read for context only. Do not touch this file. The 3D model is out of scope.**
- `src/components/orby/OrbySpeechCloud.tsx` — how speech text is rendered
- `src/components/orby/useOrbyState.ts` — the 11-state machine, scroll thresholds, section comment triggers
- `src/app/globals.css` — the full file
- `src/app/layout.tsx`, `src/app/(portfolio)/layout.tsx`, `src/app/studio/layout.tsx` — all three layout files

Do not redesign Orby's persona, 3D model, or chat-navigation pipeline. Only the specific fixes listed below.

---

## Part A — Globals.css Audit (answer these questions, then act)

### Step 1: Audit and answer

Read `src/app/globals.css` in full. Then produce a written audit that answers:

1. **Which CSS blocks are dead/unused?** List any animation keyframes, class definitions, or CSS variables that are not referenced anywhere in the `src/` directory. Use `grep -r` to verify each suspected dead block. Do not guess — verify every deletion candidate.

2. **Which effects are duplicated?** List any keyframe animations or utility classes that do the same thing under different names.

3. **Are all the `@keyframes` used?** For every `@keyframes` block, find at least one component or class in `src/` that uses it. If none: mark it as dead.

4. **The `.section-backdrop::before` pseudo-element** — does it inject layout height (any `height`, `min-height`, `padding-top`, `padding-bottom`, `margin-top`, `margin-bottom` that is not zero)? If yes, this is the cause of blank boxes between sections. Note exactly what it sets.

### Step 2: Remove only what is verified dead

After the audit:
- Delete only the CSS blocks that `grep` confirms have zero references across `src/`.
- Do not consolidate or refactor working code — only remove confirmed dead code.
- Leave a one-line comment above any block you keep that was borderline: `/* used by: ComponentName */`.

### Step 3: Report on layout.tsx files

The project has (at minimum) three layout files:
- `src/app/layout.tsx` — root layout (providers, fonts, global CSS import)
- `src/app/(portfolio)/layout.tsx` — portfolio route group layout
- `src/app/studio/layout.tsx` — Sanity Studio layout

All three are legitimate and needed. Confirm this by reading each one. Note what each does. If any layout file is empty or only re-exports children with no added providers/wrappers, flag it as a candidate for deletion. Do not delete without confirming.

---

## Part B — Clerk Audit (understand and clarify, then act if needed)

### What to find

1. **Search for all Clerk imports across `src/`:** `grep -r "from '@clerk" src/` and `grep -r "ClerkProvider\|SignIn\|SignedIn\|SignedOut\|useAuth\|useUser\|currentUser\|auth()" src/`.

2. **Map where Clerk is used.** Expected finding: Clerk is only in `src/app/studio/layout.tsx` (wrapping Sanity Studio) and possibly `src/middleware.ts`. It should NOT appear in any portfolio-facing page or component.

3. **Confirm the intended use:** Clerk protects the `/studio` route so only authorized users (Anant) can access the Sanity CMS. The portfolio itself (`/`, `/about`, etc.) does not use Clerk auth. This is the correct setup.

4. **If Clerk appears in portfolio-facing code** (hero, sections, pages, actions that aren't studio-related): flag it as incorrect and remove it.

5. **If `src/middleware.ts` exists**: read it. It should only protect `/studio(.*)` routes. If it is protecting the whole app, narrow the matcher to `/studio(.*)` only and report what you changed.

### What to report

Produce a brief written summary:
- Where Clerk is used (file paths)
- Whether the setup is correct (studio-only protection = correct)
- What you changed, if anything

Do not add Clerk to any new routes. Do not remove Clerk from the studio layout.

---

## Part C — Orby Visual Fixes

### Fix C1 — Orby's hand wave animation

**Problem:** The wave animation (Orby waving hello/goodbye) does not look clean. The wave function applied to the arm/hand is either too mechanical, has the wrong easing, or uses a sine that makes the motion feel robotic.

**What to do:**

1. **In `OrbyCanvas.tsx`** (read only — do not restructure the file): find the bone or mesh that controls the arm/hand wave. Note the variable name, what drives it (sine of time, animation mixer, or manual transform).

2. **In `Orby.tsx`**: find where the wave state is triggered (intro, goodbye, or similar states) and how it passes to `OrbyCanvas`.

3. **The wave fix targets `OrbyCanvas.tsx`** even though it is "out of scope" for UI fixes in general — the hand is an exception because the wave is broken visually. Apply a smoother easing to the arm rotation:
   - Replace any `Math.sin(t * speed)` pure sine with a damped or eased wave. Use `Math.sin(t * 2.5) * Math.exp(-t * 0.3)` to produce a decaying wave (energetic start, settles naturally). Reset `t` at the start of each wave trigger.
   - If the wave is driven by a Mixamo/GLTF animation mixer: ensure the animation clip plays at `1.0` speed and is not looping incorrectly. If there is a clip called `wave` or `Wave`, play it with `clampWhenFinished: true`, `loop: THREE.LoopOnce`. Check that the mixer's `update(delta)` is called in the RAF loop.
   - If no wave animation clip exists and the arm is driven manually: implement the decaying sine above on the arm bone's `rotation.z`, resetting when the state exits wave.

4. **The wave should trigger in `intro` state** (when Orby first appears and points/greets) and in `goodbye/departingLeft` states. Confirm these state transitions correctly start and stop the wave.

### Fix C2 — Arrow hidden behind portfolio button; reposition arrow

**Problem:** `OrbyArrow` is rendering behind the portfolio lab toggle button instead of pointing at its boundary.

**What to do:**

1. **Read `OrbyArrow.tsx`**: understand how it positions itself (absolute vs fixed, z-index, offset from Orby's center).

2. **Find the portfolio lab toggle button** in `Orby.tsx` or wherever it lives. Note its size, position, and z-index.

3. **Raise `OrbyArrow`'s z-index** above the portfolio button. The button is likely `z-40` or `z-50` — the arrow should be at least one level above it, or at the same level with a proper stacking context.

4. **Point the arrow at the button's boundary (edge), not its center.** The arrow's target point should be the nearest edge of the portfolio button div, not its center coordinate. If the arrow currently points at the center of the button, offset the arrow tip by `(buttonWidth / 2)` or `(buttonHeight / 2)` in the correct direction so it lands on the perimeter.

5. **Test that the arrow is fully visible and not obscured** at 1280px and 1440px widths.

### Fix C3 — Portfolio button: slightly bigger, slightly up and left

**Problem:** The portfolio lab toggle button (the "beaker" or lab icon button near the bottom-right, or wherever it is) is too small and in a slightly wrong position.

**What to do:**

1. **Find the portfolio toggle button** in `Orby.tsx` (or in `PortfolioLab.tsx` / `src/app/(portfolio)/layout.tsx` — read to find it). It is likely the bottom-right trigger button that opens the Lab sidebar.

2. **Increase size slightly:** If it is `w-10 h-10` or `w-12 h-12`, make it `w-12 h-12` or `w-14 h-14` respectively. One step up only — "slightly" means one Tailwind size increment.

3. **Move it up and left slightly:** Reduce `bottom-*` by one step (e.g., `bottom-6` → `bottom-8`) and reduce `right-*` by one step (e.g., `right-6` → `right-8`). "Slightly" means one Tailwind step each direction.

4. **Do not change the button's icon, color, or behavior.**

### Fix C4 — New Orby message: "Click and hover everything, it all does something"

**Problem:** After the user passes the About Me section entirely and just before the Education section appears, Orby should pop up a new contextual message. This message should trigger once only, after the About section has been fully scrolled past.

**Message (exact text):** `"Click and hover everything you see — it all does something."`

**What to do:**

1. **Read `useOrbyState.ts`** to understand how `section-comment` states work and how scroll percentage thresholds fire speech events for the Projects, Blog, and Contact sections.

2. **Add a new scroll threshold** that fires between the About and Education sections. Find the approximate scroll percentage where the About section ends and the Education section begins. This will need to be estimated — use `~35%–40%` of total page scroll as a starting point and calibrate after testing. The exact value depends on section heights.

3. **Add the new state/speech trigger** in `useOrbyState.ts` following the same pattern as the existing `projects`, `blog`, and `contact` section comments:
   - Create a new trigger condition: when scroll passes the about→education threshold AND this message has not been shown yet in this session.
   - Fire the speech text: `"Click and hover everything you see — it all does something."`
   - Mark it as shown so it does not repeat if the user scrolls up and down.

4. **Wire it through the state machine** so Orby visually pops up (if not already visible) and displays the speech cloud. Follow the exact same pattern as the other `section-comment` implementations — do not invent a new state; reuse `section-comment` with the appropriate trigger.

5. **The trigger is one-time per page load**, not per scroll pass.

---

## Acceptance criteria for the full session

- `pnpm typecheck` passes with zero errors.
- Sidebar opens: background + all content compress left together, sphere visually centered in remaining space at 1280px and 1440px.
- Education → Certifications gap matches other inter-section gaps.
- Blog card Visit button is clickable without the card drifting away.
- Contact card responds only to hover with minimal tilt.
- Skill category buttons are clearly readable against the background.
- `globals.css` dead code is removed; report produced for the audit.
- Clerk is confirmed studio-only; no changes to portfolio-facing routes.
- layout.tsx count is confirmed correct (3 files, all needed).
- Orby wave looks natural (decaying oscillation, not a stiff sine).
- Arrow is visible above the portfolio button, pointing at its edge.
- Portfolio button is one step bigger and slightly higher-left.
- "Click and hover everything" message fires once after the About section.

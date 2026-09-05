---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, hero, background]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
---

# UI Fix 01 — Hero & Background Sphere

> **Status:** partial (scatter intro exists; click lacks perceptible depth; overlay gap needs repro)
> **Ledger:** [[UI Fixes]] §1 | **Task:** [[frontend-ui-fixes-tasks]] Phase 2 (2.1, 2.2)
> **2026-09-05 correction pass:** the "Current code" section below was re-verified line-by-line against `ObsidianBackgroundCanvas.tsx` on `post-frontend`. The previous version of this note referenced symbols (`handleClick`, `burstActive`, `scatterBurstActive`, `BURST_DURATION`, `burstScale`) that **do not exist in the file** — they described an earlier or imagined implementation. The mechanism below is the real one. Same correction applied to [[frontend-ui-fixes-design]] Fix 1 and [[frontend-ui-fixes-tasks]] Task 2.1.

## Purpose

First impression: static profile presence, full-bleed hover overlay, and a particle sphere whose click response **reads as volumetric** — not just IS volumetric in the underlying math — synced later with pinned About/Projects scroll moments.

## Current code (re-verified 2026-09-05)

| File | What exists today |
|---|---|
| `src/components/three/ObsidianBackgroundCanvas.tsx` (1196 lines) | Click → formation replay → `pScatter` regenerated via `randomOffsetInSphere` → fly-apart / reassemble. Full mechanism below. |
| `src/components/sections/ProfileImage.tsx` | Owns the Lab open/close hover overlay (`button.float-btn` → `Image fill` + `div.absolute.inset-0`). **Not** in `HeroContent.tsx` as previously noted. |
| `src/components/sections/HeroContent.tsx` (255 lines) | Profile `motion.div` entrance (opacity/scale, one-shot) at lines 223–250; comet sweep gradient overlay at lines 236–247 (`x: -120% → 120%`, `duration: 1.4`, no repeat — already one-shot, already correct). |
| `src/components/PortfolioContent.tsx` | HeroTerminal removed from tree (unchanged, verify still true) |

### Click mechanism, exactly as implemented

1. `window.addEventListener("click", onClick)` (line ~475) — deliberately **not** an R3F/DOM `onClick`, because `<main>` sits at `z-10` above the fixed canvas and would eat the event. It raycasts against an invisible hit-mesh (`sphereGeometry` radius `PLANET_RADIUS * 1.1`, line ~1052) whose *scale* is lerped at runtime between `HITBOX_SCALE_START` (1.0) and `HITBOX_SCALE_END` (1.35) by `stretchT` (scroll progress), so the clickable area keeps matching the sphere's apparent size as the camera moves in.
2. A hit sets `formRetrigger.current = true`; consumed once at the top of the next `useFrame` (line ~537).
3. That frame captures every point's **live current position** into `pFormOrigin` (not an assumed rest position — this is why re-clicking mid-animation never pops/teleports) and rolls a **fresh** `pScatter` offset per point via `randomOffsetInSphere(FORM_SCATTER_RADIUS)` (`FORM_SCATTER_RADIUS = 2`).
4. Fly-apart leg (`FORM_CLICK_OUT_DURATION = 0.9s`): lerp from `pFormOrigin` to `pPos0 + pScatter`.
5. Reassemble leg (`FORM_CLICK_IN_DURATION = 2.6s`): lerp back toward rest, blended with a shared radial "breathing" wiggle along each point's own surface normal (`pNorm`) so the whole sphere pulses together on settle.
6. This is the **exact same code path** as the one-time mount intro (`FORM_MOUNT_IN_DURATION = 7.0s`) — click just re-triggers it with shorter durations. There is no separate "burst" system.

### `randomOffsetInSphere` is already true 3D — confirmed

```ts
function randomOffsetInSphere(maxRadius: number): [number, number, number] {
  const u = Math.random();
  const v = Math.random();
  const theta = u * Math.PI * 2;
  const phi = Math.acos(2 * v - 1);
  const r = Math.cbrt(Math.random()) * maxRadius;
  return [r * Math.sin(phi) * Math.cos(theta), r * Math.sin(phi) * Math.sin(theta), r * Math.cos(phi)];
}
```

This is correct uniform sampling inside a sphere (spherical coords + cube-root radius) — **not** biased toward the XY plane, **not** a flat ripple. The camera is also a real perspective camera (`fov: 55`) on an angled, scroll-driven path (`CAM_START [3.5, 2.8, 5.2] → CAM_END [0.4, 0.2, 3.2]`, always `lookAt(0,0,0)`), and planet points already use `sizeAttenuation={true}` with additive blending. So the data and the camera are genuinely 3D.

### Real diagnosis: why it still *reads* as 2D

Given the above, the gap is **perceptual, not mathematical**. Three concrete, verifiable causes:

1. **No parallax during the click.** The camera only moves in response to scroll (`stretchT`/`smoothScroll`), never in response to a click. A completely static viewpoint removes the strongest depth cue humans have (motion parallax). The only depth signal left is `sizeAttenuation`'s size-by-distance falloff, which at this scale (points a few tenths of a unit apart, camera ~3–5 units away) is subtle enough to miss.
2. **No occlusion/depth stratification.** `depthWrite={false}` (needed for additive blending to look right) means points don't sort or occlude by depth — near and far points blend into one bright mass rather than reading as layered.
3. **Scatter direction is disconnected from the click location.** `pScatter` is a fresh independent random pick every time, unrelated to where on the sphere the raycast actually hit. It reads as "the whole sphere re-explodes" rather than "I poked it there and it rippled outward from that point" — the latter is what would make it feel like a solid 3D object responding to touch.

## Target behavior

### 1. Profile image — always static
- One-time entrance only (already correct — verify no regression): `opacity 0→1`, `scale 0.96→1`, then stop.
- Comet sweep: one-shot only (already correct — `HeroContent.tsx` lines 236–247, no `repeat`).

### 2. Hover overlay — full cover
- **File is `ProfileImage.tsx`, not `HeroContent.tsx`.** Structure today: `<button className="float-btn relative aspect-square w-full overflow-hidden rounded-2xl border border-white/10 ...">` wraps `<Image fill>` and `<div className="absolute inset-0 ...">`. This is already the textbook full-cover pattern (`inset-0` inside `relative overflow-hidden`) — nothing in the static markup obviously produces a left/bottom gap.
- **Do not guess-fix this.** Screenshot it first at the `lg:` breakpoint, hovered. If a gap is real, the two concrete suspects to check (in order): the button's `border border-white/10` reading as a visual inset against the image edge, and any rounding/subpixel effect from the `float-btn` class's `translateY` transform interacting with `overflow-hidden` clipping.

### 3. Sphere click — make the volumetric scatter *read* as volumetric

Two small, targeted changes, additive to the existing formation code — do not touch the mount-intro timing or durations:

- **(A) Depth-correlated brightness/size, beyond built-in `sizeAttenuation`.** During `formationActive`, compute each point's distance to `camera.position` and drive an explicit extra multiplier on that point's contribution to size/opacity — e.g. lerp between a "near" and "far" opacity/size band across the actual distance range points reach during this specific animation (not a generic global fog). This makes the depth gradient obvious instead of subtle, without disturbing the resting-state sphere's look.
- **(C) Bias scatter direction from the actual click point.** `onClick`'s raycast hit already returns `hit[0].point` (world-space hit location) — it's computed but currently discarded. Blend it into the `pScatter` roll for points near that hit location, so nearby points get an outward-from-hit-point bias on top of their random jitter, while distant points stay close to the current isotropic behavior. This makes the burst read as "I touched it there" rather than "everything re-explodes."
- Treat **(B) biasing the scatter offset itself toward/away from the camera-forward axis** (rather than the point-of-hit) as an optional stretch goal only if A+C together are not enough — it touches the shared mount+click code path and needs more care not to change the mount-intro's look.
- Reassemble physics, `pNorm` breathing wiggle, and both duration constants stay exactly as-is.

### 4. Background mode API (for About/Projects pins — later phase, do not build yet here)
- Listen for `background:mode` CustomEvent: `idle | click-scatter | about-pin | projects-edge`. Out of scope for this task; just leave a note/stub if trivial, do not build the consumer side.

## Files to modify

1. `src/components/three/ObsidianBackgroundCanvas.tsx` — depth-correlated opacity/size during formation; scatter bias from raycast hit point.
2. `src/components/sections/ProfileImage.tsx` — only if the overlay gap reproduces in a real screenshot.

## Do NOT

- Do not touch `FORM_MOUNT_IN_DURATION`, `FORM_CLICK_OUT_DURATION`, `FORM_CLICK_IN_DURATION`, or the mount-intro's own scatter look.
- Do not add a new "burst" system, new state machine, or new dependency — this extends the existing `formationActive` branch.
- Do not re-add `HeroTerminal` to the render tree.
- Do not add CometCard deep tilt on the profile image (light sweep only, already correct).
- Do not touch `HeroContent.tsx`'s comet-sweep overlay — it's already one-shot and correct.
- Do not build the About-pin / Projects-edge background-mode consumers yet — that's a later phase.

## Accessibility

- Canvas/scene remains decorative (`aria-hidden`).
- `prefers-reduced-motion`: sphere fully formed on load (already gated via `reducedMotion` check in the click listener and the mount-time data setup); skip click scatter and any new depth/bias effects.

## Acceptance criteria

- [ ] Click sphere: a viewer without being told can tell particles moved toward/away from them, not just sideways — depth is visible without needing to say "trust me, it's 3D"
- [ ] Click near one edge of the sphere vs. the other visibly differs in *where* the burst originates
- [ ] Mount-time intro (page load) is visually unchanged from before this change
- [ ] Profile: zero motion 2s after page load (regression check only)
- [ ] Hover overlay: screenshot confirms full cover or confirms no bug exists at `lg:` breakpoint
- [ ] Reduced motion: no scatter animation, no depth/bias effects applied
- [ ] `pnpm typecheck && pnpm lint` pass

## Implementation prompt

> Written for a single autonomous coding session (Claude Sonnet 5 in Cursor). Everything the agent needs is below — it should not need a follow-up turn to ask what "more 3D" means.

```
Read ui-fix-01-hero-background.md in full before touching any file — it contains a verified, corrected diagnosis; do not re-derive it from scratch or trust older comments/notes that mention `handleClick`, `burstActive`, `scatterBurstActive`, `BURST_DURATION`, or `burstScale` — none of those exist in this file, ignore any instruction that references them.

CONTEXT: The sphere click effect in src/components/three/ObsidianBackgroundCanvas.tsx already scatters particles in true isotropic 3D (see randomOffsetInSphere, ~line 212) using a real perspective camera. The underlying math is not flat. The user's complaint ("looks completely 2D") is a perceptual gap, not a math gap, caused by: (1) zero camera movement during the click animation, so there's no parallax; (2) depthWrite={false} + additive blending, so near/far points don't visually stratify; (3) the scatter direction is independent of where the sphere was actually clicked.

TASK — implement exactly these two changes, nothing else:

1. Depth-correlated visibility during the click/mount formation sequence (formationActive branch, ~line 742 onward):
   - Per point, compute distance from the point's current animated position to camera.position (you're already inside the per-point loop with x/y/z available; camera is already in scope via useThree).
   - Map that distance to an additional opacity and/or size multiplier layered on top of the existing PointsMaterial opacity/size — nearer points should read visibly brighter/larger than farther ones during the scatter, more strongly than the existing built-in sizeAttenuation alone produces.
   - Compute the near/far range from the actual spread of points during THIS animation (e.g. track min/max distance once per frame while formationActive), not a hardcoded guess — so it self-scales instead of needing hand-tuned constants.
   - This must have zero visible effect when formationActive is false (resting/scroll-driven state) — gate it accordingly.

2. Bias the click-triggered scatter from the actual click location:
   - In the onClick handler (~line 475), the raycast hit already provides hit[0].point (world-space). Currently discarded — capture it.
   - When rolling each point's fresh pScatter target inside formRetrigger handling (~line 539), blend the existing randomOffsetInSphere(FORM_SCATTER_RADIUS) result with an outward vector from the hit point for points whose rest position (pPos0) is near that hit point, tapering to the current unbiased random behavior for points farther from the hit. Use a smooth falloff (not a hard cutoff) so there's no visible seam between "biased" and "unbiased" points.
   - This bias applies ONLY to click-triggered replays, not the mount-time intro (mount calls the same scatter-generation code with no hit point — branch cleanly, don't change mount's look).

CONSTRAINTS:
- Do not change FORM_MOUNT_IN_DURATION, FORM_CLICK_OUT_DURATION, FORM_CLICK_IN_DURATION, or any other existing named constant's value.
- Do not add new dependencies. Do not create a new state machine or new "burst" abstraction — extend the existing formationActive branch and existing refs/typed arrays in place. No new per-frame allocations (this file is written zero-alloc per frame on purpose — reuse scratch variables/refs, don't `new THREE.Vector3()` inside useFrame).
- Do not touch HeroContent.tsx, ProfileImage.tsx, PortfolioContent.tsx, or anything about the background:mode CustomEvent system in this task.
- Respect prefers-reduced-motion exactly as the file already does (reducedMotion ref) — new depth/bias effects must be no-ops when it's true.

VERIFY before reporting done, and state the result of each explicitly:
(a) Click near the top-left of the sphere vs. click near the bottom-right visibly originate differently.
(b) During a click burst, particles nearer the camera are visibly brighter/larger than particles farther away, beyond what sizeAttenuation alone gave before your change.
(c) Page-load mount intro looks unchanged (screenshot or describe — no regression).
(d) prefers-reduced-motion: sphere stays fully formed, no scatter, no depth effect.
(e) No new console errors/warnings on click.
Run pnpm typecheck && pnpm lint and paste the output. Do not deploy, do not commit.

If after implementing (1) and (2) the effect still doesn't read as volumetric to you, stop and report what you tried and why it fell short, rather than escalating to changing FORM_SCATTER_RADIUS, the durations, or the camera path — those are out of scope for this task and affect the mount intro too.
```

## Dependencies

- None for this task.
- Blocks: Task 3.4 (About pin scatter sync) — that task should read this file's final state, not this note's pre-fix description.

## Risks

- Formation lerp fighting scroll physics — already gated (formationActive ignores velocity/physics until sequence completes); don't change that gating.
- Mobile: point counts already reduced via `useIsMobile` — the new per-point distance computation adds work inside the hot loop; keep it to cheap scalar math (squared-distance compares where possible, avoid `Math.sqrt`/`normalize` calls beyond what's already unavoidable) so mobile frame time doesn't regress.

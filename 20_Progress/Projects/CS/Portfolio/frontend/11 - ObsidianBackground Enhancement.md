---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - three
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# ObsidianBackground Enhancement
> Source of truth derived from [[10 - Codebase Reality & Confusion Clearance]] Part 2. Files: `src/components/three/ObsidianBackground.tsx` (next/dynamic `ssr:false` wrapper) and `src/components/three/ObsidianBackgroundCanvas.tsx` (836 lines — the implementation). **Delegate to the `three-artist` agent.** Do not touch the physics; only add the post-processing/colour layer described here.

## What already exists (do not rebuild)
A full per-frame physics simulation, zero-allocation, with three geometry layers and a CSS vignette:
- Fibonacci sphere (2,800 pts desktop / 1,400 mobile, `PLANET_RADIUS 0.8`), tilted torus ring (2,000/1,000, `RING_MAJOR_RADIUS 2.6`, 30° tilt), random starfield (5,500/2,750 over a 30-unit volume), and `LineSegments` connecting nearby sphere/ring points.
- Spring-return dots; **magnetic cursor dent** (facing dots pulled to cursor, back-side sympathetic wobble); **click burst** radial ripple; **scroll-progressive physics** (`stretchT` ramps 0→1 over the bottom 60% of scroll — stiffer springs, deeper displacement, camera zoom path); ring orbit + cursor attraction; stars dim mid-scroll.
- Soft-glow sprite `alphaMap` (64×64 radial gradient) so every point is a soft dot; **DPR capped at 1.25**; `antialias:false`; sidebar-aware right-edge shift (448px); reduced-motion drops pull 4.5× / drift 25×.
- Palette constants: planet `#9D8BBF`, ring/lines `#8A7AAE`, stars `#D0CBE8`, base `#05040A`. **No post-processing, no additive blending, no bloom.**

## The gap and the plan (impact/effort ordered)
The physics are strong; the *look* lacks the luminosity of premium 2025–26 space scenes. Add a post-processing + colour layer.

**Tier 1 — transforms the scene:**
1. Confirm/add `@react-three/postprocessing` (may already be present as an R3F peer; else `pnpm add @react-three/postprocessing`).
2. Wrap the Canvas scene in `<EffectComposer>` and add `<Bloom luminanceThreshold={0.18} luminanceSmoothing={0.9} intensity={0.35} />`. Tune to luminous, not blown out. Highest-impact change.
3. Switch planet + ring `PointsMaterial` to **`additiveBlending`**; drop base opacity (~0.52/0.46) to ~0.30–0.35 to compensate for accumulation → dense-cluster glow.

**Tier 2 — polish:**
4. `<ChromaticAberration offset={[0.0004, 0.0004]} />` inside the EffectComposer (subtle, cinematic).
5. Barely-perceptible **hue drift**: derive `COL_PLANET` from elapsed seconds (`t * 0.003`) in HSL so the sphere drifts `#9D8BBF`↔`#8BBFC0` over ~a minute — living, not frozen.

**Tier 3 — future sprint (defer):**
6. GLSL depth-based opacity falloff on stars. 7. Env-map reflections on ring line segments. 8. GPU-instanced lines (profile first).

## Performance guard (mandatory)
Post-processing adds a render pass on top of a heavy sim. Keep `dpr` at 1.25. Test on a mid-range phone after Tier 1; if <~50fps, gate effects off on mobile/reduced-motion:
```tsx
const skipEffects = isMobile || prefersReducedMotion;
// only wrap with <EffectComposer> when !skipEffects
```

## Done conditions
- EffectComposer + Bloom + additive blending live (Tier 1), optional chromatic aberration + hue drift (Tier 2); physics untouched.
- `dpr` still 1.25; mobile/reduced-motion bypass effects; ≥~50fps on mid-range mobile; no visual blow-out.
- Out of scope: the physics, the camera path, Tier 3 items.

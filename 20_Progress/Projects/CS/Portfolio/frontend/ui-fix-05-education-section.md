---
type: concept
status: active
updated: 2026-09-05
tags: [portfolio, frontend, ui-fixes, education, gsap, r3f]
notes:
  - "[[UI Fixes]]"
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[frontend-ui-fixes-index]]"
---

# UI Fix 05 — Education Section (Spring, Rope, Dot-Sync Deform)

> **Status:** partial — more is already built than earlier drafts of this note claimed
> **Ledger:** [[UI Fixes]] §4 | **Tasks:** 5.1–5.4
> **2026-09-05 correction pass:** re-verified line-by-line against `src/components/EducationFlowchart.tsx` (536 lines) and `src/components/sections/EducationSection.tsx` (39 lines) on `post-frontend`. Two of the four tasks below turned out to be **already implemented or mostly implemented** — the previous draft asked Cursor to build a rope connector and a dot-sync deform from scratch when both already exist in some form. Building them "from scratch" as instructed would have duplicated working code or fought it. Corrected below; same correction applied to [[frontend-ui-fixes-design]] Fix 7b and [[frontend-ui-fixes-tasks]] Phase 5.

## Purpose

Education becomes a **one-screen pinned performance**: spring bounce entry for three blobs, rope-like connectors, travelling dot with a clean loop restart, and College's blob deform tracking the dot without a visible snap.

## Current code (re-verified 2026-09-05)

| Symbol / component | Location | Status |
|---|---|---|
| `BASE_POS`, `DISTORT = [0, 0.42, 0.68]` | `EducationFlowchart.tsx` L14–18, L28 | Accurate as previously noted. `[0]=college` (top-centre), `[1]=high-school` (far left), `[2]=middle-school` (far right) |
| Entrance stagger | L31–46, L164–201 | **Exists**, but it's a `distort`-value stagger driven by `IntersectionObserver` (`hasEntered`) + cubic ease, not a position bounce. College resolves first, then +0.4s HS, then +0.4s MS |
| `StretchingLine` | L267–341 | **Already a dynamic curved connector**, not a rigid line — see below |
| `TravellingDot` | L347–390 | Loops middle→high→college continuously over `DOT_LOOP_DURATION_SEC = 14`, **no delay at loop restart** |
| `collegeDistortForT(t)` | L41–46 | **College's distort is already driven by dot progress** — see below |
| `EducationSection.tsx` | L22–34 | `section-pad-top-tight` + `mb-16` header — claim about it obscuring the sphere not yet visually confirmed (can't tell from static code; positions are 3D-projected) |
| ScrollTrigger / pin | — | **Does not exist for Education.** No gsap import anywhere in either file |

### `StretchingLine` is already a bent, live-synced curve — not a rigid line

Every frame it recomputes a `THREE.QuadraticBezierCurve3` from the two blobs' **live** positions: endpoints pulled in by `BLOB_R` so the line meets each blob's surface, and a control point offset perpendicular to the segment by `amplitude` (`CURVE_AMPLITUDE_MS_HS = 0.9`, `CURVE_AMPLITUDE_HS_COLLEGE = 0.35`) — a real bow/arc, not a straight segment, sampled into 28 points and drawn with drei's `Line` (dashed). Because it reads the blobs' floating positions every frame, it already visibly stretches and bends as the blobs drift.

This means the design doc's three-way choice ("SVG overlay vs R3F tube vs GSAP morph") is **moot** — a fourth, already-built, and arguably better option exists: R3F-native `QuadraticBezierCurve3` + drei `Line`. No new file, no new sync layer.

### College's blob deform already tracks the travelling dot

```ts
function collegeDistortForT(t: number): number {
  const ease = (p: number) => 1 - (1 - p) ** 3;
  return t < 0.5
    ? DISTORT[2] + (DISTORT[1] - DISTORT[2]) * ease(t * 2)   // dot at MS → HS: college 0.68 → 0.42
    : DISTORT[1] + (0 - DISTORT[1]) * ease((t - 0.5) * 2);   // dot at HS → college: college 0.42 → 0
}
```

Wired into `EduBlob` via `dotProgressRef` + `dotDrivesCollege`. So today: when the dot is at middle school, college reads as deformed to middle-school's level (0.68); as the dot travels to high school then arrives at college, college eases down to perfectly rigid (0). **The bug is the loop wrap**: `TravellingDot` resets `t` from ~1 straight to 0 (`% 1`) with no transition, and once the entrance stagger has finished (`eased` reaches 1), `EduBlob` sets `materialRef.current.distort = target` directly every frame with no smoothing — so the instant the dot loops, college's distort **jumps** from 0 to 0.68 in a single frame. That single-frame jump is almost certainly the "snaps rather than tracking gradually" complaint, not a missing feature.

## Target behavior

### 1. Header padding (Task 5.1 — quick win, unchanged)
- Verify visually first (screenshot at 375px + 1280px) whether the header actually overlaps the college blob before changing anything — the static markup (`mb-16`, `section-pad-top-tight`) doesn't prove the overlap either way once the R3F camera projection is involved.
- If confirmed: reduce `mb-16` → `mb-8` or a custom value; verify `section-pad-top-tight` isn't double-stacking with the section's own top padding.

### 2. ScrollTrigger pin + spring entry (Task 5.2 — genuinely not built)
- `ScrollTrigger` is already registered app-wide in `src/components/Providers.tsx` (`gsap.registerPlugin(ScrollTrigger)`) and already wired to Lenis's scroll event there — do not re-register it or reach for `ScrollSmoother`.
- `src/components/ui/split-heading.tsx` is the established local pattern for this codebase: `useGSAP` (`@gsap/react`) + `gsap.matchMedia()` for the reduced-motion branch. Copy that idiom, not a fresh one from GSAP's generic docs.
- New `src/lib/gsap/education-pin.ts` (genuinely doesn't exist — `src/lib/gsap/` isn't a directory yet): pin `#education` for ~1 viewport, then run an elastic **position** bounce (`ease: "elastic.out(1, 0.5)"`) — college first, high school +0.2s, middle school +0.4s. This is additive to, not a replacement for, the existing `distort` stagger in `EduBlob` — both can run off the same entrance trigger.
- Reduced motion: skip the pin and the position bounce; the existing `prefersReduced` branch in `EduBlob` already snaps distort to final values — leave that as-is.

### 3. Rope connectors (Task 5.3 — mostly done, tune don't rebuild)
- Do **not** build `EducationRopeOverlay.tsx` or any SVG/DOM sync layer — `StretchingLine` already produces a live, bent, blob-synced curve (see above).
- If it still doesn't read as "rope" enough: the tunable knobs are already there — `CURVE_AMPLITUDE_MS_HS` / `CURVE_AMPLITUDE_HS_COLLEGE` (bow depth) and `CURVE_SAMPLES` (smoothness). Try raising amplitude before adding any new mechanism. If a true sag/gravity droop (asymmetric curve, not a symmetric bow) is wanted, that's a one-line change to where `perpVec` is added relative to `midVec` in `StretchingLine`, not a new component.

### 4. Dot delay + college dot-sync fix (Task 5.4 — narrower than previously scoped)
- **Loop delay:** add a ~500ms pause at `t === 0` (dot at middle school, freshly looped) before `tRef.current` starts advancing again, inside `TravellingDot`'s `useFrame`.
- **Fix the snap, don't rebuild the mapping:** `collegeDistortForT` already encodes the right target curve. Add a short smoothing lerp (a few hundred ms) on `materialRef.current.distort` toward `target` instead of assigning `target` directly once `eased` has reached 1 in `EduBlob` — this removes the single-frame jump at loop restart without touching the entrance-stagger math.
- High school (idx 1) and middle school (idx 2) keep their static `DISTORT[1]` / `DISTORT[2]` — unaffected, already correct.

### 5. Reduced motion
- Already correct in `EduBlob` (`prefersReduced` branch snaps to final distort, no animation) and `Scene` (`TravellingDot` isn't even rendered when `prefersReduced`). New pin/bounce work in Task 5.2 must respect the same flag.

## Files to modify

| File | Action |
|---|---|
| `src/components/sections/EducationSection.tsx` | Header spacing — only after visual confirmation |
| `src/components/EducationFlowchart.tsx` | Loop delay in `TravellingDot`; smoothing lerp in `EduBlob`'s distort assignment; optional curve-amplitude tuning in `StretchingLine` |
| `src/lib/gsap/education-pin.ts` | NEW — pin + elastic position bounce, following `split-heading.tsx`'s `useGSAP`/`matchMedia` pattern |

~~`EducationRopeOverlay.tsx` (NEW, optional SVG overlay)~~ — not needed, remove from scope.

## Acceptance criteria

- [ ] Visual confirmation (or refutation) of header/sphere overlap before any header change
- [ ] Pin + elastic position bounce on entry: college, then HS +0.2s, then MS +0.4s
- [ ] Connector curve reads as rope/bent (tune existing amplitude first; only add mechanism if tuning genuinely isn't enough)
- [ ] Dot pauses ~500ms at middle school before each loop
- [ ] College's distort transition at loop restart is smooth, no single-frame snap
- [ ] `prefers-reduced-motion`: no pin, no bounce, no dot animation, distort at final per-blob values (already true — regression check only)
- [ ] `pnpm typecheck && pnpm lint` pass

## Implementation prompt

> Written for a single autonomous coding session (Claude Sonnet 5 in Cursor). Context is front-loaded so it shouldn't need a follow-up turn to figure out what already exists.

```
Read ui-fix-05-education-section.md in full before touching any file. It contains a verified 2026-09-05 correction: two of the four sub-tasks here (rope connectors, dot-synced deform) are ALREADY substantially implemented in src/components/EducationFlowchart.tsx. Do not rebuild StretchingLine or collegeDistortForT from scratch — you will duplicate or break working code. If any instruction elsewhere (older notes, comments) tells you to build a rope overlay component or a dot-sync deform system from zero, that instruction is stale — ignore it in favor of this file.

CONTEXT (confirmed by reading the file):
- StretchingLine (~L267) already draws a live, per-frame-recomputed QuadraticBezierCurve3 between blobs, offset by a tunable `amplitude` constant — it is already a bent, rope-like connector, not a straight line.
- collegeDistortForT (~L41) already maps the travelling dot's progress to College's MeshDistortMaterial.distort, ranging from middle-school's deform level down to fully rigid as the dot arrives at college.
- The one real bug: TravellingDot loops instantly (t goes from ~1 to 0 with a plain modulo, no pause), and once EduBlob's entrance stagger finishes, it assigns distort = target directly every frame with no smoothing — so College's distort visibly SNAPS at every loop restart. That snap is very likely what "not subtle at all" refers to.
- gsap + @gsap/react are already installed and ScrollTrigger is already registered + wired to Lenis in src/components/Providers.tsx — do not re-register it, do not evaluate ScrollSmoother. src/components/ui/split-heading.tsx is this codebase's existing useGSAP + gsap.matchMedia pattern for reduced-motion branching — follow that idiom.
- There is NO pin and NO position-bounce entrance for Education today — only a distort-value stagger (RESOLVE_STAGGER_SEC) driven by an IntersectionObserver. That part is a genuine, from-scratch task.

TASK — four independent-ish changes:

1. (Verify first, code second) Screenshot the Education section at 375px and 1280px. Only if the header visibly overlaps the college blob: reduce EducationSection.tsx's `mb-16` (or the `section-pad-top-tight` value) until it doesn't. If there's no overlap, say so and skip this — do not change spacing that isn't broken.

2. New src/lib/gsap/education-pin.ts (or a hook, matching split-heading.tsx's style): pin #education for ~1 viewport on scroll entry, then animate each blob's mesh POSITION (not distort — distort staggering already exists and should keep running independently) with `ease: "elastic.out(1, 0.5)"`: college first, high school +0.2s after, middle school +0.4s after. Use useGSAP with cleanup on unmount. prefers-reduced-motion: skip the pin and bounce entirely (EduBlob's existing prefersReduced branch already handles the static end-state).

3. In TravellingDot's useFrame: add a ~500ms pause at the top of each loop (when t wraps to 0) before resuming advancement — the dot should sit at middle school briefly, not restart instantly.

4. In EduBlob's useFrame, where `materialRef.current.distort = target` is assigned after the entrance stagger completes (`eased` at or near 1): replace the direct assignment with a short lerp of the CURRENT distort value toward `target` (a few hundred ms of smoothing), so the loop-restart transition is gradual instead of a single-frame jump. Do not change collegeDistortForT's math — the mapping itself is correct, only the assignment needs smoothing.

CONSTRAINTS:
- Do not touch DISTORT, DISTORT_SPEED, BASE_POS, CURVE_AMPLITUDE_MS_HS, CURVE_AMPLITUDE_HS_COLLEGE, RESOLVE_DURATION_SEC, RESOLVE_STAGGER_SEC, or DOT_LOOP_DURATION_SEC values unless a verify step in this prompt fails without changing them.
- Do not create EducationRopeOverlay.tsx or any new connector system — StretchingLine stays.
- Do not add new dependencies — gsap, @gsap/react, three, and drei are already installed and sufficient.
- Match the zero-per-frame-allocation discipline already used in this file (reuse refs/useMemo'd THREE objects; don't `new THREE.Vector3()` inside useFrame).

VERIFY before reporting done, state each explicitly:
(a) Header/sphere overlap: confirmed present and fixed, OR confirmed absent (with which viewport widths you checked).
(b) On scroll into Education: college bounces up first, then HS, then MS, each with a visible elastic settle — not a hard cut.
(c) The connector curves still track blob float in real time (unchanged from before your change).
(d) Dot visibly pauses at middle school before starting each loop.
(e) Watch two full dot loops — no visible snap/jump in college's blob shape at the loop boundary.
(f) prefers-reduced-motion: no pin, no bounce, no dot movement, blobs at static final distort values.
Run pnpm typecheck && pnpm lint and paste the output. Do not deploy, do not commit.
```

## Dependencies

- GSAP pin idiom: reuse `split-heading.tsx`'s `useGSAP`/`gsap.matchMedia` pattern directly — do not treat "GSAP pin research" as a prerequisite for this task the way [[ui-fix-02-about-section]] might; the registration and Lenis wiring already exist app-wide.
- Task 5.2 → 5.4 are independent of each other; 5.1 is independent of both.

## Risks

- Position-bounce entrance (new, Task 5.2) running alongside the existing distort-stagger (old, unchanged) — verify they don't visually fight (e.g. a blob's position bounce settling before its distort resolve finishes, or vice versa) rather than assuming they'll naturally line up.
- Mobile: `Canvas` already has `performance={{ min: 0.5 }}`; a new pin timeline shouldn't run a second RAF loop — drive it off the same GSAP ticker already ticking in `Providers.tsx`.
- `MeshDistortMaterial.distort`'s own `speed` prop (`DISTORT_SPEED`) already animates a wobble independent of the `distort` target value — the new smoothing lerp (Task 4) changes the target's transition, not the material's own internal animation; don't conflate the two.

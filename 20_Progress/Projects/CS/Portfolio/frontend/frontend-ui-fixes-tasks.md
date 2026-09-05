---
type: concept
status: active
created: 2026-07-11
updated: 2026-09-05
tags:
  - portfolio
  - frontend
  - ui-fixes
  - tasks
notes:
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-design]]"
  - "[[UI Fixes]]"
---

# Frontend UI Fixes — Tasks & Build Prompts

> **Updated:** 2026-09-05. Each task includes a **copy-paste implementation prompt** referencing [[frontend-ui-fixes-requirements]] and [[frontend-ui-fixes-design]].
> Run `pnpm typecheck && pnpm lint` after each phase; `pnpm build` before marking phase done.
> Master ledger: [[UI Fixes]].

## How To Use These Prompts

> **Per-component detailed specs:** [[frontend-ui-fixes-index]] — read the linked `ui-fix-*.md` note before each task.

1. Complete tasks in phase order unless marked independent.
2. Paste the **Prompt** block into a fresh agent session with repo access.
3. Agent must read cited files before editing.
4. Do not implement superseded items (July 4-card telemetry accordion).

---

## Phase 0 — Pre-Flight

### Task 0.1 — Deployment sync verification

**Prompt:**
```
Verify localhost vs production deployment sync for the portfolio repo.
Compare git rev-parse HEAD against latest Vercel production deployment SHA.
Record finding in a comment on Task 0.1 in frontend-ui-fixes-tasks.md or BUILD-STATUS:
- in-sync (SHA + date), out-of-sync (delta), or unable-to-verify (missing access).
If out-of-sync, STOP and flag before any UI work.
No code changes unless documenting the finding.
```

---

## Phase 1 — Sanity & Content Prep

### Task 1.1 — About summary + 2 stats content contract

**Files:** `src/sanity/schemaTypes/profile.ts`, `AboutSection.tsx` query

**Prompt:**
```
Read frontend-ui-fixes-requirements Fix Area 2 and profile.ts schema.
1. Confirm aboutSummary field exists (add if missing: text, max ~400 chars).
2. Confirm profile.stats[] has label, value, and optional order.
3. Update ABOUT_QUERY to fetch aboutSummary and stats[]{label, value, order} ordered asc.
4. Document in Studio: populate exactly 2 stats — "Ongoing always (5+)" / Side Quests and "100%" / Eager to Learn.
Run pnpm typegen && pnpm typecheck.
Do NOT build UI yet.
```

**Dependencies:** None

---

## Phase 2 — Hero & Background

### Task 2.1 — Click scatter: depth read + hit-point bias

**Files:** `src/components/three/ObsidianBackgroundCanvas.tsx`

**Prompt:** Use the implementation prompt in [[ui-fix-01-hero-background]] verbatim (its "Implementation prompt" section) — it was rewritten 2026-09-05 with a verified diagnosis and does not reference the old (nonexistent) `handleClick`/`burstActive`/`scatterBurstActive`/`BURST_DURATION`/`burstScale` symbols this task used to cite. Do not paste an older version of this prompt.

### Task 2.2 — Profile image static + hover overlay full cover

**Files:** `src/components/sections/HeroContent.tsx`, `ProfileImage.tsx`

**Prompt:**
```
Implement hero fixes from UI Fixes §1:
1. Profile image must have ZERO motion after entrance animation completes.
2. Hover overlay for Open Portfolio Lab / Close tab must cover ENTIRE image — fix visible gap on left and bottom borders.
Use absolute inset-0 on overlay inside overflow-hidden rounded wrapper.
Read HeroContent.tsx motion.div wrapping ProfileImage before editing.
Do not add CometCard deep tilt — light sweep only if already present.
Run pnpm typecheck. Manual QA at lg breakpoint.
```

**Dependencies:** Independent of 2.1

---

## Phase 3 — About Section (Pinned + 2 Glow Cards)

### Task 3.0 — GSAP ScrollTrigger research (prerequisite)

**Prompt:**
```
Most of this research is already answered by existing code, verified 2026-09-05:
gsap + @gsap/react are installed (package.json). gsap.registerPlugin(ScrollTrigger)
and Lenis→ScrollTrigger.update wiring already exist in src/components/Providers.tsx.
useGSAP is already used for a scroll-triggered reveal in src/components/ui/split-heading.tsx.
Read both files and confirm the pattern for yourself, then write a short note (a few lines,
not a page) at the top of the new about-pin file confirming: (1) which useGSAP pattern you're
copying, (2) that Lenis + ScrollTrigger is the confirmed scroll driver (no ScrollSmoother),
(3) your reduced-motion fallback approach. Do not implement the pin itself yet — that's Task 3.1.
Reference: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
```

### Task 3.1 — About ScrollTrigger pin + summary beats

**Files:** `AboutSectionClient.tsx`, new `src/lib/gsap/about-pin.ts`

**Prompt:** Use the "Implementation prompt" in [[ui-fix-02-about-section]] verbatim — rewritten 2026-09-05 with verified file/line references and the resolved Lenis+ScrollTrigger architecture question. Do not paste an older version of this prompt.

### Task 3.2 — Click-anywhere bio expand

**Files:** `AboutSectionClient.tsx`

**Note:** folded into Task 3.1's prompt (see [[ui-fix-02-about-section]]) since both edit the same `expanded` state in the same file — running them as separate agent sessions risks one clobbering the other's change to that state. Do not run this as a standalone task; treat 3.1's prompt as covering both.

### Task 3.3 — Telemetry: 2 cards, glow only (SUPERSEDES July accordion)

**Files:** `AboutTelemetry.tsx` — remove `TelemetryDetail` usage (confirmed present at line 6/108–112, do not delete the file itself)

**Prompt:** Use the "Implementation prompt" in [[ui-fix-03-about-telemetry]] verbatim — re-verified 2026-09-05 against the live file (line numbers confirmed accurate) with a corrected `order`-field note. Do not paste an older version of this prompt.

### Task 3.4 — Background sync for About pin scatter

**Files:** `ObsidianBackgroundCanvas.tsx`

**Prompt:**
```
Wire background:mode about-pin from About pin timeline to ObsidianBackgroundCanvas.
When mode=about-pin: run high-amplitude mesmerizing scatter/reform loop.
When mode returns idle: settle to normal scroll physics.
Use CustomEvent or React context — match existing orby:navigate pub/sub pattern.
Read ObsidianBackgroundCanvas intro/scatter code from Task 2.1.
prefers-reduced-motion: ignore about-pin mode.
Run pnpm typecheck.
```

**Dependencies:** Task 3.1, Task 2.1

---

## Phase 4 — Projects Pinned Cinematic

> **2026-09-05 correction:** both tasks below previously assumed auto-play was capped to indices 0–2 (it isn't — the live code cycles all projects) and missed the existing `Draggable` swipe gesture, "tether flash" effect, and `useSpaceFloat` ambient drift already on every visible card. **Auto-play scope resolved:** keep cycling all projects, confirmed by the user — do not paste an older version of either prompt below, use [[ui-fix-04-projects-section]] directly.

###### Task 4.1 — Projects ScrollTrigger pin + card emerge

**Files:** `src/components/three/ProjectsSlider.tsx`, `src/components/PortfolioContent.tsx` (the `#projects` section already lives there — no new wrapper component needed), new `src/lib/gsap/projects-pin.ts`

**Prompt:** Use the implementation prompt in [[ui-fix-04-projects-section]] verbatim — it covers pin + one-time emerge and explicitly protects the existing `slideVariants`/`AnimatePresence`, `Draggable`/`InertiaPlugin`, and `tetherActive` systems from being touched.

###### Task 4.2 — Projects edge border effect + side card drift

**Files:** `globals.css` (or scoped style), `src/hooks/use-space-float.ts` (read before extending)

**Prompt:** Also covered in [[ui-fix-04-projects-section]]'s implementation prompt (steps 3–4) — the edge effect is genuinely new CSS; side-card drift already exists via `useSpaceFloat` and stays as-is (always-on), only tune if the emerge transition needs it.

**Dependencies:** Task 4.1

## Phase 5 — Education Spring, Rope, Deform

> **2026-09-05 correction:** [[ui-fix-05-education-section]] was re-verified against the live repo — Tasks 5.3 and 5.4 are largely already implemented (rope connector, dot-sync deform both exist; only a loop-restart smoothing bug needs fixing). Use that note's single "Implementation prompt" instead of the four separate prompts below — they duplicate a now-corrected spec and the "replace rigid lines" framing in 5.3 is factually wrong (the connector is already curved).

### Task 5.1 — Education header padding fix

**Files:** `src/components/sections/EducationSection.tsx`

**Prompt:** Use [[ui-fix-05-education-section]]'s "Implementation prompt" (covers all of 5.1–5.4 in one pass, item 1). Verify the overlap visually before changing spacing — the old instruction to just "reduce top padding" assumed a bug that hasn't been screenshotted.

### Task 5.2 — Education ScrollTrigger pin + spring entry

**Files:** `src/components/sections/EducationSection.tsx`, `src/components/EducationFlowchart.tsx`, new `src/lib/gsap/education-pin.ts`

**Prompt:** Use [[ui-fix-05-education-section]]'s "Implementation prompt" (item 2). This is the one genuinely from-scratch piece of Phase 5 — no pin or position-bounce exists today. Reuse the app's already-registered ScrollTrigger + Lenis wiring (`Providers.tsx`) and the `useGSAP`/`gsap.matchMedia` pattern in `split-heading.tsx`; do not re-research GSAP setup (Task 3.0's research applies here too, once done for About).

### Task 5.3 — Rope connectors (replace rigid lines)

**Status: already implemented — do not run this task as written.**

`StretchingLine` in `EducationFlowchart.tsx` already draws a live, per-frame `QuadraticBezierCurve3` between blobs with a tunable bow amplitude — a real bent connector, not a rigid line. Rebuilding it (SVG overlay, `TubeGeometry`, or otherwise) would duplicate or break working code. If the curve still doesn't read as rope-like enough, tune `CURVE_AMPLITUDE_MS_HS`/`CURVE_AMPLITUDE_HS_COLLEGE` first. Full detail: [[ui-fix-05-education-section]] item 3.

### Task 5.4 — Dot delay + Bachelor's dot-sync deform

**Files:** `src/components/EducationFlowchart.tsx`

**Prompt:** Use [[ui-fix-05-education-section]]'s "Implementation prompt" (items 3–4). Narrower than it looks: `collegeDistortForT` already implements the dot-sync deform mapping — the only real bug is an instant loop-restart snap (no dot pause, no distort smoothing). Do not rebuild the mapping; add the pause + smoothing lerp only.

## Phase 6 — Logo, Footer, Lab Input

### Task 6.1 — Logo: remove tab glow, thinner cursive A

**Files:** `src/lib/logoGlyphPath.ts` (glyph shape only — the "remove tab glow" half of this task is blocked, see below)

**Prompt:** Use the implementation prompt in [[ui-fix-06-logo-footer]] verbatim. 2026-09-05 correction: no logo instance exists in the header or Lab panel today (only in `Footer.tsx`), and no code ties glow to sidebar open/closed state anywhere — the "remove tab glow" premise did not survive a repo check. That prompt implements only the glyph-shape regeneration and excludes the glow item pending a fresh repro from the user. Do not paste an older version of this prompt that sends an agent hunting for a glow bug in `HeaderLogoCanvas.tsx`/`useAnimationGate.ts`.

### Task 6.2 — Footer logo placement

**Files:** `src/components/Footer.tsx`

**Prompt:** Use the implementation prompt in [[ui-fix-06-logo-footer]] verbatim (its footer-sizing item). 2026-09-05 correction: placement is **already done** — `<HeaderLogo show={true} />` already sits leftmost, left of "Anant's Hub", in `Footer.tsx` line ~43. The real remaining gap is sizing: `HeaderLogo` has no size prop and hardcodes a fixed 32×32px footprint, so it doesn't match the `~1em` footer-text height yet. Fix locally in `Footer.tsx` with a wrapper + CSS transform — do not add a size prop to `HeaderLogo`/`HeaderLogoCanvas`/`HeaderLogoFallback` for a single call site.

### Task 6.3 — Lab textarea vertical centering

**Files:** `src/components/lab/ChatInputBar.tsx`

**Prompt:** Use the implementation prompt in [[ui-fix-07-portfolio-lab]] verbatim (its "Implementation prompt" section, Task 1) — rewritten 2026-09-05 with the exact line numbers (80–85) and a conditional-alignment approach that reuses the existing `resize()` measurement instead of a new one.

**Dependencies:** None

## Phase 7 — Carry-Forward (July, if not done)

### Task 7.1 — Portfolio Lab mobile send button repro + fix

**Prompt:** Use [[ui-fix-07-portfolio-lab]] Implementation prompt, Task 2. Reproduce at 320/375/390px in `src/components/lab/ChatInputBar.tsx` inside the Portfolio Lab sidebar (`src/components/ui/sidebar.tsx`, `SIDEBAR_WIDTH_MOBILE = "100%"`) BEFORE editing anything. No code-level evidence of a bug exists today — if it doesn't reproduce, say so and make no changes.

### Task 7.2 — Chat bubble break-words

**Status: ALREADY DONE — 2026-09-05 verification.** `src/components/lab/ChatThread.tsx` line 162 already has `break-words` on the user message bubble class list. No code change needed. If re-running this task, only do the regression check (paste a long unbroken string, confirm it wraps) — see [[ui-fix-07-portfolio-lab]] Implementation prompt, Task 3.

### Task 7.3 — Skills graph 2022 + 35 cap

**Files:** `SkillsCapabilityGraph.tsx`

**Prompt:**
```
Shift YEARS to start 2022. Clamp first plotted value to max 35 in buildCurveValues.
See requirements Fix Area 7.
```

### Task 7.4 — Dark mode toggle + light tokens

**Files:** `HeaderScrolling.tsx`, `globals.css`

**Prompt:**
```
Wire useTheme setTheme on header button. Add :root:not(.dark) cosmic-card companions.
ObsidianBackgroundCanvas stays dark-only.
See requirements Fix Area 9.
```

### Task 7.5 — Orby polish bundle

**Files:** `OrbyModel.tsx`, `Orby.tsx`, `useOrbyIdleCommentary.ts`, `api/orby-comment/route.ts`

**Prompt:**
```
Implement remaining Orby items from requirements Fix Area 9:
- Radio antenna prop
- Deeper wave animation
- Idle commentary hook + API route
- radio-talk + walking poses during roaming
- Ground anchoring oscillation toward bottomY
Sequence changes to avoid merge conflicts in OrbyModel.tsx.
```

---

## Phase 8 — Verification

### Task 8.1 — Full pipeline + manual QA

**Prompt:**
```
Run: pnpm typegen && pnpm typecheck && pnpm lint && pnpm test && pnpm build
Manual QA checklist:
- [ ] Hero sphere click: 3D volumetric scatter
- [ ] Profile overlay: full image cover on hover
- [ ] About: pin, summary beats, 2 glow cards, click-anywhere bio
- [ ] Projects: pin, emerge, edge effect, side drift
- [ ] Education: pin, spring, rope, dot deform, header padding
- [ ] Logo: no tab glow, footer placement
- [ ] Lab: textarea vertical center
- [ ] prefers-reduced-motion: all fallbacks
- [ ] 320px, 375px, 768px, 1280px, 1440px
Fix any failures before marking UI fix pass complete.
```

---

## Task Dependency Graph

```
0.1 (deploy sync) → gates all

1.1 (Sanity) → 3.1, 3.3

2.1 (volumetric scatter) → 3.4
2.2 (hero overlay) — independent

3.0 (GSAP research) → 3.1 → 3.2, 3.4
3.3 (glow cards) — parallel with 3.1 after 1.1

4.1 (projects pin) → 4.2

5.1 (padding) — independent
5.2 (education pin) → 5.3 → 5.4

6.1 (logo) → 6.2
6.3 (lab input) — independent

7.x carry-forward — mostly independent

8.1 — final gate
```

---

## Superseded Tasks (Do Not Run)

| Old Task | Reason |
|---|---|
| July 2.7 Telemetry accordion + TelemetryDetail | Replaced by Task 3.3 glow-only |
| July 3.10 Education entry-only stagger | Replaced by Phase 5 full sequence |
| July 3.4–3.5 auto-play only | Superseded by Phase 4 pin (auto-play retained inside) |

---

## Task → component spec map

| Task | Read first |
|---|---|
| 0.1 | [[ui-fix-08-carry-forward]] |
| 1.1 | [[ui-fix-02-about-section]], [[ui-fix-03-about-telemetry]] |
| 2.1–2.2 | [[ui-fix-01-hero-background]] |
| 3.0–3.4 | [[ui-fix-02-about-section]], [[ui-fix-03-about-telemetry]] |
| 4.1–4.2 | [[ui-fix-04-projects-section]] |
| 5.1–5.4 | [[ui-fix-05-education-section]] |
| 6.1–6.2 | [[ui-fix-06-logo-footer]] |
| 6.3, 7.1–7.2 | [[ui-fix-07-portfolio-lab]] |
| 7.3–7.5, 8.1 | [[ui-fix-08-carry-forward]] |

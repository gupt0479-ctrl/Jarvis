---
type: concept
status: active
created: 2026-07-11
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
# Frontend UI Fixes — Tasks

> Implementation-focused companion to [[frontend-ui-fixes-requirements]] and [[frontend-ui-fixes-design]]. Each task maps back to a Fix Area in the requirements doc. Run `pnpm typecheck` and `pnpm lint` after every phase; run `pnpm build` before considering a phase done.

## Phase 1 — Sanity Backend Prep

### Task 1.1 — Add `profile.aboutSummary` field
- **File(s):** `src/sanity/schemaTypes/profile.ts`
- **Change:** Add new `defineField({ name: "aboutSummary", type: "text", rows: 3, validation: (Rule) => [Rule.max(400).warning(...)] })`
- **Dependencies:** None
- **Sanity changes:** Schema field addition; run `pnpm typegen` after
- **Testing:** Manual — open Studio, confirm field renders; `pnpm typecheck` passes after typegen
- **Estimated impact:** About section only
- **Rollback:** Remove the field block; re-run `pnpm typegen`. Non-destructive (existing docs unaffected by an added optional field).

### Task 1.2 — Extend `profile.stats[]` with `summary`
- **File(s):** `src/sanity/schemaTypes/profile.ts` (inside the `stats` array member's `fields`)
- **Change:** Add `defineField({ name: "summary", type: "string" })` to the `stats[]` object member
- **Dependencies:** None
- **Sanity changes:** Schema field addition; `pnpm typegen`
- **Testing:** Manual Studio check + `pnpm typecheck`
- **Estimated impact:** About Telemetry cards only
- **Rollback:** Remove the field; existing `stats[]` entries keep working without it (optional field)

### Task 1.3 — Update `ABOUT_QUERY` and `PROFILE_QUERY` projections
- **File(s):** `src/components/sections/AboutSection.tsx` (inline `ABOUT_QUERY`), `src/sanity/lib/queries.ts` (`PROFILE_QUERY`)
- **Change:** Add `aboutSummary` to `ABOUT_QUERY`; add `summary` to `stats[]{...}` projection in `PROFILE_QUERY`
- **Dependencies:** Tasks 1.1, 1.2
- **Sanity changes:** None (query-only)
- **Testing:** `pnpm typecheck`; manually verify the query returns the new fields via Sanity Vision or a console log during dev
- **Estimated impact:** About section, Telemetry cards
- **Rollback:** Revert projection changes; queries degrade gracefully (missing fields become `undefined`)

### Task 1.4 — Data entry: populate `aboutSummary` and `stats[].summary` in Studio
- **File(s):** None (content-only, done in Sanity Studio)
- **Dependencies:** Tasks 1.1–1.3 deployed
- **Sanity changes:** Content authoring, not schema
- **Testing:** Visual check once Fix Area 2/3 UI ships
- **Estimated impact:** About section content quality
- **Rollback:** N/A (content edit)

---

## Phase 2 — Component Refactors

### Task 2.1 — Remove HeroTerminal from render tree
- **File(s):** `src/components/PortfolioContent.tsx`
- **Current code location:** Import line (`import { HeroTerminal } from "@/components/HeroTerminal";`) and the `<div className="relative z-10 flex justify-center"><HeroTerminal /></div>` block, directly below `<HeroSection />`
- **Change:** Delete both the import and the JSX block. Do NOT delete `src/components/HeroTerminal.tsx` itself.
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Visual check — hero renders with no terminal window below it; `pnpm build` succeeds (no dangling import)
- **Estimated impact:** Hero section only
- **Rollback:** Re-add the two removed lines

### Task 2.2 — Add comet-sweep overlay to profile image
- **File(s):** `src/components/sections/HeroContent.tsx`
- **Change:** Wrap the existing `<ProfileImage>` `motion.div` in a new `relative overflow-hidden` container; add a one-shot `motion.div` gradient sweep per design doc's animation spec (`initial={{x:"-120%"}}`, `animate={{x:"120%"}}`, `transition={{duration:1.4, delay:0.6, ease:"easeInOut"}}`, no repeat)
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Visual check on desktop (`lg:` breakpoint, since this wrapper is `hidden lg:flex`); confirm sweep plays once on mount and does not repeat or trigger on hover
- **Estimated impact:** Hero section, desktop only
- **Rollback:** Remove the wrapper and sweep `motion.div`

### Task 2.3 — Background scatter-intro animation
- **File(s):** `src/components/three/ObsidianBackgroundCanvas.tsx`
- **Current code location:** `Graph` component's `data` `useMemo` (where `pPos0`/`pPos` are initialized, ~line with `pPos0[i3] = pPos[i3] = pPts[i][0]`) and the `useFrame` callback (planet physics loop)
- **Change:** In the `data` `useMemo`, initialize `pPos[i3..2]` to a scattered offset from `pPos0[i3..2]` instead of an identical copy (skip if `useReducedMotion()` is true). In `useFrame`, add an `introProgress` ref-driven lerp term that pulls `pPos` toward `pPos0` over ~2–4s, fading its own influence to zero as `introProgress → 1`, before scroll/pointer physics engage.
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Manual visual verification on page load (desktop + mobile point counts); confirm `prefers-reduced-motion` skips the effect entirely (sphere renders already-formed); confirm no console errors from the added ref
- **Estimated impact:** Landing hero background only
- **Rollback:** Revert `pPos` initialization to direct copy; remove the `introProgress` lerp block from `useFrame`

### Task 2.4 — Click-triggered scatter/rejoin (blast radius)
- **File(s):** `src/components/three/ObsidianBackgroundCanvas.tsx`
- **Current code location:** `handleClick`/`burstActive`/`burstTimer` block and the burst-force calculation inside the planet physics loop (`if (burstActive.current && burstP > 0) {...}`)
- **Change:** Add a second burst mode (`scatterBurstActive`) triggered by the same `handleClick`, using constant outward-push force (via `pNorm`) instead of the existing radial-ripple sine wave; reuse `BURST_DURATION`/`burstScale` constants
- **Dependencies:** Task 2.3 (shares the scatter visual language)
- **Sanity changes:** None
- **Testing:** Click inside the sphere's hit-mesh at multiple scroll positions; confirm scatter/rejoin plays and scales with `stretchT`/`burstScale`; confirm existing radial-ripple burst still works if kept as an alternate mode (or confirm intentional replacement if scatter fully replaces ripple — clarify with user before removing the ripple entirely)
- **Estimated impact:** Landing hero + full-page background (click works at any scroll position)
- **Rollback:** Remove the `scatterBurstActive` branch; existing ripple burst is untouched throughout

### Task 2.5 — About section split into server + client components
- **File(s):** `src/components/sections/AboutSection.tsx` (keep as server component, trim to just the fetch), new `src/components/sections/AboutSectionClient.tsx` (new file, client component)
- **Change:** Move the `CometCard`/`PortableText`/heading JSX into `AboutSectionClient.tsx`; `AboutSection.tsx` fetches via `ABOUT_QUERY` (updated in Task 1.3) and passes `profile` as a prop
- **Dependencies:** Task 1.3
- **Sanity changes:** None (already done in Phase 1)
- **Testing:** Visual regression check — section should render identically to before this split, before adding the toggle in Task 2.6
- **Estimated impact:** About section
- **Rollback:** Revert to the single-file server component

### Task 2.6 — About collapsible toggle
- **File(s):** `src/components/sections/AboutSectionClient.tsx`
- **Change:** Add `const [expanded, setExpanded] = useState(false)`. Render `profile.aboutSummary` (fallback: first Portable Text block of `fullBio`) when collapsed; render full `fullBio` PortableText when expanded. Add a `<button aria-expanded={expanded}>` toggle, `AnimatePresence` + `height:auto` wrapper (reuse `ExperienceCard.tsx`'s exact transition values)
- **Dependencies:** Task 2.5
- **Sanity changes:** None
- **Testing:** Manual — verify collapsed state ≈1 viewport at 375px/1440px; verify toggle expands/collapses without page jump; verify `aria-expanded` toggles correctly (inspect via browser devtools/axe)
- **Estimated impact:** About section
- **Rollback:** Remove toggle state, always render full `fullBio` (previous behavior)

### Task 2.7 — Telemetry cards: click-to-expand + mini-graph
- **File(s):** `src/components/AboutTelemetry.tsx`, new `src/components/TelemetryDetail.tsx`
- **Change:** Lift `expandedIndex: number | null` state into `AboutTelemetry.tsx`; make `TelemetryCard` a `<button>`-driven expandable card; new `TelemetryDetail.tsx` renders a small SVG graph (source: derive from `SKILLS_QUERY`/`PROJECTS_QUERY` per design doc — needs the relevant query result passed down as a prop from a parent that already fetches it, likely threading through `AboutSectionClient.tsx`) plus `stat.summary` text
- **Dependencies:** Task 1.2/1.3 (for `summary` field), Task 2.5 (for the client-component split enabling prop-threading)
- **Sanity changes:** None beyond Phase 1
- **Testing:** Manual click-through all 4 cards; verify only one expands at a time (accordion); verify `aria-expanded` + `role="img"`/`aria-label` on the SVG
- **Estimated impact:** About section (Telemetry sub-block)
- **Rollback:** Revert to static, non-interactive cards

---

## Phase 3 — Complex Interactions

### Task 3.1 — Portfolio Lab: growable textarea
- **File(s):** `src/components/lab/ChatInputBar.tsx`
- **Change:** Replace `<input type="text">` with `<textarea>`; add auto-grow logic (measure `scrollHeight`, cap at 3 lines via `maxHeight`); update `onKeyDown` so `Enter` submits and `Shift+Enter` inserts a newline; add `aria-label="Message to Orby"` (textarea currently relies on placeholder only — add a real label)
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Manual — type multi-line messages, verify growth caps at 3 lines then scrolls internally; verify `Shift+Enter` inserts newline, plain `Enter` sends; verify existing paste-persona-detection logic (`handlePaste`) still fires correctly with the new element type
- **Estimated impact:** Portfolio Lab sidebar, all viewports
- **Rollback:** Revert to `<input type="text">`

### Task 3.2 — Portfolio Lab: character-length indicator + cap
- **File(s):** `src/components/lab/ChatInputBar.tsx`
- **Change:** Add `const MAX_LEN = 1000` (confirm exact value with user first — flagged in design doc), block input past cap (`if (e.target.value.length <= MAX_LEN)`), render a length indicator that becomes visible only near the cap (`value.length > MAX_LEN * 0.8`)
- **Dependencies:** Task 3.1
- **Sanity changes:** None
- **Testing:** Manual — paste a very long string, confirm input is blocked (not truncated) past `MAX_LEN`; confirm indicator appears only near the limit; confirm `aria-live="polite"` doesn't spam screen readers during normal typing
- **Estimated impact:** Portfolio Lab sidebar
- **Rollback:** Remove cap/indicator; textarea from Task 3.1 remains functional without it

### Task 3.3 — Verify mobile sidebar/send-button layout (root cause investigation)
- **File(s):** Likely `src/components/ui/sidebar.tsx`, `src/components/lab/PortfolioLab.tsx`, `src/components/lab/ChatInputBar.tsx` — **exact file TBD pending reproduction**
- **Change:** None until root cause is confirmed. Reproduce the reported "send button off-screen, must zoom out" bug on an actual 320–375px viewport (browser devtools device emulation at minimum, real device ideally) before touching code.
- **Dependencies:** None (can run in parallel with other Phase 3 tasks)
- **Sanity changes:** None
- **Testing:** Device/emulator reproduction first; once root cause is identified, write a regression test (Vitest + jsdom, or a Playwright viewport test if the E2E suite in `e2e-screenshots/` supports it) that asserts the send button's bounding box stays within the viewport at 320px width
- **Estimated impact:** Portfolio Lab sidebar, mobile only
- **Rollback:** N/A (investigation task)

### Task 3.4 — Projects carousel: auto-play for indices 0–2
- **File(s):** `src/components/three/ProjectsSlider.tsx`
- **Change:** Add `AUTO_PLAY_INTERVAL_MS`, `AUTO_PLAY_MAX_INDEX = 3` constants; add `autoPlayPaused` state + `idleTimerRef`; add the `useEffect` interval per design doc; ensure `setCurrentIndex` modulo is `% AUTO_PLAY_MAX_INDEX` for auto-advance only (manual nav keeps `% safeProjects.length`)
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Manual — load page, confirm carousel cycles 1→2→3→1 automatically without user input; confirm it never auto-advances past index 2 (project 3)
- **Estimated impact:** Projects section
- **Rollback:** Remove the new `useEffect`/state; carousel reverts to fully manual (current behavior)

### Task 3.5 — Projects carousel: pause on interaction + reduced motion
- **File(s):** `src/components/three/ProjectsSlider.tsx`
- **Change:** Add `setAutoPlayPaused(true)` inside `goNext`, `goPrev`, dot-click handler, drag handlers; add `onMouseEnter`/`onFocus` pause at the `<section>` level; add a local `prefersReducedMotion` check (matching the pattern in `ObsidianBackgroundCanvas.tsx`) that disables auto-play entirely; add resume-after-idle timer (~10s)
- **Dependencies:** Task 3.4
- **Sanity changes:** None
- **Testing:** Manual — interact with any nav control, confirm auto-play stops immediately and resumes ~10s after last interaction; confirm `prefers-reduced-motion: reduce` (OS-level or devtools emulation) disables auto-play entirely
- **Estimated impact:** Projects section
- **Rollback:** Remove pause logic; auto-play runs continuously (acceptable fallback, though violates WCAG 2.2.2 — do not ship without this task)

### Task 3.6 — Projects carousel: slug-lookup dead-code cleanup
- **File(s):** `src/components/three/ProjectsSlider.tsx`
- **Current code location:** `handleOrbNav`'s slug-resolution logic (`typeof p.slug === "string" ? p.slug : (p.slug as {current?:string}|null)?.current`)
- **Change:** Simplify to `const slug = (p.slug as { current?: string } | null)?.current ?? null;` since `PROJECTS_QUERY` always returns `slug{current}`, never a bare string
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** `pnpm typecheck`; manually trigger `orby:navigate` with a known project slug (e.g., via browser console `window.dispatchEvent(new CustomEvent("orby:navigate", {detail: {sectionId: "projects", itemSlug: "<real-slug>"}}))`) and confirm the carousel jumps to the correct project
- **Estimated impact:** Projects section, chat-driven navigation
- **Rollback:** Revert to the `typeof` branch (functionally equivalent, just noisier)

### Task 3.7 — Skills graph: shift year range forward, enforce 35-cap
- **File(s):** `src/components/sections/SkillsCapabilityGraph.tsx`
- **Current code location:** `const YEARS = [...]` constant; `buildCurveValues` function
- **Change:** **Confirm with user first** (flagged in design doc) whether to shift to `["2022"..."2027"]` or drop to a 5-point `["2022"..."2026"]`. Once confirmed, update `YEARS`. In `buildCurveValues`, add `values[0] = Math.min(values[0], 35)` clamp before returning.
- **Dependencies:** User confirmation on year-range approach
- **Sanity changes:** None
- **Testing:** Manual — inspect the rendered graph, confirm no category line starts above the Y=35 gridline; confirm X-axis labels read correctly
- **Estimated impact:** Skills section graph
- **Rollback:** Revert `YEARS` and remove the clamp line

### Task 3.8 — Skills: reduce SkillPill hover-effect variety
- **File(s):** `src/components/sections/SkillsSectionClient.tsx`
- **Current code location:** `SkillPill`'s `effect = effectIndex % 7` and the associated conditional JSX blocks (constellation dots, glitch-scan, orbit-dot, etc.)
- **Change:** **Confirm with user which 3 effects to keep** (design doc recommends keeping ring-pulse/gradient-wash/3D-tilt, dropping glitch-scan/constellation/orbit-dot/box-shadow-halo). Change `effect = effectIndex % 3` and delete the unused effect branches.
- **Dependencies:** User sign-off on which effects to keep
- **Sanity changes:** None
- **Testing:** Manual hover-through of the skill pill grid; confirm smoother, more cohesive feel; `pnpm lint` (Biome) passes after removing dead JSX branches
- **Estimated impact:** Skills section
- **Rollback:** Restore `% 7` and the removed branches

### Task 3.9 — Education/Skills/Certifications spacing tightening
- **File(s):** `src/app/globals.css`, `src/components/sections/EducationSection.tsx`, `src/components/sections/SkillsSection.tsx`
- **Current code location:** New CSS classes added near the existing `.section-pad` rule; `className` on the `<section>` elements in `EducationSection.tsx`/`SkillsSection.tsx`
- **Change:** Add `--section-pad-y-tight` custom property + `.section-pad-top-tight`/`.section-pad-bottom-tight` utility classes; apply `section-pad-bottom-tight` to Skills' `<section>` and `section-pad-top-tight` to Education's `<section>` (in place of / alongside the existing `section-pad` class — verify cascade order per design doc's note)
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Visual check of the Skills→Education→Certifications vertical rhythm together (not Education in isolation, since Certifications already has custom `pt-12`); confirm no double-tightening artifact
- **Estimated impact:** Skills, Education, Certifications section spacing
- **Rollback:** Remove the new classes; sections revert to uniform `section-pad`

---

## Phase 4 — Orby & Global Features

### Task 4.1 — Orby radio prop redesign
- **File(s):** `src/components/orby/OrbyModel.tsx`
- **Current code location:** The `<motion.div>` "Radio" block inside the right-arm JSX (`{/* Radio */}` comment)
- **Change:** Add an antenna sub-element (thin rotated div + glowing tip dot) as a sibling inside the radio's wrapper; adjust radio body proportions slightly if needed for visual balance
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Visual check of Orby in `wave`/`pointing`/`idle` poses — confirm the radio reads clearly as a radio with antenna at all sizes (`64px` mobile, `88px` desktop canvas)
- **Estimated impact:** Orby companion, all pages
- **Rollback:** Remove the antenna sub-element

### Task 4.2 — Orby wave animation: full arm-raise
- **File(s):** `src/components/orby/OrbyModel.tsx`
- **Current code location:** `animate={pose === "wave" ? { rotate: [0, -25, 0, -25, 0] } : undefined}` on the right-arm `motion.div`
- **Change:** Update to a deeper rotation range (e.g., `[0, -70, -50, -70, -20]`), extend `transition.duration` slightly (e.g., `1.4`)
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Visual check during `intro`/`goodbye`/`departingLeft` states (all map to `pose === "wave"` per `getPose()` in `Orby.tsx`)
- **Estimated impact:** Orby companion
- **Rollback:** Revert to `[0, -25, 0, -25, 0]`

### Task 4.3 — Orby idle commentary: backend endpoint
- **File(s):** New `src/app/api/orby-comment/route.ts`
- **Change:** New route handler reusing `routeChat`'s provider chain from `src/lib/model-router.ts` with a minimal, tool-free, ungrounded flavor-text system prompt; rate-limited via a new Upstash key namespace (`orby:idle:${sessionId}`)
- **Dependencies:** None (independent of frontend hook, but hook in Task 4.4 depends on this)
- **Sanity changes:** None — explicitly ungrounded per design doc's decision
- **Testing:** `curl`/Postman test against the new route in dev; confirm rate-limiting triggers correctly after repeated calls; confirm graceful fallback (canned line) if all providers fail, matching the existing `degraded`/`cooldown` modes pattern in `model-router.ts`
- **Estimated impact:** New backend surface, no existing route touched
- **Rollback:** Delete the new route file; frontend hook (Task 4.4) simply has nothing to call

### Task 4.4 — Orby idle commentary: frontend hook
- **File(s):** New `src/components/orby/useOrbyIdleCommentary.ts`, composed inside `src/components/orby/Orby.tsx`
- **Change:** New hook tracks scroll-dwell time and/or Orby-click count; on trigger, calls Task 4.3's endpoint and dispatches `window.dispatchEvent(new CustomEvent("orby:speech", {detail:{text}}))` — reuses the existing event channel `useOrbyState.ts` already listens for; enforce a client-side minimum cooldown (~45s) between triggers independent of server-side rate limiting
- **Dependencies:** Task 4.3
- **Sanity changes:** None
- **Testing:** Manual — scroll and pause on a section, confirm an idle comment appears after the dwell threshold; confirm cooldown prevents rapid-fire commentary; confirm `useOrbyState.ts` requires zero code changes (verify via git diff — this file should not appear in the diff for this task)
- **Estimated impact:** Orby companion, all pages
- **Rollback:** Remove the hook and its composition in `Orby.tsx`; no other file affected

### Task 4.5 — Orby: additional roaming visual sub-states
- **File(s):** `src/components/orby/OrbyModel.tsx` (new `pose` value handling), `src/components/orby/Orby.tsx` (`getPose()` cycling logic)
- **Change:** Add a `"radio-talk"` pose (head-tilt + radio-hand shake animation) to `OrbyModel.tsx`; in `Orby.tsx`, add a local timer that alternates the pose between `"idle"` and `"radio-talk"` while `state === "roaming"`, without modifying `useOrbyState.ts`
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Visual check during the `roaming` state (mid-scroll) — confirm Orby's animation reads as more varied than a single continuous drift
- **Estimated impact:** Orby companion
- **Rollback:** Remove the pose-cycling timer; `roaming` reverts to a single `idle`-pose look

### Task 4.6 — Dark/Light theme: wire the toggle
- **File(s):** `src/components/HeaderScrolling.tsx`
- **Current code location:** `useTheme();` (unused return) and the no-op `onClick` on the theme `<button>`
- **Change:** `const { theme, setTheme } = useTheme();`; `onClick={() => setTheme(theme === "dark" ? "light" : "dark")}`; dynamic `aria-label`; swap `Moon`/`Sun` icon based on `theme`; remove `cursor-default` styling
- **Dependencies:** Task 4.7 (light tokens should exist before the toggle is user-facing, though technically the toggle can ship first with a broken-looking light mode temporarily during development)
- **Sanity changes:** None
- **Testing:** Manual — click toggle, confirm `<html>` class changes (`next-themes` behavior), confirm icon/label update
- **Estimated impact:** Global header, all pages
- **Rollback:** Revert to the no-op `onClick` and static label

### Task 4.7 — Light-mode design tokens
- **File(s):** `src/app/globals.css`
- **Change:** Add `:root:not(.dark)` (or equivalent) companion rules for `.cosmic-card`, `.cosmic-card--dark`, `.cosmic-card--subtle`, `.orbit-chip`, `.section-kicker`, `.float-btn`/`.header-btn` glow colors — per design doc's example block, using an off-white/lavender-tinted palette, never pure white
- **Dependencies:** None (can be built independently of Task 4.6, tested via manually toggling the `dark` class in devtools before the toggle is wired)
- **Sanity changes:** None
- **Testing:** Manual — toggle `.dark` class on `<html>` via devtools, visually audit every section for contrast/readability issues
- **Estimated impact:** Every section (global design system change)
- **Rollback:** Remove the new light-mode CSS block; site remains dark-only (current behavior)

### Task 4.8 — Light-mode text-color audit
- **File(s):** Every component using `text-white/*` utility classes (large, cross-cutting — expect touches across most `src/components/sections/*.tsx` and `src/components/**/*.tsx` files)
- **Change:** Systematic pass adding `dark:text-white/NN` + a light-mode equivalent (e.g., `text-slate-800/NN`) wherever a bare `text-white/*` class exists, OR — simpler — define the text-color tokens as CSS variables consumed via a small number of shared utility classes rather than hundreds of inline Tailwind opacity variants (architectural call to make during implementation, not fully resolved in design doc)
- **Dependencies:** Task 4.7
- **Sanity changes:** None
- **Testing:** Full visual regression pass across every section in light mode; this is the highest-risk task in the entire fix-pass per the design doc's explicit flag — budget real QA time here, not just a spot-check
- **Estimated impact:** Every section, site-wide
- **Rollback:** Ship dark-mode-only (skip Tasks 4.6–4.8 entirely) if this audit proves too large for the current pass — **acceptable fallback**, flag to user if scope needs to be cut

### Task 4.9 — Footer polish pass
- **File(s):** `src/components/Footer.tsx`
- **Change:** Add a subtle `useSpaceFloat`-driven ambient touch (low radius, e.g. `radius: 2`) to the glyph/copyright elements; specific visual enhancement (gradient, iconography) to be decided during implementation per design doc
- **Dependencies:** None
- **Sanity changes:** None
- **Testing:** Visual check — confirm footer still reads cleanly, 3-column structure intact, back-to-top button still functions
- **Estimated impact:** Footer, all pages
- **Rollback:** Remove the `useSpaceFloat` wrapper; footer reverts to fully static (current behavior)

---

## Phase 5 — Polish & Testing

### Task 5.1 — Responsive testing pass (mobile/tablet/desktop)
- **File(s):** N/A — testing task across all changed components
- **Change:** Manually verify every fix area at 320px, 375px, 390px, 768px, 1280px, 1440px
- **Dependencies:** All Phase 1–4 tasks for the areas being tested
- **Testing approach:** Manual device/emulator pass; leverage existing `e2e-screenshots/` infrastructure if it supports capturing new screenshots at these breakpoints
- **Estimated impact:** Whole site
- **Rollback:** N/A

### Task 5.2 — Animation performance pass
- **File(s):** `src/components/three/ObsidianBackgroundCanvas.tsx`, `src/components/three/ProjectsSlider.tsx`, `src/components/orby/OrbyModel.tsx`
- **Change:** Profile the new scatter-intro, auto-play carousel, and Orby pose-cycling for frame drops on a mid-tier mobile device (Chrome DevTools Performance tab or real device); adjust point counts/interval timings if jank is observed
- **Dependencies:** Tasks 2.3, 2.4, 3.4, 4.5
- **Testing approach:** DevTools Performance recording, target 60fps sustained during scatter-intro and carousel auto-play
- **Estimated impact:** Whole site perceived smoothness
- **Rollback:** N/A (tuning task, not a revert)

### Task 5.3 — Accessibility audit
- **File(s):** All components touched in Fix Areas 2, 3, 4, 6 (interactive additions)
- **Change:** Run an automated audit (axe DevTools or equivalent) plus manual keyboard-only navigation pass across: About toggle, Telemetry cards, Chat textarea, Projects carousel auto-play pause-on-focus, theme toggle
- **Dependencies:** All Phase 1–4 tasks
- **Testing approach:** axe DevTools browser extension + manual Tab-key navigation + screen reader spot-check (VoiceOver/NVDA) on the new interactive elements
- **Estimated impact:** Whole site, focused on new interactive elements
- **Rollback:** N/A — flag any failures found as follow-up bugfix tasks rather than blocking this note

### Task 5.4 — Cross-browser smoke test
- **File(s):** N/A
- **Change:** Verify the R3F-heavy sections (background, Education flowchart) and the new light-mode CSS render correctly in Chrome, Firefox, Safari
- **Dependencies:** All prior phases
- **Testing approach:** Manual smoke test in each browser; pay particular attention to `backdrop-filter` support (used pervasively in `.cosmic-card`) and WebGL context creation on Safari
- **Estimated impact:** Whole site
- **Rollback:** N/A

### Task 5.5 — Final verification: full build pipeline
- **File(s):** N/A
- **Change:** Run `pnpm typegen && pnpm typecheck && pnpm lint && pnpm test && pnpm build` in sequence; fix any errors surfaced
- **Dependencies:** All prior tasks
- **Testing approach:** CI-equivalent local run
- **Estimated impact:** Whole site — release gate
- **Rollback:** N/A — this is the final gate before considering the fix pass complete

---

## Task Dependency Summary

```
Phase 1 (Sanity) ──┬─→ Task 2.5 (About split) ─→ Task 2.6 (toggle) ─→ Task 2.7 (telemetry expand)
                    └─→ Task 2.7 (telemetry — needs summary field)

Task 2.3 (scatter-intro) ─→ Task 2.4 (click scatter/rejoin, shares visual language)

Task 3.1 (textarea) ─→ Task 3.2 (length cap/indicator)
Task 3.3 (mobile repro) — independent, informs any follow-up fix

Task 3.4 (auto-play) ─→ Task 3.5 (pause/reduced-motion)
Task 3.6 (slug cleanup) — independent

Task 3.7 (year range) — needs user confirmation first
Task 3.8 (effect reduction) — needs user confirmation first
Task 3.9 (spacing) — independent

Task 4.3 (backend) ─→ Task 4.4 (frontend hook)
Task 4.1, 4.2, 4.5 — independent, all touch OrbyModel.tsx/Orby.tsx (sequence to avoid merge conflicts)
Task 4.7 (light tokens) ─→ Task 4.6 (toggle wiring, can ship before 4.7 for dev/testing) ─→ Task 4.8 (text audit)
Task 4.9 — independent

Phase 5 — depends on all prior phases; Task 5.5 is the final gate
```

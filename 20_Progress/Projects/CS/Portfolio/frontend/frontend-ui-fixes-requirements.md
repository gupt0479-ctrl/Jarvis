---
type: concept
status: active
created: 2026-07-11
tags:
  - portfolio
  - frontend
  - ui-fixes
  - requirements
notes:
  - "[[frontend-ui-fixes-design]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[UI Fixes]]"
  - "[[BUILD-STATUS]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Frontend UI Fixes — Requirements

> Source of truth for the portfolio UI overhaul. Companion docs: [[frontend-ui-fixes-design]] and [[frontend-ui-fixes-tasks]] in this folder.
> Source brief: [[UI Fixes]] (Anant's dictated notes + screenshots, 2026-07-11).
> Every claim below was verified by reading the live component in `src/components/` on the `portfolio` repo — file paths are exact, not inferred.

## Glossary

| Term | Meaning |
|---|---|
| Lab / Portfolio Lab | The right-side chat sidebar (`src/components/lab/PortfolioLab.tsx`), powered by `/api/chat` |
| Orby | The floating astronaut companion (`src/components/orby/`), NOT the chat itself |
| Blast radius | The invisible sphere-click hit area in the hero/scroll background (`ObsidianBackgroundCanvas.tsx`, `PLANET_RADIUS * 1.1`) |
| Comet effect | The 3D tilt-on-hover wrapper (`src/components/ui/comet-card.tsx`), 4 variants: `default`, `dark`, `subtle`, `ghost` |
| Space float | Continuous zero-gravity drift applied via `useSpaceFloat` hook |
| Capability graph | The SVG line-chart in Skills section (`SkillsCapabilityGraph.tsx`) |
| Deformity | `MeshDistortMaterial.distort` value on the Education blobs — 0 = perfect sphere |

## Executive Summary

The portfolio is functionally complete but eight areas fall short of a polished first impression and coherent interaction model: the hero is static/lifeless on load, the About section is too long, the 4 telemetry stat boxes are static, the Lab sidebar breaks on small phones and has no visual feedback for message length, the Projects carousel loops through too many items with no auto-play at all, Skills/Education have flat or under-differentiated visuals, and Orby, dark mode, and the footer are all under-built relative to the surrounding polish. None of these are Sanity data gaps — they are UI/animation/interaction gaps in existing, already-wired components.

---

## Fix Area 1 — Landing Hero & Background Particle System

**Components:** `src/components/sections/HeroSection.tsx`, `HeroContent.tsx`, `ProfileImage.tsx`, `HeroTerminal.tsx`, `src/components/three/ObsidianBackgroundCanvas.tsx`

### Problem Statement
1. The profile image area currently animates in with `scale: 0.96 → 1` (`HeroContent.tsx`, motion.div wrapping `ProfileImage`) — read by users as "moving around" rather than a static presence. There is no directional light-wave/comet sweep over the photo itself.
2. `HeroTerminal.tsx` renders a floating terminal window directly below the hero with a continuous `cosmic-drift` CSS animation (18s loop, `translate` up to 50px in any direction — defined in `globals.css`). This is the "wiggle effect" flagged as unnecessary.
3. On page load, `ObsidianBackgroundCanvas.tsx` renders the sphere already fully formed (`fibonacciSphere` positions are the literal starting state — there is no scatter-in animation). The scroll-driven "dent" physics only begin reacting past 40% scroll (`stretchT` gate), so the first viewport is visually static aside from ambient jitter (`BASE_DRIFT`).
4. There is no "scatter apart → converge into sphere" entrance sequence, and no click-triggered scatter/rejoin tied to a "blast radius" perimeter distinct from the existing click-burst (`BURST_STRENGTH`, a radial ripple wave only — not a full scatter/reform).

### User Impact
First-time visitors see a comparatively flat, non-eye-catching entry point; the site "gets better as you scroll," which is the opposite of ideal first-impression sequencing for a recruiter with a short attention budget. The terminal's continuous drift consumes visual attention without adding information, and duplicates identity/stack info already stated in `HeroContent.tsx`'s headline + short bio.

### Success Criteria
- Profile image container has zero ambient motion after its one-time entrance; a single subtle light-sweep (comet-style, shallow depth, similar to `CometCard variant="ghost"`) plays across the image, not a full 3D tilt-on-hover interaction.
- `HeroTerminal.tsx` is removed from the render tree in `PortfolioContent.tsx` (file kept, not deleted, per source brief: "we're not deleting the file, but we're just removing it for now").
- On initial mount, the background sphere's points visibly start scattered (random offset from their `fibonacciSphere` rest position) and animate into the current formed-sphere state over a slow, one-time intro (2–4s), before the existing scroll-reactive physics take over.
- Clicking inside the sphere's blast-radius perimeter (existing invisible hit-mesh, `PLANET_RADIUS * 1.1`) triggers a scatter → rejoin animation using the same visual language as the load-in scatter, scaled to the current camera zoom/scroll position — not just the existing radial burst wave.

### Content Dependencies
None — pure animation/behavior change. Profile image and headline continue to come from `PROFILE_QUERY` (`src/sanity/lib/queries.ts`).

### Responsive Considerations
- Mobile already halves `PLANET_COUNT`/`RING_COUNT`/`STAR_COUNT` (`useIsMobile`) and skips post-processing (`skipEffects`). The scatter-intro and click-scatter must respect this same mobile point-count reduction and must be skipped or shortened under `prefers-reduced-motion` (existing `useReducedMotion` hook already present in the canvas).
- The comet-sweep on the profile image must not shift `ProfileImage`'s layout box on any breakpoint (it's `hidden lg:flex` today — desktop-only element).

### Accessibility Notes
- The intro scatter-to-sphere animation is decorative canvas content (`aria-hidden` scene) — no ARIA changes needed, but it MUST branch off `prefers-reduced-motion` the same way `REDUCED_PULL_STR`/`REDUCED_MAX_DISPLACE` already branch scroll physics (render the sphere already formed, no motion).
- Removing `HeroTerminal` removes redundant, non-essential decorative text — confirmed nothing else references the `~/anant` terminal text for AT users.

### Behavioral Flow (Before → After)
- **Before:** Page loads → sphere already formed and jittering gently → terminal wiggles below hero → user must scroll to see any real motion payoff.
- **After:** Page loads → points visibly scattered around the sphere's future position → they converge into the familiar formed sphere over ~2–4s → terminal is gone → profile image has a single static comet-light sweep → clicking the sphere at any scroll position re-triggers a scaled scatter/rejoin.

---

## Fix Area 2 — About Me Section (Collapsible Toggle + Summary)

**Components:** `src/components/sections/AboutSection.tsx`, `src/components/AboutTelemetry.tsx`

### Problem Statement
`AboutSection.tsx` renders `profile.fullBio` (a Sanity Portable Text array) in full, uncollapsed, inside a `CometCard variant="ghost"`. There is no toggle, no short-form summary, and no expand/collapse state. The section can run to a full screen or more of prose even before scrolling to the 4 stat cards below it.

### User Impact
Visitors get a wall of text before reaching anything interactive; the section reads as "About Me" homework rather than a quick scan, contradicting its own kicker copy ("// scan report" / "A quick system scan.").

### Success Criteria
- Default (collapsed) state shows a distinct 3–4 sentence summary — not a truncated slice of `fullBio`, but purpose-written short content — occupying roughly one viewport height including the kicker/heading.
- A visible toggle control expands the section to reveal the existing full `fullBio` Portable Text content in place; toggling back re-collapses without a page jump (scroll position anchored to section top).
- All content inside the collapsed state must remain clickable/interactive per the source brief ("Everything should be clickable in the About Me section") — at minimum the 4 telemetry stat cards below remain reachable and interactive when collapsed.

### Content Dependencies
New Sanity field required: a short-form summary (3–4 sentences) distinct from `shortBio` (already used in the Hero) and `fullBio` (long-form, used here today). Recommend `profile.aboutSummary` (`text`, ~2–3 sentence validation) added to `src/sanity/schemaTypes/profile.ts`, projected in the existing `ABOUT_QUERY` in `AboutSection.tsx`. `profile.stats[]` (existing field, already wired to `AboutTelemetry`) is unaffected.

### Responsive Considerations
- Collapsed height target (~1 viewport) must hold on mobile (375px width) without the toggle control being pushed below the fold.
- Toggle hit target must meet the existing 44px minimum already used elsewhere in the codebase (e.g., `ProjectsSlider` nav buttons: `min-w-[44px] min-h-[44px]`).

### Accessibility Notes
- Toggle must be a real `<button>` with `aria-expanded` reflecting state (pattern already used correctly in `ExperienceCard.tsx`'s more/less toggle — reuse that pattern).
- Portable Text content must remain in the DOM (not conditionally unmounted after first render — animate height like `ExperienceCard`'s `AnimatePresence`/`height: auto` pattern) so screen readers relying on heading navigation aren't broken by content visibility.

---

## Fix Area 3 — Interactive Content Boxes (4-Box Telemetry Section)

**Components:** `src/components/AboutTelemetry.tsx`

### Problem Statement
The 4 `TelemetryCard` components render a static icon, value, label, and decorative sparkline (`SPARKLINE_BARS`, a fixed 5-bar shape — not data-driven). They are not clickable; hover only triggers a CSS color/scale transition. The source brief asks for these to become clickable, each revealing a small graph plus a summary about the specific stat.

### User Impact
The cards read as decorative widgets rather than earning their real estate; a recruiter skimming for evidence has no way to drill into what a stat like "10+ Projects" actually means.

### Success Criteria
- Each of the 4 cards is a real interactive control (button or equivalent) with a visible affordance (hover/focus state already present via `hover:border-[rgba(167,139,250,0.35)]` — extend, don't replace).
- Clicking a card reveals a small graph (reusing the existing SVG line-chart approach from `SkillsCapabilityGraph.tsx` at reduced scale, not a new Three.js scene — see design doc for the "SVG vs Three.js" decision) plus 1–2 sentences of context specific to that stat.
- Expand behavior (independent per-card vs. mutually exclusive accordion) is an open decision — flagged below, not resolved by the source brief.

### Content Dependencies
`profile.stats[]` currently only has `label` and `value` (both `string`). To render a real per-stat graph and summary, each stat needs additional fields: a short `summary` string, and a data source for the mini-graph. **Flagged for clarification:** the source brief says "this could be something like my skill section graph, but much tinier" — recommend the graph re-derive from existing `SKILLS_QUERY`/`PROJECTS_QUERY` data per stat type rather than requiring new hand-authored time-series fields, to avoid a second manually-maintained dataset. Minimum schema addition regardless of graph source: `profile.stats[].summary` (`string`, short).

### Responsive Considerations
Expanded detail view must not push the whole page layout on mobile — recommend an inline accordion-style expand (matching `ExperienceCard`'s `AnimatePresence height:auto` pattern) rather than a modal/popover that could clip on narrow viewports.

### Accessibility Notes
- Must use `<button>` semantics with `aria-expanded` per card, matching the pattern established in Fix Area 2's About toggle for consistency.
- Sparkline/graph SVGs need `role="img"` + `aria-label` describing the trend in words (pattern already used in `SkillsCapabilityGraph.tsx`).

---

## Fix Area 4 — Portfolio Lab / Orby Sidebar (Chat UX & Responsiveness)

**Components:** `src/components/lab/PortfolioLab.tsx`, `ChatInputBar.tsx`, `ChatThread.tsx`, `src/components/ui/sidebar.tsx`

### Problem Statement
1. `src/components/ui/sidebar.tsx` sets `SIDEBAR_WIDTH_MOBILE = "100%"` — on phones the Lab sidebar is full-viewport-width. `ChatInputBar.tsx` renders the send button (`h-7 w-7`, `<Send>` icon) at the end of a flex row with a `flex-1` input — this itself is a safe, contained flex layout and should not overflow by inspection. The reported bug ("send button gets outside the phone, have to zoom out") indicates the issue is elsewhere in the sidebar's outer container sizing on specific small viewports, not necessarily in `ChatInputBar` itself — **needs direct on-device verification before assuming root cause**, flagged in Open Questions.
2. `ChatInputBar.tsx` uses a single-line `<input type="text">` with no character counter, no multi-line growth, and no cap — contradicts the source brief's request for a growing textarea (up to 3 lines) with a visible length indicator.
3. `<input>` elements support native cursor left/right arrow-key navigation by default; the reported "cursor movement not working" bug is likely a symptom of the current single-line `<input>` combined with some interaction elsewhere — **root cause unverified, flagged for direct reproduction before fix.**
4. Neither `ChatThread.tsx` nor `PortfolioLab.tsx` enforces message length — arbitrarily long/gibberish input is sent as-is to `/api/chat`, consuming model-router quota (`src/lib/model-router.ts`) before Orby's canned fallback ever engages.

5. **Confirmed gap (screenshot-verified):** `ChatThread.tsx`'s user-message bubble renders `{msg.text}` inside a plain `<div className="ml-auto max-w-[80%] rounded-xl px-3 py-2 ...">` with no `break-words`/`overflow-wrap` utility applied. An unbroken string with no spaces (e.g., the gibberish test string in the source brief) overflows the bubble's `max-w-[80%]` constraint horizontally instead of wrapping, producing a horizontal scrollbar in the chat thread panel — visible directly in both embedded screenshots accompanying the gibberish-test paragraph (see `Pasted image 20260711204507.png` and `Pasted image 20260711204540.png`). The assistant-message bubble (rendered via `ReactMarkdown`'s `p` component in `MARKDOWN_COMPONENTS`) also lacks an explicit wrap override in its own class list, but assistant replies are natural-language sentences with spaces, so the bug has not visibly triggered there in the screenshots — this is a difference in typical *content*, not a confirmed difference in CSS between the two bubble types.

### User Impact
On mobile, users may be unable to comfortably compose messages; on all devices, users get no feedback about how much room they have before hitting a length constraint, and can send unbounded gibberish that the backend silently absorbs.

### Success Criteria
- Verified layout: input bar and send button remain fully on-screen and tappable without horizontal scroll/zoom on a 320–375px wide viewport (iPhone SE class), with the sidebar at its mobile 100% width.
- Input control grows from 1 line up to a 3-line cap as the user types, matching the source brief's spec; beyond the cap, the box becomes internally scrollable instead of growing further.
- A visible character/length indicator appears as the user approaches the cap.
- Left/right arrow-key and click-to-position cursor movement is confirmed working in the shipped textarea component (default browser behavior for `<textarea>`; success criteria is "does not regress" once the component moves from `<input>` to a growable `<textarea>`).

- Long unbroken strings (no whitespace to break on) wrap within the user-message bubble in `ChatThread.tsx`; no horizontal scrollbar appears in the chat thread panel regardless of input length (see `Pasted image 20260711204507.png`, `Pasted image 20260711204540.png`).

### Content Dependencies
None — pure UI component change. `/api/chat` already accepts arbitrary-length `messages[].content` strings.

### Responsive Considerations
This fix area is responsive-first by definition. Test matrix: 320px, 375px, 390px (per `Orby.tsx`'s own `vw <= 390` narrow-phone branch, showing the codebase already tracks this breakpoint elsewhere), and desktop at the fixed 400px (`25rem`) sidebar width.

### Accessibility Notes
- Growable textarea must retain a proper `<label>` or `aria-label` (the current `<input>` has only a `placeholder`, which is not a substitute for a label — carry this forward as a fix, not just parity).
- Any character-limit indicator should use `aria-live="polite"` only near the limit — avoid constant screen-reader chatter.

---

## Fix Area 5 — Experience Section (Content Wrapping + Truncation)

**Components:** `src/components/sections/ExperienceSection.tsx`, `src/components/cards/ExperienceCard.tsx`

### Problem Statement
The source brief states the UI for this section is already correct ("UI-wise, actually, it's perfect") and the remaining problems are (a) content quality — summary/bullets/achievements need to read better, a content/copywriting task, not a UI task — and (b) unbounded summary length inside each card, which can overflow the card without a hard visual stop. `ExperienceCard.tsx` today renders `responsibilities` (max 3, sliced) and `achievements` (max 2, sliced) as full-text `<li>` items with no `line-clamp`, and the expandable `description` (Portable Text) has no clamp either.

### User Impact
Long entries make cards visually inconsistent in height across the section and can push the "more/less" toggle far down, weakening scannability.

### Success Criteria
- Each experience card's collapsed-state summary content (responsibilities/achievements) has a hard visual line-clamp so no card's default height varies wildly due to content length alone.
- The expandable `description` block, when opened, is allowed to be longer but should have a sane max height with internal scroll for extreme entries.
- Actual wording of `responsibilities[]`/`achievements[]`/`description` content is out of scope for this UI-fix pass — flagged as a content/copywriting task via Sanity Studio, not code.

### Content Dependencies
No schema changes. This is a rendering-constraint fix on existing `EXPERIENCE_QUERY` fields.

### Responsive Considerations
Line-clamp values may need to differ by breakpoint (e.g., 2 lines on mobile, 3 on desktop) since effective characters-per-line changes with card width.

### Accessibility Notes
Compatible with the existing expand mechanism as long as the clamp only ever applies to the *collapsed* summary bullets, never to the fully expanded description.

---

## Fix Area 6 — Projects Carousel (Loop Limit + Navigation)

**Components:** `src/components/three/ProjectsSlider.tsx`, `src/lib/chat-tools.ts` (navigate/showProject tools), `src/sanity/schemaTypes/project.ts`

### Problem Statement
1. `ProjectsSlider.tsx` has no auto-rotation today — it is fully manual (arrow buttons, drag, dot-click, keyboard arrows). The source brief's ask — "only auto-roll the first 3 projects, but let the user see there are 9 and click through" — requires *adding* an auto-advance behavior scoped to indices 0–2, while preserving full manual navigation to all 9.
2. The chat-driven navigation tool `navigate` (in `chat-tools.ts`) already emits `itemSlug` for the projects section, and `ProjectsSlider.tsx` already listens for `orby:navigate` and does a slug-based lookup — this mechanism is architecturally sound. The source brief's complaint that "the chatbot can't seem to go to the exact project number" points to either (a) the model not reliably passing the correct slug in tool calls, or (b) `PROJECTS_QUERY`'s `slug{current}` shape mismatching the client-side lookup's `typeof p.slug === "string"` branch — the query always returns an object `{current}`, so that string-typed branch in `ProjectsSlider.tsx` is likely dead code, worth confirming as a latent bug.

### User Impact
With 9 projects and no auto-advance, the section is currently just a manual carousel — the source brief's stated user problem ("too many projects and too many buttons to click") stands.

### Success Criteria
- On mount (and after any idle period following manual interaction), the carousel auto-advances index 0 → 1 → 2 → back to 0, never automatically advancing into indices 3–8.
- The existing "X / 9" counter, dot indicators, and manual arrow/drag/keyboard navigation continue to allow reaching any of the 9 projects at any time; manual interaction pauses auto-play.
- Chat-driven navigation to a specific project reliably lands on that exact project every time, with the slug-shape bug (if confirmed) fixed so the lookup path is not silently dead.

### Content Dependencies
No schema changes required. `PROJECTS_QUERY` already returns all fields needed (`slug{current}`, `order`, `featured`).

### Responsive Considerations
Auto-play should respect `prefers-reduced-motion` (currently not checked anywhere in `ProjectsSlider.tsx`) — reduced-motion users get a static carousel with manual navigation only.

### Accessibility Notes
- Auto-advancing content must pause on hover/focus at minimum (WCAG 2.2.2 applies) — pausing on any manual interaction, as specified above, satisfies this if it also pauses on keyboard focus entering the carousel.
- Existing `aria-label`/`aria-current` semantics on nav buttons and dots are already correct and should be preserved unchanged.

---

## Fix Area 7 — Skills & Education Sections (Animations + Spacing)

**Components:** `src/components/sections/SkillsSectionClient.tsx`, `SkillsCapabilityGraph.tsx`, `src/components/EducationFlowchart.tsx`, `src/app/globals.css` (`.section-pad`)

### Problem Statement — Skills
1. `SkillsCapabilityGraph.tsx`'s `YEARS` array starts at `"2021"` — the source brief explicitly wants the graph to start at 2022.
2. `CATEGORY_SHAPES` defines each category's first-year value via `startFloor` (e.g., `frontend.startFloor = 18`) — several categories' *pattern-scaled* first-year value can exceed the "no skill above 35 at the starting point" ceiling the source brief specifies, once recalculated for a 2022 start.
3. `SkillPill` implements 7 distinct hover effects selected by `effectIndex % 7` — the source brief calls these "laggy" and "not eye-pleasing." No expensive re-renders were found in the code (effects are CSS `transition`/`animation` driven) — this is a design-quality complaint about the chosen effects, not a measured performance bug.

4. **Confirmed gap — category-chip effects are a separate, unaudited component.** The dictated transcript makes two distinct complaints: "very limited types of effects... on each and every single skill" (individual skill tags) and, separately, "the skill category UI effects almost seem to be laggy" (the filter chips labeled e.g. "Ai Ml 7", "Backend 8", "Cloud 6" sitting above the graph/grid). These are two different components in the code: individual skill tags are `SkillPill` (already audited above, 7 effects via `effectIndex % 7`); the category filter row is a separate `CategoryPill` component, also defined inline in `SkillsSectionClient.tsx`, rendered by `SkillsFilter`. `CategoryPill` has its own independent hover-effect system — a `k === "frontend"` shimmer sweep, `k === "mobile"` expanding ring overlay, `k === "backend"` blinking cursor, `k === "tools"` terminal-prompt blink, `k === "devops"` sequential deploy-dots, `k === "database"`/`"data-systems"` sparkline bars, `k === "testing"` sequential checkmarks, `k === "cloud"` floating micro-dots, `k === "academic"` an orbiting star dot, plus a `useSpaceFloat`-driven continuous ambient drift on every pill regardless of hover state. This is a materially larger and more varied effect system than `SkillPill`'s — 9+ distinct category-specific animations layered on top of continuous drift, versus `SkillPill`'s 7 effects with no continuous drift. Nothing in the current design.md distinguishes these two components; treating them as one paragraph would understate the scope of the "laggy" complaint, since the category row's continuous `useSpaceFloat` drift plus a hover-triggered animation running simultaneously is a more plausible source of a "laggy" feel than `SkillPill`'s effects alone.

### Problem Statement — Education / Certifications spacing
The source brief calls out excess padding between Education and the sections immediately above/below it (per render order in `PortfolioContent.tsx`: Skills → Education → Certifications). Both sections use the shared `section-pad` utility (`padding-block: var(--section-pad-y)` = `5rem` both sides) with no section-specific override — the "too much gap" is a `--section-pad-y` tuning issue at these two boundaries specifically, not a structural layout bug.

### User Impact
The Skills section's core pitch — "watch capability grow over time" — is undermined by starting the timeline a year earlier than intended and by category lines potentially starting implausibly high. Excess whitespace around Education breaks the narrative continuity the flowchart is building (middle school → high school → bachelor's).

### Success Criteria — Skills
- Graph X-axis reads either `2022–2026` (drop 2021, 5 points) or a forward-shifted `2022–2027` (6 points) — **flagged for clarification**, see Open Questions.
- No category's first plotted year value exceeds 35 on the 0–100 Familiarity/Applied Depth axis.
- Skill-pill and category-pill hover effects are visually cohesive and smooth, with variety reduced if that is what "cleaner" is confirmed to mean during design.

- `CategoryPill`'s effect variety is reduced and its continuous ambient drift (`useSpaceFloat`) is reconsidered independently from `SkillPill`'s fix — do not assume the same "keep 3 of N" prescription applies identically to both components, since `CategoryPill`'s baseline (continuous drift + hover effect) is architecturally different from `SkillPill`'s (hover-only, no drift).

### Success Criteria — Education/Certifications spacing
Vertical gap between Certifications and Education, and between Skills and Education, is visually tightened relative to current `5rem`/`5rem` — target value set in the design doc after a visual pass (likely a `--section-pad-y` override scoped to only these two boundaries, since global `section-pad` is used everywhere else).

### Content Dependencies
None. All changes are constants/CSS in existing components; no Sanity schema impact (`skill.percentage` already exists and already drives `avg` in `buildCategoryData`).

### Responsive Considerations
Verify axis label legibility at narrow widths after any year-range change (more/fewer tick labels can crowd the 42%-width sidebar layout on tablet breakpoints).

### Accessibility Notes
No change to existing `role="img"`/`aria-label` on the graph SVG regardless of tick-count changes.

---

## Fix Area 8 — Character & Global Features (Orby, Dark Mode, Footer)

**Components:** `src/components/orby/OrbyModel.tsx`, `Orby.tsx`, `useOrbyState.ts`, `src/components/HeaderScrolling.tsx`, `src/components/ThemeProvider.tsx`, `src/components/Footer.tsx`

### Problem Statement — Orby
1. `OrbyModel.tsx`'s "radio" is a plain 6×10px rounded rectangle with no antenna and no visual read as a radio — matches the source brief's "just a purple thing" complaint exactly.
2. The wave animation exists (`pose === "wave"` triggers `rotate: [0, -25, 0, -25, 0]` on the right arm) but only reaches -25°, not a full arm-raise; the source brief wants a visible hand-lift to say hi.
3. Orby's speech content is a fixed, hand-written copy bank (`INTRO_COPY`, `LAB_HINT_COPY`, `SECTION_COPY`, `GOODBYE_COPY` in `useOrbyState.ts`) plus model-generated `orbyMessage` strings that only arrive as a side effect of an active chat tool-call flow. There is currently **no standalone AI-generated commentary independent of an active chat turn** — i.e., Orby cannot "drop funny comments" on its own while a user scrolls/clicks without a chat message having been sent first. This is a new capability, not a bug fix.
4. Orby's roaming state already does orbit + drift as it slides with scroll (`orbitRx`/`orbitRy` up to 22px on desktop) — the source brief's "all it does is slide/zoom" complaint suggests the *perceived* motion should be richer (more distinct action states — walking, radio-talking, idle-hover) rather than one continuous orbit-drift blend.

### Problem Statement — Dark Mode
`HeaderScrolling.tsx`'s theme button is fully inert: `onClick={() => { /* light mode not yet designed */ }}`, with `cursor-default` and an `aria-label` that literally states "light mode coming soon." `ThemeProvider.tsx` wraps `next-themes` with `defaultTheme="dark"` and `enableSystem` — the plumbing exists, but no light theme token set exists in `globals.css`; the cosmic design system classes (`.cosmic-card`, `.orbit-chip`, `.section-kicker`, etc.) are all hardcoded to dark RGBA values with no light-mode split.

### Problem Statement — Footer
`Footer.tsx` is a minimal 3-column grid (glyph / back-to-top / copyright) with a top border gradient — functionally complete and on-brand, but the source brief calls it under-designed.

### User Impact
Orby currently reads as a scroll-reactive prop rather than a "living" character, undercutting a stated differentiator. The dark-mode toggle actively misleads users into believing a working feature exists. The footer, while clean, doesn't carry the same personality established everywhere else in the design system.

### Success Criteria — Orby
- Radio prop redesigned with a visually distinct antenna element and clearer device silhouette.
- Wave animation reaches a full arm-raise, easing adjusted to read as intentional greeting.
- New AI-driven idle commentary capability: Orby can speak a short, model-generated line independent of an active chat send, triggered by scroll dwell time or click, reusing the existing model-router chain (`src/lib/model-router.ts`) — not a new provider integration, but a new server action/route generating one short line on demand.
- Roaming state gets at least 2 additional distinguishable visual sub-states so movement doesn't read as one continuous slide.

### Success Criteria — Dark Mode
The toggle becomes a real, working control. Given the source brief's framing ("should not exactly be white"), the deliverable is a genuine second theme (inverted-but-not-pure-white) wired through `next-themes`, not a no-op removed entirely. All cosmic design-system classes need light-mode counterparts, or an explicit light token layer.

### Success Criteria — Footer
Footer visual treatment upgraded (direction deferred to design doc) while preserving the existing 3-column semantic structure and `<button>`-based back-to-top control.

### Content Dependencies
Orby's AI commentary needs no new Sanity fields — it can be grounded via the existing `CHAT_CATALOG_QUERY` context or ungrounded flavor text (**flagged for clarification**, see Open Questions). No schema changes for dark mode or footer.

### Responsive Considerations
- Orby's new commentary triggers must not fire more aggressively on mobile where the speech-cloud width is already tightly clamped (reuse existing clamping logic in `Orby.tsx`'s RAF loop).
- Light mode must be tested against the same 375px/768px/1440px breakpoints as dark mode, particularly around `ObsidianBackgroundCanvas` (hardcoded dark-space colors today — needs either a light-mode palette variant or an explicit decision to keep the 3D background dark-only regardless of theme).

### Accessibility Notes
- A functioning toggle must update `aria-label` dynamically (today's label is static and describes the non-functional state).
- Orby's AI commentary must remain `aria-hidden`, consistent with the entire existing Orby component tree.

---


---

## Fix Area 7b — Education Deformity Sequencing & Bachelor's Highlight (confirmed gap)

**Components:** `src/components/EducationFlowchart.tsx`

### Problem Statement
The dictated transcript describes a specific, load-bearing requirement that no existing fix area covers: as the user lands on the Education section, the node "deformity" should trace a path — Middle School most deformed, High School in between, Bachelor's in Computer Science at 0 deformity (a solid sphere) — with the transition itself being animated and "UI-pleasing." The transcript also separately states Bachelor's is "not highlighted at all" and needs distinct color/background contrast.

Verified against the live code: `EducationFlowchart.tsx` already defines `const DISTORT = [0, 0.42, 0.68] as const;`, indexed against `BASE_POS`'s own comment (`[0]=college, [1]=high-school, [2]=middle-school`, sorted descending by `startDate`). This means the *end-state* hierarchy the transcript describes already exists as static per-node values — Bachelor's (`idx 0`) is `distort: 0` (solid sphere), High School (`idx 1`) is `0.42`, Middle School (`idx 2`) is `0.68` (most deformed). `DISTORT_SPEED = [0, 2.0, 3.5]` similarly scales the *ongoing* distortion animation speed per node, not a one-time entrance sequence. `TravellingDot` (a separate glowing sphere) already loops continuously middle→high→college along `StretchingLine` connectors, but this is a decorative, infinitely-looping dot — it is not tied to the blobs' own distort values, and does not drive any transition in the blobs themselves. **There is no code that sequences the distort values themselves on section entry** — the blobs render at their final `DISTORT` values immediately on mount, with no scroll-into-view or on-mount transition from a shared starting deformity down to their individual targets. The earlier design.md claim that "`EducationFlowchart.tsx`'s scene is untouched by this fix pass" is incorrect now that this gap is confirmed — this file requires a targeted addition (not a rewrite).

On the Bachelor's-highlight complaint: `BLOB_COLOR`/`BLOB_EMIT`/`BLOB_EMIT_I` already assign each node a distinct color (college: `#7c3aed`/`#a78bfa`/emissive intensity `2.0` — the *highest* emissive intensity of the three), which suggests some differentiation already exists in code, contradicting the transcript's "not highlighted at all" framing. This discrepancy is most plausibly explained by the *shape* difference being the dominant visual signal today — a perfect solid sphere (Bachelor's) can read as visually "flatter"/less eye-catching than a busier, more organic-looking deformed blob (Middle School), even with a higher emissive intensity, especially since deformity and emissive glow are visually competing signals rather than reinforcing ones. This is a plausible explanation grounded in the actual constants, not a confirmed root cause — flag as informed hypothesis, not fact, until visually verified against the actual rendered page.

### User Impact
Without a sequenced entrance animation, the Education section's core narrative device (an academic journey visualized as decreasing deformity) is invisible — a first-time viewer sees three static blobs with different levels of "wobbliness" but no visual story connecting them. Without a stronger highlight treatment, the Bachelor's node — the most important credential on the page — does not read as more significant than Middle School.

### Success Criteria
- On section entry (scroll-into-view, matching the `whileInView` convention used elsewhere in the codebase per the steering rules), each blob's `distort` value animates from a shared "high deformity" starting point down to its final target (`0` for Bachelor's, `0.42` for High School, `0.68` for Middle School) over a short, clean transition — not an instant snap to the final `DISTORT` array values.
- The transition plays once per section visit (not on every frame, and not replaying on every scroll direction change) and is visually smooth ("UI-pleasing," per the transcript, meaning no popping/stuttering between deformity states).
- Bachelor's in Computer Science receives an additional, distinct visual treatment beyond its already-differentiated `BLOB_COLOR`/`BLOB_EMIT_I` values — options include a background glow/halo behind the solid sphere, a stronger border/rim-light effect, or a size increase relative to the other two nodes — resolved during design, not fully specified by the transcript.
- Existing behavior is preserved: `TravellingDot`'s continuous loop, `StretchingLine` connectors, logo clip-paths per node, and `EduCard` info panels are unaffected by this fix.

### Content Dependencies
None — this is a pure animation/visual-treatment fix on existing `DISTORT`/`BLOB_COLOR`/`BLOB_EMIT` constants and the `EduBlob` component's render logic. No Sanity schema or query changes.

### Responsive Considerations
`EducationFlowchart.tsx` already branches on `prefersReduced` (via `window.matchMedia("(prefers-reduced-motion: reduce)")`, checked once in the parent `EducationFlowchart` component and passed down as a prop) — the new entrance sequencing must skip directly to final `distort` values when `prefersReduced` is true, consistent with how `DISTORT_SPEED` already zeroes out (`speed={prefersReduced ? 0 : DISTORT_SPEED[idx]}`) under the same flag. No new breakpoint logic needed — the R3F `Canvas` here has no separate mobile/desktop point-count branching (unlike `ObsidianBackgroundCanvas.tsx`), so the sequencing timing does not need device-tiering.

### Accessibility Notes
Purely decorative 3D content, no ARIA impact. Must respect `prefers-reduced-motion` per the Responsive Considerations above — this is already the dominant accessibility mechanism for this component and the new sequencing must plug into the same existing flag rather than introduce a second one.

### Behavioral Flow (Before → After)
- **Before:** Education section scrolls into view → all three blobs are already at their final, static distort values → `TravellingDot` loops decoratively but disconnected from any blob-level story.
- **After:** Education section scrolls into view → all three blobs briefly share a similarly high deformity → over a short, clean transition, each blob settles into its final distort value (Bachelor's fully resolving to a solid sphere) → Bachelor's carries an additional highlight treatment that reads clearly as the most significant node → `TravellingDot`'s existing loop continues unchanged, now reinforcing rather than contradicting the sequencing narrative.

## Open Questions (must resolve before design doc is finalized)

1. **Fix Area 3 — Telemetry accordion vs. independent expansion.** **RESOLVED — accordion (mutually exclusive).** Verified against `SkillsSectionClient.tsx`'s existing `selected` state pattern (single selected category at a time, not a multi-open set) — the telemetry cards should follow the same established interaction convention already in use elsewhere in the codebase rather than introducing a second, inconsistent expand/collapse model.
2. **Fix Area 3 — Per-stat graph data source.** **PARTIALLY RESOLVED — scope corrected.** Checked `SKILLS_QUERY` and `PROJECTS_QUERY` (`src/sanity/lib/queries.ts`) directly: neither projection carries a date or time-series field, only current-state values. Re-deriving from existing data can only produce a **distribution snapshot** (e.g., a breakdown across categories/projects at a single point in time), not a true historical trend line. If a trend line is actually wanted, new hand-authored Sanity fields (e.g., yearly snapshots) are required — that is a scope increase beyond this fix pass and is NOT recommended here. Success criteria for Fix Area 3 should be worded as "snapshot visualization," not "growth over time," to match what the data actually supports.
3. **Fix Area 4 — Mobile chat bug root cause.** **STILL OPEN — cannot be resolved by code reading, rewritten as an actionable reproduction task.** This is not a "flag and move on" item; it needs a concrete repro pass before any fix is written:
   - Reproduce at three viewport widths: **320px, 375px, 390px** (iPhone SE / iPhone 12-14 / iPhone 14 Pro logical widths)
   - Test in at least one real mobile browser context, not just a resized desktop window (iOS Safari and Android Chrome if both are available; browser dev-tool device emulation as a fallback only, noted as such)
   - Capture: (a) a screenshot of the send-button/textarea layout at each width showing the overflow, (b) a screen recording or step list of the exact cursor-movement bug (what action triggers it — tap-to-position, autocomplete, keyboard dismiss, etc.)
   - Record the OS/browser/version combination used for each repro
   - This reproduction output is a prerequisite input to the design doc's Fix 4 section — do not write an implementation fix based on assumptions about the cause.
4. **Fix Area 7 — Skills graph year-range (drop 2021 vs. shift to 2027).** **RESOLVED — shift forward.** Checked for conflicts against the newly-confirmed Fix Area 7b (Education deformity sequencing) and found none — the two changes touch unrelated components (`SkillsCapabilityGraph.tsx` vs. `EducationFlowchart.tsx`) with no shared state or timing dependency. Per design.md's existing recommendation: shift the window to `["2022","2023","2024","2025","2026","2027"]` (keep 6 points) rather than dropping 2021 to 5 points, since this preserves the existing 6-point cubic-bezier smoothing logic in `buildSmoothPath` and reads better for a forward-looking "growth trajectory" narrative.
5. **Fix Area 8 — Orby idle commentary groundedness.** **RESOLVED — ungrounded flavor text.** Verified against `src/lib/personas/recruiter.ts`, `src/lib/degraded-responses.ts`, and `src/app/api/chat/route.ts`: the codebase has a consistently strong anti-hallucination posture — the recruiter persona is explicitly instructed to never speculate beyond the record, degraded-mode responses use canned copy banks rather than generated text, and the chat route includes a sanitizer that strips leaked tool-call JSON before it reaches the user. Orby's new idle commentary should follow this same posture as **purely decorative flavor text** (mood/energy-based, not fact-based) rather than attempting to generate grounded claims about the portfolio's content, which would require new retrieval/grounding infrastructure out of scope for this pass.
6. **Fix Area 8 — Light-mode scope (full token system vs. inverted-but-never-white).** **RESOLVED in practice.** design.md already commits to a concrete approach: an off-white/lavender palette that never approaches pure white (`opacity: 1` white and true `#FFFFFF` backgrounds remain forbidden per the design system contract). The open item is implementation detail only — exact hex values for the light-mode token set — not the overall approach, which stands as decided.

**Summary — 4 resolved, 1 resolved-with-scope-correction, 1 still open (rewritten as an actionable reproduction task, not a guess).**


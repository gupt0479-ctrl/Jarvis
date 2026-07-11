---
type: concept
status: active
created: 2026-07-11
tags:
  - portfolio
  - frontend
  - ui-fixes
  - design
notes:
  - "[[frontend-ui-fixes-requirements]]"
  - "[[frontend-ui-fixes-tasks]]"
  - "[[UI Fixes]]"
---
# Frontend UI Fixes — Design

> Architecture-focused companion to [[frontend-ui-fixes-requirements]]. Every fix area below maps 1:1 to a requirements section. See [[frontend-ui-fixes-tasks]] for atomic implementation steps.
> Stack reminders: Next.js 16 App Router, Tailwind v4 (CSS-first, no config file), shadcn/Radix, Framer Motion (`motion/react`), React Three Fiber + drei, Sanity, Biome, pnpm.

## Component Dependency Map

```
PortfolioContent.tsx (server)
├── HeaderScrolling.tsx ─── useTheme() (next-themes) ─── ThemeProvider.tsx
├── SidebarAwareContent.tsx
│   ├── ObsidianBackground.tsx → ObsidianBackgroundCanvas.tsx (R3F, scroll+click physics)
│   ├── HeroSection.tsx → HeroContent.tsx → ProfileImage.tsx
│   ├── [HeroTerminal.tsx]  ← REMOVED from render tree (Fix 1)
│   ├── AboutSection.tsx → AboutTelemetry.tsx (4 stat cards)
│   ├── ExperienceSection.tsx → ExperienceSectionClient.tsx → ExperienceCard.tsx
│   ├── [inline] Projects section → ProjectsSlider.tsx (R3F-free, Framer Motion)
│   ├── SkillsSection.tsx → SkillsSectionClient.tsx → SkillsCapabilityGraph.tsx (SVG)
│   ├── EducationSection.tsx → EducationFlowchart.tsx (R3F, drei MeshDistortMaterial)
│   ├── CertificationsSection.tsx
│   ├── AchievementsSection.tsx / BlogSection.tsx / ContactSection.tsx (unaffected)
│   └── Footer.tsx
├── Orby.tsx (fixed, aria-hidden, RAF-driven position)
│   ├── OrbyCanvas.tsx → OrbyModel.tsx (radio prop redesign, Fix 8)
│   ├── OrbySpeechCloud.tsx
│   ├── OrbyArrow.tsx
│   └── useOrbyState.ts (state machine + new idle-commentary channel, Fix 8)
└── SidebarToggle.tsx → opens PortfolioLab.tsx (Radix Sidebar primitive, src/components/ui/sidebar.tsx)
    └── PortfolioLab.tsx
        ├── PersonaSelector.tsx
        ├── ChatInputBar.tsx ← becomes growable textarea (Fix 4)
        ├── ChatThread.tsx
        └── PanelOrby.tsx
```

**Data flow for chat-driven navigation** (relevant to Fix 6): `PortfolioLab.tsx` posts to `/api/chat` → `chat-tools.ts`'s `navigate` tool returns `{sectionId, orbyMessage, itemSlug, itemIndex}` → `PortfolioLab.tsx` dispatches `window` CustomEvent `orby:navigate` → both `ProjectsSlider.tsx` (listens, resolves `itemSlug` to an index) and `useOrbyState.ts` (listens, drives Orby's `chat-nav-home`/`chat-nav-arrival` states) react independently to the same event. This pub/sub pattern via native `CustomEvent` is already established — new features (auto-play pause, Orby idle commentary) should reuse it rather than introducing a new state manager.

## Design System Updates

No new Tailwind config is created (CSS-first, forbidden). All new tokens are added as CSS custom properties in `src/app/globals.css`, following the existing pattern (`--section-pad-y`, etc.).

**New tokens needed:**
- `--section-pad-y-tight`: a reduced padding value for the Education↔Certifications/Skills boundaries (Fix 7). Recommend `2.5rem` (half of the default `5rem`) as a starting point, applied via a new utility class `.section-pad-tight` alongside the existing `.section-pad`.
- Light-mode token layer (Fix 8): rather than inventing new class names, extend the existing `.cosmic-card`, `.cosmic-card--dark`, `.cosmic-card--subtle`, `.orbit-chip`, `.section-kicker`, `.float-btn`/`.header-btn` rules with a `:root:not(.dark)` or `.light` companion block, mirroring how shadcn's own `:root`/`.dark` OKLCH split already works one layer up. Do NOT rewrite `.dark` — it stays the default and unchanged; add a genuinely new light selector block.

**No breakpoint changes** — existing Tailwind defaults (`sm`, `md`, `lg`) and the codebase's own `768px`/`390px` custom breakpoints (`useIsMobile`, `Orby.tsx`'s `vw <= 390`) are sufficient for every fix area.

## Animation Library — Framer Motion Patterns Used

Per the steering rules, section entry uses `initial={{opacity:0, y:24}}` + `whileInView` + `viewport={{once:true}}`; buttons use `whileHover={{y:-2}}`/`whileTap={{y:1}}`. New animations introduced by this fix pass:

| Fix Area | New Pattern | Where |
|---|---|---|
| 1 (Hero) | One-shot `AnimatePresence`-free comet sweep on mount (a single `motion.div` with `animate` targeting a gradient-position CSS var, `transition={{duration: 1.2, delay: 0.4}}`, no `repeat`) | New wrapper inside `HeroContent.tsx`'s image column |
| 2 (About) | `AnimatePresence` + `height: "auto"` expand/collapse — **reuse `ExperienceCard.tsx`'s existing pattern verbatim**, don't reinvent | `AboutSection.tsx` |
| 3 (Telemetry) | Same `AnimatePresence height:auto` pattern as Fix 2 | `AboutTelemetry.tsx` |
| 5 (Experience) | No new Framer Motion — pure CSS `line-clamp-N` utility, no animation change | `ExperienceCard.tsx` |
| 6 (Carousel) | Auto-play driven by a `setInterval`/`requestAnimationFrame`-based idle timer (not Framer Motion) that calls the *existing* `goNext()` — the slide transition itself (`slideVariants`) is unchanged | `ProjectsSlider.tsx` |
| 8 (Orby wave) | Extend existing `animate={{rotate:[0,-25,0,-25,0]}}` to a larger sweep, e.g. `[0,-70,-40,-70,0]`, same `transition={{duration:1.2, ease:"easeInOut"}}` | `OrbyModel.tsx` |

## 3D Scene Architecture (React Three Fiber)

Two independent R3F scenes exist today and remain independent: `ObsidianBackgroundCanvas.tsx` (background sphere/rings/stars) and `EducationFlowchart.tsx` (blob flowchart). Neither should be merged — they have different lifecycles (background is `position:fixed`, persists across the whole scroll; the flowchart mounts only inside `#education`).

**Fix 1 (scatter-intro) — architecture:**
- Add a `introProgress` ref (0→1 over ~3s, driven by `state.clock.getElapsedTime()` inside the existing `useFrame`, no new Canvas).
- At `t=0`, each `pPos[i]` (planet point) is initialized to a *scattered* position: `pPos0[i] + randomOffsetInSphere(scatterRadius)` instead of the current direct assignment `pPos[i3] = pPos0[i3]`. As `introProgress` eases 0→1, lerp `pPos[i]` from the scattered position toward `pPos0[i]` (the already-computed Fibonacci-sphere rest position).
- This reuses the exact same per-point animation loop that already exists for scroll physics — it's an *additional* lerp term applied only while `introProgress < 1`, gated so it never fights the scroll-driven `pullStr`/`springK` logic (multiply the intro lerp's contribution by `(1 - introProgress)` so it fades out cleanly).
- Click-triggered scatter/rejoin (blast radius): extend the existing `handleClick`/`burstActive` mechanism. Currently `burstActive` drives a *radial ripple* (`Math.sin(pPhase[i] - burstP * Math.PI * 5)`). Add a second burst mode — a boolean `scatterBurstActive` — that instead pushes each point outward along its `pNorm` by a *larger*, non-oscillating displacement, then lets the existing spring-back (`vx += (x0-x) * springK`) pull it back in. This reuses `BURST_DURATION`/`BURST_SHELL_MAX` constants; only the per-point force calculation differs (constant outward push vs. sine ripple).
- **Reduced motion:** skip the scatter entirely — initialize `pPos[i] = pPos0[i]` directly (current behavior) when `useReducedMotion()` is true, exactly like the existing `REDUCED_PULL_STR` branch pattern.

**Fix 1 (hero comet sweep) — NOT R3F.** The profile image is a flat `<Image>` inside `ProfileImage.tsx` — the "light wave" is a CSS/Framer Motion overlay (`::before`-style gradient sweep via a `motion.div` with `mix-blend-mode: overlay`), not a Three.js effect. Keep it out of the Canvas entirely; this avoids adding render cost to a component that's already `hidden lg:flex` (desktop-only, no mobile GPU cost either way, but simplicity wins regardless).

**Fix 7 (Education/Skills — no R3F changes needed).** `EducationFlowchart.tsx`'s scene is untouched by this fix pass; only the *outer* `section-pad` CSS spacing around it changes.

## State Management Strategy

The codebase already uses a consistent, minimal-state philosophy: local `useState`/`useRef` per component, custom hooks for cross-cutting concerns (`useSpaceFloat`, `useOrbyState`, `useIsMobile`), and native `CustomEvent`s for cross-component signaling (`orby:navigate`, `orby:speech`). **No Context API, no external state library, is introduced by this fix pass** — every new piece of state fits the existing pattern:

| Fix Area | New State | Owner | Why local state is sufficient |
|---|---|---|---|
| 2 (About toggle) | `expanded: boolean` | `AboutSection.tsx` (must become `"use client"` — currently server-only) | Single component, no cross-component consumers |
| 3 (Telemetry expand) | `expandedIndex: number \| null` | `AboutTelemetry.tsx` | Single component; accordion behavior is just "one index or null" |
| 4 (Chat input) | `value: string` (already exists) + a derived `lineCount` | `ChatInputBar.tsx` | No change to ownership, just input type swap |
| 6 (Carousel auto-play) | `autoPlayPaused: boolean`, `idleTimerRef` | `ProjectsSlider.tsx` | Already owns `currentIndex`; auto-play is a natural extension |
| 8 (Orby idle commentary) | New hook `useOrbyIdleCommentary()` — wraps a `fetch` to a new server action, dispatches `orby:speech` on success | New file `src/components/orby/useOrbyIdleCommentary.ts`, composed inside `Orby.tsx` alongside `useOrbyState` | Keeps the existing `useOrbyState` state machine unmodified; commentary is an *additional* speech-text source that dispatches through the same `orby:speech` channel `useOrbyState.ts` already listens for — zero changes needed inside `useOrbyState.ts` itself |
| 8 (Dark/light toggle) | Already exists via `next-themes`' `useTheme()` — currently called but unused (`useTheme()` in `HeaderScrolling.tsx` with no destructured `theme`/`setTheme`) | `HeaderScrolling.tsx` | Just needs `const { theme, setTheme } = useTheme()` and wiring the existing no-op `onClick` |

**Important:** `AboutSection.tsx` is currently an **async server component** (`export async function AboutSection()`). Adding a client-side expand/collapse means either (a) splitting it into a server data-fetch wrapper + a new `AboutSectionClient.tsx` for the interactive parts (matching the existing `SkillsSection.tsx`/`SkillsSectionClient.tss` and `ExperienceSection.tsx`/`ExperienceSectionClient.tsx` split pattern already used twice in this codebase), or (b) making the whole thing client and fetching via a route handler. **Recommend (a)** — it's the codebase's own established pattern, zero new architecture.

## Sanity Query Changes

| Fix Area | Query | Change |
|---|---|---|
| 2 (About summary) | `ABOUT_QUERY` in `AboutSection.tsx` | Add `aboutSummary` to the projection: `..., aboutSummary` |
| 3 (Telemetry detail) | `PROFILE_QUERY` in `queries.ts` | Extend `stats[]` projection: `stats[]{label, value, summary}` (assuming schema addition below) |
| 6 (Carousel slug bug) | `PROJECTS_QUERY` — no query change; fix is in `ProjectsSlider.tsx`'s consumption of `slug{current}` (see Fix 6 below) | — |

**Schema additions (`src/sanity/schemaTypes/profile.ts`):**
```
// New field on `profile` document
{
  name: "aboutSummary",
  type: "text",
  rows: 3,
  description: "3-4 sentence collapsed-state summary for the About section.",
  validation: (Rule) => [Rule.max(400).warning("Keep to 3-4 sentences")],
}

// Extend the existing `stats[]` array member with:
{
  name: "summary",
  type: "string",
  description: "1-2 sentence context shown when this stat card is expanded.",
}
```
Run `pnpm typegen` after any schema change — regenerates `src/sanity/types/index.ts` (per the codebase's own documented pipeline: `pnpm typegen && pnpm typecheck`).

---

## Per-Fix Design Detail

### Fix 1 — Hero & Background

**Component structure:** No new components. `HeroTerminal.tsx` import + JSX removed from `PortfolioContent.tsx` (2 lines: the import statement and the `<div className="relative z-10 flex justify-center"><HeroTerminal /></div>` block). File stays on disk, unreferenced.

**Hook requirements:** `ObsidianBackgroundCanvas.tsx`'s existing `Graph` component gains one new `useRef<number>` (`introStartTime`) initialized on mount, read inside the existing `useFrame`. No new `useEffect` needed — the intro is purely a function of elapsed time, same as the existing scroll-driven physics.

**Tailwind changes:** None for the background. For the comet sweep on `ProfileImage`, a new wrapper `<div className="relative overflow-hidden">` around the existing `<ProfileImage>` in `HeroContent.tsx`, with a `motion.div` absolutely positioned inside using inline `background: linear-gradient(...)` (matches the existing inline-style pattern already used for `IridCTA`'s `var(--irid-bg)` — reuse that CSS variable convention).

**Animation spec:** `initial={{ x: "-120%" }}` → `animate={{ x: "120%" }}`, `transition={{ duration: 1.4, delay: 0.6, ease: "easeInOut" }}`, runs once, no `repeat`, no `whileHover`.

**Mobile-first:** Comet sweep is inside the `hidden lg:flex` wrapper already — no mobile cost. Background scatter-intro point count already respects `useIsMobile`'s halving; no new logic needed there.

**Performance:** Zero new draw calls — reusing existing `BufferGeometry`/`BufferAttribute` arrays (`pPos`), just changing their *initial* values before the first `needsUpdate` flush. No `useMemo` changes needed since `data` (in `Graph`'s existing `useMemo`) already recomputes `pPos0`/`pPos` on `[planetCount, ringCount, starCount]` — the scatter offset should be applied as a *runtime* mutation of `data.pPos` right after creation, inside a `useEffect` that runs once on mount (or folded into the existing `useMemo` block directly, since it already builds `pPos` — simplest: initialize `pPos[i3] = pPos0[i3] + scatterOffset` instead of `pPos[i3] = pPos0[i3]` directly in that `useMemo`).

**Z-index / stacking:** No changes — background stays `z-0`/`fixed`, hero content stays `z-10`.

**Event handlers:** The existing `handleClick` on the invisible hit-mesh (`onClick={handleClick}`) already sets `burstActive.current = true`. Add a second entry point — check `scroll01.current` or camera distance to decide burst *scale*, matching the requirement "scaled to the current camera zoom/scroll position." Concretely: `burstScale` already exists (`1.0 + stretchT * 1.2`) — reuse it verbatim for the new scatter-burst mode; no new event wiring needed beyond the existing click handler.

**What could go wrong:** If the scatter-intro's lerp and the scroll-driven `pullStr` physics both write to `pPos[i]` in the same frame without careful ordering, the sphere could visibly "fight itself" (partially formed, then yanked by pointer/scroll forces mid-formation). Mitigate by gating: scroll/pointer forces only apply once `introProgress >= 1` (i.e., the intro fully completes before scroll physics engage) — the intro is short (2–4s) and most users won't scroll instantly, but a defensive gate avoids a jarring transition on fast scrollers.

---

### Fix 2 — About Me Collapsible Toggle

**Component structure:** Split `AboutSection.tsx` (stays a server component, keeps the Sanity fetch) into a thin wrapper that renders a new `AboutSectionClient.tsx` (client component owning the toggle state and rendering both the collapsed summary and the expandable `fullBio`). This exactly mirrors the existing `SkillsSection.tsx` → `SkillsSectionClient.tsx` split.

**Hook requirements:** `const [expanded, setExpanded] = useState(false)` in `AboutSectionClient.tsx`. No `useEffect` needed.

**Tailwind changes:** None beyond what's already used (`AnimatePresence` + `height: auto` needs `overflow-hidden` on the animated wrapper, same as `ExperienceCard.tsx`).

**Animation spec:** Directly reuse `ExperienceCard.tsx`'s block:
```
initial={{ height: 0, opacity: 0 }}
animate={{ height: "auto", opacity: 1 }}
exit={{ height: 0, opacity: 0 }}
transition={{ duration: 0.3, ease: "easeInOut" }}
```

**Mobile-first:** Collapsed summary + toggle + 4 telemetry cards must fit ~1 viewport at 375px width — verify with the `aboutSummary` field capped at ~400 chars (matches the Sanity validation rule proposed above) and Tailwind's existing `text-white/65 leading-relaxed` typography scale (no new type scale needed).

**Performance:** Negligible — this is a small, infrequently-toggled UI element.

**Z-index:** None.

**Event handlers:** One `onClick` on the toggle `<button>`, toggling `expanded`. `aria-expanded={expanded}` on the button (pattern match with `ExperienceCard`'s `aria-expanded={isOpen}`).

**What could go wrong:** If `aboutSummary` is left empty in Sanity (not yet populated), the collapsed state has nothing to show. Fallback: if `aboutSummary` is falsy, fall back to rendering the *first paragraph* of `fullBio` (Portable Text — take the first `block` of type `normal`) as a temporary summary, so the section never renders empty while content is being migrated.

---

### Fix 3 — Interactive Telemetry Boxes

**Component structure:** `AboutTelemetry.tsx`'s `TelemetryCard` becomes a `<button>`-wrapped expandable card. New sub-component `TelemetryDetail.tsx` (small SVG line/sparkline + summary text), rendered conditionally inside the same `CometCard`.

**Open decision resolved for design purposes:** Recommend **mutually exclusive expansion** (accordion) — matches the Skills section's existing "one category selected at a time" interaction model (`SkillsSectionClient`'s `selected` state) and avoids 4 simultaneous expanded blocks competing for vertical space in a 2-column grid.

**Hook requirements:** `const [expandedIndex, setExpandedIndex] = useState<number | null>(null)` lifted to `AboutTelemetry.tsx` (the parent), passed down as `isExpanded`/`onToggle` props to each `TelemetryCard` — same lifted-state pattern already used in `SkillsSectionClient.tsx` (`selected` lifted, passed to `SkillsFilter`/`SkillsCapabilityGraph`).

**Graph source decision (resolves an Open Question from requirements):** Recommend deriving the mini-graph from **existing structured data** rather than new hand-authored time-series fields — e.g., for a "Projects" stat, pull `PROJECTS_QUERY`'s count-by-category as a tiny bar/line; for a "Skills" stat, reuse `SKILLS_QUERY`'s `percentage` distribution. This avoids a second manually-maintained dataset per the requirements doc's own flag. If a given stat has no obvious structured-data mapping, fall back to a static decorative sparkline (already exists: `SPARKLINE_BARS`) — better than blocking the whole feature on 1:1 data mapping for every possible stat label.

**Animation spec:** Same `AnimatePresence height:auto` pattern as Fix 2.

**Mobile-first:** Detail view renders *below* the 2-column grid row (not as an overlay), pushing content down — acceptable on mobile since it's user-initiated, not automatic.

**Performance:** Mini-graphs are small SVGs (reuse `SkillsCapabilityGraph.tsx`'s `buildSmoothPath` helper, extracted to a shared util if reused 2+ places — see `src/lib/svg-chart.ts` proposal in tasks doc).

**Event handlers:** `onClick` per card toggles `expandedIndex` (click again to collapse, click a different card to switch).

**What could go wrong:** If a stat's `summary` field is empty (schema addition not yet populated in Studio), the expand reveals a graph with no context text — acceptable degraded state, not a blocker, but flag as a known gap until content is filled in.

---

### Fix 4 — Portfolio Lab Chat Input

**Component structure:** `ChatInputBar.tsx`'s `<input type="text">` becomes a `<textarea>` with auto-grow logic. No new files — this is a targeted rewrite of one component.

**Hook requirements:** New local `useRef<HTMLTextAreaElement>` to measure `scrollHeight` and manually set `style.height` on each `onChange` (the standard "auto-grow textarea" technique — no external library needed, avoids adding a dependency for a solved problem). Cap growth at 3 lines by computing `maxHeight = lineHeightPx * 3` and clamping.

**Tailwind changes:** `<textarea>` needs `resize-none` (prevent manual drag-resize, since auto-grow handles it) and `overflow-y-auto` for when the 3-line cap is hit. Rest of the styling (`bg-transparent`, `text-sm`, `outline-none`) carries over unchanged from the `<input>`.

**Animation spec:** None needed — height changes can be instant or a short CSS `transition: height 120ms ease` (native CSS, no Framer Motion needed for this).

**Mobile-first:** This is the fix area's entire point (per requirements). Test the growable textarea + send button combination at 320/375/390px widths inside the mobile 100%-width sidebar (`SIDEBAR_WIDTH_MOBILE`).

**Performance:** Negligible.

**Event handlers:** `onKeyDown` must change: currently `Enter` always submits (`e.preventDefault(); handleSubmit()`). With a multi-line textarea, standard UX is `Enter` submits, `Shift+Enter` inserts a newline — update the handler: `if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); handleSubmit(); }`. This is a **behavior addition**, not just a wrapper change — flag explicitly since it changes existing keyboard semantics.

**Character/length indicator:** A small `<span>` showing `value.length / MAX_LEN` that only renders (or only becomes non-transparent) once `value.length > MAX_LEN * 0.8`, matching the codebase's existing "opacity-based reveal" pattern already used in `SkillPill`'s proficiency label (`opacity: hovered ? 1 : 0`, always in DOM). Recommend `MAX_LEN = 1000` as a starting cap (generous for a chat message, prevents pathological input) — **flag for confirmation with the user**, since the source brief doesn't specify an exact number, only "until the send button" as a visual metaphor.

**What could go wrong:** If `MAX_LEN` is enforced by truncating `value` on `onChange`, users typing near the limit could see characters silently disappear mid-word — bad UX. Prefer *blocking further input* past the cap (`if (e.target.value.length <= MAX_LEN) setValue(...)`) over truncation, so the cursor position and typed text stay predictable.

---


**Chat bubble text overflow (Gap 3, confirmed via code read — scoped separately from the textarea/cap work above):** `ChatThread.tsx`'s user-message bubble (`<div className="ml-auto max-w-[80%] rounded-xl px-3 py-2 ...">{msg.text}</div>`) has no `break-words`/`overflow-wrap` class, so a single long unbroken token (URL, long identifier, etc.) overflows the `max-w-[80%]` bound instead of wrapping. This is unrelated to the textarea growth/character-cap work above (that governs *input*; this governs *rendered message* overflow) and should be tracked as its own small CSS fix:
- **Change:** add `break-words` (Tailwind) or equivalently `overflow-wrap: anywhere` to the bubble's className
- **Scope:** single className addition, no state/logic change, no Sanity impact
- **Risk:** low — purely additive CSS, does not alter existing wrapping behavior for normal text, only affects the edge case of unbroken long tokens

### Fix 5 — Experience Section Line Clamping

**Component structure:** No new components. `ExperienceCard.tsx`'s `responsibilities`/`achievements` `<li>` text spans get a `line-clamp-2` (mobile) / `line-clamp-3` (desktop) Tailwind utility added to the `<span className="font-sans leading-relaxed">` wrapper.

**Tailwind changes:** `className="font-sans leading-relaxed line-clamp-3 md:line-clamp-3 sm:line-clamp-2"` (or equivalent responsive clamp variants — Tailwind's `line-clamp-*` utilities are already available via the base Tailwind v4 install, no plugin needed).

**Animation spec:** None.

**Mobile-first:** Clamp value differs by breakpoint as noted in requirements — verify against real card widths at 375px vs 1280px+ (characters-per-line differs significantly).

**Performance:** Zero cost — CSS-only.

**What could go wrong:** `line-clamp` combined with the existing `flex gap-3` bullet layout (`→` prefix + text) needs the *text span specifically* clamped, not the parent `<li>` (which would also clamp the bullet glyph oddly) — apply the class to the inner `<span>` only, exactly as scoped above.

---

### Fix 6 — Projects Carousel Auto-Play + Navigation Fix

**Component structure:** No new components. `ProjectsSlider.tsx` gains an idle-timer effect.

**Hook requirements:**
```
const AUTO_PLAY_INTERVAL_MS = 5000;
const AUTO_PLAY_MAX_INDEX = 3; // only indices 0,1,2

const [autoPlayPaused, setAutoPlayPaused] = useState(false);
const idleTimerRef = useRef<ReturnType<typeof setInterval> | null>(null);

useEffect(() => {
  if (prefersReducedMotion || autoPlayPaused) return;
  idleTimerRef.current = setInterval(() => {
    setCurrentIndex((prev) => {
      const next = (prev + 1) % AUTO_PLAY_MAX_INDEX;
      setDirection(1);
      return next;
    });
  }, AUTO_PLAY_INTERVAL_MS);
  return () => clearInterval(idleTimerRef.current!);
}, [autoPlayPaused, prefersReducedMotion]);
```
Need a new `useReducedMotion`-equivalent check — `ProjectsSlider.tsx` currently has none; add the same `window.matchMedia("(prefers-reduced-motion: reduce)")` pattern already used in `ObsidianBackgroundCanvas.tsx`/`EducationFlowchart.tsx` (three separate ad-hoc implementations exist already in this codebase — a shared `useReducedMotion` hook would be a nice consolidation but is **out of scope** for this fix pass; just match the existing pattern locally).

**Pause-on-interaction:** Every existing manual navigation entry point (`goNext`, `goPrev`, dot click, drag, keyboard arrow) must call `setAutoPlayPaused(true)` — add this single line inside each existing handler. Do not add a "resume after idle" timer unless explicitly requested; the requirements doc says auto-play "resumes after any idle period following manual interaction" — implement via a second `setTimeout` inside the pause-setter that flips `autoPlayPaused` back to `false` after e.g. 10s of no further manual interaction (reuse the interval-based `idleTimerRef` pattern, just a second, separate timer for resume).

**Auto-play boundary correctness:** The modulo must be `% AUTO_PLAY_MAX_INDEX` (3), NOT `% safeProjects.length` (9) — this is the core requirement. Manual navigation continues to use `% safeProjects.length` unchanged (existing `goNext`/`goPrev` logic is untouched).

**Slug-shape bug fix (chat navigation):** `PROJECTS_QUERY` always returns `slug: { current: string }` (never a bare string) per the query definition in `queries.ts`. The current lookup:
```
const slug = typeof p.slug === "string" ? p.slug : (p.slug as {current?: string} | null)?.current;
```
The `typeof p.slug === "string"` branch is dead code. Simplify to:
```
const slug = (p.slug as { current?: string } | null)?.current ?? null;
```
This isn't a functional bug fix per se (the `?? current` fallback branch already worked) — but it removes a misleading dead branch that could mask a real bug if the query shape ever changes. **Flag:** if chat navigation is still unreliable after this cleanup, the actual root cause is more likely in `chat-tools.ts`'s `navigate` tool description/prompt engineering (the model not passing `itemSlug` reliably) — that is a persona/prompt-engineering fix, not a frontend fix, and is **out of scope** for this UI-fixes pass; flag for a follow-up on the chatbot side (`src/lib/personas/`).

**Event handlers:** Auto-play must also pause on `onMouseEnter`/`onFocus` of the carousel `<section>` per WCAG 2.2.2 — add `onMouseEnter={() => setAutoPlayPaused(true)}` at the `<section aria-label="Projects carousel">` level (in addition to the manual-interaction pausing above).

**What could go wrong:** If the auto-play interval isn't cleared on unmount (e.g., user navigates away via SPA routing — unlikely here since this is a single-page portfolio, but still), it could throw a "setState on unmounted component" warning. The `useEffect` cleanup (`clearInterval`) above already handles this correctly.

---

### Fix 7 — Skills Graph Year Range + Section Spacing

**Component structure:** No new components. `SkillsCapabilityGraph.tsx`'s `YEARS` constant and `CATEGORY_SHAPES` values are recalculated.

**Year-range decision (resolves an Open Question from requirements):** Recommend **shifting forward** (`["2022","2023","2024","2025","2026","2027"]`) rather than dropping 2021 and shrinking to 5 points — this preserves the existing 6-point cubic-bezier smoothing logic (`buildSmoothPath` assumes reasonably dense points; 5 points would work but changes the curve's visual character) and gives the graph one extra forward-looking year, which reads better for a "growth trajectory" narrative than a foreshortened one. **Flag for user confirmation** before implementing — this is explicitly listed as unresolved in requirements.

**Ceiling enforcement ("no skill above 35 at start"):** With the year window shifted forward by one, every `CATEGORY_SHAPES[key].pattern[0]` value effectively represents 2022 instead of 2021 — recompute each category's `startFloor` so that `startFloor` (the absolute Y at pattern=0) combined with `pattern[0]` (already tuned per-category, e.g. `frontend: 0.32`) never produces a first-year value >35. Concretely: `firstYearValue = startFloor + pattern[0] * (avg - startFloor)`. For categories where `avg` is high (e.g., `tools` at high proficiency), even a modest `pattern[0]` can push `firstYearValue` over 35. Recommend adding a clamp directly in `buildCurveValues`:
```
const raw = shape.pattern.map((p) => shape.startFloor + p * (avg - shape.startFloor));
if (raw[0] > 35) {
  const scale = 35 / raw[0];
  return raw.map((v, i) => (i === 0 ? 35 : v * scale + (v - v * scale) * (i / (raw.length - 1))));
}
return raw;
```
This is one valid approach; the simplest correct fix is to just cap `raw[0]` at 35 directly and leave the rest of the curve as authored (since `pattern[5] = 1.0` always pins the endpoint to real `avg` regardless of the first-point clamp): 
```
const values = shape.pattern.map((p) => shape.startFloor + p * (avg - shape.startFloor));
values[0] = Math.min(values[0], 35);
return values.map((v) => Math.min(100, Math.max(0, v)));
```
**Recommend this simpler clamp** — matches the requirement literally ("no skill above 35 at the starting point") without over-engineering a smooth rescale.

**Skill/category pill hover-effect reduction:** The requirements doc flags 7 distinct `SkillPill` effects (`effectIndex % 7`) as "not cohesive." Recommend reducing to **3 effects** (down from 7) selected from the existing set based on visual coherence — e.g., keep effect 1 (ring pulse), effect 4 (gradient wash), effect 6 (3D tilt); drop effects 0, 2, 3, 5 (glitch-scan, constellation dots, orbit-dot — the most "busy" ones per the source brief's "laggy" complaint, even though none are measurably slow). **Flag for design sign-off** — this is a subjective call, not a measured bug fix.

**Section spacing:** Add new CSS class in `globals.css`:
```
.section-pad-tight {
  padding-block: var(--section-pad-y-tight, 2.5rem);
}
```
Apply to the *top* padding of `EducationSection.tsx` and *bottom* padding of `SkillsSection.tsx` (i.e., tighten the gap from both sides of the Education boundary) — requires splitting `section-pad`'s combined `padding-block` into explicit `padding-top`/`padding-bottom` on these two sections specifically, since `section-pad` currently applies symmetric padding. Recommend a more surgical utility: `.section-pad-bottom-tight { padding-bottom: 2.5rem; }` and `.section-pad-top-tight { padding-top: 2.5rem; }`, applied as additional classes alongside the existing `section-pad` (Tailwind/CSS cascade: later-applied explicit `padding-top`/`padding-bottom` overrides the shorthand `padding-block` from `.section-pad` as long as they're both present and order is respected — verify in the browser, since CSS specificity here is same-specificity-different-property, so it should just work via source order, `.section-pad` defined first in the stylesheet).

**What could go wrong:** Tightening Education's top padding without also checking Certifications' `pt-12` (already reduced, per the existing CSS comment: "Certifications uses reduced top padding... for tighter visual coupling with Education") could result in *double-tightening* — re-verify the whole Skills→Education→Certifications visual rhythm together, not just Education in isolation, since Certifications already has a special-cased padding value.

---


**`CategoryPill` audit (Gap 2 — distinct from `SkillPill` above, confirmed via code read):** `CategoryPill` (in `SkillsSectionClient.tsx`) is a separate, richer effect system from `SkillPill` — it layers 9+ per-category animation variants on top of a **continuous** `useSpaceFloat` idle-drift effect, whereas `SkillPill`'s 7 effects are hover-only and have no idle motion. The requirements doc's original "reduce hover-effect variety" language was written against `SkillPill` only and does not transfer directly to `CategoryPill`'s always-on drift. Recommend treating `CategoryPill` as its own reduction pass, not folded into the `SkillPill` clamp above:
- Keep the `useSpaceFloat` idle drift (it is the category-level ambient motion the section relies on, not one of the "busy" hover effects being complained about)
- Reduce the 9+ per-category hover/selection variants down to **2-3** using the same coherence criteria as `SkillPill` (favor smooth transform/opacity changes, drop multi-element choreography like constellation-dot bursts)
- **Flag for design sign-off** alongside the `SkillPill` reduction — both are subjective calls, not measured bugs, and should be reviewed together since a user will encounter both pill types in the same section.

### Fix 8 — Orby, Dark Mode, Footer

**Orby radio redesign:** `OrbyModel.tsx`'s radio `<div>` (currently `6×10px` gradient rectangle) gets a sibling `<div>` for the antenna — a thin `1×8px` element angled via `transform: rotate(15deg)`, positioned at the radio's top-right corner, with a small glowing dot at its tip (reuse the existing glow-via-`boxShadow` pattern already used throughout `OrbyModel.tsx`, e.g. `box-shadow: 0 0 4px rgba(139,92,246,0.5)`).

**Wave animation extension:** Change `animate={{ rotate: [0, -25, 0, -25, 0] }}` to `animate={{ rotate: [0, -70, -50, -70, -20] }}` (deeper raise, holds near the top longer) — `transition` duration can extend slightly to `1.4s` to avoid feeling rushed at the new range.

**Orby idle commentary — architecture:**
- New server action (or route handler) `src/app/api/orby-comment/route.ts` (or `src/app/actions/orby-comment.ts` if kept as a Server Action) — reuses `routeChat`'s provider chain from `model-router.ts`, but with a much smaller/cheaper request: no tools, no conversation history, just a short system prompt like "Generate one short, playful, in-character line (under 100 chars) that a tiny astronaut companion named Orby might say while idly watching someone browse a portfolio site. Do not mention specific facts unless given context." — matches the "flagged for clarification" open question in requirements by defaulting to **ungrounded flavor text** (lower hallucination risk, per the requirements doc's own reasoning), not fact-adjacent commentary.
- New hook `useOrbyIdleCommentary()`: tracks scroll-dwell time (no scroll event for N seconds while a section is in view) or Orby-click count, and on trigger, calls the new endpoint, then dispatches `window.dispatchEvent(new CustomEvent("orby:speech", {detail: {text}}))` — this is the *exact same event* `useOrbyState.ts` already listens for (see its `handleOrbySpeech` effect), so **zero changes needed inside `useOrbyState.ts`** — the new hook just becomes a second producer on an existing consumer channel.
- Rate-limit the new endpoint the same way `/api/chat` is rate-limited today (Upstash-backed) — reuse the existing Redis client pattern from `model-router.ts`, new key namespace e.g. `orby:idle:${sessionId}`.

**Roaming sub-states:** Add 2 new visual states to `OrbyModel.tsx`'s `pose` prop — e.g. `"radio-talk"` (small repeating head-tilt + radio-hand shake, distinct from the existing `wave`/`pointing`/`idle`) and `"drift"` (the current default idle float, renamed for clarity, no visual change needed — it already exists as `pose === "idle"`'s `motion.div` wrapper). `useOrbyState.ts`'s `roaming` state already exists; `getPose()` in `Orby.tsx` needs a new branch: alternate between `"idle"` and `"radio-talk"` every N seconds while in `roaming` state (a simple `useState` timer cycling the pose, driven from `Orby.tsx`, not `useOrbyState.ts` — keeps the state machine itself unchanged, purely a presentational cycle).

**Dark/Light mode:**
- `HeaderScrolling.tsx`: `const { theme, setTheme } = useTheme();` (currently called with no destructuring — trivial fix), wire the button: `onClick={() => setTheme(theme === "dark" ? "light" : "dark")}`, dynamic `aria-label` and icon swap (`Moon`/`Sun` from `lucide-react`, already a dependency).
- `globals.css`: add a light-mode companion block for every cosmic-system class. Example for `.cosmic-card`:
```css
:root:not(.dark) .cosmic-card {
  background: linear-gradient(135deg, rgba(245,244,250,0.85) 0%, rgba(238,236,248,0.9) 100%);
  border: 1px solid rgba(124,58,237,0.18);
  /* not pure white per source brief — off-white/lavender-tinted */
}
```
Repeat for `.cosmic-card--dark`, `.cosmic-card--subtle`, `.orbit-chip`, `.section-kicker`, `.float-btn`/`.header-btn` glow colors, and the base `body`/`:root` OKLCH tokens (already split `:root`/`.dark` for shadcn primitives — this just needs the *cosmic* system to follow the same split, which it currently doesn't).
- `ObsidianBackgroundCanvas.tsx` stays dark-only regardless of theme, per the requirements doc's flagged decision point — **recommend this explicitly** rather than building a light-mode 3D palette, since the "space command center" background concept doesn't translate to light mode without a full re-concept (out of scope).

**Footer redesign:** Direction deferred per requirements — at minimum, add a subtle `useSpaceFloat`-style ambient touch to the glyph/copyright text (very low radius, e.g. `radius: 2`) to match the "everything floats" steering rule, without changing the existing 3-column grid structure. Concrete visual treatment (gradient intensity, added iconography) is a polish decision to make during implementation, not a structural one.

**What could go wrong:**
- Orby idle commentary firing too often could feel spammy — enforce a minimum cooldown between idle-triggered lines (e.g., 45s) independent of the rate-limit backend check, purely client-side, to avoid hammering the new endpoint on rapid scroll/click bursts.
- Light mode risks breaking readability if any hardcoded `text-white/NN` Tailwind utility classes (used pervasively across every section component) aren't also given light-mode counterparts — this is the single biggest risk in Fix 8. A full audit of every `text-white/*` usage against the new light background is required before shipping; flagged explicitly in the tasks doc as its own task with a checklist, not folded silently into "add light tokens."


---

## Fix 7b — Education Deformity Sequencing & Bachelor's Highlight (confirmed gap)

**Correction to earlier claim:** an earlier pass of this design doc characterized `EducationFlowchart.tsx` as "untouched." That was inaccurate. Verified via `grep_search`: the file already defines `DISTORT = [0, 0.42, 0.68]` (index 0 = Bachelor's/college = solid/undistorted, index 1 = high-school = 0.42 distort, index 2 = middle-school = 0.68 distort) and `BASE_POS` orders the blobs `[0]=college, [1]=high-school, [2]=middle-school`. So the *target* distort values already encode "Bachelor's should read as solid/highlighted" — what's missing is any **entrance sequencing**. The existing `TravellingDot` element loops continuously along the flowchart path, but it is not wired to the blob distort values in any way — there is no timed reveal, no stagger, and no scroll-triggered start.

**Component structure:** No new component needed. `EducationFlowchart.tsx`'s blob meshes are pure R3F (`@react-three/drei` distorted-material meshes inside a `Canvas`), not DOM elements, so this cannot use a Framer Motion `whileInView` wrapper the way DOM-based sections do — it needs its own scroll-trigger mechanism.

**Sequencing mechanism:**
- Wrap the `Canvas` (or its parent DOM container) in an `IntersectionObserver`-based hook — check whether `EducationFlowchart.tsx`'s parent already sits inside a `whileInView`-capable motion wrapper at the section level; if the section wrapper's `viewport={{ once: true }}` fire can be threaded down as a prop/context flag, prefer that over adding a second observer. If no such wrapper reaches the Canvas boundary, add a lightweight `IntersectionObserver` directly (mirrors the `useSpaceFloat`-style hook pattern already used elsewhere for scroll-driven effects).
- On trigger, drive each blob's live distort value toward its `DISTORT[i]` target via a `useFrame` lerp (same pattern as Fix 1's scatter-intro animation — mutate a ref per frame, never allocate `new THREE.*` inside `useFrame`), staggered by blob index so college resolves first, then high-school, then middle-school — reinforcing "Bachelor's is the highlighted/primary node" through order as well as final distort amount.
- Before the trigger fires, blobs should start at a shared higher-distort "unresolved" state (e.g., all at `DISTORT[2]`'s value or higher) so the animation reads as a resolve-into-clarity sequence, not just a distort-amount tween.
- Respect `prefers-reduced-motion`: skip the timed stagger and lerp entirely, snapping directly to each blob's final `DISTORT[i]` value with no animated transition — consistent with the project's existing reduced-motion posture for R3F scenes.

**What could go wrong:** if the section-level `whileInView` flag and a new local `IntersectionObserver` both fire independently, they could produce a double-trigger or race condition. Decide on exactly one trigger source before implementation and confirm it against the actual parent wrapper markup, not assumed.

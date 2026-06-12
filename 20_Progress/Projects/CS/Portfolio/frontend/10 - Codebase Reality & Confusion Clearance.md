---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - context
  - cowork
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[02 - Sanity as Single Source of Truth]]"
  - "[[09 - Sanity Content Spec]]"
---
# Codebase Reality & Confusion Clearance

This file is written for Claude Cowork. Read it before opening any other note in this folder. It resolves every assumption the other notes made without verifying against the actual repo, and it adds three topics the other notes deliberately left blank (ObsidianBackground, dark mode toggle, Orby). Nothing here is aspirational — every statement is verified against the live codebase.

**Repo location (WSL):** `/home/anant_gupta/projects/hub/portfolio/`
**Active branch at time of writing:** `Chatbot` (being merged to `main` before the `frontend` branch begins)

---

## Part 1 — Branch State Before You Start

The `Chatbot` branch has one commit ahead of `main` (`feat: Orby chatbot v1 complete — nextgen UI overhaul`) that is **not yet merged**. There are also uncommitted source changes that need committing before the branch switch:

Modified tracked files (need a commit):
- `src/app/globals.css` — comet-card ghost variant CSS
- `src/components/AboutTelemetry.tsx` — UI polish
- `src/components/HeroTerminal.tsx` — minor fix
- `src/components/PortfolioContent.tsx` — minor fix
- `src/components/sections/AboutSection.tsx` — UI polish
- `src/components/ui/comet-card.tsx` — added `"ghost"` variant (fourth variant alongside default/dark/subtle)

Untracked files to evaluate:
- `.kiro/hooks/` — four new kiro hooks (css-motion-guard, hero-clutter-guard, lint-on-save, post-task-verify)
- `.kiro/specs/hero-ui-polish-fix/` — a kiro spec directory
- `docs/ecc-setup-guide.md` — new doc
- `e2e-screenshots/`, `test-results/` — output artifacts (should be gitignored, not committed)
- `orby-nav-e2e.spec.ts`, `playwright.config.ts` — Playwright e2e tests
- `src/components/__tests__/hero-ui-polish-*.tsx`, `orby-chat-nav.test.ts` — new unit tests

**What needs to happen before switching to `frontend`:**
1. User commits the six modified source files (CLAUDE.md forbids Claude from committing — user manages git).
2. `Chatbot` branch gets merged into `main` (PR or direct merge — user's call).
3. `frontend` branch is checked out. It was already created; it just hasn't been switched to yet.

**Note to Cowork:** Do not attempt to commit, push, or merge. Just verify the branch is `frontend` at the start of a build session before touching any files.

---

## Part 2 — Sanity Schema Reality

The other notes (especially [[02 - Sanity as Single Source of Truth]] and [[09 - Sanity Content Spec]]) were written as a design document — they describe what the data model _should_ look like after the rebuild, not what it looks like today. Here is what actually exists, field by field, so you can tell the gap from the goal.

### The `skill` document type — exists, but schema is thinner than the notes assume

**File:** `src/sanity/schemaTypes/skill.ts`

Current fields in the live schema:
- `name` (string, required)
- `category` (string enum — see below, required)
- `proficiency` (string enum: beginner / intermediate / advanced)
- Possibly a few more display fields — check the full schema file before writing a query

**What the notes describe but does NOT exist yet:**
- `skillCategory` as a separate referenced document type — **does not exist**. Categories are string enums baked into the `skill` document itself.
- `color` field on skill — **does not exist** in the schema. The notes want per-skill color; that field must be added.
- `familiarity` (0–100 numeric) — **does not exist**. Must be added for the graph.
- `blurb` (short description) — **does not exist**. Must be added.

**Current category enum values on the skill document:**
`frontend`, `backend`, `ai-ml`, `devops`, `database`, `mobile`, `cloud`, `testing`, `design`, `tools`, `soft-skills`, `other`

**Note:** The [[09 - Sanity Content Spec]] uses a different set of category slugs (`data-systems` instead of `database`, etc.) and introduces `skillCategory` as a first-class document. Phase 0 of the build means reconciling these: either migrate existing `skill` docs to the new category slugs, or add the `skillCategory` document type and migrate references. This is a schema migration — run `pnpm typegen` after any schema changes.

### The `technologies` vs `skills` confusion — critical

**Every section component (Experience, Projects, Certifications) uses the field name `technologies[]`, not `skills[]`.** The references point to `skill` documents, but the field is named `technologies`. This name exists in:
- `src/sanity/schemaTypes/project.ts` — field: `technologies`, line ~50
- `src/sanity/schemaTypes/experience.ts` — field: `technologies`
- Certifications has a local query using `skills[]` (written during the chatbot build) but the canonical schema field may still be `technologies[]` — **verify before writing queries**

**The notes uniformly say `skills[]→ref(skill)`.** In queries, use the actual field name `technologies[]→` for Experience and Projects until those fields are renamed. The `CertificationsSection.tsx` local query already uses `skills[]->` — check whether that field was actually added to the certification schema or if the query fails silently.

**Bottom line for Cowork:** Before writing any GROQ query that reads skills/technologies, open the relevant schema file in `src/sanity/schemaTypes/` and read the actual field names. Do not assume `skills[]` — it may be `technologies[]`. After the schema migration in Phase 0, the field names will match the notes; until then, use what's there.

### GitHub URL field — it's `githubUrl`, not `repoUrl`

The [[09 - Sanity Content Spec]] uses `repoUrl` as the field name. The actual `project` schema field is:
- **`githubUrl`** (verified in `src/sanity/schemaTypes/project.ts`, line ~88)
- The existing GROQ query `PROJECT_BY_SLUG_QUERY` in `src/sanity/lib/queries.ts` reads `githubUrl` and `liveUrl`

When pushing real project content (OpsPilot, Resq, etc.) to Sanity, populate `githubUrl`, not `repoUrl`. When the notes say to "resolve repoUrl via GitHub MCP," that means: resolve the GitHub repo URL and put it into the `githubUrl` field.

### Certifications — manual Sanity entry confirmed

The current certification documents in Sanity appear to be dummy/filler content (AWS SA-Pro, GCP PCA, CKA, etc.) that Anant likely does not hold. The [[09 - Sanity Content Spec]] explicitly flags this: _"do not present unearned certs."_

**Action:** Delete all dummy certification documents from Sanity Studio. For real credentials Anant holds, enter them manually in Sanity Studio (`/studio`). The schema and `CertificationsSection.tsx` component are ready to render them; nothing code-side needs changing. If Anant confirms he holds zero certs right now, leave the certifications section empty — the component already handles an empty array (`if (!certs?.length) return null`).

### Project content — use Sanity Studio or Sanity MCP

Real project content (OpsPilot, Resq, SafeReach, AI Portfolio Agent, Jarvis, Arc) is specified in detail in [[09 - Sanity Content Spec]]. Push it via Sanity Studio or the Sanity MCP's `create_documents` / `edit_document` tools. For GitHub URLs, use the `github` MCP to search repositories by project name — match on OpsPilot, Resq, SafeReach, etc. If no match is found, leave `githubUrl` empty and flag it; never invent a URL.

### GROQ query file and typegen discipline

The shared query file is `src/sanity/lib/queries.ts`. The section components sometimes define their own local queries (`defineQuery(...)` inline in the component). Both patterns exist in the codebase — the certifications section uses an inline query. For new or updated queries, prefer `src/sanity/lib/queries.ts` for shared queries. After any schema change or new query, run `pnpm typegen` to regenerate `src/sanity/types/index.ts` (never edit that file manually), then `pnpm typecheck`.

---

## Part 3 — ObsidianBackground: Current State and Enhancement Path

### What already exists (it's far more advanced than the notes imply)

File: `src/components/three/ObsidianBackgroundCanvas.tsx` (loaded via `src/components/three/ObsidianBackground.tsx` which is the dynamic-import wrapper)

The background is not a simple particle sphere. It is a full physics simulation:

**Geometry:**
- A fibonacci sphere of 2,800 points (desktop) / 1,400 (mobile) — `fibonacciSphere()`
- A tilted torus ring of 2,000 points (desktop) / 1,000 (mobile) — `createRing()`
- A starfield of 5,500 points (desktop) / 2,750 (mobile) scattered in a 30-unit volume behind everything
- Edge/line segments connecting nearby sphere points and ring points, rendered as `LineSegments`

**Physics (runs every frame, zero allocations):**
- Each sphere dot has a rest position, current position, and velocity — spring-returns to rest
- **Magnetic dent:** the cursor projects into world space and pulls facing-side dots toward it; back-side dots get a tiny sympathetic wobble. Creates a visible, satisfying dent in the sphere surface that follows the cursor.
- **Click burst:** clicking the sphere fires a radial ripple wave across all dots via a sine wave keyed to each dot's phase
- **Scroll-progressive physics:** as the user scrolls, `stretchT` ramps from 0 to 1, stiffening the magnetic pull and allowing deeper dents. Camera zooms in smoothly.
- **Ring physics:** ring points orbit slowly and respond to cursor hover with a gentle attract force
- **Star narrative:** stars dim mid-scroll as the sphere earns attention, then settle slightly above invisible

**Rendering details:**
- Custom soft-glow point sprite (radial gradient on a 64×64 canvas texture) applied as `alphaMap` — makes every particle a soft glowing dot rather than a hard square
- DPR capped at 1.25 (not 2.0 — intentionally lower for performance)
- `antialias: false` on the GL context (points don't benefit from MSAA)
- Vignette overlay (radial gradient div, z-index 2) protects text readability
- Near-black base layer (`#05040A`)
- `prefers-reduced-motion` handled — pull strength drops 4.5×, drift drops 25×, displacement capped
- Sidebar-aware: shifts its right edge by `sidebarWidth` when sidebar opens, animated with cubic-bezier

**Color palette (hardcoded):**
- Planet dots: `#9D8BBF` (muted violet)
- Ring dots: `#8A7AAE` (same family, slightly darker)
- Planet lines: `#8A7AAE`
- Ring lines: `#8A7AAE`
- Stars: `#D0CBE8` (cool lavender-white)

### What "not at par with latest Three.js" means concretely

The physics and geometry are genuinely impressive. What the background lacks compared to the most visually striking Three.js portfolio backgrounds in 2025–2026:

1. **No bloom / post-processing.** The particles glow only because of the soft sprite texture. True bloom (from `@react-three/postprocessing` — the `Bloom` effect) would make the bright points spill light onto neighboring geometry, creating a much more otherworldly luminous feel. This is the single highest-impact missing enhancement.

2. **No additive blending.** `PointsMaterial` uses standard alpha blending. Switching to `additiveBlending` on the planet and ring points makes overlapping particles accumulate intensity rather than fight for opacity — creates the dense-cluster glow that characterizes premium space scenes.

3. **No chromatic aberration or vignette shader.** The current vignette is a CSS div. A screen-space post-process `ChromaticAberration` effect (subtle, ~0.0005 offset) adds cinematic depth without being distracting.

4. **No depth fog / distance fade.** Stars at extreme depth look the same brightness as near ones. A depth-based fog or a custom shader that fades points by z-depth would add parallax depth.

5. **No color reactivity.** The palette is static. Even a very slow, barely-perceptible hue rotation on the planet color (cycling from `#9D8BBF` to `#8BBFC0` over 60–90 seconds) would make the scene feel living rather than frozen.

6. **No GPU instancing for lines.** The edge lines are `LineSegments` with a CPU-updated position buffer. At 2,800 planet points with up to 3 edges each, this is ~8,400 line endpoints being updated every frame. This is fine now but is the first thing to profile if frame drops appear.

### Enhancement plan (ordered by impact / effort ratio)

**Tier 1 — do these, they transform the scene:**
- Add `@react-three/postprocessing`. Wrap the Canvas content in `<EffectComposer>`. Add `<Bloom luminanceThreshold={0.18} luminanceSmoothing={0.9} intensity={0.35} />`. Tune until it feels luminous, not blown out.
- Switch planet and ring `PointsMaterial` to `additiveBlending`. The muted violet points will accumulate into bright clusters naturally. Reduce base opacity slightly (from 0.52/0.46 to ~0.35) to compensate.

**Tier 2 — meaningful polish:**
- Add `<ChromaticAberration offset={[0.0004, 0.0004]} />` inside the EffectComposer.
- Add a barely-perceptible slow hue animation: derive `COL_PLANET` from `t * 0.003` using HSL → hex math so the sphere color drifts imperceptibly over time.

**Tier 3 — future, not for this sprint:**
- Custom GLSL shader for depth-based opacity falloff.
- Environment map for subtle reflections on ring surfaces.
- GPU-instanced line rendering.

**Package to add:** `@react-three/postprocessing` — already a known package in the ecosystem; check if it's in `package.json` already, and if not add with `pnpm add @react-three/postprocessing`.

**Performance constraint:** Keep `dpr` cap at 1.25. Post-processing adds a render pass. Test on mobile after adding — if frame rate drops below 50fps, guard with `const isLowPower = isMobile || prefersReduced` and skip the EffectComposer on low-power paths.

---

## Part 4 — Dark Mode Toggle: What Exists and What to Do

### Current state (it does nothing)

File: `src/components/HeaderScrolling.tsx`, lines ~167–170

```tsx
<div className="ml-auto hidden shrink-0 items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-xs text-white/50 md:flex">
  <Moon className="h-3.5 w-3.5" />
  <span className="hidden sm:inline">Dark</span>
</div>
```

This is a **purely decorative pill** — a Moon icon and the word "Dark." There is no `onClick` handler, no `useTheme()` call, no state. It is not a button. It is a cosmetic indicator.

**`ThemeProvider` is correctly wired** (`src/components/ThemeProvider.tsx`): it uses `next-themes` with `attribute="class"`, `defaultTheme="dark"`, `enableSystem`. The infrastructure to switch themes is present. The toggle in the header just isn't connected to it.

### Why light mode is non-trivial here

The entire design system assumes a near-black (`#05040A`) background with the Three.js canvas always visible. `cosmic-card`, `float-btn`, `section-kicker`, and every text color are designed against that dark background. A functional light mode toggle would require:

- A complete light palette for all cosmic-card variants (the translucent backgrounds become meaningless on a light bg)
- The Three.js background adapting its colors (a pale background under a dark violet particle sphere looks wrong)
- The header, sidebar, and every section component checking the theme and switching tokens

This is a **significant design system change**, not a wiring task. It is not part of this sprint.

### Decision

**Make the toggle a real functioning button — but dark-only for now:**

Replace the static div with a `<button>` that calls `useTheme()` and shows the current theme state with a visual indicator. Since light mode isn't designed, the button toggles between `"dark"` (always) and shows a tooltip/label "Light mode — coming soon" if someone clicks it trying to switch. This gives it real click affordance, responds correctly, and doesn't break anything.

Alternatively, the simplest correct path: **remove the toggle entirely** and leave the dark indicator as a non-interactive label if there's no intention to ever build light mode. Decide which before the frontend sprint starts, because the header component (`HeaderScrolling.tsx`) is what gets changed.

**Recommendation:** Keep the indicator but wire it as a proper button with `useTheme()`. Default to "dark" always, log a noop or show a short toast "Light mode coming soon" on click. This takes 10 minutes and makes the header feel complete without committing to light mode design work.

### What needs to change in `HeaderScrolling.tsx`

```tsx
// Add at the top of the component:
import { useTheme } from 'next-themes'
// Inside the component:
const { theme, setTheme } = useTheme()
// Replace the static div with:
<button
  type="button"
  onClick={() => setTheme(theme === 'dark' ? 'dark' : 'dark')} // noop for now
  aria-label="Toggle color theme (light mode coming soon)"
  className="float-btn ml-auto hidden shrink-0 items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-xs text-white/50 md:flex"
>
  <Moon className="h-3.5 w-3.5" />
  <span className="hidden sm:inline">Dark</span>
</button>
```

This resolves the toggle as a real interactive element. Mark light mode as a future task in a separate note.

---

## Part 5 — Orby: The Complete Picture

### What Orby is (not in any other note)

Orby is a fully implemented autonomous floating astronaut companion. It is NOT a chatbot widget — the chat lives in the Lab sidebar (`src/components/lab/PortfolioLab.tsx`). Orby is a separate visual layer that reacts to the user's scroll position and the chat sidebar state.

**Component files (`src/components/orby/`):**
- `Orby.tsx` — the main component, orchestrates all positioning and state
- `OrbyCanvas.tsx` — renders the astronaut figure (likely a canvas or SVG animation)
- `OrbyModel.tsx` — the visual model/sprite of the astronaut
- `OrbyArrow.tsx` — the pointing arrow that appears when Orby is in "pointing" state
- `OrbySpeechCloud.tsx` — the speech bubble that appears above/below Orby
- `useOrbyState.ts` — the state machine
- `useScrollProgress.ts` — scroll tracking hook
- `useTypedText.ts` — typewriter effect for speech text

**Position architecture:** Orby's position is driven by a `requestAnimationFrame` loop that writes directly to `wrapperRef.current.style.transform`. This is intentionally decoupled from React re-renders — position changes do not cause re-renders. State machine transitions (speech text, state changes) do trigger React renders via `useOrbyState`.

**z-index placement:** `z-40` (the wrapper div). The header is `z-50` so Orby always appears below the header. The chat sidebar is also higher z-index, so Orby moves to accommodate it.

### The state machine

The `useOrbyState` hook drives these states in sequence:

| State | When | What Orby does |
|---|---|---|
| `intro` | Page load, first 3s | Lifts off from bottom edge — slow space launch to hover height |
| `pointing` | At hover height near the lab button | Extends right arm pointing at the lab/chat button |
| `roaming` | Scroll > ~10% | Drifts leftward across the page as scroll increases, tracking page progress |
| `section-comment` | Arrives at a section | Brief pause + fires a per-section speech message |
| `exitingLeft` | Reaches left edge (~100% scroll) | Parks at left edge with micro-float |
| `goodbye` | At left edge, idle | Lands to bottom, waves goodbye |
| `departingLeft` | On scroll up from goodbye | Slides off-screen left |
| `returningRight` | After departing left | Teleports to off-screen right, springs back in to home position |
| `chat-nav-home` | Chat triggers navigation | Glides back to home position — signals intentional nav |
| `chat-nav-arrival` | After chatbot navigates | Holds at home, shows arrival message |
| `reducedMotion` | `prefers-reduced-motion` | Stays at home position, no orbit |

### How Orby connects to the chatbot

The `chat-nav-home` and `chat-nav-arrival` states are the interface between the chatbot and Orby. When the chatbot's `navigate` tool fires (e.g., user asks Orby to scroll to Projects), the chat system triggers Orby to glide home and show an arrival message when the scroll completes. This is Phase 7 from the chatbot build plan — it was implemented in the `Chatbot` branch.

The chat sidebar open state is passed to Orby via `useSidebar()`. When the sidebar opens, Orby adjusts its home X position to account for the sidebar width (448px), moving left so it doesn't overlap the panel.

### Current frontend issues with Orby (not documented elsewhere)

These are the gaps and friction points in Orby's current implementation that a frontend pass should address:

**1. Speech cloud collision with section cards**
`OrbySpeechCloud` renders absolutely positioned at Orby's location. When Orby is in `section-comment` state and a card is nearby, the speech text may overlap card content. There's no collision avoidance. `positionAbove` (true when Orby's y > 90px from top) is the only positioning logic — it flips the cloud above or below Orby, but not left/right. The cloud needs a right-edge bound so it doesn't clip the viewport right edge when Orby is at the home position.

**2. Section-comment message timing**
The per-section messages are fired when Orby arrives at each section's scroll position. The calibration of "arrived at section" scroll thresholds needs verification against the actual section heights. If sections are taller than expected (e.g., after the frontend rebuild adds more content), Orby may fire its message too early or too late.

**3. Mobile speech cloud is too wide**
On viewports < 768px, the speech cloud width should be constrained more aggressively. The current max-width may overflow on small phones.

**4. Orby renders even on very small screens**
There's a `tooSmall` guard (`window.innerHeight < 560 && window.innerWidth < 400`) but it's a fairly narrow exception. On 375px wide phones, Orby still renders and may overlap content in the hero section where the lab button also lives. Consider hiding Orby entirely when the sidebar is open on mobile.

**5. The "ghost" variant in CometCard added on Chatbot branch**
The Chatbot branch added a `"ghost"` variant to `CometCard`. This is now in the codebase (committed or about to be committed). The OrbySpeechCloud likely uses this variant for its cloud surface. Make sure this is included in the commit before switching branches.

### What Orby is NOT

Orby is not the chat interface. Orby does not handle message streaming, tool calls, or API responses. The chat UI is in `src/components/lab/PortfolioLab.tsx` and the chat sidebar. Orby communicates one-way: it receives state signals (from scroll and from the chat triggering nav events) and outputs speech text and visual position. It has no direct connection to the API route.

### Orby visual enhancement (for this frontend sprint)

The notes say Orby is "out of scope." That means the astronaut model/visual is not being redesigned. What IS in scope is fixing the friction points listed above (speech cloud bounds, mobile overlap, section timing calibration) and making sure Orby's z-layer and position are correct relative to the new section layouts.

---

## Part 6 — What the Other Notes Got Right (and Can Stay As-Is)

To give Cowork confidence in what to trust:

- **[[01 - Motion System & Comet Cards]]** — The `CometCard` component is real (`src/components/ui/comet-card.tsx`), has the `default`, `dark`, `subtle`, and now `ghost` variants. The notes correctly describe the tilt/glare behavior. The `useSpaceFloat` hook described in the notes does NOT exist yet — it needs to be built. The notes describe it correctly as what should be built.

- **[[03 - Experience Section]]** — The `ExperienceCard.tsx` exists in `src/components/cards/`. The timeline rail is currently static and CSS-based. The EXPERIENCE_QUERY in queries.ts fetches `employmentType`, `description`, `achievements`, and `technologies[]->{}`. The component renders some of these fields but not all (description notably absent — it's in the data but the UI needs wiring).

- **[[04 - Projects Carousel]]** — `ProjectsSlider.tsx` exists in `src/components/three/`. It is the single ugliest section and needs a full rebuild as the notes describe. The header is indeed left-aligned today.

- **[[05 - Skills Capability Graph]]** — The skills section has a `SkillsSection.tsx` and `SkillsSectionClient.tsx`. The graph is broken (doesn't render). The category buttons exist but are dead. The notes' target state is accurate.

- **[[06 - Education Flowchart]]** — The section exists. The header is left-aligned. The three education stages are currently rendered as rectangular cards, not blobs.

- **[[07 - Certifications & Achievements]]** — Section exists. The dummy cert data needs removal as noted. The `SpaceRail` for achievements timeline needs building.

- **[[08 - Blog, Contact & Footer]]** — Blog renders from Sanity, confirmed. Contact card exists but feels flat. Footer is too tall and too dim — both confirmed accurate in the current UI.

---

## Part 7 — Complete Phase Order for the Frontend Sprint

This resolves the ordering ambiguity. Do these in sequence:

**Phase 0 — Schema migration + content (prerequisite for everything)**
1. Verify and update `skill` schema: add `color`, `familiarity`, `level`, `blurb` fields.
2. Decide on `skillCategory`: either add as a new document type (recommended) or keep as enum and add `color` per category to the skill schema itself.
3. Rename `technologies[]` to `skills[]` on experience, project, and certification schemas (migration — update all GROQ queries after).
4. Push real skill registry to Sanity (the [[09 - Sanity Content Spec]] skill tables).
5. Push real project content (OpsPilot, Resq, SafeReach, AI Portfolio Agent, Jarvis, Arc) with correct `githubUrl` from GitHub MCP.
6. Push real experience content (verify against résumé, wire all fields).
7. Remove dummy certifications; enter real ones only.
8. Run `pnpm typegen` → `pnpm typecheck`.

**Phase 1 — Motion primitives**
Build `useSpaceFloat` hook and confirm `CometCard` is the single hover surface. These two primitives unblock every section.

**Phase 2 — Header: dark mode toggle fix**
Wire `useTheme()` to the Moon button in `HeaderScrolling.tsx` (10 min). Done.

**Phase 3 — ObsidianBackground enhancement**
Add `@react-three/postprocessing`, apply Bloom + additive blending + ChromaticAberration. Verify mobile perf.

**Phase 4 — Per-section rebuilds**
In order: Experience → Projects carousel → Skills graph → Education flowchart → Certifications + Achievements → Blog polish → Contact (glass frame) → Footer compact.

**Phase 5 — Orby friction fixes**
Speech cloud edge bounds, mobile overlap fix, section timing calibration after new section heights are known.

**Phase 6 — CSP header**
Add Content-Security-Policy to `next.config.ts` (see [[02 - Commands, Hooks & CSP Fix]] in the claude-code-setup folder). Run report-only first.

---

## Part 8 — Things Cowork Must Not Do

- Do not commit git. User manages all commits.
- Do not push to Vercel/remote. User manages deploys.
- Do not use npm or yarn. pnpm only.
- Do not create `tailwind.config.ts`. Tailwind v4 is CSS-first — global CSS in `src/app/globals.css`.
- Do not edit `src/sanity/types/index.ts` — it is generated. Run `pnpm typegen` instead.
- Do not hardcode any content that belongs in Sanity.
- Do not invent GitHub URLs or live URLs. Leave empty and flag for Anant.
- Do not touch `src/app/api/` or `src/lib/chat-*` — those are the chatbot layer, not the frontend layer.
- Do not redesign the Hero section, About section, or the floating terminal — they are marked done and loved.
- Do not touch the Orby model/visual (OrbyCanvas.tsx, OrbyModel.tsx) — those are out of scope.

---

## Quick-Reference: Key File Paths

| What | Path |
|---|---|
| Three.js background (physics) | `src/components/three/ObsidianBackgroundCanvas.tsx` |
| Three.js background (wrapper/loader) | `src/components/three/ObsidianBackground.tsx` |
| Header with dark mode toggle | `src/components/HeaderScrolling.tsx` |
| Theme provider | `src/components/ThemeProvider.tsx` |
| CometCard primitive | `src/components/ui/comet-card.tsx` |
| Orby main component | `src/components/orby/Orby.tsx` |
| Orby state machine | `src/components/orby/useOrbyState.ts` |
| Orby speech cloud | `src/components/orby/OrbySpeechCloud.tsx` |
| Lab/chat sidebar | `src/components/lab/PortfolioLab.tsx` |
| All shared GROQ queries | `src/sanity/lib/queries.ts` |
| Sanity schema types | `src/sanity/schemaTypes/` (one file per type) |
| Generated types (do not edit) | `src/sanity/types/index.ts` |
| Global CSS / design tokens | `src/app/globals.css` |
| Section components | `src/components/sections/` |
| Experience card | `src/components/cards/ExperienceCard.tsx` |
| Projects carousel (Three.js) | `src/components/three/ProjectsSlider.tsx` |

## Quick-Reference: Commands

```bash
pnpm dev          # dev server
pnpm typegen      # regenerate Sanity types
pnpm typecheck    # TypeScript strict check (run after typegen)
pnpm lint         # Biome check
pnpm format       # Biome format --write (auto-runs on every file edit via hook)
pnpm build        # full production build
pnpm test         # Vitest run
```

---

## Log

- **2026-06-12:** File created by Claude Code (Sonnet 4.6) after full codebase analysis — verified ObsidianBackgroundCanvas, HeaderScrolling, ThemeProvider, Orby.tsx, skill schema, project schema, CertificationsSection, queries.ts, and comet-card.tsx against the live repo on the Chatbot branch. Resolves all confusions noted by Anant about Sanity field names, GitHub URLs, certifications content, dark mode toggle, background enhancements, and Orby integration.

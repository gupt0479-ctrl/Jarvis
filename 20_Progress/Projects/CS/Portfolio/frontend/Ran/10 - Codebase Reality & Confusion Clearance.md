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

This file is written for Claude Cowork. Read it before opening any other note in this folder. It resolves every assumption the other notes made without verifying against the actual repo, and it adds full verified context on three topics the other notes deliberately left blank — ObsidianBackground, dark mode toggle, and Orby. Nothing here is aspirational. Every statement is verified against the live codebase at `/home/anant_gupta/projects/hub/portfolio/` on the `Chatbot` branch (being merged to `main` before the `frontend` branch begins).

**Repo location (WSL):** `/home/anant_gupta/projects/hub/portfolio/`

---

## Part 1 — Sanity Schema Reality

The other notes (especially [[02 - Sanity as Single Source of Truth]] and [[09 - Sanity Content Spec]]) were written as a design brief — they describe what the data model should look like after the rebuild, not what exists today. Here is what is actually in the live schema files, verified by reading each one in full.

### The `skill` document (`src/sanity/schemaTypes/skill.ts`) — richer than the notes assume

The notes claim `skill` is bare and needs several fields added. In reality the schema already has:

| Field | Type | Notes |
|---|---|---|
| `name` | string (required) | |
| `category` | string enum | `frontend`, `backend`, `ai-ml`, `devops`, `database`, `mobile`, `cloud`, `testing`, `design`, `tools`, `soft-skills`, `other` |
| `proficiency` | string enum | `beginner` / `intermediate` / `advanced` / `expert` |
| `percentage` | number (0–100) | Numeric proficiency — this IS the "familiarity" / "level" field the notes say is missing |
| `yearsOfExperience` | number | |
| `tone` | string enum | `neutral` / `accent` / `highlight` / `muted` — used for visual display weighting |

**Fields the notes say to add that should NOT be added:**
- `color` — was deliberately removed from the schema. A comment at line 90 says `// remove old "color" field from your type`. Colors are derived at render time from `category` (see `CATEGORY_COLORS` in `SkillsSectionClient.tsx` and `ExperienceCard.tsx`). Do not add it back.
- `familiarity` / `level` — `percentage` (0–100) already serves this exact role. Do not add a duplicate.
- `blurb` — a short description field. This one does NOT exist and could legitimately be added if the UI needs it. But it is not required for any of the sections in scope for this sprint.

**`skillCategory` as a separate document type — does not exist and should not be created.** Categories are string enums baked into the `skill` document. The GROQ queries already normalize and group by category on the client side (`SkillsSectionClient.tsx`). Creating a separate `skillCategory` document type would require a schema migration, a typegen run, and rewrites of every skills-related query. The current approach works correctly.

**The SKILLS_QUERY (from `src/sanity/lib/queries.ts`):**
```groq
*[_type == "skill"] | order(category asc, name asc){
  _id, name, category, proficiency, percentage, yearsOfExperience,
  "tone": coalesce(tone, "neutral")
}
```
All relevant fields are already being fetched. No query changes needed for the skills section.

### `technologies[]` vs `skills[]` — the actual split

This is the most commonly misunderstood thing in all the notes. The correct reality:

- **`experience` schema** → field is `technologies[]` → array of references to `skill` documents
- **`project` schema** → field is `technologies[]` → array of references to `skill` documents
- **`certification` schema** → field is `skills[]` → array of references to `skill` documents

**This is not a mistake to fix — it is the current state of the schema.** The certification section's local query (`CERTS_SECTION_QUERY` in `CertificationsSection.tsx`) already correctly uses `skills[]->{ _id, name, category }` and works.

The notes uniformly say `skills[]→ref(skill)` as if it's one field name across all types. It isn't. The EXPERIENCE_QUERY and PROJECTS_QUERY both use `technologies[]->{...}`. This is what you write in GROQ for those types.

**Do not rename `technologies[]` to `skills[]` on experience and project.** Phase 0 of the build plan calls for this rename — that guidance is wrong. The rename would break all existing queries, require a Sanity migration, and provide no UI benefit. The field names are fine as-is.

### The `project` schema (`src/sanity/schemaTypes/project.ts`) — critical corrections

**`githubUrl` not `repoUrl`.** Every other note in this folder uses `repoUrl`. The actual field is `githubUrl`. The PROJECTS_QUERY and PROJECT_BY_SLUG_QUERY both read `githubUrl`. When entering project data in Sanity Studio or via Sanity MCP, use `githubUrl`.

**`visibility` is a string enum, not a boolean.** The project schema has `visibility: "featured" | "standard"` AND an older `featured: boolean` field. The PROJECTS_QUERY normalizes both:
```groq
"featured": select(featured == true => true, visibility == "featured" => true, false),
"visibility": select(defined(visibility) => visibility, featured == true => "featured", "standard")
```
Both patterns work. Enter `visibility: "featured"` for new projects.

**No `description` field on project.** The project schema has `tagline` (short text) but NOT a long `description` field. The PROJECT_BY_SLUG_QUERY does list `description` in its projection — that may be stale. The main PROJECTS_QUERY only fetches `tagline`. For the carousel, `tagline` is the field that renders.

**`coverImage` is required.** All project cards assume a cover image. A project without `coverImage` renders without the hero banner section.

**`category` is a string enum:** `web-app`, `mobile-app`, `ai-ml`, `api-backend`, `devops`, `open-source`, `cli-tool`, `desktop-app`, `browser-extension`, `game`, `other`.

### The `experience` schema (`src/sanity/schemaTypes/experience.ts`)

- `companyWebsite` (not `companyUrl` — the notes use the wrong name)
- `description` is Portable Text (array of block — NOT a plain string). The EXPERIENCE_QUERY fetches it but `ExperienceCard.tsx` does NOT render it. This is the main content gap on the experience card.
- `responsibilities[]` is an array of strings — this IS rendered (up to 3)
- `achievements[]` is an array of strings — this IS rendered (up to 2, styled green with ★)
- `technologies[]` → skill refs — rendered as orbit-chips (up to 4)
- `tenure`: "current" | "past" — the query normalizes this alongside the old `current: boolean` field

### The `certification` schema (`src/sanity/schemaTypes/certifications.ts`)

Uses `skills[]` (not `technologies[]`) for skill refs. Has: `name`, `issuer`, `issueDate`, `expiryDate`, `credentialId`, `credentialUrl`, `logo`, `description` (plain text), `order`.

**The dummy certifications in Sanity (AWS SA-Pro, GCP PCA, CKA, etc.) are fake credentials that Anant does not hold.** Delete them from Sanity Studio before any frontend work. The section handles an empty list: `if (!certs?.length) return null`.

### The `education` schema (`src/sanity/schemaTypes/education.ts`)

- Fields: `institution`, `degree`, `fieldOfStudy`, `startDate`, `endDate`, `current (boolean)`, `gpa`, `description (text)`, `achievements[]`, `logo`, `website`, `order`
- **No `stage` field.** The blob stage (`amoeba`, `forming`, `stable`) is a pure UI concept — `EducationFlowchart.tsx` assigns them by sort order: first item = `stable`, second = `forming`, third = `amoeba`. This is not in Sanity, it is hardcoded index-based in the component.

### The `achievement` schema (`src/sanity/schemaTypes/achievement.ts`)

- `type` enum: `award`, `experience`, `leadership`, `entrepreneurship`, `sports`, `hackathon`, `publication`, `speaking`, `open-source`, `milestone`, `recognition`, `other`
- Has `featured: boolean` and `order` for sorting
- `url` is the external link (rendered as an `ExternalLink` icon button in `AchievementsSection.tsx`)

### The `profile` singleton (`src/sanity/schemaTypes/profile.ts`)

- `socialLinks` object: `github`, `linkedin`, `twitter`, `website`, `medium`, `devto`, `youtube`, `stackoverflow`
- `stats[]`: array of `{label, value}` objects
- `headlineAnimatedWords[]`, `headlineStaticText`, `headlineAnimationDuration` — used by the hero animated headline
- Singleton: `_id == "singleton-profile"`

### Shared GROQ queries (`src/sanity/lib/queries.ts`)

All queries use `defineQuery()` from `next-sanity` so `pnpm typegen` can extract types. After any schema change:
1. Run `pnpm typegen` → regenerates `src/sanity/types/index.ts`
2. Run `pnpm typecheck` → TypeScript strict check
3. Never edit `src/sanity/types/index.ts` manually

Some sections define their own inline queries beside the component (`AchievementsSection.tsx`, `CertificationsSection.tsx`, `BlogSection.tsx`, `ContactSection.tsx`). The shared queries in `queries.ts` are the canonical ones. Where a section uses an inline query that isn't in `queries.ts`, that's fine — just make sure `defineQuery()` is used so the type gets picked up.

---

## Part 2 — ObsidianBackground: Full Technical Reality

### What already exists (it's far more advanced than the notes imply)

**Files:**
- `src/components/three/ObsidianBackground.tsx` — next/dynamic wrapper with `{ ssr: false }`
- `src/components/three/ObsidianBackgroundCanvas.tsx` — 836 lines, the actual implementation

The background is a full physics simulation with three geometry layers and no post-processing:

**Geometry:**
- Fibonacci sphere — 2,800 points desktop / 1,400 mobile (`PLANET_RADIUS = 0.8`)
- Tilted torus ring — 2,000 points desktop / 1,000 mobile (`RING_MAJOR_RADIUS = 2.6`, tilted 30°)
- Random starfield — 5,500 points desktop / 2,750 mobile, scattered across a 30-unit volume
- `LineSegments` connecting nearby sphere and ring points

**Physics (runs every frame, zero object allocations):**
- Every sphere dot has a rest position, current position, and velocity — spring-returns to rest
- **Magnetic cursor dent:** projects cursor into world space, pulls facing-side dots toward it. Back-side dots get a sympathetic wobble. Creates a visible indent that follows the cursor.
- **Click burst:** clicking the sphere fires a radial ripple wave keyed to each dot's phase offset
- **Scroll-progressive physics:** `stretchT` ramps 0→1 over the bottom 60% of scroll. At full stretch: pull strength increases, displacement allowed deeper, spring K stiffens, damping drops. Camera position moves along a path that zooms in.
- Ring points orbit and respond to cursor hover with gentle attraction
- Stars dim mid-scroll then settle near-invisible

**Rendering:**
- Custom soft-glow sprite texture (radial gradient on a 64×64 canvas, used as `alphaMap`) — every point is a soft glowing dot, not a hard square
- DPR capped at 1.25 (not 2.0 — intentional performance cap)
- `antialias: false` on the GL context
- CSS vignette overlay (radial gradient div) at z-index 2
- `prefers-reduced-motion`: pull strength drops 4.5×, drift drops 25×, displacement capped
- Sidebar-aware: shifts the canvas right edge by `sidebarWidth` (448px) when sidebar opens, animated with cubic-bezier

**Color palette (hardcoded constants):**
- Planet points: `#9D8BBF` (muted violet)
- Ring/line points: `#8A7AAE`
- Stars: `#D0CBE8` (cool lavender-white)
- Background base: `#05040A` (near-black)

**No post-processing.** No `@react-three/postprocessing`. No Bloom. No additive blending. No ChromaticAberration. These are the visual gaps.

### What "not at par with latest Three.js" means specifically

The physics are genuinely impressive. What the background lacks compared to premium 2025–2026 Three.js portfolio backgrounds:

1. **No bloom.** The glow effect is purely from the soft sprite `alphaMap`. True `Bloom` from `@react-three/postprocessing` makes bright points spill light onto neighboring geometry — the single highest-impact missing enhancement.

2. **No additive blending.** `PointsMaterial` uses standard alpha blending. Switching to `additiveBlending` makes overlapping points accumulate intensity rather than fight for opacity — creates the dense-cluster luminosity that characterizes premium space scenes. Free visual upgrade.

3. **No chromatic aberration.** A screen-space `ChromaticAberration` effect (subtle, ~0.0004–0.0005 px offset) adds cinematic depth. Takes one line to add once the `EffectComposer` is wired.

4. **No depth fade.** Stars at extreme depth look the same brightness as near ones. A depth-based opacity falloff (custom shader) would add parallax depth. This is Tier 3 work.

5. **Static palette.** The color never changes. A very slow hue drift on `COL_PLANET` (cycling ±10° in HSL over 60–90 seconds) would make the scene feel living rather than frozen. Easy to add.

### Enhancement plan (ordered by impact / effort ratio)

**Tier 1 — do these, they transform the scene:**
1. Add `@react-three/postprocessing` (check if it's already in `package.json` — `@react-three/postprocessing` is a peer dependency of R3F, it may already be present). If not: `pnpm add @react-three/postprocessing`.
2. Wrap the Canvas scene in `<EffectComposer>`. Add `<Bloom luminanceThreshold={0.18} luminanceSmoothing={0.9} intensity={0.35} />`. Tune until luminous, not blown out.
3. Switch planet and ring `PointsMaterial` to `additiveBlending`. Reduce base opacity (currently ~0.52/0.46) to ~0.30–0.35 to compensate for accumulation.

**Tier 2 — meaningful polish:**
4. Add `<ChromaticAberration offset={[0.0004, 0.0004]} />` inside the EffectComposer.
5. Add a barely-perceptible hue animation: derive `COL_PLANET` from `t * 0.003` (elapsed seconds) using HSL math. The sphere drifts between `#9D8BBF` and `#8BBFC0` imperceptibly over a minute.

**Tier 3 — future sprint:**
6. GLSL shader for depth-based opacity falloff on stars.
7. Environment map for subtle reflections on ring line segments.
8. GPU-instanced line rendering (current `LineSegments` with CPU-updated buffer is fine at this scale, but profiles first as particle counts increase).

**Performance constraint:** Keep `dpr` cap at 1.25. Post-processing adds a render pass — test on mobile after adding. If frame rate drops below ~50fps on a mid-range phone, guard with:
```tsx
const skipEffects = isMobile || prefersReducedMotion
// Conditionally wrap with EffectComposer only when !skipEffects
```

**Entry point for the three-artist agent:** Delegate the ObsidianBackground enhancement to the `three-artist` agent (see `.claude/agents/three-artist.md`). That agent has full R3F context and the `ObsidianBackgroundCanvas.tsx` file path in its system prompt.

---

## Part 3 — Dark Mode Toggle: What Exists and What to Do

### Current state (it does nothing — literally)

**File:** `src/components/HeaderScrolling.tsx`, lines ~167–170

```tsx
<div className="ml-auto hidden shrink-0 items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-xs text-white/50 md:flex">
  <Moon className="h-3.5 w-3.5" />
  <span className="hidden sm:inline">Dark</span>
</div>
```

This is a decorative pill — a `<div>`, not a `<button>`. No `onClick`, no `useTheme()`, no state. It shows the Moon icon and the word "Dark" as a cosmetic status indicator.

**`ThemeProvider` is correctly wired** (`src/components/ThemeProvider.tsx`): `next-themes` with `attribute="class"`, `defaultTheme="dark"`, `enableSystem`. The infrastructure to switch themes exists. The header element is simply not connected to it.

### Why light mode is not a quick task

The entire design system assumes the near-black canvas (`#05040A`) is always present. **All** cosmic-card, float-btn, section-kicker, section-backdrop, orbit-chip CSS vars are defined exclusively inside the `.dark { }` block in `src/app/globals.css`. There is no `.light` block, no light-mode cosmic palette. Enabling light mode means:

- A complete light palette for all `.cosmic-card` variants (translucent backgrounds become invisible on a white bg)
- The Three.js background adapting its star/planet colors (muted violet on a light background looks muddy)
- Every `text-white/60` and `border-white/10` class breaking on a light bg — those would need explicit dark: prefixes or a full color token rethink

This is a substantial design system rewrite. It is explicitly out of scope for this sprint per [[00 - Frontend Overhaul — Build Plan]].

### Decision and implementation (10 minutes of work)

**Make the pill a real interactive element but dark-only:**

In `HeaderScrolling.tsx`, replace the `<div>` with a proper `<button>` that uses `useTheme()` and shows affordance without committing to light mode:

```tsx
'use client'
// Add to imports:
import { useTheme } from 'next-themes'

// Inside the component (HeaderScrolling is already a client component):
const { theme } = useTheme()

// Replace the static div:
<button
  type="button"
  onClick={() => {/* light mode not yet designed */}}
  aria-label="Color theme — dark mode active (light mode coming soon)"
  className="float-btn ml-auto hidden shrink-0 items-center gap-1.5 rounded-full border border-white/10 bg-white/5 px-3 py-1.5 text-xs text-white/50 md:flex cursor-default"
>
  <Moon className="h-3.5 w-3.5" />
  <span className="hidden sm:inline">Dark</span>
</button>
```

The `cursor-default` keeps it from feeling clickable since it's a noop. This gives it semantic correctness (a `<button>` is a role=button, screen readers understand it) without committing to light mode design work. When light mode design is done, wire `setTheme('light')` into the onClick.

Alternatively: leave it as a `<div>` and add `role="status"` and `aria-label="Color theme: dark"` so it's semantically correct as a status indicator. Either approach takes minutes.

---

## Part 4 — Orby: The Complete Picture

### What Orby is

Orby is a fully implemented autonomous floating astronaut companion. It is NOT the chatbot — the chatbot lives in the Lab sidebar (`src/components/lab/PortfolioLab.tsx`). Orby is a visual layer that follows scroll position and reacts to the Lab sidebar state.

**Component files (`src/components/orby/`):**
- `Orby.tsx` — main orchestrator. RAF loop writes to DOM transforms directly (zero React re-renders for position).
- `OrbyCanvas.tsx` — renders the full 3D astronaut figure using R3F primitives (helmet sphere, visor dome, body box, capsule arms, capsule legs with boots). **This is NOT a sprite or image — it is a live R3F canvas.**
- `OrbySpeechCloud.tsx` — speech bubble above/below Orby. Typewriter effect at 32 chars/s.
- `OrbyArrow.tsx` — animated pointing arrow, shown in `pointing` state only.
- `useOrbyState.ts` — the state machine (11 states).
- `useTypedText.ts` — typewriter hook used by `OrbySpeechCloud`.

**There is no `OrbyModel.tsx`.** The astronaut model is built entirely within `OrbyCanvas.tsx`.

### Position architecture (the most important technical fact)

Orby's position is driven by a `requestAnimationFrame` loop inside `Orby.tsx` that writes directly to `wrapperRef.current.style.transform`. React state changes (speech text, state transitions) cause React renders. Position changes do NOT. This is intentional — running position through `useState` would cause 60 React re-renders per second.

**Canvas size:** 88px desktop, 64px mobile. Canvas height = `size * 1.3`.

**Home position computation (simplified):**
```
homeX = vw - 72 - 20 - canvasSize - sidebarOffset
homeY = vh - canvasH/2 - 48  // vertically centers Orby with the lab button
```
When the sidebar opens: `sidebarOffset = 448` — Orby moves 448px left to clear the panel.

**z-index:** `z-40`. Header is `z-50` (Orby always under the header). The outer `aria-hidden="true"` wrapper is `pointer-events-none`; the inner wrapper is `pointer-events-auto` (Orby is clickable — nudges on click).

**Toosmall guard:** Hidden when `window.innerHeight < 560 && window.innerWidth < 400`.

### The 11-state machine

| State | Trigger | Orby behaviour |
|---|---|---|
| `intro` | Page load | Lifts off from bottom over 3s — slow space launch |
| `pointing` | After liftoff at home position | Extends right arm pointing at the Lab button |
| `roaming` | Scroll > ~10% | Drifts left across page tracking scroll progress (0.1→0.9) |
| `section-comment` | Arrives at a section trigger | Brief pause, fires per-section speech message |
| `exitingLeft` | Near 100% scroll | Parks at left edge with micro-float |
| `goodbye` | Idle at left edge | Lands to bottom, waves — says farewell |
| `departingLeft` | Any scroll up from goodbye | Slides off-screen left |
| `returningRight` | After departing left | Teleports to off-screen right, springs in to home |
| `chat-nav-home` | Chat's `navigate` tool fires | Glides back to home — signals navigation underway |
| `chat-nav-arrival` | Navigation complete | Holds at home, shows arrival message from chatbot |
| `reducedMotion` | `prefers-reduced-motion` | Stays at home, no orbit |

**Section triggers (which sections fire speech):** Only `projects`, `blog`, and `contact` trigger the `section-comment` state. Experience, skills, education, certifications, and achievements do NOT trigger Orby speech. This is a deliberate calibration choice — extending triggers to more sections means writing copy for each and is a product decision, not a code gap.

### How Orby connects to the chatbot (Phase 7)

Phase 7 wires Orby to the chatbot's `navigate` tool. The interface is a CustomEvent:

```ts
window.dispatchEvent(new CustomEvent('orby:navigate', {
  detail: { sectionId: 'projects', orbyMessage: 'Here are the projects!' }
}))
```

`useOrbyState.ts` listens for `orby:navigate` on `window`. On receipt, it transitions to `chat-nav-home`, then `chat-nav-arrival` with the provided message. The speech cloud shows the arrival message from the chat context. This is already implemented in the `Chatbot` branch.

**The chat sidebar state** is read via `useSidebar()`. When `sidebarOpen === true`, the speech cloud hides (`cloudVisible = speechText !== null && !sidebarOpen`). This prevents the cloud from overlapping the open panel.

### OrbyCanvas 3D model details

Built from R3F primitives:
- Helmet: sphere with `#1a1a2e` (dark navy)
- Visor: hemisphere dome with `#06b6d4` (cyan, emissive 0.15)
- Body: box with `#c8d0de` (light grey)
- Arms: capsule geometry with suit texture, right arm has a radio antenna box
- Legs: capsule geometry with `#c8d0de`, boots are darker boxes at the base
- Violet rim ring: `#8b5cf6`

**Poses (driven by `getPose(state)` in `Orby.tsx`):**
- `idle` — microgravity arm drift in `useFrame`
- `pointing` — right arm extended toward the lab button
- `wave` — oscillating arm wave (used in `goodbye` and `departingLeft`)
- `speaking` — expressive gesturing (used when speech cloud is visible)

Camera: `position: [0, 0, 3.2]`, `fov: 38`. `gl={{ alpha: true, antialias: true, powerPreference: "low-power" }}`.

### OrbySpeechCloud layout gaps

`OrbySpeechCloud.tsx` renders with `min-w-[200px] max-w-[300px]`, positioned `left-1/2 -translate-x-1/2` relative to Orby's wrapper. **There is no viewport edge clamping.** When Orby is at its home position (far right, near the viewport right edge), the speech cloud may clip outside the visible area on narrow viewports. This is a known gap that should be fixed during this frontend sprint.

`positionAbove` (true when Orby's Y > 90px) flips the cloud above vs. below, but provides no left/right clamping. The fix is to clamp the cloud X to stay within `[0, vw - cloudWidth]` in the RAF loop.

### Orby gaps for this frontend sprint

1. **Speech cloud right-edge clamping.** Fix `OrbySpeechCloud` or `Orby.tsx`'s cloud position logic so the cloud never clips the viewport right edge.
2. **Section timing calibration.** After sections are rebuilt with new heights, verify that the scroll thresholds in `useOrbyState.ts` for the `section-comment` triggers still fire at the right visual moment.
3. **Mobile overlap check.** On 375px phones, verify Orby doesn't overlap the Lab toggle button or hero content in a distracting way. The `tooSmall` guard (560×400) may not catch all problem cases.

**Out of scope for this sprint:** OrbyCanvas.tsx model visuals, new section speech copy, the overall Orby persona voice.

---

## Part 5 — Section-by-Section Reality: What Each Component Renders Today

This is what exists RIGHT NOW, verified by reading the actual component files. Use this to know the delta between current and target.

### HeroSection (`src/components/sections/HeroSection.tsx`)
Delegates to `HeroContent.tsx`. Fetches `PROFILE_QUERY`. Renders profile image, animated headline (from `headlineAnimatedWords[]`), name, shortBio, CTA buttons. **Hero is marked done. Do not touch unless a concrete bug is found.**

### HeroTerminal (`src/components/HeroTerminal.tsx`)
The floating terminal card below the hero. Marked done.

### AboutSection (`src/components/sections/AboutSection.tsx`)
Marked done. Do not touch.

### ExperienceSection (`src/components/sections/ExperienceSection.tsx`)
- Header: **already `text-center`** — the notes say it's left-aligned, that is wrong.
- Timeline rail: gradient divs (`w-0.5`, `bg-gradient-to-b`), violet dots with `box-shadow` glow
- Renders max 5 experiences via `slice(0, 5)`
- Delegates to `ExperienceCard`

**`ExperienceCard.tsx` (`src/components/cards/ExperienceCard.tsx`) currently renders:**
- Company logo (40×40 rounded, `bg-white/[0.04]` pad)
- Position (h3), employment type chip (orbit-chip), company name (with companyWebsite link), location (MapPin icon)
- Date range (startDate / endDate / "Present" if current)
- `responsibilities[]` — up to 3, prefixed `→`
- `achievements[]` — up to 2, styled emerald with ★
- `technologies[]` — up to 4 orbit-chips with per-category color via `getCategoryColor()`
- Hover sweeping light effect (translateX gradient sweep)
- Uses `CometCard variant="dark"` with `rotateDepth={3} translateDepth={5}`

**`description` (Portable Text blocks) is NOT rendered by `ExperienceCard`.** The EXPERIENCE_QUERY fetches it, but there's no `<PortableText>` component in the card. This is the primary content gap. Adding a collapsible expand/collapse section to show the Portable Text description would complete the card.

### Projects Section (`src/components/PortfolioContent.tsx` + `ProjectsSlider.tsx`)

**Section header is in `PortfolioContent.tsx` (not in `ProjectsSlider.tsx`).** It's NOT text-centered — it's left-aligned with kicker + h2 + description. This matches what the notes say needs centering.

**`ProjectsSlider.tsx` (`src/components/three/ProjectsSlider.tsx`) currently renders:**
- 3-card visible slider (previous / center / next)
- Center card: `cosmic-card`, `cursor-default`, fully interactive
- Flanking cards: `cosmic-card--dark`, `pointer-events-none`, visually dimmed
- Each card: `coverImage` (h-40 at top), title, `tagline`, tech tags (up to 4), `ViewLiveButton` and `SourceButton` if URLs present
- `ViewLiveButton` uses `useIridescentEffect` for a shimmer on the "View Live" pill
- Navigation: ChevronLeft/ChevronRight buttons with `AnimatePresence`
- Ordered by `order asc, title asc`

**Gaps:** No 3D Three.js physics for the cards (it's Framer Motion). The flanking cards are standard HTML not positioned in 3D space. The "carousel in space" look from the notes requires rebuilding this with R3F if that's the target. However, the current implementation is clean and works — treat this as a design decision, not a broken component.

### SkillsSection (`src/components/sections/SkillsSection.tsx` + `SkillsSectionClient.tsx`)

**The skills section is NOT broken.** The earlier note calling it broken refers to an old 3D sphere visualization that was deliberately removed. The current implementation is a fully working 2D pill grid with sophisticated interactivity. A comment at the top of `SkillsSectionClient.tsx` explains:

> "The earlier Three.js/R3F skills 'sphere' visualization was intentionally removed in favor of this readable 2D layout (Phase H, Option 2)."

**What it renders:**
- Summary bar: skill count + category count
- Category chips: each shows skill count, colored per category
- Category filter pills (horizontal scroll): "All" + one per category, with unique hover micro-interactions per category:
  - `frontend` → shimmer sweep across the pill
  - `backend` → blinking cursor `_` on hover
  - `ai-ml` → `pulse-glow` animation
  - `devops`/`tools` → three animated deploy dots
  - `database`/`data-systems` → animated sparkline bars
  - `soft-skills` → `translate-y-[-2px]` lift
- Skill pills: grouped by category with category heading + description. Each pill shows skill name + proficiency level. On hover: `perspective(600px) translateY(-2px) scale(1.02)` + iridescent shimmer from `useIridescentEffect`

**`tone` and `percentage` / `yearsOfExperience` are fetched but NOT rendered.** They're available for a future data visualization (the stock-chart graph from note [[05 - Skills Capability Graph]]) but aren't displayed in the current UI.

The notes describe an ambitious stock-chart / capability graph visualization. That is the *target* state, not the current state. The current state is clean and working. The notes' graph is the upgrade target.

### EducationSection (`src/components/sections/EducationSection.tsx` + `EducationFlowchart.tsx`)

**Header is NOT text-centered** — the section-kicker + h2 are left-aligned. This is a real gap the notes correctly identify.

**`EducationFlowchart.tsx` already renders blob shapes.** The CSS classes `edu-blob--stable`, `edu-blob--forming`, `edu-blob--amoeba` are used in the component AND defined in `src/app/globals.css` with morph keyframe animations. The education section already has the blob visual treatment — the note saying "currently rendered as rectangular cards, not blobs" is WRONG.

**What the flowchart renders:**
- Sort by `startDate desc` (most recent first)
- Each item: blob shape (size/color/variant by index), `edu-connector` between items, Framer Motion `whileInView` entry
- Blob interior: institution logo if present, else `●`/`◐`/`◌` icon
- Text panel: `cosmic-card`, degree, fieldOfStudy, institution, year range, GPA chip, description (clamp-3)

**Gap:** The EDUCATION_QUERY in `queries.ts` does NOT fetch `logo`. The CertificationsSection uses logo. The EducationSection's `FlowchartItem` interface includes `logo` but the query projection doesn't include it: `*[_type == "education"] | order(startDate desc){ _id, institution, degree, fieldOfStudy, startDate, endDate, current, description, gpa }`. Logo needs to be added to the EDUCATION_QUERY.

### CertificationsSection (`src/components/sections/CertificationsSection.tsx`)

- Kicker `// credentials`, centered h2 "Certifications", left description
- 3-column responsive grid (`grid-cols-1 md:grid-cols-2 lg:grid-cols-3`)
- Uses `CometCard variant="dark"` for each cert
- Each cert-card div has the `cert-card` class — the holographic corner effect from `globals.css` is already applied via `.cert-card::after`
- Renders: logo (h-40 banner image), name, credentialId (mono tiny), issuer, issueDate, expiryDate, description (clamp-3), skills chips (up to 4), "View Credential →" link

**The `skills[]` field in the local CERTS_SECTION_QUERY is `skills[]->{ _id, name, category }`.** This works because the `certification` schema uses `skills[]`.

**Action needed:** Delete all fake AWS/GCP/CKA certification documents from Sanity Studio. The section renders nothing when empty (`if (!certs?.length) return null`).

### AchievementsSection (`src/components/sections/AchievementsSection.tsx`)

- Small section: `py-8` (not full `section-backdrop py-24`)
- Single `CometCard variant="subtle"` wrapping a vertical timeline rail
- Rail: left-side gradient line (`left-6`), dots at each row's midpoint
- Ordered by `featured desc, date desc`
- Renders: year (from `date`), featured dot (violet filled vs empty), title, type chip, issuer, description, external link button

**Gap:** No section kicker (`// credentials` or similar), no centered h2. The section header is a bare `<h2>` with no kicker or visual treatment matching the other sections.

### BlogSection (`src/components/sections/BlogSection.tsx` + `BlogFeed.tsx`)

- Shows/hides based on `siteSettings.showBlog` (Sanity toggle)
- Fetches up to 6 posts: `_id, title, slug, excerpt, externalUrl, publishedAt, readTime, category`
- Delegates to `<BlogFeed posts={list} />`
- Kicker `// uplink`, h2 "What I Read or Do", description "Resources, updates and second brain"

**AGENTS.md notes:** "`BlogFeed.tsx` contains a TODO for an archive toggle that needs a Sanity schema change." Read `BlogFeed.tsx` before touching.

### ContactSection (`src/components/sections/ContactSection.tsx` + `ContactPanel.tsx`)

- Fetches: `email`, `location`, `socialLinks{ github, linkedin, twitter, website }` from the profile singleton
- Delegates to `<ContactPanel profile={...} />`
- No kicker, no h2 in `ContactSection.tsx` — the header must be inside `ContactPanel.tsx`

### Footer (`src/components/Footer.tsx`)

Exists. Not read in detail. The notes say it's too tall and too dim — trust that.

---

## Part 6 — Corrections to the Existing Notes

A precise list of what is wrong in the notes so Cowork knows what to trust and what to discard:

### In [[09 - Sanity Content Spec]]:
- `repoUrl` → use `githubUrl` everywhere
- `skills[]→ref(skill)` for experience → use `technologies[]→ref(skill)` for experience AND projects; `skills[]` is only correct for certifications
- `skillCategory` as a document type → does not exist, do not create
- `color` field on skill → was deliberately removed, do not add back
- `familiarity (0–100)` as a field to add → already exists as `percentage (0–100)`

### In [[05 - Skills Capability Graph]]:
- "skills section is broken" → WRONG. The section works. The 3D sphere was intentionally replaced with the 2D pill grid. The capability graph (stock chart) is the TARGET state, not a fix for a broken section.
- Category buttons described as "dead" → WRONG. They work with sophisticated hover micro-interactions per category.

### In [[06 - Education Flowchart]]:
- "education rendered as rectangular cards, not blobs" → WRONG. Blob shapes (`edu-blob--stable/forming/amoeba`) are already implemented in the component and CSS.
- "stage field in Sanity" → does not exist. Stage is UI-side index logic.
- EDUCATION_QUERY does not fetch `logo` → this IS a real gap. Add `logo` to the query projection.

### In [[03 - Experience Section]]:
- "header is left-aligned" → WRONG. `ExperienceSection.tsx` already uses `text-center`. The real gap is the missing `description` (Portable Text) render in `ExperienceCard`.

### In [[00 - Frontend Overhaul — Build Plan]] Phase 0:
- "Rename `technologies[]` to `skills[]` on experience, project, certification schemas" → DO NOT DO THIS. The field names are intentionally different. Renaming would break working queries and require a Sanity data migration with no benefit.
- "Add `color`, `familiarity`, `level`, `blurb` fields to skill schema" → `percentage` and `proficiency` already exist and serve those roles. `color` was deliberately removed. Only `blurb` is genuinely missing if needed.

### In [[01 - Motion System & Comet Cards]]:
- CometCard now has 4 variants: `default`, `dark`, `subtle`, `ghost`. Notes only describe 3. The `ghost` variant was added on the `Chatbot` branch (no background class, no card shadow, capped tilt at 6°).

---

## Part 7 — Corrected Phase Order for the Frontend Sprint

The original phase order in [[00 - Frontend Overhaul — Build Plan]] has errors (see Part 6). Use this corrected version:

**Phase 0 — Real content (no schema changes required)**
1. Delete all fake certification documents from Sanity Studio.
2. Push real project content (OpsPilot, Resq, SafeReach, AI Portfolio Agent, Jarvis, Arc) with `githubUrl` resolved from GitHub. Use the `mcp__github__search_repositories` tool to find repos by name. Never invent a URL.
3. Push real experience content (BOOM Research Assistant, NSEdu, CSE Student Ambassador, Techlit). Verify all fields against the résumé.
4. Push real skills registry (the tables in [[09 - Sanity Content Spec]]). Use the actual schema field names: `name`, `category` (enum), `proficiency`, `percentage`, `tone`.
5. If Anant holds real certifications, enter them. If none currently, leave empty.
6. Fix the EDUCATION_QUERY to include `logo` in the projection.
7. Run `pnpm typegen` → `pnpm typecheck`.

**Phase 1 — Motion primitives**
Build `useSpaceFloat` hook. Confirm `CometCard` with all 4 variants (including `ghost`) is the single hover surface. These unblock every section.

**Phase 2 — Header fix (10 min)**
Wire `useTheme()` to the Moon pill in `HeaderScrolling.tsx` as described in Part 3. Change the `<div>` to a `<button>` with correct aria attributes.

**Phase 3 — ObsidianBackground enhancement**
Add `@react-three/postprocessing`. Apply `Bloom` + `additiveBlending` + `ChromaticAberration`. Verify mobile perf. Delegate to `three-artist` agent.

**Phase 4 — Per-section rebuilds (in order)**
1. Experience — add Portable Text `description` render with expand/collapse
2. Projects — center the section header in `PortfolioContent.tsx`; decide whether to rebuild the carousel in R3F or keep the current Framer Motion approach
3. Skills — build the capability graph (stock-chart) on top of the working pill grid
4. Education — center the header; fix EDUCATION_QUERY for `logo`; the blobs are already done
5. Certifications — delete fake data first; section renders correctly once real data is added
6. Achievements — add section kicker + styled h2 to match other sections
7. Blog — read `BlogFeed.tsx` first to understand the archive TODO before touching
8. Contact — read `ContactPanel.tsx` to understand current state before polishing
9. Footer — tighten height and increase contrast

**Phase 5 — Orby friction fixes**
After sections are rebuilt and heights are known: fix speech cloud right-edge clamping, verify section-comment scroll thresholds, check mobile overlap.

**Phase 6 — CSP header**
Add `Content-Security-Policy` to `next.config.ts`. The current file has HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, and Permissions-Policy — but **no CSP**. See `docs/ecc-setup-guide.md` and the `claude-code-setup/` notes. Run in report-only mode first (`Content-Security-Policy-Report-Only`).

---

## Part 8 — What Cowork Must Not Do

- **Do not commit git.** User manages all commits. `CLAUDE.md` is explicit.
- **Do not push to Vercel/remote.** User manages deploys.
- **Do not use npm or yarn.** pnpm only (`pnpm add`, `pnpm dev`, etc.)
- **Do not create `tailwind.config.ts`.** Tailwind v4 is CSS-first — all tokens in `src/app/globals.css`.
- **Do not edit `src/sanity/types/index.ts`.** It is generated. Run `pnpm typegen` after schema changes.
- **Do not hardcode any content that belongs in Sanity.**
- **Do not invent GitHub URLs, live URLs, or credential IDs.** Leave fields empty and note "needs real URL" if not found via MCP.
- **Do not rename `technologies[]` to `skills[]`** on experience or project schemas. This would break working queries.
- **Do not add `color` back to the skill schema.** It was deliberately removed.
- **Do not touch `src/app/api/` or `src/lib/chat-*`.** Those are the chatbot layer, Cowork does not own them.
- **Do not touch `OrbyCanvas.tsx`.** The 3D model is out of scope.
- **Do not redesign HeroSection, HeroTerminal, or AboutSection.** They are marked done.
- **Do not add ESLint, Prettier, or `tailwind.config.ts`.** Biome is the only linter/formatter.
- **Do not create `src/pages/`.** This is App Router — all pages live in `src/app/`.

---

## Quick-Reference: Key File Paths

| What | Path |
|---|---|
| Three.js background (physics) | `src/components/three/ObsidianBackgroundCanvas.tsx` |
| Three.js background (dynamic wrapper) | `src/components/three/ObsidianBackground.tsx` |
| Header with dark mode toggle | `src/components/HeaderScrolling.tsx` |
| Theme provider | `src/components/ThemeProvider.tsx` |
| CometCard primitive (4 variants) | `src/components/ui/comet-card.tsx` |
| Page section composition | `src/components/PortfolioContent.tsx` |
| Hero section | `src/components/sections/HeroSection.tsx` |
| Experience section | `src/components/sections/ExperienceSection.tsx` |
| Experience card | `src/components/cards/ExperienceCard.tsx` |
| Projects carousel | `src/components/three/ProjectsSlider.tsx` |
| Skills (server) | `src/components/sections/SkillsSection.tsx` |
| Skills (client, interactive) | `src/components/sections/SkillsSectionClient.tsx` |
| Education (server) | `src/components/sections/EducationSection.tsx` |
| Education flowchart | `src/components/EducationFlowchart.tsx` |
| Certifications | `src/components/sections/CertificationsSection.tsx` |
| Achievements | `src/components/sections/AchievementsSection.tsx` |
| Blog | `src/components/sections/BlogSection.tsx` |
| Contact | `src/components/sections/ContactSection.tsx` |
| Orby main | `src/components/orby/Orby.tsx` |
| Orby state machine | `src/components/orby/useOrbyState.ts` |
| Orby 3D figure | `src/components/orby/OrbyCanvas.tsx` |
| Orby speech cloud | `src/components/orby/OrbySpeechCloud.tsx` |
| Lab/chat sidebar | `src/components/lab/PortfolioLab.tsx` |
| All shared GROQ queries | `src/sanity/lib/queries.ts` |
| Sanity schema types (do not edit) | `src/sanity/types/index.ts` |
| Sanity schema files | `src/sanity/schemaTypes/` |
| Global CSS / design tokens | `src/app/globals.css` |
| Security headers | `next.config.ts` |

## Quick-Reference: Schema Field Names

| Schema type | Skill/tech field | Correct GROQ |
|---|---|---|
| `experience` | `technologies[]` | `technologies[]->{ _id, name, category, ... }` |
| `project` | `technologies[]` | `technologies[]->{ _id, name, category, ... }` |
| `certification` | `skills[]` | `skills[]->{ _id, name, category }` |
| `project` GitHub URL | `githubUrl` | `githubUrl` |
| `project` live URL | `liveUrl` | `liveUrl` |
| `project` short desc | `tagline` | `tagline` (no `description` on project) |
| `experience` company URL | `companyWebsite` | `companyWebsite` |
| `skill` numeric proficiency | `percentage` | `percentage` (0–100) |
| `skill` named proficiency | `proficiency` | `proficiency` (beginner/intermediate/advanced/expert) |

## Quick-Reference: Commands

```bash
pnpm dev          # dev server
pnpm typegen      # regenerate Sanity types (after any schema change)
pnpm typecheck    # TypeScript strict (run after typegen)
pnpm lint         # Biome check
pnpm format       # Biome format --write
pnpm build        # full production build (runs typegen + typecheck + next build)
pnpm test         # Vitest run
```

---

## Log

- **2026-06-12 v1:** Created by Claude Code (Sonnet 4.6) after initial file reads — verified schema files, main section components, ObsidianBackground, HeaderScrolling, ThemeProvider, Orby.tsx, CometCard.
- **2026-06-12 v2:** Full deep-read pass completed. Added verified details from: SkillsSectionClient.tsx (full interactive pill grid with per-category effects — section is NOT broken), EducationFlowchart.tsx (blobs already implemented), ExperienceCard.tsx (exact field render inventory), ProjectsSlider.tsx (exact card structure), AchievementsSection.tsx, CertificationsSection.tsx, BlogSection.tsx, ContactSection.tsx, all Sanity schema files in full, queries.ts in full, next.config.ts (CSP gap confirmed), AGENTS.md, Orby.tsx / OrbyCanvas.tsx / OrbySpeechCloud.tsx / useOrbyState.ts in full. Removed the branch cleanup section (not related to frontend build). Corrected major errors in existing notes: skill schema is richer than assumed, skills section is not broken, education blobs are already implemented, experience header is already centered, technologies[] rename instruction is wrong.

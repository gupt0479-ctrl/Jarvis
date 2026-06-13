---
type: concept
status: active
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - status
  - gap-analysis
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[claude-code-setup/03 - Per-Phase Build Prompts]]"
---
# Frontend Build Status — What's Left, What's Broken, What Was Missed

> Written 2026-06-12 after reading all 14 frontend notes (00–13) plus all 4 claude-code-setup notes. Ground truth is [[10 - Codebase Reality & Confusion Clearance]] — every factual claim here is reconciled against it. The build prompts in [[claude-code-setup/03 - Per-Phase Build Prompts]] define the exact execution order.

---

## TL;DR

| Phase | What | Status |
|---|---|---|
| 0 | Real content + 2 schema touches | ❌ Not done |
| 1 | Motion primitives (`useSpaceFloat` + `SpaceRail`) | ❌ Not done |
| 2 | Header theme pill semantic fix | ❌ Not done (~10 min) |
| 3 | ObsidianBackground post-processing | ❌ Not done |
| 4a | Experience — Portable Text + rail | ❌ Not done |
| 4b | Projects — header centre + space carousel enhancements | ❌ Not done |
| 4c | Skills — capability graph on top of working pill grid | ❌ Not done |
| 4d | Education — centre header + logo + off-axis + pulse connector | ❌ Not done |
| 4e | Certifications — delete fakes + centre description | ❌ Not done |
| 4f | Achievements — kicker + SpaceRail outside box | ❌ Not done |
| 4g | Blog — CometCard polish on both card types | ❌ Not done |
| 4h | Contact — glass frame + localized scrim | ❌ Not done |
| 4i | Footer — compact rebuild | ❌ Not done |
| 5 | Orby friction fixes | ❌ Not done (needs Phase 4 heights) |
| 6 | CSP header + a11y pass | ❌ Not done (must run last) |

**Nothing in Phase 0–6 has been built yet.** Hero, HeroTerminal, and About are complete and must not be touched. Everything else is either unbuilt, partially present, or incorrectly described in earlier notes.
## Sanity Fixes

## UI Fixes
1. Experience: The "contract, internship, freelance, etc." should render next to the location. The achievements are in yellow/gold which looks so weird and shitty. Match the color with the theme of my website and the card color, maybe blueish or purpleish. I want the description to show up only when the user clicks on the experience. This button (more) on the bottom right of each card. very subtle and almost not visible to the user because if the user clicks on the experience the description shows up. The entire experience card should not occupy the entire screen though. The drop down should be small. The comet card on experiences need to be dialed down by a bit, they are moving way too much hovering. Just reduce it a little bit.  
2. These skills might need to be set up properly on sanity but make sure that these are not hard coded. Everything in the experience cards should be rendered from sanity. The dot color next to each skill text inside the box should also be coming from sanity based on the color selected on sanity.

3. Projects: The comet card effect on the center project is a little too much and needs to be brought down a notch. It should still have the same hover effect but the comet is just dialed down. The space that it wiggles around should be limited to it's padding. The cards on the left and right should only have a comet card effect when they appear in the center(correct). Right now they are translucent, prefer it that way. I want these two left and right cards to wandering at the same opacity they are at(correct). When hovered I do not want the left and right cards also to move down, right now they move down as the center card gets hovered. They should be independent of the hover and continue to wiggle around in their space. The "case note" should not be there, just the summary of the project right in that box. Nothing more than the summary, good that you cut off the summary because it got too long. Keep all projects the same way. Each project should not cross more than 4 skills as well, do not render more than 4 skills.
4. Sanity: There is a cover image for projects which is really cool and I like it but that's a required field or the sanity will not publish because it is empty. Remove that requirement for each and every single project. what even is this: "Visibility: Featured, Standard"? It just adds a star to my projects on sanity, what else does it even do? It seems useless to me, remove it.  

5. Skills: There is a colored skill boxes which is rendering on top of the graph and the skills categories. Let's remove that entirely, the number: "56 skills across 10 categories" should appear on top of the skills category on the right side but this should not take extra space. The graph and the skill categories should be on the same line(alignment). I also want to remove the "all" button entirely, there should be no all section in the skills because it elongates the skill section by a lot. The skills and expertise graph looks good now. I want it to appear as a trading stock graph sort of with multiple trajectories as lines such as ai, devops etc. This graph should go up and down basically and each of the lines are not the same ups and downs. Right now, they follow almost the same trajectory as other skill categories. Each skill category should be slightly different even if they are intermediate or advanced. The buttons for each skill category have been listed and it should appear exactly like that. The "mobile, soft skills and testing" have the same effect on the buttons, let's give them unique effects. All these skills should be listed in sanity and this should be concrete. Right now they do not have a color(the color dot rendering everywhere on my potfolio) section in sanity, let's add that. We are going to use the skill color and name to be rendered all across the website. We have this on sanity which does not do anything: "Tone, Used to style badges consistently without hardcoding colors: Neutral, Accent, Highlight, Muted". These should be changed to render the dot next to the skill all over the portfolio. But on the skills section these colors do not render - only the hover effect and the skill level. 
6. Buttons: The buttons below the skills section are complete garbage, they look so shit. They repeat the same behavior on hover repeatedly. Let's do it this way: Each skill category has approx 5-10 skills listed in them, I want each of these 5-10 skills to have a different hover effect per 7 skills. 3 of them can be repetitive, main goal is this have 7 effects in total. I want each skills section to have something unique in them. Firstly, all the skills are being rendered right now which is a really long list, remove that. Let's update out sanity from rendering all skills to a systematic approach - skill categories first upon loading the sanity and then we can see the skills listed under each category. On automatic the most high level skill category renders first and the user is able to pick which skill category he wants to see on top of all the skills listed like right now. Second, the skills category have some features on hovering right now which need to be enhanced completely, mentioned above clearly. Thirdly, upon hovering the skills boxes become bigger - each box should be fixed and upon hover the skill box shape or the size should not change.

7. 

---

## Phase 0 — Real Content + 2 Schema Touches

**Status: NOT STARTED**

This is the prerequisite for all section rebuilds. No UI work should start before this is done.

### The only two schema changes needed

1. **Add `summary` (text) field to `project` schema** (`src/sanity/schemaTypes/project.ts`) — the long-form hover detail the carousel needs. Not `description` (project has no description field). After: add `summary` to `PROJECTS_QUERY`, run `pnpm typegen`.
2. **Add `logo` to `EDUCATION_QUERY` projection** in `src/sanity/lib/queries.ts` — the query projection already fetches everything except logo. No schema change needed, just query fix. After: run `pnpm typegen`.

### Content to push into Sanity Studio

**Skills registry** — push all real skill documents with fields: `name`, `category` (enum), `proficiency`, `percentage` (0–100, the graph line value), `yearsOfExperience`, `tone` (neutral/accent/highlight/muted). No `color` field. Reference [[09 - Sanity Content Spec]] section 2 for the full list per category.

**Projects** — push 6 projects: OpsPilot, Resq, SafeReach, AI Portfolio Agent (this site), Jarvis, Arc. Each needs: `title`, `slug`, `tagline`, `summary` (new field), `technologies[]` refs, `githubUrl` (NOT `repoUrl`) resolved via `mcp__github__search_repositories`, `coverImage`, `category`, `visibility` (featured/standard), `order`. Leave `liveUrl` empty where undeployed — never invent. Reference [[09 - Sanity Content Spec]] section 3 for the full spec per project including the exact summary paragraphs.

**Experience** — push 4 entries: BOOM Research Assistant (UMN, contract), NSEdu Full Stack Intern, TechLit Web Developer, Entrepreneur (placeholder). Each needs: position, company, `companyWebsite` (NOT `companyUrl`), dates, `employmentType`, `tenure`, `responsibilities[]` (≤3), `achievements[]` (≤2), `technologies[]` refs (≤4), `description` (Portable Text). Reference [[09 - Sanity Content Spec]] section 4.

**Delete fake certifications** — AWS SA-Pro, GCP PCA, CKA, TensorFlow Developer, MongoDB Developer do not belong to Anant. Delete them from Studio before any frontend cert work. The section returns `null` when empty — this is fine.

**Real certifications** — ask Anant which certs are real; enter only those. Never invent.

### What NOT to do in Phase 0

- **Do NOT rename `technologies[]` → `skills[]`** on experience or project types. The field names are intentional and the queries work. This rename was listed in the original Phase 0 plan and is WRONG.
- **Do NOT add `color`, `familiarity`, `level`, or `blurb` fields** to skill. `percentage` and `proficiency` already cover those roles; `color` was deliberately removed.
- **Do NOT create a `skillCategory` document type.** Categories are string enums on the `skill` doc. Client-side `CATEGORY_COLORS` handles display.

---

## Phase 1 — Motion Primitives

**Status: NOT STARTED**

Must complete before Phase 4 section rebuilds.

### `useSpaceFloat` — build from scratch

A new hook. Does not exist yet. Spec:
- Bounded zero-gravity drift using 2–3 low-frequency sines per axis with random per-instance phase offsets
- Transform-only (CSS `transform` on a ref) — no layout-affecting animation
- Hover does NOT stop the drift
- `prefers-reduced-motion`: returns a static/frozen transform
- One shared rAF ticker or Framer's batched scheduler — do not create a ticker per hook instance

Apply on the outer wrapper; `CometCard` tilt goes on the inner layer. Never both on the same element.

### `SpaceRail` — extract from ExperienceSection

The Experience section already has a timeline rail (gradient divs, violet dots with box-shadow glow). Extract it into a shared `SpaceRail` component so Achievements can reuse it. The extracted component should add: scroll-progress fill (the rail visually fills as user scrolls past the section), a slow breathing wiggle. Even dot glow, smooth gradient.

### CometCard — no new work needed

`CometCard` already exists at `src/components/ui/comet-card.tsx` with 4 variants: `default`, `dark`, `subtle`, `ghost`. The `ghost` variant (no background, no shadow, 6° max tilt) was added in the Chatbot branch — the earlier notes only described 3 variants, that was stale. Do not rebuild CometCard. Confirm it is the single hover/tilt surface everywhere.

---

## Phase 2 — Header Theme Pill

**Status: NOT STARTED (~10 minutes of work)**

**File:** `src/components/HeaderScrolling.tsx`, ~lines 167–170

The "Dark" pill in the header is a **decorative `<div>`** — Moon icon + the word "Dark" — with no `onClick`, no `useTheme()`, no state. `ThemeProvider` (`src/components/ThemeProvider.tsx`) is correctly wired with `next-themes` and `defaultTheme="dark"`. The infrastructure exists; the pill is just not connected.

**What to do:** Convert the `<div>` to a `<button>` that uses `useTheme()`, has a documented no-op `onClick` (light mode not yet designed), `aria-label="Color theme — dark mode active (light mode coming soon)"`, and `cursor-default` to prevent a pointer cursor on a noop.

**What NOT to do:** Do not build a light mode palette. The entire design system — every `cosmic-card`, `float-btn`, `section-kicker`, `orbit-chip` token — is defined only inside the `.dark {}` block in `globals.css`. There is no light palette. A real light mode is a full design-system rewrite. That is explicitly deferred.

---

## Phase 3 — ObsidianBackground Enhancement

**Status: NOT STARTED**

**Delegate to `three-artist` agent. Do NOT touch the physics.**

### What already exists (do not rebuild)

`ObsidianBackgroundCanvas.tsx` is 836 lines of a full physics simulation: fibonacci sphere (2,800 pts desktop), tilted torus ring (2,000 pts), starfield (5,500 pts), `LineSegments` connecting nearby points. Physics: spring-return dots, **magnetic cursor dent** (facing dots pulled to cursor), **click burst** radial ripple, **scroll-progressive `stretchT`** ramps 0→1 over bottom 60% of scroll (stiffer springs, deeper displacement, camera zoom path). Soft-glow sprite `alphaMap`, DPR capped at 1.25, `antialias:false`, sidebar-aware 448px right-edge shift, `prefers-reduced-motion` guard. This is already impressive. Do not touch it.

### What's missing (the visual gap)

No `@react-three/postprocessing`. No Bloom. No additive blending. No ChromaticAberration. The glow is purely from the sprite alphaMap. This is why the scene looks good but not premium.

### What to add

**Tier 1 (transforms the scene, do these):**
1. Check if `@react-three/postprocessing` is in `package.json`. If absent: `pnpm add @react-three/postprocessing`.
2. Wrap the Canvas scene in `<EffectComposer>`. Add `<Bloom luminanceThreshold={0.18} luminanceSmoothing={0.9} intensity={0.35} />`. Tune until luminous, not blown out.
3. Switch planet + ring `PointsMaterial` to `additiveBlending`. Drop base opacity from ~0.52/0.46 to ~0.30–0.35.

**Tier 2 (meaningful polish):**
4. `<ChromaticAberration offset={[0.0004, 0.0004]} />` inside the EffectComposer.
5. Slow HSL hue drift: derive `COL_PLANET` from elapsed `t * 0.003` seconds, drifting `#9D8BBF` ↔ `#8BBFC0` over ~60 seconds.

**Performance gate (mandatory):** Keep DPR at 1.25. After adding Tier 1, test on mid-range mobile. If <~50fps: `const skipEffects = isMobile || prefersReducedMotion` and only wrap with `EffectComposer` when `!skipEffects`.

---

## Phase 4 — Per-Section Rebuilds

Each section is independent; they can run in parallel sessions. Read the relevant Part 5 section in [[10 - Codebase Reality & Confusion Clearance]] plus the section's design note before touching any component.

---

### 4a — Experience Section

**File:** `src/components/cards/ExperienceCard.tsx` + `src/components/sections/ExperienceSection.tsx`

**Already works (do not redo):**
- Header is already `text-center` — note 03 said left-aligned, that was WRONG
- Company logo, position, type chip, company link, date range render correctly
- `responsibilities[]` (up to 3, prefixed `→`), `achievements[]` (up to 2, styled emerald `★`), `technologies[]` chips (up to 4) all render
- Hover sweeping light effect exists
- Uses `CometCard variant="dark"` already

**Still left to build:**
1. **Portable Text `description`** — the EXPERIENCE_QUERY fetches `description` but `ExperienceCard.tsx` has no `<PortableText>` render. Add a collapsible expand/collapse section (subtle bottom-right chevron toggle) that reveals the Portable Text blocks. Use `@portabletext/react`.
2. **Recolour achievements off green** — the `★` achievement chips are currently emerald green. Change to a neutral accent (violet or cyan) to stop them reading as "completed task" status indicators.
3. **Add `useSpaceFloat`** to each card's outer wrapper (after Phase 1).
4. **`SpaceRail` breathing** — replace the static timeline rail with the extracted `SpaceRail` component from Phase 1 (scroll-progress fill + slow breathing wiggle).

---

### 4b — Projects Section

**Files:** `src/components/PortfolioContent.tsx` + `src/components/three/ProjectsSlider.tsx`

**Already works (do not redo):**
- 3-card Framer Motion slider renders, navigation works
- CometCard on center card, dimmed flanking cards
- `coverImage`, `tagline`, tech tags (up to 4), source/live buttons render
- `useIridescentEffect` shimmer on "View Live" pill already in place
- The decision to use Framer Motion (not R3F) for the carousel is a validated design decision — do not rebuild in Three.js

**Still left to build:**
1. **Centre the section header** — the kicker + h2 + description in `PortfolioContent.tsx` are left-aligned. Centre them.
2. **Space motion on cards** — centre card gets `CometCard` + `useSpaceFloat`; side cards get `useSpaceFloat` drift-only with no CometCard tilt and `pointer-events-none`.
3. **Tether transition** — elastic spring (or rubber-band Framer spring) between card slides so the center card has a settling bounce.
4. **Orbit dot pagination** — replace or supplement ChevronLeft/Right with small orbital dots indicating current position.
5. **Hover detail** — reveal `summary` (new field from Phase 0) on hover/focus of center card, plus conditional Source (`githubUrl`) and View-Live (`liveUrl`) buttons — hide View-Live when `liveUrl` is empty, cap revealed area height with overflow scroll.

---

### 4c — Skills Section

**Files:** `src/components/sections/SkillsSection.tsx` + `src/components/sections/SkillsSectionClient.tsx`

**Already works (do not redo — the section is NOT broken):**
- 2D pill grid with category filter is fully working
- Per-category hover micro-interactions: `frontend` shimmer sweep, `backend` blinking cursor `_`, `ai-ml` pulse-glow, `devops/tools` animated deploy dots, `database` sparkline bars, `soft-skills` translate lift
- Category filter chips are interactive, not dead
- `tone` and `percentage` are fetched but not yet rendered anywhere

**Still left to build (ADD these on top of the working grid — do not remove anything):**
1. **Stock-chart capability graph** — Recharts line chart, per-category lines, X axis = 2021–2026, Y axis = Familiarity / Applied Depth (0–100, sourced from `percentage`). Default-open category: `ai-ml` (violet line). Hover: individual line highlight + tooltip with skill name + percentage. Insight panel: 1-2 sentence synthesis per active category, shown below the chart. Use `CATEGORY_COLORS` for line colours for consistency.
2. **Category pills get `useSpaceFloat` + `CometCard`** (after Phase 1).
3. **Compact pill sizing** — proficiency level shown only on hover (currently always visible). Keep skill name always visible.
4. **Cycle through 7 distinct per-skill effects** — shimmer is already 1 of 7. Define 6 more. Apply cyclically (e.g. `index % 7` picks the effect). The existing per-category effects stay on the category pills; these 7 are for individual skill pills.

---

### 4d — Education Section

**Files:** `src/components/sections/EducationSection.tsx` + `src/components/EducationFlowchart.tsx`

**Already works (do not redo):**
- Blob shapes exist: `edu-blob--stable`, `edu-blob--forming`, `edu-blob--amoeba` CSS classes are in `globals.css` with morph keyframes — note 06 saying "rectangular cards" was WRONG
- Stage assignment is UI-side: first item → stable, second → forming, third → amoeba (by sort order index, not Sanity field)
- Framer Motion `whileInView` entry animations
- Text panels with degree, institution, year, GPA chip, description (clamp-3)

**Still left to build:**
1. **Centre the section header** in `EducationSection.tsx` — kicker + h2 are left-aligned.
2. **Add `logo` to EDUCATION_QUERY** (Part of Phase 0, but the UI also needs to use it): once the query fetches `logo`, mask it to the blob perimeter (clip-path matching the blob CSS shape).
3. **Off-axis layout** — items currently lay out in a single column. Rearrange: high school mid-right, middle school high-left, college (UMN, most recent) near-centre. Use absolute/relative positioning with Framer `whileInView`.
4. **Living-pulse connector** — the current `edu-connector` is a static gradient line. Replace with an upward-looping glow pulse (a dot or glow travels upward along the line in a continuous loop, suggesting energy flowing from origins to present).
5. **Reduced-motion fallback** — static layout with no connector animation when `prefers-reduced-motion`.

---

### 4e — Certifications Section

**File:** `src/components/sections/CertificationsSection.tsx`

**Already works (do not redo):**
- 3-column grid with `CometCard variant="dark"` per cert
- Holographic `.cert-card::after` corner effect from `globals.css` already applied
- `skills[]→{ _id, name, category }` query is already correct (certifications use `skills[]`, not `technologies[]`)
- Section returns `null` when empty

**Still left to build:**
1. **Delete fake certs** (Phase 0 content task) — AWS SA-Pro, GCP PCA, CKA, TensorFlow Developer, MongoDB Developer. Must happen before any visual work so you're working with real data.
2. **Centre description text** — the cert card description is currently left-aligned. Centre it.
3. **Shared category chips** — confirm skills chips use `CATEGORY_COLORS` consistently (no hardcoded `color` field on skill — color is derived from category). Should already be the case; verify.

---

### 4f — Achievements Section

**File:** `src/components/sections/AchievementsSection.tsx`

**Already works (do not redo):**
- Timeline rail inside a `CometCard variant="subtle"` wrapper exists
- Renders year, featured dot (violet filled vs empty), title, type chip, issuer, description, external link

**Still left to build:**
1. **Add section kicker + styled h2** — currently a bare `<h2>` with no kicker label. Add kicker (e.g. `// milestones` or similar, in monospace cyan-muted style matching other sections) and a centered h2 that matches the design system.
2. **Move `SpaceRail` outside the CometCard box** — the timeline rail should run as a standalone `SpaceRail` component (from Phase 1) on the left of the section, with achievement cards floating to the right. The rail being inside the card wrapper is the current structure; it needs to come out.
3. **Years tight to titles** — tighten the spacing between the year badge and the achievement title.

---

### 4g — Blog Section

**Files:** `src/components/sections/BlogSection.tsx` + `src/components/BlogFeed.tsx`

**Already works (do not redo):**
- Kicker `// uplink`, h2 "What I Read or Do" already present
- Sanity-driven (fetches ≤6 posts: title, slug, excerpt, externalUrl, publishedAt, readTime, category)
- `siteSettings.showBlog` gate works

**Still left to build:**
1. **Read `BlogFeed.tsx` FIRST** — AGENTS.md notes a TODO for an archive toggle that needs a Sanity schema change. Understand the shape of the TODO before touching anything, to avoid unblocking half-done work.
2. **GitHub pinned card polish** — the GitHub card already has a wobble (`useSpaceFloat` equivalent?) and bottom-lift hover. Add `CometCard` polish while keeping: solid background (no change), left violet rail, icon, copy, Visit action, liked bottom-lift hover.
3. **Small resource cards** — add `CometCard` with a **more translucent** background than the GitHub card (the small cards are the ones that go translucent; the GitHub card stays solid). Add: category chip, title, excerpt, date/read-time, open icon.
4. **Legibility** — ensure the background sphere doesn't wash out text on any card.

---

### 4h — Contact Section

**Files:** `src/components/sections/ContactSection.tsx` + `src/components/ContactPanel.tsx`

**Already works (do not redo):**
- Fetches `email`, `location`, `socialLinks{ github, linkedin, twitter, website }` from profile singleton
- Delegates to `ContactPanel.tsx`
- The existing buttons + social pop-out are noted as good — keep them

**Still left to build:**
1. **Read `ContactPanel.tsx` first** to understand what the header/kicker/h2 currently look like (they live inside ContactPanel, not ContactSection).
2. **"Frame not fill" glass card** — make the card an open glass frame: thin luminous border + soft outer glow, interior largely transparent so the background sphere shows through. The card marks a region in space, not a solid block.
3. **Localized legibility scrim** — soft radial `backdrop-filter: blur` + slight darken hugging **only** the email, Copy/Open-Mail buttons, and social row. Fades to nothing at card edges. Background is gorgeous everywhere except a gentle halo behind the words.
4. **Copy/heading** — kicker `// uplink`, heading "Let's build something,", subhead "Internships, collaborations, or just to say hi." Email + socials from the profile singleton.

---

### 4i — Footer

**File:** `src/components/Footer.tsx`

**Already exists (but reportedly too tall and too dim).**

**Still left to build — compact rebuild:**
1. **Left edge:** `</>` programmer glyph (not emoji)
2. **Right edge:** `© 2026 Anant Gupta · building in public`
3. **Centre:** "Back to top" button, centred, wrapped in `CometCard`
4. **Text legibility:** raise to normal legibility (not glowing, not dim — readable)
5. **Height:** shrink to only what the content needs
6. **Surface:** very subtle `border-top`, translucent background so the page background bleeds into it

---

## Phase 5 — Orby Friction Fixes

**Status: NOT STARTED — must run AFTER Phase 4 (needs final section heights)**

**Do NOT touch `OrbyCanvas.tsx`.** The 3D model, persona voice, new section speech copy, and chat-navigation pipeline are all out of scope.

### Three frictions to fix

1. **Speech cloud right-edge clamping** — `OrbySpeechCloud.tsx` has no viewport horizontal clamping. When Orby is at home position (far right), the cloud clips off-screen on narrow viewports. `positionAbove` flips above/below but does no left/right clamp. Fix: clamp cloud X to `[8, vw - cloudWidth - 8]` in the RAF position logic in `Orby.tsx`.

2. **Section-comment scroll threshold recalibration** — `useOrbyState.ts` fires `section-comment` speech for `projects`, `blog`, and `contact` sections at hardcoded scroll percentages. After section heights change in Phase 4, verify these thresholds still trigger at the right visual moment. Adjust if not.

3. **Mobile overlap check (375px)** — the `tooSmall` guard hides Orby when `innerHeight < 560 && innerWidth < 400`. On phones that pass this guard but are still narrow, verify Orby doesn't overlap the Lab toggle button or hero content distractingly. Add a small offset or guard if needed.

---

## Phase 6 — CSP Header + A11y Pass

**Status: NOT STARTED — must run LAST (needs the finished page to verify zero violations)**

### CSP gap

`next.config.ts` already has: `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`. **CSP is missing entirely.**

Add `Content-Security-Policy` in **report-only mode first** (`Content-Security-Policy-Report-Only`). Verify zero violations across:
- ObsidianBackground Three.js canvas render
- Sanity images via `cdn.sanity.io`
- Orby's `/api/chat` + Upstash calls
- All section media

Switch to enforcing CSP once clean. Drop `'unsafe-eval'` in production if the stack allows. Use `security-reviewer` agent for this phase.

### A11y pass

- Accessible names on all icon-only buttons (carousel arrows, expand toggles, category buttons, back-to-top)
- Keyboard navigation for the Projects carousel
- No text overlap at mobile / 1280px / wide viewports
- `prefers-reduced-motion` respected in every animated component (ObsidianBackground, useSpaceFloat, EducationFlowchart connectors, timeline rails)

---

## What Was Done Incorrectly (Corrections to the Build Plan)

These items from the earlier build plan notes are **wrong** per [[10 - Codebase Reality & Confusion Clearance]]. Do not follow them.

| What the notes said | What is actually true |
|---|---|
| Phase 0: rename `technologies[]` → `skills[]` on experience + project | DO NOT DO THIS. Field names are correct. Renaming breaks working queries with no benefit. |
| Add `color`, `familiarity`, `level` fields to skill schema | `percentage` (0–100) and `proficiency` (enum) already serve these roles. `color` was deliberately removed. |
| Create `skillCategory` as a Sanity document type | Does not exist, should not be created. Categories are string enums on `skill`. |
| Notes 03: experience header is left-aligned | WRONG. `ExperienceSection.tsx` already uses `text-center`. |
| Note 05: skills section is broken, 3D sphere removed incorrectly | WRONG. The 3D sphere was intentionally replaced with the 2D pill grid in Phase H. The section works. |
| Note 06: education rendered as rectangular cards | WRONG. Blob shapes (`edu-blob--stable/forming/amoeba`) are already implemented in the component and CSS. |
| Note 06: `stage` is a Sanity field | Does not exist. Stage is UI-side index logic (first item = stable, etc.). |
| Notes use `repoUrl` for project | Wrong field name. The actual field is `githubUrl`. |
| Notes use `skills[]→ref(skill)` for experience + project | Wrong. Experience and project use `technologies[]→ref(skill)`. Only certification uses `skills[]`. |
| Note 01: CometCard has 3 variants | CometCard has 4 variants: `default`, `dark`, `subtle`, `ghost`. The `ghost` variant was added in the Chatbot branch. |
| Note 09: `description` is a project field | Project has `tagline` (short). No long `description` field on project. The new field is `summary` (added in Phase 0). |
| `companyUrl` for experience | Wrong. The actual field is `companyWebsite`. |

---

## What Was Missed Entirely

Items not mentioned anywhere in the build plan notes but significant for implementation:

1. **`useIridescentEffect` is already in use** — `ProjectsSlider.tsx` uses it for the "View Live" shimmer. `SkillsSectionClient.tsx` uses it for skill pill hover. Don't rebuild this; use the existing hook.

2. **ObsidianBackground is already sidebar-aware** — it shifts its right edge 448px when the Lab sidebar opens, animated with cubic-bezier. This is already implemented. The Phase 3 enhancement notes don't mention this; don't break it.

3. **`stretchT` scroll-progressive physics already in ObsidianBackground** — the background intensifies physics and moves the camera as the user scrolls. Phase 3 adds post-processing on top; the scroll physics are already there.

4. **`SpaceRail` must be extracted FROM Experience** — it's not built from scratch. The existing gradient-divs + dot timeline in ExperienceSection is the source; Phase 1 extracts it into a shared component. Note 01 implies building SpaceRail new, but it comes from the current Experience implementation.

5. **BlogFeed.tsx archive toggle TODO** — AGENTS.md flagged a TODO in BlogFeed.tsx that requires a Sanity schema change before the blog can add an archive toggle. This must be understood before touching blog UI. The notes mention it but treat it as trivial; it's a gating concern for the blog section.

6. **Orby `chat-nav-home` / `chat-nav-arrival` states are already wired** — the CustomEvent `orby:navigate` interface is already implemented in `useOrbyState.ts`. Phase 7 chatbot wiring is not frontend build work; it's chatbot work. Phase 5 (Orby frictions) only fixes viewport clamping and scroll thresholds.

7. **`OrbySpeechCloud` hides when sidebar is open** — `cloudVisible = speechText !== null && !sidebarOpen`. This collision avoidance is already implemented. Phase 5 doesn't need to re-implement it.

8. **`CometCard ghost` variant** — added in the Chatbot branch (no background class, no card shadow, max 6° tilt). The notes describe only 3 variants. If ghost is already present in the file, don't add it again.

9. **CATEGORY_COLORS is in `SkillsSectionClient.tsx` AND `ExperienceCard.tsx`** — colors are derived from category at render time in both components. If a new section needs category colors, import or reuse the same map rather than duplicating.

10. **Sanity `profile.stats[]`** — the profile singleton has a `stats[]` array of `{label, value}` objects. This is used in About/Hero and is not to be touched, but could be useful for Skills section insight panel copy.

---

## Sequencing Rules

Per [[claude-code-setup/03 - Per-Phase Build Prompts]]:

- **Phase 0 and Phase 1 are prerequisites.** Nothing in Phase 4 should start without both done.
- **Phases 2 and 3** are independent — can run in parallel with Phase 0 and each other.
- **Phase 4 sections** are independent of each other — can parallelize across sessions.
- **Phase 5** needs final section heights → runs after all Phase 4 sections complete.
- **Phase 6** needs the finished page → runs absolutely last.

Each phase should run in its own `/clear` session using the prompt from [[claude-code-setup/03 - Per-Phase Build Prompts]]. Every session ends with `pnpm typecheck` passing before the session closes.

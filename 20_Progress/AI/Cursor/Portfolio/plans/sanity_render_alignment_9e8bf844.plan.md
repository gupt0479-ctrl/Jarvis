---
name: Sanity Render Alignment
overview: Audit every Sanity field against GROQ queries and UI components, fix schema drift causing Studio errors, and wire missing fields so the landing page reflects CMS content instead of hardcoded or orphaned data.
todos:
  - id: fix-about-telemetry-matching
    content: "Fix AboutTelemetry stat matching: replace keyword matching with direct pass-through of Sanity stats"
    status: in_progress
  - id: experience-card-fields
    content: Render companyLogo, employmentType, achievements (max 2), companyWebsite in ExperienceCard
    status: pending
  - id: education-logo-description
    content: Add logo to EDUCATION_SECTION_QUERY and render it + description in EducationFlowchart
    status: pending
  - id: certs-expiry-credentialid
    content: Add expiryDate to CERTS_SECTION_QUERY; render expiryDate and credentialId in CertificationsSection
    status: pending
  - id: achievements-issuer
    content: Add issuer to ACHIEVEMENTS_SECTION_QUERY and render below title in AchievementsSection
    status: pending
  - id: projects-coverimage
    content: Render coverImage in ProjectCard using next/image + urlFor
    status: pending
  - id: skills-graph
    content: Decide fate of skills graph — restore Three.js sphere viz or document intentional removal
    status: pending
  - id: site-settings-gate
    content: Gate BlogSection on siteSettings.showBlog; use siteLogo in header or OG image
    status: pending
  - id: schema-drift-migration
    content: "Sanity content: migrate current→tenure on experience, featured→visibility on projects, remove color from skills"
    status: pending
  - id: replace-seed-content
    content: "Studio: replace 6 seed projects, remove fake certs, fill profile.stats with real KPI labels"
    status: pending
  - id: verify-build-qa
    content: Run typegen/typecheck/test/build + section-by-section visual QA
    status: pending
isProject: false
---

# Sanity ↔ Website Render Alignment — Precise Audit

> This plan was produced by a full codebase read of every section component, card, query, and schema.
> It supersedes the earlier Cursor plan which had several inaccuracies.
> All file:line references are verified against the live source tree.

---

## How content flows

```
Sanity CMS
  └─ sanityFetch() [src/sanity/lib/live.ts]
       └─ GROQ query [src/sanity/lib/queries.ts or inline defineQuery]
            └─ Section component [src/components/sections/]
                 └─ Card / sub-component renders fields (or ignores them)
```

A field can be **missing** at any of three layers:
1. **Schema** has it, **query** doesn't fetch it — field never reaches the component
2. **Query** fetches it, **component** ignores it — data arrives but is thrown away
3. **Component** hardcodes the value — Sanity is bypassed entirely

---

## Section-by-section ground truth

### 1. Hero (`HeroSection.tsx` → `HeroContent.tsx`)

Query: **`PROFILE_QUERY`** from `src/sanity/lib/queries.ts`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `firstName`, `lastName` | ✅ | ✅ | Fallback "Anant Gupta" hardcoded in component |
| `headlineStaticText` + `headlineAnimatedWords` | ✅ | ✅ | `LayoutTextFlip` component |
| `shortBio` | ✅ | ✅ | 3-line clamp |
| `profileImage` | ✅ | ✅ | `urlFor()` + `ProfileImage` |
| `socialLinks` (github, linkedin, twitter, website, email) | ✅ | ✅ | Icon row |
| `location` | ✅ | ✅ | MapPin |
| **`availability`** | ✅ | ✅ | **RENDERED** — green pulsing dot + text below socials. Cursor plan was WRONG here. |
| `yearsOfExperience`, `stats` | ✅ | ❌ | Fetched by PROFILE_QUERY but never used by Hero — About fetches them separately |

**Hardcoded in Hero (not Sanity):**
- `"NEXT.JS • SANITY • 3D • TYPESCRIPT"` at line 111 — static subtitle, no Sanity field
- CTA buttons (View Projects, View Experience, Contact) — by design, they're nav anchors

---

### 2. About (`AboutSection.tsx` → `AboutTelemetry.tsx`, `HeroTerminal.tsx`)

Query: **inline `ABOUT_QUERY`** in `src/components/sections/AboutSection.tsx:8`

Fetches: `firstName, lastName, fullBio, yearsOfExperience, stats, email, phone, location`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `fullBio` | ✅ | ✅ | Full Portable Text |
| `stats[]` | ✅ | **PARTIAL** | See critical bug below |
| `yearsOfExperience` | ✅ | ❌ | Fetched, never used in JSX |

**Critical bug — `AboutTelemetry` keyword matching (`src/components/AboutTelemetry.tsx:9–34`)**

The component defines 4 *canonical* readouts with fixed labels and keyword match terms:

| Canonical label | Match terms | Sanity label (user data) | Matches? |
|---|---|---|---|
| Projects Built | `["project"]` | "Side Quests" | ❌ falls back to "10+" |
| Technologies | `["tech", "language", "tool", "stack"]` | "Technologies Mastered" | ✅ → shows "30+" |
| Currently Learning | `["learn", "studying", "current"]` | "Years Experience" | ❌ falls back to "Rust · LLMs" |
| Research Focus | `["research", "focus", "interest"]` | "Client Satisfaction" | ❌ falls back to "AI Systems" |

**Result:** 3 of 4 stats show hardcoded defaults instead of Sanity values. Only "Technologies Mastered" (partial match on "tech") renders correctly.

**Fix:** Remove canonical fixed-label system. Instead render `profile.stats[]` directly in order, using whatever `label` and `value` Sanity provides. Keep the same card UI but don't force specific canonical slots.

**Hardcoded elements in About (not Sanity):**
- `HeroTerminal` component (`src/components/HeroTerminal.tsx`) — the terminal widget below the bio text. This is **entirely hardcoded** with static `TERMINAL_LINES` and `ORBITING_CHIPS` arrays. **This is the "image below About me" the user asked about.** It renders `$ whoami`, `$ stack --top`, `$ status` with fixed strings. It has no Sanity connection and none was planned.

---

### 3. Experience (`ExperienceSection.tsx` → `ExperienceCard.tsx`)

Query: **`EXPERIENCE_QUERY`** from `src/sanity/lib/queries.ts`

Fetches: all fields including companyLogo, employmentType, achievements[], description, companyWebsite

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `position`, `company`, `location` | ✅ | ✅ | Card header |
| `startDate`, `endDate`, `current` | ✅ | ✅ | Date range |
| `responsibilities[]` | ✅ | ✅ | Max 3 bullets |
| `technologies[]` | ✅ | ✅ | Max 4 orbit chips |
| **`companyLogo`** | ✅ | ❌ | Queried, entirely absent from `ExperienceCard.tsx` JSX |
| **`employmentType`** | ✅ | ❌ | Queried, ignored in render |
| **`description`** | ✅ | ❌ | Queried (Portable Text), ignored |
| **`achievements[]`** | ✅ | ❌ | Queried, ignored |
| **`companyWebsite`** | ✅ | ❌ | Queried, ignored |

**Schema drift (Studio yellow warning):**
- `current: false` exists on old experience documents but schema uses `tenure` field
- GROQ handles it via `select()` coalesce so the site renders fine, but Studio shows "Unknown field" yellow box
- Fix: Sanity content migration — patch all experience docs to set `tenure: "current"|"past"` and `unset current`

---

### 4. Projects (`PortfolioContent.tsx` → `ProjectsSlider.tsx` → `ProjectCard`)

Query: **`PROJECTS_QUERY`** from `src/sanity/lib/queries.ts`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `title` | ✅ | ✅ | Card heading |
| `tagline` | ✅ | ✅ | Subtitle below title |
| `technologies[].name` | ✅ | ✅ | Max 4 chips |
| `category`, `liveUrl`, `githubUrl` | ✅ | ✅ | Case note box + buttons on hover |
| **`coverImage`** | ✅ | ❌ | Queried but `ProjectCard` has zero image rendering |
| `slug` | ✅ | ❌ | By design — no detail pages yet |
| `featured` / `visibility` | ✅ | ❌ | Query computes them but ProjectsSlider renders ALL projects regardless |

**"Entirely broken" is inaccurate — the slider UI is correct.** The problem is Sanity still has **seed/fake data** (AI Content Generator, johndoe GitHub URLs). This is a **content** problem, not a code problem. The slider renders whatever Sanity returns.

**One real code gap:** no `coverImage` is ever rendered. ProjectCard doesn't import `next/image` or `urlFor`. No visual cover for any project.

---

### 5. Skills (`SkillsSection.tsx` → `SkillsSectionClient.tsx`)

Query: **`SKILLS_QUERY`** from `src/sanity/lib/queries.ts`

Fetches: `_id, name, category, proficiency, percentage, yearsOfExperience, tone`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `name` | ✅ | ✅ | Pill label |
| `category` | ✅ | ✅ | Filter buttons + grouping |
| `proficiency` | ✅ | ✅ | Right-aligned in pill (e.g. "advanced") |
| **`tone`** | ✅ | ❌ | Queried, ignored — colors are applied per-category not per-skill |
| **`percentage`** | ✅ | ❌ | Queried, ignored |
| **`yearsOfExperience`** | ✅ | ❌ | Queried, ignored |

**The skills graph/sphere visualization is completely absent from the codebase.** `SkillsSectionClient.tsx` contains only: category summary chips, category filter pills, and a skill pill grid. There is no Three.js/R3F component, no sphere, no graph. It was removed at some point. The current "sphere with count" the user mentioned is the `SkillsSummary` — a plain 2D row of orbit chips showing "N skills across M categories".

**"Division different"** — skills are grouped by their `category` field from Sanity. Whatever category values are set in Sanity, that's what appears. If user expects different groupings, change the category tags on individual skills in Studio.

---

### 6. Education (`EducationSection.tsx` → `EducationFlowchart.tsx`)

Query: **inline `EDUCATION_SECTION_QUERY`** in `src/components/sections/EducationSection.tsx:6`

Fetches: `_id, institution, degree, fieldOfStudy, startDate, endDate, current, description, gpa`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `degree`, `fieldOfStudy`, `institution` | ✅ | ✅ | |
| `startDate`, `endDate`, `current` | ✅ | ✅ | Year range / "Present" |
| `gpa` | ✅ | ✅ | Pill when set |
| **`description`** | ✅ | ❌ | Queried but `FlowchartItem` interface (line 17) omits it — silently dropped |
| `logo` | ❌ | ❌ | Not in query, not in schema path for section |
| `achievements[]` | ❌ | ❌ | Not in query (user said not needed) |
| `website` | ❌ | ❌ | Not in query |

---

### 7. Certifications (`CertificationsSection.tsx`)

Query: **inline `CERTS_SECTION_QUERY`** in `src/components/sections/CertificationsSection.tsx:9`

Fetches: `_id, name, issuer, issueDate, credentialId, credentialUrl, logo, description, skills[]`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `logo` | ✅ | ✅ | Large banner image when present |
| `name`, `issuer` | ✅ | ✅ | |
| `issueDate` | ✅ | ✅ | Formatted "Month Year" |
| `description` | ✅ | ✅ | 3-line clamp |
| `skills[]` | ✅ | ✅ | Max 4 orbit chips |
| `credentialUrl` | ✅ | ✅ | "View Credential →" link |
| **`credentialId`** | ✅ | ❌ | Queried but not rendered in any JSX |
| **`expiryDate`** | ❌ | ❌ | NOT in query at all — must add to `CERTS_SECTION_QUERY` |

---

### 8. Achievements (`AchievementsSection.tsx`)

Query: **inline `ACHIEVEMENTS_SECTION_QUERY`** in `src/components/sections/AchievementsSection.tsx:7`

Fetches: `_id, title, description, date, type, featured, url`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `title`, `description` | ✅ | ✅ | |
| `date` | ✅ | ✅ | Year only |
| `type` | ✅ | ✅ | Orbit chip |
| `featured` | ✅ | ✅ | Violet dot |
| `url` | ✅ | ✅ | External link icon |
| **`issuer`** | ❌ | ❌ | In schema (`src/sanity/schemaTypes/achievement.ts:37`) but not in query |

---

### 9. Blog (`BlogSection.tsx` → `BlogFeed.tsx`)

Query: **inline `BLOG_SECTION_QUERY`** in `src/components/sections/BlogSection.tsx:6`

Fetches: `_id, title, slug, excerpt, externalUrl, publishedAt, readTime, category`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `title`, `excerpt`, `publishedAt`, `readTime`, `category`, `externalUrl` | ✅ | ✅ | |
| `slug` | ✅ | ❌ | No detail pages — by design |
| `featuredImage` | ❌ | ❌ | In global BLOG_QUERY but not the section query |
| `tags[]` | ❌ | ❌ | User said not needed |

**Hardcoded GitHub card** at top of `BlogFeed.tsx:7–13`: URL `https://github.com/anantgupta129` and description are static constants. This is intentional design — works fine.

**`showBlog` gate is NOT wired.** `BlogSection` always renders regardless of `siteSettings.showBlog`. The flag is fetched by `SITE_SETTINGS_QUERY` in `layout.tsx` but only used for `generateMetadata()`. It is never checked by `BlogSection.tsx`.

---

### 10. Site Settings

Used by: `src/app/(portfolio)/layout.tsx:generateMetadata()`

| Field | Used? | Notes |
|---|---|---|
| `siteTitle` | ✅ | Browser tab + OG title |
| `siteDescription` | ✅ | SEO meta description |
| `siteLogo` | ❌ | Fetched but unused — not in header, footer, or OG image |
| `showBlog` | ❌ | Fetched but never checked by BlogSection |

---

### 11. Contact (`ContactSection.tsx` → `ContactPanel.tsx`)

Query: **inline `CONTACT_QUERY`** in `src/components/sections/ContactSection.tsx:5`

Fetches: `email, location, socialLinks { github, linkedin, twitter, website }`

| Field | Queried? | Rendered? | Notes |
|---|---|---|---|
| `email`, `location` | ✅ | ✅ | |
| `socialLinks` (github, linkedin, twitter, website) | ✅ | ✅ | Icon buttons |
| `phone` | ❌ | ❌ | Not in contact query |
| `socialLinks.medium`, `.devto`, `.youtube`, `.stackoverflow` | ❌ | ❌ | Not in contact query |

---

### 12. Header / Navigation (`HeaderScrolling.tsx`)

- Navigation items: from **`NAVIGATION_QUERY`** — if Sanity has internal-link nav items they take priority; otherwise falls back to **hardcoded `CORE_NAV`** array (line 26)
- `"Anant."` logo text — **HARDCODED** at line 136
- `"Dark"` mode indicator — **HARDCODED**, non-functional (no theme switching wired)

---

### 13. Footer (`Footer.tsx`)

**100% hardcoded.** No Sanity connection:
- `© {year} Anant Gupta · building in public` — hardcoded string (intentional)
- Back to top button — by design

---

## Schema drift cleanup (Studio yellow warnings)

| Legacy field | Documents | Schema today | Fix |
|---|---|---|---|
| `current: false` | experience | Now uses `tenure` field | Patch all experience docs: set `tenure: "current"\|"past"`, unset `current` |
| `featured: true\|false` | project | Now uses `visibility` field | Patch projects: set `visibility`, unset `featured` |
| `color` | skill | Removed — now uses `tone` | Unset `color` on all skill docs |

---

## Implementation order (smallest safe diffs first)

### Phase A — Fix the stat cards (breaks user expectation most visibly, ~20 min)

**File:** `src/components/AboutTelemetry.tsx`

**Problem:** 4-slot canonical system with keyword matching causes 3 of 4 stats to show hardcoded defaults even when Sanity has real values.

**Fix:** Replace the entire `CANONICAL_READOUTS` / `findStat` system with a direct render loop over whatever `stats` array Sanity returns. Remove the fixed 4-slot assumption. Render up to 4 cards from `profile.stats[]` in order, using `stat.label` as label and `stat.value` as value. Keep the TelemetryCard UI and icons (pick icon by index). Show `yearsOfExperience` as a 5th chip if `stats` is empty.

**Prerequisite Sanity content action:** Update `profile.stats[]` in Studio to exactly the 4 items you want displayed (e.g. "Side Quests: 3", "Client Satisfaction: 100%", "Years Experience: 2+", "Technologies Mastered: 30+").

---

### Phase B — Wire queried-but-unused experience fields (~1 hr)

**File:** `src/components/cards/ExperienceCard.tsx`

All 5 missing fields are already fetched by `EXPERIENCE_QUERY` — no query changes needed.

1. **companyLogo** — add `next/image` + `urlFor()` beside company name. Small logo (32×32 or 40×40). Make it optional.
2. **employmentType** — add pill ("Internship", "Contract", "Full-time") next to position title.
3. **achievements[]** — add up to 2 achievement bullets below responsibilities, styled differently (e.g. bold metric text in teal).
4. **companyWebsite** — wrap company name in an `<a>` tag (or add a link icon).
5. **description** — do NOT render long description in card; it duplicates responsibilities. Keep in Studio as internal note only.

---

### Phase C — Education logo + description (~30 min)

**Files:** `src/components/sections/EducationSection.tsx`, `src/components/EducationFlowchart.tsx`

1. Add `logo` to `EDUCATION_SECTION_QUERY` (line 7 in EducationSection.tsx)
2. Extend `FlowchartItem` interface to include `logo` and `description`
3. Render `logo` with `next/image` inside the blob shape (replace or augment the `icon` glyph)
4. Render `description` as a short paragraph below GPA in the text panel

---

### Phase D — Certifications: expiryDate + credentialId (~20 min)

**File:** `src/components/sections/CertificationsSection.tsx`

1. Add `expiryDate` to `CERTS_SECTION_QUERY` (currently absent)
2. Render `expiryDate` as "Expires Month Year" in small text below issueDate (only when set)
3. Render `credentialId` as a monospace small text under the title (only when set)

---

### Phase E — Achievements: issuer (~15 min)

**File:** `src/components/sections/AchievementsSection.tsx`

1. Add `issuer` to `ACHIEVEMENTS_SECTION_QUERY`
2. Render `issuer` as muted text below title in each achievement row

---

### Phase F — Projects cover image (~30 min)

**File:** `src/components/three/ProjectsSlider.tsx` → `ProjectCard`

1. Import `next/image` + `urlFor` 
2. Add a `coverImage` display area at top of `ProjectCard` (visible for center card at minimum)
3. Use `next/image` with `urlFor(project.coverImage).width(600).height(280).url()`
4. Make it optional — if no image, keep the card header-only layout

---

### Phase G — Site settings: gate blog + logo (~20 min)

**Files:** `src/components/sections/BlogSection.tsx`, `src/app/(portfolio)/layout.tsx`

1. Pass `showBlog` from `SITE_SETTINGS_QUERY` to `BlogSection` (or fetch it inside BlogSection)
2. If `showBlog === false`, return `null` from BlogSection
3. Optionally: use `siteLogo` in `generateMetadata()` for the OG image

---

### Phase H — Skills graph decision (~varies)

The graph/sphere visualization is **completely absent** — not hidden, not broken, not there.

**Option 1 (restore):** Build a new Three.js/R3F skills graph component that positions skill nodes as a 3D sphere. Wire it to Sanity `percentage` + `category` fields. Effort: 2–4 hours.

**Option 2 (keep current):** The current category-chip + pill grid is clean and functional. Document that the graph was removed intentionally. Effort: 0 hours.

---

### Phase I — Schema drift (Sanity content, ~30 min)

Use Sanity Studio or MCP to patch documents:
- Experience: `unset current`, set `tenure: "current"` or `"past"` per record
- Projects: `unset featured`, set `visibility: "featured"` or `"standard"` per record
- Skills: `unset color` on all skill documents

---

### Phase J — Replace seed content (your work in Studio)

- Replace 6 seed projects with real ML/engineering projects
- Remove fake certifications you don't hold
- Replace blog resources with real content
- Fill `profile.stats[]` with correct labels matching what you want rendered

---

### Phase K — Verify

```bash
pnpm typegen && pnpm typecheck && pnpm test && pnpm build
```

Then visual QA: open each section side-by-side with Studio.

---

## What is permanently hardcoded (by design, leave it)

| Component | What is hardcoded | Why |
|---|---|---|
| `HeroTerminal.tsx` | Terminal lines, orbiting chips | Pure design element / personal brand |
| `HeroContent.tsx:111` | "NEXT.JS • SANITY • 3D • TYPESCRIPT" subtitle | Stack callout, intentional |
| `HeroContent.tsx:25` | CTA buttons (View Projects, View Experience, Contact) | Just nav anchors, no CMS field needed |
| `BlogFeed.tsx:7` | GitHub pinned card (URL + description) | Intentional permanent link |
| `Footer.tsx` | Name, tagline, copyright | Fine as-is |
| `HeaderScrolling.tsx:136` | "Anant." logo mark | Intentional — no need for Sanity field |

---

## Quick fixes by impact (for triage)

| Priority | Fix | File | Effort |
|---|---|---|---|
| P0 | Fix AboutTelemetry to show real Sanity stats | `AboutTelemetry.tsx` | 20 min |
| P0 | Fix seed projects in Studio | Studio only | 30 min |
| P1 | Wire companyLogo on ExperienceCard | `ExperienceCard.tsx` | 20 min |
| P1 | Wire employmentType on ExperienceCard | `ExperienceCard.tsx` | 10 min |
| P1 | Wire achievements on ExperienceCard | `ExperienceCard.tsx` | 20 min |
| P2 | Add expiryDate to certs query + render | `CertificationsSection.tsx` | 15 min |
| P2 | Render credentialId in certs | `CertificationsSection.tsx` | 10 min |
| P2 | Add issuer to achievements query + render | `AchievementsSection.tsx` | 15 min |
| P2 | Add logo to education query + render | `EducationSection.tsx`, `EducationFlowchart.tsx` | 30 min |
| P3 | Render education description | `EducationFlowchart.tsx` | 15 min |
| P3 | Render project coverImage | `ProjectsSlider.tsx` | 30 min |
| P4 | Gate blog on showBlog | `BlogSection.tsx` | 15 min |
| P4 | Skills graph (restore or document removal) | `SkillsSectionClient.tsx` | 2–4 hrs or 0 |
| P5 | Schema drift migration | Sanity Studio | 30 min |

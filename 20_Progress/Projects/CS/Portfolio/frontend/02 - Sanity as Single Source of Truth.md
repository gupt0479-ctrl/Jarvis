---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - sanity
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[09 - Sanity Content Spec]]"
---
# Sanity as Single Source of Truth
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]] (2026-06-12).** The first draft of this note assumed a greenfield schema and was wrong in several places. The live schema is **richer than assumed** and mostly correct already. This note now describes the *actual* schema and the *real* gaps. Read note 10 Part 1 alongside this.

The thesis still holds: **nothing visible may be hardcoded; everything renders from Sanity; the same skill looks identical everywhere.** What changed is the *mechanism* — it is already largely built. Our job is to close specific gaps, not rebuild the data model.

## The skill model that actually exists (do not "fix" it)
`skill` document (`src/sanity/schemaTypes/skill.ts`) already has: `name`, `category` (string enum), `proficiency` (beginner/intermediate/advanced/expert), `percentage` (0–100), `yearsOfExperience`, `tone` (neutral/accent/highlight/muted).

- **There is no `skillCategory` document — and we must not create one.** Categories are a string enum on `skill`. The client groups by category in `SkillsSectionClient.tsx`. Creating a doc type would force a migration + typegen + query rewrites for zero UI gain.
- **`color` field — REVERSED 2026-06-13: now ADD it.** Earlier this note said "do not add `color` back." The user has decided per-skill colour must be Sanity-controlled (the dot next to each skill across the site). **Add a `color` field to the `skill` schema as a preset palette** (a `string` enum of on-theme presets, not a free colour picker, so nothing goes off-theme): `violet, cyan, emerald, sky, pink, amber, orange, slate`, each mapping to a hex in one place. The dot/chip uses `skill.color` everywhere it appears; **fall back to the `category`-derived `CATEGORY_COLORS` when `color` is unset.** Keep `CATEGORY_COLORS` for the graph lines. See [[05 - Skills Capability Graph]] for where it does and doesn't render.
- **`tone` (neutral/accent/highlight/muted)** currently does nothing visible. Either retire it or keep it only for badge weight — it is **not** the colour source; the new `color` field is. (User explicitly noted tone "does not do anything.")
- **`percentage` is the "familiarity/level" the first draft wanted to add.** Don't add `familiarity`/`level` — use `percentage`. The capability graph ([[05 - Skills Capability Graph]]) reads `percentage` + `proficiency` (both already fetched, not yet rendered).
- `blurb` is the one field that genuinely doesn't exist; add it only if a section needs short skill copy. Not required this sprint.

Category enum values (real): `frontend, backend, ai-ml, devops, database, mobile, cloud, testing, design, tools, soft-skills, other`.

## Schema changes for the refinement pass (2026-06-13) — the full list
The build largely ran; these are the only schema edits left. Each is followed by `pnpm typegen` → `pnpm typecheck`.
1. **`skill.color`** — add the preset-palette `color` field (above). Drives the dot everywhere except the Skills section.
2. **`project.summary`** — add the long-form field (decision 2026-06-12) for the carousel hover detail.
3. **`project.coverImage`** — remove the `required` validation (make optional).
4. **`project.visibility`** — remove the enum entirely; rely on `featured` + `order`.
5. **`EDUCATION_QUERY`** — add `logo` to the projection (query-only, no schema change).
No renames, no `skillCategory` doc, no `familiarity`/`level`/`blurb`.

## The reference-field reality: `technologies[]` vs `skills[]`
The first draft said `skills[]→ref(skill)` uniformly. **Wrong.** The actual split, and we keep it as-is:

| Schema | Skill/tech field | GROQ |
|---|---|---|
| `experience` | **`technologies[]`** → refs `skill` | `technologies[]->{ _id, name, category, proficiency }` |
| `project` | **`technologies[]`** → refs `skill` | `technologies[]->{ _id, name, category }` |
| `certification` | **`skills[]`** → refs `skill` | `skills[]->{ _id, name, category }` |

**Do not rename `technologies[]` to `skills[]`.** It would break every working query and require a data migration for no benefit. The shared `<SkillChip>` reads `{name, category}` and colours via `getCategoryColor(category)` — same chip everywhere, fed by whichever field name the parent type uses.

## Other real field names (the first draft got several wrong)
| Concept | Wrong (old notes) | **Correct (live schema)** |
|---|---|---|
| Project GitHub URL | `repoUrl` | **`githubUrl`** |
| Project live URL | — | `liveUrl` |
| Project featured | `featured` bool only | `visibility` enum (`featured`/`standard`) + legacy `featured` bool, both normalized in query |
| Project long copy | `description` | **none today → add `summary`** (decision 2026-06-12; see [[04 - Projects Carousel]]) |
| Project cover image | required | **make OPTIONAL (2026-06-13)** — drop the required validation so projects publish without one |
| Project `visibility` enum | keep | **REMOVE (2026-06-13)** — it only painted a star; rely on the `featured` bool + `order`. Drop `visibility` from schema + the PROJECTS_QUERY normalization |
| Experience company URL | `companyUrl` | **`companyWebsite`** |
| Experience long copy | string `description` | **Portable Text `description`** (blocks) |
| Education stage | Sanity `stage` field | **none — UI assigns by sort index** in `EducationFlowchart.tsx` |

## The genuine "not rendering / missing" gaps (the real fix list)
These are verified against the components, not assumed:
1. **Experience Portable Text `description` is fetched but never rendered** by `ExperienceCard.tsx`. Primary content gap — wire a `<PortableText>` block behind the click-to-expand ([[03 - Experience Section]]).
2. **`EDUCATION_QUERY` does not project `logo`** even though `FlowchartItem` expects it. Add `logo` to the query ([[06 - Education Flowchart]]).
3. **Project has no long-form field.** Add `summary` to the schema + `PROJECTS_QUERY`, run `pnpm typegen` ([[04 - Projects Carousel]]).
4. **Skills `percentage`/`tone` fetched but unrendered** — they feed the capability graph, not a bug ([[05 - Skills Capability Graph]]).
5. **Fake certifications exist in Sanity** (AWS SA-Pro, GCP PCA, CKA, …). Delete them in Studio; section returns `null` when empty ([[07 - Certifications & Achievements]]).

## Typing & query discipline (from note 10)
- All shared queries in `src/sanity/lib/queries.ts` use `defineQuery()` so `pnpm typegen` extracts types. Some sections (Achievements, Certifications, Blog, Contact) keep their own inline queries beside the component — fine, as long as they use `defineQuery()`.
- After any schema change: `pnpm typegen` → `pnpm typecheck`. **Never hand-edit `src/sanity/types/index.ts`.**
- Live reads (already the pattern). Missing fields render nothing gracefully — never a hardcoded fallback string.

## Phase ordering consequence (updated)
Because the schema is already mostly right, **Phase 0 is mostly content + two small schema touches** (add `summary`, add `logo` to the education query), not a model rebuild. See the corrected phase order in [[00 - Frontend Overhaul — Build Plan]] (mirrors note 10 Part 7).

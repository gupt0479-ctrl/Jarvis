---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - frontend
  - skills
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[02 - Sanity as Single Source of Truth]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[BUILD-STATUS]]"
---
# Skills Capability Graph
> **Refinement pass (2026-06-13).** The graph + category pills + skill grid are built and rendering (`sections/SkillsSection.tsx`, `SkillsSectionClient.tsx`, Recharts via shadcn `ChartContainer`). The capability graph looks good. This note is the **fix list** for layout, line shape, effects, and data flow.

## Layout fixes (BUILD-STATUS UI Fix #5 + Anant's 2026-06-13 note)
There are currently **two** category rows stacked above the content: a coloured **count-pills row** (`Ai Ml 7 · Backend 8 · Cloud 3 …`, with dots) AND the interactive **filter-buttons row** (`All · Ai Ml · Backend …`, no counts). Plus a `56 skills across 10 categories` caption over the sphere. Collapse this:
1. **Delete the coloured count-pills row entirely.** Remove that whole block.
2. **Fold the counts onto the real category filter buttons.** Each interactive category button shows its count inline (e.g. `Ai Ml 7`, `Backend 8`) — the number that used to live on the deleted coloured pills now lives on the actual button for that category. One row of category buttons, each with its count.
3. **Remove the "All" button entirely.** No "All" filter — the default-open (highest) category renders on load; the user switches between specific categories.
4. **Keep the `N skills across M categories` caption** but small and placed so it does **not** add vertical space or break alignment (tuck it just above the category-buttons row).
5. **Perfect alignment + no header gap.** After removing the count-pills row, the **graph (left)** and the **category-buttons + skill list (right)** must align cleanly on one row, and there must be **no extra empty space between the section header ("Skills & Expertise" + description) and this content**. Tighten the top padding so the content sits directly under the header.

## Graph fixes
5. **Make the trajectories diverge.** Right now every category line follows nearly the same curve. Each category's line must have a **distinct shape** — different inflection points, slopes, and plateaus — even between two "advanced" categories. Drive each line from its own skills' `percentage` values over the 2021→2026 timeline; add per-category jitter/offset so no two lines are parallel. Keep axes labelled (X = year, Y = Familiarity / Applied Depth, never "Mastery").

## Category & skill interaction fixes (BUILD-STATUS UI Fix #6)
6. **Category-first data model, not "all skills" dump.** Don't render every skill as one long flat list. Structure: **categories first**, the highest-level category auto-open on load, the rest selectable; the chosen category then reveals its skills. (This matches the user's "systematic approach — categories, then skills under each.")
7. **Unique effect for every category pill.** `mobile`, `soft-skills`, and `testing` currently share the same hover effect — give each its own. Every category pill has a distinct signature interaction (the existing `frontend` shimmer / `backend` cursor / `ai-ml` pulse / `devops` deploy-dots / `database` sparkline / `soft-skills` lift stay; add unique ones for `mobile`, `testing`, and any other sharing duplicates). Category pills keep `useSpaceFloat` + `CometCard`.
8. **7 distinct per-skill effects, fixed-size boxes.** Each category has ~5–10 skills; cycle **7 distinct hover effects** across them (3 may repeat within a category — the goal is 7 effects total across the system). Independent of the category effects. **Critical: the skill box must NOT resize or change shape on hover** — fixed dimensions; only the effect + the proficiency level appear on hover. (Today boxes grow on hover — stop that.)
9. **Colour does NOT render in the Skills section.** The new `skill.color` dot shows everywhere else (Experience/Projects/Certs) but **not here** — in the Skills section only the hover effect + skill level show. (Per the user.)

## Data (Phase 0)
- Skills come from the `skill` registry; the new `skill.color` field is added in Sanity ([[02 - Sanity as Single Source of Truth]]) and used for dots site-wide except here. Graph line colours stay from `CATEGORY_COLORS`.

## Done conditions
- Coloured count-pills row deleted; counts now shown inline on each category filter button; no "All" button; `N skills across M categories` kept as a small caption that adds no height.
- Graph (left) and category-buttons + skills (right) align on one row; **no empty gap between the section header and the content.**
- Trajectories visibly diverge per category.
- Category-first reveal; every category pill has a unique effect (no shared mobile/soft-skills/testing); 7 distinct per-skill effects; skill boxes fixed-size on hover (effect + level only); no colour dot in this section.

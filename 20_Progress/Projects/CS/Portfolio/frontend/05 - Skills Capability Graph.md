---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - skills
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Skills Capability Graph
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]].** Files: `src/components/sections/SkillsSection.tsx`, `SkillsSectionClient.tsx`. Kicker `// capability matrix`.

## Correction from note 10 — the section is NOT broken
The first draft said "broken, doesn't render, dead buttons." **Wrong.** The 3D sphere was *deliberately* removed (Phase H, Option 2) in favour of a working, sophisticated 2D pill grid. What exists today:
- Summary bar (skill count + category count); category chips coloured per category.
- Category filter pills with **unique per-category hover micro-interactions already implemented**: `frontend`→shimmer sweep, `backend`→blinking cursor `_`, `ai-ml`→pulse-glow, `devops`/`tools`→three deploy dots, `database`→sparkline bars, `soft-skills`→lift. **Keep and enhance these; they are the brief's "each category does something unique."**
- Skill pills grouped by category with heading + description; hover = `perspective(600px) translateY(-2px) scale(1.02)` + iridescent shimmer.
- **`percentage`, `proficiency`, `tone` are fetched but not yet rendered** — they are exactly the data the capability graph needs.

So this section is an **augmentation on a working base, not a rescue.**

## What to build (the target the brief asks for)
### 1. The stock-chart capability graph (new, left column)
Add a multi-line "trajectory" graph beside the existing pill UI (graph left, categories + skills right).
- One line per category, coloured from `CATEGORY_COLORS` (see [[09 - Sanity Content Spec]] §1). Shape each line from its skills' `percentage` values across a learning timeline.
- Lines have distinct, non-identical curves trending upward; intermediate/beginner categories visibly still climbing.
- **Axes labelled.** X = progression `2021 → 2026`. Y = `Familiarity / Applied Depth` — **never "Mastery"/"Expert" as the headline** (honesty). 
- Hover a line → highlight it, dim others, tooltip (category + direction + related skills).
- Reuse **Recharts** (already a dependency) or lightweight SVG. Soft gradient fills under lines, glowing endpoints.
- Add an **Insight panel** that updates with the selected category, e.g. "Currently trending toward: AI / data systems and retrieval workflows."

### 2. Category buttons → add float + comet (right column)
The category pills are the **only** skills elements that get `useSpaceFloat` + `CometCard` (wiggle in space, comet on hover). On click: that category becomes active → its graph line highlights, its description shows (only on click), the insight panel updates, and the default-open category renders on load. Keep their existing signature micro-interactions (above) and make them pop more.

### 3. Listed skills — compact + the 7 effects
- The skill pills take too much space → shrink to fit. Level (`proficiency`) shows **only on hover** alongside the skill's effect.
- **7 distinct per-skill effects** cycled by index (`effects[N mod 7]`), independent of the category interactions and of each other. Build an `effects[0..6]` registry; the current iridescent shimmer can be **one** of the seven. Candidate set (refine to 7): magnetic ripple, glitch/scan, constellation lines, liquid `percentage` fill, orbit dot, typewriter name, depth-tilt + comet shadow. Reduced-motion → all degrade to a simple opacity/colour change.

## Done conditions
- Stock-chart graph added (labelled Familiarity axis, per-category lines from `percentage`, hover highlight + tooltip + insight panel) without removing the working pill grid.
- Category pills float + comet, click reveals description + updates graph/insight, default category opens; existing per-category effects kept + enhanced.
- Skill pills compact; `proficiency` on hover; 7 distinct cycled effects (existing shimmer = one of them).

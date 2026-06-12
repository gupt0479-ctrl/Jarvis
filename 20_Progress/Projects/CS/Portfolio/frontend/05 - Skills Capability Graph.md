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
  - "[[02 - Sanity as Single Source of Truth]]"
---
# Skills Capability Graph
Files: `SkillsSection.tsx`, `SkillsSectionClient.tsx`. Kicker: `// capability matrix`. The current bar chart is broken (doesn't render) and the buttons are dead. This is the most interaction-heavy section.

## Layout: graph left, skills right (brief items 8, 9)
Two-column. **Left: the trajectory graph. Right: the category buttons + the listed skills** for the selected category. On load, the category with `defaultOpen` renders (the highest-level one); the user picks others from the right.

## The graph (brief item 8) — stock-chart trajectories
Replace the bar chart with an eye-pleasing, stock-market-style **multi-line** chart.
- One line per `skillCategory` (AI/ML, Backend, Data Systems, Frontend, DevOps/Tools, Soft Skills…), each in its Sanity `color`.
- Lines are **not** identical curves — each has its own ups and downs, trending upward overall; intermediate/beginner categories visibly still climbing. Drive shape from each category's skills' `familiarity` values over a learning timeline.
- **Axes labelled.** X = learning progression (`2021 → 2026`). Y = `Familiarity / Applied Depth` — **not "mastery,"** and avoid "Expert" as the headline claim (honesty; consistent with chatbot grounding ethos).
- **Hover a line:** highlight it, dim the others, tooltip with category + current direction + related skills.
- Render with a charting lib already acceptable in the stack (Recharts is already used in OpsPilot/Resq; reuse it) or lightweight SVG. Make it aesthetic: soft gradients under lines, glowing endpoints.

## Category buttons (brief items 9, 10) — float + comet
The category buttons are the **only** skills elements that get `useSpaceFloat` + `CometCard` (wiggle in space, comet on hover). Each:
- On hover: enhanced effect (today's hover is weak — make it pop).
- On click: becomes active → its graph line highlights, the insight panel updates, and its **description** (from Sanity, `skillCategory.description`) appears. Description shows **only when clicked**, not by default.
- Add an **Insight panel** that updates with the selection, e.g. "Currently trending toward: AI / data systems and retrieval workflows."

### Per-category unique interaction (independent of the 7 skill effects)
Each category has its own signature micro-interaction on hover/active — these are separate from and not counted against the skill effects:
- **AI/ML:** pulse / glow.
- **Backend:** terminal cursor blink.
- **Frontend:** shimmer sweep.
- **DevOps/Tools:** deployment dots / trail.
- **Data Systems:** animated tick bars.
- **Soft Skills:** subtle bounce / wave.

## Listed skills (brief item 10) — compact, mastery on hover
Under the active category's description come its skills.
- The skill boxes today take too much space — **shrink them** to fit the section; tune sizes until compact.
- Each skill renders name (+ its `color`). The **level** (beginner/intermediate/advanced) appears **only on hover**, together with that skill's effect.
- Chips are the same shared `<SkillChip>` colour/name used site-wide — this section is the *registry* those chips read from.

## The 7 skill effects (brief item 11) — the unique factor
Every individual skill has a hover effect, and there are **exactly 7 distinct effects** cycled across the skills (skill N uses effect `N mod 7`). These are independent of the category interactions and of each other. Make them genuinely distinct and memorable — think, don't phone it in. Candidate set (pick/refine 7):
1. **Magnetic ripple** — concentric rings emanate from the cursor on the chip.
2. **Glitch/scan** — brief RGB-split scanline pass across the label.
3. **Constellation** — tiny stars connect across the chip with thin lines.
4. **Liquid fill** — the chip's `color` floods in from bottom like a gauge to the level.
5. **Orbit dot** — a small particle orbits the chip once.
6. **Typewriter** — the name retypes with a blinking cursor.
7. **Depth tilt + parallax shadow** — chip lifts with a long soft comet shadow.

Implement as a small registry `effects[0..6]`, each a self-contained component/hook, assigned by index. Reduced-motion → all degrade to a simple opacity/colour change.

## Done conditions
- Graph renders, labelled axes (Familiarity, not Mastery), per-category lines with distinct shapes, hover highlight + tooltip.
- Categories float + comet, click reveals description + updates graph + insight panel; default category opens on load.
- Skill boxes compact; level + per-skill effect on hover; 7 distinct effects cycled; categories have their own 6 signature interactions.
- Everything from the Sanity `skill` / `skillCategory` registry — concrete, no hardcode.

---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - education
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Education Flowchart
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]].** Files: `src/components/sections/EducationSection.tsx`, `src/components/EducationFlowchart.tsx`. Kicker `// origins`.

## Corrections from note 10 — blobs already exist
- **The first draft said "rendered as rectangular cards, not blobs" — WRONG.** `EducationFlowchart.tsx` already renders blob shapes via CSS classes `edu-blob--stable`, `edu-blob--forming`, `edu-blob--amoeba`, defined with morph keyframes in `globals.css`. The amoeba→circle treatment is built.
- **Stage is UI-side, not a Sanity field.** The component assigns stage by sort order (sorted `startDate desc`): most-recent (college) = `stable` circle, then `forming`, then `amoeba`. There is no `stage` field to add — do not add one.
- Each item already has: blob shape, `edu-connector` between items, `whileInView` entry, blob interior logo-or-glyph, and a `cosmic-card` text panel (degree, fieldOfStudy, institution, years, GPA chip, clamped description).

## The one real data gap
**`EDUCATION_QUERY` does not project `logo`.** The component's `FlowchartItem` expects `logo`, but the query omits it: `*[_type == "education"] | order(startDate desc){ _id, institution, degree, fieldOfStudy, startDate, endDate, current, description, gpa }`. **Add `logo` to the projection** (Certifications already fetches a logo — mirror it). Then the blob interiors can show real school logos masked to their stage perimeter.

## What to actually build (enhancements on the existing blobs)
1. **Centre the header** — `EducationSection.tsx` kicker + h2 are left-aligned (real gap). Centre them like the other sections.
2. **Mask the logo to the stage perimeter:** clip each blob's centre logo to its own outline — college logo to the clean circle, high-school to the partly-formed shape, middle-school to the amoeba. (Needs the `logo` query fix above.)
3. **Off-axis flowchart layout:** today the stages read as a straight line. Offset anchors — middle school more **right**, high school more **left**, college **near-centre** (not dead-centre) — and let each wobble around its anchor with `useSpaceFloat`, its `cosmic-card` floating with it.
4. **Living-pulse connector:** the `edu-connector` dotted lines should **stretch and return** as the blobs wobble, and a glowing pulse should travel **upward** — starting at middle school (right), up to high school (left), then a new pulse high→college, looping (progression toward the present). Reduced-motion → static dotted line with a gentle opacity breathe.
5. **Cards:** keep them comet (`CometCard`) and have them move as one with their blob (shared transform). Content unchanged from Sanity. Mobile stacks vertically, short connectors.

## Done conditions
- Header centred; `logo` added to `EDUCATION_QUERY`; logos masked to stage perimeter.
- Off-axis flowchart (mid right / high left / college near-centre) with wobble; connectors stretch; upward looping pulse; reduced-motion fallback.
- Blobs (already built) + cards float together; content unchanged.

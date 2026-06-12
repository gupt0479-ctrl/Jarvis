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
---
# Education Flowchart
Files: `EducationSection.tsx`, `EducationEntry.tsx`. Kicker: `// origins`. This is the "life-form flowchart" idea — three stages that grow from amoeba to perfect circle.

## Header (brief item 12)
Centre the header — kicker `// origins`, "Education" title, and description all centred, like the other sections. Today it's left-aligned.

## The three stages as morphing shapes (brief item 12)
Three stages, each a floating organic blob, not a rectangle. The shape's perimeter encodes how "formed" the stage is:
- **Middle school** — most deformed amoeba (irregular, wobbling perimeter).
- **High school** — less deformed, partially formed.
- **College (University of Minnesota–Twin Cities, B.S. CS)** — near-perfect, glowing, most stable circle.
- Implement with an animated blob border (SVG path morph / `feTurbulence` displacement / blob-keyframes), parameterised by a `formedness` value per stage so the same component renders all three at different deformation levels.
- The **school logo image sits at the centre** of each shape, and the **image's own mask/perimeter matches the stage's deformation** — middle-school logo is clipped to the amoeba outline, college logo to the clean circle. (Brief: "adjust the perimeters of these images to the specific education category.")
- Each shape uses `useSpaceFloat` — wiggles in its own area — and its card floats with it.

## The off-axis flowchart layout (brief item 13)
Not a straight vertical line — make it read like a flowchart:
- **Middle school more to the right**, **high school more to the left**, **college almost centre** (but not exactly — it's still a flowchart). The stages wobble around these offset anchor points.
- Connected by the existing glowing dotted lines (keep those).

## The living pulse connector (brief item 13)
The signature motion. The dotted connectors are alive:
- As the shapes wobble, the dotted line between them visibly **stretches and returns** — an elastic connection, not a rigid line.
- A **glowing pulse travels upward** along the connectors: it **starts at middle school (right)**, travels the stretching dotted line up to high school (left), then a new pulse runs from high school up to college — same upward motion, repeating. (The existing downward glow becomes this directed upward pulse.)
- Sequence loops: middle → high, then high → college, conveying progression toward the present.
- Reduced-motion → static dotted line with a gentle opacity breathe, no traveling pulse.

## Cards (brief item 14)
The per-stage cards already render correctly from Sanity and need **no content change** — UI only:
- Each card gets `CometCard` and floats together with its shape (`useSpaceFloat`, shared transform with the blob so card + shape move as one).
- Keep readable dark backing behind text where it overlaps the background sphere.
- Mobile: stack vertically, keep connectors short and readable.

## Done conditions
- Header centred; three blobs with stage-specific deformation; logos masked to their stage perimeter.
- Off-axis flowchart layout (mid right, high left, college near-centre); dotted lines stretch with the wobble.
- Upward traveling pulse, looping middle→high→college; reduced-motion fallback.
- Cards comet + float with their shapes; content unchanged from Sanity.

---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-13
tags:
  - portfolio
  - frontend
  - education
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
  - "[[BUILD-STATUS]]"
---
# Education Flowchart
> **Refinement pass (2026-06-13).** Built and rendering. **Correction: the flowchart is R3F.** Per the graphify map, `EducationFlowchart.tsx` uses **`MeshDistortMaterial` + `Float` from `@react-three/drei`**, with `BLOB_VARIANTS`, `BLOB_COLORS`, `BLOB_SIZES`, `BLOB_ICONS`. The deformed blobs already exist. This note is the **fix list**.

## Shape fixes (BUILD-STATUS UI Fix #7)
1. **Same opacity for all three blobs.** Currently the deformation differences are tied to size/opacity so middle school's deformation is barely visible. **Equalize opacity (and ideally size)** across all three so the ONLY thing that differs is the perimeter deformation.
2. **Deformation gradient via `MeshDistortMaterial.distort`** (the differentiator):
   - **Middle school** — most deformed (`distort` high, e.g. ~0.45–0.5).
   - **High school** — better but still de-arranged (`distort` mid, e.g. ~0.2–0.25) — NOT a clean circle.
   - **College** — perfect circle (`distort` ~0, glowing/most stable).
   Tie this to `BLOB_VARIANTS` so each stage maps to its distort value; same material/opacity otherwise.

## Layout fixes (BUILD-STATUS UI Fix #8)
3. **Off-axis flowchart, not a straight line.** Reposition: **high school to the LEFT, middle school to the RIGHT, college near-centre** (almost centre, not exactly — it's a flowchart). Each still wobbles in its own area via `Float`.
4. **Single travelling pulse along the connectors.** Keep the glowing dotted connectors. Replace the current glow with **ONE dot** that travels **upward**: it **starts at middle school (right)**, the dotted line stretches/returns as the blobs wobble, the dot reaches **high school (left)**, then the same single dot continues **high school → college**. One pulse, looping, bottom-to-top (origins → present). Reduced-motion → static dotted line, no travelling dot.

## Card fixes (BUILD-STATUS UI Fix #9)
5. **Subtle comet on the cards.** Each stage's text card gets `CometCard` and moves with its blob — but this is a **small card**, so the comet must be **subtler / less than other sections**. Content is already correct from Sanity; UI only.
6. **Logo masked to stage perimeter.** Once `EDUCATION_QUERY` projects `logo` (Phase 0), clip each centre logo to its stage's blob outline (amoeba/forming/circle).

## Done conditions
- All three blobs same opacity (and size); deformation is the sole differentiator via `distort` (middle most → college perfect circle).
- High left / middle right / college near-centre; each wobbling.
- ONE upward travelling dot looping middle→high→college; reduced-motion fallback.
- Cards: subtle comet, move with the blob; logos masked to perimeter.

---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - claude-setup
  - frontend
notes:
  - "[[00 - Frontend Build Kit — Index]]"
---
# Subagents & Existing .claude
Map each phase to an agent so the main thread stays lean. The repo's existing five agents cover almost everything; only one optional new agent is worth adding.

## Existing agents → what they own here
- **`three-artist`** — the motion layer: `useSpaceFloat`, the `CometCard` standardisation, `SpaceRail`, the education blob morph + living-pulse connector, the projects tether transition, the 7 skill effects, the stock-chart graph. This is the heaviest, most novel work; keep it in its own context.
- **`frontend-builder`** — section assembly on top of the primitives: Experience, Projects carousel shell, Skills layout, Certifications/Achievements, Blog, Contact, Footer. Consumes typed Sanity data; wires interactions.
- **`sanity-schema`** — the `skill`/`skillCategory` refactor (string → referenced doc), the no-hardcode field wiring, GROQ query modules, type generation. Runs in Phase 0 before anything visual.
- **`security-reviewer`** — used once, at the CSP/headers phase, to confirm the `next.config.ts` security headers are correct and don't break the three.js/Sanity asset loads.
- **`test-runner`** — `/typecheck` + any visual smoke/e2e after each phase.

## Optional new agent: `motion-systems`
If you'd rather not overload `three-artist`, split out a `motion-systems` agent that owns **only** the three reusable primitives in [[01 - Motion System & Comet Cards]] (`useSpaceFloat`, `CometCard`, `SpaceRail`) and their reduced-motion + shared-ticker plumbing. Then `three-artist` owns the section-specific set-pieces (blobs, pulse, graph, 7 effects) that consume the primitives. Worth it because every section depends on the primitives being right — isolating them prevents churn. Not required; one capable agent can do both.

## Division rule
Primitives before sections, schema before either. When a phase needs both a primitive and a section, the prompt tells Claude Code to build/confirm the primitive first (via `three-artist`/`motion-systems`), then hand the section to `frontend-builder`. Never let a section agent re-invent a float/tilt — it must import the shared primitive.

## Keep AGENTS.md thin
The repo `AGENTS.md` holds stack conventions only (Next 16/React 19/TS/Tailwind 4/Sanity, Biome, transform-only animation rule, "all chips render colour+name from `skill` refs"). The detailed plan stays in `frontend/` and is pulled per phase. A fat AGENTS.md is paid every turn.

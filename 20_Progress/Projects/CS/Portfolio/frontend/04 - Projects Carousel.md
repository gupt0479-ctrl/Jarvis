---
type: concept
status: sprout
created: 2026-06-12
updated: 2026-06-12
tags:
  - portfolio
  - frontend
  - projects
notes:
  - "[[00 - Frontend Overhaul — Build Plan]]"
  - "[[01 - Motion System & Comet Cards]]"
  - "[[09 - Sanity Content Spec]]"
  - "[[10 - Codebase Reality & Confusion Clearance]]"
---
# Projects Carousel
> **Reconciled to [[10 - Codebase Reality & Confusion Clearance]].** Header lives in `src/components/PortfolioContent.tsx`; slider in `src/components/three/ProjectsSlider.tsx`. Kicker `// build log`.

## Corrections from note 10
- **The section header is in `PortfolioContent.tsx`, not `ProjectsSlider.tsx`, and it is left-aligned** → centre it (kicker + h2 + description), matching the other sections. This part of the first draft was right.
- **The slider is a clean Framer-Motion 3-card slider, not R3F.** It is not broken. Center card = `cosmic-card`, `cursor-default`, interactive; flanking cards = `cosmic-card--dark`, `pointer-events-none`, dimmed. Each card: `coverImage` (h-40), title, `tagline`, tech tags (≤4), `ViewLiveButton` (uses `useIridescentEffect`) + `SourceButton` when URLs present. Nav = ChevronLeft/Right with `AnimatePresence`. Ordered `order asc, title asc`.
- **Field name is `githubUrl`, not `repoUrl`.** Live URL is `liveUrl`.
- **There is no long description field today** → we are **adding `summary`** to the project schema (decision 2026-06-12) for the hover detail.

## Decision: enhance Framer Motion, do NOT rebuild in R3F (2026-06-12)
Keep the working DOM/Framer slider and layer the space feel on top. Lower effort/risk, no extra GPU cost on top of the background sim. The "in space / no gravity / tether-pull" look is achievable with DOM transforms + `useSpaceFloat` + Framer.

## What to build
1. **Centre the header** in `PortfolioContent.tsx`.
2. **Schema:** add `summary` (long text or Portable Text) to `project`; add it to `PROJECTS_QUERY`; `pnpm typegen` → `pnpm typecheck`. Populate from [[09 - Sanity Content Spec]].
3. **Space motion (from [[01 - Motion System & Comet Cards]]):**
   - Centre card: `CometCard` (reduced tilt) + `useSpaceFloat` bounded to its padding — premium before hover, wandering, never leaving its box.
   - Side cards: keep translucent + `pointer-events-none` look, each drifting in its own padding via `useSpaceFloat`. **No comet until centred.** Keep drifting even on hover.
   - On left/right: chosen card glides to centre (gains comet), old centre glides out (loses comet), with a subtle **tether/string-pull** background cue (particle trail or elastic line). Respect reduced-motion.
   - Pagination: glowing orbit dots; keep the `1 / 6` counter; arrows vertically centred beside the card, not overlapping.
4. **Hover detail:** centre card is never empty (title, tagline, tech chips, small inner "case note" box). On hover, reveal the Sanity **`summary`** plus floating **Source** (always, `githubUrl`) and **View Live** (only when `liveUrl` non-empty) buttons. Cap the expanded height — never balloon; scroll internally if needed. Side cards keep wandering while hovered.
5. **Content + links (from [[09 - Sanity Content Spec]]):** replace all filler with real projects (OpsPilot, Resq, SafeReach, AI Portfolio Agent, Jarvis, Arc). Resolve `githubUrl` via `mcp__github__search_repositories`; leave `liveUrl` empty where undeployed (View Live hides; Orby's "site may be down, check GitHub" line covers it). Chips = shared category-coloured chips from `technologies[]` refs.

## Done conditions
- Header centred; `summary` field added + queried + populated; real content; `githubUrl` resolved; empty `liveUrl` hides View Live.
- Framer slider enhanced: centre comet+float, side drift (no comet, keep on hover), tether transition, orbit dots, capped hover detail.

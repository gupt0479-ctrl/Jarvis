# Portfolio Graph — Overview & Key Insights

## God Nodes (Core Abstractions)

These are the most-connected nodes — they are the glue of the codebase.

| Rank | Node | Edges | What it means |
|------|------|-------|---------------|
| 1 | `cn()` | 96 | Tailwind class merger from `src/lib/utils.ts` — every component calls it |
| 2 | `sanityFetch()` | 35 | Only CMS data-fetching function — enforces the single-source rule |
| 3 | `Data Overview` | 22 | Local fallback data hub used across the content pipeline |
| 4 | `useSidebar()` | 20 | Lab sidebar state — central to the Orby UI panel |
| 5 | `GROQ Query Examples` | 18 | Sanity query documentation used by multiple features |
| 6 | `CometCard()` | 17 | Base floating-card primitive powering most visible UI |
| 7 | `Sanity Portfolio Local Fallback Data` | 17 | Local content fallback (referenced widely) |
| 8 | `getLocalDataForQuery()` | 16 | Routes queries to local data when Sanity is unavailable |
| 9 | `Sanity Portfolio Dummy Data` | 16 | Dev seed data |
| 10 | `useIridescentEffect()` | 15 | Iridescent hover effect — shared across social/contact UI |

## Key Bridges (High Betweenness Centrality)

- **`cn()`** (0.094) — bridges 14 communities; touching it affects the entire component tree
- **`CometCard()`** (0.032) — bridges 5 communities; the visual identity anchor
- **`dataset`** (0.032) — bridges the Sanity client community to the API gate community

## Surprising Connections
- `OrbyModel()` calls `cn()` — 3D character uses CSS class utilities
- `Spinner`, `Card`, `CardHeader`, `CardTitle` all call `cn()` — every shadcn primitive flows through utils

## Knowledge Gaps
- **359 isolated nodes** with ≤1 connection: `securityHeaders`, `ERRORS`, `labButton`, `chatInput`, `submitTime` + 354 more
  - These are likely undocumented helpers or need edge extraction
  - Use `graphify update .` after adding docs/comments to improve connectivity

## Suggested Investigation Questions
- Why does `cn()` bridge 14 communities? → it's literally called in every component
- Should Community 0 (67 nodes, cohesion 0.07) be split? → yes, it's a catch-all utility dump
- Should Community 1 (51 nodes, cohesion 0.05) be split? → yes, it mixes API gate + chatbot logic

## Graph Freshness
- Built from commit: `89cd2c0e` (Chatbot branch, 2026-06-12)
- Check staleness: `git rev-parse HEAD` vs graph commit
- Rebuild (no API cost): `graphify update .` from portfolio root

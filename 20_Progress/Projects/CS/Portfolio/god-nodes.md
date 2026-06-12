---
tags: [portfolio, graph, god-nodes, architecture]
---

# God Nodes — Most Connected Abstractions

> [[INDEX|← Back to Index]]

God nodes are the highest-betweenness-centrality nodes in the knowledge graph. They are the core abstractions everything else passes through.

## Top 20 by Edge Count

| Rank | Node | Edges | File | Community |
|------|------|-------|------|-----------|
| 1 | `cn()` | 96 | `src/lib/utils.ts:L4` | 6 |
| 2 | `sanityFetch()` | 35 | `src/sanity/lib/live.ts:L41` | 7 |
| 3 | `Data Overview` | 22 | local fallback data | 8 |
| 4 | `useSidebar()` | 20 | `src/components/ui/sidebar.tsx:L33` | 67 |
| 5 | `GROQ Query Examples` | 18 | docs/queries reference | 27 |
| 6 | `CometCard()` | 17 | `src/components/ui/comet-card.tsx:L15` | 13 |
| 7 | `Sanity Portfolio Local Fallback Data` | 17 | local data docs | 8 |
| 8 | `getLocalDataForQuery()` | 16 | `src/lib/localContent.ts:L546` | 0 |
| 9 | `Sanity Portfolio Dummy Data` | 16 | dummy data docs | 31 |
| 10 | `useIridescentEffect()` | 15 | `src/hooks/useIridescentEffect.ts:L14` | 3 |
| 11 | `CLAUDE.md — Claude's Source of Truth` | 15 | `CLAUDE.md:L1` | 11 |
| 12 | `urlFor()` | 14 | `src/sanity/lib/image.ts:L9` | 15 |
| 13 | `Orby / RB: Scroll Companion Concept` | 14 | `docs/ORBY.md` | 19/21 |
| 14 | `Orby / RB: Scroll Companion Concept` | 14 | (duplicate ref) | 19/21 |
| 15 | `📋 FILES UPDATED` | 13 | commit/session note | — |
| 16 | `dataset` | 11 | `src/sanity/env.ts:L4` | 2 |
| 17 | `projectId` | 11 | `src/sanity/env.ts:L9` | 2 |
| 18 | `getServerClient()` | 10 | `src/sanity/lib/server-client.ts:L13` | 1 |
| 19 | `Anant Gupta Portfolio` | 10 | README/docs | 18 |
| 20 | `PROJECTS_QUERYResult` | 8 | `src/sanity/types/index.ts:L797` | 0 |

## Deep Dives

### cn() — 96 edges — The Universal Glue

```typescript
// src/lib/utils.ts L4
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'
export function cn(...inputs: ClassValue[]) { return twMerge(clsx(inputs)) }
```

Every component calls it. It bridges Community 6 → 32, 3, 4, 37, 67, 5, 9, 13, 47, 17, 81, 24, 28, 30. Betweenness centrality: **0.094** — the highest in the graph.

Even 3D components call it: `OrbyModel()` uses `cn()` (surprising connection).

### sanityFetch() — 35 edges — The Content Gate

The **only** authorized path to read CMS data. Every section component reaches it. Betweenness centrality: high. Lives in Community 7 alongside `PortfolioContent`, `Footer`, `ObsidianBackground`.

### useSidebar() — 20 edges — The State Singleton

Global sidebar state. Community 67 is tight (3 nodes: `SidebarToggle()`, `Sidebar()`, `useSidebar()`). Its hook is called from every component that needs to know if the sidebar is open.

### CometCard() — 17 edges — Cross-Community Card

Betweenness centrality: **0.032** — the second highest. Bridges:
- Community 13 (CertificationsSection) 
- Community 3 (ContactPanel, HeroContent)
- Community 6 (sidebar/cn cluster)
- Community 7 (PortfolioContent)
- Community 12 (AboutSection, TelemetryCard)
- Community 29 (ExperienceSection, ExperienceCard)

### dataset — 11 edges — Config Bridge

Betweenness centrality: **0.032** — bridges Community 2 (Sanity config/schema) ↔ Community 1 (chatbot backend). The Sanity `dataset` env var is used by both the public client and the server-only chat tools.

### getServerClient() — 10 edges — Write Path

The only way to write to Sanity (contact form submissions, draft mode). Uses `SANITY_API_TOKEN`. Shared between contact form Server Action and Orby chat tools.

### Orby / RB: Scroll Companion Concept — 14 edges

Two nodes with the same name (14 edges each) — likely the design doc for Phase 7 (scroll-triggered Orby messages). Both live in Communities 19 and 21 which contain overlapping Phase 7 planning content.

## Cross-Community Bridges

The graph identified these surprising cross-community connections:
- `cn()` → bridges 14+ communities
- `CometCard()` → bridges 6 communities  
- `dataset` → bridges Community 2 ↔ Community 1
- `sanityFetch()` → bridges Community 7 ↔ sections (7 → 15, 3, 13, 12, 29, 34)

## Knowledge Gaps

359 isolated nodes (≤1 connection) — possible undocumented components:
- `securityHeaders` — likely in `next.config.ts`, no documented connections
- `ERRORS` — error constants, weakly connected
- `labButton` — Lab open/close button, possibly direct DOM ref
- `chatInput` — raw input ref, not connected to component tree
- `submitTime` — contact form field, isolated

## See Also
- [[INDEX|Main Index]]
- [[communities/community-overview|All Communities]]

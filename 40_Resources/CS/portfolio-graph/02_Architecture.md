# Portfolio Graph — Core Architecture

## Community 7 — Page Composition (cohesion 0.13)
**Nodes:** `Home()`, `Footer()`, `PortfolioContent()`, `client`, `hasUsableData()`, `live`, `loadLocalQueryResult()`, `sanityFetch()` + 7 more

The root page pipeline:
```
Home() [app/page.tsx]
  └─ PortfolioContent() [src/components/PortfolioContent.tsx]  ← section compositor
       ├─ sanityFetch() / loadLocalQueryResult()  ← data layer
       └─ hasUsableData()  ← guards rendering
```
`sanityFetch()` is the **only** CMS data entry point — no direct Sanity client calls allowed in page components.

## Community 9 — Navigation & Routing (cohesion 0.15)
**Nodes:** `buildNavItems()`, `CORE_NAV`, `HeaderScrolling()`, `HeaderScrollingProps`, `isExternalHref()`, `NavItem`, `NavLink()`, `SECTION_IDS` + 14 more

- `SECTION_IDS` drives scroll-to-section behavior across the whole app
- `HeaderScrolling()` detects scroll position and highlights the active section
- `buildNavItems()` + `CORE_NAV` define the nav structure declaratively

## Community 11 — CLAUDE.md / Dev Docs (cohesion 0.08)
**Nodes:** `AI Chatbot — Phases 0–6 Complete`, `Architecture`, `Build Pipeline to Zero Errors`, `CLAUDE.md — Claude's Source of Truth`, `Commands`, `Content Flow`, `Current Architecture` + 15 more

This community is the codebase documentation itself — graphify extracted CLAUDE.md as a graph node, meaning the instructions ARE part of the knowledge graph.

## Community 48 — Clerk Auth Proxy (cohesion 0.57)
**Nodes:** `clerk`, `config`, `event`, `isPublicRoute`, `proxy()`

Tightly coupled, high-cohesion cluster. The `proxy.ts` / `src/proxy.ts` dual-file pattern is intentional — one is the Next.js middleware entry point, the other the Clerk SDK proxy config. Only the `/studio` route is protected.

## Community 57 — Route Guards (cohesion 0.4)
**Nodes:** `config`, `isPublicRoute`, `isStudioRoute`

Separates public portfolio (open) from the Sanity Studio route (Clerk-gated).

## Build Pipeline
As captured in the graph (Community 11):
1. `pnpm typegen` → regenerate `src/sanity/types/index.ts`
2. `pnpm typecheck` → TypeScript strict
3. `pnpm lint` → Biome 2.2.0
4. `pnpm build` → Next.js production build

## Key Invariants
- `PortfolioContent` is a **Server Component** — no `'use client'`
- All sections get data through the server component tree, never client-side fetched
- `sanityFetch()` from `src/sanity/lib/live.ts` is the **only** sanctioned data access path

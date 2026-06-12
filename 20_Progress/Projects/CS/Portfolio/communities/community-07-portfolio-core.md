---
tags: [portfolio, graph, community, core, sanity, sections]
---

# Community 7 — Portfolio Core

> [[../INDEX|← Back to Index]] · [[../communities/community-overview|All Communities]]

**33 nodes · Cohesion: 0.13**

## What This Community Is

The load-bearing center of the portfolio page. `sanityFetch()` (35 edges, the #2 god node) lives here alongside `PortfolioContent`, `ObsidianBackground`, and the section components that render directly from server fetches.

## Nodes

### Data Layer
- `live.ts` (both paths) — the `sanityFetch` module
- `live` — the next-sanity live client instance
- `sanityFetch()` — god node, 35 edges
- `hasUsableData()` — validates Sanity result shape
- `loadLocalQueryResult()` — fallback loader
- `createFetchFallback()` — fallback factory
- `client` — public Sanity read client

### Page Structure
- `page.tsx` (both paths) — `Home()` component
- `Home()` — entry point, renders PortfolioContent in Suspense
- `PortfolioContent.tsx` (both paths)
- `PortfolioContent()` — server component, orchestrates all section fetches

### Footer
- `Footer.tsx` (both paths)
- `Footer()` — site footer with back-to-top, social links

### Three.js
- `ObsidianBackground.tsx` (both paths)
- `ObsidianBackground` — dynamic import wrapper (must load with `ssr: false`)

### Sections (server-side)
- `SkillsSection.tsx` (both paths) + `SkillsSection()`
- `AchievementsSection.tsx` (both paths) + `AchievementsSection()`
- `ACHIEVEMENTS_SECTION_QUERY` — defined inline in AchievementsSection
- `ContactSection.tsx` + `ContactSection()`

### Queries Used
- `SKILLS_QUERY` — from queries.ts

## Why This Community Is the Core

`sanityFetch()` reaches into every section. `PortfolioContent()` is the server component tree root that calls `sanityFetch` × N queries (one per section) and passes results down as props. Every user-visible section flows through this community's data layer.

## Relationship to Other Communities

- Feeds data to: Community 3 (HeroContent, SkillsSectionClient), Community 12 (AboutSection), Community 13 (CertificationsSection), Community 29 (ExperienceSection), Community 23 (EducationSection), Community 34 (BlogSection)
- Uses `cn()` from Community 6
- Served by Community 2 (Sanity client, schema config)
- Chat route in Community 1 uses the same Sanity infrastructure

## See Also
- [[../architecture/02-sanity-cms|Sanity CMS]]
- [[../architecture/01-nextjs-routes|Next.js Routes]]
- [[../components/01-page-sections|Page Sections]]

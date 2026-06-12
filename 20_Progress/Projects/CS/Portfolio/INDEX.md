---
tags: [portfolio, codebase-map, MOC]
created: 2026-06-12
---

# Portfolio Codebase — Knowledge Map

> Auto-generated from graphify knowledge graph · Commit `89cd2c0e` · 141 files · 129,597 words

## Graph Stats

| Metric | Value |
|--------|-------|
| Nodes | 1,230 |
| Edges | 2,146 |
| Communities | 99 |
| Extraction | 100% extracted, 0% inferred |
| Files mapped | 141 |

## Navigation

### Core Sections
- [[architecture/00-overview|🏗️ Architecture Overview]] — Stack, data flow, entry points
- [[architecture/01-nextjs-routes|📦 Next.js App Router]] — Pages, layouts, API routes
- [[architecture/02-sanity-cms|🗄️ Sanity CMS]] — Schemas, queries, live API
- [[architecture/03-auth-clerk|🔐 Auth (Clerk)]] — Proxy, middleware, studio guard
- [[architecture/04-design-system|🎨 Design System]] — Tailwind v4, cn(), CometCard

### AI Chatbot — Orby
- [[chatbot/00-orby-overview|🤖 Orby Overview]] — Phases 0–6, god nodes, communities
- [[chatbot/01-api-route|🛡️ API Route]] — POST handler, gates, rate limiting
- [[chatbot/02-model-router|🔀 Model Router]] — Gemini → Groq → degraded
- [[chatbot/03-personas|🎭 Personas]] — Recruiter / Friend / Weirdo / CEO
- [[chatbot/04-tools|🔧 Closed Tools]] — 6 tools: navigate, showProject…
- [[chatbot/05-evals|🧪 Eval Suite]] — Promptfoo grounding/refusal/tools

### Components
- [[components/00-overview|🧩 Component Map]]
- [[components/01-page-sections|📄 Page Sections]] — Hero, About, Experience…
- [[components/02-lab-chat-ui|💬 Lab / Chat UI]] — PortfolioLab, ChatThread…
- [[components/03-orby-companion|🚀 Orby Companion]] — Orby.tsx, canvas, speech
- [[components/04-three-js|✨ Three.js / R3F]] — ObsidianBackground, ProjectsSlider
- [[components/05-ui-primitives|🪵 UI Primitives]] — CometCard, shadcn, sidebar

### Data Layer
- [[data/00-sanity-schemas|📋 Sanity Schemas]] — 11 document types
- [[data/01-groq-queries|🔍 GROQ Queries]] — All queries by domain

### Graph Intelligence
- [[god-nodes|⚡ God Nodes]] — Top 20 most-connected abstractions
- [[communities/community-01-chatbot-backend|Community 1: Chatbot Backend]]
- [[communities/community-04-lab-ui|Community 4: Lab UI]]
- [[communities/community-07-portfolio-core|Community 7: Portfolio Core]]
- [[communities/community-overview|All 99 Communities]]

## God Nodes (Quick Reference)

| Node | Edges | Role |
|------|-------|------|
| `cn()` | 96 | Class-name utility — used everywhere |
| `sanityFetch()` | 35 | Only way to read CMS content |
| `Data Overview` | 22 | Local fallback data hub |
| `useSidebar()` | 20 | Sidebar state singleton |
| `GROQ Query Examples` | 18 | GROQ documentation hub |
| `CometCard()` | 17 | Base floating card primitive |
| `getLocalDataForQuery()` | 16 | Fallback resolver |
| `useIridescentEffect()` | 15 | Iridescent hover effect hook |

## Surprising Connections

- `OrbyModel()` → calls → `cn()` — 3D model uses class utility
- `Spinner()` → calls → `cn()` — spinner uses class utility  
- `dataset` bridges Community 2 (Sanity config) ↔ Community 1 (Chatbot backend)
- `CometCard()` bridges 6 communities — it's the cross-cutting card primitive

## Knowledge Gaps (359 isolated nodes)
Notable weakly-connected nodes: `securityHeaders`, `ERRORS`, `labButton`, `chatInput`, `submitTime` — possible undocumented components or missing edges.

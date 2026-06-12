---
tags: [portfolio, architecture, overview]
---

# Architecture Overview

> [[../INDEX|← Back to Index]]

## Stack

| Layer | Tech | Notes |
|-------|------|-------|
| Framework | Next.js 16.1.1 App Router | React 19.2.3 |
| Language | TypeScript strict | `@/*` → `src/*` |
| Styling | Tailwind CSS v4 | CSS-first, no tailwind.config.ts |
| CMS | Sanity v4 + next-sanity | Live content API |
| Auth | Clerk | Guards `/studio` only |
| 3D | Three.js + R3F + drei | `@react-three/fiber`, `@react-three/drei` |
| AI | Gemini 2.5 Flash → Groq → degraded | Server-only keys |
| Lint | Biome 2.2.0 | Never ESLint or Prettier |
| Tests | Vitest 4 + jsdom + @testing-library | `pnpm test` |
| Deploy | Vercel | Auto-deploy on push to `main` |
| Package | pnpm | Never npm or yarn |

## High-Level Data Flow

```
Browser
  │
  ├─► GET / (portfolio page)
  │     └─► Home() [src/app/(portfolio)/page.tsx]
  │           └─► PortfolioContent() [server component]
  │                 ├─► sanityFetch() × N queries
  │                 └─► renders all sections
  │
  ├─► GET /studio/* (Sanity Studio)
  │     └─► Clerk auth guard → StudioClient
  │
  └─► POST /api/chat (Orby chatbot)
        ├─► isAllowedOrigin() gate
        ├─► HMAC token verification
        ├─► Upstash rate limit (burst + daily)
        ├─► fetchCatalog() → buildSystemPrompt()
        ├─► routeChat() → Gemini → Groq → degraded
        └─► streaming response
```

## Key Files

| File | Role |
|------|------|
| `src/app/(portfolio)/page.tsx` | Portfolio home entry |
| `src/components/PortfolioContent.tsx` | Section composition (server) |
| `src/sanity/lib/live.ts` | `sanityFetch()` — only way to read content |
| `src/sanity/lib/queries.ts` | All GROQ queries |
| `src/app/api/chat/route.ts` | Chat POST handler |
| `src/lib/model-router.ts` | Gemini → Groq → degraded routing |
| `src/lib/chat-context.ts` | System prompt builder |
| `src/lib/chat-tools.ts` | 6 closed tools |
| `src/lib/personas/index.ts` | 4 persona system prompts |
| `proxy.ts` / `src/proxy.ts` | Clerk auth proxy |
| `src/app/globals.css` | Design system (Tailwind v4 CSS-first) |

## Build Pipeline

```bash
pnpm typegen        # 1. Sync Sanity schema → src/sanity/types/index.ts
pnpm typecheck      # 2. TypeScript strict
pnpm lint           # 3. Biome check
pnpm build          # 4. Full production build
```

## Environment Variables (server-only, never NEXT_PUBLIC_)

- `GEMINI_API_KEY` — primary AI model
- `GROQ_API_KEY` — fallback AI model  
- `CHAT_TOKEN_SECRET` — HMAC token signing
- `UPSTASH_REDIS_REST_URL` — rate limit store
- `UPSTASH_REDIS_REST_TOKEN` — rate limit auth

## See Also
- [[01-nextjs-routes|Next.js Routes]]
- [[02-sanity-cms|Sanity CMS]]
- [[03-auth-clerk|Auth (Clerk)]]
- [[../chatbot/00-orby-overview|Orby Chatbot]]

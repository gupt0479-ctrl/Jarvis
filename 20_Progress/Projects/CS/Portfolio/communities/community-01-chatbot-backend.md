---
tags: [portfolio, graph, community, chatbot, backend]
---

# Community 1 — Chatbot Backend

> [[../INDEX|← Back to Index]] · [[../communities/community-overview|All Communities]]

**67 nodes · Cohesion: 0.05** (low — this is the broadest, most interconnected backend cluster)

## What This Community Is

Everything that runs server-side for the Orby chatbot. The lowest cohesion of any named community because it pulls in authentication, rate limiting, AI model routing, persona management, tool definitions, and contact form submission — all cross-cutting concerns united by the "server-only" constraint.

## Nodes by Sub-System

### API Route (`src/app/api/chat/route.ts`)
- `route.ts`
- `redis` — Upstash Redis instance
- `burstLimit` — sliding window rate limiter (10 req / 10s)
- `dailyLimit` — daily rate limiter (100 req / 24h)
- `isAllowedOrigin()` — origin allowlist check
- `POST()` — main handler

### Context Builder (`src/lib/chat-context.ts`)
- `chat-context.ts`
- `getSanityClient()` — gets server Sanity client
- `fetchCatalog()` — runs CHAT_CATALOG_QUERY
- `buildSystemPrompt()` — assembles full system prompt with catalog + persona

### Degraded Responses (`src/lib/degraded-responses.ts`)
- `degraded-responses.ts`
- `NAV_PATTERNS` — navigation intent regex patterns
- `getDegradedNavigation()` — navigation fallback
- `Intent` — intent enum
- `detectIntent()` — classifies user message
- `DegradedTemplates` — template type
- `TEMPLATES` — pre-written responses per intent × persona
- `getDegradedText()` — returns best match
- `DEGRADED_ORBY_MESSAGES` — Orby UI messages
- `getDegradedOrbyMessage()` — gets Orby message for degraded state

### Model Router (`src/lib/model-router.ts`)
- `model-router.ts`
- `google` — Gemini AI SDK instance
- `groq` — Groq SDK instance
- `LiveResult` — streaming result type
- `RouterOpts` / `RouterResult` — input/output types
- `isQuotaError()` — quota error detector
- `routeChat()` — routes to Gemini → Groq → degraded

### Chat Tools (`src/lib/chat-tools.ts`)
- `chat-tools.ts`
- `Catalog` — full data catalog type
- `NavigateResult`, `ShowProjectResult`, `ShowExperienceResult`, `LookupFactResult`, `GetResumeResult`, `ContactResult` — tool return types
- `getSanityClient()` — (local alias)
- `SECTION_IDS` — section → DOM id map
- `NONE_SENTINEL` — no-result sentinel
- `toEnum()` — string to enum converter
- `buildChatTools()` — builds AI SDK tool array
- `ChatTools` — tool array type

### Personas (`src/lib/personas/index.ts` + 4 persona files)
- `index.ts`, `PERSONAS`, `Persona`, `PERSONA_BLOCKS`, `getPersonaBlock()`
- `weirdo.ts`, `ceo.ts`, `recruiter.ts`, `friend.ts`

### Server Client (`src/sanity/lib/server-client.ts`)
- `server-client.ts` (both paths)
- `ServerClient` — type
- `assertValue()` — env var guard
- `getServerClient()` — write-authorized Sanity client
- `token` — SANITY_API_TOKEN reference

### Contact / GROQ Queries
- `PROJECT_BY_SLUG_QUERY`, `EXPERIENCE_BY_ID_QUERY`, `CHAT_CATALOG_QUERY`
- `PROJECT_BY_SLUG_QUERYResult`, `EXPERIENCE_BY_ID_QUERYResult`
- `submit-contact-form.ts`, `submitContactForm()`
- `ContactForm.tsx`, `ContactForm()`

## Key Cross-Community Edges

- `dataset` bridges this community ↔ Community 2 (Sanity config)
- `getServerClient()` is shared with contact form Server Action
- `CometCard()` from Community 13 reaches into this community via evidence cards

## See Also
- [[../chatbot/01-api-route|API Route]]
- [[../chatbot/02-model-router|Model Router]]
- [[../chatbot/03-personas|Personas]]
- [[../chatbot/04-tools|Closed Tools]]

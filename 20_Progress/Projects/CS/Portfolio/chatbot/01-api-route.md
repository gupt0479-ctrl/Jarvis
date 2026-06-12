---
tags: [portfolio, chatbot, api, security, rate-limiting]
---

# Chatbot API Route

> [[../INDEX|← Back to Index]] · [[00-orby-overview|Orby Overview]]

## File

`src/app/api/chat/route.ts` — Community 1

## Security Gate Stack (in order)

```
POST /api/chat
  │
  1. isAllowedOrigin() — checks Origin header against allowlist
  │   → 403 if origin not permitted
  │
  2. HMAC token — verifies cookie signed with CHAT_TOKEN_SECRET
  │   → 401 if token missing or invalid
  │
  3. Upstash rate limit
  │   ├── burstLimit  — short window (per-IP burst protection)
  │   └── dailyLimit  — 24h window (quota protection)
  │   → 429 if either limit exceeded
  │
  4. Scraper block — checks User-Agent for known bot patterns
  │   → 403 if detected
  │
  └── ✅ Pass → build context → route to model → stream response
```

## Key Exports from route.ts

| Export | Role |
|--------|------|
| `redis` | Upstash Redis instance (rate limit store) |
| `burstLimit` | Ratelimit instance — burst window |
| `dailyLimit` | Ratelimit instance — daily window |
| `isAllowedOrigin()` | Origin allowlist check function |
| `POST()` | Main handler |

## Request Flow inside POST()

```
POST()
  ├── Parse body: { messages, persona }
  ├── getSanityClient() → fetchCatalog() → buildSystemPrompt()
  │     └── Injects full Sanity catalog as grounding context
  ├── getPersonaBlock(persona) → append persona system prompt
  ├── buildChatTools() → 6 closed tools
  └── routeChat({ messages, systemPrompt, tools })
        ├── Try Gemini 2.5 Flash (Google)
        ├── On quota error → try Groq
        ├── On Groq quota error → getDegradedText()
        └── Stream response back
```

## HMAC Token Flow

1. On page load, `ChatTokenInit` component calls `GET /api/chat-token`
2. Server signs a token with `CHAT_TOKEN_SECRET` and sets `httpOnly` cookie
3. Chat route reads cookie and verifies HMAC signature
4. Tokens are short-lived; `ChatTokenInit` refreshes on mount

## Rate Limiting (Upstash Redis)

```typescript
// Community 1
const redis = Redis.fromEnv()
const burstLimit = new Ratelimit({
  redis,
  limiter: Ratelimit.slidingWindow(10, '10 s'),
})
const dailyLimit = new Ratelimit({
  redis,
  limiter: Ratelimit.slidingWindow(100, '24 h'),
})
```

## System Prompt Construction

`buildSystemPrompt()` in `src/lib/chat-context.ts`:
1. `fetchCatalog()` — runs `CHAT_CATALOG_QUERY` against Sanity
2. Formats catalog: profile, experience, projects, skills, education, certs, achievements
3. Appends refusal rules (no hallucination, grounded-only answers)
4. Persona block appended after base prompt

## See Also
- [[02-model-router|Model Router]]
- [[../architecture/03-auth-clerk|Auth (Clerk)]]
- [[../communities/community-01-chatbot-backend|Community 1 Detail]]

# Portfolio Graph — Orby Chatbot Layer

## Status: Phases 0–6 Complete, Phase 7 Pending

| Phase | Description |
|-------|-------------|
| 0 | `/api/chat` pipe (Gemini, server-only key) |
| 1 | Gates: origin check, HMAC token, Upstash rate-limit, scraper block |
| 2 | Grounding + refusal (Sanity catalog injected per turn) |
| 3 | Eval suite (`evals/`) + GitHub Actions gate |
| 4 | Four personas (recruiter/friend/weirdo/ceo) + power-prompts |
| 5 | Closed tool set (6 tools) + evidence cards |
| 6 | Groq fallback + degraded mode |
| 7 | Wire Orby navigation (scroll → section → on-arrival message) — **🔜 next** |

## Community 1 — API Gate + Chat Backend (cohesion 0.05)
**Nodes:** `submitContactForm()`, `burstLimit`, `dailyLimit`, `isAllowedOrigin()`, `POST()`, `redis`, `buildSystemPrompt()`, `fetchCatalog()` + 43 more

This is the largest mixed community — contains the full API pipeline:
- **Gate layer**: `isAllowedOrigin()`, HMAC token check, `redis` (Upstash rate limiter)
- **Context layer**: `buildSystemPrompt()`, `fetchCatalog()` — injects Sanity content per turn
- **Persona layer**: four persona system prompts
- **Fallback layer**: Groq router + degraded pre-written responses

Key env vars (server-only, never `NEXT_PUBLIC_`):
- `GEMINI_API_KEY` — primary model
- `GROQ_API_KEY` — fallback model
- `CHAT_TOKEN_SECRET` — HMAC signing
- `UPSTASH_REDIS_REST_URL` + `UPSTASH_REDIS_REST_TOKEN` — rate limiting

## Community 4 — Chat UI (cohesion 0.09)
**Nodes:** `ChatInputBar()`, `ChatInputBarProps`, `ChatMessage`, `ChatThread()`, `ChatThreadProps`, `ToolResult`, `EvidenceCard()`, `EvidenceCardProps` + 24 more

The client-side chat UI. Key types:
- `ChatMessage` — message shape (role, content, tool calls)
- `EvidenceCard()` — rich card shown when Orby calls a tool (project/experience cards)
- `ToolResult` — wraps tool call return values for display

## Community 36 — Orby State Machine (cohesion 0.2)
**Nodes:** `INTRO_COPY`, `LAB_HINT_COPY`, `OrbyState`, `OrbyStateResult`, `pickRandom()`, `PositionModifiers`, `SECTION_COPY`, `SECTION_TRIGGERS` + 1 more

Drives Orby's ambient behavior — what it says when idle, on section arrival, on hover. `SECTION_TRIGGERS` maps scroll positions to Orby messages (Phase 7 hook).

## Community 37 — Orby 3D Panel (cohesion 0.2)
**Nodes:** `PanelOrby()`, `PanelOrbyProps`, `PanelOrbyState`, `AstronautProps`, `OrbyCanvas()`, `OrbyCanvasProps`, `SceneProps`

The R3F canvas that renders the Orby astronaut character in the Lab sidebar. `PanelOrby()` is the top-level component; `OrbyCanvas()` wraps the Three.js scene.

## Community 30 — Speech & Text Animation (cohesion 0.21)
**Nodes:** `OrbySpeechCloud()`, `OrbySpeechCloudProps`, `speechCloudTransition`, `speechCloudVariants`, `prefersReducedMotion()`, `useTypedText()` + 2 more

The speech bubble + typewriter effect. `useTypedText()` drives the character-by-character reveal; `prefersReducedMotion()` disables it for accessibility.

## Community 32 — Orby Character (cohesion 0.2)
**Nodes:** `getPose()`, `Orby()`, `OrbyArrow()`, `OrbyArrowProps`

The Orby character mesh + pose system. `getPose()` selects animation based on `OrbyState`.

## Closed Tool Set (6 tools — from `src/lib/chat-tools.ts`)
1. `navigate` — scroll to portfolio section
2. `showProject` — display project evidence card
3. `showExperience` — display experience evidence card
4. `lookupFact` — query grounded Sanity facts
5. `getResume` — serve resume link
6. `contact` — open contact form

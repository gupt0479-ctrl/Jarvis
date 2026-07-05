---
inclusion: fileMatch
fileMatchPattern: "src/components/orby/**,src/components/lab/**,src/lib/chat*,src/lib/model-router*,src/lib/personas*,src/lib/fixed-prompts*,src/app/api/chat/**"
setup_status: static
updated: 2026-07-05
notes:
  - "[[20_Progress/AI/Kiro/Portfolio/Setup]]"
---

# Orby System — Architecture & Constraints

## Overview

Orby is the portfolio's 3D scroll companion + AI chatbot in the Portfolio Lab.
Two roles: (1) animated astronaut that roams the page, (2) conversational AI in the Lab sidebar.

## 3D Model & Visual

- R3F-based 3D astronaut rendered in a fixed-position Canvas
- Rounded helmet with reflective visor, backpack, stubby limbs
- Violet/cyan rim light matching the cosmic theme
- Speech cloud: holographic vapor puff (HTML overlay, not 3D)
- `aria-hidden="true"`, `pointer-events: none`
- Respects `prefers-reduced-motion` → static fallback

## State Machine (`useOrbyState.ts`)

States: `intro` → `pointing` → `roaming` → `section-comment` → `exitingLeft` → `goodbye` → `departingLeft` → `returningRight` → back to `pointing`

Additional states: `chat-nav-home`, `chat-nav-arrival`, `reducedMotion`

Scroll progress drives roaming (right-to-left across viewport bottom).
Section IntersectionObservers trigger one-shot comments (Set tracks fired IDs).
Custom events: `orby:navigate` (chat-driven scroll), `orby:speech` (late messages).

## Chat System — Model Router

File: `src/lib/model-router.ts`

Failover chain (Upstash-backed cooldown, 30s per provider):
1. **Cerebras** — `zai-glm-4.7` (tool-use optimized, strict constrained decoding)
2. **Groq** — `llama-3.3-70b-versatile` (dedicated SDK)
3. **Mistral** — `mistral-small-latest` (dedicated SDK)

Budget tiering (per session, Upstash counter):
- Messages 1–10: start at Cerebras
- Messages 11+: start at Groq (skip Cerebras)

Fallback modes: `degraded` (all failed), `cooldown` (all rate-limited)

## Chat Tools (6 total)

File: `src/lib/chat-tools.ts`

| Tool | Purpose |
|------|---------|
| `navigate` | Smooth-scroll to a section, with orbyMessage |
| `showProject` | Fetch + render project card in UI |
| `showExperience` | Fetch + render experience card |
| `lookupFact` | Search catalog for facts (up to 5 matches) |
| `getResume` | Assemble proof-pack resume summary |
| `contact` | Open contact form / direct user to reach out |

## Streaming Protocol

Prefix-encoded lines (one JSON value per line):
- `0:` — text delta
- `a:` — tool result `{toolCallId, toolName, result}`
- `t:` — replacement text (sanitized full text replaces prior `0:` deltas)
- `m:` — orbyMessage (standalone speech for Orby)
- `d:` — finish `{finishReason}`
- `e:` — error

## Turnstile Flow

1. `ChatTokenInit` component loads Turnstile widget (invisible)
2. Widget token → `POST /api/chat-token`
3. Server does CF siteverify (direct, no proxy)
4. Success → HMAC-signed cookie issued
5. `/api/chat` validates cookie before processing

## Zod Schema Constraints (tool parameters)

- `strict: true` on ALL tool definitions
- No `.min()` / `.max()` on schemas (breaks Cerebras constrained decoding)
- `.nullable()` for optional fields (not `.optional()`)
- Enums built from live Sanity catalog at request time
- Empty arrays guarded with `'__none__'` sentinel for `z.enum()`

## Key Files

| File | Role |
|------|------|
| `src/components/orby/Orby.tsx` | Main Orby component (position, render) |
| `src/components/orby/OrbyModel.tsx` | 3D astronaut model |
| `src/components/orby/OrbySpeechCloud.tsx` | Speech bubble overlay |
| `src/components/orby/useOrbyState.ts` | State machine hook |
| `src/components/lab/PortfolioLab.tsx` | Lab sidebar (chat UI) |
| `src/lib/model-router.ts` | Provider failover router |
| `src/lib/chat-tools.ts` | Tool definitions + execute fns |
| `src/lib/personas.ts` | Persona definitions |
| `src/lib/fixed-prompts.ts` | Pre-canned prompt mappings |
| `src/app/api/chat/route.ts` | Chat endpoint (stream handler) |
| `src/app/api/chat-token/route.ts` | Turnstile verification endpoint |

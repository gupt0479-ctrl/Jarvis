---
tags: [portfolio, chatbot, model-router, gemini, groq, degraded]
---

# Model Router

> [[../INDEX|← Back to Index]] · [[00-orby-overview|Orby Overview]]

## File

`src/lib/model-router.ts` — Community 1

## Routing Logic

```
routeChat(opts)
  │
  ├── Try: google (Gemini 2.5 Flash)
  │     ├── Success → stream LiveResult
  │     └── isQuotaError() → fall through
  │
  ├── Try: groq (Groq LLaMA/Mixtral)
  │     ├── Success → stream LiveResult
  │     └── isQuotaError() → fall through
  │
  └── Degraded: getDegradedText(intent, persona)
        └── Return pre-written answer from src/lib/degraded-responses.ts
```

## Key Exports

| Export | Role |
|--------|------|
| `google` | Google AI SDK instance (Gemini) |
| `groq` | Groq SDK instance |
| `routeChat()` | Main routing function |
| `isQuotaError()` | Detects 429/quota errors from either provider |
| `LiveResult` | Type for streaming result |
| `RouterOpts` | Input type |
| `RouterResult` | Output type |

## Degraded Mode — `src/lib/degraded-responses.ts`

When both Gemini and Groq are quota-exhausted, Orby falls back to pre-written answers.

Key exports:
- `Intent` — enum of detectable user intents
- `detectIntent()` — classifies user message into Intent
- `DegradedTemplates` / `TEMPLATES` — pre-written responses per intent × persona
- `getDegradedText(intent, persona)` — returns best pre-written answer
- `DEGRADED_ORBY_MESSAGES` — Orby-specific fallback messages
- `getDegradedOrbyMessage()` — gets Orby UI message for degraded state
- `NAV_PATTERNS` — regex patterns for navigation intent detection
- `getDegradedNavigation()` — returns navigation instructions in degraded mode

## Environment Variables

```
GEMINI_API_KEY   # Gemini 2.5 Flash — primary
GROQ_API_KEY     # Groq — secondary fallback
```

Both are server-only. Never expose to client.

## See Also
- [[01-api-route|API Route (calls routeChat)]]
- [[03-personas|Personas (injected into routeChat opts)]]
- [[04-tools|Tools (passed to routeChat)]]

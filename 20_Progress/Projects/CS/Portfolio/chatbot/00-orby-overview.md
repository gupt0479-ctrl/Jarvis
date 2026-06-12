---
tags: [portfolio, orby, chatbot, AI]
---

# Orby — AI Chatbot Overview

> [[../INDEX|← Back to Index]]

## What is Orby?

Orby is the portfolio's AI companion — a chatbot that answers questions about Anant as if it were a knowledgeable friend. It lives in the Portfolio Lab sidebar and can navigate the portfolio, show projects/experience, and look up facts.

## Build Phases

| Phase | What | Status |
|-------|------|--------|
| 0 | `/api/chat` pipe (Gemini, server-only key) | ✅ |
| 1 | Gates: origin check, HMAC token, Upstash rate-limit, scraper block | ✅ |
| 2 | Grounding + refusal (Sanity catalog injected per turn) | ✅ |
| 3 | Eval suite (`evals/`) + GitHub Actions gate | ✅ |
| 4 | Four personas (recruiter/friend/weirdo/ceo) + power-prompts | ✅ |
| 5 | Closed tool set (navigate, showProject, showExperience, lookupFact, getResume, contact) + evidence cards | ✅ |
| 6 | Groq fallback + degraded mode (pre-written answers when all quotas exhausted) | ✅ |
| 7 | Wire Orby navigation (scroll → section → on-arrival message) | 🔜 Next |

## Graph Position

Orby-related code spans **3 communities** and touches the top god nodes:
- **Community 1** — backend: API route, model router, personas, tools, degraded responses
- **Community 4** — Lab UI: PortfolioLab, ChatThread, ChatInputBar, PersonaSelector, EvidenceCard
- **Community 32** — Orby component: `Orby()`, `OrbyArrow()`, `getPose()`
- **Community 36** — State: `OrbyState`, `OrbyStateResult`, `pickRandom()`, `SECTION_COPY`, `SECTION_TRIGGERS`
- **Community 37** — Canvas: `PanelOrby()`, `OrbyCanvas()`, `SceneProps`

`Orby / RB: Scroll Companion Concept` has 14 edges — it's a design doc that anchors Phase 7.

## Spec Document

`docs/ORBY.md` — full Phase 7 implementation spec including:
- Local Character Animation
- Scroll-Progress Animation  
- Section-Triggered Messages
- Acceptance Criteria
- Copy Bank

## Key Server-Side Env Vars

```
GEMINI_API_KEY       # Primary model (Gemini 2.5 Flash)
GROQ_API_KEY         # Fallback model
CHAT_TOKEN_SECRET    # HMAC signing
UPSTASH_REDIS_REST_URL
UPSTASH_REDIS_REST_TOKEN
```

**Never** prefix these with `NEXT_PUBLIC_` — all server-only.

## See Also
- [[01-api-route|API Route + Gates]]
- [[02-model-router|Model Router]]
- [[03-personas|Personas]]
- [[04-tools|Closed Tools]]
- [[05-evals|Eval Suite]]
- [[../components/02-lab-chat-ui|Lab / Chat UI]]
- [[../components/03-orby-companion|Orby Companion Components]]

---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - ai
  - ai-infrastructure
notes:
  - "[[00 - Nextgen Chatbot — Build Plan]]"
---
# Layered Architecture
This note owns the architecture thesis: the model SDK is the *bottom* layer, and everything that makes the assistant good sits above it. It maps the professional agent stack onto our portfolio and says, per layer, what the minimal-but-real version is. Other notes implement individual layers; this one is the map.
## The thesis: build above the SDK
> [!QUESTION] "Do AI engineers use an SDK or build their own?" is the wrong question. 
> - Nobody hand-rolls SSE parsing or tool-call JSON extraction — that is the SDK's job, the bottom layer. 
> - What you own is the orchestration, grounding, tools, and evals. A toy agent loop is 40 lines; a production one adds state management, retries with timeouts (tool, model, network), observability, evals, cost controls, and graceful failure. 
> - Those are the layers below. We keep the model layer thin and swappable so we are never locked to one provider, and we put the engineering where it matters: above it.
## The stack, mapped to this portfolio
Read top-down as a request flows:
```
Frontend (Orby + chat UI + persona sidebar)
    ↓
Agent Runtime (the loop: call → tool → result → repeat; state, retries, timeouts, cost caps)
    ↓
Context Engine (assemble system prompt: persona + grounded Sanity facts + refusal rule)
    ↓
Memory Layer (working memory = this session's turns; no long-term store in v1)
    ↓
Retrieval / Grounding (structured Sanity query as a tool; NOT vector RAG by default)
    ↓
Tool Layer (closed enum: navigate, showProject, showExperience, getResume, contact, lookupFact)
    ↓
Model Providers (Gemini primary, Groq fallback — thin, swappable)
    ↓
Evaluation + Observability (wraps everything: traces every turn, runs the eval set in CI)
```
## Layer-by-layer: minimal but real
**Frontend.** Orby, the chat panel, persona sidebar, suggested chips, the copy-paste power-prompt blocks. Renders evidence cards from tool results, not just text. Owns the scroll/animation side of Orby. Detail: [[04 - Orby Integration]], [[06 - Tool System & Generative UI]].
**Agent runtime.** The loop that calls the model, runs any requested tool, feeds the result back, and repeats until the model returns a final answer. This is where the real engineering beyond 40 lines lives: a max-step cap (e.g. 4 tool calls) so it cannot loop forever, a per-request token budget, a timeout on every model and tool call, and one retry with backoff on transient failure. At our scale this fits in a single Vercel route handler — we do not need a durable task runner yet, but the loop must be written as if it could be lifted into one.
**Context engine.** Per turn, assembles the system prompt from three parts: the active persona, the grounded facts pulled from Sanity for this question, and the hard refusal rule ("answer only from provided facts; if absent, say you don't have it"). This is where grounding is enforced. Detail: [[03 - Context Engine, Grounding & Personas]].
**Memory.** v1 is **working memory only** — the current session's message history, held client-side and replayed to the model. No vector store, no knowledge graph, no episodic memory, no cross-session user profile. The 2026 production pattern is hybrid memory, but that is for agents that must remember across sessions; a portfolio visitor is anonymous and one-shot. We note the upgrade path (episodic memory if we ever want "you asked about Rust earlier") but do not build it. Saying no here is a feature, not a gap.
**Retrieval / grounding.** A tool that returns clean structured records from Sanity (projects, experience, skills) — not chunked-and-embedded text. For a small bounded corpus this beats vector RAG: more accurate, cheaper, and the model reasons over structured JSON instead of fuzzy chunks. Vector search stays available as *one* tool if we later index blog posts, but it is not the default path.
**Tool layer.** A small closed set with strict schemas. Closed enums (the section IDs come straight from Sanity nav links) are how we survive weak free-model tool-calling — the model can only pick from a fixed list, and every call is validated before it runs. Detail: [[06 - Tool System & Generative UI]].
**Model providers.** Gemini 2.5 Flash primary, Groq Llama fallback, behind a thin router. Swappable by design. Detail: [[05 - Model Layer, Rate Limiting & Abuse]].
**Evaluation + observability.** Not a layer in the request path but wrapped around all of it: trace each turn (input, tool calls, output, latency, which model answered) and a small eval set that runs before any deploy. Detail: [[07 - Evaluation & Observability]].
## What we deliberately leave out
Honest scoping so we do not over-build: no multi-agent planner/critic/executor graph (overkill for "answer questions about one person"), no long-term memory, no vector store in v1, no human-escalation path (there is no human to escalate to on a portfolio). If a single agent with good tools and grounding ever proves too weak, *then* we add structure — not before. Over-engineering is its own failure mode; see [[02 - Premortem & Failure Defenses]].

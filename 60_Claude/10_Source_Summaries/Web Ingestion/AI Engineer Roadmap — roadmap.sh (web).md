---
type: input
status: sprout
created: 2026-07-04
updated: 2026-07-04
tags:
  - summary
notes:
  - "[[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]]"
  - "[[Claude OS]]"
source_url: https://roadmap.sh/ai-engineer
source_note: "[[AI Engineer Roadmap.md]]"
input_kind: web
track: ai
---
# AI Engineer Roadmap (roadmap.sh) — Summary
**Source:** `60_Claude/05_Clippings/Web/AI Engineer Roadmap.md` (roadmap.sh, Kamran Ahmed, 2026 version)
**Ingested:** 2026-07-04
**Pages:** interactive roadmap (SVG)
## Source
The **roadmap.sh AI Engineer roadmap** — a step-by-step topic map for becoming an AI Engineer in 2026, distinguishing the AI Engineer (uses pre-trained models via APIs, RAG, agents) from the ML Engineer (trains models). The clip is the visual SVG diagram; captured below are all its node labels reorganized into the roadmap's sections, since the topic *structure* is the deliverable.
## Key Claims
- ==The AI Engineer role is model-*consumer*, not model-*builder*: it centers on pre-trained LLMs, prompting, RAG, agents, and multimodal APIs — distinct from the ML Engineer who trains models==
- The spine is: LLM fundamentals → prompt/context engineering → embeddings + vector DBs → RAG → AI agents (+ MCP) → multimodal → **evaluation & observability**
- **AI safety, evaluation, and observability are first-class sections**, not afterthoughts — the roadmap treats "can you evaluate and monitor it" as core competence
- **MCP has its own full sub-section** (host/client/server, data & transport layers, building servers and clients) — it's now a standard part of the AI-engineer skill set
- The roadmap explicitly cross-links to Prompt Engineering, AI Agents, Vibe Coding, and Claude Code as adjacent tracks
## Full Content — the roadmap, by section
### Introduction & terminology
What is an AI Engineer · AI Engineer vs ML Engineer · LLM · Inference · Training · Vector DBs · RAG · Prompt Engineering · AI Agents · AI vs AGI · Pre-trained Models · Tokens · Context · roles/responsibilities · impact on product development (Frontend / Backend / Full-Stack prerequisite).
### Working with LLMs
==Providers and how they work, plus the shift from prompt engineering to context engineering.== Providers: Anthropic Claude, Google Gemini, OpenAI (GPT/o-series), Meta Llama, Mistral, Cohere, DeepSeek, Gemma2, Qwen. How LLMs work: ReAct, Chain-of-Thought, Zero-Shot, Few-Shot, Top-K, Top-P, Temperature, sampling parameters, repetition penalties. **Context Engineering** (vs prompt engineering): input format, system prompting, role & behavior, constraints, structured output, function calling, prompt caching, streaming responses.
### Model selection & ecosystem
Closed vs open-source vs self-hosted models · choosing the right model · APIs & SDKs (Claude Messages API, OpenAI Response/compatible APIs, Google Gemini API) · platforms (OpenRouter, Hugging Face Hub, LM Studio, Ollama, Transformers.js).
### AI safety and ethics
==Safety is a named competence: understanding safety issues, prompt-injection attacks, bias & fairness, security/privacy.== Best practices: adversarial testing, content-moderation APIs, end-user IDs in prompts, robust prompt engineering, constraining inputs/outputs, know your customers/use-cases.
### Embeddings & vector databases
What are embeddings · use cases (semantic search, recommendations, anomaly detection, classification) · embedding models (OpenAI Embeddings, Gemini Embedding, Jina, Sentence Transformers, HF models) · vector DBs (pick one): Chroma, Pinecone, Weaviate, FAISS, LanceDB, Qdrant, Supabase, MongoDB Atlas · indexing embeddings, similarity search, implementing vector search.
### RAG
What are RAGs · use cases · **RAG vs fine-tuning** · the pipeline (chunking → embedding → vector DB → retrieval → generation) · implementing RAG via SDKs directly, LangChain, LlamaIndex, Haystack, RAGFlow · tools & function calling.
### AI agents
Agent use cases · ReAct prompting · manual implementation · OpenAI AgentKit & Agent SDK · Claude Agent SDK · Vertex AI Agent Builder · Google ADK · building AI agents · multi-agents. **Context management for agents:** external memory, RAG + dynamic filters, context compaction, context isolation.
### Model Context Protocol (MCP)
==MCP has a full sub-track: core components (Host, Client, Server), the Data Layer and Transport Layer, and building both an MCP server and client (connect to local or remote server).==
### Multimodal AI
Use cases · image understanding/generation · video understanding · audio processing · TTS/STT · APIs (OpenAI Vision, DALL-E, Whisper, NanoBanana, HF models) · LangChain / LlamaIndex for multimodal apps.
### Evaluation & observability
==The production layer: LLM observability (tracing & logging, cost/latency monitoring, production monitoring) and LLM evaluations.== Evaluation types: deterministic evals, model-based evals, human evals, regression testing, evaluation metrics. Tools: LangSmith, Langfuse, Helicone, Arize AI, DeepEval, RAGAS.
### Adjacent tracks
Prompt Engineering Roadmap · AI Agents Roadmap · Vibe Coding Roadmap · Claude Code · AI-assisted coding tools (Cursor, Codex, Windsurf, Replit, Gemini) · Forward Deployed Engineering · AI & Data Scientist Roadmap.
### FAQ
The roadmap affirms AI engineering as a strong 2026 career choice given cross-industry AI adoption and demand growth (the rest of the clip's FAQ body didn't capture).
## Why It Matters
This is the **canonical skill checklist** for the AI-Engineer path that the [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] guide names as the highest-opening-volume role — and it doubles as a gap audit for Anant's existing work: the vault already touches most of the spine (LLMs via Claude, MCP servers, agents in CausalOps/Jarvis, RAG roadmap in jarvis-memory), so the roadmap makes the *missing* pieces legible — chiefly **evaluation & observability** (LangSmith/Langfuse/RAGAS, deterministic vs model-based evals), which is exactly the gap the BASWE projects and the Jarvis skills both lack. The clean AI-Engineer-vs-ML-Engineer split also confirms the positioning question raised in the pivot-guide note. Use it as the checklist to pick which [[BASWE 15 AI Engineering Projects That Land Jobs (PDF)]] project to build (each maps to a roadmap section).
## Links Into The Vault
- Source clip: `60_Claude/05_Clippings/Web/AI Engineer Roadmap.md`
- [[How to Pivot into an AI-ML Engineering Role in 2026 (PDF)]] — the market/roadmap this is the topic checklist for
- [[BASWE 15 AI Engineering Projects That Land Jobs (PDF)]] — projects map onto these roadmap sections
- [[Claude OS]] — the vault already covers LLMs, MCP, and agents from this roadmap
- Evaluation & observability concept note `(to create)` — the clearest gap the roadmap surfaces
## Open Questions
- [ ] Which roadmap sections does the current project portfolio already evidence (LLMs, MCP, agents) vs which are gaps (evals/observability)?
- [ ] Is "add an eval + observability layer" the single highest-leverage next skill, given it's a gap in both this roadmap and the Jarvis skills?
- [ ] Context Engineering vs Prompt Engineering — worth a dedicated concept note tying to the vault's token-optimization work?
## Flashcards
#cards/ai
How does the roadmap distinguish an AI Engineer from an ML Engineer?::An **AI Engineer consumes pre-trained models** (via APIs, prompting, RAG, agents, multimodal) rather than training them — the ML Engineer trains and deploys models.
What is the AI-Engineer roadmap's core spine, in order?::LLM fundamentals → prompt/context engineering → embeddings + vector DBs → RAG → agents (+ MCP) → multimodal → **evaluation & observability**.
What does the roadmap treat as first-class competence that hobby projects skip?::**Evaluation & observability** — LLM tracing/logging, cost/latency and production monitoring, and evals (deterministic, model-based, human, regression) via LangSmith/Langfuse/RAGAS/DeepEval.
What is "context engineering" vs prompt engineering, per the roadmap?::A superset of prompting covering **input format, system prompting, role/behavior, constraints, structured output, function calling, prompt caching, and streaming** — engineering the whole context window, not just the prompt string.

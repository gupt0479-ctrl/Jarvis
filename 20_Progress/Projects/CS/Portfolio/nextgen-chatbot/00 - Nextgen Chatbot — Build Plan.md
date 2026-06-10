---
type: project
status: active
created: 2026-06-10
updated: 2026-06-10
deadline:
tags:
  - progress
  - portfolio
  - ai
related_progress:
  - "[[Portfolio]]"
  - "[[00 - AI Setup — Index & Integration Guide]]"
notes:
  - "[[01 - Layered Architecture]]"
  - "[[02 - Premortem & Failure Defenses]]"
next: "Phase 0 — stand up /api/chat calling Gemini behind an origin-locked route, plain text only. See [[08 - Build Phases & Milestones]]."
---
# Nextgen Chatbot — Build Plan
This is the spine note for the portfolio's AI assistant. It owns *what we are building and why*; each layer's *how* lives in its own note, linked below. Read this first, then the layer note for whatever you are about to build.
## Goal
A grounded, tool-using agent — fronted by Orby — that answers questions about Anant using only real Sanity content, can navigate the visitor to the right section, costs nothing to run, and cannot embarrass me. Done looks like: a recruiter asks "show me his backend work," Orby answers from real data, scrolls the page to Projects, and pops a one-line message there — and a malicious visitor cannot drain quota, jailbreak the persona, or make it invent a project.
## The core idea: an agent, not a chatbot
We already tried plain RAG and dropped it because it produced FAQ-shaped walls of text. The replacement is not "RAG but better" — it is a different shape. The model does not just *describe* the portfolio, it *operates* it through a small set of tools, and every factual claim is grounded in Sanity or refused. RAG-style retrieval survives as **one tool** inside this, not the architecture.
The real work is not the model call — that is the bottom layer and the least interesting part. The work is everything above it: the agent runtime (state, retries, timeouts), the context engine (grounding + persona), the tool system (closed, validated, fail-safe), and the eval/observability that tells us when it breaks. This is the [[01 - Layered Architecture]] thesis, and it is why "use an SDK vs build your own" is a false question — we use a thin SDK at the bottom and own every layer above it.
## What the chatbot does
- Answers questions about Anant — projects, experience, skills, education — strictly from Sanity content, with refusal when the answer is not in the data (see [[03 - Context Engine, Grounding & Personas]]).
- Renders **evidence cards** (real project/experience components) inside the chat instead of prose paragraphs — generative UI (see [[06 - Tool System & Generative UI]]).
- Switches **persona** — recruiter, friend, weirdo, ceo — each a different system prompt and tone, proving deliberate context engineering, not a model swap.
- **Navigates** the visitor to a section and has Orby speak there (see [[04 - Orby Integration]]).
- Runs free, rate-limited, and abuse-resistant (see [[05 - Model Layer, Rate Limiting & Abuse]]).
## How Orby fits
Orby is the *face* of the agent, not a separate thing. Two distinct behaviors that must not be confused:
- **Scroll popups** — already built. Orby reacts to scroll position with canned lines. Unchanged. We do not touch these.
- **Chat-driven navigation + speech** — new. Only when the visitor is *talking to the chatbot*: the agent emits a `navigate(sectionId)` tool call, the page scrolls to that Sanity nav link, and on arrival Orby pops the message the agent generated for that reply. This message is a property of the chat turn, never of scroll.
The hard part is keeping these two channels separate and making the chat-driven one deterministic: one tool call → one scroll → one on-arrival message. Loose wiring here is how Orby ends up talking about Projects while the page sits on Contact. Detail in [[04 - Orby Integration]].
## The four persona buttons
Recruiter, friend, weirdo, ceo are system-prompt personas surfaced in the sidebar. Clicking a section drops suggested messages into the chat bar (click → drop → send). The "generate recruiter prompt" / "generate ceo prompt" blocks above the chat bar are hand-written power-prompts the visitor copies and pastes — these are the showcase of prompt engineering and context prioritization, so they stay author-written, not model-generated. Full persona + prompt design in [[03 - Context Engine, Grounding & Personas]].
## Two-machine rule (carried over from the kit)
The portfolio repo lives in WSL; build it there with Claude Code in the terminal. This vault is the playbook — design and decisions live here, code does not. Do not try to edit repo files from Cowork. Same rule as [[00 - AI Setup — Index & Integration Guide]].
The build itself is driven by Claude Code in the WSL repo, one phase per prompt, reading these notes through the jarvis MCP. The operating kit — MCP config, subagents, commands, hooks, eval harness, and the eight copy-paste prompts — lives in the sibling folder `claude-code setup/`: [[00 - Claude Code Build Kit — Index]].## Note index
- [[01 - Layered Architecture]] — the stack, layer by layer, and our minimal-but-real version of each.
- [[02 - Premortem & Failure Defenses]] — every way this fails and the defense that prevents it. Read before building.
- [[03 - Context Engine, Grounding & Personas]] — grounding-first, refusal, the four personas, the power-prompts.
- [[04 - Orby Integration]] — the deterministic navigate→scroll→speak pipeline.
- [[05 - Model Layer, Rate Limiting & Abuse]] — free models, router, degraded mode, caps, injection, content safety.
- [[06 - Tool System & Generative UI]] — closed-enum tool contracts, validation, evidence cards.
- [[07 - Evaluation & Observability]] — the eval set and tracing that catch silent degradation.
- [[08 - Build Phases & Milestones]] — the order we build in, with done-conditions per phase.
## Current State
Planning only. No code. The earlier `Portfolio.md` "AI Lab v1 = static deterministic answers" plan is **superseded** by this: we are now building a real grounded agent on a free model. ChatKit removal from that note still stands.
## Next Action
Phase 0 — stand up `/api/chat` calling Gemini behind an origin-locked route, plain text only, to prove the pipe. See [[08 - Build Phases & Milestones]].
## Open Questions
All v1 forks are now decided (2026-06-10). Kept as a decision log:
- [x] **Agent runtime** = a single Vercel route handler for v1, not a durable task runner. Sufficient at portfolio scale; the loop is written so it could be lifted into a runner later.
- [x] **Memory** = per-session working memory only for v1. Clerk is in the stack, so the v2 upgrade is real and planned: key an episodic store (Supabase or Upstash) by Clerk `userId` so a returning signed-in visitor gets persistent memory. Deferred to v2 — see the memory note in [[05 - Model Layer, Rate Limiting & Abuse]].
- [x] **Persona prompts** = in-repo, versioned beside the eval set. They are the prompt-engineering proof, reviewed like code, never editable content.

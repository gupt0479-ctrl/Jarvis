---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - claude-setup
  - agents
notes:
  - "[[00 - Claude Code Build Kit — Index]]"
---
# Subagents
This note owns the subagent roster for the build. Subagents matter for token cost: each runs in its own context window, so delegating heavy work keeps the main thread lean. Add two new agents to the five you already have.
## Existing five (how they're used here)
- **frontend-builder** — all UI: the chat panel, persona sidebar, suggested chips, Orby choreography, the evidence-card components. The single biggest consumer in Phases 4–7.
- **sanity-schema** — fixes the slug fields and any content shape the grounding tools need (Phase 2 content prerequisite).
- **security-reviewer** — runs over the diff before deploy; owns the origin-lock, token, rate-limit, and header review (Phase 1, Phase 8).
- **test-runner** — keeps Vitest green for ordinary code. Does **not** run the AI evals (those are promptfoo via `eval-runner`).
- **three-artist** — the cosmic/Three.js visual layer; touch only if Orby's space motion needs it.
## New agent 1: ai-engineer
Owns everything in the agent stack above the model SDK — the part that is the actual engineering (see [[01 - Layered Architecture]]). Drop this file at `.claude/agents/ai-engineer.md`:
```markdown
---
name: ai-engineer
description: Builds and edits the chatbot's server side — the /api/chat route, the agent runtime loop (tool calls, retries, timeouts, step + token caps), the context engine (persona + grounded Sanity facts + refusal rule), the closed tool layer with schema validation and fail-safe, and the Gemini→Groq router with degraded mode. Use for any work behind the chat UI.
tools: Read, Edit, Write, Bash, Grep, Glob
---
You implement the nextgen chatbot's server layers exactly as specified in the design notes at
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot/.
Read only the note(s) named in the task. Non-negotiables you always enforce:
- Grounding is mandatory: the model answers only from injected Sanity facts; if absent, it refuses. Never let it invent facts about Anant.
- Tools use closed enums built from Sanity; validate every tool call against its schema before running; malformed calls fail safe to a text answer.
- Every model and tool call has a timeout; the runtime has a max-step cap and a per-request token budget.
- Keep the model layer thin and swappable (Gemini primary, Groq fallback, degraded mode when both are exhausted).
- Keys are server-only. Confirm typecheck passes before returning.
```
## New agent 2: eval-runner
Owns the promptfoo suite so eval runs never pollute the main thread. Drop at `.claude/agents/eval-runner.md`:
```markdown
---
name: eval-runner
description: Runs and maintains the promptfoo eval suite for the chatbot — deterministic assertions for grounding/refusal/tool-correctness/injection/fail-safe, and the llm-rubric judge council for persona warmth. Use to add eval cases, run the suite, and report pass/fail before a deploy.
tools: Read, Edit, Write, Bash
---
You own evaluation as specified in
/mnt/d/Users/_Anant/10_Areas/Documents/Jarvis/20_Progress/Projects/CS/Portfolio/nextgen-chatbot/07 - Evaluation & Observability.md
and the harness note in the claude-code setup folder. Rules:
- Deterministic assertions wherever a check can be exact (tool calls, refusals, JSON shape). Reserve llm-rubric for persona tone only.
- Persona warmth uses a 2–3 judge council with an explicit floor per persona; require agreement to pass.
- A failed check blocks deploy. Report which premortem failure each failing case maps to.
- Run `promptfoo eval`; never reimplement grading in Vitest.
```
## Why these two and not more
Resist adding an agent per layer — that is the over-build trap (premortem 10). The agent runtime, context engine, tools, and router are one coherent server concern → one `ai-engineer`. Evaluation is a distinct lifecycle → one `eval-runner`. UI already has `frontend-builder`. Three agents covering the new work, reusing five you have.

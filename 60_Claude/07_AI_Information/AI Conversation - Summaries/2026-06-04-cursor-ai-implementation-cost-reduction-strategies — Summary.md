---
type: input
input_kind: ai-conversation-summary
status: sprout
created: 2026-06-04
source_app: cursor
source_note: "[[60_Claude/05_Clippings/AI Conversations/Windows/Cursor/06-04 Cursor - AI implementation cost reduction strategies.md]]"
project: Jarvis
decision_count: 4
action_count: 4
tags:
  - input
  - ai-conversation-summary
notes: []
---

# Conversation Summary — AI implementation cost reduction strategies

## What Was Decided
- Problem frame: startup hitting Copilot Enterprise token limits across parallel projects; goal is near-zero marginal AI cost using existing office GPU/server + employee laptops.
- Honest thesis: "own the floor, rent the ceiling" — control + no per-seat scaling + killing token walls, not literal $0 (TCO labor breaks naive self-host savings at 15–40 seats).
- Stack direction: vLLM + LiteLLM gateway + Open WebUI/Continue; AirLLM demoted to offline fallback only; Llama-3.3-70B rejected for 24GB VRAM.
- Continue autocomplete must bypass LiteLLM (FIM bug #6900); route chat/edit through gateway only.

## What Changed
- Claude produced an HTML pitch deck for a "Zero-Cost Enterprise Proposal" internal AI stack.
- Cursor research produced two vault deliverables: `10_Areas/Life/Plans/Zero-Cost AI Stack/Research Dossier — Internal LLM Inference at Near-Zero Cost.md` and `Architecture & Setup Runbook — 24GB Hybrid Stack.md`.
- Thesis corrected from "$0" to "own the floor, rent the ceiling" after TCO analysis (labor dominates self-host cost at 15–40 seats).

## Important Context
- Resources live in `40_Resources/CS/Repos`; conversation is research/pitch prep, not implemented infrastructure.
- Export captures the user prompt + deck HTML + expanded research instructions; most agent tool output was stripped from the raw note.

## Source Claims (Quoted From Transcript)
- "My main goal over here to solve the enterprise and subscription problem so that each and every employee can work with ai at almost 0 cost."
- "Let's not try to invent our own solution. Search the internet regarding this matter in brief."

## Inferred Claims (Distiller Interpretation)
- The pitch needs an explicit quality-gap section (open models vs frontier APIs) to avoid overselling self-hosting.

## Open Questions
- Actual GPU model (VRAM, count) and concurrent user load — needed to size vLLM honestly.
- Whether Copilot Enterprise can be partially retained for PR review while routing coding to self-hosted stack.

## Follow-Up Actions
- [ ] Run the seven-section research brief and merge citations into the pitch deck
- [ ] Validate airllm vs vLLM for the office server GPU before recommending airllm to the client
- [ ] Add a "what failed" slide from Section 6 findings before presenting

## Related Notes
- [[40_Resources/CS/Repos]]

## Should Be Promoted?
- decision: no for now — keep as research input until a client-facing output lands in `35_Outputs/` or a project brief.

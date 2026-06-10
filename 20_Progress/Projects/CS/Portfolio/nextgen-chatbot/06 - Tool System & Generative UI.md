---
type: concept
status: sprout
created: 2026-06-10
updated: 2026-06-10
tags:
  - portfolio
  - ai
  - tools
notes:
  - "[[00 - Nextgen Chatbot — Build Plan]]"
  - "[[04 - Orby Integration]]"
---
# Tool System & Generative UI
This note owns the tool layer and the generative UI it drives. It is the fix for premortem failure 3 (weak free-model tool-calling breaking the wow feature). The design principle: assume the model is unreliable at structured output and make the system robust anyway.
## Why tools, not just text
The agent-not-chatbot idea lives here. Instead of describing a project in prose, the model calls `showProject(slug)` and the real project component renders inside the chat — generative UI. Tool results become React components, not strings. This is the leap from "RAG FAQ" to "assistant that operates the portfolio."
## The closed tool set
A small, fixed set with strict schemas. Keep it minimal — every extra tool is another thing the model can get wrong.
- `navigate(sectionId)` — scroll to a section. `sectionId` is a **closed enum** built from Sanity nav links. Drives the Orby pipeline in [[04 - Orby Integration]].
- `showProject(slug)` — render a real project evidence card from Sanity.
- `showExperience(id)` — render a real experience entry.
- `lookupFact(query)` — structured grounding read against Sanity (the surviving, non-vector "retrieval"). Returns records, not chunks.
- `getResume()` — surface the resume / generate a client-side proof-pack summary.
- `contact()` — open the contact flow.
The IDs and slugs come straight from existing Sanity content, so the enums are real and small.
## Surviving weak tool-calling (the core defense)
Free models emit malformed or wrong tool calls more often than frontier models. Three rules make that survivable:
1. **Closed enums over free strings.** The model picks `sectionId` from a fixed list it cannot expand. A hallucinated section simply is not in the enum and gets rejected. This is why navigation is robust even on a shaky model.
2. **Validate every call before running it.** Each tool has a schema; an argument that fails validation is rejected, not executed. No malformed call ever reaches a side effect.
3. **Fail-safe to text.** A rejected or malformed call means the model's text answer still shows; the UI action just does not happen. Orby never pretends to do something it failed to do. (Same principle as the navigation fail-safe in [[04 - Orby Integration]].)
## Generative UI: declarative, not arbitrary
The model does not emit UI code — it picks a registered tool, and *we* own the component that renders. This is the declarative pattern: the model chooses from a known set of cards/widgets, we keep visual control and consistency. It cannot produce broken markup because it never produces markup. Evidence cards (project, experience, skill, proof-pack) are author-built components fed by validated tool results.
## Evidence cards as the grounding receipt
Evidence cards do double duty: they are the generative-UI payoff *and* the visible proof behind a grounded claim (see [[03 - Context Engine, Grounding & Personas]]). When the recruiter persona says "he built a Kafka/Mongo pipeline," it renders the real BOOM project card next to the claim — the receipt, not just the assertion.
## Tool contracts as the stable interface
Treat each tool's schema as a contract: name, typed arguments, what it returns, what it renders. The agent runtime, the model layer, and the frontend all depend on these contracts, so they change deliberately and are covered by the eval set (see [[07 - Evaluation & Observability]]) — a tool whose behavior silently changes is exactly the kind of drift evals exist to catch.
## Open questions
Resolved for v1 (2026-06-10):
- [x] **Use the Vercel AI SDK for layer 3 only** — the streaming + generative-UI render plumbing. We still own the agent loop, grounding, and tools ourselves. The SDK is a convenience at the bottom, not the architecture (see [[01 - Layered Architecture]]).
- [x] **`showProject` and `navigate` use exact, closed enums, not fuzzy-match.** Slugs already exist as a Sanity field; the prerequisite is to *populate them correctly* (the `Portfolio` note flags slugs as not yet set up). Once every project has a clean slug, the server builds the enum from Sanity at request time and validates the model's choice against it — lower-risk than fuzzy title matching, which can silently resolve to the wrong project. Fuzzy-match is a **fallback only** for an item that genuinely has no slug. Net: fix the Sanity slugs first (a content task in the build phases), then rely on exact slugs.
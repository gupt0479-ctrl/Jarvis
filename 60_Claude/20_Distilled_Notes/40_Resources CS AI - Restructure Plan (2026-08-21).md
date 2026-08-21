---
type: evergreen
status: sprout
created: 2026-08-21
tags:
  - plan
  - ai
  - resources
notes:
  - "[[Engineer Edge Roadmap]]"
  - "[[10_Areas/Career/Certifications/Certifications Strategy]]"
  - "[[Jarvis Systems Audit - Retrieval, Sync, and Plugins (2026-08-21)]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[Evergreen Standard]]"
next: "Write the first module note (tokens/context-window/inference) once Weeks 1-2 of the syllabus in Engineer Edge Roadmap actually run"
---
# 40_Resources/CS/AI - Restructure Plan (2026-08-21)
A plan, not a rewrite. Per explicit instruction this session, `40_Resources/CS/AI` itself was not touched - this note only states what should happen there, so the actual restructuring is a deliberate future pass, not something done blind tonight.
## What is there now and why it falls short
`Gen AI Meeting.md` and `AI Workflow.md` were read in full this session. Both are tool-list and workflow-template dumps from a March-July 2026 course: `Gen AI Meeting.md` names over 40 tools (Bolt, Lyser, WAPI, VAPI, N8N, Chronicle, Kite) with one-line descriptions each; `AI Workflow.md` is a which-tool-for-which-task schedule with copy-paste prompt templates. Neither explains what a token actually is, why embeddings let you search by meaning, what makes something genuinely RAG versus prompt-stuffing, or what actually distinguishes an agent from a workflow. This matches [[HUMAN_WRITING]]'s own definition of the gap between a tool list and a concept note: a tool list says what exists, a concept note explains the mechanism. These notes are not wrong or slop by [[HUMAN_WRITING]]'s standard - they are an honest record of a course - but they are the wrong shape for what `40_Resources/CS/AI` is supposed to hold, per [[40_Resources/Obsidian/Jarvis Vault Architecture]]'s definition of `40_Resources` as "your private search engine," not a course-notes archive.
## What changed tonight that this plan builds on
Two things now exist that did not exist before this session, and the restructure should build on them rather than duplicate them:
1. **A real, hands-on, 17-week AI fundamentals syllabus** now lives in [[Engineer Edge Roadmap]]'s Arena 3, reset to start 2026-08-21. It names six concrete modules - base vocabulary, retrieval and memory, knowledge graphs, harness engineering, evaluation, craft/security - each with a verified external resource and a real build artifact. This is the map; `40_Resources/CS/AI` should become the place the concept explanations that back each module actually live, not a second copy of the syllabus itself.
2. **A worked example of the target depth already exists in this session's own transcript** - the base-vocabulary teaching on tokens, embeddings, the context window, training versus inference, and prompt caching, done at builder depth with mechanism, contrast, and a real vault-grounded consequence for each term. That transcript is the gold-standard bar for what a module note in `40_Resources/CS/AI` should read like, the same way [[Evergreen Standard]] names a gold-standard note for every other content type in this vault.
## The proposed shape
One evergreen note per syllabus module, filed under `40_Resources/CS/AI`, each following [[Evergreen Standard]] (Core Claim, Mechanism, Why This Matters Here, Failure Modes, Evidence, Related) rather than a tool-list shape:
- `Tokens, Context Windows, and Inference.md` - the Week 1-2 module, mechanism-first, the transcript above as the starting draft
- `Retrieval and RAG.md` - the Week 3-5 module, written once the DataTalksClub LLM Zoomcamp modules are actually run, not before - concept notes here should come from real understanding, not from reading a course description
- `Knowledge Graphs vs. Embeddings.md` - the Week 6-7 module
- `Harness Engineering.md` - the Week 8-11 module, explicitly covering both senses of "harness" surfaced this session (agent-harness and reliability/failure-harness), with a cross-link to [[Engineer Edge Roadmap]]'s Arena 2 rather than a duplicate explanation
- `Evaluation and LLM-as-Judge.md` - the Week 12-13 module
- `Prompt Engineering vs. Context Engineering.md` - the Week 14-15 module
Each note gets written **after** its syllabus week actually runs, not in advance - a concept note drafted from a course's marketing description rather than real use would be exactly the fake-confidence failure [[HUMAN_WRITING]] warns against ("never make a note sound finished if the underlying understanding is partial").
## What happens to the existing rough notes
Not deleted. `Gen AI Meeting.md` and `AI Workflow.md` hold real tool references (`MCP`, `Ollama`, `OpenRouter`, the Custom-GPT workflow) that are still individually useful even though the notes as a whole are the wrong shape. Once the six module notes above exist, mine both files for any tool reference not already covered elsewhere, fold each surviving reference into the `Related` or `Evidence` section of whichever new module note it belongs to, then mark the two original files `status: archived` with a superseded banner pointing at the new structure - the same pattern already used elsewhere in this vault for retired notes (see the `History Depth Blocker` and `Phase 2b — Promotion Study` supersede banners in the TradingView project).
## Priority queue
**Fix now:** nothing - this is a plan, not a backlog of quick fixes.
**Decide:** whether `Prompts/Chat Gpt Prompts.md`, `Token Optimization/Claude Optimization Master Setup.md`, and `Token Optimization/Claude Pro Workflow.md` (the three files under `40_Resources/CS/AI` not read this session) belong in this same restructure or are a separate, already-adequate track - read them before assuming either way.
**Build, in order, one module at a time:** write `Tokens, Context Windows, and Inference.md` after Weeks 1-2 of the syllabus actually run -> write `Retrieval and RAG.md` after Weeks 3-5 -> continue through the remaining four modules on the same after-not-before rule -> once all six exist, run the archive pass on `Gen AI Meeting.md` and `AI Workflow.md` described above.
**Low priority:** nothing deferred - this whole plan is sequenced behind the syllabus actually running, not behind anything else in the vault.

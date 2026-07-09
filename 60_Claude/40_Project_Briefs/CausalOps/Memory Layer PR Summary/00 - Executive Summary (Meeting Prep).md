---
type: project
status: complete
created: 2026-07-09
tags: [causalops, memory-layer, pr-summary, meeting-prep]
---

# Executive Summary — Persistent Semantic Memory Layer (Meeting Prep)

> [!info] Read this note first if you only have five minutes before the meeting. Every other note in this folder goes deeper on one specific piece of this work — links are at the bottom of every section.

## The One-Sentence Version

CausalOps agents used to start every incident investigation from zero — no memory of past runs, no cross-run entity tracking, no sense of "have we seen something like this before." This PR gives them **persistent memory**: every completed run is embedded, indexed, and made retrievable, so the next similar incident automatically surfaces what happened last time, weighted by how recently it happened, and cross-referenced against a growing knowledge graph of assets, MITRE ATT&CK techniques, and CVEs seen across every past investigation.

## Why This Matters — The Business Case, Not Just the Technical One

Without this feature, every incident is investigated in isolation. A SOC analyst using CausalOps to investigate "lateral movement via RDP on host-042" gets no benefit from the fact that CausalOps *already investigated* an almost-identical incident on host-017 three weeks ago — the same technique, the same root cause, maybe even the same attacker. With this feature, that prior investigation surfaces automatically, with its causal graph, its statistical estimate, and its outcome, *before* the orchestrator even starts decomposing the new incident. This is the difference between a system that reasons fresh every time and one that accumulates institutional knowledge — which is precisely what the original roadmap sentence (below) describes, and precisely why "longitudinal reasoning" and "adaptive learning" are the promised payoffs.

## What Was Asked For (the Original Roadmap Line, in Full)

> *"Develop a hybrid long-term memory architecture combining vector retrieval, graph traversal, and temporal indexing. Agents will maintain persistent contextual awareness across tasks, enabling longitudinal reasoning, adaptive learning, and higher-order strategic coordination over time."*

This is a direct quote from CausalOps's own roadmap document (`Roadmap.md` → "Future Enhancements → Persistent Semantic Memory and Retrieval Layer"). It is the single sentence this entire body of work exists to satisfy, and every subsequent note in this folder maps back to one or more clauses of it.

## Is It Done? Yes — With Receipts, Not Just Claims

A theme worth stating up front, because it shaped how this entire project was run: **every claim below was independently verified live** against the real Supabase project and the real Gemini API — not asserted, not "should work," not "passed in CI so it's probably fine." The full methodology behind that discipline is in [[06 - Testing & Verification Methodology]], but the short version is: nothing in this summary is a guess.

| Roadmap requirement | Built | Proof it works, specifically |
|---|---|---|
| Vector retrieval | Gemini embeddings (`gemini-embedding-001`, 1536-dim) → Supabase pgvector | Live search returns ranked past runs by cosine similarity, verified against real embedded rows |
| Graph traversal | Entities (assets, MITRE techniques, CVEs) + edges persisted across runs | Live query for a known entity returns its correct, real relationships |
| Temporal indexing | `exp(-0.023 × age_in_days)` decay (30-day half-life) | A row backdated 30 days measured its weight at exactly `0.5016` — matches the formula to 4 decimal places |
| Persistent contextual awareness | `memory_retrieve` / `memory_write` coordinator phases | Two sequential runs, through the *real* coordinator (not a simulation), proven to round-trip context — run 2 correctly "remembers" run 1's `run_id`, `ate`, `method`, and `n_rows` |
| MCP exposure | Standalone FastMCP server, 4 tools | A live protocol round trip via `fastmcp.Client` — real tool discovery, real argument validation — not a mocked function call |

**Full breakdown of each component, including code:** [[02 - The Persistent Memory Layer, Component by Component]]

## The Numbers That Matter in a Meeting

- **111 files changed** in the final pull request (`darshgarg7/CausalOps#25`), across three follow-up commits after the initial submission (a CI-lint fix, and a code-review-findings fix)
- **22/22 memory-layer tests passing**, against *live* infrastructure, not mocks — this includes a full coordinator round-trip test, a real MCP-protocol round-trip test, and a decay-math correctness test
- **97/97 backend unit tests passing**, confirmed with **zero regressions** introduced anywhere else in the codebase — verified by direct comparison against the unmodified target branch, not assumed
- **4 Supabase migrations**, now version-controlled as SQL files in the repository — previously applied ad hoc with no local record at all, a real gap this work closed
- **2 real Postgres security advisories and 1 performance advisory** found by Supabase's own automated linter and fixed, live, on the production project
- **6 real bugs found and fixed**, five from an automated code-review pass (GitHub Copilot) and one additional bug found independently while re-verifying Copilot's own fixes — full story in [[05 - Reconciling With Main — The Rebase Story]] and [[06 - Testing & Verification Methodology]]
- **5 unrelated upstream commits** had to be reconciled by hand before this PR could even be opened cleanly — see below

## A Timeline, If Asked "How Did This Actually Go"

1. **Implementation** — the five roadmap components (vector retrieval, knowledge graph, temporal decay, MCP server, agent integration) were built and unit-tested.
2. **Independent gap review** — rather than declaring the feature "done" once it compiled, a deliberately skeptical review was run against the actual live Supabase project and the actual codebase, surfacing a real deployment bug (the MCP server's Docker/SSE port binding) and several documentation drifts.
3. **Fixes applied and reverified live** — including the MCP deployment fix, doc/schema drift cleanup, the missing end-to-end integration test, and Supabase schema hardening.
4. **Branch reconciliation** — by the time this was ready to submit, `main` had moved five commits ahead with unrelated work (a new LLM backend, a new execution-mode architecture). The branch was reconciled by hand rather than opening a conflict-laden PR — full story in [[05 - Reconciling With Main — The Rebase Story]].
5. **Pull request opened**, with Copilot requested as an automated reviewer alongside the human reviewer.
6. **CI failures diagnosed and fixed** — a pre-existing backend lint issue and 159 pre-existing frontend formatting issues, both confirmed pre-existing (not introduced by this work) before being fixed anyway to unblock CI.
7. **Copilot's five findings addressed** — each independently re-verified as real, fixed, and a sixth bug found in the process that Copilot's review had missed.
8. **A second, deeper review requested** from Copilot specifically targeting the branch-reconciliation files — still outstanding as of this writing.

## Why This Wasn't a Simple Merge — the Short Version

Between when this feature branch was started and when it was ready to submit, `main` moved forward with substantial, unrelated work: a new primary LLM backend (NVIDIA Nemotron), a new "standard vs. deep" execution-mode architecture, and a frontend redesign. Landing this PR meant reconciling with all of that by hand — including catching a bug the merge itself silently introduced, and a second bug that was completely invisible to Git's own conflict detection. Full story: [[05 - Reconciling With Main — The Rebase Story]].

## What's Genuinely Left (Not Done, By Deliberate Choice — Not an Oversight)

Three things were explicitly scoped *out* of this PR, each for a stated reason:

1. **Automated memory-row retention/deletion** — a manual SQL query is documented instead; automating deletion is deferred until real usage data shows what retention window actually makes sense. Building an unattended job that deletes production data on a schedule, before there's evidence to size that schedule correctly, was judged premature.
2. **Multi-hop graph traversal / graph embeddings** — the current graph traversal is single-hop entity-neighborhood lookup, which matches what was actually scoped from the start. Deeper traversal is genuine future work, not a corner that was cut.
3. **A second, deeper Copilot re-review** of the merge-conflict-resolved files specifically — requested in the PR but not yet returned as of this writing.

Full detail, prioritized, plus what to say if asked "what's next": [[07 - Next Steps, Deferred Work & Career Takeaways]].

## A Glossary, In Case the Meeting Includes Non-Technical Stakeholders

- **Embedding** — a numeric representation of text (a list of ~1500 numbers) such that texts with similar *meaning* end up numerically close together. This is what makes "find me past incidents similar to this one" a mathematical operation rather than a keyword search.
- **Vector database (pgvector)** — a database extension that can efficiently search millions of these numeric representations for the closest matches.
- **Knowledge graph** — a network of entities (assets, techniques, CVEs) and the relationships between them, built up across every investigation rather than reset each time.
- **Temporal decay** — a mathematical weighting that makes recent information matter more than old information, without discarding the old information entirely.
- **MCP (Model Context Protocol)** — the standard way an AI agent (like Claude) discovers and calls external tools. This is the same mechanism used to let Claude Code itself query CausalOps's memory directly, for real, during this project's own verification work.

## If You Only Read One Other Note

If the meeting is technical, read [[02 - The Persistent Memory Layer, Component by Component]]. If the meeting is about *how* the work was done (process, rigor, engineering judgment) rather than *what* was built, read [[06 - Testing & Verification Methodology]] and [[05 - Reconciling With Main — The Rebase Story]] — those two notes are where the real engineering difficulty lived, arguably more so than in writing the new feature itself.

## Note Index

1. [[01 - What is CausalOps (Project Primer)]] — start here if you need the *entire* project explained from zero, including a worked example
2. [[02 - The Persistent Memory Layer, Component by Component]] — the five components in depth, with code
3. [[03 - Supabase Schema, Migrations & Data Layer]] — the database side, with full SQL
4. [[04 - The MCP Server and Protocol Bridge]] — how agents (including Claude Code itself) actually talk to the memory layer
5. [[05 - Reconciling With Main — The Rebase Story]] — the hardest part of this PR, and why
6. [[06 - Testing & Verification Methodology]] — how "done" was actually proven, not just claimed
7. [[07 - Next Steps, Deferred Work & Career Takeaways]] — what's left, and how to talk about this work externally

---
type: project
status: active
created: 2026-07-19
tags:
  - causalops
  - meeting-prep
  - memory-layer
  - pr-25
related:
  - "[[CausalOps — Index]]"
  - "[[memory-layer]]"
  - "[[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/00 - Executive Summary (Meeting Prep)]]"
  - "[[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/02 - The Persistent Memory Layer, Component by Component]]"
  - "[[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/05 - Reconciling With Main — The Rebase Story]]"
  - "[[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/06 - Testing & Verification Methodology]]"
  - "[[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/07 - Next Steps, Deferred Work & Career Takeaways]]"
next: "Read this top to bottom once tonight, then skim the Q&A section again right before the meeting"
---

# Meeting Prep — Persistent Memory Layer (PR #25)

Meeting: tomorrow. Subject: `darshgarg7/CausalOps#25` — "feat: Persistent Semantic Memory and Retrieval Layer." Open, not yet merged. This note is what I actually say, not a summary to re-read and improvise from. The deep technical source material lives in [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/00 - Executive Summary (Meeting Prep)|the PR Summary folder]] — this note is the meeting-facing distillation of it, organized around what gets said out loud and what gets asked back.

## The 30-Second Answer, If That's All I Get

CausalOps agents used to investigate every incident from zero — no memory of past runs. This PR gives them persistent memory: every completed run gets embedded and indexed, so a new incident automatically retrieves the most similar past investigations, weighted so recent ones matter more than old ones, cross-referenced against a knowledge graph of assets, MITRE techniques, and CVEs built up across every run. It directly implements one sentence from CausalOps's own roadmap: vector retrieval, graph traversal, temporal indexing, persistent contextual awareness across tasks. All four pieces are built, tested against live infrastructure (not mocks), and the PR is open for review.

## What I Actually Built — Five Pieces, in the Order They Run

I want to walk this as the data flow, because that's the order it actually makes sense in, not the order I wrote the files:

1. **Vector retrieval.** A new incident's description gets embedded (`gemini-embedding-001`, 1536 dimensions) and Postgres (via pgvector) finds the most similar past runs by cosine similarity. `src/memory/embedder.py` — one function, `embed_text()`.
2. **Knowledge graph.** Entities — assets, MITRE technique IDs, CVEs, causal-graph nodes — get pulled out of every run's evidence and causal graph, deterministically, zero LLM calls, and persisted as nodes and edges that accumulate across every run. `src/memory/extractor.py`.
3. **Temporal decay.** Similarity gets multiplied by `exp(-0.023 × age_in_days)` — a 30-day half-life. A run from today weighs ~1.0; 30 days ago, ~0.5; 90 days ago, ~0.125. Recent incidents outrank stale ones with the same textual similarity, without discarding the old ones.
4. **MCP server.** A standalone FastMCP process (`python -m memory.mcp_server`) exposing four tools — `search_similar_incidents`, `get_entity_relationships`, `get_asset_timeline`, `write_run_to_memory` — over stdio (for Claude Desktop/Code) or SSE on port 8001 (Docker). Deliberately never mounted inside the main FastAPI app.
5. **Agent integration.** Two new coordinator phases, `memory_retrieve` (before the orchestrator decomposes the incident) and `memory_write` (after every run completes). Both wrapped in try/except that logs and swallows — a Supabase or embedding-API outage can never fail an actual investigation. Memory is enhancement, not a dependency.

If I need one sentence for *why* this design specifically: **the LLM never touches what counts as memory.** Entity extraction is regex/dict-based, not an LLM call. The database is the source of truth for what's similar, not a model's judgment. This is the same "LLM proposes, deterministic code decides" boundary that governs the rest of CausalOps, applied to memory.

## Why 111 Files Changed for a "Memory Layer" — Say This Before Anyone Asks

This is the question I expect first, and I want to lead with it rather than wait for it. My branch (`plan/persistent-memory-mcp`) split off `main` before five unrelated commits landed: a new primary LLM backend (NVIDIA Nemotron replacing Gemini as default), a new `execution_mode` concept (fast "standard" path vs. the full "deep" pipeline), a frontend redesign, and new visual-regression tests. Rather than open a PR that conflicts with current `main`, I reconciled by hand first — a `git merge --squash` with 19 files genuinely touched by both sides, nine of which had real conflicts I resolved individually. The other ~90 files in the diff are the completed `hivemind` → `causalops` rebrand (renamed component files, import-path updates) that had been in flight and needed finishing so the branch would diff cleanly against `main`. **The memory layer itself is about 10 new files** (`src/memory/*`, `tests/memory/*`, four SQL migrations). The other hundred are the cost of landing a long-lived branch cleanly instead of leaving a conflict-laden PR for someone else to untangle.

This reconciliation is genuinely the hardest part of this PR — harder than writing the memory layer itself — and I want to be able to say that plainly, not undersell it. Full story, if it goes deep: [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/05 - Reconciling With Main — The Rebase Story]].

## Was There a Better Way? — Honest Answers, Not Defensive Ones

I'd rather volunteer the real tradeoffs than get cornered into defending choices as if they were obviously correct.

**Embeddings: Gemini, not the originally planned Azure OpenAI.** The plan called for Azure's `text-embedding-3-small`. Azure's embedding credits ran out mid-project, so I switched to Gemini's `gemini-embedding-001`, truncated to 1536 dimensions specifically to match the already-sized database column and avoid a schema migration. This is independent of the chat LLM — `embedder.py` makes its own direct API call, it never routes through the shared `src/llm.py` client, which is exactly why it didn't need to change again when `main` later switched the primary chat model to NVIDIA. Was Gemini the "right" choice in some absolute sense? No — it was the available choice. If asked whether I'd revisit it: only if there's a concrete reason (cost, latency, a provider outage pattern), not just because a newer embedding model exists.

**Squash-merge, not rebase, for the reconciliation.** A standard `git rebase` replays commits one at a time; with 19 overlapping files including core coordinator logic, the same conceptual conflict could have surfaced fragmented across multiple replays with inconsistent resolutions. I measured the actual overlap first (`git merge-tree` dry run, `comm -12` on touched-file lists) before deciding, and squash-merging let me resolve each conflict once, correctly. The real cost: five original, semantically distinct commits collapsed into one pushed commit. I didn't lose that history — it's preserved on `backup/plan-persistent-memory-mcp-pre-rebase` — but the pushed branch reads as one big commit instead of five focused ones. If I'm asked whether that's a real downside: yes, for reviewability. I made the call that resolving conflicts correctly once mattered more than commit granularity, and I can defend that specific tradeoff if pushed.

**Postgres/pgvector, not a dedicated vector database.** I didn't evaluate Pinecone/Weaviate/etc. head-to-head — the existing stack was already Postgres via Supabase, and pgvector avoids introducing an entirely new technology and its own ops burden for what's currently three tables and a few hundred rows. This is the right call *at this scale*. If retrieval volume or query complexity grows substantially, that's a real re-evaluation point, not a decision I'd defend as permanent.

**Single-hop graph traversal, not multi-hop.** `get_entity_relationships()` returns one entity's direct neighbors only — "what techniques are associated with assets that share a CVE with this asset" would need two hops, which this doesn't do. This matches what was actually scoped from the start, not a corner I cut under time pressure. It's explicitly future work, discussed below.

**Automated retention, not built.** No scheduled job deletes old rows — a manual, documented SQL query exists instead. Automating deletion means committing to a specific retention window (30 days? 90? 365?) before there's real usage data to justify one. I'd rather ship the manual escape hatch now and make that decision once usage patterns exist, than guess a number and encode it into an unattended job that deletes production data.

## Next Steps — What I'd Say If Asked "What's Left"

In priority order, each with a reason it's next rather than already done:

1. **Automated memory-row retention.** Highest-value next step. Two real implementation paths: a Supabase Edge Function on a cron schedule, or enabling the `pg_cron` Postgres extension (confirmed not currently installed) and running the deletion query natively in the database. The deletion logic itself is already proven correct — it's the documented manual query — the remaining work is purely safe scheduling, plus giving the scheduled version its own live-verified test before trusting it unattended (an off-by-one in date math is exactly the kind of bug that's invisible until it's already deleted the wrong rows).
2. **Multi-hop graph traversal and graph embeddings.** Today only the task-description *text* gets embedded, not the causal graph *structure* — two incidents with structurally similar graphs but different wording won't be recognized as similar. Multi-hop querying would need either a recursive Postgres CTE or a small number of chained single-hop calls in application code.
3. **A second, deeper Copilot review pass**, specifically targeting the branch-reconciliation files, requested but not yet returned as of this PR.

What's explicitly **not** next, so I don't accidentally imply it needs finishing: I'm not adding RLS policies to the memory tables (deny-all-except-service-role is a deliberate, reviewed decision — see below), and I'm not mounting the MCP server inside `api.py` (a stale onboarding script assumed exactly that and it was a real bug, fixed).

## The Database Side, If It Comes Up

Three tables: `memory_runs` (one row per completed run, with the 1536-dim embedding, HNSW-indexed), `memory_entities` (deduplicated across runs — same asset seen in ten incidents is one row with `last_seen` updated), `memory_entity_edges` (relationships, foreign-keyed to both entities and the originating run, `ON DELETE CASCADE`). Four migrations, now tracked as SQL files in `supabase/migrations/` — closing a real gap, since the schema had only ever existed as ad hoc changes applied directly to the live project with no local record.

**RLS is enabled with zero policies on all three tables — this is correct, not incomplete.** In Postgres, RLS enabled plus no policies means deny-all except the table owner and any role with `BYPASSRLS`. The backend authenticates with `SUPABASE_SERVICE_ROLE_KEY`, which has `BYPASSRLS` by default, so backend reads/writes work fine while the frontend's low-privilege anon key is locked out entirely — with no policy needed to enforce that. Concretely, this prevents a specific scenario: if the frontend's Supabase client were ever accidentally pointed at these tables directly (instead of going through the backend API), Postgres itself refuses the request, at the database layer, regardless of what application code does or doesn't check. I verified nothing in the frontend queries these tables today before relying on this.

Supabase's own advisory linter also caught two real issues after the schema was live — both RPC functions had a mutable `search_path` (a real, if narrow, privilege-escalation risk class for functions that reference unqualified table names), and one foreign key had no covering index. Both fixed in a fourth migration, reverified live against the running project afterward.

## How I Know This Actually Works — Not Just "Tests Pass"

This is worth being precise about because it's the strongest part of the story, and I don't want to undersell it into a generic "I wrote tests" line.

- **22/22 memory-layer tests passing against live infrastructure** — the real Supabase project and the real Gemini API, not mocks. This includes a full coordinator round-trip test, a real MCP-protocol round trip through `fastmcp.Client` (not just calling the underlying Python function), and a decay-math correctness test.
- **97/97 backend unit tests passing, zero regressions** — confirmed by direct comparison against the unmodified `main`, not assumed from a green run.
- **The decay formula was proven live before I wrote the test for it.** I backdated a row's `created_at` by exactly 30 days and measured its weight: `0.501575820192095`. `exp(-0.023 × 30) = 0.50158...` — matches to four decimal places. Only after that live confirmation did I write `test_temporal_decay.py` to codify it.
- **Three independent layers of proof for the MCP server specifically**, each catching a failure class the others can't: a mocked-store protocol test (fast, proves tool discovery and argument marshaling), a live in-memory protocol round trip against real Supabase (proves the whole chain works without needing a deployed process), and a live Docker/SSE check (`curl http://localhost:8001/sse` → `200 OK`, container confirmed running for hours, not crash-looping) — which is the only one of the three that would have caught the real deployment bug I found (below).
- **A "skip is not a pass" discipline** — integration tests skip silently without real credentials, which can misread as a clean pass. Every integration run in this project explicitly sourced `.env` into the same shell and checked the skip count was zero, not just the failure count.

## The Real Bugs I Found — Have These Ready, Don't Undersell Them

Six real bugs, from three different sources. I want to be able to state each one specifically, because "I found bugs" is a weak claim and "here's exactly what broke and how I found it" is a strong one.

1. **MCP server deployment bug (found by me, independent review).** The server's `__main__` block never passed `host`/`port` to `mcp.run()` for the SSE transport, so `MCP_PORT=8001` from Docker Compose was silently ignored and the server always bound to FastMCP's default `127.0.0.1:8000` — completely unreachable from the Docker host despite the container looking like it started fine. Fixed, then verified live against the actual running container.
2. **Non-idempotent entity-edge writes (Copilot finding, verified real).** `write_run()` unconditionally inserted edges — calling it twice for the same run (a retry, a rerun) would double them. Fixed with a delete-then-insert; verified live that two consecutive writes produce exactly one edge, not two.
3. **Credential-placeholder gap (Copilot finding, verified real).** `_memory_configured()` treated any non-empty `SUPABASE_SERVICE_ROLE_KEY` as configured — including `.env.example`'s literal placeholder text — so a fresh clone would try real network calls on every run and fail noisily. Fixed to match the same placeholder-detection heuristic the tests already used.
4. **Inefficient asset-timeline query (Copilot finding, verified real).** `get_asset_timeline()` pulled every edge in the time window and filtered client-side in Python. Fixed to resolve the asset entity ID first and filter server-side in Postgres; verified live that a real asset returns its edges and an unrelated one returns empty, confirming it's a targeted filter, not a full scan that happened to look right on a small dataset.
5. **Two stale onboarding-script references (Copilot finding, verified real).** A generated `.mcp.json` and a generated test-instructions file both pointed at `http://localhost:8000/mcp` — an HTTP bridge that was never built and never should be. Fixed to spawn the real stdio server directly; investigating why surfaced the whole onboarding script predated the standalone-MCP-server decision, so I cleaned up the rest of its staleness in the same pass rather than patching only the two flagged lines.
6. **A latent test bug the rebase itself introduced — Copilot never flagged this one.** Days after the rebase, rerunning the memory suite for an unrelated reason, `test_end_to_end.py` failed. It calls `execute_run()` without specifying `execution_mode`, which didn't exist when the test was written; the new default (`"standard"`) routed it through fast-path functions the test's mocks never accounted for — one traceback for a missing `publish_artifact` mock, a second for missing fallback-function imports in the test's faked `causal` module. Fixed by pinning `execution_mode="deep"` explicitly, matching the convention the codebase's other coordinator test already used. **The lesson I want to say out loud if asked:** "all tests passed right after I made the change" is not the same claim as "no latent bugs exist" — a default value silently changing behavior underneath an existing test is exactly the failure mode branch-reconciliation work produces, and it was only caught by re-running tests later, for an unrelated reason, not by the original green run.

One more, not a functional bug but worth naming: `ScenarioBuilder.tsx` got a new import from `main` (`@/lib/hivemind-types`, a path already renamed on my branch) in a region Git's three-way merge considered perfectly clean — zero conflict markers, because only one side had touched that exact line. It would have failed at build time, not at merge time. Caught by a deliberate repo-wide grep for leftover old-naming references after resolving the visible conflicts, not by the merge tool and not by any test. **The point worth making if this comes up:** "no conflict markers" is not the same claim as "nothing broke."

## Anticipated Questions — Exact Answers

**"Why does the LLM not do the entity extraction — wouldn't that be more flexible?"**
Because flexibility here means the LLM decides what counts as an asset or a technique, and that's exactly the kind of ungoverned judgment CausalOps's whole design exists to avoid. `extractor.py` is pure regex/dict matching against known ID formats (`T####` for MITRE techniques, `CVE-####-#####`) — zero LLM calls. It's less flexible and more auditable, on purpose.

**"What happens if Supabase goes down?"**
Nothing breaks. `memory_retrieve` and `memory_write` are both wrapped in try/except that logs and swallows. A run proceeds without past context if retrieval fails, and completes normally without being persisted to memory if the write fails. Memory is additive, never a dependency the rest of the system needs to function.

**"Why 1536 dimensions specifically?"**
It matches the database column, which was already sized for that dimensionality from the original Azure-based plan — switching to Gemini and truncating to 1536 avoided a schema migration. Not a number chosen for its own merits; a number chosen to not break an existing contract.

**"Why a 30-day half-life for the decay, not something else?"**
Honestly — it's a reasonable default, not a value derived from CausalOps-specific incident-recurrence data. I can defend the *mechanism* (recent runs should outrank equally-similar old ones without discarding old ones entirely) far more confidently than I can defend the specific number 0.023. If pushed on why not 60 or 90 days: I'd want real usage data before re-tuning it, same reasoning as the retention-window question.

**"Does this actually make the agents reason better over time?"**
Unmeasured, and I want to say that plainly rather than imply it's proven. The roadmap's language — "longitudinal reasoning, adaptive learning, higher-order strategic coordination" — is the intended *emergent effect* of the orchestrator having real historical context, not something a unit test can assert. The infrastructure is built and verified working; whether it measurably improves reasoning quality over time is a genuinely open question that would need real usage data to answer.

**"Couldn't Git's conflict detection have caught the ScenarioBuilder bug?"**
No, structurally — Git only flags a conflict when both sides changed the *same* line. Only `main`'s side touched that particular import line; my branch's changes to that file were elsewhere. The merge proceeded cleanly by Git's own definition of clean. I caught it with a deliberate post-merge grep for old naming, specifically because I don't trust "no conflict markers" as proof of correctness.

**"What would you do differently if you started over?"**
Two things. First, I'd write `test_coordinator_runner.py`-style explicit `execution_mode` pins into every coordinator test from day one, rather than discovering the gap after a rebase silently changed a default. Second, I'd measure the file-overlap between branches earlier and more routinely during long-running feature work, rather than only right before opening the PR — the 19-file overlap was real, quantifiable risk that existed for a while before I explicitly checked for it.

**"Is this ready to merge?"**
The memory-layer feature itself: yes — 22/22 live tests, all five roadmap components implemented and verified, zero regressions in the other 97 tests. What's not resolved: a second Copilot review pass specifically on the reconciliation files, requested but not yet returned. I'd say it's ready pending that second review coming back clean, not unconditionally ready.

**"How do you use AI coding tools in your workflow, concretely?"**
Every one of Copilot's five findings was independently re-verified against the actual code before I acted on it — not applied on faith, not dismissed on faith. All five turned out to be real. I also found a sixth bug it missed entirely while doing that verification work. That's the honest answer: useful second opinion, not infallible, and worth checking rather than either blindly trusting or ignoring.

## If the Room Is Non-Technical

A few terms, in plain language, in case they come up: an **embedding** is a numeric fingerprint of text such that similar meanings end up numerically close — this is what turns "find me a similar past incident" into math instead of keyword search. A **vector database** searches millions of these fingerprints efficiently. A **knowledge graph** is a network of entities and their relationships, built up across every investigation instead of reset each time. **Temporal decay** makes recent information matter more without throwing away old information. **MCP** is the standard protocol an AI agent uses to discover and call external tools — the same mechanism Claude Desktop and Claude Code themselves use, which is literally how I ran several of this project's own verification steps: by calling these tools the same way a production agent would.

## Where the Full Depth Lives, If Someone Wants More Than I Can Cover Live

- [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/01 - What is CausalOps (Project Primer)|What is CausalOps]] — full project primer with a worked incident example, for anyone starting from zero
- [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/02 - The Persistent Memory Layer, Component by Component|Component by Component]] — every component with real code
- [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/03 - Supabase Schema, Migrations & Data Layer|Schema & Migrations]] — full SQL, RLS reasoning
- [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/04 - The MCP Server and Protocol Bridge|MCP Server & Protocol Bridge]] — the three-layer testing story
- [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/05 - Reconciling With Main — The Rebase Story|The Rebase Story]] — the 111-files answer, in full
- [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/06 - Testing & Verification Methodology|Testing & Verification Methodology]] — the "prove it live first" discipline
- [[60_Claude/40_Project_Briefs/CausalOps/Memory Layer PR Summary/07 - Next Steps, Deferred Work & Career Takeaways|Next Steps & Career Takeaways]] — prioritized backlog, resume/interview framing
- PR itself: [darshgarg7/CausalOps#25](https://github.com/darshgarg7/CausalOps/pull/25)

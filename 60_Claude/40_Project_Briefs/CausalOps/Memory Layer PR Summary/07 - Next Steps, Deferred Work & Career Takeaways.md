---
type: project
status: active
created: 2026-07-09
tags: [causalops, memory-layer, next-steps, career, portfolio]
---

# Next Steps, Deferred Work & Career Takeaways

> [!info] This note answers two things directly and in detail: *"what's actually left to do, and how would I build it"* and *"how should I talk about this work outside this project — LinkedIn, GitHub, an interview, a performance review."*

## First, a Direct Answer to a Specific Question

**Yes — "what's deliberately out of scope" is the same thing as "future work."** Every item listed as deliberately out of scope in this project was scoped out for a *stated reason*, not forgotten, and every one of them is a legitimate candidate for a future PR. That distinction (deliberate scoping decision vs. oversight) is itself worth being able to explain clearly in a review or interview — it's the difference between "we ran out of time" and "we made a considered judgment call about what belongs in this specific change," and the second framing is both more accurate here and more credible to say out loud.

## What's Actually Left — In Priority Order, With Implementation Sketches

### 1. Automated memory-row retention (highest-value next step)

**What exists today:** a manual, documented SQL query (see [[03 - Supabase Schema, Migrations & Data Layer]]) — no scheduled job deletes anything automatically.

**Why it was deliberately deferred, not built:** automating deletion is a bigger, harder-to-reverse commitment than it sounds — it means picking a specific retention window (30 days? 90? 365?) *before* there's real usage data to justify one, and it means running an unattended job that deletes production data on a fixed schedule. The considered judgment was: build the manual escape hatch now (so retention *can* happen whenever someone decides it should), and defer the automation decision itself until real usage patterns exist to inform what window is actually correct. Picking a number now would be guessing, not engineering.

**A sketch of how it would actually get built, if picked up next:**
- Option A — a Supabase-native scheduled **Edge Function** (a serverless function Supabase can trigger on a cron schedule) that calls the existing manual query.
- Option B — enable the **`pg_cron`** Postgres extension (confirmed, directly, to *not* currently be installed on this project) and schedule the deletion query as a native Postgres cron job, keeping everything inside the database rather than adding a separate serverless component.
- Either way, the actual deletion logic already exists and is already proven correct (it's the documented manual query) — the remaining work is purely about *scheduling* it safely, plus (per item 4 below) giving that automation its own live-verified test before trusting it to run unattended.

### 2. Multi-hop graph traversal and graph embeddings

**What exists today:** single-hop entity-neighborhood lookup (`get_entity_relationships`) — see [[02 - The Persistent Memory Layer, Component by Component]] for exactly why this boundary exists and what it does and doesn't answer.

**What's still open, concretely:** the README's own "Future Work" section (updated as part of this PR to reflect what's actually done) lists two specific next steps in this area:
- **"Graph embeddings"** — today, only the *task description text* is embedded. The causal graph *structure* itself (which nodes, which edges, which relationships) is not — meaning two incidents with structurally similar causal graphs but differently-worded descriptions won't be recognized as similar by the current vector search. Embedding graph structure directly (e.g., via a graph-neural-network-style encoding, or a simpler serialize-and-embed approach) would close this gap.
- **"Multi-hop causal querying"** — e.g., "what techniques are associated with assets that share a CVE with this asset" requires walking two hops (asset → CVE → other assets with that CVE → their techniques), which the current single-hop `get_entity_neighborhood` RPC cannot do. This would likely mean either a recursive SQL query (Postgres supports recursive CTEs) or a small number of chained single-hop calls done in application code.

### 3. A second, deeper automated code-review pass

A follow-up review was explicitly requested — of every file touched by the branch-reconciliation work specifically (see [[05 - Reconciling With Main — The Rebase Story]]), not just the new memory-layer code — since that reconciliation was hand-done and is exactly the kind of work most likely to hide something an initial pass missed (as demonstrated by the fact that the *first* review pass itself missed the `execution_mode` default bug, which was only caught by manual re-verification). As of this writing, that second pass had not yet returned results. **What to do when it does return:** apply the same discipline as the first round — verify every finding independently before fixing it, don't dismiss anything without reasoning through it first, and specifically watch for anything in `coordinator/runner.py`'s mode-branching logic or the hand-merged config files, since those are exactly the areas most likely to still have a subtle issue.

### 4. Temporal-decay math has an automated test now — retention math would need the same treatment

The decay *search* math is now proven correct with a dedicated, live-verified test (see [[02 - The Persistent Memory Layer, Component by Component]]). If automated retention (item 1) is ever built, its own correctness — e.g., "does the scheduled job actually only delete rows older than exactly N days, and does it correctly leave everything newer untouched" — should get the exact same live-verification treatment described in [[06 - Testing & Verification Methodology]] before being trusted to run unattended in production. This is not a formality; an unattended deletion job with an off-by-one error in its date math is precisely the kind of bug that's invisible until it's already deleted the wrong data.

## What NOT to Do Next (Explicitly, So It Doesn't Get "Fixed" By Accident)

- **Do not add RLS policies** to the memory tables. Deny-all-except-service-role is a deliberate, reviewed decision (see [[03 - Supabase Schema, Migrations & Data Layer]], including the specific attack scenario it prevents), not an incomplete setup that needs "finishing."
- **Do not mount the MCP server inside `api.py`.** This has already been the subject of one real bug (a stale onboarding script assuming exactly this) — see [[04 - The MCP Server and Protocol Bridge]]. The standalone-process design is a deliberate architecture decision, not a temporary state.
- **Do not assume a clean CI run or a clean merge means nothing is broken** without the kind of independent re-verification described in [[06 - Testing & Verification Methodology]] — this project found two genuinely separate real bugs specifically *because* it didn't stop checking after the first green result.

## How This Work Is Useful on a Resume, LinkedIn, or GitHub — For an Upcoming AI Engineer

This is worth being specific and honest about, rather than vague. The *feature itself* ("I added a vector database to an AI agent") is a fine one-liner, but it is not the most valuable or most differentiating thing to highlight. The **process** this project demonstrates is more valuable, and more rare, and is what should actually anchor how this gets described externally — hiring managers and interviewers have seen "I added RAG to a chatbot" many times; they have seen far fewer candidates who can walk through a specific, real merge-conflict bug they caught and fixed.

### What to actually emphasize, ranked by how differentiating it is

1. **Reconciling a long-lived feature branch with a fast-moving main branch, safely.** This is a routine, high-stakes task at any real engineering job, and most engineers have a story about getting it wrong at least once. This project has a concrete, specific story about doing it carefully — including catching two real bugs the merge itself introduced, one of them completely invisible to Git's own conflict detection. **This is genuinely senior-level judgment**, not a beginner task, and it's rare to see it demonstrated this concretely in a portfolio piece, because most portfolio projects are built from scratch on an empty repository and never encounter this problem at all.
2. **Building retrieval-augmented memory for an agentic system** (vector search + knowledge graph + temporal decay) is a directly relevant, currently in-demand skill set — this maps precisely onto what production RAG (retrieval-augmented generation) and agent-memory systems look like in industry, described in the vocabulary the industry actually uses (embeddings, pgvector, HNSW indexing, temporal decay, cosine similarity, MCP). Being able to explain *why* 1536 dimensions, *why* a 30-day half-life, and *why* Postgres/pgvector instead of a dedicated vector database, shows genuine understanding rather than having copied a tutorial.
3. **Treating an AI code-review tool as a genuine second opinion rather than a checkbox** — verifying every one of its findings, and finding one more real bug it missed — is a specific, demonstrable example of working *with* AI tooling critically rather than either blindly trusting it or ignoring it. This is an increasingly relevant skill to be able to speak to directly, given how much of the industry now uses these tools, and it's a good, concrete answer to the increasingly common interview question "how do you use AI tools in your workflow."
4. **The MCP (Model Context Protocol) work specifically** is current, in-demand, and not yet common experience — MCP is the emerging standard for how AI agents connect to tools and data (the same protocol Claude Desktop and Claude Code themselves use), and building a real MCP server (not a toy "hello world" example) with genuine protocol-level test coverage — as opposed to just calling the underlying Python functions directly — is a concrete, specific, and current thing to be able to talk about that most candidates cannot.
5. **Statistical rigor in an AI system** — the "LLM proposes, deterministic code falsifies" design principle this whole project (not just this PR) is built around is itself a strong thing to understand and be able to explain, even though this specific PR didn't build that principle — understanding *why* a system refuses to answer when evidence is weak, and being able to explain that as a deliberate trustworthiness feature rather than a limitation, demonstrates a level of thinking about AI system design that goes beyond "make the model answer confidently."

### A concrete way to phrase this for a resume or LinkedIn post (adapt freely, don't copy verbatim)

> *Designed and shipped a persistent memory layer for a multi-agent causal-reasoning system: vector retrieval (pgvector), a cross-run entity knowledge graph, and temporal decay-weighted ranking, exposed via a standalone MCP server with full protocol-level test coverage. Reconciled the feature branch with five commits of unrelated upstream changes (new LLM backend, new execution-mode architecture), catching and fixing two real bugs introduced by the merge — including one invisible to Git's own conflict detection. Verified every AI-code-review finding independently before acting on it, and found an additional bug the review missed.*

**A shorter, single-line variant, if space is limited:**

> *Built a Supabase/pgvector-backed memory layer with temporal decay and MCP protocol exposure for a multi-agent system; reconciled it against a diverged main branch, catching two real bugs the merge itself introduced.*

### Interview questions this work directly prepares you to answer well

- *"Tell me about a time you had to merge a long-lived branch with significant drift from main."* — Use the [[05 - Reconciling With Main — The Rebase Story]] example directly: the squash-vs-rebase decision, the 19-file overlap measurement done *before* starting, and both real bugs found (one from the merge, one invisible to the merge tool entirely).
- *"How do you verify something actually works, beyond the tests passing?"* — Use [[06 - Testing & Verification Methodology]]: the "prove it live first" discipline, the worktree-comparison technique for distinguishing pre-existing issues from newly-introduced ones, and being specific about the "a skip is not a pass" trap.
- *"Describe a system you built that uses vector search / RAG / embeddings."* — Use [[02 - The Persistent Memory Layer, Component by Component]]: be ready to explain cosine similarity, why 1536 dimensions was chosen, what the temporal-decay formula does and why a 30-day half-life, and the specific idempotency bug found and fixed in the write path.
- *"How do you use AI coding tools, and how do you know you can trust their output?"* — Use the Copilot-review story from [[06 - Testing & Verification Methodology]]: five real findings, all independently verified before fixing, plus one additional bug found that the tool missed — a concrete example of critical, non-blind use of AI tooling.
- *"What would you build next if you had another sprint on this?"* — Use the prioritized list above: automated retention (and why it wasn't built yet), multi-hop traversal, graph embeddings — each with a one-sentence reason it's next rather than done.

### For a GitHub portfolio / pinned repo description

If this repo (or a similar one) is used as a portfolio piece, the pull request itself (`darshgarg7/CausalOps#25`) is a legitimate, presentable artifact — not something to hide the mechanics of. A detailed, honest PR description and commit history (which this project has, deliberately, including a commit message that explicitly documents the two real rebase-introduced bugs and their fixes) *is* the portfolio piece. A reviewer or interviewer who reads the actual commit messages and PR description gets a genuine, verifiable demonstration of engineering judgment, not just a claim about it made after the fact in a resume bullet.

### What to be honest about, if asked directly — this matters for credibility

- The *"longitudinal reasoning, adaptive learning, higher-order strategic coordination"* language from the original roadmap sentence is **aspirational** — the infrastructure enabling it is built and tested, but whether it produces measurably better reasoning over time has not been measured, and saying so plainly if asked is more credible than implying it's already proven.
- Retention automation, multi-hop traversal, and a second review pass are genuinely unfinished — say so plainly rather than implying total completeness. A reviewer who asks "what's left" and gets a clear, prioritized answer (as in this note) reads as more credible than one who claims everything is done, and demonstrates exactly the kind of "know the boundary of what you actually verified" discipline described throughout [[06 - Testing & Verification Methodology]].

## Where to Go Next

If you need the whole story again from the top: [[00 - Executive Summary (Meeting Prep)]].

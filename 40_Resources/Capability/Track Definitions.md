---
type: evergreen
status: tree
created: 2026-04-24
updated: 2026-04-24
tags:
  - evergreen
  - system
  - capability
notes:
  - "[[Capability Engine Guide]]"
  - "[[Vault Operating System]]"
  - "[[Metadata Extension Guide]]"
---
# Track Definitions
Five tracks organize all long-term capability work. The `track` field accepts only: `ai`, `systems`, `algorithms`, `career`, `trading`.
A concept note can belong to multiple tracks when it genuinely spans domains (e.g., observability touches both `systems` and `ai`).
## AI (`ai`)
**Scope**: ML fundamentals, agents, MCP tooling, prompt engineering, AI-assisted workflows, evaluation, automation.
**Primary vault sources**:
- `40_Resources/CS/AI/` — durable AI reference notes
- AI-related clippings in `60_Claude/05_Clippings/`
- AI distilled notes in `60_Claude/20_Distilled_Notes/`
- MCP, agent, and workflow notes scattered across the vault
**What belongs here**: transformer internals, RAG retrieval mechanics, MCP server design, prompt patterns that actually work, agent planning strategies, LLM evaluation methods.
**What does not**: general programming concepts that happen to use an AI library. If the core idea is "how to call an API," that is `systems`.
**Boards**: [[AI Field OS]] · [[AI Depth Ladder]] · [[AI Question Bank]]
## Systems (`systems`)
**Scope**: Backend engineering, infrastructure, Rust, observability, data flow, Docker, Kafka, MongoDB, APIs, deployment.
**Primary vault sources**:
- `20_Progress/UROP/` — UROP research and [[BOOM Board]] concepts
- Rust learning path notes
- Backend, API, observability, Docker, Kafka, MongoDB notes across `40_Resources/` and `20_Progress/`
**What belongs here**: distributed tracing, Kafka consumer group rebalancing, Docker networking, Rust ownership and borrowing, MongoDB aggregation pipelines, API versioning strategies.
**What does not**: pure algorithm analysis (that is `algorithms`). If the note is about how a hash map works theoretically, it is algorithms. If it is about choosing Redis vs Memcached for a caching layer, it is systems.
**Boards**: [[Systems Field OS]] · [[Systems Depth Ladder]] · [[Systems Question Bank]]
## Algorithms (`algorithms`)
**Scope**: Data structures, algorithms, complexity analysis, OCaml, functional programming, algorithmic reasoning, problem-solving patterns.
**Primary vault sources**:
- `10_UMN/CSCI 4041/` — algorithms and data structures coursework
- `10_UMN/CSCI 2041/` — functional programming and OCaml
- DSA and complexity notes in `40_Resources/CS/`
**What belongs here**: graph traversal, dynamic programming recurrences, OCaml pattern matching, tree rotations, amortized analysis, sorting trade-offs, induction proofs.
**What does not**: implementation-focused notes about using a library's sort function. If the note is about quicksort's partition scheme, it is algorithms. If it is about configuring a database index, it is systems.
**Feeder layer note**: `10_UMN/` is treated as a feeder. Prefer creating distilled mirror notes in `40_Resources/` or `60_Claude/20_Distilled_Notes/` over restructuring school notes. Selective enrichment of flagship notes is fine when it builds long-term understanding.
**Boards**: [[Algorithms Field OS]] · [[Algorithms Depth Ladder]] · [[Algorithms Question Bank]]
## Career (`career`)
**Scope**: Portfolio building, interview prep, mentorship, internship search, career strategy, project briefs, professional storytelling.
**Primary vault sources**:
- `20_Progress/Career/` — career strategy and internship search
- `20_Progress/Mentorship Program/` — mentorship notes
- Portfolio and project brief notes
**What belongs here**: STAR method mechanics, portfolio bullet construction from real project evidence, technical interview patterns, mentorship feedback loops, career positioning.
**What does not**: general project execution notes. If the note is about how to run a sprint, it is probably `systems`. If it is about how to tell the story of that sprint in an interview, it is `career`.
**Boards**: [[Career Field OS]] · [[Career Depth Ladder]] · [[Career Question Bank]]
## Trading (`trading`)
**Scope**: Financial markets, trading tools, quantitative workflows, market analysis, trading strategy.
**Primary vault sources**:
- `40_Resources/Trading/` — durable trading reference notes
- Trading-related clippings in `60_Claude/05_Clippings/`
- Market workflow and tooling notes
**What belongs here**: technical analysis mechanics, AI-assisted trading workflows, order flow analysis, risk management math, backtesting methodology.
**What does not**: general statistics or probability theory (that is `algorithms` unless it is specifically applied to a trading context).
**Boards**: [[Trading Field OS]] · [[Trading Depth Ladder]] · [[Trading Question Bank]]
## Cross-Track Concepts
Some concepts genuinely span tracks. Use the `track` list to assign multiple values:
```yaml
track:
  - systems
  - algorithms
```
Concrete examples from this vault:
- **Rust ownership vs OCaml immutability** — both enforce memory safety, but through different mechanisms (`systems` + `algorithms`)
- **Kafka pipelines vs agent tool orchestration** — both are async message-passing systems with different failure modes (`systems` + `ai`)
- **Observability in backend vs evaluation in AI** — same idea (instrument, measure, debug), different domains (`systems` + `ai`)
Cross-track concepts are strong candidates for synthesis notes in `60_Claude/20_Distilled_Notes/Synthesis/`.
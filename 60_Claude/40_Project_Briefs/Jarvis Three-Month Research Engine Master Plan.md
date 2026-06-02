---
type: project
status: active
created: 2026-04-24
updated: 2026-04-24
tags:
  - project
  - jarvis
  - ai
  - pkm
  - research-engine
  - roadmap
notes:
  - "[[Jarvis]]"
  - "[[00_Dashboard]]"
  - "[[AI_CONTEXT]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/Obsidian/Jarvis Enrichment Engine]]"
  - "[[40_Resources/Capability/Capability Engine Guide]]"
  - "[[40_Resources/CS/AI/MCPs]]"
  - "[[Knowledge Enrichment Dashboard]]"
  - "[[Capability Dashboard]]"
next: Build Week 1 registry hardening and conversation capture spine.
---
# Jarvis Three-Month Research Engine Master Plan
## One-Line Mission
Build Jarvis into my private AI research engine: a vault-native system that all my AI tools can read through Obsidian/MCP, that captures my future LLM conversations, strengthens my existing notes, and answers questions from my own knowledge with evidence.
## What Jarvis Is Supposed To Become

Jarvis is not a notes folder with AI sprinkled on top.

Jarvis is a separate project whose output is an operating system for my knowledge:

- a private research engine
- a learning coach
- a semantic memory layer
- a project context server
- a source-grounded answer system
- a conversation recorder for all LLMs I use
- a place where every concept I care about becomes concrete, connected, and testable

The future state is simple to describe:

> Before any AI helps me, it can ask Jarvis what I already know, what I am working on, what I have tried, what decisions I made, and where the source notes are.

Jarvis should make my AI tools feel less like strangers and more like agents inside my actual life context.

## Non-Negotiable Principles

### 1. Jarvis Is The Source Of Context

Every AI I use should treat Jarvis as the context source:

- Codex reads the vault before changing project files.
- Claude Code reads `AI_CONTEXT`, dashboards, and relevant notes before writing.
- Kiro specs link to Jarvis notes instead of inventing context.
- Cursor rules point to Jarvis context files.
- ChatGPT/Claude web conversations get exported or summarized back into Jarvis.
- Ollama/local models operate on indexed vault content.

### 2. Human Notes Are Allowed To Stay Human

Jarvis can edit this vault, but it should not flatten my notes into generic AI prose.

Default enrichment rule:

```text
preserve existing note
append Jarvis Enrichment
add links, definitions, examples, drills, source anchors
leave original structure visible
```

### 3. Raw Conversation Is Not Knowledge Yet

LLM conversations are valuable, but raw transcripts are noisy.

Store three layers:

1. raw conversation archive
2. normalized machine registry
3. human-useful distillation

Only durable insights get promoted into concept notes, project briefs, outputs, or dashboards.

### 4. Jarvis Must Say What It Does Not Know

The system is only useful if it can refuse fake certainty.

Every answer should be able to say:

- I found strong support in these notes.
- I found partial support.
- This is inferred.
- The vault does not know this yet.
- This note needs enrichment.

### 5. Build The Spine Before The Brain

The first month should not chase fancy UI or agent hype.

The spine is:

- registry
- indexing
- conversation capture
- context packs
- enrichment queue
- evaluation set

Once that works, Jarvis can become powerful without becoming chaotic.

## Current Foundation

Jarvis already has:

- [[AI_CONTEXT]] as shared context manifest
- [[00_Dashboard]] as control panel
- [[40_Resources/Obsidian/Vault Operating System]] as schema contract
- [[40_Resources/Obsidian/Jarvis Enrichment Engine]] as enrichment workflow
- [[Knowledge Enrichment Dashboard]] as enrichment queue
- [[40_Resources/Capability/Capability Engine Guide]] as mastery/drill/output system
- `30_Order/System/jarvis-cli/` as deterministic local CLI
- `.claude/skills/` and `.claude/agents/` as Claude Code operations layer
- `.kiro/specs/` as planning/spec layer
- `.cursor/rules/` as Cursor context wrappers
- Obsidian Local REST API MCP configuration

The current problem is not lack of structure. The problem is lack of depth, indexing, and operational memory across all tools.

## Final Three-Month Outcome

By the end of three months, Jarvis should be able to:

1. ingest and index the whole vault
2. record new AI conversations into a registry
3. build context packs for any AI/tool
4. answer questions from the vault with citations
5. enrich weak notes across the whole vault
6. create learning paths from existing notes
7. track mastery and drills
8. expose gaps and contradictions
9. produce research briefs from vault + sources
10. act as the default memory layer for AI/ML projects I build later

## Architecture Overview

```text
AI tools I use
  -> Obsidian MCP / local files / exports
  -> Jarvis context pack builder
  -> answer and research engine
  -> conversation registry
  -> enrichment engine
  -> semantic index + graph index
  -> Obsidian dashboards and notes
```

## Core Subsystems

### A. Vault Substrate

Purpose: make the vault machine-readable and safe to operate on.

Components:

- Markdown note registry
- frontmatter schema
- file hash tracking
- link graph
- metadata health checks
- enrichment candidate scoring
- source/citation registry

Main files:

- `30_Order/System/jarvis-cli/`
- `40_Resources/Obsidian/Vault Operating System.md`
- `60_Claude/60_Indexes/Vault Health Dashboard.md`
- `60_Claude/60_Indexes/Knowledge Enrichment Dashboard.md`

### B. AI Conversation Memory

Purpose: capture LLM conversations so future tools can learn from decisions without reading raw chat dumps.

Storage:

```text
60_Claude/05_Clippings/AI Conversations/
60_Claude/30_Source_Summaries/AI Conversations/
30_Order/System/jarvis-memory/conversations.sqlite
30_Order/System/jarvis-memory/conversations.jsonl
```

Conversation schema:

```json
{
  "conversation_id": "stable id",
  "source_app": "codex|claude-code|chatgpt|cursor|kiro|ollama|other",
  "title": "human title",
  "started_at": "timestamp",
  "ended_at": "timestamp",
  "project": "Jarvis",
  "topics": ["ai", "pkm", "retrieval"],
  "decisions": [],
  "actions": [],
  "related_notes": [],
  "raw_path": "",
  "summary_path": "",
  "status": "raw|distilled|promoted|archived",
  "checksum": ""
}
```

### C. Context Pack Builder

Purpose: give any AI exactly the relevant Jarvis context for the task.

Pack types:

- `live`: dashboard, session log tail, active projects
- `project`: project notes, specs, decisions, open tasks
- `topic`: concept notes, prerequisites, source summaries, related outputs
- `agent`: tool-specific instructions for Codex, Claude, Cursor, Kiro
- `research`: vault notes + source summaries + unanswered questions

Context pack rule:

```text
small enough to fit
rich enough to orient
cited enough to verify
specific enough to act
```

### D. Semantic Index

Purpose: retrieve by meaning, not just filenames.

Index fields:

- note path
- heading path
- chunk text
- note type
- status
- track
- source status
- enrichment status
- updated date
- embedding model
- hash

Retrieval modes:

- keyword search
- semantic search
- hybrid search
- graph-expanded search
- recent conversation search

### E. Knowledge Graph

Purpose: make relationships first-class.

Edges:

- note links
- prerequisites
- used_in
- evidence
- source_concepts
- related_progress
- concepts
- tracks
- generated entities
- conversation-to-note links

Questions graph should answer:

- What should I learn before this?
- What projects prove this concept?
- What notes repeat the same idea?
- What source summaries feed this concept?
- Which concept has no evidence?
- Which AI conversation decided this?

### F. Enrichment Factory

Purpose: turn weak existing notes into strong learning nodes.

Pipeline:

```text
candidate note
  -> profile note
  -> retrieve related notes
  -> detect missing learning sections
  -> draft enrichment
  -> critic pass
  -> append under Jarvis Enrichment
  -> update metadata
  -> create drills
```

### G. Query And Answer Engine

Purpose: answer questions from Jarvis with citations and uncertainty.

Answer modes:

- quick answer
- teach me
- compare
- trace topic
- research brief
- exam mode
- project context
- build plan
- what do I know about X?
- what am I missing about X?

### H. Research Workbench

Purpose: help me explore AI/ML and other future projects without losing the trail.

Research brief structure:

- question
- what Jarvis already knows
- source notes
- external sources if used
- concept map
- gaps
- next notes to enrich
- experiments to run
- follow-up questions

### I. Evaluation And Truthfulness

Purpose: prevent Jarvis from becoming a confident hallucination machine.

Checks:

- citation coverage
- source support
- contradiction detection
- stale/future-date warnings
- answer benchmark
- retrieval hit-rate
- human writing check
- provenance labels

## Three-Month Build Map

# Month 1 - Build The Spine

Month 1 is about making Jarvis structurally aware of itself.

No flashy interface yet. No pretending it is a perfect AI brain yet.

The deliverable is the backend spine: registry, context packs, conversation capture, indexing, and a reliable enrichment queue.

## Week 1 - Jarvis Project Spine And Registry Hardening

### Goal

Turn Jarvis into a visible standalone project with a clear build control plane.

### Build

1. Create/maintain [[Jarvis]] as the project hub.
2. Treat this file as the canonical three-month roadmap.
3. Extend `jarvis_ops.py` into a stable CLI surface.
4. Create `30_Order/System/jarvis-memory/`.
5. Define registry schemas:
   - notes
   - chunks
   - conversations
   - source summaries
   - enrichment events
   - answer benchmark
6. Add a `jarvis status` command that reports:
   - vault file count
   - indexed note count
   - enrichment candidates
   - active conversations waiting for distillation
   - open benchmark failures
   - stale projects

### Implementation Details

Registry tables:

```text
notes(id, path, title, type, status, track, hash, updated, indexed_at)
headings(id, note_id, heading, level, position)
links(source_note_id, target, target_note_id, link_type, status)
chunks(id, note_id, heading_path, text, hash, token_estimate)
conversations(id, source_app, title, started_at, raw_path, summary_path, status)
enrichment_events(id, note_id, level, created, summary)
benchmarks(id, question, expected_notes, status, last_score)
```

### Deliverables

- Jarvis project hub
- local registry folder
- schema file
- `jarvis status`
- updated dashboard links

### Acceptance Test

Run:

```powershell
.\30_Order\System\jarvis-cli\jarvis.ps1 health
.\30_Order\System\jarvis-cli\jarvis.ps1 enrich-candidates --limit 25
```

Pass if:

- Jarvis project appears in active projects
- registry schema is documented
- candidate queue is reproducible
- no raw clippings are modified

## Week 2 - Conversation Capture Spine

### Goal

Make Jarvis capable of remembering future LLM conversations without dumping chaos into the vault.

### Why This Matters

You are going to use many AIs:

- Codex
- Claude Code
- Kiro
- Cursor
- ChatGPT
- Claude web
- Ollama/local models
- future AI/ML agents

If those conversations are not captured, your reasoning history disappears. If raw transcripts are dumped blindly, the vault becomes noise.

### Build

1. Create folders:

```text
60_Claude/05_Clippings/AI Conversations/
60_Claude/30_Source_Summaries/AI Conversations/
60_Claude/60_Indexes/AI Conversation Dashboard.md
30_Order/System/jarvis-memory/
```

2. Build conversation import command:

```powershell
jarvis conversation-import "path/to/export"
```

3. Build conversation registry command:

```powershell
jarvis conversations
jarvis conversations --undistilled
jarvis conversations --project Jarvis
```

4. Define conversation distillation template:

```markdown
# Conversation Summary

## What Was Decided
## What Changed
## Important Context
## Source Claims
## Inferred Claims
## Open Questions
## Follow-Up Actions
## Related Notes
## Should Be Promoted?
```

### Initial Adapters

Build in this order:

1. manual Markdown transcript import
2. Codex/Codex Desktop exported summaries or copied session logs
3. Claude Code/Claude exported conversation text
4. Kiro spec conversation notes
5. ChatGPT export format
6. Cursor chat export or copied summary

### Acceptance Test

Import three conversations:

- one Jarvis/Codex conversation
- one Kiro plan/spec conversation
- one ChatGPT/Claude web conversation

Pass if:

- all three appear in registry
- raw files stay in clippings
- summaries are created in source summaries
- session log gets one line per import
- no transcript is promoted as durable knowledge automatically

## Week 3 - Context Pack Builder For All AIs

### Goal

Make every AI tool start from Jarvis context.

### Build

Command:

```powershell
jarvis context-pack --mode live
jarvis context-pack --mode project --project Jarvis
jarvis context-pack --mode topic --query "MCP and Obsidian"
jarvis context-pack --mode agent --agent codex
```

### Context Pack Format

```markdown
# Jarvis Context Pack

## Task
## Live State
## Relevant Project Notes
## Relevant Concepts
## Recent Conversations
## Open Decisions
## Safety Rules
## Suggested Next Actions
```

### Agent-Specific Requirements

Codex pack:

- AGENTS.md
- AI_CONTEXT.md
- current project note
- relevant files
- latest session log entries

Claude Code pack:

- CLAUDE.md
- AI_CONTEXT.md
- skills/agents involved
- relevant vault notes

Kiro pack:

- steering files
- relevant spec folder
- requirements/design/tasks links

Cursor pack:

- `.cursor/rules`
- project context
- coding/spec notes

ChatGPT/Claude web pack:

- compressed project summary
- relevant notes
- constraints
- what not to rewrite

### Acceptance Test

Ask three tools the same task after giving them a context pack:

> What is Jarvis, what phase is it in, and what should I build next?

Pass if their answers agree on:

- Jarvis as separate project
- current phase
- active next action
- no raw clipping mutation
- enrichment-first note strategy

## Week 4 - Index V1 And Enrichment Factory V1

### Goal

Make Jarvis able to profile any note and decide how to strengthen it.

### Build

Commands:

```powershell
jarvis index
jarvis note-profile "path/to/note.md"
jarvis enrich-plan "path/to/note.md"
jarvis enrich-note "path/to/note.md" --dry-run
```

### Note Profile Should Show

- note type
- status
- track
- word count
- headings present
- headings missing
- backlinks
- outlinks
- source anchors
- evidence links
- drill fields
- recommended enrichment mode

### Enrichment Plan Should Include

- what to preserve
- what to append
- source notes to use
- missing definitions
- missing examples
- missing contrasts
- drill suggestions
- confidence

### Seed Work

Enrich 25 notes:

- 8 AI/tooling notes
- 8 algorithms/programming notes
- 5 systems/UROP notes
- 4 project/career notes

### Acceptance Test

Pass if:

- enriched notes keep original content
- `enrichment_status` is updated
- each enrichment has source anchors
- candidate queue decreases
- no mass rewrite happens

# Month 2 - Build The Brain

Month 2 is where Jarvis starts acting like a knowledge engine.

The goal is semantic retrieval, graph reasoning, question answering, and learning flows.

## Week 5 - Semantic Search And Chunk Index

### Goal

Make Jarvis retrieve by meaning.

### Build

1. Chunk all approved notes.
2. Create embeddings locally first.
3. Store embeddings with chunk IDs.
4. Add semantic search command:

```powershell
jarvis semantic-search "why does greedy fail for knapsack"
```

5. Add hybrid search:

```powershell
jarvis search "observability tracing metrics" --hybrid
```

### Approved Index Sources

Index:

- `10_UMN/`
- `20_Progress/`
- `40_Resources/`
- `60_Claude/20_Distilled_Notes/`
- `60_Claude/30_Source_Summaries/`
- `60_Claude/40_Project_Briefs/`
- selected conversation summaries

Do not index raw clippings as equal peers.

### Ranking Formula

Score should combine:

- semantic similarity
- keyword match
- title match
- note status
- enrichment status
- track match
- graph distance
- recency when useful

### Acceptance Test

Create 30 semantic queries.

Pass if top 5 results include expected notes at least 80% of the time.

Example queries:

- "local models for private note analysis"
- "why tracing beats logs in a distributed system"
- "how OCaml checks mistakes before runtime"
- "what makes dynamic programming different from greedy"
- "what should I build next for Jarvis"

## Week 6 - Knowledge Graph V1

### Goal

Make relationships queryable.

### Build

Commands:

```powershell
jarvis graph build
jarvis graph-neighborhood "OCaml"
jarvis prerequisites "Dynamic Programming"
jarvis evidence "Observability and Tracing"
jarvis gaps --track ai
```

### Graph Edge Types

```text
links_to
backlinked_by
prerequisite_of
used_in
evidenced_by
source_of
conversation_about
same_track_as
contrasts_with
duplicate_candidate
```

### Graph Dashboards

Create:

- Knowledge Graph Dashboard
- Orphan Concepts Dashboard
- Prerequisite Gaps Dashboard
- Evidence Graph Dashboard

### Acceptance Test

Ask:

- What concepts support Jarvis?
- What concepts support AI/ML project readiness?
- Which notes are central but under-enriched?
- Which concepts have no proof/evidence?

Pass if the graph returns useful neighborhoods, not only raw link lists.

## Week 7 - Ask Jarvis V1

### Goal

Build the first answer engine.

### Command

```powershell
jarvis ask "Explain MCP in the context of my vault"
```

### Answer Contract

Every answer must include:

```markdown
## Answer
## Evidence From Jarvis
## Related Notes
## Confidence
## What Jarvis Does Not Know Yet
## Next Useful Action
```

### Modes

```powershell
jarvis ask "..." --mode quick
jarvis ask "..." --mode teach
jarvis ask "..." --mode compare
jarvis ask "..." --mode research
jarvis ask "..." --mode exam
```

### Retrieval Pipeline

```text
query
  -> classify intent
  -> keyword search
  -> semantic search
  -> graph expansion
  -> conversation search
  -> rerank
  -> answer with citations
  -> uncertainty check
```

### Acceptance Test

Create a benchmark of 75 questions:

- 15 definition questions
- 15 comparison questions
- 15 course/exam questions
- 15 project context questions
- 15 research synthesis questions

Pass if:

- answer cites sources
- retrieved notes are relevant
- uncertainty is explicit
- no unsupported claims are presented as fact

## Week 8 - Tutor, Drill, And Learning Path Engine

### Goal

Make Jarvis teach me.

### Build

Commands:

```powershell
jarvis teach "OCaml"
jarvis quiz "Time Complexity"
jarvis drill-due
jarvis learning-path "AI agents"
jarvis explain-ladder "Dynamic Programming"
```

### Tutor Modes

- beginner mode
- 30-second review
- deep dive
- exam cram
- interview mode
- implementation mode
- misconception mode

### Learning Path Output

```markdown
# Learning Path

## Goal
## Prerequisites
## Core Notes
## Order
## Practice Questions
## Build/Proof Task
## Evidence To Create
```

### Capability Integration

Update only with approval:

- `last_drilled`
- `next_drill`
- `mastery_score`
- `mastery_level`

### Acceptance Test

For 20 concepts:

- generate a learning path
- generate quiz questions
- grade sample answers
- suggest next drill date
- produce evidence ideas

# Month 3 - Build The Research Engine

Month 3 turns Jarvis from a good vault assistant into a serious research system.

It should help decide what to study, what to build, what is missing, and what sources to trust.

## Week 9 - Source Ingestion And Research Feed

### Goal

Make external sources flow into Jarvis without polluting it.

### Build

Commands:

```powershell
jarvis ingest-source "file.md"
jarvis ingest-batch --limit 5
jarvis source-status
jarvis source-dedupe
```

### Ingestion Pipeline

```text
raw source
  -> clipping
  -> source summary
  -> claim extraction
  -> entity/concept extraction
  -> related note search
  -> promotion recommendation
```

### Source Summary Must Include

- source URL/path
- source type
- date accessed
- key claims
- source strength
- what is useful to Jarvis
- what should be ignored
- related notes
- promotion recommendation

### Acceptance Test

Process 30 clippings.

Pass if:

- no raw clipping is rewritten
- each summary cites source
- duplicates are detected
- only reusable ideas are promoted

## Week 10 - Research Brief Generator

### Goal

Make Jarvis produce serious research briefs for topics I might deep dive into.

### Command

```powershell
jarvis research "AI agents for personal knowledge systems"
```

### Research Brief Structure

```markdown
# Research Brief

## Research Question
## Why This Matters For Me
## What Jarvis Already Knows
## Source Notes
## External Sources Used
## Core Concepts
## Concept Map
## Technical Stack Options
## Experiments To Run
## Risks / Unknowns
## Notes To Enrich
## Project Ideas
## Next 7 Days
```

### Research Areas To Seed

Because you are not sure yet where to deep dive in AI/ML, Jarvis should help explore:

- AI agents
- RAG and GraphRAG
- local models and Ollama
- AI evaluation
- multimodal AI
- agent memory
- AI coding workflows
- knowledge graphs
- data pipelines for AI
- observability for AI systems

### Acceptance Test

Create 5 serious research briefs.

Pass if each brief:

- uses vault context
- identifies what is missing
- suggests experiments
- links to notes
- creates an enrichment queue

## Week 11 - Truthfulness, Validation, And Contradiction Layer

### Goal

Make Jarvis trustworthy enough to rely on.

### Build

Commands:

```powershell
jarvis validate-answer "question"
jarvis source-gaps
jarvis contradiction-scan "MCP"
jarvis stale-knowledge
jarvis confidence-report
```

### Validation Checks

1. Does the answer cite notes?
2. Do cited notes actually support the answer?
3. Is the claim copied, inferred, or external?
4. Are there conflicting notes?
5. Is the note stale?
6. Does the vault lack enough knowledge?
7. Is the answer too generic?

### Confidence Labels

Use:

- `vault-grounded`
- `source-grounded`
- `inferred`
- `uncertain`
- `missing`

### Acceptance Test

Build 30 trick questions:

- things not in the vault
- ambiguous topics
- stale notes
- duplicate concepts
- partially supported claims

Pass if Jarvis admits uncertainty instead of inventing.

## Week 12 - Operating System, Demo, And Scale Plan

### Goal

Make Jarvis usable every day and ready for future AI/ML projects.

### Build Daily Loop

Morning:

```text
context pack
health check
drill queue
top enrichment candidates
active project next actions
conversation import reminders
```

During work:

```text
ask Jarvis
capture conversations
enrich notes
research topics
log decisions
```

Evening:

```text
closeday
conversation distillation
what changed
what is still open
next actions
```

Weekly:

```text
10 notes enriched
5 conversations distilled
1 research brief
1 synthesis note
benchmark run
index rebuild
```

### Final Demo

Jarvis should be able to perform this demo:

1. Import an AI conversation.
2. Summarize decisions.
3. Link it to the Jarvis project.
4. Answer a question using vault sources.
5. Identify missing knowledge.
6. Enrich a weak note.
7. Generate a learning path.
8. Create a research brief.
9. Log everything.

### Acceptance Test

End-of-three-month targets:

- 100+ enriched notes
- 75 benchmark questions
- 80%+ answer benchmark pass rate
- 50+ conversation summaries indexed
- 5 research briefs
- semantic index operational
- graph index operational
- context packs for Codex, Claude Code, Kiro, Cursor, ChatGPT/Claude web
- every active project has `next`
- Jarvis can say what it knows and what it does not know

## Detailed Workstreams

## Workstream 1 - Conversation Memory

### Why

The biggest missing layer is durable conversation memory.

You are going to make many decisions with LLMs. If Jarvis does not capture those decisions, every new AI starts from zero.

### Build Order

1. manual import folder
2. registry schema
3. transcript normalizer
4. summary generator
5. promotion gate
6. conversation dashboard
7. search over conversations
8. context-pack integration

### Done Means

You can ask:

> What did I decide last week about Jarvis retrieval?

and get:

- conversation summary
- source transcript
- decisions
- linked notes
- open actions

## Workstream 2 - AI Tool Integration

### Why

Every AI should become more useful because it can read Jarvis.

### Integration Policy

All AI tools should follow this pattern:

```text
read AI_CONTEXT
read relevant context pack
read active project note
use Obsidian MCP/local files for note context
write outputs back to correct Jarvis layer
append session log
```

### Tool-Specific Integration

Codex:

- implementation
- CLI scripts
- vault automation
- codebase changes
- testing

Claude Code:

- note operations
- skills and agents
- distillation
- writing quality

Kiro:

- requirements
- design
- task planning
- spec-driven development

Cursor:

- codebase editing
- project implementation
- app/UI work

ChatGPT/Claude web:

- long brainstorming
- research synthesis
- model comparison
- high-level planning

Ollama:

- local extraction
- embeddings
- private note classification
- cheap first-pass parsing

## Workstream 3 - Enrichment Factory

### Why

The vault already has structure. Now the nodes need depth.

### Enrichment Levels

Light:

- definition
- links
- questions

Standard:

- definition
- mechanism
- example
- contrast
- misconceptions
- source anchors
- drills

Deep:

- formal model
- implementation
- worked examples
- synthesis
- evidence
- output artifact

### Done Means

Opening any major note feels like opening a private textbook page:

- clear
- concrete
- linked
- testable
- source-grounded
- connected to projects

## Workstream 4 - Retrieval And Answering

### Why

Jarvis must answer questions from the vault, not behave like generic ChatGPT.

### Answer Rule

No source, no confidence.

Every serious answer needs:

- cited notes
- confidence label
- missing knowledge section
- suggested next action

### Done Means

Ask:

> Teach me observability for AI systems using my BOOM notes.

Jarvis retrieves:

- Observability and Tracing
- API Work
- BOOM notes
- outputs/interview stories
- AI evaluation parallels

Then it explains with your project context.

## Workstream 5 - Evaluation

### Why

If Jarvis cannot be tested, it will slowly become vibes.

### Benchmark Types

Definition:

- What is MCP?
- What is dynamic programming?

Comparison:

- MCP vs function calling
- logs vs traces
- greedy vs DP

Project:

- What did I build in BOOM?
- What evidence do I have for systems skills?

Learning:

- What should I learn before GraphRAG?
- Quiz me on OCaml pattern matching.

Research:

- What AI/ML direction fits my current notes?
- What project could connect agents and observability?

### Done Means

Weekly benchmark produces:

- pass/fail
- weak retrieval cases
- weak answer cases
- missing note recommendations
- enrichment actions

## Workstream 6 - Research Engine

### Why

You do not yet know exactly which AI/ML direction to deep dive into. Jarvis should help you discover it.

### Research Engine Jobs

- map a field
- compare paths
- find prerequisites
- inspect what the vault already knows
- find gaps
- propose experiments
- turn experiments into project briefs
- connect projects to career proof

### Done Means

Jarvis can help decide:

- Should I study RAG, agents, evals, or multimodal AI next?
- What do I already know that gives me an advantage?
- What project should I build to prove it?
- What notes need enrichment first?

## Dashboards To Build

### Required Dashboards

- Jarvis Project Dashboard
- Conversation Memory Dashboard
- Knowledge Enrichment Dashboard
- Semantic Index Health Dashboard
- Research Brief Dashboard
- Benchmark Dashboard
- Source Ingestion Dashboard
- Context Pack Dashboard
- AI Tool Integration Dashboard

### Dashboard Philosophy

Dashboards should answer:

- What is active?
- What is missing?
- What is due?
- What changed?
- What should I do next?

They should not become decorative pages.

## CLI Commands To Eventually Support

```powershell
jarvis status
jarvis health
jarvis index
jarvis search "query"
jarvis semantic-search "query"
jarvis ask "question"
jarvis teach "topic"
jarvis quiz "topic"
jarvis research "topic"
jarvis enrich-candidates
jarvis note-profile "path"
jarvis enrich-plan "path"
jarvis enrich-note "path" --mode standard
jarvis conversation-import "file"
jarvis conversations --undistilled
jarvis context-pack --mode project --project Jarvis
jarvis benchmark run
jarvis validate-answer "question"
jarvis graph-neighborhood "topic"
```

## File And Folder Targets

### System Tooling

```text
30_Order/System/jarvis-cli/
30_Order/System/jarvis-memory/
30_Order/System/jarvis-index/
30_Order/System/jarvis-prompts/
```

### Conversation Memory

```text
60_Claude/05_Clippings/AI Conversations/
60_Claude/30_Source_Summaries/AI Conversations/
60_Claude/60_Indexes/AI Conversation Dashboard.md
```

### Research Engine

```text
60_Claude/40_Project_Briefs/Research Briefs/
60_Claude/60_Indexes/Research Engine Dashboard.md
```

### Evaluation

```text
60_Claude/50_Reviews/Benchmarks/
60_Claude/60_Indexes/Jarvis Benchmark Dashboard.md
```

### Context Packs

```text
60_Claude/45_Outputs/Context Packs/
30_Order/System/jarvis-context/
```

## Risks And Guardrails

### Risk: Transcript Graveyard

Mitigation:

- raw transcripts stay raw
- summaries are short
- promotion gate required
- dashboards show undistilled conversations

### Risk: AI Slop

Mitigation:

- HUMAN_WRITING gate
- mechanism over vibes
- concrete examples
- no generic summaries
- source anchors required

### Risk: Overbuilding Before Retrieval Works

Mitigation:

- first pass uses CLI + SQLite
- no heavy UI until `ask` works
- no graph database until graph schema proves useful

### Risk: Every Tool Has Different Memory

Mitigation:

- AI_CONTEXT stays canonical
- context packs are generated from Jarvis
- tool-specific files only point back to shared context

### Risk: Hallucinated Confidence

Mitigation:

- answer confidence labels
- citation check
- validation benchmark
- "Jarvis does not know yet" section

## Monthly Milestones

## End Of Month 1

Jarvis has:

- project hub
- conversation capture folders
- registry schema
- context pack builder
- note index
- note profile command
- enrichment factory V1
- 25 enriched notes
- first benchmark set

The system is not fully intelligent yet, but it has memory plumbing.

## End Of Month 2

Jarvis has:

- semantic search
- graph index
- Ask Jarvis V1
- Tutor Mode V1
- Drill Mode V1
- 60 enriched notes total
- 75 benchmark questions
- context packs usable by multiple AIs

The system can answer and teach from the vault.

## End Of Month 3

Jarvis has:

- conversation memory
- semantic + graph retrieval
- research brief generator
- validation layer
- mature dashboards
- 100+ enriched notes
- 50+ conversation summaries
- answer benchmark above 80%
- source ingestion pipeline
- daily/weekly operating cadence

The system becomes a private research engine.

## The Weekly Operating Rhythm

Every week:

1. import important AI conversations
2. distill 3-5 conversations
3. enrich 10 notes
4. run benchmark
5. process 5 sources
6. create 1 synthesis or research brief
7. update Jarvis project note
8. review next build action

This rhythm matters more than any single feature.

## The Actual Build Order

If there is confusion, build in this order:

1. conversation capture folders and schema
2. `jarvis status`
3. `jarvis context-pack`
4. registry SQLite
5. chunk index
6. semantic search
7. graph index
8. `jarvis ask`
9. answer benchmark
10. enrichment factory
11. conversation distillation
12. research brief generator
13. validation layer
14. dashboards polish

## Definition Of "Insane Jarvis"

Jarvis is working when this becomes normal:

1. I start a new AI/ML project.
2. I ask Jarvis what I already know.
3. Jarvis retrieves relevant notes, conversations, sources, projects, and gaps.
4. I give a generated context pack to Codex, Claude, Kiro, or Cursor.
5. The AI starts with my real context.
6. During the project, conversations flow back into Jarvis.
7. Jarvis distills what changed.
8. Weak concepts become enriched notes.
9. New evidence gets linked.
10. Future AIs inherit the whole trail.

That is the compounding loop.

Jarvis should make every future AI session smarter than the last one.

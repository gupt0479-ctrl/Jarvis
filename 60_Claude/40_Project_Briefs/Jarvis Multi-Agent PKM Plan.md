---
type: project
status: sprout
created: 2026-04-24
updated: 2026-04-24
tags:
  - project
  - jarvis
  - ai
  - pkm
notes:
  - "[[00_Dashboard]]"
  - "[[AI_CONTEXT]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/CS/AI/AI Workflow]]"
  - "[[40_Resources/CS/AI/MCPs]]"
  - "[[40_Resources/Capability/Capability Engine Guide]]"
  - "[[60_Claude/40_Project_Briefs/40_Project_Briefs Board]]"
next: Build Phase 1 conversation registry, context pack builder, and promotion manifest.
---

# Jarvis Multi-Agent PKM Plan

## What this needs to become

Jarvis should not be "every AI tool writes everywhere." That turns the vault into a transcript graveyard.

The better model is:

1. collect raw traces without trusting them
2. distill them into source-grounded notes
3. promote only durable pieces into canonical notes
4. keep one shared context layer so tools stop drifting

The vault already has the start of this:

- `AI_CONTEXT.md` as the cross-tool manifest
- `00_Dashboard.md` and `60_Claude/10_Session_Logs/log.md` as the continuity layer
- `60_Claude/05_Clippings/` -> `30_Source_Summaries/` -> durable notes as the cleanest existing ingestion pattern
- the Capability Engine work as the place where knowledge becomes drills, outputs, and evidence

So the job is not to invent a new system. It is to tighten the loop and add the missing machinery around conversations, context packs, and promotion.

## Core architecture

```text
AI tools and agents
  -> vendor adapters / export hooks
  -> normalized conversation registry
  -> raw archive in 05_Clippings
  -> distillation pass into 30_Source_Summaries
  -> promotion gate into canonical notes / project briefs / outputs
  -> dashboard + session log + AI_CONTEXT refresh

Shared context layer
  -> AI_CONTEXT
  -> 00_Dashboard
  -> session log
  -> active project notes
  -> semantic retrieval over approved notes
  -> tool-specific wrappers (AGENTS.md, CLAUDE.md, Cursor rules, Kiro steering)
```

## 1. Centralized conversation and history logging

### Design rule

Store three things, not one:

- raw transcript
- normalized machine record
- human-usable summary

If Jarvis stores only transcripts, retrieval gets noisy. If it stores only summaries, provenance disappears.

### Storage layout

- Raw exports and captured chats: `60_Claude/05_Clippings/AI Conversations/`
- Distilled conversation notes: `60_Claude/30_Source_Summaries/AI Conversations/`
- Session continuity: `60_Claude/10_Session_Logs/log.md`
- Machine registry: `30_Order/System/ai-conversation-registry/` or another non-hidden tooling folder inside the vault

I would avoid a hidden folder for the main registry because Obsidian Sync excludes hidden folders other than `.obsidian`.

### Normalized schema

Use one schema for every adapter, even if each tool exports differently.

```json
{
  "conversation_id": "vendor-thread-id",
  "source_app": "claude|codex|cursor|chatgpt|kiro|ollama|lovable|aws|tinyfish",
  "workspace": "jarvis",
  "project": "optional project name",
  "title": "human title",
  "started_at": "2026-04-24T10:12:00-05:00",
  "ended_at": "2026-04-24T10:44:00-05:00",
  "participants": ["user", "assistant"],
  "tags": ["urop", "pkm", "agents"],
  "related_notes": ["[[AI_CONTEXT]]", "[[MCPs]]"],
  "raw_path": "60_Claude/05_Clippings/AI Conversations/...",
  "summary_path": "60_Claude/30_Source_Summaries/AI Conversations/...",
  "decision_count": 3,
  "action_count": 2,
  "checksum": "sha256..."
}
```

### Adapter strategy

Build adapters in this order:

1. file-based exports first
2. local tool logs second
3. API-backed ingestion only where export is weak

That keeps the system cheap and debuggable.

Priority order:

1. Claude Code / Codex / Cursor / Kiro local session artifacts
2. ChatGPT and Claude exported conversations
3. Ollama local chat logs
4. tool-specific API pulls only when the export path is bad

### Distillation rule

Every imported conversation should produce the same short summary shape:

- what was decided
- what changed
- what still looks fuzzy
- what belongs in the vault
- what should stay archived only

### Example ingestion flow

```text
export chat -> drop file in inbox folder
  -> watcher runs normalize_chat.py
  -> append record to registry.sqlite + conversations.jsonl
  -> create raw note in 05_Clippings/AI Conversations
  -> run distill_conversation.py
  -> create summary note in 30_Source_Summaries/AI Conversations
  -> append one-line continuity entry to session log
```

## 2. Context awareness and persistent cross-agent memory

### The context stack

Jarvis needs three memory layers.

### Layer A: shared live context

This already exists and should stay small:

- `AI_CONTEXT.md`
- `00_Dashboard.md`
- `60_Claude/10_Session_Logs/log.md`
- active project board or project note

This layer answers: what is happening right now?

### Layer B: tool-specific durable memory

Each tool has its own persistence mechanism. Use the native one instead of pretending one giant prompt will solve it.

- Claude Code: `CLAUDE.md` and imported memory files
- Cursor: `AGENTS.md` plus scoped `.cursor/rules/*.mdc`
- Kiro: steering files
- ChatGPT / Claude web: project instructions and project knowledge
- local pipelines: versioned prompt files in the vault

### Layer C: retrieval memory

This is where the vault starts acting like a real second brain instead of a pile of markdown:

- semantic index over approved notes
- keyword search over titles, frontmatter, and note bodies
- conversation registry filters by app, project, date, and tag

Only index approved sources:

- `40_Resources/`
- `20_Progress/`
- `60_Claude/20_Distilled_Notes/`
- `60_Claude/30_Source_Summaries/`
- selected session summaries

Do not index raw clippings as equal peers to canonical notes.

### Context pack builder

Instead of handing every agent the whole vault, build a bounded pack per task.

```python
def build_context_pack(task, project=None):
    live = read([
        "AI_CONTEXT.md",
        "00_Dashboard.md",
        "60_Claude/10_Session_Logs/log.md",
    ])

    project_notes = lookup_active_project_notes(project, task)
    semantic_hits = search_index(task, k=8)
    recent_threads = search_conversation_registry(task, k=5)

    return {
        "live_context": live,
        "project_notes": project_notes,
        "retrieved_notes": semantic_hits,
        "recent_threads": recent_threads,
    }
```

### Practical rule

Agents should read:

- live context every time
- project context when relevant
- retrieved context on demand

They should not reload half the vault by default.

## 3. Integrating multiple model and tool chains

### Tool roles

Use lanes, not brand loyalty.

| Lane | Default role | Good tools |
|---|---|---|
| Capture and extraction | structured parsing, metadata extraction, cheap summarization | Ollama, local scripts |
| Repo and vault operations | file-aware edits, scripts, refactors | Codex, Claude Code, Cursor, Kiro |
| Long synthesis | planning, comparison, architectural tradeoffs | Claude, ChatGPT |
| Retrieval | semantic + keyword search over approved notes | local embeddings, OpenAI file search if remote is acceptable |
| Review | writing smell detection, evidence checks, gap finding | second-pass model, local rules, lint scripts |

### Recommended operating model

- Local first for ingestion, indexing, and private context
- Cloud models for hard synthesis and major planning passes
- Repo-aware agents for implementation
- One shared promotion gate before anything becomes durable

### Current external findings that matter

Checked on 2026-04-24:

- MCP currently defines `stdio` and Streamable HTTP transports, and the spec says clients should support `stdio` whenever possible. That makes local `stdio` MCP servers the right default for Jarvis.
- Cursor's docs are explicit that models do not retain memory between completions, so rules and `AGENTS.md` are the persistence layer, not optional extras.
- Claude Projects are self-contained workspaces with chat history and project knowledge. Claude Code also has a memory hierarchy across project and user files.
- OpenAI file search gives you a hosted semantic + keyword retrieval layer over uploaded files and vector stores.
- Ollama now supports local embeddings and structured outputs, which is enough to build a cheap local retrieval and extraction pipeline.

### Practical stack

Cheap baseline:

- extraction and normalization: Python scripts + Ollama structured outputs
- embeddings: Ollama `embeddinggemma` or another local embedding model
- local registry: SQLite + JSONL
- note retrieval: ripgrep + semantic search
- heavy synthesis: Claude / ChatGPT only for the hard parts

Escalation path:

- OpenAI file search for selected project corpora when cloud retrieval is worth the tradeoff
- remote MCP servers only when local `stdio` is too limiting

## 4. Human-like writing enforcement

### Core rule

Do not ask one model for final prose and trust it.

Use a three-stage writing gate:

1. extract claims
2. rewrite for mechanism and contrast
3. run a slop check before saving

### Writing pipeline

```text
source material
  -> extractor returns claims / evidence / open questions
  -> drafter writes compressed note
  -> critic checks against HUMAN_WRITING.md
  -> human does final pass on anything durable or public
```

### What the critic should flag

- vague praise words
- repeated framing
- no real example
- claims with no source anchor
- paragraph could fit any generic blog post

### What to add to the current standard

The existing `HUMAN_WRITING.md` is already strong. I would add two small operational rules:

1. every durable note needs at least one concrete example from this vault or a named project
2. any note generated from AI conversation must mark which claims are copied from source, inferred, or still unverified

That keeps confidence honest.

## 5. Sync between Jarvis and the source-of-truth vault

### Core decision

Do not full-sync two active vaults and hope merge conflicts stay polite.

Use two modes:

- promotion mode for notes that have become durable
- limited bidirectional sync only for low-risk folders

### Recommended split

Jarvis:

- working vault
- raw conversations
- distillation notes
- AI-heavy project briefs
- experimental prompts, scripts, adapters

Source-of-truth vault:

- curated evergreen notes
- approved project notes
- reviewed outputs
- final references you actually want to live with

### Sync policy by note class

| Content class | Sync mode | Why |
|---|---|---|
| raw conversation exports | one-way into Jarvis only | high volume, low signal |
| source summaries | one-way Jarvis -> source vault only if reviewed | still semi-raw |
| evergreen notes | promotion only | canonical note should have one home |
| attachments / shared assets | optional bidirectional | lower semantic conflict |
| `.obsidian` configs | keep separate | different vault roles |

### Promotion manifest

Instead of syncing everything by folder, track approved promotions explicitly.

```yaml
- id: jarvis-mcp-note
  source: "60_Claude/20_Distilled_Notes/MCP Patterns.md"
  destination: "../SourceVault/40_Resources/CS/AI/MCP Patterns.md"
  mode: promote
  status: approved
  last_hash: "sha256..."
```

### Safe sync tooling

If you need bidirectional sync for selected folders, use tools that have real safety rails.

Best local-first option:

- `rclone bisync` on a narrow allowlist, with `--dry-run`, `--check-access`, `--max-delete`, and backup dirs on both sides

Fallback:

- Syncthing with staggered file versioning enabled

Do not use bidirectional sync for the full live note tree until the promotion boundary is stable.

### Why this recommendation is stricter than the usual advice

Obsidian's own docs warn against mixing sync services on the same vault, and hidden folders do not sync except `.obsidian`. So the least fragile setup is:

- keep each vault's own sync method simple
- keep the cross-vault relationship explicit and file-level
- make promotions reversible

## 6. Overall system optimization

### What "smart student" means in practice

Jarvis should keep proving four habits:

1. it remembers what is active
2. it turns sources into claims, not fluff
3. it links new work back to old work
4. it surfaces the next useful question

### Metrics worth tracking

- conversations ingested this week
- summaries promoted this week
- orphan summaries with no promotion decision
- projects with no `next`
- durable notes touched by more than one project
- notes failing the writing gate
- repeated unanswered questions across sessions

### Weekly cadence

1. ingest new conversations and exports
2. distill only the threads that changed decisions or produced reusable knowledge
3. run the writing critic on new durable notes
4. review the promotion queue
5. append a short system note to the session log

## Implementation roadmap

## Phase 1: Build the capture spine

Deliverables:

- normalized conversation schema
- `registry.sqlite` + append-only `conversations.jsonl`
- raw conversation intake folder
- first 3 adapters
- conversation distillation template

Success test:

- one Claude thread, one Codex thread, and one ChatGPT export all land in the same registry and produce the same summary shape

## Phase 2: Build the context engine

Deliverables:

- context pack builder
- approved-note semantic index
- project note resolver
- conversation search by topic, project, and date

Success test:

- a new agent can answer "what am I doing on X?" from live vault state without rereading the whole vault

## Phase 3: Build the promotion boundary

Deliverables:

- promotion manifest
- promotion script with hash checks
- reviewed / approved / rejected states
- source-vault destination map

Success test:

- one distilled note becomes a promoted canonical note without duplicate creation or silent overwrite

## Phase 4: Add writing and quality gates

Deliverables:

- writing critic prompt or script
- provenance markers for inferred vs sourced claims
- dashboard for notes awaiting human review

Success test:

- a durable note fails the gate if it has no example, no source anchor, or generic prose

## Phase 5: Tighten the loop

Deliverables:

- weekly review note for the system itself
- registry health checks
- stale thread cleanup
- top repeated question dashboard

Success test:

- Jarvis starts surfacing missing links and repeated confusion without you asking first

## Immediate next build

If I were starting tomorrow, I would build this in order:

1. conversation registry schema and storage
2. adapter for Claude Code / Codex local sessions
3. adapter for exported ChatGPT conversations
4. conversation distiller into `30_Source_Summaries`
5. context pack builder over `AI_CONTEXT`, dashboard, session log, and active project notes
6. promotion manifest and one-way promotion script

That gets the spine in place before touching more ambitious automation.

## External source anchors

Checked on 2026-04-24:

- MCP transports and server features: https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
- Cursor rules and `AGENTS.md`: https://docs.cursor.com/context/rules-for-ai
- Claude Projects: https://support.anthropic.com/en/articles/9517075-what-are-projects
- Claude Code memory: https://docs.anthropic.com/en/docs/claude-code/memory
- OpenAI file search / retrieval: https://platform.openai.com/docs/guides/tools-file-search
- OpenAI retrieval guide: https://platform.openai.com/docs/guides/retrieval
- Ollama embeddings: https://docs.ollama.com/capabilities/embeddings
- Ollama structured outputs: https://docs.ollama.com/capabilities/structured-outputs
- Obsidian sync notes: https://obsidian.md/help/sync-notes
- Obsidian sync settings: https://obsidian.md/help/sync/settings
- rclone bisync: https://rclone.org/commands/rclone_bisync/
- Syncthing versioning: https://docs.syncthing.net/users/versioning?version=v2.0.0

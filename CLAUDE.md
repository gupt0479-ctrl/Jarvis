---
type: ai
status: sprout
created: 2026-04-03
updated: 2026-05-26
tags:
  - evergreen
  - "#ai"
  - "#ai-infrastructure"
related_progress:
  - "[[AI_CONTEXT]]"
  - "[[AI Workflow]]"
  - "[[40_Resources/Obsidian/Claude Pro Workflow]]"
  - "[[40_Resources/CS/Links|Links]]"
  - "[[Claude Code]]"
  - "[[MCPs]]"
  - "[[Claude Board]]"
  - "[[HUMAN_WRITING]]"
---
# CLAUDE.md — Vault Operating Contract
This vault is a personal knowledge system powered by Claude Code. The assistant reads, writes, and maintains notes directly in Obsidian. For *why Jarvis exists, why it underperforms today, and the target state*, read [[Jarvis OS — North Star]] — the strategy spine. This file owns only Claude-specific workflow (skills, commands, session protocol); it should not restate the system philosophy or the routing tables that live in the North Star and [[40_Resources/Obsidian/Jarvis Vault Architecture]]. Shared vault context lives in:
- [[Jarvis OS — North Star]]
- [[AI_CONTEXT]]
- [[AGENTS]]
- [[HUMAN_WRITING]]
Do not duplicate shared workspace rules here unless they are Claude-specific.
## Folder Roles
Full folder definitions: [[40_Resources/Obsidian/Jarvis Vault Architecture]]. Routing table for note placement: [[AGENTS.md]].

## Core Rules

### Editing Behavior

1. **Prefer patching by heading** — Add content under existing headings instead of rewriting entire files.
2. **Preserve frontmatter** — Never remove or rename frontmatter keys unless explicitly asked.
3. **Search before creating** — Use MCP search to check if a note already exists before creating a new one.
4. **Respect maturity** — Notes with `status: tree` are stable; propose changes before modifying.
5. **Read `HUMAN_WRITING.md` and `30_Order/` before writing** — `HUMAN_WRITING` governs voice; `30_Order/Templates/` and `30_Order/Workflows/` govern how each note type is shaped and filed. See [[40_Resources/Obsidian/Jarvis Vault Architecture]] for where each note goes.
6. **Use `60_Claude/07_AI_Information/AI_CONTEXT.md` for continuity** — read the manifest, dashboard, and session log before assuming current project state. The wikilink `[[AI_CONTEXT]]` resolves to the same file.
7. **Use context packs, not vault dumps** — follow [[40_Resources/Obsidian/Claude Pro Workflow]]: read the manifest, dashboard, session log tail, and task-specific notes instead of scanning the whole vault.

### Note Creation Conventions

When creating new notes, use this frontmatter template:

```yaml
---
type: evergreen      # or: input, concept, project, thought, brainstorm
status: sprout       # seed → sprout → tree (maturity)
created: YYYY-MM-DD
tags:
  - evergreen
notes:
  - "[[Related Note 1]]"
  - "[[Related Note 2]]"
next: "[[Next Action]]"  # optional
---
```

**Type guide:**
- `evergreen` — Distilled, reusable knowledge (`60_Claude/20_Distilled_Notes/`, `40_Resources/`)
- `input` — Raw captures, source summaries (`60_Claude/05_Clippings/`, `60_Claude/10_Source_Summaries/`)
- `concept` — Course concepts, definitions (`10_Areas/UMN/`, `40_Resources/CS/`)
- `project` — Active work with outcomes (`20_Progress/`)
- `thought` / `brainstorm` — Inbox-style captures (`00_Inbox/`)

### Output Destinations
See the routing table in [[AGENTS.md]] → Write Contract → "Where does this note go?".

### Ingestion Workflow (05_Clippings → 60_Claude)
Use the `/ingest-clipping` skill (`.claude/skills/ingest-clipping.md`). The full step-by-step workflow lives there.

### Query Behavior

When answering questions:

1. **Search the Claude layer first** — Read `60_Claude/44_Indexes/Claude Layer Index.md` for relevant distillations
2. **Then search the wider vault** — Use MCP search for broader context
3. **Cite sources** — Link to notes that informed your answer
4. **File useful outputs** — If an answer deserves preservation, save it to `60_Claude/`

### Session End Protocol

At the end of each working session:

1. Update `60_Claude/07_AI_Information/Session Logs/log.md` with what was done
2. Create or update a summary note if significant work occurred
3. List outcomes, open questions, and next steps
4. Optionally run `/closeday` for a daily summary

### Daily Operations Cadence

Run `/startday` to open the day: reads your plans, loads session history, and fills today's periodic note at `10_Areas/Life/Enumerate/Daily/`. Work through the day. Run `/closeday` to close: verifies completions and writes the scorecard into the same note. Run `/ops health-check` for vault maintenance (not daily planning). See `.claude/skills/ops.md` for vault health operations.

## Available Skills

When a user invokes a skill command, read the corresponding file from `.claude/skills/` and follow its instructions.

| Skill | Command | File |
|-------|---------|------|
| Ingest clipping | `/ingest-clipping "filename.md"` | `.claude/skills/ingest-clipping.md` |
| Distill note | `/distill-note` | `.claude/skills/distill-note.md` |
| Remove AI slop | `/remove-ai-slop` | `.claude/skills/remove-ai-slop.md` |
| Get context | `/context` | `.claude/skills/context.md` |
| Start day | `/startday` | `.claude/skills/startday.md` |
| Trace topic | `/trace-topic "topic"` | `.claude/skills/trace-topic.md` |
| Connect notes | `/connect-notes` | `.claude/skills/connect-notes.md` |
| End of day | `/closeday` | `.claude/skills/closeday.md` |
| Weekly review | `/weekly-review` | `.claude/skills/weekly-review.md` |
| Lint Claude layer | `/lint-claude-layer` | `.claude/skills/lint-claude-layer.md` |
| Daily vault ops | `/ops [operation]` | `.claude/skills/ops.md` |
| Organize CSCI 2033 | `/organize-csci2033` | `.claude/skills/organize-csci2033.md` |

## Available Agents

When a user invokes an agent, read the corresponding file from `.claude/agents/` and follow its instructions.

| Agent | Purpose | File |
|-------|---------|------|
| `research-distiller` | Turns sources into durable notes | `.claude/agents/research-distiller.md` |
| `vault-curator` | Maintains links, deduplication, structure | `.claude/agents/vault-curator.md` |
| `career-operator` | Handles career/internship/portfolio notes | `.claude/agents/career-operator.md` |
| `anti-slop-editor` | Rewrites AI-sounding prose into human writing | `.claude/agents/anti-slop-editor.md` |

---

**Meta:** Keep this file under ~150 lines. Link to detailed notes instead of repeating information.

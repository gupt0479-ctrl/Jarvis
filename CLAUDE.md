---
type: evergreen
status: sprout
created: 2026-04-03
updated: 2026-05-26
tags:
  - evergreen
notes:
  - "[[AI_CONTEXT]]"
  - "[[AI Workflow]]"
  - "[[40_Resources/Obsidian/Claude Pro Workflow]]"
  - "[[40_Resources/CS/Links|Links]]"
  - "[[Claude Code]]"
  - "[[MCPs]]"
  - "[[60_Claude/60_Claude Board]]"
  - "[[HUMAN_WRITING]]"
---
# CLAUDE.md — Vault Operating Contract
This vault is a personal knowledge system powered by Claude Code. The assistant reads, writes, and maintains notes directly in Obsidian. Shared vault context lives in:
- [[AI_CONTEXT]]
- [[AGENTS]]
- [[HUMAN_WRITING]]
Do not duplicate shared workspace rules here unless they are Claude-specific.
## Folder Roles

| Folder                    | Purpose                                        | Claude Behavior                                             |
| ------------------------- | ---------------------------------------------- | ----------------------------------------------------------- |
| `60_Claude/05_Clippings/` | Raw source material (articles, clips, imports) | Read-only input; never modify                               |
| `60_Claude/`              | Claude-generated knowledge layer               | Full write access; create distillations, summaries, reviews |
| `20_Progress/`            | Active projects, career, mentorship            | Read for context; update with user permission               |
| `30_Order/`               | Templates and system structure                 | Read for conventions; don't modify                          |
| `40_Resources/`           | Reference knowledge, concepts, links           | Read for context; add backlinks when relevant               |
| `00_Inbox/`               | User's quick capture                           | Read for context; don't modify unless asked                 |
| `50_Archive/`             | Past courses, completed work                   | Read-only; historical reference                             |
| `.claude/`                | Skills, agents, settings                       | Full write access for tooling                               |

## Core Rules

### Editing Behavior

1. **Prefer patching by heading** — Add content under existing headings instead of rewriting entire files.
2. **Preserve frontmatter** — Never remove or rename frontmatter keys unless explicitly asked.
3. **Search before creating** — Use MCP search to check if a note already exists before creating a new one.
4. **Respect maturity** — Notes with `status: tree` are stable; propose changes before modifying.
5. **Read `HUMAN_WRITING.md` before drafting prose** — remove filler, avoid generic AI tone, prefer mechanism, contrast, and concrete examples from the vault.
6. **Use `AI_CONTEXT.md` for continuity** — read the dashboard and session log before assuming current project state.
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
- `input` — Raw captures, source summaries (`60_Claude/05_Clippings/`, `60_Claude/30_Source_Summaries/`)
- `concept` — Course concepts, definitions (`30_Order/Notes/`, `40_Resources/CS/`)
- `project` — Active work with outcomes (`20_Progress/`)
- `thought` / `brainstorm` — Inbox-style captures (`00_Inbox/`)

### Output Destinations

| Output Type | Destination |
|-------------|-------------|
| Session summaries | `60_Claude/10_Session_Logs/log.md` |
| Source distillations | `60_Claude/30_Source_Summaries/` |
| Evergreen knowledge | `60_Claude/20_Distilled_Notes/` |
| Project briefs | `60_Claude/40_Project_Briefs/` |
| Daily/weekly reviews | `60_Claude/50_Reviews/` |
| Indexes | `60_Claude/60_Indexes/` |

### Ingestion Workflow (05_Clippings → 60_Claude)

1. User adds source to `60_Claude/05_Clippings/`
2. Run `/ingest-clipping "filename.md"` or ask Claude to process it
3. Claude:
   - Reads the source
   - Extracts key claims, entities, concepts, quotes, actions
   - Creates summary in `60_Claude/30_Source_Summaries/`
   - Updates/creates entity pages where relevant
   - Adds backlinks to related notes
   - Appends to `60_Claude/10_Session_Logs/log.md`
4. User reviews in Obsidian, files or adjusts as needed

### Query Behavior

When answering questions:

1. **Search the Claude layer first** — Read `60_Claude/60_Indexes/Claude Layer Index.md` for relevant distillations
2. **Then search the wider vault** — Use MCP search for broader context
3. **Cite sources** — Link to notes that informed your answer
4. **File useful outputs** — If an answer deserves preservation, save it to `60_Claude/`

### Session End Protocol

At the end of each working session:

1. Update `60_Claude/10_Session_Logs/log.md` with what was done
2. Create or update a summary note if significant work occurred
3. List outcomes, open questions, and next steps
4. Optionally run `/closeday` for a daily summary

### Daily Operations Cadence

Run `/ops morning-start` to open the day: gathers context, builds a plan, runs a health check, and surfaces the top triage items and overdue drills. Work through the day normally. Run `/ops evening-close` to wrap up: creates the closeday summary, runs a capability audit, and logs the health delta. See `.claude/skills/ops.md` for all operations and cost profiles.

## Available Skills

When a user invokes a skill command, read the corresponding file from `.claude/skills/` and follow its instructions.

| Skill | Command | File |
|-------|---------|------|
| Ingest clipping | `/ingest-clipping "filename.md"` | `.claude/skills/ingest-clipping.md` |
| Distill note | `/distill-note` | `.claude/skills/distill-note.md` |
| Remove AI slop | `/remove-ai-slop` | `.claude/skills/remove-ai-slop.md` |
| Get context | `/context` | `.claude/skills/context.md` |
| Today plan | `/today` | `.claude/skills/today.md` |
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

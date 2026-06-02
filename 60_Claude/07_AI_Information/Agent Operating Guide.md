---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - ai-agents
notes:
  - "[[AI_CONTEXT]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[Jarvis Writing and Formatting]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[40_Resources/Obsidian/Plugins/00 Plugin Reference Index]]"
---
# Agent Operating Guide

This is the runbook for AI agents working inside Jarvis.

Jarvis is not just a folder tree. It is an Obsidian knowledge system with live dashboards, metadata, backlinks, review loops, source layers, and agent-generated synthesis. Work with that system.

Operational agent rules live in `60_Claude/07_AI_Information`; stable plugin research and deeper workflow references live in [[40_Resources/Obsidian/Plugins/00 Plugin Reference Index]].

## Start Of Session Checklist

Before creating, rewriting, or organizing notes, read:

- `60_Claude/07_AI_Information/Vault Map.md` (read-me-first orientation)
- `60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md` (governing specification — read before writing anything)
- `AGENTS.md` (root rules + Write Contract)
- `40_Resources/Obsidian/Jarvis Vault Architecture.md` (where every note goes)
- `30_Order/` (Templates + Workflows — read before writing)
- `AI_CONTEXT.md`
- `00_Dashboard.md`
- `HUMAN_WRITING.md`
- `40_Resources/Obsidian/Vault Operating System.md`
- `60_Claude/07_AI_Information/Session Logs/log.md`

Then identify the task type:

- **Capture:** fast inbox or source collection.
- **Distillation:** turning raw material into source-grounded summary.
- **Evergreen synthesis:** reusable concept or mechanism note.
- **Project work:** active execution, plans, boards, next actions.
- **Review:** daily, weekly, monthly, or capability reflection.
- **System documentation:** agent guides, vault docs, templates, dashboards.

Search before creating a note. Prefer extending a canonical note over making a duplicate.

## Where Content Goes

Use the folder system already in place.

| Content type | Destination |
|---|---|
| Raw or imported material | `60_Claude/05_Clippings/` |
| AI outputs awaiting review | `60_Claude/00_Inbox/` |
| Source-grounded summaries | `60_Claude/10_Source_Summaries/` |
| Durable AI-generated knowledge | `60_Claude/20_Distilled_Notes/` |
| Reusable output artifacts | `60_Claude/35_Outputs/` |
| Synthesized project briefs | `60_Claude/40_Project_Briefs/` |
| Daily, weekly, monthly reviews | `60_Claude/50_Reviews/` |
| Dashboards and indexes | `60_Claude/44_Indexes/` |
| Agent/plugin operating docs + session logs | `60_Claude/07_AI_Information/` |
| Active projects and career work | `20_Progress/` |
| Active coursework | `10_Areas/UMN/` |
| Stable reference knowledge | `40_Resources/` |
| Templates, workflows, and structure | `30_Order/` |
| Historical material | `50_Archive/` |

Do not modify `60_Claude/05_Clippings/` unless the user explicitly asks.

Treat `50_Archive/` as historical reference unless the task is archival cleanup.

## Workflow Chooser

Use the smallest workflow that fits the job.

### Use Dataview When

- A list should stay current.
- A dashboard needs to query metadata.
- You are surfacing active projects, missing next actions, orphan notes, stale notes, or review queues.
- The information already exists in frontmatter or task lines.

Do not use Dataview for a one-off explanation.

### Use Tasks When

- There is a concrete action.
- The action should appear in task queries.
- The action has a due date, scheduled date, priority, recurrence, or completion state.

Write action tasks, not vague intentions.

### Use Kanban When

- The work has lanes or stages.
- The user needs to move cards through a workflow.
- Habit tracking, project triage, or execution status is the natural shape.

Use notes for knowledge. Use boards for flow.

### Use Excalidraw When

- The concept is easier as a map, graph, feedback loop, or system diagram.
- Spatial grouping clarifies relationships.
- A visual mechanism would reduce rereading time.

Always keep searchable text near visual work.

### Use Spaced Repetition When

- The concept is already understood.
- The card tests one idea.
- The card helps with course, interview, systems, or capability memory.

Do not make flashcards from raw source before distillation.

### Use Templater When

- Creating notes in folders with configured templates.
- You need consistent frontmatter.
- The note belongs to an established note class.

If writing outside Obsidian, manually follow the same template fields.

### Use Copilot, Local REST API, Or Git Only When

- The user explicitly asks for that tool or workflow.
- The action is necessary and safe.
- Sensitive values will not be exposed.

These are automation surfaces, not default note-writing tools.

## Note Creation Procedure

1. Search for an existing canonical note.
2. Choose the correct destination folder.
3. Use the matching template/frontmatter pattern.
4. Write the note according to [[HUMAN_WRITING]] and [[Jarvis Writing and Formatting]].
5. Add wikilinks to source notes, related concepts, projects, and dashboards.
6. Add `next:` only when a concrete next step exists.
7. If the note creates tasks, use Tasks-compatible syntax.
8. If the note should be tracked by dashboards, verify metadata fields.

Do not create a new structure when a current one already solves the problem.

## Editing Existing Notes

Preserve:

- frontmatter
- source links
- user wording that carries meaning
- backlinks
- task metadata
- heading anchors
- Dataview query logic

Prefer adding under an existing heading or adding a dated addendum when the note is mature.

For `status: tree` notes, be conservative. Propose large restructures before doing them.

If rewriting prose, follow the [[HUMAN_WRITING]] rewrite procedure:

- remove generic framing
- collapse repetition
- replace vague praise with mechanism
- add a concrete example if the note floats
- keep uncertainty explicit
- leave the note denser than before

## Source Handling

Keep the source layers separate:

- Raw capture stays raw.
- Source summaries preserve claims and source anchors.
- Durable notes synthesize concepts without pretending the source said more than it did.

If a source is incomplete, weak, or inferred, say so.

Do not make notes sound complete when the underlying understanding is partial.

## Plugin Safety

Do not edit Obsidian settings unless explicitly asked:

- `.obsidian/plugins/*/data.json`
- `.obsidian/community-plugins.json`
- `.obsidian/app.json`
- `.obsidian/appearance.json`
- `.obsidian/hotkeys.json`
- `.obsidian/workspace.json`
- `.obsidian/workspaces.json`
- CSS snippets

Do not copy API keys, tokens, licenses, plugin auth material, or Local REST API secrets into notes.

When documenting plugin settings, describe behavior and safe operational rules. Do not expose sensitive values.

## End Of Session

After meaningful vault changes, append a concise entry to:

`60_Claude/07_AI_Information/Session Logs/log.md`

Include:

- what was created or changed
- why it matters
- open questions
- next action if one exists

If the work changes current focus, update the relevant dashboard or board. Do not update dashboards just to create activity.

## Stop Conditions

Pause and ask the user before:

- restructuring stable system docs
- modifying `.obsidian` settings
- changing template schemas
- editing raw clippings
- deleting or moving notes
- modifying `50_Archive/` outside archival cleanup
- exposing or using plugin secrets
- converting task formats

When in doubt, preserve the existing system and add a small, well-linked note.

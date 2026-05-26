---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - tasks
  - kanban
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/7_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Tasks Kanban and Project Tracking

Tasks is the atomic action layer. Kanban is the lane layer. Project notes are the context and decision layer.

Use all three deliberately:

- Tasks answer: what action exists?
- Kanban answers: what stage is this item in?
- Project notes answer: why does this work matter, what has been decided, and what is the current `next:` move?

## Current Tasks Settings

- Task format: `tasksPluginEmoji`.
- Done date: set automatically.
- Cancelled date: set automatically.
- Auto-suggest in editor: enabled.
- Global query: empty.
- Global filter: empty.

Configured statuses:

| Markdown | Name | Type | Toggle target |
|---|---|---|---|
| `[ ]` | Todo | TODO | `[x]` |
| `[x]` | Done | DONE | `[ ]` |
| `[/]` | In Progress | IN_PROGRESS | `[x]` |
| `[-]` | Cancelled | CANCELLED | `[ ]` |

Existing status report:

- [[40_Resources/Obsidian/Data View's/Tasks Plugin - Review and check your Statuses 2025-12-20 18-37-12]]

## Tasks Emoji Syntax

Use Tasks emoji metadata when the task itself needs dates, priority, recurrence, or audit trail.

Examples:

```markdown
- [ ] Draft the BOOM queue failure diagram 📅 2026-05-20
- [ ] Review CSCI 2041 closure notes ⏳ 2026-05-17
- [ ] Start internship application batch 🛫 2026-05-18 📅 2026-05-24
- [ ] Drill graph traversal mistakes 🔁 every week 📅 2026-05-22
- [ ] Fix project dashboard query 🔺 📅 2026-05-16
```

Use these meanings:

| Marker | Meaning |
|---|---|
| `📅` | Due date. |
| `⏳` | Scheduled date. |
| `🛫` | Start date. |
| `🔁` | Recurrence. |
| `🔺`, `⏫`, `🔼`, `🔽`, `⏬` | Priority levels, from highest-ish to lowest-ish. |
| `✅` | Done date, normally set by the plugin. |
| `❌` | Cancelled date, normally set by the plugin. |
| `➕` | Created date if manually needed. |

Needs verification: exact preferred priority scale for coursework vs projects.

## Writing Good Tasks

Good:

```markdown
- [ ] Verify whether Excalibrain is intentionally absent before documenting it as removed
- [/] Expand Dataview dashboard examples from `00_Dashboard`
- [-] Replace this manual checklist because the dashboard query covers it
```

Weak:

```markdown
- [ ] Learn plugins
- [ ] Improve Jarvis
- [ ] Do research
```

Those are intentions. A task should name a visible next action.

## `next:` vs Task Line

Use `next:` when the note itself has one current next move.

```yaml
next: "Choose QuickAdd capture choices for inbox and source clipping"
```

Use task lines when multiple actions need tracking:

```markdown
- [ ] Draft capture menu choices
- [ ] Decide whether source clipping creates raw or summary notes
- [ ] Test QuickAdd choice in a disposable note
```

Do not keep a different next action in prose, frontmatter, and a Kanban card. Pick one canonical current move and let dashboards surface it.

## Task Query Blocks

Use Tasks query blocks when task semantics matter:

````markdown
```tasks
not done
path includes 20_Progress
sort by due
sort by priority
short mode
```
````

Coursework due soon:

````markdown
```tasks
not done
path includes 10_UMN
due before in 14 days
sort by due
short mode
```
````

In-progress work:

````markdown
```tasks
status.name includes In Progress
sort by due
short mode
```
````

Use Dataview task queries when a dashboard is mostly about page metadata and only needs a simple open-task list.

## Kanban Boundaries

Current Kanban settings:

- Checkboxes shown.
- Card counts hidden.
- Full-list lane width disabled.
- Dates link to daily notes.

Use Kanban when lane movement is the point:

- habit boards
- source ingestion
- project pipelines
- study workflow boards
- review queues where drag-and-drop helps humans decide stage

Do not use Kanban as a second task database. If a card contains a real action, either make it a Tasks-compatible checkbox or link to the project note where tasks live.

## Recommended Lane Templates

Habit board:

```markdown
## Seed
## Active
## Stabilizing
## Review
## Paused
```

Project pipeline:

```markdown
## Ideas
## Next
## Doing
## Waiting
## Done
```

Source ingestion:

```markdown
## Captured
## Summarize
## Distill
## Link
## Archived
```

Study workflow:

```markdown
## To Learn
## Practicing
## Review
## Exam Ready
## Revisit
```

Needs verification: preferred canonical lane names for future project boards.

## Agent Rule

When adding work to Jarvis:

1. Put durable context in the note.
2. Put one current move in `next:` if the note is active.
3. Put trackable actions as Tasks-compatible task lines.
4. Use Kanban only if stage movement is useful.
5. Avoid duplicate task systems.

## Sources

- [Tasks User Guide - Task formats](https://publish.obsidian.md/tasks/Reference/Task+Formats/About+Task+Formats)
- [Tasks User Guide](https://publish.obsidian.md/tasks/)
- [Kanban README](https://github.com/obsidian-community/obsidian-kanban)
- [Kanban Publish docs](https://publish.obsidian.md/kanban/)
- [[40_Resources/Obsidian/Data View's/Tasks Plugin - Review and check your Statuses 2025-12-20 18-37-12]]

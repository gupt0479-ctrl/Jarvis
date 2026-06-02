---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - workflow
notes:
  - "[[00_Workflows Index]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
---
# Brief to Progress

Turn a synthesized plan into a live project note that the dashboard can track. This is how an idea becomes tracked, accountable work.

**Use when:** a project brief is ready to become active execution.

**Moves:** `60_Claude/40_Project_Briefs/` → `20_Progress/` (under the matching project folder)

**Template:** `30_Order/Templates/Classes/Project Template.md` (adapt for non-course projects)

## Steps

1. Write the brief in `40_Project_Briefs/` first if it does not exist — scope, approach, the architecture or plan, risks. The brief is the thinking; the progress note is the doing.
2. Create the project note in `20_Progress/` under the right home (`Projects/`, `Internship/`, `Mentorship Program/`, `UROP/`, etc.). Read `30_Order/Standards/Project Standard.md` before writing.
3. State the outcome in one line, then the current state, then the immediate next action.
4. Set a `next:` — this is non-negotiable. A project note without `next:` is invisible to the "projects missing a next action" dashboard.
5. Link back to the brief, and to the distilled concepts and resources the project depends on.
6. As work proceeds, update the note and its `next:`; when it ends, archive it to `50_Archive/`.

## Frontmatter to set

```yaml
type: project
status: active        # active | paused | complete | archived
deadline: YYYY-MM-DD  # if one exists
next: "<the immediate next action>"
track: <ai|systems|algorithms|career|trading>
```

## Done when

- The project note exists in `20_Progress/` with a live `next:`.
- It links to its brief and its supporting concepts.
- The dashboard shows it as active with a next action.
- The session log records it.

A simple test for whether `20_Progress` is doing its job: can you name something you are actively working on that has no note here? If yes, that thread is invisible to the system — give it one.

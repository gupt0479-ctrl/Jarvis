---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - dataview
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/07_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Dataview and Dashboards

Use Dataview when the list should be rebuilt from frontmatter, tags, links, or task lines instead of maintained by hand. In Jarvis, that means project queues, stale notes, metadata cleanup, flashcard queues, source-summary indexes, and enrichment dashboards.

## Current Settings

- Inline Dataview: enabled.
- Inline DataviewJS: enabled.
- DataviewJS blocks: enabled.
- HTML rendering: enabled.
- Refresh: enabled every `2500ms`.
- Empty-result warnings: enabled.
- Result counts: shown.
- Task completion tracking: disabled.

Because DataviewJS and HTML rendering are enabled, agents should prefer plain Dataview and treat scripts as code, not decoration.

## Why This Is Central

[[00_Dashboard]] already uses Dataview for:

- knowledge enrichment candidates
- active projects
- projects missing `next`
- AI staging queue
- raw clippings to distill
- active classes
- recent Claude outputs
- open tasks
- flashcard review queue
- orphan durable notes
- metadata cleanup
- recent reviews

The same pattern should hold in [[60_Claude/60_Indexes]]. A dashboard is trustworthy only when the fields it reads are consistent.

## Canonical Fields To Query

From [[40_Resources/Obsidian/Vault Operating System]]:

| Field | Query use |
|---|---|
| `type` | Separates project, concept, input, review, dashboard, index, output. |
| `status` | Separates active, paused, complete, archived, seed, sprout, tree. |
| `created` / `updated` | Finds stale or newly created notes. |
| `next` | Shows current action at note level. |
| `deadline` | Sorts active projects and coursework. |
| `reviewed` | Finds review candidates. |
| `enrichment_status` / `enrichment_level` | Drives enrichment queues. |
| `source_status` / `source_url` | Separates vault-grounded and externally sourced notes. |
| `track` / `tracks` | Routes capability notes into field dashboards. |
| `mastery_level`, `next_drill`, `last_drilled` | Supports capability and review loops. |

If a query returns nonsense, check metadata before editing the query.

## Query Recipes

Active projects:

```dataview
TABLE status, deadline, next, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived"
SORT deadline ASC, file.mtime DESC
LIMIT 12
```

Projects missing a current move:

```dataview
TABLE status, deadline, file.mtime AS "Updated"
FROM "20_Progress"
WHERE type = "project" AND status != "archived" AND !next
SORT file.mtime DESC
LIMIT 10
```

Stale durable notes:

```dataview
TABLE status, updated, reviewed, file.mtime AS "Modified"
FROM "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE type AND status != "archived"
AND file.mtime < date(today) - dur(60 days)
SORT file.mtime ASC
LIMIT 20
```

Raw clippings waiting for distillation:

```dataview
TABLE file.ctime AS "Captured"
FROM "60_Claude/05_Clippings"
SORT file.ctime DESC
LIMIT 12
```

Source summaries needing links or synthesis:

```dataview
TABLE source_status, source_url, notes, file.mtime AS "Updated"
FROM "60_Claude/30_Source_Summaries"
WHERE type = "input"
SORT file.mtime DESC
LIMIT 20
```

Flashcard queue:

```dataview
LIST
FROM #cards
WHERE !contains(file.folder, "30_Order/Templates")
SORT file.mtime DESC
LIMIT 10
```

Enrichment candidates:

```dataview
TABLE type, status, track, enrichment_status, file.mtime AS "Updated"
FROM "10_UMN" OR "20_Progress" OR "40_Resources" OR "60_Claude/20_Distilled_Notes"
WHERE (type = "concept" OR type = "evergreen" OR type = "project")
AND (!enrichment_status OR enrichment_status != "enriched")
SORT file.mtime ASC
LIMIT 10
```

Course boards:

```dataview
TABLE WITHOUT ID file.link AS "Board", length(file.inlinks) AS "Linked Notes"
FROM "10_UMN"
WHERE contains(file.name, "Board")
SORT file.name ASC
```

Recent reviews:

```dataview
TABLE file.folder AS "Folder", file.ctime AS "Created"
FROM "60_Claude/50_Reviews"
WHERE file.name != "50_Reviews Board"
SORT file.ctime DESC
LIMIT 8
```

## Dataview vs Tasks

Use Dataview when the question is about notes:

- Which projects are active?
- Which concepts lack enrichment metadata?
- Which source summaries are recent?
- Which notes are orphaned?

Use Tasks when the question is about actions:

- What is due?
- What is scheduled?
- Which task is in progress?
- Which task has high priority?

Dataview can render `TASK` queries, but Tasks understands Tasks-specific emoji metadata and recurrence semantics better. Do not build a second task system with ad hoc inline fields unless there is a clear reason.

## DataviewJS Rule

Use DataviewJS only when plain Dataview cannot express the transformation.

Good reasons:

- complex grouping that Dataview cannot express readably
- computed summaries over multiple fields
- small generated tables with clear code comments

Bad reasons:

- decorative charts
- hidden business logic
- queries that only one agent can maintain
- HTML-heavy output that breaks plain Markdown readability

When DataviewJS is used, add a one-sentence explanation above the block.

## Failure Modes

- Inconsistent frontmatter: a note with `Type` or `type:` missing will vanish from queries.
- Missing `next:`: active projects look idle even if prose contains next steps.
- Stale manual lists: a hand-written index can disagree with a dashboard.
- Folder drift: moving a note can remove it from a path-based query.
- HTML/JS risk: enabled HTML and DataviewJS can make dashboards execute more than a reader expects.
- Over-broad `FROM`: vault-wide queries can become slow. Restrict by folder when possible.

## Agent Workflow

Before changing a dashboard:

1. Read the existing query and the fields it depends on.
2. Check several matching notes to verify the field is real.
3. Prefer tightening metadata over adding complicated query workarounds.
4. Keep examples in this doc and live dashboards aligned.
5. Link the dashboard to this note if the pattern becomes canonical.

## Integration Map
- **Templater/QuickAdd → Dataview:** Dataview only sees fields that were written at note creation. Templater folder templates and (once configured) QuickAdd choices are what guarantee `type:`/`status:`/`track:` exist. A note created outside Obsidian without that frontmatter is invisible to every query here. See [[Templates Capture and Periodic Notes]] and [[QuickAdd Capture Menu]].
- **Dataview vs Tasks:** Dataview answers questions about *notes* (which projects are active, which concepts lack enrichment); Tasks answers questions about *actions* (what is due, what is in progress). Dataview can render `TASK` blocks, but Tasks understands emoji dates and recurrence — do not build a second action system in inline fields. See [[Tasks Kanban and Project Tracking]].
- **SR → Dataview:** the flashcard-queue recipe reads the `#cards` tag; capability dashboards read `last_drilled`/`next_drill`/`mastery_level`. Cards or capability notes with missing fields drop out of the queue. See [[Spaced Repetition and Learning Loops]].
## Gold-Standard Example
[[00_Dashboard]] is the canonical live example: it drives enrichment candidates, active projects, projects missing `next`, the AI staging queue, clippings-to-distill, the flashcard queue, orphan notes, and metadata cleanup entirely from frontmatter. It is the proof that the field schema is worth keeping consistent — every block there breaks the moment a note's metadata drifts.
## Verified Open State
- Several recipes above query `60_Claude/30_Source_Summaries`, but the live path is `60_Claude/10_Source_Summaries`. Are these recipes stale, and should they be repointed? — *known path drift; repair is tracked in the audit roadmap, out of scope for the current pass*
- Is `source_status` actually populated on enough notes to query, or is it aspirational? — *the field is documented but inconsistently set*
- Should DataviewJS/HTML stay enabled given the execution risk, or be restricted? — *risk noted; no change without user decision*
## Sources

- [Dataview docs](https://blacksmithgu.github.io/obsidian-dataview/)
- [Dataview query structure](https://blacksmithgu.github.io/obsidian-dataview/queries/structure/)
- [Dataview metadata docs](https://blacksmithgu.github.io/obsidian-dataview/annotation/metadata-pages/)
- [[00_Dashboard]]
- [[40_Resources/Obsidian/Vault Operating System]]

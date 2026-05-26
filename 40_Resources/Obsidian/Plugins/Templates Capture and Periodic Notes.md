---
type: evergreen
status: sprout
created: 2026-05-15
updated: 2026-05-15
tags:
  - evergreen
  - system
  - obsidian
  - templates
notes:
  - "[[AI_CONTEXT]]"
  - "[[HUMAN_WRITING]]"
  - "[[40_Resources/Obsidian/Vault Operating System]]"
  - "[[60_Claude/7_AI_Information/Plugins]]"
  - "[[00 Plugin Reference Index]]"
---
# Templates Capture and Periodic Notes

Templater is the active template engine. Periodic Notes owns daily, weekly, and monthly reviews. QuickAdd is installed, but it is not yet doing the capture work it could do.

Core Templates is disabled. Do not document or depend on the core Templates plugin as the active system.

## Current Templater State

- Templates folder: `30_Order/Templates`.
- Trigger on file creation: enabled.
- Folder templates: enabled.
- System commands: disabled.
- File templates: disabled.
- User scripts folder: empty.

Folder template map:

| Folder | Template | Implication for agents |
|---|---|---|
| `10_UMN` | `30_Order/Templates/Classes/Week Template.md` | Coursework notes need class/week structure when created through Obsidian. |
| `20_Progress` | `30_Order/Templates/Metadata/For Progress.md` | Active project notes should support `next:` and progress metadata. |
| `40_Resources` | `30_Order/Templates/Metadata/For Evergreen.md` | Stable references should have evergreen-style metadata. |
| `60_Claude/20_Distilled_Notes` | `30_Order/Templates/Metadata/For Evergreen.md` | AI-synthesized durable knowledge follows evergreen rules. |
| `60_Claude/30_Source_Summaries` | `30_Order/Templates/Metadata/For Inputs.md` | Source summaries are input notes, not finished evergreen notes. |
| `60_Claude/40_Project_Briefs` | `30_Order/Templates/Metadata/For Progress.md` | Project briefs behave like active progress artifacts. |

Needs verification: whether `60_Claude/7_AI_Information` should get its own folder template.

## Manual Template Matching

When an agent writes files through the filesystem, Obsidian may not run Templater. The agent must manually match the template intent:

- `40_Resources/Obsidian/Plugins` -> evergreen/system frontmatter.
- `60_Claude/30_Source_Summaries` -> input/source frontmatter with source grounding.
- `20_Progress` -> project/progress frontmatter with `next:` when a concrete action exists.
- `60_Claude/50_Reviews` -> review frontmatter and review date.

Do not leave a note without frontmatter because the file was created outside Obsidian.

## QuickAdd State

Observed state:

- Plugin installed and lazy-loaded.
- Hotkey `Alt+Q` runs QuickAdd.
- `choices` count is `0`.
- Online features are disabled.
- Selection-as-capture-value is enabled.
- AI provider configuration exists, but secrets must not be exposed.

QuickAdd is one of the highest-value unused plugins because it can turn folder rules into a fast menu.

Proposed choices after approval:

| Choice | Destination | Template behavior |
|---|---|---|
| Inbox capture | `60_Claude/00_Inbox` | Quick thought with minimal metadata and a review prompt. |
| Source clipping | `60_Claude/05_Clippings` | Raw source container; do not rewrite content. |
| Project note | `20_Progress/Projects` or active project folder | Progress template and `next:` prompt. |
| Concept note | `40_Resources` or `60_Claude/20_Distilled_Notes` | Evergreen/concept metadata and related notes. |
| Daily review | `60_Claude/50_Reviews/Daily` | Periodic Notes template. |
| Flashcard candidate | current note or inbox | Adds a review prompt, not a finished card bank. |

Do not configure these choices during documentation work.

## Periodic Notes Review Flow

Configured reviews:

| Review | Format | Folder | Template |
|---|---|---|---|
| Daily | `YYYY-MM-DD` | `60_Claude/50_Reviews/Daily` | `30_Order/Templates/Headway Templates/Better Today.md` |
| Weekly | `YYYY-[W]ww` | `60_Claude/50_Reviews/Weekly` | `30_Order/Templates/Headway Templates/Better Week.md` |
| Monthly | `YYYY-MM` | `60_Claude/50_Reviews/Monthly` | `30_Order/Templates/Headway Templates/Better Month.md` |
| Yearly | disabled | none | none |

Review notes should pull from [[00_Dashboard]], recent session log entries, open tasks, and active projects. Do not create daily notes in a second folder.

## Capture Destination Rules

Use [[60_Claude/7_AI_Information/Agent Operating Guide]] as the full folder map. The short rule:

- Raw or imported material -> `60_Claude/05_Clippings`.
- AI output awaiting review -> `60_Claude/00_Inbox`.
- Source-grounded summary -> `60_Claude/30_Source_Summaries`.
- Durable synthesis -> `60_Claude/20_Distilled_Notes` or `40_Resources`.
- Active execution -> `20_Progress`.
- Reviews -> `60_Claude/50_Reviews`.

The failure mode is mixing raw capture and durable synthesis in the same note. That makes source claims hard to audit later.

## Note Composer Boundaries

Use Note Composer only when the split or merge boundary is obvious:

- A source summary has become a reusable concept note.
- A long project note contains a separable decision record.
- A course note has a standalone concept worth linking elsewhere.

Do not split stable notes just because they are long. Add a precise heading or dated addendum first.

## Agent Workflow

When creating a note:

1. Search for an existing canonical note.
2. Decide whether the material is raw, source-grounded, durable, active, or review.
3. Use the folder and metadata that match that role.
4. Add links to projects, courses, concepts, or dashboards that should rediscover it.
5. Add `next:` only when there is a concrete next step.

The template gets the note into the right shape. [[HUMAN_WRITING]] decides whether the prose is worth keeping.

## Sources

- [Templater docs](https://silentvoid13.github.io/Templater/)
- [QuickAdd docs](https://quickadd.obsidian.guide/docs/)
- [QuickAdd Capture choice](https://quickadd.obsidian.guide/docs/Choices/CaptureChoice)
- [QuickAdd Macro choice](https://quickadd.obsidian.guide/docs/Choices/MacroChoice/)
- [Periodic Notes README](https://github.com/liamcain/obsidian-periodic-notes)
- [[40_Resources/Obsidian/Vault Operating System]]
- [[60_Claude/7_AI_Information/Agent Operating Guide]]

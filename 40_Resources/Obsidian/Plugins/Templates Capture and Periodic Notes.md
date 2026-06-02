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
  - "[[60_Claude/07_AI_Information/Plugins]]"
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

## QuickAdd
QuickAdd has its own deep reference now: [[QuickAdd Capture Menu]]. Short version: installed, lazy-loaded, `Alt+Q` bound, but `choices` is empty, so the capture menu does nothing. It is the highest-value unused plugin because it turns the routing table into a one-keystroke menu. Proposed choices and the full integration with Templater live in that doc. Do not configure choices during documentation work — it edits `data.json`.

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

Use [[Agent Operating Guide]] as the full folder map. The short rule:

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

## Integration Map
- **Templater → frontmatter schema:** the folder template fires on note creation inside Obsidian and stamps canonical fields. This is the mechanism that keeps [[Dataview and Dashboards]] queries reliable — a note created outside Obsidian skips Templater, so the agent must apply the same fields by hand.
- **Templater ↔ QuickAdd:** a QuickAdd Template choice points at a `30_Order/Templates/` file; QuickAdd places the note and Templater fills it. They must agree on the destination folder. See [[QuickAdd Capture Menu]].
- **Periodic Notes → reviews:** Periodic Notes creates dated review notes from the Headway templates into `60_Claude/50_Reviews/`. The review pulls from [[00_Dashboard]], the session log tail, and open tasks — it is a read-of-state, not a new data source.
- **Templater bug surface:** `60_Claude/30_Source_Summaries` appears in the folder-template map, but the live source-summary path is `60_Claude/10_Source_Summaries`. A template bound to the dead path never fires.
## Gold-Standard Example
- *Templater output:* [[10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 9|Week - 9]] is what the `Week Template` folder template should produce — class frontmatter, the right section skeleton, ready for content.
- *Periodic Notes output:* [[60_Claude/50_Reviews/Weekly Synthesis/Weekly Synthesis — 2026-W22|Weekly Synthesis — 2026-W22]] is a real review note in the configured folder.
## Verified Open State
- The folder map lists `60_Claude/30_Source_Summaries`; the live path is `10_Source_Summaries`. Which folders actually have a Templater template bound, and should the map be repointed? — *path drift; confirm in Templater settings*
- Should `60_Claude/07_AI_Information` get its own folder template? — *unresolved; raised in the gaps register*
- Several `Metadata/For *` templates are frontmatter-only shells (`For Evergreen`, `For Progress`) — they need bodies before they teach anything. — *addressed in the template-enrichment work, tracked separately*
## Sources

- [Templater docs](https://silentvoid13.github.io/Templater/)
- [QuickAdd docs](https://quickadd.obsidian.guide/docs/)
- [QuickAdd Capture choice](https://quickadd.obsidian.guide/docs/Choices/CaptureChoice)
- [QuickAdd Macro choice](https://quickadd.obsidian.guide/docs/Choices/MacroChoice/)
- [Periodic Notes README](https://github.com/liamcain/obsidian-periodic-notes)
- [[40_Resources/Obsidian/Vault Operating System]]
- [[Agent Operating Guide]]

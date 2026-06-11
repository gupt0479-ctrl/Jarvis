---
type: evergreen
status: tree
created: 2026-04-24
updated: 2026-04-24
tags:
  - evergreen
  - system
  - obsidian
notes:
  - "[[00_Dashboard]]"
  - "[[CLAUDE.md]]"
  - "[[30_Order/Templates/MOC]]"
---
# Vault Operating System
This note is the canonical operating contract for Jarvis as an AI second brain.
## What this vault is for
This note is the **canonical property/field schema** for Jarvis. Read before creating or restructuring notes.

For folder definitions and placement rules → [[40_Resources/Obsidian/Jarvis Vault Architecture]].
For write contract and routing → [[AGENTS.md]].
For formatting rules → [[Jarvis Writing and Formatting]].
For strategy → [[Jarvis OS — North Star]].

## Canonical Properties

| Property              | Type    | Use                                                                                                                                        |
| --------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `type`                | text    | Note class: `input`, `evergreen`, `concept`, `project`, `thought`, `brainstorm`, `class`, `plan`, `review`, `dashboard`, `index`, `output` |
| `status`              | text    | State or maturity: `seed`, `sprout`, `tree`, `active`, `paused`, `complete`, `archived`                                                    |
| `created`             | date    | Creation date                                                                                                                              |
| `updated`             | date    | Last meaningful update                                                                                                                     |
| `tags`                | tags    | Retrieval tags, not folder replacements                                                                                                    |
| `notes`               | list    | Primary related notes                                                                                                                      |
| `next`                | text    | Next concrete action or next note                                                                                                          |
| `area`                | list    | Ongoing life or work area when useful                                                                                                      |
| `related_progress`    | list    | Active project links                                                                                                                       |
| `source_url`          | text    | External source pointer                                                                                                                    |
| `input_kind`          | text    | Input subtype like `book`, `article`, `board`, `ai`                                                                                        |
| `thought_kind`        | text    | Thought subtype like `reflection`, `memory`, `musing`                                                                                      |
| `deadline`            | date    | Project or task deadline                                                                                                                   |
| `reviewed`            | date    | Last review date for system or reference notes                                                                                             |
| `enrichment_status`   | text    | Enrichment state: `candidate`, `in-progress`, `enriched`, `needs-review`                                                                   |
| `enrichment_level`    | text    | Depth of enrichment: `light`, `standard`, `deep`                                                                                           |
| `source_status`       | text    | Claim grounding state: `vault-grounded`, `externally-sourced`, `mixed`, `uncertain`                                                        |
| `cli_used`            | boolean | Whether jarvis-cli was available during the ops scan                                                                                       |
| `scan_dimensions`     | number  | Number of health check dimensions scanned                                                                                                  |
| `critical_count`      | number  | Count of critical-priority triage items in an Ops Report                                                                                   |
| `high_count`          | number  | Count of high-priority triage items in an Ops Report                                                                                       |
| `carry_forward_count` | number  | Count of triage items carried from the previous Ops Report                                                                                 |
## Capability Extension Properties

| Property | Type | Use |
|---|---|---|
| `track` | list | Long-term domain: `ai`, `systems`, `algorithms`, `career`, `trading` |
| `prerequisites` | list | Required concepts that should be understood first |
| `used_in` | list | Projects, boards, briefs, or implementations that apply the concept |
| `evidence` | list | Outputs, demos, interview stories, or other proof artifacts |
| `difficulty` | number | Relative complexity from 1 to 5 |
| `mastery_level` | text | Capability stage: `novice`, `familiar`, `proficient`, `expert` |
| `mastery_score` | number | Optional numeric confidence score, usually 1 to 10 |
| `last_drilled` | date | Last active review date |
| `next_drill` | date | Next scheduled review date |
| `drill_interval` | number | Days between reviews |
| `question_kind` | text | Question type: `open`, `misconception`, `oral-exam`, `debugging`, `build` |
| `question_status` | text | Question state: `open`, `active`, `resolved` |
| `output_kind` | text | Output type for `type: output` notes |
| `source_concepts` | list | Concept notes that feed an output |
| `concepts` | list | Concept links inside a synthesis note |
| `tracks` | list | Tracks bridged by a synthesis note |
## Folder Logic
See [[40_Resources/Obsidian/Jarvis Vault Architecture]].

## Default Workflows
See `30_Order/Workflows/` for per-note-type procedures.

## Note Creation Rules
See [[AGENTS.md]] Write Contract.

## AI Working Agreements
See [[AGENTS.md]] Working Rules.

## Enrichment Rules
See [[40_Resources/Obsidian/Jarvis Enrichment Engine]] for the enrichment workflow.


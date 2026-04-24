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

- Capture fast.
- Distill deliberately.
- Retrieve reliably.
- Keep one durable home for each idea, project, and source trail.

## Canonical Properties

| Property | Type | Use |
|---|---|---|
| `type` | text | Note class: `input`, `evergreen`, `concept`, `project`, `thought`, `brainstorm`, `class`, `plan`, `review`, `dashboard`, `index`, `output` |
| `status` | text | State or maturity: `seed`, `sprout`, `tree`, `active`, `paused`, `complete`, `archived` |
| `created` | date | Creation date |
| `updated` | date | Last meaningful update |
| `tags` | tags | Retrieval tags, not folder replacements |
| `notes` | list | Primary related notes |
| `next` | text | Next concrete action or next note |
| `area` | list | Ongoing life or work area when useful |
| `related_progress` | list | Active project links |
| `source_url` | text | External source pointer |
| `input_kind` | text | Input subtype like `book`, `article`, `board`, `ai` |
| `thought_kind` | text | Thought subtype like `reflection`, `memory`, `musing` |
| `deadline` | date | Project or task deadline |
| `reviewed` | date | Last review date for system or reference notes |
| `enrichment_status` | text | Enrichment state: `candidate`, `in-progress`, `enriched`, `needs-review` |
| `enrichment_level` | text | Depth of enrichment: `light`, `standard`, `deep` |
| `source_status` | text | Claim grounding state: `vault-grounded`, `externally-sourced`, `mixed`, `uncertain` |
| `cli_used` | boolean | Whether jarvis-cli was available during the ops scan |
| `scan_dimensions` | number | Number of health check dimensions scanned |
| `critical_count` | number | Count of critical-priority triage items in an Ops Report |
| `high_count` | number | Count of high-priority triage items in an Ops Report |
| `carry_forward_count` | number | Count of triage items carried from the previous Ops Report |

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

### Capture

- `60_Claude/00_Inbox/`: AI outputs waiting to be reviewed or filed.
- `60_Claude/05_Clippings/`: raw clips, imports, pasted sources, and ingestion inputs.

### Work

- `10_UMN/`: current school work.
- `20_Progress/`: current execution and projects.

School notes in `10_UMN/` are a feeder layer. Avoid broad restructuring there, but selectively enrich flagship concept notes or create distilled mirror notes when they contribute to long-term tracks.

### Structure

- `30_Order/Templates/`: templates only.

### Durable Knowledge

- `40_Resources/`: stable reference material and system docs.
- `60_Claude/20_Distilled_Notes/`: evergreen AI-synthesized knowledge.
- `60_Claude/30_Source_Summaries/`: source-linked summaries.
- `60_Claude/40_Project_Briefs/`: synthesized project docs.

### Review and Retrieval

- `60_Claude/50_Reviews/`: daily, weekly, monthly reviews.
- `60_Claude/60_Indexes/`: dashboards, indexes, and health checks.

## Default Workflows

### 1. Capture

- Fast thought -> `60_Claude/00_Inbox/`
- Web/article/source clip -> `60_Claude/05_Clippings/`
- Active task or execution note -> `20_Progress/`

### 2. Distill

- Raw source -> summarize into `60_Claude/30_Source_Summaries/`
- If the idea is reusable, create or update a canonical note in `40_Resources/` or `60_Claude/20_Distilled_Notes/`
- Add backlinks to the project, class, or concept notes that should surface it later

### 3. Review

- Use `00_Dashboard` for current focus
- Use `60_Claude/60_Indexes/Vault Health Dashboard` to find metadata drift, orphan notes, and stale inbox items
- Use `60_Claude/50_Reviews/` for daily and weekly reflection

## Note Creation Rules

- Search before creating.
- Prefer one canonical note per concept.
- Use wikilinks aggressively when a note should be discoverable from another path.
- Keep templates clean and machine-readable.
- Do not use tags as a substitute for note relationships.
- Do not duplicate large summaries across multiple files.

## AI Working Agreements

- Preserve frontmatter.
- Prefer patching existing notes over full rewrites.
- Keep raw sources raw.
- Keep indexes dynamic where possible with Dataview rather than manually maintained tables.
- Add system docs in `40_Resources/Obsidian/` and operational dashboards in `60_Claude/60_Indexes/`.

## Enrichment Rules

- Preserve existing human-written note content unless the user explicitly asks for rewriting.
- Prefer adding `## Jarvis Enrichment` or `## Addendum - Jarvis Enrichment YYYY-MM-DD` over reorganizing the whole note.
- Enrichment should add mechanism, concrete definitions, examples, contrasts, misconceptions, source anchors, and drills.
- Mark enriched notes with `enrichment_status` and `enrichment_level` so dashboards can track progress.
- Use [[Jarvis Enrichment Engine]] for the detailed enrichment workflow.

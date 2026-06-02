---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - workflow
notes:
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[HUMAN_WRITING]]"
  - "[[60_Claude/07_AI_Information/Agent Operating Guide]]"
---
# Workflows Index

This folder is the procedure half of `30_Order`. `Templates/` gives the note skeletons; these workflows give the steps that move a note from raw capture to durable, connected, testable knowledge. Read the one that matches your task before writing. For where any note goes, see [[40_Resources/Obsidian/Jarvis Vault Architecture]]; for how prose should sound, see [[HUMAN_WRITING]].

These are written for the vault Jarvis is becoming over the next three months: every capture ends as a connected note, every concept carries evidence, every answer can cite its source. A workflow that does not leave the note searchable, linked, and honestly labeled is not finished.

## The pipeline

```
capture        05_Clippings (raw source)   ·   00_Inbox (loose AI output)
   ↓ one source → one summary
summarize      10_Source_Summaries
   ↓ many summaries → one concept
distill        20_Distilled_Notes
   ↓ stable + reused → out of the workshop
promote        10_Areas (identity)  ·  40_Resources (reference)  ·  20_Progress (active work)
   ↓ understanding → deliverable
produce        35_Outputs (with source_concepts provenance)

across all of it:  enrich existing notes in place  ·  capture AI conversations  ·  log every change
```

## Pick a workflow

| Your task | Workflow |
|---|---|
| Turn a raw clip / web page / video into a usable summary | [[Capture to Summary]] |
| Turn one or more summaries into a reusable concept note | [[Summary to Distilled]] |
| Move a mature concept out of the workshop into Areas/Resources | [[Promotion]] |
| Turn a project brief into a live `20_Progress` note | [[Brief to Progress]] |
| Build a reusable deliverable (story, bullet, prompt) with provenance | [[Output with Provenance]] |
| Capture an LLM conversation so its decisions survive | [[Conversation Capture]] |
| Strengthen an existing note without rewriting it | [[Enrichment]] |

## Rules every workflow shares

- **Search first.** Look for an existing canonical note and extend it. Most "new" notes should be edits.
- **Set frontmatter from the schema.** Use the canonical fields in [[40_Resources/Obsidian/Vault Operating System]] and the matching template in `30_Order/Templates/`. Always set `type`, `status`, `created`, `tags`. Add `source_status`, `track`, `enrichment_status`, `next` where the note type calls for it.
- **Maturity is a state, not a guess.** `seed` = rough capture, `sprout` = working draft, `tree` = trusted and stable. Promote maturity only when the note earns it.
- **Link both ways.** A note that nothing links to and that links to nothing is invisible to retrieval and to the future graph. Wikilink its sources, its siblings, and the project or domain it serves.
- **Be honest about support.** Mark claims as source-grounded, inferred, or uncertain. Never make a note sound finished when the understanding is partial.
- **End with a log line.** After a meaningful change, append one entry to `60_Claude/07_AI_Information/Session Logs/log.md`: what changed, why, and the next action if one exists.

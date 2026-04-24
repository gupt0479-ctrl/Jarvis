---
type: evergreen
status: tree
created: 2025-07-18
updated: 2025-07-18
tags:
  - index
  - capability
---

# Output Index

This folder holds output notes — portfolio bullets, interview stories, demo specs, project briefs, blog drafts, and reusable prompts generated from enriched concept notes.

## Output Gate

An output note requires at least one of:

- A source concept with `mastery_level` of `familiar` or higher
- A linked project under `used_in`
- A linked artifact under `evidence`

No gate, no output. This prevents writing stories about things you cannot demonstrate.

Every output must have a non-empty `source_concepts` field linking back to the concept notes it draws from. When an output is created, it gets added to the source concept's `evidence` field — closing the loop.

## Output Kinds

| Kind | When to use |
|---|---|
| `portfolio-bullet` | Concept demonstrated in a project or implementation |
| `interview-story` | Concept has a problem-action-result narrative |
| `demo-spec` | Concept can become a mini build or proof artifact |
| `project-brief` | Knowledge ready to become an execution plan |
| `blog-draft` | Concept is teachable and differentiated |
| `reusable-prompt` | Concept best operationalized as an agent workflow |

## Dashboards

- [[Proof Dashboard]] — outputs by track, concepts with no evidence, in-progress artifacts
- [[Output Pipeline]] — editable base for triaging output status and kind

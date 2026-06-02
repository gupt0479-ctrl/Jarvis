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
# Output with Provenance

Build a reusable deliverable for someone else — a recruiter, an interviewer, a future prompt, a portfolio. This is the one workflow whose consumer is external, which is exactly why it must be traceable.

**Use when:** you need an artifact you will reuse: an interview story, a portfolio/resume bullet, a reusable prompt, a one-pager.

**Moves:** `60_Claude/20_Distilled_Notes/` + `20_Progress/` evidence → `60_Claude/35_Outputs/`

**Template:** `30_Order/Templates/Capability/Output Template.md`

## The line between this and a distilled note

A distilled note teaches *you* (`20_Distilled_Notes`). An output is something you hand to *another person or system* (`35_Outputs`). If you would put it on a resume, send it to a mentor, paste it into a job application, or reuse it as a prompt, it is an output.

## Steps

1. Identify the concepts and project evidence the artifact draws on — the BOOM observability work, a distilled concept, a project note.
2. Write the artifact in `35_Outputs/` using the output template.
3. **Set `source_concepts:`** in the frontmatter, listing the notes it came from. This provenance is what makes the output trustworthy and lets you regenerate or verify it later. An output without provenance is a claim with no backing.
4. Keep it tight and concrete — outputs are judged by an outsider, so no filler, no inflation (see [[HUMAN_WRITING]]).
5. Link it into `35_Outputs/Output Index.md` so it is findable when you need it.

## Frontmatter to set

```yaml
type: output
status: sprout
output_kind: <interview-story|portfolio-bullet|prompt|one-pager>
source_concepts:
  - "[[<concept or project note>]]"
track: <ai|systems|algorithms|career|trading>
```

## Done when

- The artifact is reusable and reads cleanly to an outsider.
- `source_concepts:` traces every claim back to a vault note.
- It is linked from the Output Index.
- The session log records it.

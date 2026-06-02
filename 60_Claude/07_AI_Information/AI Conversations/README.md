---
type: dashboard
status: tree
created: 2026-05-29
updated: 2026-05-29
tags:
  - source-summaries
  - ai-conversations
  - readme
notes:
  - "[[60_Claude/05_Clippings/AI Conversations/README]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
---

# AI Conversations — Distilled Summaries

Distilled, human-useful summaries of LLM conversations. The raw transcripts live in `60_Claude/05_Clippings/AI Conversations/`.

## Rules

- One distilled summary per raw conversation.
- Every summary cites its raw source via `source_note:` frontmatter.
- Summaries are short and decision-focused. They are not transcripts in a different format.

## File Naming

Mirror the raw file name with ` — Summary` appended:

```
YYYY-MM-DD-{source-app}-{slugified-title} — Summary.md
```

## Required Frontmatter

```yaml
---
type: input
input_kind: ai-conversation-summary
status: sprout
created: YYYY-MM-DD
source_app: claude-code | claude-web | codex | cursor | kiro | chatgpt | ollama | other
source_note: "[[60_Claude/05_Clippings/AI Conversations/Original File]]"
project: optional project name
decision_count: N
action_count: N
tags:
  - input
  - ai-conversation-summary
notes:
  - "[[Related Note]]"
---
```

## Summary Shape

Use the distillation template from the Master Plan:

```markdown
# Conversation Summary — [Title]

## What Was Decided
- ...

## What Changed
- ...

## Important Context
- ...

## Source Claims (Quoted From Transcript)
- ...

## Inferred Claims (Distiller Interpretation)
- ...

## Open Questions
- ...

## Follow-Up Actions
- [ ] ...

## Related Notes
- [[...]]

## Should Be Promoted?
- decision: yes/no/partial — and what to promote where
```

## Workflow

1. Raw transcript exists in `60_Claude/05_Clippings/AI Conversations/`.
2. Distill via `/ingest-clipping` or `research-distiller` agent.
3. Summary lands here. Source note links both directions.
4. Append a one-line entry to `60_Claude/10_Session_Logs/log.md`.
5. Promotion to concept notes / project briefs / outputs is a separate manual decision.

## Related

- [[60_Claude/05_Clippings/AI Conversations/README]] — raw archive rules.
- [[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]] — defines the full workstream and the registry schema.
- [[60_Claude/40_Project_Briefs/Vault-Audit-2026-05-29]] — Phase 4 / Month 1 deliverable.

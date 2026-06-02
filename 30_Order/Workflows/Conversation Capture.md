---
type: evergreen
status: tree
created: 2026-05-31
updated: 2026-05-31
tags:
  - system
  - workflow
  - conversation-memory
notes:
  - "[[00_Workflows Index]]"
  - "[[40_Resources/Obsidian/Jarvis Vault Architecture]]"
  - "[[60_Claude/40_Project_Briefs/Jarvis Three-Month Research Engine Master Plan]]"
---
# Conversation Capture

Capture an LLM conversation so its decisions survive after the chat closes. This is the biggest missing layer in Jarvis and the backbone of the three-month plan: you make many decisions with AI tools, and without capture, every new AI starts from zero.

**Use when:** a conversation with any AI (Claude, Codex, Cursor, Kiro, ChatGPT, a local model) produced a decision, a plan, or context worth keeping.

**Moves:** raw transcript → `60_Claude/05_Clippings/AI Conversations/` → summary in `60_Claude/10_Source_Summaries/` (and, once built, the `jarvis-memory` registry under `30_Order/System/`)

## The three layers

Raw conversation is not knowledge yet. Store it in three layers and only promote the durable parts:

1. **Raw archive** — the transcript, untouched, in `05_Clippings/AI Conversations/`.
2. **Summary** — a short distillation in `10_Source_Summaries/`, using the structure below.
3. **Promotion** — only durable decisions become concept notes, project updates, outputs, or `next:` actions. The transcript itself never becomes a durable note.

## Summary structure

```markdown
## What Was Decided
## What Changed
## Important Context
## Source Claims
## Inferred Claims
## Open Questions
## Follow-Up Actions
## Related Notes
## Should Be Promoted?
```

## Steps

1. Save the raw transcript to `05_Clippings/AI Conversations/`. Do not edit it.
2. Write the summary in `10_Source_Summaries/` using the structure above. Keep it short — the value is the decisions, not the back-and-forth.
3. Wikilink the project and concept notes the conversation touched.
4. Promote only what is durable: turn a decision into a project `next:`, a new understanding into a distilled note, an artifact into an output. Leave the rest as summary.
5. Append a one-line session-log entry noting the import and whether anything was promoted.

## Frontmatter to set (on the summary)

```yaml
type: input
status: sprout
source_app: <claude-code|codex|cursor|kiro|chatgpt|claude-web|ollama|other>
source_status: mixed
```

## Done when

- The raw transcript is archived and untouched.
- A short summary captures decisions, changes, and open questions.
- Durable items are promoted; the transcript is not promoted wholesale.
- The session log records the import.

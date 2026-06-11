---
type: project
status: active  # active | paused | complete | archived
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
deadline:
related_progress: []
tags:
  - "#progress"
next:  # the single next move — also stated in ## Next Action
---
# <% tp.file.title %>

## Goal

The concrete outcome you're building toward. One sentence. If you can't state the goal in one sentence, the project isn't ready to start.

*Example:* Ship a working RAG pipeline demo that runs locally against the BOOM queue data by June 20th.

## Current State

Where you are right now — what's done, what's in motion, what's blocked, and why. Update this every time you touch the note.

*Example:* Chunking and indexing complete. Retrieval working on test queries. Stuck on: context window overflow when top-k = 10 and chunks are large. Next: test with k=5 and smaller chunk size.

## Next Action

The single next physical action. Mirror the `next:` frontmatter field exactly. No multi-step plans here — one move.

*Example:* Rerun retrieval test with chunk_size=512, k=5 and compare output quality against baseline.

## Open Questions

Concrete unknowns that are blocking decisions or next actions. Each item should be answerable.

- [ ] 

## Log

Date-stamped one-line entries. What changed or was decided. Past tense.

- **<% tp.date.now("YYYY-MM-DD") %>:** Created note.

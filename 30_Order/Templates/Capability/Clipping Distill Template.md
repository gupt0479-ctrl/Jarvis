---
type: input
status: sprout
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - summary
notes: []
input_kind:  # pdf | web | video | image | conversation
track:  # ai | systems | algorithms | career | trading | general
source_note:  # "[[Filename.pdf]]" — filename + extension, no folder path
source_url:
next:
---
# <% tp.file.title %> — Summary

**Source:**
**Ingested:** <% tp.date.now("YYYY-MM-DD") %>
**Pages:**

## Source

One paragraph describing what this source is: author, medium, context, thesis. Enough that the note is interpretable without opening the original.

## Key Claims

The main claims the source makes. Each claim is a complete sentence, not a label. Bold a short name if useful, then state the actual claim.

- **Claim:** Full sentence stating what the source argues or demonstrates.

*Example:*
- **Retrieval quality gate:** RAG systems fail silently — the model produces confident output even when retrieved context is irrelevant. Retrieval quality must be evaluated independently of generation quality.

## Full Content

Everything in the source, mapped section by section in the source's own order. The goal: after reading this note, the user should never need to open the original again.

==Highlight SR anchor claims.== **Bold key concepts.** *Italic sub-labels.* Use callouts for warnings, tips, or key frameworks the source emphasizes.

## Why It Matters

Connect to something concrete in this vault — a project, a course, a problem you're working on. Generic "this is useful for AI" sentences should be deleted.

## Links Into The Vault

Confirmed-existing wikilinks to notes this source relates to. Grep before adding.

- [[ ]]

## Open Questions

Concrete unknowns the source raises or leaves unresolved.

- [ ] 

## Flashcards

#cards/<% tp.frontmatter.track %>
Mechanism question::Answer that tests understanding, not a label.

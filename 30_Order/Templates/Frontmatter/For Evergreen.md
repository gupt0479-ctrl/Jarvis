---
type: evergreen
status: sprout
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags:
  - evergreen
notes: []
next:
---
# <% tp.file.title %>

*Gold standard: see [[10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 4]] for a mature vault note in this style.*

## Core Claim

==The single most important true statement about this concept. One sentence, in your own words. This becomes an SR cloze.==

*Example:* ==Retrieval-augmented generation only improves reliability if the retriever surfaces documents that are decision-relevant — bad retrieval feeds the model cleaner nonsense.==

## Mechanism

How it actually works. What causes what. Prefer 2–3 sentences that a sharp peer could follow over polished abstraction.

*Example:* At inference time, the user query is embedded and matched against an index of chunked documents. The top-k chunks are prepended to the prompt. The model then conditions its answer on both the query and the retrieved context — so if the retrieval is wrong, the model's confidence just anchors to the wrong evidence.

## Why This Matters Here

Connect to something concrete in this vault — a course, a project, a problem you are actively working on. Generic "this matters because AI is important" sentences should be deleted.

*Example:* Directly relevant to the BOOM queue ingestion pipeline: if Omnisearch returns the wrong chunks, the summarization step will produce confident-sounding but wrong output. This is the failure mode I need to handle with fallback logic.

## Failure Modes

What breaks this concept. What people commonly confuse it with. Use `> [!WARNING]` for the main trap.

> [!WARNING]
> The main failure mode for this concept is…

*Example:*
> [!WARNING]
> Assuming better retrieval = better generation. The relationship is conditional: generation quality is bounded by retrieval quality, not improved by it unconditionally.

## Evidence

Wikilinks to vault notes where this concept is used, demonstrated, or tested. Grep the vault before adding links.

- [[ ]] (to create)

## Related

Wikilinks to concepts this one depends on, extends, or contrasts with.

- [[ ]] (to create)

## Flashcards

#cards/[track]
<% tp.file.title %>::[one-line answer that tests understanding, not a label]

---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[Alerts and Data Flow]]"
  - "[[API and Backend]]"
  - "[[Postman]]"
---
# MongoDB Data Model and Filters

This note explains the storage side of BOOM and why filters are central to its usefulness.

Related notes:

- [[Alerts and Data Flow]]
- [[API and Backend]]
- [[Kafka Redis and Workers]]
- [[Postman]]

## Why This Note Matters

This is the note to study if you want to learn:

- how a document database fits a scientific pipeline
- why storage shape matters
- how filtering turns raw data into usable results

These are directly transferable ideas for data engineering and ML systems work.

## Why BOOM Uses MongoDB

BOOM's data is:

- nested
- heterogeneous
- survey-specific
- evolving across pipeline stages

MongoDB fits that well because:

- document-shaped records are natural for alert data
- schemas can evolve
- nested fields are normal
- aggregation and query patterns are flexible

## Core Data Entities

### Alert

One candidate event or alert instance coming from the survey stream.

### Object

A source-level record that can aggregate information across alerts.

### Image or cutout

Visual slices or image-associated data tied to an alert.

### Filter

User-defined logic for deciding whether an alert is interesting.

### Filter version

A stored version of a filter definition so results are reproducible and changes are trackable.

The BOOM docs broaden this vocabulary with a few more useful entities:

- survey: the upstream observing program
- catalog: an archival or live collection used for context
- cross-match: a positional link between BOOM's object and another catalog object

## Why Stored Shape Is A Design Decision

An important architecture lesson from BOOM:

- Rust structs and MongoDB documents are related, but they are not identical on purpose

Why:

- Rust types are strict and optimized for code correctness
- MongoDB documents are optimized for storage and query patterns
- blindly serializing everything can produce noisy, null-heavy records

This is a real engineering lesson:

- storage design is not the same as in-memory type design

The architecture docs make this concrete:

- Rust structs preserve fields needed for strict in-memory typing
- MongoDB documents are sanitized to avoid noisy null-heavy storage

## Why Filters Matter

Without filtering, the stream is too large and too noisy for most users.

Filters let BOOM move from:

- "something changed in the sky"

to:

- "this changed thing is relevant to a particular scientific or operational goal"

## Why Filtering After Enrichment Is Powerful

BOOM filters can use more than raw fields. They can also use:

- cross-match data
- derived quantities
- classification scores
- richer context produced during enrichment

That makes BOOM significantly more useful than a dumb pass-through broker.

Examples of context available after enrichment include:

- cross-match identities
- derived features
- classifier outputs
- object-history context

## Data Questions To Practice Asking

When reading the code or docs, ask:

- what is the unit being stored here?
- is this alert-level or object-level data?
- what fields are derived versus raw?
- what query patterns does this schema support?
- what breaks if the filter changes version?

These are database-engineering questions, not astronomy-only questions.

## Query And Access Patterns

BOOM's storage layer has to satisfy several consumers:

- internal workers reading and updating records
- the API serving processed results
- filter logic evaluating enriched records

## Command Recipes

### Search MongoDB usage

```bash
cd ~/projects/boom
rg -n "mongodb|Collection<|aggregate\\(|find_one|insert_one|replace_one|update_one" src
```

### Search filter-related types and logic

```bash
rg -n "Filter|FilterVersion|pipeline|match.*filter|evaluate" src
```

### Open likely starting points

```bash
sed -n '1,260p' src/filter/base.rs
sed -n '1,260p' src/api/db.rs
```

### Search for BSON and serialization boundaries

```bash
rg -n "bson|serde|to_document|from_document" src
```

## Screenshot Placeholders

- [ ] one filter definition or filter version example
- [ ] MongoDB-related code showing collections or queries
- [ ] a BOOM API response that returns stored data
- [ ] a diagram showing alert record versus object record

## Engineering Takeaways

- Document databases are strong when domain data is nested and evolving.
- Storage design should follow query needs, not only type definitions.
- Filter versioning is a reproducibility feature, not just bookkeeping.
- This is directly relevant to feature stores, experiment tracking, and data-serving systems in AI/ML.

## Data view
### UROP notes that reference this concept
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

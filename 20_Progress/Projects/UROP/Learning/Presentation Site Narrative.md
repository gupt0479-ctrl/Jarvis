---
type: evergreen
status: sprout
created: 2026-04-23
tags:
  - evergreen
notes:
  - "[[BOOM]]"
  - "[[Symposium]]"
  - "[[Observability and Tracing]]"
---
# Presentation Site Narrative

This note explains the BOOM observability website as a technical narrative. The site is not only a presentation artifact; it is also one of the clearest explanations of the system and of your UROP work.

Related notes:

- [[BOOM]]
- [[Symposium]]
- [[API and Backend]]
- [[Kafka Redis and Workers]]
- [[Observability and Tracing]]

## Why This Note Matters

The website compresses a year of engineering work into a clean order:

- what BOOM is
- how the pipeline works
- what changed with tracing
- what evidence proves it
- what future work it enables

If you understand the site section by section, you understand how to explain the project clearly.

## Page Structure As A Technical Story

The site assembles its sections in this order:

1. Hero
2. Pipeline primer
3. Before vs After tracing
4. Subsystem deep dive
5. Trace anatomy
6. Trace explorer
7. Postman evidence
8. Failure gallery
9. Metrics charts
10. Alert journey
11. Challenge and solution grid
12. Future work
13. Implementation details
14. Ask-me-about prompts

That order is strong engineering communication:

- system first
- implementation second
- evidence third
- future work last

## Hero

The hero section says:

- BOOM is a Rust-based astronomical alert broker
- your work made the system observable, debuggable, and easier to trust

That is the right opening because it leads with system value rather than a PR number.

## Pipeline Primer

The pipeline section matches the BOOM architecture directly:

- surveys
- Kafka topics
- Kafka consumer
- Redis or Valkey
- scheduler
- alert workers
- enrichment workers
- MongoDB
- API

This section matters because tracing only makes sense once the audience understands the pipeline boundaries.

## Before vs After Tracing

This is the main argument:

- before: disconnected logs and unclear subsystem boundaries
- after: nested spans and readable trees

It is the shortest correct explanation of why your UROP mattered.

## Trace Explorer

This is the strongest evidence section. It shows:

- login and token creation flow
- protected route access and validation flow

These traces are useful because they connect real requests to real subsystem boundaries.

## Postman Evidence

This section pairs:

- the request sent from Postman
- the trace shown in the terminal

That is important because it proves the instrumentation against live endpoint behavior.

## Failure Gallery

The failure gallery captures why observability work matters in practice:

- malformed bearer token
- missing Kafka topic
- ONNXRuntime or CUDA issue
- setup or helper-script issue
- route expectation mismatch

The value of the work is that these failures become classifiable.

## Metrics Charts

The charts are used correctly. They visualize:

- runtime coverage
- trace depth
- diagnostic timeline
- error families

They do not invent fake benchmark claims.

## Future Work

The future-work section is careful and correct:

- observability is delivered
- replay-based science and filter tuning come next

That honesty makes the presentation stronger.

## Command Recipes

### Open the page structure

```bash
cd ~/projects/lovable/boom-tracer
sed -n '1,220p' src/pages/Index.tsx
```

### Read the most important sections

```bash
sed -n '1,220p' src/components/Hero.tsx
sed -n '1,260p' src/components/PipelinePrimer.tsx
sed -n '1,320p' src/components/TraceExplorer.tsx
sed -n '1,260p' src/components/FailureGallery.tsx
sed -n '1,260p' src/components/MetricsCharts.tsx
```

## Screenshot Placeholders

- [ ] full homepage hero
- [ ] pipeline primer section
- [ ] trace explorer section
- [ ] Postman evidence section
- [ ] failure gallery section

## Engineering Takeaways

- A good technical website can also be a systems-explanation tool.
- The site is useful because it organizes the work by subsystem boundary and evidence type.
- If you can explain every section of the site, you can explain the project clearly.

## Data view
### UROP notes that reference this concept
```dataview
TABLE type, status, file.folder
FROM "20_Progress/UROP"
WHERE file.path != this.file.path
AND contains(file.outlinks, this.file.link)
SORT file.folder ASC, file.name ASC
```

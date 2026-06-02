---
type: evergreen
status: tree
created: 2025-07-18
updated: 2026-05-28
tags:
  - index
  - capability
  - review
---

# Weekly Synthesis Index

This folder holds weekly synthesis review notes — periodic snapshots of enrichment activity, drill status, open questions, and synthesis opportunities.

## Review Cadence

One note per week. Each review covers:

1. **Concepts enriched this week** — which notes moved from seed to sprout, or sprout to tree
2. **Overdue drills** — concepts where `next_drill` is earlier than today
3. **Unresolved questions** — open questions from Question Banks and the Question Dashboard
4. **Outputs created** — new interview stories, portfolio bullets, demos, or briefs
5. **Synthesis candidates** — 1-3 cross-track connections worth pursuing next week

## How Overdue Drills Are Computed

A concept is overdue when `next_drill < today`. The drill formula:

```
next_drill = last_drilled + clamp(round(drill_interval × mastery_multiplier), 3, 180)
```

Weekly reviews surface these so they don't silently accumulate.

## Template

Use [[Weekly Synthesis Template]] to generate new review notes. The template includes Dataview queries for overdue drills and unresolved questions so the review is partially auto-populated.

## Review History

| Week | Note | Theme |
|------|------|-------|
| 2026-W17 | [[Weekly Synthesis — 2026-W17]] | Capability Engine seed — 24 notes enriched across 5 tracks |
| 2026-W22 | [[Weekly Synthesis — 2026-W22]] | Claude Pro workflow wired in; three-month spine 30% complete, 4 weeks behind |

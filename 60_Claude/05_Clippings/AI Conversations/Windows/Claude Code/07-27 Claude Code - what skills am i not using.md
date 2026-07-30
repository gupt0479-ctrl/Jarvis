---
type: input
input_kind: ai-conversation
source_app: claude-code
title: "what skills am i not using"
started_at: 2026-07-27T15:06:00
ended_at: 2026-07-27T15:21:16
project: Jarvis
status: raw
session_id: 6f63ab3c-7ef1-4f99-8eb5-5b0e381d6300
cwd: 'D:\Users\_Anant\10_Areas\Documents\Jarvis'
tags:
  - input
  - ai-conversation
  - claude-code
---

# what skills am i not using

## You

what skills am i not using?

## Claude

I'll check recent activity to see which skills have actual usage evidence versus which have never been invoked.

Based on git history, session logs, and actual output artifacts in the vault, here's the split:

**Actually used (evidence in outputs, not just skill-file edits):**
- `/ingest-clipping` — dozens of processed PDFs in `PDF Ingestion/Read/`
- `/startday` + `/closeday` — the daily loop, heavily iterated and clearly run daily
- `/ops` (health-check, morning-start, evening-close) — verified checklist entries in the log
- `/excalidraw-diagram` — 2 real `.excalidraw` files exist (`Claude OS Map`, `Internship Research Loop`)
- `/tag-month` — ran once, tag `2026-06` exists

**No evidence of ever being run** (only created/edited, never invoked — or invoked once and abandoned):
- **`/organize-csci2033`** — the giveaway: `20_Progress/Degree/CSCI 2033/` still has `Concepts_old/`, `Concepts_new/`, and stray files like `Untitled.md` and `Midterm Notes(1).md`. That's exactly the messy, unmerged state this skill exists to clean up.
- **`/lint-claude-layer`** — no lint report anywhere in the vault.
- **`/trace-topic`** — only appears in "skills to build" lists and path-fix commits, never as an actual trace output.
- **`/connect-notes`** — same pattern, no orphan/link-fix report exists.
- **`/distill-note`** — one passing mention in a "todo" list, no standalone distillation output attributable to it.
- **`/remove-ai-slop`** — no evidence of a rewrite pass.
- **`/weekly-review`** — heavily *edited* (three separate rewrites logged) but no actual weekly synthesis note exists anywhere in the vault. You've tuned this skill repeatedly without ever running it.
- **`/tag-month`** — only ran once, for June. It's now July 27 and there's no July checkpoint tag yet — this one's overdue, not just unused.
- **`export-ai-session`** (global skill) — the raw `exported-claude-sessions.json` / `exported-cowork-sessions.json` capture files exist, but there's no evidence the distillation pass into `60_Claude/` has run.

The pattern: you've been in **build/tune mode** on the review, cleanup, and synthesis skills (weekly-review, lint, connect-notes, trace-topic, organize-csci2033) without ever closing the loop by actually running them. The daily-operational skills (startday/closeday/ops/ingest-clipping) are the ones getting real mileage.

Want me to actually run `/organize-csci2033` or `/tag-month` (July is overdue) now, or `/lint-claude-layer` as a first health check?

*Tools used: Bash, Glob, Grep*



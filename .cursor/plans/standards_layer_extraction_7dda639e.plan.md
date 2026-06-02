---
name: Standards Layer Extraction
overview: Extract the per-heading guidance currently embedded as HTML comments in template files into a new 30_Order/Standards/ layer (five docs), then strip the comments from six templates and wire the Standards docs into AGENTS.md, the Vault Rules pre-flight, three workflows, and two skills.
todos:
  - id: standards-docs
    content: Create five Standards docs in 30_Order/Standards/ (Source Summary, Course Week, Concept, Evergreen, Project), each deriving per-heading guidance from the confirmed gold-standard real notes, with verified frontmatter wikilinks.
    status: completed
  - id: strip-templates
    content: Strip all HTML comment instructions from the six templates while preserving Templater syntax, frontmatter, headings, and format-reference flashcard.
    status: completed
  - id: agents-table
    content: Add a 'Standards doc to read first' column to the AGENTS.md routing table; fill Source Summary, Evergreen, Project rows; leave others blank.
    status: completed
  - id: vault-rules-step
    content: Patch Vault Rules Part 1 'Analyze the Vault Before Writing' with one step to read the matching Standards doc before writing.
    status: completed
  - id: workflow-refs
    content: Add one Standards-doc reference line to Capture to Summary, Summary to Distilled, and Brief to Progress at their create-the-note steps.
    status: completed
  - id: audit-skills
    content: Compress duplicated content specs in ingest-clipping.md and research-distiller.md and point both to the Source Summary Standard; keep tooling steps.
    status: completed
  - id: log-closeout
    content: Append a session-log entry; run read-only verification grep checks.
    status: completed
isProject: false
---

# Standards Layer Extraction

Move per-heading note-writing guidance out of template files (where it currently lives as `<!-- ... -->` comments) into a dedicated, queryable Standards layer, then clean the templates and reference the Standards docs from the routing/rule/workflow/skill layers.

## Ground truth gathered
Confirmed gold-standard real notes that each Standards doc must describe (derive from these, do not invent):
- Source Summary -> [`Quant Foundations (PDF)`](60_Claude/10_Source_Summaries/PDF Ingestion/Quant Foundations (PDF).md); aligns with Vault Rules Part 9 structure order.
- Course Week -> [`Week - 9`](10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 9.md) and [`Week - 4`](10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Week - 4.md) (the `## Lecture-to-textbook synthesis` pattern).
- Concept -> [`Teams and Team Effectiveness`](10_Areas/UMN/Previous Classes/Minor/MGMT 3001/Concepts/Teams and Team Effectiveness.md).
- Evergreen -> [`Observability in Backend vs Evaluation in AI`](60_Claude/20_Distilled_Notes/Synthesis/Observability in Backend vs Evaluation in AI.md); [`BOOM`](20_Progress/Projects/UROP/BOOM.md) as a mechanism-rich example.
- Project -> [`Jarvis`](20_Progress/Projects/AI Second Brain/Jarvis.md) (active, has `next:`); [`OpsPilot`](20_Progress/Projects/CS/Hackathons/Opspilot.md) (complete retrospective).

## Phase 1 — Create 30_Order/Standards/ (five docs)
**Files (new):**
- [`Source Summary Standard.md`](30_Order/Standards/Source Summary Standard.md)
- [`Course Week Standard.md`](30_Order/Standards/Course Week Standard.md)
- [`Concept Standard.md`](30_Order/Standards/Concept Standard.md)
- [`Evergreen Standard.md`](30_Order/Standards/Evergreen Standard.md)
- [`Project Standard.md`](30_Order/Standards/Project Standard.md)

**Method:** Each is a proper Obsidian note: frontmatter (`type: evergreen`, `status: sprout`, `created/updated: 2026-06-01`, `tags: [system, standards]`, `notes:` wikilinks to its template + workflow + gold-standard note — all verified to exist). Body structure per doc:
- Intro line + `## Maps To` (template wikilink) and `## Used By Workflow` (workflow wikilink).
- `## Per-Heading Standard` — one `###` per template heading. For each: what content belongs (specific), how dense (bullet count / sentence-count guideline), which plugins apply + exact syntax, one concrete example quoted/linked from the gold-standard note, and a `> [!WARNING]` failure mode.
- `## Done Conditions` — what a complete note of this type looks like.
- `## Gold Standard Example` — wikilink to the best real note.

Heading sets to cover (from the cleaned templates):
- Source Summary: `Source / Key Claims / Full Content / Why It Matters / Links Into The Vault / Open Questions / Flashcards`, plus the `**Source:**/**Ingested:**/**Pages:**` header lines and frontmatter (`input_kind`, `track`, `source_note` filename+ext). Must match Vault Rules Part 9 exactly.
- Course Week: `What you must be able to do / Key ideas (short) / Concepts created today / Examples worth keeping / Lecture / Textbook integration / Takeaways / Lecture-to-textbook synthesis / Flashcards` — capture the lecture-to-textbook synthesis pattern (definition anchor highlight, `*Mechanism:*`, lecture example, textbook connection, concept links, WARNING + SUMMARY callouts).
- Concept: `One-Line Answer / Mechanism / Contrast — What It Is Not / Failure Modes / Evidence From This Vault / Flashcards`.
- Evergreen: `Core Claim / Mechanism / Why This Matters Here / Failure Modes / Evidence / Related`.
- Project: `Goal / Current State / Next Action / Open Questions / Log` + the `next:` frontmatter mirror.

**Done when:** Five docs exist, each frontmatter link verified, and an agent reading only the Standards doc + its template could pass all 16 points of Vault Rules Part 12 on the first try.

## Phase 2 — Strip HTML comments from six templates
**Files:** [`Clipping Distill Template.md`](30_Order/Templates/Capability/Clipping Distill Template.md), [`Week Template.md`](30_Order/Templates/Classes/Week Template.md), [`Concept Template.md`](30_Order/Templates/Classes/Concept Template.md), [`For Evergreen.md`](30_Order/Templates/Metadata/For Evergreen.md), [`For Progress.md`](30_Order/Templates/Metadata/For Progress.md), [`Textbook Template.md`](30_Order/Templates/Classes/Textbook Template.md).

**Method:** Remove every `<!-- instruction -->` block. Preserve: all Templater syntax (`<% tp.date.now(...) %>`, `<% tp.file.title %>`), the exact frontmatter the previous session set, heading structure, and the empty list/heading scaffolding. Keep the example flashcard line(s) only where they serve as a pure format reference. The Clipping Distill Template currently has example single-line and multiline flashcards inside comments — keep one short uncommented format-reference card under `#cards/[track]`, drop the commented examples.

**Done when:** Pasting any template into a blank note yields clean frontmatter + empty headings with zero HTML comments, and Templater tokens remain intact.

## Phase 3 — AGENTS.md routing table column
**File:** [`AGENTS.md`](AGENTS.md) — the `### Where does this note go?` table.

**Method:** Add a third column `Standards doc to read first`. Fill only the rows that map: "Summary of one source" -> `[[Source Summary Standard]]`; "Reusable distilled knowledge" -> `[[Evergreen Standard]]`; "Active project..." -> `[[Project Standard]]`. Leave all other cells blank (no invented rows). Course Week and Concept standards are not added here because the table has no rows for them; they are reached via their templates, workflows, and the Vault Rules pre-flight step.

**Done when:** Table has the new column with three populated cells; no other rows altered.

## Phase 4 — Vault Rules pre-flight step
**File:** [`Vault Rules — Complete AI Ruleset.md`](60_Claude/07_AI_Information/Vault Rules — Complete AI Ruleset.md) — patch the `### Analyze the Vault Before Writing` subsection by heading only.

**Method:** Append one step: "For the note type you are creating, check the routing table in `AGENTS.md` for its Standards doc. If one exists in `30_Order/Standards/`, read it before writing a single line of the note." No other part of the file touched.

**Done when:** The new step exists under that heading; rest of file unchanged.

## Phase 5 — Reference line in three workflows
**Files:** [`Capture to Summary.md`](30_Order/Workflows/Capture to Summary.md) -> Source Summary Standard; [`Summary to Distilled.md`](30_Order/Workflows/Summary to Distilled.md) -> Evergreen Standard; [`Brief to Progress.md`](30_Order/Workflows/Brief to Progress.md) -> Project Standard.

**Method:** In each `## Steps` block, add one line at the create-the-note step: "Read `30_Order/Standards/[Type] Standard.md` before writing." Patch by heading; no other rewriting.

**Done when:** Each workflow has exactly one new reference line at its create step.

## Phase 6 — Audit two skills
**Files:** [`ingest-clipping.md`](.claude/skills/ingest-clipping.md), [`research-distiller.md`](.claude/agents/research-distiller.md).

**Method:** Compress/remove the per-section content+formatting specs that now duplicate the Source Summary Standard (ingest-clipping Steps 3 spacing/wikilink/formatting, Step 4 formatting standard, Step 5 math, the body-structure prose in Step 6; research-distiller Steps 3–5b and the body prose in Step 6). Replace with one pointer line: "Read `30_Order/Standards/Source Summary Standard.md` before writing the note body." Keep all procedural tooling: source-type routing tables, PDF `pypdf` extraction, image/URL/markdown handling, content-extraction checklist, cross-reference, promotion candidates, logging, safety, and the file-location/frontmatter skeleton.

**Done when:** Both files keep their tooling steps, drop the duplicated content spec, and point to the Standard.

## Close-out
Append one entry to [`log.md`](60_Claude/07_AI_Information/Session Logs/log.md) (Vault Rules Part 14 format) describing the Standards layer extraction. No Git, no `.obsidian/`, no plugin `data.json`, no new top-level files.

## Verification (manual, read-only)
- Grep each Standards doc's `notes:` wikilinks to confirm targets exist.
- Grep the six templates for `<!--` to confirm zero remaining comments.
- Confirm Templater tokens (`<% tp.`) still present in each template.
- Re-read AGENTS.md table, Vault Rules subsection, and three workflows to confirm patches are scoped.
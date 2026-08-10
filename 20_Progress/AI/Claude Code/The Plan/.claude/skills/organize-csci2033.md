# organize-csci2033

**Description:** Merge and refine CSCI 2033 linear algebra notes into durable evergreen concept notes, while preserving existing weekly writing.

**Usage:** `/organize-csci2033`

---

## Instructions

When this skill is invoked:

### 0. Hard Safety Constraints

- Never delete content from any file.
- Never rewrite or replace a whole file when patching by heading is possible.
- Weekly files are append-only: do not modify existing lines, wording, or order.
- Preserve frontmatter keys that already exist.
- If a target heading is missing, add a new heading at the end instead of altering existing structure.

### 1. Scope and Sources

Work only in:

- `50_Archive/Previous Classes/CSCI 2033/Concepts/` (final evergreen outputs)
- `50_Archive/Previous Classes/CSCI 2033/Concepts_old/` (human-edited source)
- `50_Archive/Previous Classes/CSCI 2033/Concepts_new/` (Claude-generated source)
- `50_Archive/Previous Classes/CSCI 2033/Week - *.md` (weekly timeline notes)

Treat folder roles as:

- `Concepts`: final evergreen concept library
- `Concepts_old`: user-improved concept material to preserve and refine
- `Concepts_new`: supplemental/alternate distilled material
- weekly files: historical progression and class timeline

### 2. Build a Merge Map

Create a source map before editing:

- Match concept files by topic similarity (title keywords and shared formulas).
- Match weekly files from `Concepts_new/Week_*.md` to root `Week - *.md` files.
- Remove or move the files in `Concepts_new/Week_*.md` to the `Concepts` evergreen notes folder after refining the content.
- Record missing pairs and continue with best-effort matching.

Output a short plan summary before edits:

- Concepts to create or update in `Concepts/`
- Weekly files to append
- Any ambiguous matches

### 3. Create/Refine Evergreen Concept Notes in `Concepts/`

For each concept topic, create or update one evergreen note in `Concepts/`.

Required quality bar:

- Explain for future higher-level topics: matrices, PageRank, least squares, graph basics, representations, optimization.
- Keep conceptual intuition + formal math + practical interpretation.
- Include notation definitions before advanced formulas.
- Add at least one worked mini-example per major concept.
- Add "common mistakes" or "pitfalls" to prevent future confusion.
- Add cross-links to related local notes when available.

Recommended structure:

```markdown
# Concept
## MOC
- [[W__ L__ - ...]]
- [[HW__ - ...]]
## Definition
- 
## Resources
- 
### How to use them
1. 
2. 
## Textbook Summary

## Weekly Summary

## Common mistakes
- 
## Mini-test (answer without looking)
- [ ] Flashcards
- [ ] 
## Flashcards (best 3–8)
#CSCI2033
- Question::Answer
```

Frontmatter rules for `Concepts/` files:

- Ensure `type: concept`
- Keep `status` (or set `status: sprout` if absent)
- Keep existing metadata; add missing keys instead of removing any
- Follow the metadata template from the folder `Classes/Concept Template` inside the 30_Order/Templates folder.

Conflict resolution:

- Keep user-authored nuance from `Concepts_old` for checking what additional content has been added.
- Use `Concepts_new` to fill rigor, completeness, and cleaner structure.
- If two statements conflict, prefer mathematically correct statement and add a short clarification note.

### 4. Enrich Weekly Files Without Altering Existing Content

Weekly files are historical and human-authored. Do not rewrite existing text.

For each root weekly file `Week - *.md`:

- Detect headings with low content (empty, placeholder bullets, or very short sections).
- Only append new material under those underdeveloped headings.
- If no suitable heading exists, append a new section at end:
  - `## Evergreen Clarifications`
- Add concise bridge content:
  - definitions
  - one example
  - one "connect to future topics" note

Append-only policy implementation:

- Add new lines after existing content in each header.
- Do not delete existing lines. You are allowed to rearrange and add content.
- Do not "fix" grammar in old text unless user explicitly asks.

### 5. Keep Notes Durable

Write for long-term reuse:

- Use plain, direct language with minimal jargon.
- Define symbols once and reuse consistently.
- Include brief retrieval cues ("If you forget this, remember...").
- Prefer understanding over memorization.
- Use Latex for math formuals, understand how my plugins work and style my content accordingly.

### 6. Completion Report

After edits, return:

- Files created in `Concepts/`
- Files updated in `Concepts/`
- Weekly files appended and which headings were expanded
- Remaining gaps or topics needing lecture/homework sources

---

## Prompt Mode (No Skill Install)

If user asks for a one-shot prompt instead of using this skill, provide a prompt that includes:

- folder roles (`Concepts`, `Concepts_old`, `Concepts_new`, weekly files)
- strict no-deletion rule
- weekly append-only rule
- evergreen quality bar for advanced future courses
- required completion report format

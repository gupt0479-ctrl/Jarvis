---
type: evergreen
status: sprout
created: 2026-07-29
updated: 2026-07-29
tags:
  - internship
  - standard
  - automation
notes:
  - "[[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]"
  - "[[20_Progress/Internship/Building System/Source of Truth]]"
  - "[[20_Progress/Internship/Building System/System - Build Log]]"
next: "Referenced by 'Prompt 4/5' in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]] — the dossier-improvement build should conform to this, not re-derive it."
---
# Internship Notes Standard
==Was an empty stub until 2026-07-29 despite being cited by [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] and every dossier-writing code path — this is the first real content.== Written after a live audit found dossier notes structurally consistent (writer.py's template is applied uniformly) but substantively broken in four ways: unreadable pasted content, zero interlinking (notes float with no MOC/company connection), no distinction between "current" and "removed" dossiers, and a resource-limit spec (see [[20_Progress/Internship/Building System/Source of Truth]]) that exists on paper but not in code. This standard is the contract; the build that makes code match it is tracked in [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]].

## Scope
Applies to every note `gupta-builds/internship-research-loop` writes into `10_Areas/Career/Internships/List/Dossiers/` (including `Viewed/`). Does not govern Program/Contact/Tracker notes — those have their own templates (`30_Order/Templates/Career/`) and are written by `/promote-dossier`, a separate human-consent step.

## 1. Frontmatter — required fields
Every dossier carries exactly the fields `vault_writer/writer.py`'s `build_frontmatter()` produces, in this order: `company, title, url, source, terms, locations, target_year, date_posted, date_found, matched_reason, status, next, tags`. Fail-closed, same as everywhere else in this codebase (`vault_writer/validate.py`'s `REQUIRED_FRONTMATTER_FIELDS`) — a field is present even when `null`/`[]`, never omitted.

**New requirement, 2026-07-29 — `notes:` interlink field.** Every dossier must carry a `notes:` list (the same convention every other evergreen/MOC-style note in this vault already uses — see `Dossiers MOC.md`, `Source of Truth.md`, `System - Build Log.md`) containing:
- **Always:** `"[[10_Areas/Career/Internships/List/Dossiers MOC]]"` — a dossier that doesn't point back to the MOC is exactly the "floating note" problem this rule exists to close.
- **If this dossier is a removal** (moved to `Viewed/` — see §4): also `"[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"`, appended, never replacing the first link — a removed dossier is still a dossier that was once live, its MOC membership is historical fact, not something removal erases.

**Same-company clustering.** No per-company hub note exists anywhere in this vault (Program notes carry a plain `company:` string, not a link — checked directly against the real `Programs/Considering/Software Engineering Intern - Appian.md` note, 2026-07-29) and creating N-1 backfill edits every time a new same-company dossier lands is exactly the kind of accumulating maintenance cost this codebase's zero-LLM/deterministic ethos avoids elsewhere. **Use a tag, not a link list**: add `company/<slugified-company-name>` to the existing `tags:` array (e.g. `company/appian`, `company/aquatic-capital-management` — same slugification rule as filenames: lowercase, spaces to hyphens, strip `\/:*?"<>|`). Obsidian's tag pane and a `FROM #company/x` Dataview query both cluster same-company dossiers for free, with no write-time lookup of "what else exists for this company" and no risk of a stale link list. If a real need for direct company-to-company wikilinks surfaces later (not hypothetical — an actual workflow that needs it), revisit; don't build the link-list version preemptively.

## 2. Body content — readable, structured, not a raw scrape dump
Currently every dossier pastes `extract_content()`'s output verbatim under `## Posting (fetched <date>)` — real, observed problems as of 2026-07-29: repeated boilerplate (Conagra's "About Us" paragraph appears twice, verbatim, in the same note), UI chrome mixed into body text (`locationsChicago, Illinois` / `time typeFull time` / `job requisition id...` run together with no structure), and zero section structure (a wall of text, not scannable). This is a real defect, not cosmetic — the whole point of Phase 6 pasting real content was to let a 60-second read replace a page visit; unstructured noise defeats that.

**Fix stays zero-LLM** (see [[../../CLAUDE.md|internship-research-loop CLAUDE.md]] in the repo — `ingestion/posting_page.py`'s `extract_content()` is in the unattended path, ships hourly, no exception). The fix is a better deterministic content-structuring pass, not a summarizer:
- **Dedupe repeated paragraphs.** A paragraph (roughly: a blank-line-delimited block) that appears twice verbatim in the same fetch is boilerplate, not content — keep the first occurrence, drop the rest. Cheap, deterministic, no false-positive risk on genuinely short/simple postings (nothing to dedupe if nothing repeats).
- **Split the known ATS-chrome key:value run-ons** (`locations`, `time type`, `posted on`, `job requisition id`, `time left to apply`) onto their own lines before the free-text body starts, instead of leaving them jammed against the first sentence of real content.
- **Section headings, where the source text actually has them** (most real postings already write `Responsibilities` / `Qualifications` / `Requirements` / `Benefits` / `Compensation` as their own line or bolded phrase) — preserve them as real markdown `###` headings instead of flattening everything to plain paragraphs. Do not invent section boundaries the source text doesn't have; a posting with no internal structure stays one block, described as-is, not force-split.
- **Strip known non-content chrome** already partially handled (nav links, "apply now" buttons) — extend to the patterns found live: "Read More" truncation markers, repeated "Follow Us" / social-link lists, and — the real, distinct Google Careers bug (2026-07-26 audit, `[[20_Progress/Internship/Building System/Runs/Claude Code Prompts]]` Task E) — an entire unrelated search-results-listing page preceding the real posting on some ATS platforms. That's an extraction-target bug (wrong page/wrong `waitFor`), not a formatting one; fix at the fetch layer, not by trying to filter listing-page noise out after the fact.

## 3. Company & degree facts — structured, not just prose
Mirrors the "Backfill" rule already proven necessary for Program notes (`.claude/skills/promote-dossier/reference/note-templates.md` in the repo, added after the real Appian run found facts written into prose but never backfilled into frontmatter): if a dossier's own posting content states a concrete class-year, degree-level, or citizenship/OPT signal, that fact must be checked against structured filter behavior, not left to silently pass on missing-data permissiveness. Concretely: a PhD-only posting (real example, Optiver "Quantitative Research Intern, PhD," Greenhouse — no structured degree field, so `degrees_eligible()`'s missing-data permissiveness waved it through) should be caught by a content-level degree check, the same shape as the existing OPT content check (`opt_exclusion()` in `ingestion/posting_page.py`) — permissive by default, reject only on an explicit "PhD required"/"PhD only"/"doctoral candidates only" signal, never on "PhD preferred" or a degree merely being listed among several acceptable ones.

## 4. Removal — move, don't delete; mark, don't erase
`recheck.py` currently deletes a closed-posting dossier outright (`Path(r["path"]).unlink()`). **Changing, 2026-07-29**: a removed dossier moves to `10_Areas/Career/Internships/List/Dossiers/Viewed/` instead of being deleted — the posting closing is real information (a signal about that company's hiring cadence, evidence for why a later duplicate should be rejected, a record of what this pipeline actually saw), and deleting it outright throws that away for no benefit `git log` doesn't already partially provide less usably.
- On move: append `"[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"` to `notes:` (see §1) — the original Dossiers MOC link and any `company/<slug>` tag stay, unchanged. A removed dossier's history (it was once live, it was in bucket X, it was for company Y) is real and shouldn't disappear because the posting itself closed.
- Add a `removed_date` and `removed_reason` field to the frontmatter at move time (mirrors `recheck.py`'s own existing `reason` string — `"absent from live feed"` or `"active: false upstream"` — already computed, just not currently persisted anywhere once the file is gone).
- `status:` should reflect this too — set to `removed` (currently every dossier's `status` is a static `unreviewed`; this is the first real transition the field will ever see, and it existing unused until now is itself evidence this was always the intended design, not a new field to invent).
- `state/dossier_uids.json` (the uid→path manifest `vault_writer/writer.py` maintains) must be updated to the new post-move path, not left pointing at a file that no longer exists there — a stale manifest entry breaks the next `write_dossier()` idempotency check for that uid.
- `Viewed/` is a **human triage bin**, never a pipeline write target for new dossiers (per [[20_Progress/Internship/Building System/Source of Truth]]) — only `recheck.py`'s removal path writes here, and only by moving an existing file, never creating a new one directly.

## 5. Resource limits — a notification, not a silent hard stop
Per [[20_Progress/Internship/Building System/Source of Truth]] and [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]: 50 files per priority bucket, 201 total (`List/Dossiers/` excluding `Viewed/`), designed 2026-07-26, still not in code as of this writing. **Clarified 2026-07-29**: hitting a bucket's threshold is a **notification**, surfaced in two places — the vault side (a visible warning on `Dossiers MOC.md` / the Tracker dashboard, so a human opening the vault sees it without reading logs) and the codebase side (a run-log field, and a filed GitHub issue on first crossing — not a hard refusal to write). The point is forcing a human review decision to happen, not silently discarding a real, currently-open posting the same way an exclusion gate would. See [[20_Progress/Internship/Building System/Runs/Claude Code Prompts]] for the exact build spec.

## Done When
- Every dossier's `notes:` field resolves (Dossiers MOC, plus Removed Dossiers MOC for anything in `Viewed/`) — no broken/missing links.
- A same-company second dossier shares its `company/<slug>` tag with the first, verifiable via Obsidian's tag search.
- A spot-read of five random dossiers shows no duplicated paragraphs and no jammed-together UI-chrome lines.
- A bucket crossing 50 shows up on `Dossiers MOC.md` without opening `logs/runs.jsonl`.
- A closed posting's dossier is findable in `Viewed/`, not gone.

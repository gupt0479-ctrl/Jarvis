---
type: evergreen
status: active
created: 2026-08-23
tags:
  - internship
  - moc
  - automation
notes:
  - "[[30_Order/Standards/Internship Notes Standard]]"
  - "[[10_Areas/Career/Internships/List/Dossiers/Viewed/Removed Dossiers MOC]]"
  - "[[20_Progress/Internship/Applying/Now]]"
next:
---
# What Was Viewed
==Rewritten 2026-08-23 to match the system's actual, already-shipped design instead of a since-corrected earlier draft.== `Viewed/` holds postings this pipeline saw and screened out because the posting itself closed - not internships that were applied to. Per [[30_Order/Standards/Internship Notes Standard]] §4 and `recheck.py`'s real behavior: a dossier moves here only when `recheck.py` finds its posting is no longer live upstream (`removed_reason: "active: false upstream"` or `"absent from live feed"`), never because a human applied to it. `Viewed/` is a human triage bin - seen, not used - and it is never a pipeline write target for new dossiers.

## Why This Note Used To Say Something Different
An earlier draft of this note described `Viewed/` as holding "internships that have been applied for already... so that we do not repeat the same internships." That was a real, understandable need - but the wrong folder for it, and two independent audit sessions found the same mismatch independently rather than one session guessing at a fix: [[20_Progress/Internship/Building System/Runs/Claude Code Prompts — Archive]]'s Prompt 8 (2026-08-23, vault-side Standards work) flagged the conflict without resolving it; Prompt 9 (2026-08-23, the six-fork dossier audit) reached the same read from the codebase side while confirming `recheck.py`'s actual, shipped move-to-`Viewed/` behavior. Neither session touched this note or `Viewed/` itself - the human decided 2026-08-23 to keep the existing design and rewrite this note instead, which is what this rewrite does.

## Where "Applied, Don't Repeat" Actually Lives
The need the old draft was reaching for is already served by two notes that already exist in this vault - they're just empty right now because zero real applications have been submitted yet, which is exactly why the need felt unmet:
- **[[20_Progress/Internship/Applying/Now]]** - the exhaustive live list of every internship currently mid-application. This is the fastest "have I already gone after this one" check.
- **`10_Areas/Career/Internships/Tracker/Each One/Applied/` and `Result/`** - per [[30_Order/Standards/Internship Notes Standard]]'s sibling [[30_Order/Standards/Tracking Standard]], a Tracker note moves from `Current/` to `Applied/` the moment a real application goes out, and to `Result/` once an outcome lands. Once real applications start, checking either folder answers "did I already apply to this company/role" directly - no need to search `Viewed/` for it.

## What Actually Belongs Here
```dataview
TABLE company, title as "Role", removed_reason as "Why It Closed", removed_date as "Closed"
FROM "10_Areas/Career/Internships/List/Dossiers/Viewed"
WHERE company
SORT removed_date DESC
```
Real signal worth reading over time: a company that closes postings unusually fast after they're found is useful evidence about that company's hiring cadence for next cycle, and a duplicate-looking posting reappearing later is evidence for the exclusion/dedup logic tracked in [[20_Progress/Internship/Building System/Source of Truth]] - not a reason to re-screen it by hand. If this folder grows past a size where a flat view stops being useful, organize by month the same way `List/YYYY-MM Found.md` already does for discovery - that part of the original note's ambition was sound, it was just pointed at the wrong purpose.

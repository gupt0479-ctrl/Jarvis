---
type: evergreen
status: active
created: 2026-07-26
tags:
  - internship
  - moc
  - automation
notes:
  - "[[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]]"
  - "[[Source of Truth]]"
  - "[[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC]]"
---
# Dossiers — Map of Content
==Everything currently in `List/Dossiers/`, live, by priority folder.== See [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] for the gate that gets a posting here at all. Nothing here is hand-edited into existence — this note only reads what the loop already wrote. For whether what it wrote is actually correct, see [[60_Claude/30_Reviews/Internship Loop/Internship Loop Reviews MOC|Internship Loop Reviews MOC]] — the weekly review sampling this folder for gate/classification/Standard conformance.
## ⚠️ Capacity Notification
Live-computed, not code-maintained — this section reads the real folder counts every time this note renders, so a bucket crossing its threshold shows up here without anyone having to push a change. See [[Internship Notes Standard]] §5: crossing 50 is a notification, never a silent write-refusal.
```dataviewjs
const buckets = ["1 - AI & ML", "2 - Fullstack", "3 - CyS & Finance", "Other"];
const root = "10_Areas/Career/Internships/List/Dossiers";
const rows = buckets.map(b => {
  const count = dv.pages(`"${root}/${b}"`).length;
  const flag = count >= 50 ? "🔴 AT/OVER CAP (50)" : count >= 40 ? "🟡 approaching (40+)" : "🟢 ok";
  return [b, count, flag];
});
const total = rows.reduce((sum, r) => sum + r[1], 0);
dv.table(["Bucket", "Count", "Status"], rows);
dv.paragraph(`**Total (excl. Viewed/): ${total} / 201.** Design: [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]].`);
```
## 1 — AI & ML
```dataview
TABLE company, title, terms, status, preference_tier
FROM "10_Areas/Career/Internships/List/Dossiers/1 - AI & ML"
SORT preference_tier DESC, company ASC
```
## 2 — Fullstack
```dataview
TABLE company, title, terms, status, preference_tier
FROM "10_Areas/Career/Internships/List/Dossiers/2 - Fullstack"
SORT preference_tier DESC, company ASC
```
## 3 — CyS & Finance
```dataview
TABLE company, title, terms, status, preference_tier
FROM "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance"
SORT preference_tier DESC, company ASC
```
## Other — Real Software, Outside The Three Priorities
```dataview
TABLE company, title, terms, status, preference_tier
FROM "10_Areas/Career/Internships/List/Dossiers/Other"
SORT preference_tier DESC, company ASC
```
## Not Yet Sorted
Sits flat at this folder's root — written before the priority-classification build landed (see [[Claude Code Prompts]]). Once that ships, this section should stay empty.
```dataview
TABLE company, title, terms, status
FROM "10_Areas/Career/Internships/List/Dossiers"
WHERE company AND !contains(file.folder, "/Dossiers/")
SORT date_found DESC
```
## Counts By Folder
```dataview
TABLE WITHOUT ID
  file.folder as "Folder", length(rows) as Count
FROM "10_Areas/Career/Internships/List/Dossiers"
WHERE company
GROUP BY file.folder
```

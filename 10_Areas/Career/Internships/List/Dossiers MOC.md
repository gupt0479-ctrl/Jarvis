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
---
# Dossiers — Map of Content
==Everything currently in `List/Dossiers/`, live, by priority folder.== See [[10_Areas/Career/Internships/List/Dossiers/Dossiers-to-Create]] for the gate that gets a posting here at all. Nothing here is hand-edited into existence — this note only reads what the loop already wrote.
## 1 — AI & ML
```dataview
TABLE company, title, terms, status
FROM "10_Areas/Career/Internships/List/Dossiers/1 - AI & ML"
SORT company ASC
```
## 2 — Fullstack
```dataview
TABLE company, title, terms, status
FROM "10_Areas/Career/Internships/List/Dossiers/2 - Fullstack"
SORT company ASC
```
## 3 — CyS & Finance
```dataview
TABLE company, title, terms, status
FROM "10_Areas/Career/Internships/List/Dossiers/3 - CyS & Finance"
SORT company ASC
```
## Other — Real Software, Outside The Three Priorities
```dataview
TABLE company, title, terms, status
FROM "10_Areas/Career/Internships/List/Dossiers/Other"
SORT company ASC
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

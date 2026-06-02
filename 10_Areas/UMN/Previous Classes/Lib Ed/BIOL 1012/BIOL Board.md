---
type: class
input_kind: board
status: seed
created: 2026-01-21
updated: 2026-05-06
area:
  - "[[Weekly Board]]"
  - "[[UMN Board]]"
tags:
  - "#class"
next: "[[Theme 4 Hub]]"
---
# Data View
## Lecture and Discussion Assignments
```dataview
TABLE created, status, area, next
FROM "10_UMN/_Homework/Lib Ed/BIOL"
WHERE type = "class"
AND input_kind = "homework"
SORT created ASC
```
## Lecture
```dataview
TABLE created, status, area, next
FROM "10_Areas/Degree/UMN/Classes/BIOL 1012"
WHERE type = "class"
AND input_kind = "lecture"
SORT created ASC
```
## Labs
```dataview
TABLE created, status, area, next
FROM "10_Areas/Degree/UMN/Classes/BIOL 1012"
WHERE type = "class"
AND input_kind = "lab"
SORT created ASC
```
## Exams
```dataview
TABLE created, status, area, next
FROM "10_Areas/Degree/UMN/Classes/BIOL 1012"
WHERE type = "class"
AND input_kind = "exam"
SORT created ASC
```
# MOC
## Theme 4
- [[Theme 4 Hub]]
- [[Sex Characteristics and Endocrine Signaling]]
- [[Meiosis and Gametogenesis]]
- [[Hormones of Spermatogenesis]]
- [[Uterine and Ovarian Cycles]]
- [[Fertilization Pregnancy and Birth]]
- [[Cell Cycle and Cancer]]
- [[Cancer Treatments and Ethics]]
- [[Theme 4 Practice and Figures]]
- [[Theme 4 Lecture and Packet Deep Notes]]
- [[Theme 4 Prediction Drill Bank]]
- [[Theme 4 Source Coverage Checklist]]

1. *Main*:
```dataview
TABLE created, mastery, status, topics, related
FROM "10_Areas/Degree/UMN/Classes/BIOL 1012"
WHERE type = "class"
AND input_kind = "board"
SORT created ASC
```
2. *Concepts*:
```dataview
TABLE created, mastery, status, topics, related
FROM "10_Areas/Degree/UMN/Classes/BIOL 1012"
WHERE type = "concept"
SORT created ASC
```

## Resources

### Links
- *All Lecture recordings*: [Posted Here](https://docs.google.com/document/d/1_XId4SHEGFNUwzE4F-BWlI4oB7gKBaSLyPNRT2uKmBE/edit?tab=t.0#heading=h.uk6jrnhcgmcr)
  - [[Edit (docs.google.com)|source note]]
- *All Lecture Slides*: [Posted here](https://drive.google.com/drive/folders/1NDNsln6-0QBGEP_0dhayrnyKoSKf_iHH)
  - [[1Ndnsln6 0Qbgep 0Dhayrnykoskf Ihh (drive.google.com)|source note]]
- 

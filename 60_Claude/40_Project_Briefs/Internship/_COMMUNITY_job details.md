---
type: community
members: 4
---

# job details

**Members:** 4 nodes

## Members
- [[Jobs search results]] - document - tests/fixtures/posting_google_careers.md
- [[Software Engineering Intern, MS, Summer 2027]] - document - tests/fixtures/posting_google_careers.md
- [[job details]] - document - tests/fixtures/posting_google_careers.md
- [[posting_google_careers]] - document - tests/fixtures/posting_google_careers.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/job_details
SORT file.name ASC
```

---
type: community
members: 11
---

# grade

**Members:** 11 nodes

## Members
- [[(text, tags) for every '- ' line carrying at least one skill tag.]] - rationale - grade_resume.py
- [[Bullets ranked by distinct-JD-keyword overlap (score, text, tags, matched).]] - rationale - grade_resume.py
- [[grade()]] - code - grade_resume.py
- [[grade_resume.py]] - code - grade_resume.py
- [[keywords()]] - code - grade_resume.py
- [[main()_1]] - code - grade_resume.py
- [[parse_bullets()]] - code - grade_resume.py
- [[test_grade_ranks_matching_bullet_first()]] - code - tests/test_grade_resume.py
- [[test_grade_resume.py]] - code - tests/test_grade_resume.py
- [[test_keywords_drops_stopwords_keeps_tech_tokens()]] - code - tests/test_grade_resume.py
- [[test_parse_bullets_keeps_only_tagged()]] - code - tests/test_grade_resume.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/grade
SORT file.name ASC
```

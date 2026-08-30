---
type: community
members: 9
---

# Checks to run, in this order

**Members:** 9 nodes

## Members
- [[1. Full test suite_1]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[2. Scheduled workflow history (last N runs each)_1]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[3. Vault dossier counts vs. what run logs claim was written_1]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[4. seen_ids.json  vault divergence_1]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[5. Auto-filed GitHub issues_1]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[Checks to run, in this order_1]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[Output format_4]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[SKILL_4]] - document - .cursor/skills/loop-health-check/SKILL.md
- [[loop-health-check]] - document - .cursor/skills/loop-health-check/SKILL.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Checks_to_run_in_this_order
SORT file.name ASC
```

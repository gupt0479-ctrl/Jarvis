---
type: community
members: 8
---

# Checks to run, in this order

**Members:** 8 nodes

## Members
- [[1. Full test suite]] - document - .claude/agents/loop-verifier.md
- [[2. Scheduled workflow history (last N runs each)]] - document - .claude/agents/loop-verifier.md
- [[3. Vault dossier counts vs. what run logs claim was written]] - document - .claude/agents/loop-verifier.md
- [[4. seen_ids.json  vault divergence]] - document - .claude/agents/loop-verifier.md
- [[5. Auto-filed GitHub issues]] - document - .claude/agents/loop-verifier.md
- [[Checks to run, in this order]] - document - .claude/agents/loop-verifier.md
- [[Output format_1]] - document - .claude/agents/loop-verifier.md
- [[loop-verifier]] - document - .claude/agents/loop-verifier.md

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Checks_to_run_in_this_order
SORT file.name ASC
```

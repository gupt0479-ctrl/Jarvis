---
type: evergreen
status: active
created: 2026-06-03
updated: 2026-06-03
tags:
  - plan
  - summer
  - leetcode
  - dsa
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[01 - Daily Operating System]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
next: "[[06 - ML Fundamentals (2033 + 2230)]]"
---

# LeetCode & CSCI 4041

**Non-negotiable: ≥5 LeetCode problems every day.** LeetCode *is* the practical arm of CSCI 4041 — every problem should connect back to an algorithms concept from that course, so solving doubles as the 4041 overview pass you still owe yourself.

CSCI 4041 has concrete notes you haven't overviewed (too much content at once). Fix: stop trying to read all of it. Instead, **let the day's LeetCode topic pull the matching 4041 concept** into review. The notes improve as you re-encounter them through problems.

## Daily system

1. Pick **today's topic** from the rotation below.
2. Solve **5 problems** in that topic (Easy→Medium; one Hard only if energy is high).
3. For **≥1 problem**, open the matching CSCI 4041 concept note and link the pattern (this is the "4041 review 25–45 min" row).
4. Log in the Today note: `count: 5 / topics: <topic> / 4041 link: <concept>`.

**Done when:** 5 problems solved + count/topics logged + ≥1 pattern tied to a 4041 concept.

**MVP (low-energy day):** 5 Easy in the current topic, no Hard, still log the 4041 link. Five is the floor — never below.

## Weekly topic rotation (maps to CSCI 4041)

| Day | Topic | CSCI 4041 concept anchor |
|-----|-------|--------------------------|
| Mon | Arrays / Two Pointers / Sliding Window | Asymptotics, loop invariants |
| Tue | Hashing / Stacks / Queues | Elementary data structures |
| Wed | Sorting / Binary Search | Heapsort, quicksort, divide & conquer |
| Thu | Linked Lists / Trees / BST | Binary search trees, tree traversal |
| Fri | Graphs (BFS/DFS) | Graph algorithms (BFS, DFS, topological sort) |
| Sat | Dynamic Programming / Greedy | DP, greedy, optimal substructure |
| Sun | Mixed review / hardest topic of the week | Whatever was weakest — link to its 4041 note |

> Rotation is a default, not a cage. If a 4041 topic is weak, spend two days on it. The rule that never bends is **5/day**.

## CSCI 4041 overview pass (run *through* LeetCode, not separately)

The board: [[CSCI 4041 Board]] (main file [[DSA]]). Concepts live under `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/`.

- Each rotation day, after solving, spend 25–45 min on the **one** concept note that matches the topic.
- Output requirement (so it's not passive reading): add **one** line to the concept note — a pattern, a gotcha, or a link to today's LeetCode problem.
- Over ~2 weeks of rotation you complete one full overview pass without ever sitting down to "read all of 4041."

## Tracking artifact

LeetCode count is a hard scorecard metric in `/closeday`. The running log lives in the daily Today notes (`count:` line). Weekly total is summed in [[02 - Weekly Operating System]] — target **≥35/week**.

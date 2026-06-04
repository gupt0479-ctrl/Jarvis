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
  - interviews
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[01 - Daily Operating System]]"
  - "[[05a - LeetCode Tracker]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Repos]]"
next: "[[06 - ML Fundamentals (2033 + 2230)]]"
---

# LeetCode & CSCI 4041 — Summer Flagship

## 1. Strategic summary

CSCI 4041 is the **summer internship flagship**: the one course to perfect end-to-end. LeetCode is the daily engine (≥5/day, never below); the 15 vault concept notes under [[DSA]] are the long-term memory; the two professor projects (AVL midterm, Maze final) are the proof artifacts. The win condition is not "finished the course" — it's **every concept internalized and instantly revisable 48h before any interview**, with company-tagged problems already drilled. Everything here maps to a real vault file; nothing is generic.

Three layers run in parallel: **mastery** (the 15 concepts → `tree`), **practice** (daily LeetCode + company rotation, logged in [[05a - LeetCode Tracker]]), and **projects** (re-implement AVL + Maze with tests + interview bullets).

## 2. Mastery & interview revision system

The 15 concepts from the [[DSA]] MOC. Mastery 0–10 is self-rated; no concept reaches `tree` until the **Never-Forget checklist** passes. `Last reviewed` and `Company tags done` are updated as you go (mirror into [[05a - LeetCode Tracker]]).

| # | Concept | Vault note path | Mastery 0–10 | LeetCode patterns | Last reviewed | Company tags done |
|---|---------|-----------------|:---:|-------------------|:---:|---|
| 1 | Sorting Algorithms | `…/Concepts/Algorithms/Sorting Algorithms.md` | 0 | sort+scan, custom comparator, merge | — | — |
| 2 | Time Complexity | `…/Concepts/Time Complexity.md` | 0 | amortized, recurrence, Master method | — | — |
| 3 | Divide and Conquer | `…/Concepts/Algorithms/Divide and Conquer.md` | 0 | binary search, merge intervals | — | — |
| 4 | QuickSort | `…/Concepts/Algorithms/QuickSort.md` | 0 | partition, quickselect, kth-largest | — | — |
| 5 | HeapSort | `…/Concepts/Algorithms/HeapSort.md` | 0 | top-k, k-way merge, median stream | — | — |
| 6 | Elementary Data Structures | `…/Concepts/Data Structures & Methods/Elementary Data Structures.md` | 0 | stack/queue, monotonic stack, linked-list | — | — |
| 7 | AVL Trees | `…/Concepts/Trees/AVL Trees.md` | 0 | BST validate/insert/delete, rotations | — | — |
| 8 | B-Trees | `…/Concepts/Trees/B-Trees.md` | 0 | range queries, ordered map intuition | — | — |
| 9 | Hashing | `…/Concepts/Data Structures & Methods/Hashing.md` | 0 | freq map, two-sum family, dedup | — | — |
| 10 | Dynamic Programming | `…/Concepts/Algorithms/Dynamic Programming.md` | 0 | 1D/2D DP, knapsack, LIS, edit distance | — | — |
| 11 | Greedy Algorithms | `…/Concepts/Algorithms/Greedy Algorithms.md` | 0 | interval scheduling, heap-greedy | — | — |
| 12 | Graph Algorithms | `…/Concepts/Graphs/Graph Algorithms.md` | 0 | BFS/DFS, topo sort, SCC, islands | — | — |
| 13 | Minimum Spanning Trees | `…/Concepts/Graphs/Minimum Spanning Trees.md` | 0 | Kruskal+union-find, Prim | — | — |
| 14 | Shortest Paths | `…/Concepts/Graphs/Shortest Paths.md` | 0 | Dijkstra, Bellman-Ford, Floyd-Warshall | — | — |
| 15 | Maximum Flow | `…/Concepts/Graphs/Maximum Flow.md` | 0 | max-flow/min-cut, bipartite matching | — | — |

### Never-Forget checklist (per concept — required to mark `tree`)

A concept is `tree` only when all four pass, from memory:

1. **Explain** it in 3 sentences (what, when to use, cost).
2. **Implement** the core skeleton from scratch (no reference).
3. **Solve 2 LeetCode mediums** in that pattern from memory.
4. **One interview story / gotcha** written in the concept note's flashcards.

Until then: `seed` (untouched) → `sprout` (explained + skeleton) → `tree` (all four).

### Revision protocol (spaced re-touch)

- **Weekly weak-topic day** (Sun): pick the lowest-mastery concept, re-touch it (re-implement skeleton + 2 problems). Bump its `Last reviewed`.
- **Pre-interview 48h cram**: auto-build the cram list = every concept with **mastery < 7**, ordered by company tag relevance. The mastery table *is* the cram list generator.
- **Flashcards:** extend the existing `#cards/CSCI4041` pattern (already in [[DSA]]) into each concept note. Where a concept note has no `## Practice Map` heading yet (e.g. AVL Trees currently links to a missing one from DSA), create it during that concept's deep-dive day.

## 3. LeetCode daily system (≥5/day)

The floor stays **5/day**. Structure each day's five:

- **3 pattern problems** — the topic tied to the current [[DSA]] week (section 4 below), not a generic label.
- **2 company-focus problems** — from the week's rotating company (section below).

Log every problem in [[05a - LeetCode Tracker]] the same day: `count, topics, problem IDs, company tag, 4041 concept, difficulty, redo date`.

**MVP (low-energy):** 5 Easy in the current pattern, skip the company two, still log. Five is never breached.

### Company-wise layer (primary internship lever)

Primary targets: **Google, Amazon, Meta** (rotate one per week). Source repos (reference only, no setup):

- `leetcode-companywise-interview-questions` (snehasishroy) — company-wise tagged questions as of May 2026, Java solutions. **Use:** look up the week's company tag, sort by frequency, do the top N. (From [[GitHub Stars — How Anant Uses Each Repo]].)
- `interview-company-wise-problems` — second company-tagged set; cross-reference.
- Both catalogued in [[Repos]] under the Jobs list.

**Weekly:** pull the top ~10 highest-frequency problems for the rotating company × this week's topic; the daily "2 company problems" come from that pulled set.

## 4. Summer 4041 syllabus (week-by-week)

Mirrors [[DSA]] `## LeetCode / Weekly Plan` (the vault week numbering is authoritative). Company focus rotates Google → Amazon → Meta. LC minimum ≥5/day = **≥35/week**. Dates are placeholders until you fix the start Monday — fill them in [[05a - LeetCode Tracker]].

| Wk | Vault week + textbook | Concept deep-dive | LC focus (≥35/wk) | Company | Project tie-in |
|---|---|---|---|---|---|
| 1 | Week 1 & 2 · Ch 1 & 2 | Sorting Algorithms, Time Complexity | insertion/merge, asymptotics | Google | — |
| 2 | Week 3 · Ch 3 & 4 | Divide and Conquer | binary search, recurrences | Google | — |
| 3 | Week 4 · Ch 7 & 10 | QuickSort, Elementary Data Structures | partition, stack/queue, linked-list | Amazon | — |
| 4 | Week 5 · Ch 6 & 12 | HeapSort, BST basics | top-k, heap, BST ops | Amazon | — |
| 5 | Week 6 · Ch 13, 18 | AVL Trees, B-Trees | rotations, balanced-tree | Meta | **AVL midterm — start** |
| 6 | Week 7 · Ch 13 | AVL / Red-Black | tree validation, fix-up | Meta | **AVL midterm — ship** |
| 7 | Week 8 · Ch 11 | Hashing | freq map, two-sum family | Google | — |
| 8 | Week 9 · Ch 14 | Dynamic Programming | 1D→2D DP, knapsack, LIS | Amazon | — |
| 9 | Week 10 · Ch 15 | Greedy Algorithms | interval scheduling, heap-greedy | Meta | — |
| 10 | Week 11 · Ch 20 | Graph Algorithms (BFS/DFS) | islands, traversal, topo | Google | **Maze final — start** |
| 11 | Week 12 · Ch 20, 21 | Topo sort, SCC, MST | union-find, Kruskal/Prim | Amazon | **Maze final — BFS/DFS core** |
| 12 | Week 13 · Ch 22, 23 | Shortest Paths | Dijkstra, Bellman-Ford | Meta | **Maze final — ship + report** |
| 13 | Week 14 · Ch 24 | Maximum Flow | max-flow/min-cut, matching | Google | — |
| 14 | Week 15 · finals review | Redo from each block | mixed hardest-topic redo | rotate | Both projects: README + bullet |

**Milestones:** AVL midterm (Weeks 5–6), Maze final (Weeks 10–12). Concrete dates TBD — set them once the start Monday is fixed.

## 5. Professor projects (summer execution)

Re-implementation milestones, not just notes. Done = working code + tests + one interview bullet.

### AVL midterm (chosen)
- Source: `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Midterm Project/AVL Tree Project.md` (alternatives: Red Black Tree, Multiway Search Tree — not chosen).
- Do: re-implement AVL insert/delete with rotations; **invariant tests** (height-balance check after every op); trace one rebalance by hand.
- Evidence: code path + test log + 1 interview-story bullet ("balanced BST under adversarial insert order").
- Concept tie-in: [[AVL Trees]], rotations from Week 6–7.

### Maze final (chosen)
- Source: `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Final Project/Maze Project.md` + `Maze Project Details.md` (alternatives: Network Flow, Heuristic Pathfinding — not chosen).
- Do: BFS/DFS solve + shortest path; connect to spanning-tree generation.
- Evidence: demo screenshot/gif + test log + README line + 1 bullet ("graph search on a generated grid").
- Concept tie-in: [[Graph Algorithms]], [[Minimum Spanning Trees]], Weeks 11–12.

## 6. Overview pass without overload

You have concrete 4041 notes but never overviewed them — too much at once. The fix is **LeetCode pulls the concept**, not "read everything":

- Each day, after solving, spend a **25–45 min concept touch** on the note matching today's pattern, using its `## Practice Map` section (create the section if missing).
- **Cap: one concept depth per day.** The Week-by-week table (section 4) already sequences which concept each day; a full two-week rotation = one complete overview pass with zero "sit down and read all 15."

## 7. Wiring

Daily row lives in [[01 - Daily Operating System]] (unchanged — only linked). Progress logged in [[05a - LeetCode Tracker]]. Weekly LC total + weak-topic day handled in [[02 - Weekly Operating System]].

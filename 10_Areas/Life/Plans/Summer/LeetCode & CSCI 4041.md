---
type: plan
status: active
created: 2026-06-03
updated: 2026-07-27
tags:
  - plan
  - summer
  - leetcode
  - dsa
  - interviews
notes:
  - "[[00 - Summer Plans Index]]"
  - "[[Daily Operating System]]"
  - "[[Final Month Plan (Jul 28 - Sep 1)]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Repos]]"
next: "[[Final Month Plan (Jul 28 - Sep 1)]]"
---
# LeetCode & CSCI 4041 — Summer Flagship
==CSCI 4041 is the internship-flagship course: LeetCode is the daily engine, the 15 vault concepts are the long-term memory, the AVL and Maze professor projects are the proof artifacts.== Merged 2026-07-27 with the separate daily-log tracker — one file, not two, since the tracker was never anything but this plan's own data.
> [!WARNING]
> Zero problems logged all summer — the daily log table in §8 has never had a row filled in, and the mastery table below sits at `0` across every concept. The design was correct; it never ran. [[Final Month Plan (Jul 28 - Sep 1)]] restarts this as a daily-floor item.
## 1. Strategic summary
LeetCode is the daily engine (≥5/day, never below); the 15 vault concept notes under [[DSA]] are the long-term memory; the two professor projects (AVL midterm, Maze final) are the proof artifacts. The win condition is not "finished the course" — it's every concept internalized and instantly revisable 48h before any interview, with company-tagged problems already drilled. Three layers run in parallel: **mastery** (the 15 concepts → `tree`), **practice** (daily LeetCode + company rotation, logged in §8 below), and **projects** (re-implement AVL + Maze with tests + interview bullets).
## 2. Mastery & interview revision system
The 15 concepts from the [[DSA]] MOC. Mastery 0–10 is self-rated; no concept reaches `tree` until the Never-Forget checklist passes.
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
### Revision protocol
*Weekly weak-topic day (Sun):* pick the lowest-mastery concept, re-touch it, bump its `Last reviewed`.
*Pre-interview 48h cram:* every concept with mastery < 7, ordered by company-tag relevance — the mastery table above is the cram list generator.
## 3. LeetCode daily system (≥5/day)
The floor stays 5/day. Each day: 3 pattern problems (this week's [[DSA]] concept), 2 company-focus problems. Log every problem in §8 the same day: count, topics, problem IDs, company tag, 4041 concept, difficulty, redo date. **MVP for a bad day:** 5 Easy in the current pattern, skip the company two, still log — five is never breached.
### Company-wise layer
Primary targets: **Google, Amazon, Meta** — rotate one per week. Source repos: `leetcode-companywise-interview-questions` (snehasishroy) and `interview-company-wise-problems`, both catalogued in [[Repos]]. These only cover FAANG-style tagging. The real dossier targets in `10_Areas/Career/Internships/List/Dossiers/` skew toward forward-deployed and quant-trading roles — Palantir, HRT, Virtu, Chicago Trading, Marshall Wace, The Trade Desk — which lean on live coding and math/probability puzzles more than tagged LeetCode sets. That gap is covered by the System Design and Trading Knowledge daily tracks in [[Final Month Plan (Jul 28 - Sep 1)]], not by inventing fake company tags here.
## 4. Summer 4041 syllabus (week-by-week)
Mirrors [[DSA]] `## LeetCode / Weekly Plan`. Company focus rotates Google → Amazon → Meta. LC minimum ≥5/day = ≥35/week.
| Wk | Vault week + textbook | Concept deep-dive | LC focus | Company | Project tie-in |
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
Milestones: AVL midterm (Weeks 5–6), Maze final (Weeks 10–12) — dates fix once the start Monday is set against the actual calendar in [[Final Month Plan (Jul 28 - Sep 1)]].
## 5. Professor projects
Re-implementation milestones — done means working code + tests + one interview bullet.
1. **AVL midterm**
	Source: `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Midterm Project/AVL Tree Project.md`. Do: re-implement AVL insert/delete with rotations, invariant tests (height-balance check after every op), trace one rebalance by hand. Evidence: code path + test log + one interview-story bullet. Concept tie-in: [[AVL Trees]].
2. **Maze final**
	Source: `10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Final Project/Maze Project.md`. Do: BFS/DFS solve + shortest path, connect to spanning-tree generation. Evidence: demo screenshot/gif + test log + README line + one bullet. Concept tie-in: [[Graph Algorithms]], [[Minimum Spanning Trees]].
## 6. Overview pass without overload
Each day, after solving, spend a 25–45 min concept touch on the note matching today's pattern, using its `## Practice Map` section (create it if missing). Cap: one concept depth per day — section 4's table already sequences which concept each day.
## 7. Wiring
Daily row lives in [[Daily Operating System]]. Weekly LC total + weak-topic day handled in [[Weekly Operating System]].
## 8. Daily Log
Append one row per day. Redo date schedules spaced repetition for anything that needed a hint or felt shaky.
| Date | Count | Topics | Problem IDs | Company | 4041 concept | Difficulty | Redo date |
|------|:---:|--------|-------------|---------|--------------|------------|-----------|
| | | | | | | | |
### Weekly totals (target ≥35/week)
| Week of | Total solved | Weak topic flagged | Company drilled |
|---|:---:|---|---|
| 2026-07-28 | | | Google |
| 2026-08-04 | | | Amazon |
| 2026-08-11 | | | Meta |
| 2026-08-18 | | | Google |
| 2026-08-25 | | | Amazon |
### Pre-interview cram list
Pull every concept with mastery < 7 from §2, ordered by the target company's tag. Fill 48h before any interview.
- [ ]

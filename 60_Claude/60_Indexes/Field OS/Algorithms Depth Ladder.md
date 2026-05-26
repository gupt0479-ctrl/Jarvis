---
type: evergreen
status: tree
tags:
  - dashboard
  - capability
  - depth-ladder
created: 2026-04-25
updated: 2026-04-25
notes:
  - "[[Algorithms Field OS]]"
  - "[[Algorithms Question Bank]]"
  - "[[BOOM Board]]"
---
# Algorithms Depth Ladder

Modeled after the [[BOOM Board]]. Seeded from CSCI 4041 (algorithms) and CSCI 2041 (OCaml/functional programming). Refresher lists are hand-picked.

## Core Concepts

- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Algorithms/Dynamic Programming|Dynamic Programming]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Graphs/Graph Algorithms|Graph Algorithms]]
- [[QuickSort|QuickSort]]
- [[HeapSort|HeapSort]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Trees/AVL Trees|AVL Trees]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Data Structures & Methods/Hashing|Hashing]]
- [[OCaml - Pattern Matching]]
- [[Time Complexity]]

## Compare and Discriminate

| Concept A | Concept B | What to clarify |
|---|---|---|
| Dynamic programming | Greedy algorithms | DP explores all subproblems and picks the optimal; greedy commits locally and never backtracks. DP guarantees optimality when subproblems overlap; greedy only works when the greedy choice property holds. |
| QuickSort | HeapSort | QuickSort is faster in practice (cache-friendly, low constant factors) but O(n²) worst case. HeapSort is O(n log n) guaranteed but slower in practice due to poor cache behavior. |
| AVL Trees | B-Trees | AVL trees optimize for in-memory lookup with strict balance. B-Trees optimize for disk I/O by packing many keys per node. Different hardware constraints, different tree shapes. |
| OCaml pattern matching | If-else chains | Pattern matching is exhaustive — the compiler tells you if you missed a case. If-else chains are not. Pattern matching also destructures data, which if-else can't do. |

## 30-Minute Refresher

1. [[Time Complexity]]
2. [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Algorithms/Dynamic Programming|Dynamic Programming]]
3. [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Graphs/Graph Algorithms|Graph Algorithms]]

## 2-Hour Technical Refresher

1. [[Time Complexity]]
2. [[Sorting Algorithms|Sorting Algorithms]]
3. [[QuickSort|QuickSort]]
4. [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Algorithms/Dynamic Programming|Dynamic Programming]]
5. [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Graphs/Graph Algorithms|Graph Algorithms]]
6. [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Trees/AVL Trees|AVL Trees]]
7. [[OCaml - Pattern Matching]]

## Deep Relearning Pass

Start at [[CSCI 4041 Board]] and work through weekly notes in order. Then revisit [[CSCI 2041 Board]] for OCaml foundations. The textbook notes under `10_UMN/CSCI 4041/Textbook/` have the formal definitions.

## Overdue Drills

```dataview
TABLE mastery_level, difficulty, next_drill, drill_interval
FROM ""
WHERE type = "concept" AND contains(track, "algorithms") AND next_drill AND next_drill < date(today)
SORT next_drill ASC
```

## All Tracked Algorithms Concepts

```dataview
TABLE mastery_level, difficulty, status, next_drill
FROM ""
WHERE type = "concept" AND contains(track, "algorithms")
SORT file.name ASC
```

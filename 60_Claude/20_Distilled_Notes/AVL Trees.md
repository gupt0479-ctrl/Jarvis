---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
notes:
  - "[[10_UMN/CSCI 4041/Concepts/Trees/AVL Trees]]"
  - "[[10_UMN/CSCI 4041/Concepts/Trees/B-Trees]]"
track:
  - algorithms
prerequisites:
  - "[[10_UMN/CSCI 4041/Concepts/Data Structures & Methods/Elementary Data
    Structures]]"
  - "[[10_UMN/CSCI 4041/Concepts/Time Complexity]]"
used_in: []
evidence: []
difficulty: 3
mastery_level: novice
drill_interval: 10
last_drilled: 2026-04-25
next_drill: 2026-05-05
---

# AVL Trees

> Distilled from [[10_UMN/CSCI 4041/Concepts/Trees/AVL Trees|CSCI 4041 — AVL Trees]]

## Deep Dive

### One-Sentence Version

AVL trees are BSTs that maintain logarithmic height by requiring left and right subtree heights to differ by at most 1 at every node, using rotations to restore balance after insertions and deletions.

### What It Is

A self-balancing binary search tree where:
- **Balance factor** = `left_height - right_height`, must be in `{-1, 0, 1}`
- **Rotations** are local pointer rewirings that preserve BST order while improving shape
- **Four cases**: LL (right rotate), RR (left rotate), LR (left-rotate child then right-rotate), RL (right-rotate child then left-rotate)
- **Height bound**: minimum nodes for height h follows `N_h = N_{h-1} + N_{h-2} + 1`, a Fibonacci-like recurrence that proves logarithmic height

### Why It Matters

Plain BSTs degenerate to linked lists on sorted input. AVL trees guarantee `O(log n)` for search, insert, and delete regardless of insertion order. Understanding rotations and balance invariants is foundational for all balanced tree structures (red-black trees, B-trees, treaps).

### Real Example

Insert `[30, 10, 20]` into an empty AVL tree. After inserting 20, the root (30) has balance factor 2 and its left child (10) has balance factor -1. This is the LR case: left-rotate the child (10) to get `[30, 20, 10]`, then right-rotate the root (30) to get `[20, 10, 30]`. The double rotation handles the "bend" where the heavy side goes inward.

### Contrast With

- **AVL vs red-black trees**: AVL trees are more tightly balanced (stricter height bound), which means faster lookups but more rotations on updates. Red-black trees allow slightly more imbalance for cheaper updates.
- **AVL vs plain BST**: Plain BSTs have no balance guarantee. On sorted input, a plain BST becomes a chain with `O(n)` operations. AVL guarantees `O(log n)`.
- **Stored height vs recomputed balance factor**: AVL implementations store height per node for efficiency, but debugging requires recomputing balance factors from scratch — stored heights can be stale after buggy rotations.

### Source Anchors

- [[10_UMN/CSCI 4041/Concepts/Trees/AVL Trees]] — full lecture notes with rotation code and trigger sequences
- [[10_UMN/CSCI 4041/Textbook/Chapter - 13]] — CLRS rotation machinery
- [[10_UMN/CSCI 4041/Week - 6]], [[10_UMN/CSCI 4041/Week - 7]] — lecture coverage

## Four Rotation Cases

| Case | Condition | Repair |
|---|---|---|
| LL | `bf(x) == 2` and `bf(x.left) >= 0` | right_rotate(x) |
| RR | `bf(x) == -2` and `bf(x.right) <= 0` | left_rotate(x) |
| LR | `bf(x) == 2` and `bf(x.left) < 0` | left_rotate(x.left) then right_rotate(x) |
| RL | `bf(x) == -2` and `bf(x.right) > 0` | right_rotate(x.right) then left_rotate(x) |

## Diagnostic Questions

- Why does AVL need a height field rather than just checking children?
- How do you distinguish LR from LL once you know a node is left-heavy?
- Why does the Fibonacci-style recurrence imply logarithmic height?
- Why are parent-pointer checks separate from BST-order checks during debugging?

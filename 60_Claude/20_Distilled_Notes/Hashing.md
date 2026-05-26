---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
notes:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Data Structures & Methods/Hashing]]"
track:
  - algorithms
prerequisites:
  - "[[Elementary Data Structures]]"
used_in: []
evidence: []
difficulty: 3
mastery_level: novice
drill_interval: 10
last_drilled: 2026-04-25
next_drill: 2026-05-05
---

# Hashing

> Distilled from [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Data Structures & Methods/Hashing|CSCI 4041 — Hashing]]

## Deep Dive

### One-Sentence Version

Hashing maps a large key universe into a small table of slots, achieving expected constant-time operations when collisions are controlled.

### What It Is

A hash table uses a hash function to compute slot indices from keys. Collisions (two keys mapping to the same slot) are inevitable and handled by either:
- **Chaining**: each slot stores a linked list, expected search `Θ(1+α)` where `α = n/m`
- **Open addressing**: everything stays in the table, probe sequences find empty slots, load factor cannot exceed 1

The quality of the hash function is part of the algorithmic guarantee, not just an implementation detail.

### Why It Matters

Hash tables are the most-used data structure in practice. Every language has them (Python dicts, Java HashMaps, Rust HashMaps). Understanding load factor, collision handling, and deletion semantics separates someone who uses hash tables from someone who understands them. Interview problems frequently test this distinction.

### Real Example

Linear probing creates primary clustering: consecutive occupied slots form long runs, and future insertions are more likely to extend those runs. That feedback loop degrades performance. Double hashing fixes this by varying the step size per key, so different keys explore the table differently. The lecture's empirical histograms show this visually — linear probing clusters while double hashing stays closer to the ideal random model.

### Contrast With

- **Chaining vs open addressing**: Chaining allows `α > 1` and handles deletion naturally. Open addressing has better cache locality but deletion requires tombstones or backward-shift repair because blanking a slot can make later keys unreachable.
- **Hash table vs balanced BST**: Hash tables give expected `O(1)` but worst-case `O(n)`. Balanced BSTs give worst-case `O(log n)`. Hash tables win on average; BSTs win on guarantees and ordered operations.
- **Division vs multiplication vs universal hashing**: Division is simple but sensitive to table-size choice. Multiplication spreads arithmetic patterns better. Universal hashing protects against adversarial inputs by randomly choosing from a hash family.

### Source Anchors

- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Data Structures & Methods/Hashing]] — full lecture notes with chaining and probing code
- [[Chapter - 11]] — CLRS hash tables and open addressing
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 8]] — lecture coverage

## Complexity

| Method | Average search | Worst search | Key tradeoff |
|---|---|---|---|
| Chaining | `Θ(1+α)` | `Θ(n)` | simple collision handling, `α` can exceed 1 |
| Open addressing | near constant when sparse | `Θ(n)` | better locality, trickier deletion |

## Diagnostic Questions

- Why is hashing an average-case story rather than a worst-case guarantee?
- What role does load factor play in chaining performance?
- Why is deletion harder in open addressing than in chaining?
- What is primary clustering and why does it degrade linear probing?

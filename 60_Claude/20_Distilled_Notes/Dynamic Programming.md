---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
notes:
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming]]"
  - "[[Greedy Algorithms]]"
  - "[[Divide and Conquer]]"
track:
  - algorithms
prerequisites:
  - "[[Time Complexity]]"
  - "[[Divide and Conquer]]"
used_in: []
evidence: []
difficulty: 4
mastery_level: novice
drill_interval: 7
last_drilled: 2026-04-25
next_drill: 2026-05-02
---

# Dynamic Programming

> Distilled from [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming|CSCI 4041 — Dynamic Programming]]

## Deep Dive

### One-Sentence Version

Dynamic programming solves problems by solving overlapping subproblems once each and storing the answers, turning exponential recursion into polynomial table-filling.

### What It Is

A problem-solving technique that applies when two conditions hold:
1. **Optimal substructure** — an optimal solution contains optimal solutions to its subproblems
2. **Overlapping subproblems** — the recursion revisits the same subproblems repeatedly

Two implementation strategies:
- **Memoization** (top-down): recurse normally but cache results
- **Bottom-up**: fill a table from smallest subproblems upward

### Why It Matters

DP is the most common algorithmic technique in technical interviews after basic data structures. It also appears in real systems: sequence alignment in bioinformatics, shortest paths in networks, resource allocation in scheduling. The hard part is not the code — it is defining the subproblem state correctly.

### Real Example

Naive Fibonacci computes `F(2)` exponentially many times. Memoized Fibonacci stores each value once and runs in `Θ(n)`. Bottom-up Fibonacci with two variables runs in `Θ(n)` time and `O(1)` space. The 0-1 knapsack problem shows why DP matters more: greedy fails because locally attractive items can block globally optimal combinations. The DP table `dp[k][slack]` systematically preserves the optimal answer.

### Contrast With

- **Divide and conquer** splits into independent subproblems that don't overlap. DP handles overlapping subproblems by caching.
- **Greedy algorithms** make locally optimal choices without reconsidering. DP considers all subproblem combinations. Greedy works for fractional knapsack but fails for 0-1 knapsack.
- **Brute force** checks all possibilities. DP prunes by recognizing that many possibilities share the same subproblem answers.

### Source Anchors

- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming]] — full lecture notes with code
- [[Chapter - 14]] — CLRS rod cutting, LCS, matrix chain, optimal BST
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 9]] — lecture coverage

## Key Recurrences

| Problem | Recurrence | Time |
|---|---|---|
| Rod cutting | `r_n = max(p_i + r_{n-i})` | `Θ(n²)` |
| LCS | match → `c[i-1,j-1]+1`, else → `max(c[i-1,j], c[i,j-1])` | `Θ(mn)` |
| 0-1 Knapsack | `dp[k][w] = max(dp[k-1][w], dp[k-1][w-s_k] + v_k)` | `O(NM)` |
| Fibonacci | `F(n) = F(n-1) + F(n-2)` | `Θ(n)` memoized |

## DP Design Checklist

1. Define the subproblem state
2. Write the recurrence
3. Identify base cases
4. Decide memoized top-down or bottom-up order
5. If needed, store reconstruction data

## Diagnostic Questions

- What are the two hallmarks that distinguish a DP problem from divide-and-conquer?
- Why is naive Fibonacci exponential when the recurrence looks linear?
- Why does greedy fail for general 0-1 knapsack?
- How does the `best` reconstruction table in knapsack recover the actual items?

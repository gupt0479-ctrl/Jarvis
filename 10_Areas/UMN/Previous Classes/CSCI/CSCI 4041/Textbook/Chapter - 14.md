---
type: class
input_kind: book
status: sprout
created: 2026-03-25
updated: 2026-04-28
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Textbook/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 8|Week - 8]]"
---
# Chapter 14 - Dynamic Programming
## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 9#Chapter 14 - Dynamic Programming, Fibonacci, and Knapsack|Week - 9]]
- [[Dynamic Programming#Definition|Dynamic Programming]]
- [[Divide and Conquer#Definition|Divide and Conquer]]

Dynamic programming, like divide-and-conquer, solves problems by combining the solutions to subproblems. The word **programming** refers to a tabular method, not computer code. Unlike [[Divide and Conquer#Definition|divide-and-conquer]], which partitions a problem into disjoint subproblems, dynamic programming is used when subproblems **overlap**. A dynamic-programming algorithm solves each subproblem exactly once and saves the result.

> [!NOTE] Dynamic programming is typically applied to **optimization problems**, where there can be many possible solutions, each with a value, and the goal is to find the optimal one.

## 14.1 Rod Cutting
Serling Enterprises cuts steel rods of length n into shorter rods to maximize revenue. Each piece of length i has a price $p_i$.

1. **Optimal Substructure**
	- To solve rod cutting for length n, choose an initial cut i and then solve the remaining rod of length n-i optimally.
	- This gives the standard recurrence
	$$
	r_n = \max_{1 \leq i \leq n}(p_i + r_{n-i}).
	$$

2. **Naive Recursion vs Dynamic Programming**
	- naive recursion is exponential because it recomputes the same subproblems repeatedly
	- memoization stores computed results
	- bottom-up order fills a table from small lengths to large lengths

3. **Subproblem Graphs**
	- a subproblem graph records which subproblems depend on which others
	- bottom-up corresponds to computing in a safe dependency order
	- top-down memoization corresponds to DFS plus caching

### Lecture Emphasis
The lecture used Joy's lumber formulation as the intuition pump. Instead of a pure textbook rod-cutting table, the notes framed the recurrence as "skip cut i" versus "use cut i and solve the remaining board." That is useful because it matches the later knapsack table logic much more closely than the terse textbook description does.

## 14.2 Matrix-Chain Multiplication
Given a chain of matrices $\langle A_1, A_2, \dots, A_n \rangle$, find the parenthesization that minimizes the number of scalar multiplications.

- If A is $p \times q$ and B is $q \times r$, then AB takes $pqr$ multiplications.
- Let `m[i,j]` be the minimum cost of multiplying $A_i \cdots A_j$.
- Then
$$
m[i,j] =
\begin{cases}
0 & \text{if } i=j \\
\min_{i \leq k < j}\{m[i,k] + m[k+1,j] + p_{i-1}p_kp_j\} & \text{if } i<j
\end{cases}
$$

The standard dynamic-programming solution runs in $Θ(n^3)$ time and $Θ(n^2)$ space.

## 14.3 Elements of Dynamic Programming
A problem is a good candidate for dynamic programming if it has two hallmarks:

1. **Optimal Substructure**
	- the optimal solution contains optimal solutions to subproblems
	- textbook proofs usually use a cut-and-paste contradiction

2. **Overlapping Subproblems**
	- the recursive formulation revisits the same subproblems many times
	- storing solutions converts exponential recomputation into polynomial or linear work

### Lecture Emphasis
The lecture contrasted dynamic programming directly with divide-and-conquer:
- divide-and-conquer tends to create new disjoint subproblems
- dynamic programming revisits the same states repeatedly
- the algorithmic gain comes from storing those repeated states instead of re-solving them

That contrast matters because many recursive problems are *not* dynamic programming. The overlap requirement is essential.

## 14.4 Longest Common Subsequence (LCS)
Given two sequences $X=\langle x_1, \dots, x_m \rangle$ and $Y=\langle y_1, \dots, y_n \rangle$, find the maximum-length common subsequence.

- If $x_i = y_j$, then
$$
c[i,j] = c[i-1,j-1] + 1
$$
- Otherwise
$$
c[i,j] = \max(c[i,j-1], c[i-1,j])
$$

The full DP table runs in $Θ(mn)$ time, with reconstruction handled by a direction table or by backtracking through the value table.

## 14.5 Optimal Binary Search Trees
If we know search probabilities for keys and dummy keys, we can build a BST minimizing expected search cost.

- The recurrence builds optimal roots over intervals of keys.
- The DP solution is cubic in the number of keys in the straightforward textbook form.
- This section matters more for learning the DP design pattern than for direct implementation in this course.

## Lecture Anchors: Fibonacci and Knapsack
The course used Chapter 14 mainly through two notebooks rather than through the full CLRS menu.

### Fibonacci Implementations
```python
def FibRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return FibRecursive(n - 2) + FibRecursive(n - 1)
```

```python
def FibMemoize(n):
    F = {0: 0, 1: 1}
    def FibMemR(n):
        if n in F:
            return F[n]
        A = FibMemR(n - 2)
        B = FibMemR(n - 1)
        F[n] = A + B
        return F[n]
    return FibMemR(n)
```

```python
def FibBottomUp(n):
    if n <= 1:
        return n
    A, B = 0, 1
    for i in range(2, n + 1):
        F = A + B
        A = B
        B = F
    return F
```

```python
def FibBottomUp2(n):
    F = [0] * (n + 2)
    F[1] = 1
    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]
```

These four versions show the whole DP story:
- naive recursion repeats work exponentially
- memoization keeps the recursive structure but caches results
- bottom-up avoids recursive overhead entirely
- table-preserving bottom-up keeps all intermediate values when reconstruction or full history matters

### Knapsack Notebook
The lecture also used the 0/1 knapsack problem.

```python
class item:
    def __init__(self, name, size, value):
        self.name = "x_" + str(name)
        self.size = size
        self.value = value
```

```python
def generate_item_set(N, M):
    ...
```

The core DP table-filling loop for 0-1 knapsack. For each item and each remaining capacity, compare "take this item" versus "skip this item" and store the better value:

```python
def knapsack_dp(Items, N, M):
    """0-1 knapsack DP table fill"""
    dp = [[0 for _ in range(M+1)] for _ in range(N)]
    best = [[None for _ in range(M+1)] for _ in range(N)]
    
    for k in range(N):
        for slack in range(M+1):
            skip = dp[k-1][slack] if k > 0 else 0
            take = 0
            if Items[k].size <= slack:
                prev = dp[k-1][slack - Items[k].size] if k > 0 else 0
                take = Items[k].value + prev
            if take > skip:
                dp[k][slack] = take
                best[k][slack] = k
            else:
                dp[k][slack] = skip
                best[k][slack] = best[k-1][slack] if k > 0 else None
    
    return dp, best
```

This is the missing piece between item generation and reconstruction. The `dp[k][slack]` cell stores the best value achievable using items `0..k` with capacity `slack`. The `best[k][slack]` cell stores which item was chosen, enabling `re_construct` to trace back the actual solution.

The main DP table idea was:
- `dp[k][slack]` = best value using items `0..k` with capacity `slack`
- compare **take** versus **skip**
- store the chosen index in `best[k][slack]` for reconstruction

```python
def re_construct(Items, best, M, N):
    slack = M
    result = []
    for row in range(N - 1, -1, -1):
        idx = best[row][slack]
        if idx is not None:
            x = Items[idx]
            if x not in result:
                result.append(x)
                slack -= x.size
    return result
```

### Greedy Failure Demo
The lecture emphasized that knapsack is a good DP example because a simple greedy rule can fail. Taking the locally best-looking feasible item may block a better combination of smaller items later. That is the exact kind of problem where dynamic programming is the right correction.

---

## Overview
- Chapter 14 introduces dynamic programming as the method for problems with optimal substructure and overlapping subproblems.
- In CSCI 4041, the textbook examples (rod cutting, matrix-chain multiplication, LCS, optimal BST) are paired with lecture code for Fibonacci and 0-1 knapsack.
- The main study goal is to learn how to design a state, recurrence, base cases, table order, and reconstruction method.

## Core Definitions
- **Optimal substructure:** an optimal solution contains optimal solutions to its subproblems.
- **Overlapping subproblems:** the same subproblems occur repeatedly in the naive recursion tree.
- **Memoization:** top-down recursion plus a cache.
- **Bottom-up DP:** fill a table in an order where each dependency has already been solved.
- **Reconstruction table:** extra choices/pointers that recover the actual solution, not just its value.

## Main Algorithms
- Rod cutting: naive recursion, memoized top-down, bottom-up, and extended bottom-up solution recovery.
- Matrix-chain multiplication: choose the split `k` that minimizes scalar multiplication cost.
- LCS: two-dimensional table over prefixes of the two sequences.
- Optimal BST: choose roots that minimize expected search cost.
- Lecture algorithms: naive Fibonacci, memoized Fibonacci, bottom-up Fibonacci, brute-force knapsack, DP knapsack, and reconstruction.

## Correctness Ideas
- The cut-and-paste argument proves optimal substructure: replacing a nonoptimal subproblem solution would improve the original solution.
- Memoization correctness follows from computing the same recurrence as the naive algorithm but caching each state once.
- Bottom-up correctness follows from table order: every recurrence dependency is already available.
- Reconstruction correctness depends on storing the choice that achieved the optimal value, not recomputing a possibly different tie later.

## Complexity
- Naive Fibonacci is exponential; memoized and bottom-up Fibonacci are `Theta(n)`.
- Rod cutting is `Theta(n^2)` after memoization/bottom-up conversion.
- Matrix-chain multiplication is `Theta(n^3)` time and `Theta(n^2)` space.
- LCS is `Theta(mn)` time and space.
- 0-1 knapsack DP in lecture is pseudo-polynomial: `O(NM)` for `N` items and capacity `M`.

## Lecture Emphasis
- `Lectures/Week - 9/ch14_DynamicProgramming(Fibonacci).ipynb` shows the whole DP arc: repeated recursion, memoization, and bottom-up compression.

```python
def FibBottomUp(n):
    if n==0: return 0
    if n==1: return 1
    A, B = 0, 1
    for i in range(2,n+1):
        F = A + B
        A, B = B, F
    return F
```

- `Lectures/Week - 9/Ch14_DynamicProgramming(Knapsack).ipynb` shows why brute force is bad and how the DP table over `(item index, slack)` preserves optimal choices.
- `Ch14_DynamicProgramming(Knapsack)-Testing.ipynb` includes `re_construct`, which maps directly to the textbook idea of extended DP tables.
- `Homework/Coding/CodingHW_6(chapter14-CLRS).ipynb` uses rod cutting with cut cost, rod-cut reconstruction, and LCS reconstruction.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 9|Week - 9]], [[Dynamic Programming|Dynamic Programming]], [[Greedy Algorithms|Greedy Algorithms]].

## Examples
- Rod cutting: `r_n = max_{1 <= i <= n}(p_i + r_{n-i})`.
- LCS: if the last characters match, extend the diagonal subproblem; otherwise take the max of dropping one character from either sequence.
- Knapsack: for each item and remaining capacity, compare "take item plus best leftover" against "skip item."

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 9|Week - 9]]
- [[Dynamic Programming|Dynamic Programming]]
- [[Greedy Algorithms|Greedy Algorithms]]
- Source homework read: `Homework/Coding/CodingHW_6(chapter14-CLRS).ipynb` and `Homework/Paper/Paper HW - 6 (Ch - 14).pdf`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Calling any recursive algorithm "dynamic programming" without overlapping subproblems and storage.
- Forgetting to define the subproblem before writing the recurrence.
- Filling a table in an order that uses uninitialized states.
- Returning only the optimal value when the task asks for the actual solution.
- Treating pseudo-polynomial knapsack time as polynomial in the bit-length of the input.

## Review Checklist
- [ ] Identify optimal substructure and overlapping subproblems.
- [ ] Write states, recurrence, base cases, and fill order.
- [ ] Convert a naive recurrence to memoized and bottom-up forms.
- [ ] Reconstruct a solution from stored choices.
- [ ] Analyze DP time and space from table dimensions and per-cell work.

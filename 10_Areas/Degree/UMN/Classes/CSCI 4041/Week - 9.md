---
type: class
input_kind: lecture
status: seed
created: 2026-03-25
updated: 2026-04-16
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Chapter - 14]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Introduction to Algorithms|Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Lecture"
next: []
---
# Entire Week
## What you must be able to do
- [[Chapter - 14#14.1 Rod Cutting|Chapter - 14 rod cutting]], [[Chapter - 14#14.3 Elements of Dynamic Programming|elements of dynamic programming]], and [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Definition|Dynamic Programming]]: explain optimal substructure, overlapping subproblems, memoization, and bottom-up table construction.
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Core Ideas (Lecture)|Dynamic Programming - Core Ideas (Lecture)]], [[Chapter - 14#Lecture Anchors: Fibonacci and Knapsack|lecture anchors]], and [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Complexity + Tradeoffs|Dynamic Programming - Complexity + Tradeoffs]]: compare the four Fibonacci implementations and explain why knapsack needs DP rather than a simple greedy rule.
- [[Chapter - 14#14.4 Longest Common Subsequence (LCS)|LCS]] and [[Chapter - 14#14.5 Optimal Binary Search Trees|optimal BST]]: know the broader chapter recurrence patterns even though the lecture focus is on Fibonacci and knapsack.
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Practice Map|Dynamic Programming - Practice Map]]: 1D DP, 2D DP, and reconstruction-style practice are still open.

## Key ideas (textbook)
- **Dynamic programming is about repeated states, not just recursion.** A recursive problem becomes a DP problem when the same subproblems appear again and again and can be stored instead of recomputed.
- **Optimal substructure is the proof side of DP.** The standard cut-and-paste argument says an optimal whole solution must contain optimal subproblem solutions, otherwise replacing a bad subsolution would improve the whole.
- **Memoization and bottom-up tabulation solve the same state graph in different orders.** Top-down explores only reachable states through recursion, while bottom-up chooses an explicit dependency order and fills the table iteratively.
- **State design matters more than syntax.** The hardest part of DP is choosing what each table entry means, what its transition cases are, and which base cases anchor the recurrence.
- **Reconstruction is a separate design choice.** Getting the optimal value is one problem; recovering the chosen items or chosen sequence is another, which is why many DP solutions store an additional decision table.

## Concepts created / updated today
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Definition|Dynamic Programming]]
- [[Chapter - 14#Lecture Anchors: Fibonacci and Knapsack|Chapter - 14 - lecture anchors]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Canonical Examples (Max 5)|Dynamic Programming - Canonical Examples]]

## Lecture
### Chapter 14 - Dynamic Programming, Fibonacci, and Knapsack
This week translated the chapter's abstract DP language into two concrete case studies: Fibonacci and 0/1 knapsack. The lecture kept the contrast with divide-and-conquer front and center. Divide-and-conquer works well when subproblems are disjoint, but Fibonacci is the perfect counterexample because the recursion tree repeats the same small values many times. That is why the naive recursive implementation explodes even though the recurrence itself is simple. The moment those repeated states are stored, the problem changes character completely: exponential repetition becomes linear state computation.

The Fibonacci notebooks were useful because they gave four versions of the same recurrence and made the tradeoffs visible. `FibRecursive` shows the bad behavior clearly, `FibMemoize` keeps the recursive structure but saves answers in a dictionary, `FibBottomUp` uses only two variables for the minimum memory version, and `FibBottomUp2` keeps the full table when the intermediate values themselves matter. The lecture's timing comparisons at n=35 and n=5000 are worth remembering because they connect the asymptotic story to real runtime differences and to Python's recursion limit.

Knapsack then extended the same DP ideas into table design. The lecture started with an item class and a random item generator, then compared brute force, greedy, and DP. The greedy counterexample is important because it motivates the table instead of making it feel like overkill. Once greedy fails, the DP state `dp[k][slack]` becomes natural: it means "best value available using items up to row k with this remaining capacity." The reconstruction routine is equally important because it shows how DP solutions often need two structures: one for the optimal value and one for how that value was achieved. Even though the textbook chapter also covers rod cutting, matrix-chain multiplication, LCS, and optimal BSTs, the lecture's main transferable skill this week was state design and transition reasoning.

### Jupyter Notebook Explanations
#### ch14_DynamicProgramming(Fibonacci).ipynb
This notebook compares four ways to compute the same recurrence.

```python
def FibRecursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return FibRecursive(n - 2) + FibRecursive(n - 1)
```

This is the pure recursive definition, and the notebook uses it to show how much repeated work is hidden inside a short function. The lecture specifically pointed out that `FibRecursive(8)` computes `F(2)` many times, which is why the recursion tree grows so fast.

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

Memoization is the first real dynamic-programming version because it turns repeated recursive states into one-time computations.

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

This version is important because it proves that once the dependency order is known, recursion is not required. It also uses only constant extra space.

#### Ch14_DynamicProgramming(Knapsack).ipynb
This notebook provides the more substantial DP example.

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

The lecture used these helpers to generate item sets and then compare brute force, greedy, and DP behavior on the same style of inputs.

The core DP meaning is:
- `dp[k][slack]` = best value using items `0..k` with capacity `slack`
- choice = max(take, skip)

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

This reconstruction routine is the second half of the DP story. The value table alone is not enough when you also need the chosen items.

#### Ch14_DynamicProgramming(Knapsack)-Testing.ipynb
This notebook reinforced three practical ideas:
- brute force becomes too slow quickly
- greedy may return a feasible but suboptimal solution
- the DP table gives a reliable optimum as long as the state definition is correct

## Examples worth keeping
- **Naive Fibonacci:** repeated calls like `F(2)` appearing multiple times in the recursion tree.
- **Memoized Fibonacci:** same recurrence, but each n is solved once and then cached.
- **Bottom-up Fibonacci:** constant-space version using only the last two values.
- **Greedy knapsack failure:** a locally best item can block a better total combination of smaller items.
- **Knapsack reconstruction:** the optimal value and the chosen item set are related but distinct outputs.

## Takeaways (questions to resolve)
- [ ] What exactly makes a recursive problem a DP problem instead of just divide-and-conquer?
- [ ] Why is memoization still top-down DP even though it looks recursive?
- [ ] What does the state `dp[k][slack]` mean in plain English?
- [ ] Why can greedy fail even when every individual greedy step looks reasonable?
- [ ] When do you need a separate reconstruction table instead of only a value table?

## Flashcards
#cards/CSCI4041
1. Two hallmarks of dynamic programming::Optimal substructure and overlapping subproblems.
2. Why is naive Fibonacci exponential::Because the recursion repeatedly solves the same subproblems.
3. What is memoization::Top-down recursion plus a cache of solved subproblems.
4. What is bottom-up DP::Solve states in dependency order and store results iteratively.
5. Knapsack state meaning::`dp[k][slack]` is the best value using items up to k with remaining capacity slack.
6. Why can greedy fail for 0/1 knapsack::A locally best item choice can block a better global combination.
7. Why store reconstruction information::Because the optimal value does not automatically tell you which choices produced it.

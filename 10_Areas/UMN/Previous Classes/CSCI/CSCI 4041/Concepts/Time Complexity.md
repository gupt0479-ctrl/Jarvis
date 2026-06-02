---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 0
created: 2026-02-01
topics:
  - "[[CSCI 4041 Board]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Concepts/Introduction to Algorithms]]"
  - "[[DSA]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 1 & 2|Week - 1 & 2]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 3|Week - 3]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 3 & 4]]"
related:
  - "[[DSA]]"
---
# Time Complexity Boxes
## MOC
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 1 & 2#Key ideas (textbook)|Week - 1 & 2]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#2.2 Analyzing Algorithms|Chapter - 1 & 2 - Analyzing Algorithms]]
- [[Sorting Algorithms#Complexity + Tradeoffs|Sorting Algorithms - Complexity + Tradeoffs]]
- [[Graph Algorithms#Complexity + Tradeoffs|Graph Algorithms - Complexity + Tradeoffs]]

## Definition
- **Time complexity** measures how the amount of work grows as the input size grows.
- **Space complexity** measures how extra memory usage grows.
- In this course, asymptotic notation is used to describe eventual growth rather than exact timing on one machine.

## Foundation Box
### Asymptotic Notation
> [!summary]
> - **O(g(n))**: eventual upper bound
> - **Ω(g(n))**: eventual lower bound
> - **Θ(g(n))**: tight bound up to constant factors

## Core Ideas (Textbook)
### Formal Asymptotic Definitions
- **$O(g(n))$**: $\exists\, c > 0,\, n_0 > 0$ such that $0 \leq f(n) \leq c \cdot g(n)$ for all $n \geq n_0$. Upper bound.
- **$\Omega(g(n))$**: $\exists\, c > 0,\, n_0 > 0$ such that $0 \leq c \cdot g(n) \leq f(n)$ for all $n \geq n_0$. Lower bound.
- **$\Theta(g(n))$**: $\exists\, c_1, c_2 > 0,\, n_0 > 0$ such that $c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$ for all $n \geq n_0$. Tight bound.
- **Theorem**: $f(n) = \Theta(g(n))$ if and only if $f(n) = O(g(n))$ and $f(n) = \Omega(g(n))$.
- **$o(g(n))$**: for all $c > 0$, $\exists\, n_0$ such that $0 \leq f(n) < c \cdot g(n)$ for all $n \geq n_0$. Strict upper bound.
- **$\omega(g(n))$**: for all $c > 0$, $\exists\, n_0$ such that $0 \leq c \cdot g(n) < f(n)$ for all $n \geq n_0$. Strict lower bound.

### Master Method (CLRS Ch 4.5)
For recurrences of the form $T(n) = aT(n/b) + f(n)$ where $a \geq 1$, $b > 1$:
- **Watershed function**: $n^{\log_b a}$.
- **Case 1**: $f(n) = O(n^{\log_b a - \epsilon})$ for some $\epsilon > 0$ → $T(n) = \Theta(n^{\log_b a})$. Leaf work dominates.
- **Case 2**: $f(n) = \Theta(n^{\log_b a} \lg^k n)$ for $k \geq 0$ → $T(n) = \Theta(n^{\log_b a} \lg^{k+1} n)$. Work is evenly spread.
- **Case 3**: $f(n) = \Omega(n^{\log_b a + \epsilon})$ for some $\epsilon > 0$ and $af(n/b) \leq cf(n)$ for some $c < 1$ → $T(n) = \Theta(f(n))$. Root work dominates.

### Recursion Tree Method
1. Expand the recurrence level by level.
2. At depth $k$: subproblem size is $n/b^k$, number of subproblems is $a^k$.
3. Cost per level = $a^k \cdot f(n/b^k)$.
4. Base case at depth $\log_b n$, giving $a^{\log_b n} = n^{\log_b a}$ leaves.
5. Sum all levels to get the total cost, then verify with substitution.

### Substitution Method
1. Guess the form of the solution (often informed by a recursion tree).
2. Assume the bound holds for all inputs smaller than $n$.
3. Substitute into the recurrence and simplify.
4. Pick constants so the inequality closes.
5. If induction fails, strengthen the hypothesis by subtracting a lower-order term.

## Complexity Reference Boxes
### [[50_Archive/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 1 & 2#Getting Started|Chapter - 1 & 2]]
### Linear Search
> [!summary] Linear Search
> - Best case: $Θ(1)$
> - Worst / average: $Θ(n)$
> - Extra space: $O(1)$

### Insertion Sort
> [!summary] Insertion Sort
> - Best case: $Θ(n)$
> - Worst / average: $Θ(n^2)$
> - Extra space: $O(1)$ for the in-place version

### Merge Sort
> [!summary] Merge Sort
> - Recurrence: $T(n)=2T(n/2)+Θ(n)$
> - All cases: $Θ(n \log n)$
> - Extra space: $Θ(n)$ in the lecture's list-based implementations

## [[QuickSort#Complexity + Tradeoffs|QuickSort]]
### QuickSort
> [!summary] QuickSort
> - Best / average: $Θ(n \log n)$
> - Worst: $Θ(n^2)$
> - Extra space: recursion stack, typically $O(\log n)$ on average

## [[HeapSort#Complexity + Tradeoffs|HeapSort]]
### Heap Operations
> [!summary] Heap Basics
> - `MAX-HEAPIFY`: $O(\log n)$
> - `BUILD-MAX-HEAP`: $O(n)$
> - `HEAPSORT`: $O(n \log n)$
> - Extra space: $O(1)$ auxiliary

## [[Hashing#Complexity + Tradeoffs|Hashing]]
### Hash Tables
> [!summary] Hashing
> - Chaining average search: $Θ(1 + α)$
> - Open addressing average search: near constant when $α$ is small
> - Worst case: $Θ(n)$

## [[Dynamic Programming#Complexity + Tradeoffs|Dynamic Programming]]
### Dynamic Programming
> [!summary] Common DP Patterns
> - Fibonacci memoized: $Θ(n)$
> - Fibonacci bottom-up: $Θ(n)$
> - Knapsack: $O(NM)$
> - LCS: $Θ(mn)$

## [[Graph Algorithms#Complexity + Tradeoffs|Graph Algorithms]]
### Graph Traversals
> [!summary] BFS / DFS
> - BFS: $O(V + E)$
> - DFS: $O(V + E)$
> - Topological sort: $O(V + E)$
> - SCC (Kosaraju-style two-pass): $O(V + E)$

## [[Minimum Spanning Trees#Complexity + Tradeoffs|Minimum Spanning Trees]]
### MST
> [!summary] MST
> - Kruskal: dominated by edge sorting, usually $O(E \log E)$
> - Prim with heap: $O(E \log V)$

## Core Ideas (Lecture)
### Cost-Counting Pattern from FLOPS Notebook
The [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 1 & 2#ch2_Asymptotic_Analysis-FLOPS.ipynb|FLOPS notebook]] is really a cost-model notebook. It instruments sorting algorithms with explicit `cost` counters to make asymptotic predictions concrete.

The key insight is in `insertion_sort_python_cost`, where the professor toggles between two cost models using comments:

```python
def insertion_sort_python_cost(A,n):
    """sorts the array A (in-place) using the insertion sort algorithm from CLRS-ch2"""
    cost = 0

    for i in range(1,n):
        key = A.pop(i)               # pop current element
        cost += 1       # this is the cost for link-based structures
        #cost += n-i    # this is the cost for array-based structures

        j = i-1
        cost += 1

        while j>=0 and A[j]>key:    # walk back to find insertion point
            j = j-1                 # move back
            cost += 1

        A.insert(j+1,key)           # insert ith element (key) into position j+1
        cost += 1        # this is the cost for link-based -O(1)
        #cost += n-(j+1) # this is the cost for array-based -O(length)

    return A,cost
```

The commented-out lines are the lecture's real point. The same high-level algorithm has different concrete costs depending on the underlying data structure:
- **Link-based**: `pop` and `insert` are $O(1)$ local pointer operations, so the dominant cost is the backward scan.
- **Array-based**: `pop` costs $O(n-i)$ and `insert` costs $O(n-(j+1))$ because elements must shift.

This distinction matters because asymptotic analysis describes the algorithm, but the data structure determines the constant factors and sometimes even the growth rate of the actual implementation.

### Empirical FLOPS Comparison
The notebook runs all four sorting variants on $n = 10{,}000$ random integers and reports FLOP counts:
- CLRS insertion sort: ~50M FLOPs (quadratic, counts every shift)
- Python insertion sort (link-based cost): ~25M FLOPs (quadratic, but fewer counted operations)
- Merge sort (CLRS): ~594K FLOPs ($n \lg n$ regime)
- Merge sort (list-based): ~554K FLOPs ($n \lg n$ regime)

The gap between insertion sort variants and merge sort variants is the empirical confirmation of $\Theta(n^2)$ vs $\Theta(n \lg n)$.

## Proof / Reasoning Toolkit
### Asymptotic Proof Checklist
1. State the claim: $f(n) = O(g(n))$, $\Omega(g(n))$, or $\Theta(g(n))$.
2. Exhibit explicit constants $c$ (and $c_1, c_2$ for $\Theta$) and threshold $n_0$.
3. Show the inequality holds for all $n \geq n_0$.
4. For $\Theta$, prove both directions separately or use the equivalence theorem.

### Master Method Checklist
1. Identify $a$, $b$, and $f(n)$ from the recurrence.
2. Compute the watershed function $n^{\log_b a}$.
3. Compare $f(n)$ against the watershed polynomially (not just by constants).
4. Apply the matching case, or recognize when the gap is not polynomial and the method does not apply.

### Recursion Tree Checklist
1. Compute the subproblem size at depth $k$.
2. Count how many subproblems appear at that level.
3. Multiply "number of subproblems" by "cost per subproblem."
4. Sum over levels and simplify asymptotically.
5. Use the result as a guess for the substitution method.

### Cost-Model Checklist
1. Say what one unit of "cost" means.
2. Identify which operations depend on the data structure rather than just the high-level algorithm.
3. Count the dominant repeated work instead of only describing the code informally.

## Practice Map
- [[Sorting Algorithms#Practice Map|Sorting Algorithms - Practice Map]]: insertion sort and merge sort cost analysis
- [[Divide and Conquer#Practice Map|Divide and Conquer - Practice Map]]: Master Method and substitution exercises
- Paper HW - 1 (Ch - 2).pdf: written problems on asymptotic notation and insertion sort analysis
- Paper HW - 2 (Ch - 3 & 4).pdf: written problems on asymptotic notation, recurrences, and Master Method
- CodingHW_1(chapter2-CLRS).ipynb: empirical cost comparison of sorting variants

## Mini-test (answer without looking)
- [ ] Can I state the formal definition of $O$, $\Omega$, and $\Theta$ with quantifiers?
- [ ] Can I apply the Master Method to $T(n) = 4T(n/2) + n$ and identify the correct case?
- [ ] Can I explain why `BUILD-MAX-HEAP` is linear?
- [ ] Can I distinguish average-case hash performance from worst-case?
- [ ] Can I identify when a recurrence should solve to linear, logarithmic, or $n \log n$ growth?
- [ ] Can I explain the difference between link-based and array-based cost in `insertion_sort_python_cost`?
- [ ] Can I draw a recursion tree for $T(n) = 2T(n/2) + n$ and sum the levels?

## Flashcards
#cards/CSCI4041
1. What does Θ mean::A tight asymptotic bound up to constant factors.
2. Merge-sort time::$Θ(n \log n)$.
3. Quicksort worst case::$Θ(n^2)$.
4. Build-max-heap time::$O(n)$.
5. BFS / DFS time::$O(V + E)$.
6. Knapsack DP time::$O(NM)$.
7. Hashing worst-case search::$Θ(n)$ even though average behavior is much better.
8. Master Method Case 1::$f(n)$ polynomially smaller than watershed → $T(n) = Θ(n^{\log_b a})$.
9. Master Method Case 3::$f(n)$ polynomially larger with regularity → $T(n) = Θ(f(n))$.
10. Substitution method::Guess the form, prove by induction, strengthen if needed.
11. Link-based vs array-based cost::Same algorithm, different operation costs depending on the data structure.
12. Recursion tree height for $T(n) = aT(n/b) + f(n)$::$\log_b n$ levels.
13. Formal $O$ definition::$\exists\, c > 0,\, n_0 > 0$ such that $0 \leq f(n) \leq c \cdot g(n)$ for all $n \geq n_0$.

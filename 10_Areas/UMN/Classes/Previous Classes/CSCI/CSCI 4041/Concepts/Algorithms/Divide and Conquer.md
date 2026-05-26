---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 5
created: 2026-02-08
topics:
  - "[[CSCI 4041 Board]]"
  - "[[Introduction to Algorithms]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 3 & 4]]"
related:
  - "[[Sorting Algorithms]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Dynamic Programming|Dynamic Programming]]"
---
# [[Divide and Conquer]]
## MOC
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 3#Chapter - 4 Divide & Conquer Algorithms (DnC)|Week - 3]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 3 & 4#4.0 Introduction to Divide-and-Conquer and Recurrences|Chapter - 3 & 4 - Recurrences]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Textbook/Chapter - 3 & 4#4.2 Strassen’s Algorithm|Chapter - 3 & 4 - Strassen]]
- [[Sorting Algorithms#Definition|Sorting Algorithms]]
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Concepts/Algorithms/Dynamic Programming#Definition|Dynamic Programming]]

## Definition
- **Divide-and-conquer**: recursively break a problem into smaller instances of the same problem, solve them, and combine the results.
- **Recurrence**: an equation that defines `T(n)` in terms of smaller inputs such as `T(n/2)`.
- **Master Method**: a standard method for solving recurrences of the form `T(n) = aT(n/b) + f(n)`.
- **Strassen's Algorithm**: a matrix-multiplication algorithm that reduces the number of recursive multiplications from 8 to 7.
- **Block matrix**: a matrix partitioned into smaller submatrices that can be processed recursively.

## Core Ideas (Textbook)
### Chapter 3 - Asymptotic Notation
- `O(g(n))` is an asymptotic upper bound, `Omega(g(n))` is an asymptotic lower bound, and `Theta(g(n))` is a tight bound.
- The formal definitions use explicit constants and an input threshold `n_0`.
- The theorem `f = Theta(g)` iff `f = O(g)` and `f = Omega(g)` is the main bridge between upper and lower bounds.

### 4.0 Recurrences
- Recursive algorithms are analyzed by recurrences with base cases and recursive cases.
- Floors and ceilings are often omitted because they do not change the order of growth.
- If a recurrence is stated as an upper-bound inequality, solve in `O`; if lower-bound, solve in `Omega`.

### 4.1 Matrix Multiplication
- Straightforward matrix multiplication is `Theta(n^3)`.
- Recursive 8-way block multiplication gives `T(n) = 8T(n/2) + Theta(n^2)` and is still `Theta(n^3)`.

### 4.2 Strassen's Algorithm
- Divide matrices into four `n/2 x n/2` blocks.
- Form 10 helper sums `S_1 ... S_10`.
- Recursively compute 7 products `P_1 ... P_7`.
- Combine them into the four output blocks.
- Recurrence: `T(n) = 7T(n/2) + Theta(n^2) = Theta(n^{log_2 7})`.

### 4.3 Substitution Method
- Guess the form of the solution.
- Prove it by induction.
- If the induction fails, strengthen the hypothesis by subtracting a lower-order term.

### 4.4 Recursion Trees
- Model cost level by level.
- Use the tree to guess a solution before writing a substitution proof.

### 4.5 Master Method
- Compare `f(n)` against the watershed function `n^{log_b a}`.
- Case 1: `f(n)` is polynomially smaller.
- Case 2: `f(n)` matches the watershed function up to polylog factors.
- Case 3: `f(n)` is polynomially larger and satisfies regularity.

## Core Ideas (Lecture)
### Recursion-tree mechanics
- Size at depth `k`: `n/2^k`.
- Base case when `n/2^k = 1`, so `k = log_2 n`.
- Number of leaves at depth `k`: `2^k = n`.

### Lecture notebook examples
All three lecture DnC examples show that divide-and-conquer is a structural design pattern, not automatically a speedup.

```python
def min_DnC(A, p, r):
    if p == r:
        return A[r]
    q = (p+r)//2
    l_min = min_DnC(A,p,q)
    r_min = min_DnC(A,q+1,r)
    if l_min <= r_min:
        return l_min
    else:
        return r_min
```

```python
def inner_prod_DnC(x,y,n):
    if n==1:
        return x[0]*y[0]
    q = n//2
    left = inner_prod_DnC(x[:q],y[:q],q)
    right = inner_prod_DnC(x[q:],y[q:],n-q)
    return left + right
```

```python
def vector_add_DnC(x,y,z,n):
    if n==1:
        z[0] = x[0] + y[0]
        return
    q = n//2
    x_left, x_right = x[:q], x[q:]
    y_left, y_right = y[:q], y[q:]
    z_left, z_right = z[:q], z[q:]
    vector_add_DnC(x_left,y_left,z_left,q)
    vector_add_DnC(x_right,y_right,z_right,n-q)
    for i in range(q):
        z[i] = z_left[i]
    for i in range(n-q):
        z[q+i] = z_right[i]
```

These three functions all solve to `Theta(n)`, but `inner_prod_DnC` and `vector_add_DnC` also demonstrate the memory cost of Python slicing and copying.

### CodingHW2 patterns
- Zero-pad matrices to the next power of 2.
- Implement divide-and-conquer matrix addition.
- Implement Strassen from the textbook equations.
- For odd-size matrices, pad only one extra row and column instead of doubling.
- Use coarsening: fall back to naive multiplication once the matrix gets small enough.

## Proof / Reasoning Toolkit
### Substitution Checklist
1. Guess a bound shape.
2. Assume the bound for all smaller inputs.
3. Substitute and simplify.
4. Pick constants so the inequality closes.

### Master Method Checklist
1. Identify `a`, `b`, and `f(n)`.
2. Compute the watershed function `n^{log_b a}`.
3. Compare `f(n)` against the watershed.
4. Apply the right case, or recognize when the method does not apply.

### DnC Design Checklist
1. State the divide step.
2. State the conquer step and the base case.
3. State the combine step.
4. Write the corresponding recurrence.

## Complexity + Tradeoffs
| Algorithm | Recurrence | Result |
| --- | --- | --- |
| Binary search | `T(n) = T(n/2) + O(1)` | `O(log n)` |
| `min_DnC` | `T(n) = 2T(n/2) + O(1)` | `Theta(n)` |
| `inner_prod_DnC` | `T(n) = 2T(n/2) + O(1)` plus slicing overhead | `Theta(n)` time, extra copying |
| Merge sort | `T(n) = 2T(n/2) + Theta(n)` | `Theta(n log n)` |
| Recursive 8-way matrix multiply | `T(n) = 8T(n/2) + Theta(n^2)` | `Theta(n^3)` |
| Strassen | `T(n) = 7T(n/2) + Theta(n^2)` | `Theta(n^{2.81})` |

## Canonical Examples (Max 5)
### 1. `T(n) = 2T(n/2) + n`
- **Goal:** solve the merge-sort recurrence.
- **Key steps:** compare `f(n) = n` to watershed `n`.
- **Common mistake:** forgetting the extra `log n` factor from Master Method Case 2.

### 2. `min_DnC`
- **Goal:** find the minimum element recursively.
- **Key steps:** split, recurse on both halves, compare the two minima.
- **Common mistake:** forgetting the base case `p == r`.

### 3. `inner_prod_DnC`
- **Goal:** compute a dot product recursively.
- **Key steps:** split both vectors, recurse, add the two partial sums.
- **Common mistake:** ignoring the cost of slicing in Python.

### 4. Strassen
- **Goal:** beat the cubic bound for matrix multiplication.
- **Key steps:** replace 8 recursive multiplications with 7 plus extra additions/subtractions.
- **Common mistake:** thinking divide-and-conquer automatically improves asymptotic time.

### 5. Coarsening threshold
- **Goal:** improve real performance on small subproblems.
- **Key steps:** stop recursing below a threshold and switch to the naive algorithm.
- **Common mistake:** optimizing asymptotics while ignoring exploding constant factors at the leaves.

## Practice Map
- Binary search templates
- Merge-sort style recurrences
- Matrix multiplication recurrences
- Master Method exercises
- Substitution proofs

## Mini-test
1. What are the three steps of divide-and-conquer?
2. What is the watershed function in the Master Method?
3. Why does recursive 8-way matrix multiplication stay cubic?
4. What does Strassen save compared with the naive recursive method?
5. Why can a DnC algorithm be asymptotically fine but still memory-heavy in Python?

## Flashcards
#cards/CSCI4041
1. Three DnC steps::Divide, conquer recursively, combine.
2. Watershed function::`n^{log_b a}`.
3. Merge-sort recurrence::`T(n) = 2T(n/2) + Theta(n)`.
4. Strassen recurrence::`T(n) = 7T(n/2) + Theta(n^2)`.
5. Substitution method::Guess the form, then prove it by induction.
6. Why slicing matters in Python::It creates new lists and adds copying overhead.
7. Coarsening::Stop recursing below a threshold and switch to a simpler base algorithm.

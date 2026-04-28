---
type: class
input_kind: lecture
status: seed
created: 2026-02-02
updated: 2026-04-16
area:
  - "[[UMN Board]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/DSA|DSA]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Introduction to Algorithms|Introduction to Algorithms]]"
tags:
  - "#Lecture"
  - "#class"
next:
  - "[[50_Archive/UMN/Classes/CSCI 4041/Week - 4|Week - 4]]"
---
# Entire Week
## What you must be able to do
- [[50_Archive/UMN/Classes/CSCI 4041/Textbook/Chapter - 3 & 4#3.1 O - notation, Ω - notation, and Θ notation|Chapter - 3 asymptotic notation]], [[50_Archive/UMN/Classes/CSCI 4041/Textbook/Chapter - 3 & 4#3.2 Asymptotic Notation: Formal Definitions|formal definitions]], and [[50_Archive/UMN/Classes/CSCI 4041/Textbook/Chapter - 3 & 4#4.5 The Master Method|the Master Method]]: explain O, Ω, and Θ with quantifiers and solve standard divide-and-conquer recurrences.
- [[50_Archive/UMN/Classes/CSCI 4041/Textbook/Chapter - 3 & 4#4.0 Introduction to Divide-and-Conquer and Recurrences|Chapter - 4 recurrences]], [[50_Archive/UMN/Classes/CSCI 4041/Textbook/Chapter - 3 & 4#4.3 The Substitution Method|substitution method]], and [[50_Archive/UMN/Classes/CSCI 4041/Textbook/Chapter - 3 & 4#4.4 The Recursion-Tree Method|recursion trees]]: derive tree height from $n/2^k = 1$, use substitution correctly, and know when recursion trees are giving a guess versus a proof.
- [[Divide and Conquer#Core Ideas (Lecture)|Divide and Conquer - Core Ideas (Lecture)]], [[Divide and Conquer#Proof / Reasoning Toolkit|Divide and Conquer - Proof / Reasoning Toolkit]], and [[Time Complexity#Definition|Time Complexity]]: connect the chapter methods to actual code from `min_DnC`, `inner_prod_DnC`, `vector_add_DnC`, and recursive matrix multiplication.
- [[Divide and Conquer#Practice Map|Divide and Conquer - Practice Map]]: binary search, merge-sort reasoning, and recurrence drills are still open practice items.

## Key ideas (textbook)
- **Asymptotic notation is a language for eventual growth, not exact equality.** The quantified definitions of $O$, $Ω$, and $Θ$ say that after some threshold $n_0$, one function stays within constant multiples of another. That matters because algorithm analysis is really about what dominates at large scale, not about the exact number of operations on tiny inputs.
- **Recurrences model recursive algorithms by isolating self-similarity.** If an algorithm makes two recursive calls on halves and then does constant or linear extra work, that structure is captured directly in a recurrence. Once the recurrence is written correctly, methods like substitution, recursion trees, and the Master Method become reusable proof tools rather than one-off tricks.
- **Divide-and-conquer is a pattern, not a guarantee of speedup.** A recursive matrix multiply with eight subproblems still stays cubic, because the branching factor is too large. Strassen matters because it changes the number of recursive multiplications from 8 to 7 while keeping the non-recursive work quadratic.
- **Implementation details change the real cost even when the recurrence looks the same.** `inner_prod_DnC` and `vector_add_DnC` both use the same left-half/right-half recursion shape as simpler examples, but Python slicing and copying introduce extra memory work that the high-level recurrence alone does not show.
- **Recursion trees and substitution work together.** The lecture used recursion trees to guess the form of the answer and substitution to prove it. That workflow is worth copying on exams because it prevents blind algebra and makes it easier to catch when a guess needs strengthening.

## Concepts created / updated today
- [[Divide and Conquer#Definition|Divide and Conquer]]
- [[Divide and Conquer#Core Ideas (Lecture)|Divide and Conquer - lecture code and recurrences]]
- [[50_Archive/UMN/Classes/CSCI 4041/Textbook/Chapter - 3 & 4#4.2 Strassen’s Algorithm|Chapter - 3 & 4 - Strassen]]

## Lecture
### Chapter - 3 Asymptotic analysis
Let f(n) & g(n) are non negative functions.
> [!NOTE] *Definition*: Big-O Notation tell us a "worst case for algorithm with centre f(n)" $$O(g(n)) = { f(n) | \exists C, N | f(n) \leq C.g(n) \forall n>N}$$
- $\exists$:
1. **Simpler definitions**:
    2. f(n) is *Upper Bound*: $O(g(n)): { f(n) | f(n) \leq g(n)}$
    3. f(n) is *Bounded Below*: $Ω(g(n)): { f(n) | g(n) \leq f(n)}$
    4. f(n) is *Tight Bound*: $Θ(g(n)) = { f(n) | C_{1}g(n) \leq f(n) \leq C_{2}g(n)}$
5. Formal definitions (let $f(n)$ and $g(n)$ be non-negative functions):
    - $O(g(n)) = \{f(n) \mid \exists C, N_0 : f(n) \leq C \cdot g(n)\ \forall n > N_0\}$ — upper bound
    - $\Omega(g(n)) = \{f(n) \mid \exists C, N_0 : g(n) \leq C \cdot f(n)\ \forall n > N_0\}$ — lower bound
    - $\Theta(g(n)) = \{f(n) \mid \exists C_1, C_2, N_0 : C_1 g(n) \leq f(n) \leq C_2 g(n)\ \forall n > N_0\}$ — tight bound
1. *Exercise 3.2 - 5*: Prove that the running time of an algorithm is Θ(g(n)) if and only if its worst-case running time is O(g(n)) and its best-case running time is Ω(g(n)).
    *Solution*: Proved with implication rule($\implies$):  
    2. Proof 1($\implies$): Suppose the runtime $f(n) = Θ(g(n)) \implies \exists C_{1}, C_{2}, N_{1}, N_{2}$ such that $C_1$  
    > $f(n) = \Theta(g(n)) \iff$ worst-case $= O(g(n))$ AND best-case = $\Omega(g(n))$.
### Chapter - 4 Divide & Conquer Algorithms (DnC)
> [!NOTE] *Definition*: DnC algorithms solve problems by dividing the work and solve each part separately and combine the results.
> - Follow these 3 steps:
>   1. Divide the work
>   2. Compare each sub problem
>   3. Combine results
1. *Recurrence Tree*: Each function cell has fixed constant cost + 2 recursive calls.
    - At the top of the tree: *size = n*, one division down, *size = n/2*, one more, *size = $n/2^2$*, so on give give this equation:
        - Size at depth $k$: $n/2^k$. Reaches base case when $n/2^k = 1 \implies k = \log_2 n$.
        - $Size = n/2^k$
    - Height = $k = log_2(n)$
    - Base Cases = $2^k = n$
1. *The Substitution Method*: Suppose $T(k) \leq C_2k$ for some k < n.
    Compute: $T(n) = 2T(n/2) + C_1$.
    - Suppose $T(k) \leq C_2 k$ for $k < n$.
        - $T(n) = 2T(n/2) + C_1 \leq 2C_2(n/2) + C_1 = C_2 n + C_1$.
        - For large enough $n$: $T(n) \leq C_2 n \implies T(n) = \Theta(n)$.
1. *Matrix Multiply*: C = A.B
    2. Block Matrix Multiplication: Turn a huge matrix into small blocks by dividing them n/2.
        - Cost: $T(n) = 8T(n/2) + C$ or $T(n) = 8T(n/2) + Θ(n^2)$ (with copying)
        - Both solve to $\Theta(n^3)$ — no asymptotic gain.
### Jupyter Notebooks (Ch4_Divide_and_Conquer_Examples_.ipynb)
#### min_DnC
- $T(n) = 2T(n/2) + O(1) \implies \Theta(n)$.
- 0-indexed: `q = (p+r)//2`; left: `min_DnC(A,p,q)`; right: `min_DnC(A,q+1,r)`.
- Edge cases tested: min at left end, min at right end.
#### inner_prod_DnC
- Divides summation $\sum x_i y_i$ into halves; adds results (combine = $+$).
- Uses `x[:q]` slicing → $O(n)$ copy per level; total space $O(n \log n)$ across all levels.
#### vector_add_DnC
- Creates `z_left`, `z_right` sub-lists → copies back. Same $\Theta(n)$ complexity as loop.
- Demonstrates in-place vs. copy tradeoff: not always required to copy.
### Chapter 3 and Chapter 4 - Asymptotic Notation, Recurrences, and Divide-and-Conquer
This week is where the course becomes much more formal. Chapter 3 gives the language for talking about growth rates, and Chapter 4 shows how that language gets used on recursive algorithms. The big shift in lecture was that asymptotic notation stopped being a slogan and became a proof object. Instead of saying "this looks linear" or "this feels logarithmic," the lecture kept returning to the exact quantified definitions of $O$, $Ω$, and $Θ$, because those are what justify a recurrence solution. That matters in practice: once you write down a recurrence, you need a method to prove its solution, and that proof always comes back to constants, thresholds, and inequalities.

The divide-and-conquer notebooks made that idea concrete. `min_DnC` is the cleanest example: split the array in half, recurse on both halves, then do constant combine work by returning the smaller minimum. That gives $T(n)=2T(n/2)+C$, so all three standard tools agree on $Θ(n)$. `inner_prod_DnC` looks similarly innocent, but the lecture used it to make an implementation point: slicing `x[:q]` and `x[q:]` creates fresh lists, so the code is not just paying for the recursive arithmetic. `vector_add_DnC` pushed that idea further by showing the cost of creating sublists and then copying results back into z. So the lecture was not only teaching divide-and-conquer as a design pattern. It was also teaching us to separate the clean mathematical recurrence from the concrete language-level overhead of a Python implementation.

Matrix multiplication closed the loop. The naive recursive version proves that divide-and-conquer alone does not guarantee asymptotic improvement, because 8 subproblems of size $n/2$ still give cubic growth. Strassen then becomes meaningful as a structural change, not a magic formula: the algorithm wins by cutting the recursive multiplication count from 8 to 7 while keeping the extra addition/subtraction work at $Θ(n^2)$. Homework 2 then turned that into implementation engineering with zero-padding, odd-dimension padding, and a coarsening threshold that switches back to naive multiplication for small subproblems.

### Jupyter Notebook Explanations
#### Ch4_Divide_and_Conquer(Examples).ipynb
This notebook is the lecture's main bridge from recurrence theory to executable code. It starts with small recursive examples so the recurrence-writing process becomes mechanical.

```python
def min_DnC(A, p, r):
    if p == r:
        return A[r]

    q = (p + r) // 2
    l_min = min_DnC(A, p, q)
    r_min = min_DnC(A, q + 1, r)

    if l_min < r_min:
        return l_min
    return r_min
```

The important thing in this code is how little happens outside the recursion. The base case handles one element, the recursive calls split at `q = (p + r) // 2`, and the combine step is just one comparison. That is why the recurrence is $T(n)=2T(n/2)+C$ and why the solution is linear. This notebook is the best example of a recurrence where the algorithmic structure is much cleaner than the actual algebra used to solve it.

```python
def inner_prod_DnC(x, y, n):
    if n == 1:
        return x[0] * y[0]

    q = n // 2
    left = inner_prod_DnC(x[:q], y[:q], q)
    right = inner_prod_DnC(x[q:], y[q:], n - q)
    return left + right
```

At the mathematical level, this is still "split, recurse, add." The lecture point is that the code is also paying to create `x[:q]`, `y[:q]`, `x[q:]`, and `y[q:]`. So when you explain this function, you need both stories: the clean recurrence for the arithmetic work and the implementation detail that slicing adds copying overhead at every level.

```python
def vector_add_DnC(x, y, z, n):
    if n == 1:
        z[0] = x[0] + y[0]
        return

    q = n // 2
    x_left, x_right = x[:q], x[q:]
    y_left, y_right = y[:q], y[q:]
    z_left, z_right = z[:q], z[q:]

    vector_add_DnC(x_left, y_left, z_left, q)
    vector_add_DnC(x_right, y_right, z_right, n - q)

    z[:q] = z_left
    z[q:] = z_right
```

This example looks like overkill for vector addition, and that is exactly why the notebook is useful. It shows that divide-and-conquer can be correct without being the best implementation choice. The note in lecture was that copying back into z is not always required, so an in-place variant can save memory while preserving the same high-level recursion pattern.

#### Ch4_Divide_and_Conquer(Matrix-Multiply).ipynb
This notebook moves from toy examples to a standard textbook algorithm and then to Strassen's improvement.

```python
# recursive structure only
if n == 1:
    c_11 = c_11 + a_11 * b_11
    return

# divide into 4 blocks each
# make 8 recursive calls
# combine into C_11, C_12, C_21, C_22
```

The lecture contrast was straightforward: the naive recursive method preserves the same arithmetic complexity as the triple-loop version because 8 subproblems of size `n/2` still imply cubic growth. Strassen becomes important because it changes the branching factor while keeping the non-recursive work quadratic.

#### CodingHW_2(chapter4-CLRS).ipynb
Homework 2 extended the lecture examples into edge cases that matter in real code.

- **Task 1:** zero-pad matrices to the next power of 2 so recursive halving works cleanly, then extract the top-left original block afterward.
- **Task 2:** use the same divide-and-conquer structure for matrix addition, which makes the recursion pattern easier to compare against multiplication.
- **Task 3:** implement Strassen directly from the textbook's $S_1$ through $S_{10}$ and $P_1$ through $P_7$ equations.
- **Task 4:** use odd-size padding by adding just one row and column instead of over-padding aggressively.
- **Task 5:** coarsen the recursion and switch to naive multiplication when `n < 26`; the lecture point was that fewer tiny recursive calls can beat the asymptotically elegant version in practice.

## Examples worth keeping
- **Substitution example:** $T(n)=2T(n/2)+C$ with guess $T(n)\leq C_2 n$ is the cleanest worked proof of a linear recurrence.
- **Recursion-tree height derivation:** $n/2^k = 1 \Rightarrow k=\log_2 n$. This one derivation reappears in merge sort, quicksort, and balanced divide-and-conquer analysis.
- **`min_DnC` recurrence:** $2T(n/2)+C \Rightarrow Θ(n)$. Good example of constant combine work.
- **Strassen:** $T(n)=7T(n/2)+Θ(n^2) \Rightarrow Θ(n^{\log_2 7}) \approx Θ(n^{2.81})$.
- **Coarsened matrix multiplication:** switch to naive multiplication when the subproblem is small so recursion overhead does not dominate.

## Takeaways (questions to resolve)
- [ ] Why do the quantified definitions of $O$, $Ω$, and $Θ$ matter more than the informal "upper/lower/tight bound" wording?
- [ ] When does substitution require strengthening the inductive hypothesis with a lower-order correction term?
- [ ] Why does `inner_prod_DnC` have a cleaner recurrence than its actual Python memory behavior suggests?
- [ ] What is the exact structural difference between naive recursive matrix multiply and Strassen?
- [ ] Why can a coarsening threshold improve runtime even when it does not improve the asymptotic bound?

## Flashcards
#cards/CSCI4041
1. What does $Θ(g(n))$ mean formally::There exist positive constants $c_1$, $c_2$, and $n_0$ such that $c_1 g(n) \leq f(n) \leq c_2 g(n)$ for all $n \geq n_0$.
2. How do you derive recursion-tree height for halving recurrences::Set $n/2^k = 1$ and solve for $k = \log_2 n$.
3. What is the recurrence for `min_DnC`::$T(n)=2T(n/2)+C$.
4. Why is `inner_prod_DnC` more expensive in Python than the clean recurrence suggests::Because slicing creates new sublists at every recursive level.
5. What is Strassen's recurrence::$T(n)=7T(n/2)+Θ(n^2)$.
6. What is the coarsening idea in Homework 2::Switch to naive multiplication below a small threshold to reduce recursive overhead.
7. What is the Master Method watershed function::$n^{\log_b a}$.

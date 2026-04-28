---
type: class
input_kind: book
status: seed
created: 2026-02-02
updated: 2026-04-16
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/UMN/Classes/CSCI 4041/Week - 3|Week - 3]]"
---
# Chapter - 3
## Summary Links
- [[50_Archive/UMN/Classes/CSCI 4041/Week - 3#Chapter 3 and Chapter 4 - Asymptotic Notation, Recurrences, and Divide-and-Conquer|Week - 3]]
- [[Divide and Conquer#Definition|Divide and Conquer]]
- [[Time Complexity#Definition|Time Complexity]]

**Chapter 3: Characterizing Running Times** focuses on **asymptotic efficiency**, which is the study of how the running time of an algorithm increases with the size of the input in the limit as the size increases without bound. While we can sometimes calculate an exact running time, the extra precision is rarely worth the effort because for large inputs, the leading term of the function dominates the constant factors and lower-order terms.

## 3.1 O - notation, Ω - notation, and Θ notation
Asymptotic notations are mathematical tools used to focus on the **rate of growth** of a function. They characterize functions in general, but in this field, they are most often used to describe the running times of algorithms.
- *O - notation (Upper Bound)*: This notation provides an **asymptotic upper bound**, meaning it states that a function grows **no faster** than a certain rate. For example, a function like $7n^3+100n^2$ is considered $O(n^3)$. Because it grows no faster than $n^3$, it is also technically correct (though less precise) to say it is $O(n^4)$ or any higher power.
- *Ω - notation (Lower Bound):* This notation characterizes an **asymptotic lower bound**. It states that a function grows **at least as fast** as a certain rate. The function $7n^3+100n^2$ is $Ω(n^3)$, and also $Ω(n^2)$ or $Ω(n)$.
- *Θ - notation (Tight Bound):* This notation provides an **asymptotically tight bound**. It means the function grows at a specific rate to within a constant factor from both above and below.
> [!NOTE] **Theorem 3.1:** A function f(n) is $Θ(g(n))$ if and only if it is both $O(g(n))$ and $Ω(g(n))$.

### Formal Definition with Quantifiers
The lecture kept coming back to the quantified definitions because they are the exact reason asymptotic notation is useful:

- $O(g(n)) = \{f(n) \mid \exists c > 0, \exists n_0 > 0, \forall n \geq n_0,\ 0 \leq f(n) \leq c g(n)\}$
- $Ω(g(n)) = \{f(n) \mid \exists c > 0, \exists n_0 > 0, \forall n \geq n_0,\ 0 \leq c g(n) \leq f(n)\}$
- $Θ(g(n)) = \{f(n) \mid \exists c_1 > 0, \exists c_2 > 0, \exists n_0 > 0, \forall n \geq n_0,\ 0 \leq c_1 g(n) \leq f(n) \leq c_2 g(n)\}$

Those quantifiers matter because they mean "eventually" and "up to constant factors," not "exactly equal for every input size."

### Lecture Emphasis
The lecture treated Chapter 3 as the language needed to explain every later notebook. The point was not just to memorize that $O$ means upper bound and $Θ$ means tight bound, but to get comfortable reading statements like "there exist constants" and "for all sufficiently large n." That is what lets us prove a recurrence solution rather than just guess it from a graph. The lecture also used the simplified set-style definitions as intuition, then returned to the quantified form when the proof details mattered. That pattern is important for exams: use the intuitive reading first, then the formal definition when you need to justify a claim.

## 3.2 Asymptotic Notation: Formal Definitions
The sources define these notations using sets of functions where $n_0$ and c are positive constants:
1. $Θ(g(n))$: The set of functions f(n) such that there exist positive constants $c_1$, $c_2$, and $n_0$ where $0 \leq c_{1}g(n) \leq f(n) \leq c_{2}g(n)$ for all $n \geq n_0$.
2. $O(g(n))$: The set of functions f(n) such that there exist positive constants c and $n_0$ where $0 \leq f(n) \leq c g(n)$ for all $n \geq n_0$.
3. $Ω(g(n))$: The set of functions f(n) such that there exist positive constants c and $n_0$ where $0 \leq c g(n) \leq f(n)$ for all $n \geq n_0$.

**Strict Bounds (o and ω)**
- *o-notation (Little-oh):* Used to denote an upper bound that is **not asymptotically tight**. For example, $2n=o(n^2)$, but $2n^2=O(n^2)$. Intuitively, f(n) becomes insignificant relative to g(n) as n becomes large.
- *ω - notation (Little-omega):* The lower-bound version of o-notation. It denotes a lower bound that is not asymptotically tight.

**Comparing Functions:** Asymptotic comparisons share similarities with comparing real numbers:
- **Transitivity:** If f(n)=Θ(g(n)) and g(n)=Θ(h(n)), then f(n)=Θ(h(n)).
- **Reflexivity:** f(n)=Θ(f(n)).
- **Symmetry:** f(n)=Θ(g(n)) if and only if g(n)=Θ(f(n)).
- **Transpose Symmetry:** f(n)=O(g(n)) if and only if g(n)=Ω(f(n)).

One property of real numbers that does **not** carry over is **Trichotomy**: while any two real numbers can be compared, not all functions are asymptotically comparable; some may oscillate such that neither O nor Ω relationship exists between them.

### Lecture Emphasis
The most exam-relevant move here is to separate "mathematical truth" from "engineering shorthand." We often say "merge sort is $O(n \log n)$," but the formal statement is that its running-time function belongs to a set of functions eventually bounded above by a constant multiple of $n \log n$. That language matters again in Chapter 4 when we prove recurrence bounds, because the proof structure is exactly: make a guess, choose constants, then show the inequalities hold for all sufficiently large n.

## 3.3 Standard Notations and Common Functions
This section covers the mathematical foundations you will need throughout the textbook.
1. **Monotonicity:** A function f(n) is **monotonically increasing** if $m \leq n$ implies $f(m) \leq f(n)$. It is **strictly increasing** if $m < n$ implies $f(m) < f(n)$.
	1. **Floors and Ceilings**
		- **Floor (⌊x⌋):** The greatest integer less than or equal to x.
		- **Ceiling (⌈x⌉):** The least integer greater than or equal to x. Both are monotonically increasing functions.
	2. **Modular Arithmetic:** The value $a \bmod n$ is the remainder of the quotient a/n. If $(a \bmod n)=(b \bmod n)$, we write $a \equiv b \pmod n$, meaning a is equivalent to b modulo n.
	3. **Polynomials:** A polynomial in n of degree d is characterized as $p(n)=Θ(n^d)$. A function is *polynomially bounded* if $f(n)=O(n^k)$ for some constant k.
	4. **Exponentials:** Any exponential function with a base greater than 1 grows faster than any polynomial function. The base of natural logarithms is denoted by e.
	5. **Logarithms:** `lg n` means $\log_2 n$.
		- `ln n` means $\log_e n$.
		- `lg^k n` means $(\lg n)^k$. In computer science, base 2 is the most natural because many algorithms split problems into two parts. A function is **polylogarithmically bounded** if $f(n)=O(\lg^k n)$.
	6. **Factorials (n!):** Defined as $n! = 1 \cdot 2 \cdot 3 \cdots n$. A useful tool for approximating factorials is *Stirling's approximation*, which provides a tight bound for n! using e and n.
2. **Functional Iteration and Iterated Logarithms**
	1. **Functional Iteration $(f^{(i)}(n))$:** Applying a function f(n) to itself i times.
	2. **Iterated Logarithm $(\lg^* n)$:** The number of times the logarithm function must be applied to n to reach a value ≤ 1. It is an **extremely slowly growing function**; for any input size practically encountered in the universe, $\lg^* n \leq 5$.
3. **Fibonacci Numbers:** Defined by the recurrence $F_i=F_{i-1}+F_{i-2}$ starting with $F_0=0$ and $F_1=1$. They are related to the **Golden Ratio (φ)** and its conjugate, growing exponentially over time.

# Chapter - 4 Divide & Co
The divide-and-conquer style algorithms *divide* the problem to be solved into 2 or more sub-problems, *conquer* each of the problems separately, and then *combine* the solutions if needed after each sub-problem was solved on their own.
1. **Divide** the problem into one or more subproblems that are smaller instances of the same problem.
2. **Conquer** the subproblems by solving them recursively.
3. **Combine** the subproblem solutions to form a solution to the original problem.

## 4.0 Introduction to Divide-and-Conquer and Recurrences
When an algorithm contains a recursive call, its running time is described by a **recurrence equation** (or **recurrence**), which defines the function in terms of its value on smaller arguments.

1. **Recurrence Basics and Conventions**
	- *Algorithmic Recurrences:* A recurrence T(n) is "algorithmic" if, for a sufficiently large **algorithmic threshold** ($n_0$), it satisfies two properties:
		1. $T(n)=Θ(1)$ for all $n<n_0$.
		2. Every path of recursion terminates in a defined base case within a finite number of recursive invocations.
	- *Simplifications:* We frequently state algorithmic recurrences without floors and ceilings (e.g. $T(n/2)$ instead of $T(\lfloor n/2 \rfloor)$) because this simplification generally does not affect the order of growth.
	- *Inequalities:* If a recurrence is an inequality (e.g. $T(n)\leq2T(n/2)+Θ(n)$), the solution is expressed using O-notation; if the inequality is reversed, we use Ω-notation.

### Lecture Emphasis
The lecture used divide-and-conquer to connect theory and code. The main move was always the same: identify the base case, identify the recursive calls, then decide whether the combine step is constant, linear, or more expensive. That is exactly why the three small notebooks from Week 3 were so useful: `min_DnC` has constant combine work, `inner_prod_DnC` has addition as the combine step but incurs slicing cost in Python, and `vector_add_DnC` shows how copying sublists changes the space story without changing the asymptotic arithmetic work.

## 4.1 Multiplying Square Matrices
This section uses the problem of multiplying two $n \times n$ matrices A and B to compute $C=A \cdot B$ to demonstrate that not all divide-and-conquer approaches provide a speedup.

- **The Straightforward Method (MATRIX-MULTIPLY):** Using a triply nested loop to implement the standard row-by-column summation, the algorithm requires $n^3$ scalar multiplications. The running time is $Θ(n^3)$.
```python
for i = 1 to n                     # compute entries in each of n rows
	for j = 1 to n                 # compute n entries in row i
		for k = 1 to n
			c_ij = c_ij + a_ik.b_jk # add in another term
```

- **Simple Divide-and-Conquer (MATRIX-MULTIPLY-RECURSIVE):**
	- *Divide:* Partition $n \times n$ matrices into four $n/2 \times n/2$ submatrices. This can be done via **index calculations** in $Θ(1)$ time, which is faster and more practical than allocating temporary storage.
	- *Conquer:* Perform **eight recursive multiplications** of these submatrices.
	- *Combine:* No explicit combine step is needed if the matrices are updated in-place.
	- *Analysis:* The recurrence is $T(n)=8T(n/2)+Θ(1)$.
	- *Result:* Using the **Master Method**, this solves to $T(n)=Θ(n^3)$, which is no faster than the straightforward loop method.
```python
if n == 1
	# Base case
	c_11 = c_11 + a_11.b_11
	return
	# Divide
	partition A, B, and C into n/2×n/2 submatrices
	# Conquer
	recursively compute 8 products
```

### Lecture DnC Examples
The Week 3 notebook began with smaller divide-and-conquer functions before returning to matrices:

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

- Base case: one element, so that element is the minimum.
- Recurrence: $T(n)=2T(n/2)+C$.
- Solution: $Θ(n)$ by substitution or Master Method Case 2.

```python
def inner_prod_DnC(x, y, n):
    if n == 1:
        return x[0] * y[0]

    q = n // 2
    left = inner_prod_DnC(x[:q], y[:q], q)
    right = inner_prod_DnC(x[q:], y[q:], n - q)
    return left + right
```

- Same arithmetic recurrence as the minimum example, but now Python slicing copies data at every level.
- The computation is still conceptually divide-and-conquer on halves, but the implementation detail matters for space and constant factors.

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

- The notebook explicitly notes that copying back into z is not always necessary.
- That makes it a useful example of "same recursion pattern, different memory behavior."

## 4.2 Strassen’s Algorithm
In 1969, V. Strassen published a remarkable algorithm that beats the $Θ(n^3)$ bound.

- **The Key Insight:** Strassen found a way to use only *seven recursive multiplications* of $n/2 \times n/2$ submatrices instead of eight.
- **The Trade-off:** Reducing the number of multiplications requires more additions and subtractions. Because multiplications are more expensive for large matrix problems, this leads to an asymptotically faster algorithm.
- **The 4 Steps of Strassen**
	1. *Divide* into $n/2 \times n/2$ submatrices.
	2. *Create 10 matrices* by adding or subtracting submatrices.
	3. *Recursively compute 7 products* $P_1$ through $P_7$.
	4. *Update the result submatrices* by combining those products.

*Efficiency:* The recurrence is $T(n)=7T(n/2)+Θ(n^2)$. The solution is $T(n)=Θ(n^{\log_2 7})$, which is approximately $Θ(n^{2.81})$.

### Lecture Emphasis
The lecture and homework framed Strassen as more than a formula to memorize. The important story is what changes between the naive recursive algorithm and Strassen:
- Naive recursion makes 8 recursive calls, so the branching factor alone already forces cubic time.
- Strassen replaces one recursive multiplication with extra matrix additions and subtractions.
- Since the non-recursive work is still $Θ(n^2)$, reducing the recursive branching factor from 8 to 7 changes the asymptotic exponent.

## 4.3 The Substitution Method
The **substitution method** is the most general technique for solving recurrences. It involves two steps:
1. **Guess** the form of the solution using symbolic constants.
2. Use **mathematical induction** to find the constants and prove the solution works.

- *Strengthening the Induction:* If a guess is correct (e.g. $T(n)=O(n)$) but the induction fails, try subtracting a lower-order term from the guess (e.g. $T(n)\leq cn-d$ instead of $T(n)\leq cn$).
- *Common Pitfalls:* Never use asymptotic notation directly inside an inductive hypothesis, as the hidden constants can change and invalidate the proof.

### Worked Example: $T(n)=2T(n/2)+C$
The lecture worked this exact recurrence because it appears in the `min_DnC` notebook and is the cleanest substitution example.

1. Guess an upper bound of the form $T(n) \leq C_2 n$ for all sufficiently large n.
2. Assume as the inductive hypothesis that for all smaller k,
$$
T(k) \leq C_2 k.
$$
3. Then
$$
T(n) = 2T(n/2) + C_1 \leq 2\left(C_2 \frac{n}{2}\right) + C_1 = C_2 n + C_1.
$$
4. For sufficiently large n, the additive constant can be absorbed into the linear term, so the solution is
$$
T(n)=Θ(n).
$$

The main lesson is not the algebra itself. It is the structure: guess, substitute, simplify, then choose constants so the inequality closes.

## 4.4 The Recursion-Tree Method
A **recursion tree** is a visual map where each node represents the cost of a single subproblem.

- **Mechanics:** Sum the costs within each level of the tree to determine per-level costs, and then sum all level costs for the total.
- **Use Cases:** It is best used to generate a good guess for the substitution method.
- **Appendix Connection:** When summing costs, you often encounter geometric series. If the costs decrease geometrically, the total cost is dominated by the root; if they increase, the leaves dominate.

### Lecture Emphasis
The lecture repeatedly used the equation
$$
\frac{n}{2^k} = 1
$$
to derive recursion-tree height. Solving gives $k=\log_2 n$, which is the backbone for merge sort, balanced quicksort, and many divide-and-conquer algorithms. That one derivation is worth memorizing because it appears anytime the subproblem size is halved at each level.

## 4.5 The Master Method
The **master method** provides a cookbook for solving recurrences of the form $T(n)=aT(n/b)+f(n)$, where $a \geq 1$ and $b > 1$.

- **Watershed Function:** The algorithm's growth is compared to the watershed function $n^{\log_b a}$.
- **The Three Cases**
	1. **Case 1:** $f(n)$ grows polynomially slower than the watershed function.
	   - Solution: $T(n)=Θ(n^{\log_b a})$.
	2. **Case 2:** $f(n)$ and the watershed function grow at the same rate up to a polylogarithmic factor.
	   - Solution: $T(n)=Θ(n^{\log_b a}\log^{k+1} n)$.
	3. **Case 3:** $f(n)$ grows polynomially faster than the watershed function and satisfies a regularity condition.
	   - Solution: $T(n)=Θ(f(n))$.

**Gaps:** The method cannot be used if $f(n)$ is not polynomially smaller or larger than the watershed function, or if the regularity condition fails.

### CodingHW2 Extensions
The homework took the chapter ideas and made them implementation-focused:

- **Zero-padding to next power of 2:** pad matrices so recursive splitting stays legal, then extract the original top-left result block.
- **DnC matrix addition:** same recursion structure as multiplication, but combine is element-wise addition.
- **Odd-size padding optimization:** instead of padding all the way to the next power of 2, add only one row and one column when size is odd.
- **Coarsening threshold:** switch back to naive multiplication when n becomes small. The notes use `n < 26` as the threshold and explain that this prevents a huge number of tiny recursive calls.

That last point is especially important because it shows the difference between asymptotic improvement and practical performance: even if Strassen wins asymptotically, a hybrid implementation often wins in real code.

## 4.6 & 4.7 Advanced Topics (Starred)
- **Continuous Master Theorem:** A variant of the master theorem defined over real numbers rather than integers, providing a mathematical foundation for how these recurrences behave.
- **Akra-Bazzi Method:** A generalization of the master method that can solve recurrences where subproblems are of different sizes. It uses calculus to determine the asymptotic solution. For this to work, the driving function f(n) must satisfy the polynomial-growth condition.

# Chapter - 5 Probabilistic Analysis and Randomized Algorithms
**Chapter 5: Probabilistic Analysis and Randomized Algorithms** introduces tools to analyze algorithms when their performance depends on the distribution of inputs or on random choices made during execution.

## 5.1 The Hiring Problem
The textbook uses the **Hiring Problem** to illustrate these concepts.
- **The Scenario:** You need an office assistant and use an agency that sends one candidate per day for n days.
- **The Strategy:** You interview each candidate. If a candidate is better than the one you currently have, you fire the old one and hire the new one.
- **The Costs**
	- **Interviewing cost ($c_i$):** A small fee for every interview.
	- **Hiring cost ($c_h$):** A high cost to fire the old assistant and hire a better one.
	- **Total Cost Formula:** $O(c_i n + c_h m)$, where m is the number of people hired.
- **Worst-Case:** If candidates arrive in increasing order of quality, you hire n times.
- **Probabilistic Analysis:** Assume the input follows a probability distribution and compute the expected value.

## 5.2 Indicator Random Variables
- **Definition:** An indicator random variable $I\{A\}$ is 1 if event A occurs and 0 otherwise.
- **Fundamental Formula:** $E[I\{A\}] = \Pr\{A\}$.
- **Linearity of Expectation:** $E[X_1 + X_2] = E[X_1] + E[X_2]$, even without independence.

These are exactly the tools reused in the expected-analysis proof of randomized quicksort in [[Chapter - 7 & 10#7.4 Analysis of Quicksort|Chapter - 7 & 10]].

## 5.3 Randomized Algorithms
- **Probabilistic Analysis:** We assume the input is random.
- **Randomized Algorithms:** The algorithm creates randomness itself.
- **RANDOMLY-PERMUTE(A):** Shuffles the array in place so that every permutation is equally likely.

## 5.4 Advanced Probabilistic Examples (Starred Section)
1. **The Birthday Paradox:** Only 23 people are needed for a > 1/2 chance that two share a birthday.
2. **Balls and Bins:** Essential for understanding hashing.
3. **Streaks:** The expected longest streak of heads in n fair coin flips is $Θ(\lg n)$.
4. **The Online Hiring Problem:** Skip the first roughly $n/e$ candidates, then hire the next candidate better than all seen so far; success probability is about $1/e$.

> **Summary of Basics for Data Structures**
> Understanding Chapter 5 is vital for data structures because it allows us to analyze average-case performance. For example, in hash tables the worst-case search is O(n), but probabilistic analysis proves the average-case is O(1). In quicksort, randomization ensures we avoid the quadratic worst case and achieve expected $O(n \lg n)$ time.

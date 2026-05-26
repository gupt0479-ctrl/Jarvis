---
type: class
status: archived
created: 2025-12-04
updated: 2025-12-13
area:
  - "[[Chapter - 9]]"
  - "[[Chapter - 7]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2011/Chapter - 6]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2011/Chapter - 5]]"
  - "[[Chapter - 4]]"
  - "[[Chapter - 2]]"
  - "[[Chapter - 3]]"
  - "[[Chapter - 10]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2011/Chapter - 1]]"
  - "[[Main Examples]]"
  - "[[Material]]"
tags:
  - "#class"
next: "[[CSCI 2011 Board]]"
---
## Ch 1: Logic + Proofs (Essentials)
### Propositions
- Proposition = declarative statement with truth value T/F.
- Not propositions: commands; open sentences with free variables.
### Connectives (key equivalences)
- ¬p, p∧q, p∨q
- XOR: p ⊕ q ≡ (p∨q) ∧ ¬(p∧q)
- Implication: p→q ≡ ¬p ∨ q
- Negation of implication: ¬(p→q) ≡ p ∧ ¬q
- Biconditional: p↔q ≡ (p→q) ∧ (q→p)
### “If / Only if” translation (IMPORTANT)
- “A if B”  ≡ B → A
- “A only if B” ≡ A → B
- “A iff B” ≡ (A→B) ∧ (B→A)
### Standard Laws
- DeMorgan: ¬(p∧q) ≡ ¬p∨¬q ; ¬(p∨q) ≡ ¬p∧¬q
- Double negation: ¬¬p ≡ p
- Distributive:
  - p∨(q∧r) ≡ (p∨q)∧(p∨r)
  - p∧(q∨r) ≡ (p∧q)∨(p∧r)
### Predicates + Quantifiers
- Predicate P(x): not a proposition until x is bound/given value.
- ∀x P(x): true if P holds for every x (one counterexample kills it)
- ∃x P(x): true if at least one x works (give a witness)
- Negations:
  - ¬∀x P(x) ≡ ∃x ¬P(x)
  - ¬∃x P(x) ≡ ∀x ¬P(x)
### Nested Quantifiers
- Order matters: ∀x∃y P(x,y) usually ≠ ∃y∀x P(x,y)
- Negate by flipping each quantifier and negating predicate:
  ¬(∀x∃y P) ≡ ∃x∀y ¬P
### Uniqueness
- ∃!x P(x) means “exists exactly one”
- Expanded form:
  ∃x( P(x) ∧ ∀y(P(y)→y=x) )
### Rules of Inference (propositional)
- MP: (p→q), p ⟹ q
- MT: (p→q), ¬q ⟹ ¬p
- HS: (p→q), (q→r) ⟹ (p→r)
- DS: (p∨q), ¬p ⟹ q
- Simplification: (p∧q) ⟹ p
- Conjunction: p, q ⟹ (p∧q)
- Addition: p ⟹ (p∨q)
- Resolution: (p∨q), (¬p∨r) ⟹ (q∨r)
### Inference with Quantifiers (watch the caveats)
- UI: ∀xP(x) ⟹ P(c)
- UG: P(c) for arbitrary c ⟹ ∀xP(x)
- EI: ∃xP(x) ⟹ P(c) for some NEW c
- EG: P(c) ⟹ ∃xP(x)
### Proof Templates
- Direct: assume P, derive Q.
- Contrapositive: prove ¬Q→¬P.
- Contradiction: assume ¬statement, derive impossible.
- Cases: split into exhaustive + disjoint cases.
- Existence: give explicit example (constructive) or argue indirectly.
- Uniqueness: show existence + “if R and S both work, then R=S”.
## Ch 2: Sets + Functions + Sequences + Sums
### Sets
- Set = unordered collection of distinct elements.
- Membership: x∈A, x∉A
- Empty set: ∅ ; careful: {∅} ≠ ∅
- Equality: A=B ⇔ (∀x)(x∈A ↔ x∈B)
- Subset: A⊆B ⇔ (∀x)(x∈A → x∈B)
- Proper subset: A⊂B ⇔ A⊆B and A≠B
### Cardinality + Power Set
- |A| = number of distinct elements
- If |A|=n then |P(A)| = 2^n
### Tuples + Cartesian Product
- Ordered pair: (a,b) with order mattering
- A×B = {(a,b): a∈A, b∈B}
- Relation = any subset of A×B
### Set Operations
- Union: A∪B = {x: x∈A or x∈B}
- Intersection: A∩B = {x: x∈A and x∈B}
- Complement (relative to universe U): A^c = U−A
- Difference: A−B = {x: x∈A and x∉B} = A∩B^c
- Disjoint: A∩B=∅
- Counting: |A∪B| = |A|+|B|−|A∩B|
### Set Identities (high use)
- DeMorgan: (A∪B)^c = A^c ∩ B^c ; (A∩B)^c = A^c ∪ B^c
- Absorption: A∪(A∩B)=A ; A∩(A∪B)=A
- Complement: A∪A^c=U ; A∩A^c=∅
### Functions
- f:A→B means each x∈A maps to exactly one y∈B.
- Range/Image: f(A) = {f(x): x∈A} ⊆ B
- Preimage of element: f^{-1}(y) = {x∈A: f(x)=y}
- Preimage of set S⊆B: f^{-1}(S) = {x∈A: f(x)∈S}
**Injective (1-1):**
- f(a)=f(b) → a=b  (equiv: a≠b → f(a)≠f(b))
**Surjective (onto):**
- (∀y∈B)(∃x∈A) f(x)=y  (range = codomain)
**Bijective:** injective + surjective
**Inverse:**
- exists iff bijective; then f^{-1}:B→A and:
  f^{-1}(f(x))=x,  f(f^{-1}(y))=y
**Composition:**
- (g∘f)(x)=g(f(x))  (inside-out)
**Floor/Ceiling:**
- ⌊x⌋ = greatest integer ≤ x
- ⌈x⌉ = least integer ≥ x
### Sequences
**Arithmetic:**
- If a0=a: an = a + dn
- If a1=a: an = a + (n−1)d
**Geometric:**
- If a0=a: an = a r^n
- If a1=a: an = a r^(n−1)
**Recurrence:**
- needs rule + enough initial conditions.
### Summations
- Linearity: Σ(af(k)+bg(k)) = aΣf(k)+bΣg(k)
- Split range: Σ_{k=m..n} = Σ_{k=m..j}+Σ_{k=j+1..n}
Formulas:
- Σ_{i=1..n} i = n(n+1)/2
- Σ_{i=1..n} i^2 = n(n+1)(2n+1)/6
- Σ_{k=0..n} ar^k =
  a(r^{n+1}-1)/(r-1) if r≠1; else a(n+1)
## Ch 4: Divisibility, Div/Mod, Modular Arithmetic, Bases (Short Notes)
### Divides
- **a | b** ⇔ ∃ integer c such that **b = ac**.  (c can be negative/0 too)
- **a ∤ b** means no such integer c exists.
- Properties:
  1. a|b and a|c ⇒ a|(b+c)
  2. a|b ⇒ a|(bc) for any integer c
  3. a|b and b|c ⇒ a|c
### Division Algorithm
For integers a and **d>0**, ∃ unique integers q,r such that:
- **a = dq + r**, with **0 ≤ r < d**
- Then: **a div d = q**, **a mod d = r**
- For **a ≥ 0**: q = ⌊a/d⌋ and r = a − d⌊a/d⌋
### Congruence / Modular Arithmetic
- **a ≡ b (mod m)** ⇔ **m | (a − b)** ⇔ a and b have same remainder mod m
- Equivalent form: **a = b + km** for some integer k
- Arithmetic rules (if a≡b (mod m), c≡d (mod m)):
  - **a+c ≡ b+d (mod m)**
  - **ac ≡ bd (mod m)**
- Notation: **+ₘ** and **×ₘ** mean do the operation then take mod m.
### Base-B Representation
- If digits are a_k … a_0 in base B:
  - **(a_k…a_0)_B = Σ_{i=0..k} a_i B^i**
- Valid digits: 0,…,B−1 (hex uses A=10,…,F=15)
### Converting TO decimal (from base B)
- Expand using powers of B (rightmost digit is B^0).
### Converting FROM decimal (to base B)
- Repeated division by B:
  - divide by B, record remainder
  - stop when quotient = 0
  - read remainders **bottom → top**
### Binary ↔ Octal/Hex shortcuts
- Octal = 2^3 ⇒ group binary in **3s**
- Hex = 2^4 ⇒ group binary in **4s**
- Pad left with zeros if needed.
### Base-B Addition/Multiplication
- Add/multiply like usual, but when a column sum ≥ B:
  - write (sum mod B), carry ⌊sum/B⌋
## Ch 5: Induction, Strong Induction, Recursion, Structural Induction, Recursive Algorithms (Short Notes)
### 5.1 Mathematical Induction (Regular)
- Goal: prove statement **P(n)** true for all integers in some range (often n ≥ 0 or n ≥ 1).
- **2 steps**
  1. **Base case:** prove P(start) is true (start = least n in the claim).
  2. **Inductive step:** assume **P(k)** true (Inductive Hypothesis), prove **P(k+1)** true.
- Conclusion: P(n) holds for all n ≥ start (ladder/domino idea).
#### Induction for Inequalities (the “replace with bigger/smaller” trick)
- You must keep inequality direction correct.
- If you have **A < B**, you may replace **B** with something **bigger** (still true).
- Common moves: use facts like **1 ≤ 2^k** for k ≥ 0, or **k+1 ≥ 5** when k ≥ 4.
#### Induction for Divisibility
- Want: expression is divisible by m for all n.
- Use congruences: show expression ≡ 0 (mod m).
- Inductive step trick: rewrite **P(k+1)** expression in terms of **P(k)** plus a clear multiple of m.
### 5.2 Well-Ordering Principle (WOP)
- Every **nonempty set of nonnegative integers** has a **least element**.
- Used to justify induction and “smallest counterexample” proofs.
- Doesn’t work on rationals (no guaranteed least element).
### Regular vs Strong Induction
- **Regular induction:** assume only **P(k)**, prove **P(k+1)**.
- **Strong induction:** assume **P(start), P(start+1), …, P(k)**, prove **P(k+1)**.
- Use strong induction when the next case depends on **more than one earlier case** (look-back/jump-back).
### 5.3 Recursive Definitions + Structural Induction
#### Recursively defined object = (Base) + (Recursive Rule)
- **Recursive function/sequence:** give initial values + rule using previous term(s).
  - Example format: a(0)=..., a(1)=..., and a(n)=... for n≥2.
- **Recursively defined sets/structures:** define smallest elements + how to build new ones.
#### Structural Induction (for recursively built structures)
- Like induction, but on **how objects are constructed**.
- Steps:
  1. **Base structures:** prove property holds for each base object.
  2. **Build step:** assume property holds for the smaller pieces; prove it holds after combining them by the recursive rule.
- Often used for trees, strings, expressions, recursively defined sets.
### 5.4 Recursive Algorithms + Proving Correctness
- **Recursive algorithm idea:** solve problem by calling itself on a smaller input until a base case.
- Must have:
  - **Base case** (stops recursion)
  - **Progress** (each call reduces size → termination)
#### Euclidean Algorithm (GCD)
- gcd(a,b) = gcd(b mod a, a) for a>0
- Base case: gcd(0,b)=b
- Each step reduces numbers (remainder is smaller).
#### Factorial / Power (classic recursion)
- factorial(0)=1; factorial(n)=n·factorial(n−1)
- power(a,0)=1; power(a,n)=a·power(a,n−1)
#### Proving recursive algorithms work
- Usually by **induction on n** (input size):
  - Base: works on smallest n
  - Step: assume works for k, show works for k+1 using the recursive definition
## Ch 6: Counting, Permutations/Combinations, Binomial Theorem (Short Notes)
### 6.1 Counting Rules (Core “which rule do I use?”)
**Product Rule (AND / sequence)**
- If a process has steps with n1, n2, … choices, total = n1·n2·…
- Use when choices happen one after another.
**Tree Diagrams**
- Visual way to apply the product rule.
- Each root→leaf path = one outcome; count leaves.
**Sum Rule (OR, no overlap)**
- If task can be done in one of several **disjoint** ways: total = n1 + n2 + …
- Keyword: “OR” (and the options don’t overlap).
**Subtraction Rule / Inclusion–Exclusion (OR, with overlap)**
- For two sets: |A ∪ B| = |A| + |B| − |A ∩ B|
- Use when things get double-counted.
**Division Rule (overcounting / “same arrangement”)**
- If each distinct outcome is counted exactly d times, then distinct = n/d
- Classic: circular arrangements (rotations are “the same”).
**Exam triggers**
- AND → multiply
- OR → add
- OR + overlap → add then subtract overlap
- “Same up to rotation/symmetry/duplicates” → divide (after counting raw arrangements)
### 6.3 Permutations vs Combinations
**Permutation = order matters**
- Formula: P(n,k) = n! / (n−k)!
- Interpretation: choose k positions in order.
**Combination = order doesn’t matter**
- Formula: C(n,k) = n! / (k!(n−k)!)
- Relationship: C(n,k) = P(n,k) / k!
**Quick decision**
- If AB and BA count as different → permutation
- If AB and BA are same group → combination
### 6.4 Binomial Theorem + Pascal’s Triangle
**Binomial Theorem**
- (x + y)^n = Σ_{j=0..n} C(n,j) x^(n−j) y^j
- Pattern:
  - power of x decreases: n, n−1, …, 0
  - power of y increases: 0, 1, …, n
  - coefficients are C(n,j)
**Binomial Coefficient**
- C(n,k) = n! / (k!(n−k)!)
**Pascal’s Identity**
- C(n+1, k) = C(n, k−1) + C(n, k)
**Pascal’s Triangle**
- Rows give coefficients of (x+y)^n
- Row n has n+1 terms, starts/ends with 1.
**Common “find a coefficient” move**
- For term x^(n−j) y^j, coefficient is C(n,j) (then multiply by any constants inside the binomial).
## Ch 7: Probability (Short Notes)
### 7.1 Laplace Probability + Basic Rules
**Key setup**
- **Sample space (S)** = all outcomes
- **Event (A)** = outcomes you care about
- **Laplace (equally likely only):**  P(A) = |A| / |S|
**6 core rules**
1) **Total = 1:** sum of all outcome probs = 1  
2) **Range:** 0 ≤ P(A) ≤ 1  
3) **Complement:** P(Aᶜ) = 1 − P(A)  
4) **At least one:** P(≥1) = 1 − P(none)  
5) **OR (Addition):** P(A ∪ B) = P(A)+P(B)−P(A∩B)  
   - If disjoint: P(A∩B)=0 → just add  
6) **AND (Multiplication):** P(A∩B)=P(A)·P(B|A)  
   - If independent: P(B|A)=P(B) → P(A∩B)=P(A)P(B)
**Monty Hall (must-know conclusion)**
- Stay = 1/3, Switch = 2/3 (switching wins when your first pick was wrong).
**Quick exam habits**
- “At least / at most” → try complement first
- “OR” → check overlap (subtract intersection if needed)
- “AND” across steps → conditional probability / independence check
### 7.2 Probability Models + Conditional + Independence + Binomial
**Probability distribution/model**
- List outcomes + probabilities (must be 0..1 and sum to 1)
- For “biased” situations: use relationships + total=1 (ex: T=2H → H+T=1)
**Disjoint union rule**
- If events are pairwise disjoint: P(A∪B∪C…) = P(A)+P(B)+P(C)+…
**Conditional probability**
- Formula: **P(A|B) = P(A∩B) / P(B)** (P(B) ≠ 0)
- Interpretation: restrict sample space to cases where B happened
**Independence**
- A and B independent iff **P(A∩B)=P(A)P(B)**
- Equivalent test (if P(B)>0): **P(A|B)=P(A)**
### Random Variables + Binomial Distribution
**Random variable (RV)**
- A function that assigns a number to each outcome (ex: X = # of heads)
**Binomial setting (Bernoulli trials)**
- Fixed **n** trials, each trial has 2 outcomes (success/failure)
- Constant success probability **p**
- Fail probability **q = 1 − p**
- Trials independent
**Binomial probability**
- **P(X = k) = C(n,k) · p^k · q^(n−k)**
**Fast tactics**
- “Exactly k” → use binomial formula directly
- “At least / at most” → sum binomial terms OR use complement:
  - P(X ≥ k) = 1 − P(X ≤ k−1)
**Checklist for binomial questions**
- Identify n, p, k
- Confirm: 2 outcomes + independent + same p each trial
## Ch 9: Relations (Short Notes)
### 9.1 Relations + How to Represent Them
**Relation from A to B**
- A relation R is any **subset of A × B**
- So: you can include **some pairs**, not all.
**Ways to show a relation**
- Set of ordered pairs: R = {(a,b), ...}
- Arrow diagram (a → b)
- Table/grid of X’s
- Saying “a R b”
**Relations vs Functions**
- **Function:** every a ∈ A maps to **exactly one** b ∈ B
- **Relation:** an a can map to **many b’s or none**
**Counting relations**
- If |A| = n, then |A×A| = n²
- Each pair is “in or out” ⇒ **# relations on A = 2^(n²)**
### Properties of Relations (on a set A)
Let R be on A (so pairs are in A×A).
1) **Reflexive**
- Must have **(a,a) for every a**
- Matrix check: **all 1s on main diagonal**
1) **Symmetric**
- If (a,b) ∈ R ⇒ (b,a) ∈ R
- Matrix check: **M = Mᵀ** (mirror across diagonal)
1) **Anti-symmetric**
- If (a,b) and (b,a) are both in R ⇒ **a=b**
- Translation: for a≠b, you **can’t have both directions**
- Matrix check: off-diagonal mirror spots can’t both be 1
1) **Transitive**
- If (a,b) and (b,c) ∈ R ⇒ (a,c) ∈ R
- “Two-step path implies shortcut exists”
**Professor X exam rule**
- To show TRUE: argue it works for **all cases**
- To show FALSE: give **one counterexample**
**Quick checks from listed pairs**
- Reflexive: are all (a,a) present?
- Symmetric: whenever (a,b) is present, is (b,a) present?
- Anti-symmetric: any a≠b with both (a,b) and (b,a)? If yes → fails.
- Transitive: find chains (a,b),(b,c) and check (a,c).
### Operations on Relations (treat them like sets of pairs)
- **Union:** R₁ ∪ R₂ = pairs in either
- **Intersection:** R₁ ∩ R₂ = pairs in both
- **Difference:** R₁ − R₂ = in R₁ but not R₂  (**order matters**)
- **XOR:** (R₁ ∪ R₂) − (R₁ ∩ R₂)
### Composition of Relations
If R₁ ⊆ A×B and R₂ ⊆ B×C:
- **R₂ ∘ R₁ = {(a,c) : ∃b with (a,b)∈R₁ and (b,c)∈R₂}**
- Think: “go by R₁ then by R₂” (right-to-left like functions)
**Powers**
- R¹ = R
- R² = R ∘ R
- R³ = R² ∘ R, etc.
- Interpretation: R^k shows **k-step reachability**
### 9.3 Matrix Representation of Relations (0–1 matrices)
If A has m elements and B has n elements:
- Matrix is **m×n**
- Entry = 1 if (a_i, b_j) ∈ R, else 0
- Decode: every “1” corresponds to an ordered pair
**Property detection (square matrices only)**
- Reflexive: diagonal all 1
- Irreflexive: diagonal all 0
- Symmetric: equals transpose
- Anti-symmetric: no mirrored off-diagonal pair both 1
- Asymmetric: anti-symmetric + irreflexive
**Matrix ops**
- Union = OR cellwise
- Intersection = AND cellwise
**Composition via Boolean product**
- To compute S∘R, use Boolean matrix multiply (AND then OR)
- **Transitivity test idea:** compute R² and check **R² ⊆ R**
  - If R² has a 1 where R has 0 → not transitive
### 9.5 Equivalence Relations + Partitions
**Equivalence relation = reflexive + symmetric + transitive**
- Not “anti-symmetric”; equivalence needs **symmetric**.
**Equivalence class**
- [a] = {x ∈ S : x ~ a}
**Partition**
A partition of S is a collection of nonempty subsets such that:
1) no empty set
2) disjoint (no overlap)
3) union is all of S (nothing missing)
**Big fact**
- Equivalence relations ⇔ partitions (each equivalence class is a block)
- Example: integers mod m → classes [0], [1], …, [m−1]
## Ch 10: Graphs (Short Notes)
### 10.1 Intro + Types of Graphs
**Graph** G = (V, E)
- V = vertices (must have ≥ 1)
- E = edges (can be empty)
- Edge endpoints are the vertices it touches
- An edge can connect two different vertices, or a vertex to itself (loop)
**Simple graph**
- Undirected edges
- NO loops
- NO multiple edges between same two vertices
**Multigraph**
- Undirected
- Multiple edges allowed
- NO loops
**Pseudograph**
- Undirected
- Multiple edges allowed
- Loops allowed
**Directed graph (digraph)**
- Edges have direction (arrows)
- Edges are ordered pairs (u,v)
- (u,v) ≠ (v,u)
**Simple directed graph**
- Directed
- No multiple directed edges between same ordered pair
- No loops
**Directed multigraph**
- Directed
- Multiple edges allowed
- (typically no loops unless stated)
**Mixed graph**
- Can have BOTH directed and undirected edges
- Can allow multiple edges + loops (depends on definition, but “chaos allowed” idea)
### 10.2 Graph Terminology (Undirected)
**Adjacent / neighbors**
- u and v are adjacent if {u,v} is an edge
**Incident**
- An edge is incident to its endpoints
**Neighborhood**
- N(v) = {all vertices adjacent to v}
**Degree**
- deg(v) = # edges incident to v
- **Loop counts as 2** toward degree
**Special vertices**
- Isolated: deg(v)=0
- Pendant: deg(v)=1
### Handshaking Theorem (Undirected)
If a graph has m edges:
- **∑ deg(v) = 2m**
- Reason: each edge contributes 1 degree to each endpoint ⇒ counted twice.
Quick use:
- If 10 vertices each degree 6 ⇒ sum degrees = 60 ⇒ m = 60/2 = 30 edges
### Directed Graph Terminology
**In-degree / Out-degree**
- in(v) = # arrows into v
- out(v) = # arrows out of v
**Key identity**
- **∑ in(v) = ∑ out(v) = number of directed edges**
- Each directed edge adds +1 to exactly one out-degree and +1 to exactly one in-degree
### Special Graph Families
**Complete graph Kₙ**
- Simple graph with every pair of distinct vertices connected
- Each vertex degree = n−1
- edges = n(n−1)/2
**Cycle Cₙ**
- Simple cycle through n vertices (n ≥ 3)
- Each vertex degree = 2
**Wheel Wₙ**
- Take a cycle and add a center “hub” connected to all cycle vertices
- Looks like spokes
**Hypercube Qₙ**
- Vertices = all n-bit binary strings (so **2ⁿ vertices**)
- Edge between strings that differ in **exactly one bit**
### Bipartite Graphs
**Definition**
- Vertices can be split into two sets (U, W) such that every edge goes **between** U and W
- No edges inside the same group
**Two-color test**
- Color a start vertex blue
- Color its neighbors green
- Keep alternating
- If you ever need a vertex to be both colors ⇒ **NOT bipartite**
- If 2-coloring works ⇒ **bipartite**
**Complete bipartite Kₘ,ₙ**
- Bipartite with partitions sizes m and n
- Every vertex in U connects to every vertex in W
- edges = m·n

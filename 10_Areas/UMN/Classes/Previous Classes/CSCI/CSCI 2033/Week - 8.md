---
type: class
status: archived
created: 2025-11-07
updated: 2025-11-08
area:
  - "[[Final]]"
tags:
  - "#class"
next: "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 9|Week - 9]]"
---
# #Textbook Textbook (Ch - 9 & 10) 
## Chapter 9
Not coming for finals.
## 10.1 Matrix-Matrix Multiplication
Matrix multiplication (C=AB) is a way to combine two compatible matrices, A (size m×p) and B (size p×n), into a third matrix C (size m×n). Core Concept and Formula: 
- The essential rule is that for the product AB to be defined, the **number of columns in** A **must equal the number of rows in** B.
- To find any entry Cij​ of the resulting matrix: $C_{ij}​=\sum_{k=1}​A_{ik​}B_{kj}$​
**Simplified:** The entry in the i-th row and j-th column of C is the **inner product** of the i-th row of A and the j-th column of B. 
- This means every element of C is a vector inner product. 
- Key Interpretations and How to Use Them.

|                      |                                                                                                                        |                                                                                                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Interpretation       | Description                                                                                                            | When to Use It                                                                                                                                                        |
| **Column View**      | Each column of C is simply the matrix A multiplied by the corresponding column of B. (e.g., $C⋅j​=AB⋅j$​)              | When solving multiple systems of linear equations $(Ax_1​=b_1​,Ax_2​=b_2​,…)$ simultaneously, represent the solutions as a single matrix equation: AX=B.              |
| **Composition View** | C represents a single linear function achieved by applying B's function, then A's function. (Covered deeper in §10.2). | When chaining several linear operations together (e.g., rotating, then scaling).                                                                                      |
| **Gram Matrix**      | If G=ATA, the entry Gij​ is the inner product of column i of A and column j of A.                                      | When analyzing the relationship between the columns of a single matrix A, such as checking their orthogonality or calculating the normal equations for least squares. |
**Important Note on Order:** Unlike scalar arithmetic, matrix multiplication is **not commutative**. In general, $AB \not= BA$. If A and B are square and you want to check if they commute, you must calculate both products.
**Complexity:** The computational cost of AB (size m×p times p×n) is roughly 2mnp **flops**.
## 10.2 Composition of Linear Functions
This section provides the _functional_ justification for matrix multiplication. *Core Concept: Chaining Operations*. 
If you have two linear functions, g(x)=Bx and f(y)=Ay, applying g first and then applying f results in a single, combined linear function h(x)=f(g(x)). $$h(x)=f(g(x))=A(Bx)=(AB)x$$
The product matrix C=AB is the matrix that represents the **composite function** h. How to Use It:
1. **Understanding Order:** This confirms why the order of multiplication matters: doing operation B then operation A (represented by AB) is different from doing operation A then operation B (represented by BA).
2. **Modeling Sequential Effects:** When one system's output becomes the next system's input (like state transitions in a dynamical system over multiple steps, or chaining several steps in signal processing), composition is the right tool.
3. **The Second Difference Matrix (Δ**): This is a critical example. The difference matrix D calculates consecutive differences in a vector x (Dx). The product of two difference matrices, $Δ=D_{n−1}​D_n$​, calculates the **second differences**.
	- Δx calculates terms like xi​−2xi+1​+xi+2​. This is extremely useful for measuring the smoothness or roughness of a signal or series.
4. **Chain Rule in Calculus:** For composition of vector-valued functions, the derivative matrix (Jacobian) of the composite function h is the matrix product of the individual Jacobian matrices: $Dh(z)=Df(g(z))Dg(z)$
## 10.3 Matrix Power
Matrix power, Ak, is simply the matrix A multiplied by itself k times. This is only meaningful if A is a square matrix. Core Formulas and Concepts:
1. **Propagating State in Linear Dynamical Systems (LDS):** For an LDS defined by $x_{t+1}​=Ax_{t}$​, the state L periods into the future is found using the L-th power of the dynamics matrix A: $x_{t+L}​=A^Lx_{t}​$
	- AL is the single matrix that encapsulates the effect of L sequential time steps.
2. **LDS with Input (Control):** If the system has an input $u_t​ (x_{t+1}​=Ax_t​+Bu_t​)$, the future state L steps ahead depends on the initial state propagated by AL and a series of past inputs, each propagated by a corresponding power of A: $$x_{t+L}​=A^Lx_t​+A^{L−1}Bu_t​+A^{L−2}Bu_t+1​+⋯+Bu_{t+L−1}$$
3. **Graph Paths:** If A is the adjacency matrix of a directed graph, the entry (AL)ij​ is the **number of paths of length** L **from vertex** j **to vertex** i. How to Use It:
	- **LDS Analysis:** Powers are essential for simulating and analyzing the long-term behavior of dynamic systems. For instance, analyzing how the current population distribution (state xt​) will evolve into the future population distribution (xt+L​) requires computing AL.
	- **Network Analysis:** AL allows you to quickly count how many distinct ways (paths) exist to get from one node to another in exactly L steps in a network.
## 10.4 QR Factorization
The QR factorization (A=QR) is the matrix representation of the [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 5#5.4 Gram–Schmidt algorithm|Gram-Schmidt algorithm (from Chapter 5)]]. It is a method of decomposing a matrix A (size m×n, assuming linearly independent columns) into a product of two matrices. Core Formula and Components $$A=QR$$
1. **Q Matrix:** Q is an m×n matrix whose columns are **orthonormal** (unit length and mutually orthogonal). This property is expressed as: $Q^TQ=I$.
2. **R Matrix:** R is an n×n **upper triangular** matrix with positive entries on the diagonal.
	Key Concepts: 
	- **Orthogonal Matrices:** A square matrix Q whose columns are orthonormal is called **orthogonal**. Orthogonal matrices are crucial because they preserve geometric properties: they keep the length of vectors, the inner product between vectors, and the angle between vectors unchanged when multiplied.
	- **Inverse Relation:** Because Q has orthonormal columns, calculating its effective inverse is easy: for a square orthogonal matrix Q, $Q^{−1}=Q^T$. This is highly advantageous in computation.
3. **Solving Square Systems (Ax=b**): If A is square and invertible, you can solve Ax=b by:
	- Compute A=QR.
	- The solution is $x=R^{−1}Q^Tb$. c. Solve the triangular system $Rx=Q^Tb$ using **back substitution** (a fast, n2 flop procedure).
4. **Solving Least Squares Problems (Minimize** $∣∣Ax−b∣∣^2$): For over-determined systems where A is tall (m>n), the unique least squares solution x^ is found similarly: Compute A=QR.
	- The solution is $x=R^{−1}Q^Tb$. c. Solve the triangular system $Rx=Q^Tb$ using **back substitution** (a fast, n2 flop procedure).
**Method Summary:** When asked to solve complex systems like Ax=b or least squares minimization problems, the primary method is generally to find the **QR factorization** of the coefficient matrix A and use the resulting R matrix with back substitution. This approach costs approximately 2mn2 **flops**.

---
# #Lecture Lecture
## #Jupyter Jupyter
### Matrix Factorizations
Remember, we have the property:
$$D_{ij} = \begin{cases} 
  d_j & \text{ if }i = j\\
  0 & \text{ if }i\neq j
\end{cases}$$
where $\vec{d}$ is the vector of diagonal entries.
- *Multiplication of a matrix $A$ on the right by $D$ results in the columns of $A$ being scaled*.
- *Multiplication of a matrix $A$ on the left by $D$ results in the rows of $A$ being scaled*.
1. **Inverse Matrix**
	The matrix which reverses the operation of another matrix is referred to as the *inverse* of the matrix. For diagonal matrices $D$, we can define the inverse in terms of the relation below. $$D^{-1}_{ij} = \begin{cases}\frac{1}{d_j} & \text{ if }i = j\\0 & \text{ if }i\neq j\end{cases}$$where $\vec{d}$ is the vector of diagonal entries from the original diagonal matrix $D$.
	- The inverse of matrix $A$ is the matrix $X$ which satisfies the following algebraic relations: $$I_n = A\ X = X\ A,$$where $I_n$ is the $n\times n$ identity matrix.
2. *Matrix Factorization*:
	When we compute a matrix-matrix product, we are implicitly computing a matrix factorization. Consider the example where we scale the columns of $A$ by the inverse matrix $D^{-1}$ from above. $$A\ D^{-1} = S$$Re-writing this equation to solve for $A$, we can observe the factorization. $$\begin{align*} A\ D^{-1} &= S \\ A\ D^{-1}\ D &= S\ D \hspace{0.5in}\text{ multiply on the right by D}\\ A\ (D^{-1}\ D) &= S\ D \\ A\ (I_n) &= S\ D \hspace{0.5in}\text{ apply inverse property of D}\\ A &= S\ D \hspace{0.5in}\text{ apply property of identity matrix}\\ \end{align*}$$What we are left with is a factorization of $A$ in terms of the scaled matrix $S$ and the scalings $D$.
	- Inverse Scaling: `Dinv = diag([1/x for x in d])`
3. *Useful Matrix Factorizations*:
	- `rotate(angle,0,1,2)` is a $2\times 2$ **rotation matrix** by angle $−π/4$ (i.e., rotate **clockwise** 45°).
	- `scalar = 1/√2` is a **uniform scaling** by $1/\sqrt{2}$.
	So: $G = \frac{1}{\sqrt{2}}\,R(-\pi/4)$ 
	- A matrix that **undoes** what A does: A ≈ “rotate by $+\pi/4$ then scale by $\sqrt{2}$​”.
	- G ≈ “scale by $1/\sqrt{2}$ then rotate by $-\pi/4$”.
	That’s exactly the opposite transformation. So geometrically:
	-  G is (approximately) $A^{-1}$, the inverse of A.
	- If $G = A^{-1}$, then G @ A = I, the identity matrix.
4. [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 9#Householder reflector|Continuing Householder reflector]]
## #Quiz Quiz - 6
2. *Writing the system as $Ax=b$*: The system is $\begin{cases} 3x_1 + 1x_2 = 7\\ -1x_1 + 4x_2 = 11 \end{cases}$
	- We want the matrix equation $A \begin{bmatrix}x_1\\x_2\end{bmatrix} = \begin{bmatrix}7\\11\end{bmatrix}$
	- By definition, multiplying a 2×2 matrix by a 2-vector works **row by row**: $$\begin{bmatrix} a_{11} & a_{12}\\ a_{21} & a_{22} \end{bmatrix} \begin{bmatrix}x_1\\x_2\end{bmatrix} = \begin{bmatrix} a_{11}x_1 + a_{12}x_2\\ a_{21}x_1 + a_{22}x_2 \end{bmatrix}$$So each **row of A** must match the coefficients in one equation:
	- Then matrix–vector multiplication can also be seen as a **linear combination of columns**: $Ax = x_1 a_1 + x_2 a_2$. 
	- So the system $Ax = b$ is the statement: *“The vector b is a linear combination of the column vectors $a_1, a_2$ with coefficients $x_1, x_2$”.*
		- First equation $3x_1 + 1x_2 = 7$ ⇒ first row is $[3 1]$.
		- Second equation $-1x_1 + 4x_2 = 11$ ⇒ second row is $[−1,4]$.
		- That gives $$A = \begin{bmatrix} 3 & 1\\ -1 & 4 \end{bmatrix}, \qquad x = \begin{bmatrix}x_1\\x_2\end{bmatrix}, \qquad b = \begin{bmatrix}7\\11\end{bmatrix}$$Check: $$A x = \begin{bmatrix} 3 & 1\\ -1 & 4 \end{bmatrix} \begin{bmatrix}x_1\\x_2\end{bmatrix} = \begin{bmatrix} 3x_1 + 1x_2\\ -1x_1 + 4x_2 \end{bmatrix} = \begin{bmatrix}7\\11\end{bmatrix}$$which is exactly the original system. That’s why the second option is correct.
3. PageRank Question
4. PageRank graph
5. Fuck all matrix
---
# #Homework Coding HW - 6
## PageRank Algorithm
Think of a person randomly clicking links on the web:
- At any time they’re on some page.
- From that page they either
    - follow one of the outgoing links, or
    - “teleport” to some random page (typing a URL, bookmark, etc).
So the _state_ of the system is a probability vector, $x_t\in\mathbb{R}^n,$ where $(x_t)_i$ = probability you’re on page $i$ at step $t$.
Each step is a **linear dynamical system / Markov model**: $x_{t+1} = G\,x_t$​
- For some $n\times n$ matrix $G$ whose columns sum to $1$ and have non-negative entries (a _column-stochastic_ matrix). The steady-state vector $x_\star$ with $Gx_\star = x_\star$​ is the PageRank vector: entries = “importance scores” for sites.
This is exactly the kind of thing Chapter 9 calls a Markov / linear dynamical system $x_{t+1}=A x_t$. Lab 6 is: build $G$ from the web graph and then approximate $x_\star$ by iterating.
1. *Step 1 – From file to adjacency matrix $A$*:
	The file `web-Stanford-small.txt` is in **coordinate format**:
	- Each line: `i j` means “page $i$ has a hyperlink to page $j$.”
	- There are $n=281903$ pages, so $A$ is an $n\times n$ matrix.
	- Definition: $A_{ij} = \begin{cases} 1 & \text{if website } i \text{ links to website } j,\\ 0 & \text{otherwise.} \end{cases}$
	- So if you see: `0 1 1 2 2 0` that corresponds to $A = \begin{bmatrix} 0 & 0 & 1\\ 1 & 0 & 0\\ 0 & 1 & 0 \end{bmatrix}$​.
	- All you’re doing in this task is reading the pairs and setting the right entries of $A$ to $1$.
2. *Step 2 – Transition matrix $S$*: 
	Now we want a matrix that tells us: “If I am on page $j$, what is the probability that I go to page $i$ next?”. That’s the **transition matrix** $S$.
	Starting from adjacency $A$:
	1. Make a copy:`S = 1.0 * A    # float copy of adjacency matrix`
	2. Compute each column sum: `col_sums = [sum(S.data[i][j] for i in range(n)) for j in range(n)]`
	    - `col_sums[j]` = number of outgoing links from page $j$.
	3. **Scale each column** so it sums to $1$:
    ```python
    for j in range(n):
    if col_sums[j] != 0:
        for i in range(n):
            S.data[i][j] = S.data[i][j] / col_sums[j]
    else:
        # dangling node: no outgoing links
        for i in range(n):
            S.data[i][j] = 1.0 / n
    ```
    - If page $j$ has $k$ links, then each outgoing link gets probability $1/k$. $$S_{ij} = \frac{A_{ij}}{\sum_{i'} A_{i'j}}$$
    - If page $j$ has **no links** (a dangling node), we don’t want a whole zero column (the random surfer would get “stuck”). So we set that whole column to $1/n$ = uniform over all pages.
	After this:
	- Each column of $S$ sums to $1$.
	- $S_{ij}$ = probability to go from page $j$ to page $i$ **by following a link**.
	This is the standard “random surfer” Markov model.
3. *Step 3 – The damped Google matrix $G$*:
	Real web surfers don’t _always_ follow a link. Sometimes they just jump somewhere random. We model that with a **damping factor** $\alpha$ (usually $\alpha=0.85$):
	- With probability $\alpha$: follow a link according to $S$.
	- With probability $1-\alpha$: teleport uniformly to any page.
	Mathematically: $$G = \alpha S + (1-\alpha)\frac{1}{n}J$$where $J$ is the $n\times n$ matrix of all ones, so $\frac{1}{n}J$ has every column = uniform vector $(1/n,\dots,1/n)$.
	Your code:
```python
alpha = 0.85

J = Matrix([[1 for _ in range(n)] for _ in range(n)])
G = alpha * S + ((1 - alpha) / n) * J
```
Now $G$ is also column-stochastic (columns sum to $1$). Its $(i,j)$ entry is: $$G_{ij} = \alpha S_{ij} + (1-\alpha)\frac{1}{n}$$the total probability of going from page $j$ to $i$ in one step (link or teleport).
4. *Step 4 – PageRank iteration (power method)*
	We want a vector $v$ with $Gv = v$ and $|v| = 1$ (some fixed norm). That’s the _dominant eigenvector_ of $G$ with eigenvalue $1$.
	We approximate it by repeatedly multiplying by $G$ and re-normalizing:
	1. Start from a uniform vector: $v_0 = \begin{bmatrix}1/n \\ 1/n \\ \vdots \\ 1/n\end{bmatrix}$
		`v = Matrix([[1.0 / n] for i in range(n)])`
	2. Repeat for, say, 10 iterations (or more):
	```python
	for i in range(10):
	    w = G @ v              # multiply
	    norm_w = w.norm()      # compute ||w||
	    v = (1.0 / norm_w) * w # normalize
	```
    Geometrically:
    - Each step $w = Gv$ moves the probability distribution one “click” forward.
    - Normalizing keeps the vector from growing/shrinking numerically but doesn’t change its direction.
    - For a nice, well-behaved $G$, this converges to the eigenvector $v_\star$ associated with the largest eigenvalue (here $\lambda=1$).
    Result: $v$ is your **PageRank vector**. Entry $v_i$ is the steady-state probability of being on page $i$ — that’s the “importance score.”
    You can think of this as the same kind of iteration you saw for linear dynamical systems $x_{t+1} = Ax_t$ in Chapter 9, just with a probability interpretation.
---

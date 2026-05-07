---
type: class
status: archived
created: 2025-10-17
updated: 2025-10-19
area:
  - "[[Final]]"
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Midterm - 1|Midterm - 1]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Homework"
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 6|Week - 6]]"
---
# #Textbook Textbook (Ch - 5 & 6)
## Chapter 5: Linear independence
### 5.1 Linear dependence and independence
**Linear Dependence**: A collection of n-vectors $a1​,…,ak$​ is considered **linearly dependent** if you can create the zero vector (the vector containing all zeros) as a linear combination of these vectors, using coefficients ($β_{1},…,β_{k}$) that are **not all zero**. 
- **Mathematical Condition:** $$β_{1}​a_{1}​+⋯+β_{k}​a_{k}​=0$$Where at least one $\beta_{i}​=0$. the only linear combination of the vectors that equals the zero vector is the linear combination with all coefficients zero.
- **Easier Interpretation:** If vectors are linearly dependent, it means there is redundancy: at least one vector in the collection can be expressed as a linear combination of the others.
- **Examples:** A single vector is linearly dependent only if the vector itself is the zero vector. Any list of vectors containing the zero vector is automatically linearly dependent. Two vectors are dependent if one is a multiple of the other.
**Linear Independence**: A collection of n-vectors $a1​,…,ak$​ is **linearly independent** if it is _not_ linearly dependent.
- **Mathematical Condition:** The equation $β1​a1​+⋯+βk​ak​=0$ only holds if **all** coefficients are zero (β1​=⋯=βk​=0).
- **Key Property:** When a set of vectors is linearly independent, the coefficients used to express any vector x as their linear combination are **unique**.
- **Supersets and Subsets:** If you add vectors to a linearly dependent collection, the resulting superset is also dependent. Any non-empty subset of a linearly independent collection remains linearly independent.
### 5.2 Basis
A set of vectors acts as a fundamental building block for all other vectors in that space.
The Concept of Basis: A collection of n vectors a1​,…,an​ is a **basis** for n-vectors if they are **linearly independent**.
- **Key Result (Expansion in a Basis):** If a1​,…,an​ form a basis, then _any_ n-vector b can be written uniquely as a linear combination (or expansion) of these vectors: $$b=\alpha_{1}​a_{1}​+⋯+\alpha_{n}​a_{n}$$The coefficients α1​,…,αn​ are unique.
- **Example:** The standard unit vectors e1​,…,en​ are a basis. 
- Independence-Dimension Inequality (A Fundamental Rule): If you have a collection of linearly independent n-vectors, the number of vectors (k) cannot exceed the dimension (n). **In simpler terms:** You can have at most n linearly independent vectors in an n-dimensional space. 
- **Consequence:** Any collection of n+1 or more n-vectors must be linearly dependent. For example, three 2-vectors must be linearly dependent. 
Basis Example: Cash Flows, For modeling cash flows over n periods, a natural basis exists that includes the initial payment vector (e1​) and n−1 single-period loan vectors (li​).
- Any cash flow vector c can be expressed as a linear combination of these basis vectors.
- The first coefficient of this expansion (α1​) is exactly the **Net Present Value (NPV)** of the cash flow, calculated using the interest rate r. This implies that any cash flow can be replicated by an initial income equal to its NPV, plus a series of one-period loans.
### 5.3 Orthonormal vectors
Orthonormal vectors are highly structured sets of linearly independent vectors.
Definitions:
1. **Orthogonal Vectors:** A collection of vectors is **orthogonal** (or mutually orthogonal) if every distinct pair of vectors is perpendicular, meaning their inner product is zero ($ai​\perp aj$ or​ $a_{i}^T​a_{j}​=0$).
2. **Orthonormal Vectors:** A collection of vectors is **orthonormal** if they are orthogonal and every vector is normalized, meaning its norm (length) is one (∥ai​∥=1).
• **Compact Inner Product Condition:** For an orthonormal set, $a_{i}^T​a_{j}​=1$ if i=j, and 0 if i=j.
Significance: 
- **Linear Independence:** Orthonormal vectors are always linearly independent.
- **Easy Coefficients:** If a vector x is known to be a linear combination of orthonormal vectors a1​,…,ak​, finding the coefficients is simple: βi​=aiT​x. The coefficient is just the inner product of the vector with the corresponding basis vector.
- **Orthonormal Basis:** If n orthonormal n-vectors form a basis, this is called an **orthonormal basis**. The expansion of any vector x is given by the **orthonormal expansion formula**: $$x=(a_{1}^T​x)a_{1}​+⋯+(a_{n}^T​x)a_{n}$$
### 5.4 Gram–Schmidt algorithm
The Gram–Schmidt algorithm is a procedure for testing linear independence and generating an orthonormal set of vectors.
Algorithm Purpose: The algorithm takes a list of n-vectors a1​,…,ak​ and aims to produce a sequence of orthonormal vectors q1​,…,qk​. It also explicitly checks for linear independence.
Core Steps: The algorithm proceeds iteratively for each input vector ai​:
1. **Orthogonalization (Step 1):** The component of ai​ that is parallel to the previously calculated orthonormal vectors (q1​,…,qi−1​) is subtracted from ai​. This yields a temporary vector q~​i​ that is guaranteed to be orthogonal (perpendicular) to all previous qj​ vectors.
2. **Test for Linear Dependence (Step 2):** If the resulting vector q~​i​ is zero, the algorithm terminates early. This means the original vector ai​ was a linear combination of a1​,…,ai−1​, and thus the collection is linearly dependent.
3. **Normalization (Step 3):** If q~​i​ is non-zero, it is divided by its own norm (∥q~​i​∥) to scale it to unit length, resulting in the new orthonormal vector qi​.
	Outcome and Complexity: 
	- **If successful:** If the algorithm runs to completion without early termination, the original vectors a1​,…,ak​ are linearly independent. The resulting vectors q1​,…,qk​ form an orthonormal set.
	- **QR Factorization Connection:** The results of the Gram–Schmidt algorithm can be expressed using matrices as the **QR factorization** of A: A=QR.
	- **Complexity:** The complexity of the Gram–Schmidt algorithm is approximately 2nk2 flops, where n is the vector length and k is the number of vectors. The computational cost scales linearly with the dimension n and quadratically with the number of vectors k.
## Chapter 6: Matrices
**Definition and Dimensions:** A matrix is a **rectangular array of numbers**. Its size (or dimensions) is given as **$m \times n$**, where $m$ is the number of rows and $n$ is the number of columns. The **$i, j$ elements** of a matrix $A_{ij}$ is the value in the $i$th row and $j$th column.
Matrix Types: 
	- **Square matrix:** $m = n$.
	- **Tall matrix:** $m > n$.
	- **Wide matrix:** $n > m$.
	- An $n$-vector is an $n \times 1$ matrix (column vector). A $1 \times n$ matrix is a **row vector**.
**Submatrices**
An $m \times n$ matrix $A$ can be viewed as:
1. A concatenation of its $n$ column vectors $a_1, \ldots, a_n$.
2. A stacking of its $m$ row vectors $b_1^T, \ldots, b_m^T$. **Block matrices** are matrices whose entries are themselves submatrices (or blocks). **Colon notation** $A_{p:q, r:s}$ is used to denote submatrices extracted from rows $p$ through $q$ and columns $r$ through $s$.
Applications of Matrices are used to represent data indexed by two quantities (like a table), such as:
	- **Images** ($M \times N$ matrix for monochrome images).
	- **Asset returns** ($T \times n$ matrix $R$ where $R_{ij}$ is the return of asset $j$ in period $i$).
	- A **data matrix** or **feature matrix** $X$ can represent a collection of $N$ feature $n$-vectors $x_1, \ldots, x_N$ as its columns.
	- An **adjacency matrix** $A$ represents a directed graph where $A_{ij}=1$ if there is an edge from vertex $j$ to vertex $i$.
### Zero and Identity Matrices
**Zero Matrix ($0$):** All entries are zero. The size is usually determined by context.
**Identity Matrix ($I$):** A square matrix with ones on the diagonal and zeros elsewhere. Its columns are the standard unit vectors $e_1, \ldots, e_n$.
**Sparse Matrix:** A matrix with many zero entries. The **density** is $\text{nnz}(A)/(m.n)$. The number of non-zeros of a sparse matrix A is the number of entries in its sparsity pattern ,and denoted $nnz(A)$. If A is m.n we have nnz(A) is less than or equal to m.n. Its density is $\text{nnz}(A)/(m.n)$),which is no more than one.
**Diagonal Matrix:** A square matrix where all off-diagonal entries are zero ($A_{ij}=0$ for $i \ne j$). Notation: $\text{diag}(a_1, \ldots, a_n)$.
**Triangular Matrices:** Upper triangular ($A_{ij}=0$ for $i>j$) or lower triangular ($A_{ij}=0$ for $i<j$). A triangular n.m matrix A has upto $n(n+1)/2$ non-zero entries, i.e. ,around half its entries are zero. Triangular matrices are generally not considered sparse matrices, since their density is around 50%.
### Transpose, Addition, and Norm
The **transpose** of an $m \times n$ matrix $A$, denoted $A^T$, is an $n \times m$ matrix where $(A^T)_{ij} = A_{ji}$. The rows and columns are swapped. $(A^T)^T = A$. A square matrix $A$ is **symmetric** if $A = A^T$.
- **Addition:** Matrices of the same size are added element-wise. 
	- Property: $(A + B)^T = A^T + B^T$.
- **Scalar Multiplication:** Multiply every element by the scalar $\gamma$.
- **Matrix Norm**: The **norm of an $m \times n$ matrix $A$** (or Frobenius norm, $|A|_F$) is the square root of the sum of the squares of its entries:__$$ ||A|| = \sqrt{\sum_{i=1}^m \sum_{j=1}^n A_{ij}^2} $$
	- The matrix norm satisfies the standard norm properties (nonnegativity, definiteness, nonnegative homogeneity, and the triangle inequality). The distance between two matrices is defined as $||A-B||$.

### Matrix-Vector Multiplication
If $A$ is an $m \times n$ matrix and $x$ is an $n$-vector, the product $y = Ax$ is an $m$-vector. Interpretations:
1. **Row interpretation:** The $i$th element of $y$ ($y_i$) is the **inner product** of the $i$th row of $A$ and the vector $x$.
2. **Column interpretation:** $y = Ax$ is a **linear combination of the columns of $A$**, where the coefficients are the elements of $x$: $$ y = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n $$
Special Examples: The product of $A$ and the unit vector $e_j$ selects the $j$th column of $A$: $A e_j = a_j$.
- The **difference matrix** $D$ (6.5) yields the differences of consecutive entries of $x$: $(Dx)_i = x_{i+1} - x_i$.
- The notation $a^T b$ for the inner product is consistent with matrix multiplication, treating $a^T$ as a $1 \times n$ matrix and $b$ as an $n \times 1$ matrix.

### Matrix Properties and Linear Independence
Matrix-vector multiplication provides a concise way to define linear independence of matrix columns:
- The columns of $A$ are **linearly dependent** if $Ax = 0$ for some $x \ne 0$.
- The columns of $A$ are **linearly independent** if $Ax = 0$ implies $x = 0$.
Matrix-Vector Product Properties: Matrix-vector multiplication satisfies associativity and distributivity properties:
- $A(u+v) = Au + Av$
- $(A+B)u = Au + Bu$
- $(\alpha A)u = \alpha(Au) = A(\alpha u)$
### Complexity
In complexity analysis, operations are counted in floating point operations (flops). For an $m \times n$ matrix $A$:
- Matrix addition ($A+B$) or scalar multiplication ($\alpha A$): $mn$ flops.
- Matrix transposition ($A^T$): 0 flops (only copying time).
- Matrix-vector multiplication ($Ax$): $2mn$ flops.
- Matrix storage: $8mn$ bytes. Sparse matrix storage requires approximately $16 \text{nnz}(A)$ bytes.


---
# #Lecture Lecture
## #Jupyter Jupyter


---
# #Homework Coding HW


---

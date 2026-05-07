---
type: class
status: archived
created: 2025-11-14
updated: 2025-11-15
area:
  - "[[Final]]"
tags:
  - "#class"
  - "#Lecture"
  - "#Quiz"
  - "#Jupyter"
  - "#Homework"
  - "#Textbook"
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 10]]"
---
# #Textbook Textbook (Ch - 10) 
[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 8#Textbook Textbook (Ch - 9 & 10)|Entire thing except householder reflector]]

---
# #Lecture Lecture
## #Jupyter Jupyter
### Matrix Factorizations
### Householder reflector
We want a matrix Q that:
- **Reflects** vectors across some line (or hyperplane), 
- Is **orthogonal**: $Q^\top Q = I$
- Is its **own inverse**: $Q^{-1} = Q^\top = Q$.
The standard Householder reflector has the form: $$Q = I - 2vv^\top$$where v is a **unit vector** ($\|v\| = 1$). Given a vector x, construct a reflector $Q = I - 2vv^\top$ so that $Qx = \pm\|x\| e_1$.
Geometrically:
- v is the **normal** to a mirror line/plane.
- Q reflects any vector across the hyperplane perpendicular to v.
Important properties (this is what makes it useful):
- Q is orthogonal ⇒ it preserves lengths and angles.
- $Q^{-1} = Q^\top = Q$ ⇒ super easy to invert.
- We can _choose_ v so that, when we apply Q to some vector x, the result has zeros in certain positions (this is the trick used in QR factorization).
1. **How to choose v**: 
	There’s a standard, numerically stable formula: 
	1. Start with your vector x.
	2. Define: $$u = x + \operatorname{sgn}(x_1)\,\|x\|\,e_1$$where $x_1$ is the first component of x.
	3. Normalize: $$v = \frac{u}{\|u\|}$$
	4. Then $Q = I - 2vv^\top$ will satisfy $Qx = -\operatorname{sgn}(x_1)\,\|x\|\,e_1$ i.e. same length as x, all zeros below the first entry. 
	The sign choice (`sgn(x_1)`) is for numerical stability (avoids subtracting nearly equal numbers).
### Connecting to my code
Here is your snippet, annotated.
```python
# constructing a Householder Reflector
I = eye(2)                 # 2x2 identity matrix

x = A[:2,0:1]              # extract a column from A (a 2x1 vector)
print(x)
```
- `eye(2)` = identity matrix III of size 2×2.
- `A[:2,0:1]` takes the first **two rows** of column 0 → a vector $x\in\mathbb{R}^2$. 
	- In a larger QR algorithm, you would take the sub-vector from row k downwards. Next:
```python
# compute v = x + -sgn(x)||x||e_1
x[0][0] += x.norm() if x[0][0] >= 0 else -x.norm()
```
This line is encoding $$u = x + \operatorname{sgn}(x_1)\,\|x\|\,e_1$$
- `x[0][0]` is the first component x1​. 
- `x.norm()` = ∥x∥.
- If `x[0][0] >= 0`, we do `x1 += ||x||`; else we do `x1 += -||x||`.  
    That’s exactly “add `sgn(x1)*||x||` to the first entry”.
So now the vector `x` actually holds `u` (they’re reusing the same variable). 
- Then they normalize: `# normalize v = (1/x.norm()) * x print(v)`
	- Now `v` is the unit vector: $$v = \frac{u}{\|u\|}$$exactly as in the formula. Finally, they build the reflector:
```python
Qt = I - 2*v@v.transpose()    # Householder Reflector formula
print(Qt)
```
This is: $$Q = I - 2vv^\top$$They call it `Qt` because they know later they’ll use its transpose as `Q`. But remember, for a Householder reflector, $Q^\top = Q$, so it doesn’t really matter (up to floating-point noise).
- Moving on we work on a larger data set and we use the householder reflector again and again: 
	- Each Householder reflector only zeroes out **one column below the diagonal**. To turn a whole tall matrix into an upper-triangular one, you have to do this **for each column** (one after another).
## #Quiz Quiz - 7
1. The product of two matrices $(A_{m\times n})$ and $(B_{n\times p})$ can be computed as follows:$$C_{i,j} = \sum_{k=0}^{n-1} A_{i,k}\, B_{k,j}$$
2. **True version:** The Householder QR algorithm computes the QR factorization of a matrix A using **Householder reflection matrices** (orthogonal reflectors), not rotation matrices.
3. We can invert any matrix by inverting all the entries of the matrix, i.e. $A^{-1}_{ij} = \dfrac{1}{A_{ij}}$​.
	**True version:** We can invert a **diagonal** matrix D with nonzero diagonal entries by inverting its diagonal entries: $$(D^{-1})_{ij} = \begin{cases} \dfrac{1}{D_{ii}} & i = j,\\[4pt] 0 & i \ne j. \end{cases}$$In general, the inverse of a matrix is **not** the elementwise reciprocal.
4. **True version:** The Householder QR algorithm computes the factorization A = QR by applying a sequence of Householder reflectors to A to form R; the matrix Q is the product of those reflectors (often stored implicitly via their vectors).
---
# #Homework Coding HW - 7
Review the lab comments for understanding the complete optimization of householder reflector. Key points: 
- **How a single step updates the matrix**$$A_{k:m,\;k:n} \;\leftarrow\; A_{k:m,\;k:n} - 2\,\vec{v}\,\big(\vec{v}^{T} A_{k:m,\;k:n}\big).$$
- **Why we store vectors $\vec{v}_k$ instead of $Q$**: Storing full $Q$ would be $m^{2}$ memory; storing the vectors $\vec{v}_k$ is $n\cdot m$ and we can always apply $Q$ or $Q^{T}$ to a vector using the reflector formulas.
- **How to apply $Q^{T}$ and $Q$**
	- $Q^{T}\vec{b}$: apply reflectors for $k = 0 \rightarrow n-1$.
	- $Q\vec{x}$: apply reflectors for $k = n-1 \rightarrow 0$.
- **Reconstructing $Q$ or $Q^{T}$**
	- Columns of $Q^{T}$ are $Q^{T}\vec{e}_i$.
	- Columns of $Q$ are $Q\vec{e}_i$.
---

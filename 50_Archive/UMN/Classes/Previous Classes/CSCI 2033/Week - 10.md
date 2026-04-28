---
type: class
status: archived
created: 2025-11-21
updated: 2025-11-22
area:
  - "[[Final]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2033/Week - 11|Week - 11]]"
---
# #Textbook Textbook (Ch - 11) 
## 11.1 Left and Right Inverses
When working with matrices, the concept of division must be split into two operations because matrix multiplication is not generally commutative $(AB \not= BA)$. Core Concepts:
1. **Left Inverse (C):** A matrix C is a left inverse of A if multiplying C on the left side of A yields the identity matrix: CA=I.
	- **Existence Condition:** A matrix A is left-invertible if and only if **the columns of** A **are linearly independent**.
	- **Applicability:** Only square or **tall** matrices (m>n) can be left-invertible.
2. **Right Inverse (B):** A matrix B is a right inverse of A if multiplying B on the right side of A yields the identity matrix: AB=I.
	- **Existence Condition:** A matrix A is right-invertible if and only if **the rows of** A **are linearly independent**.
	- **Applicability:** Only square or **wide** matrices (m<n) can be right-invertible.
	How to Use These Inverses

| Problem Type              | Matrix Shape | Solution Method                                                                                                   | Why it works                                                                        |
| ------------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Over-determined** Ax=b  | Tall (m>n)   | Use a Left Inverse C. If $A(Cb)=b$, then $x=Cb$ is the **unique solution**. If $A(Cb)\not=b$, no solution exists. | Multiplying Ax=b on the left by C yields $C(Ax)=Cb$, which simplifies to $Ix=x=Cb$. |
| **Under-determined** Ax=b | Wide (m<n)   | Use a Right Inverse B. $x=Bb$ is **a solution**.                                                                  | Multiplying x=Bb on the left by A yields $A(Bb)=(AB)b=Ib=b$.                        |
## 11.2 Inverse
When a matrix is both left-invertible and right-invertible, it must be square, and its left and right inverses are equal and unique. Core Concepts:
1. **Inverse ($A^{−1}$):** If A has both a left and right inverse, that unique matrix is the inverse, $A^{−1}$, satisfying $AA^{−1}= A^{−1}A=I$.
2. **Requirement:** Invertible matrices must be **square**.
3. **Equivalence for Square Matrices:** For a square matrix A, being invertible is equivalent to having linearly independent columns, having linearly independent rows, having a left inverse, or having a right inverse.
4. **Solving Square Systems:** If A is invertible, the system Ax=b has the **unique solution** $x=A^{−1}b$ for any vector b. Important Formulas and Relationships:
	- **Transpose Inverse:** The inverse of a transpose is the transpose of the inverse: $(A^T)^{−1}=(A^{−1})^T$.
	- **Product Inverse:** The inverse of a product is the product of the inverses in reverse order: $(AB)^{−1}=B^{−1}A^{−1}$.
	- **Orthogonal Matrices:** If a square matrix A has orthonormal columns (it is an orthogonal matrix), its inverse is simply its transpose: $A^{−1}=A^T$.
	- **Dual Basis:** If A is invertible, the rows of $A^{−1}$ (called the dual basis) can be used to find the coefficients required to write any vector x as a linear combination of the columns of A.
## 11.3 Solving Linear Equations (Computational Methods)
While the formula $x=A^{−1}b$ is mathematically elegant, directly computing $A^{−1}$ is generally computationally inefficient. Instead, practical methods focus on factor-solve schemes, particularly those involving the QR factorization.
1. **Back Substitution (Solving Triangular Systems)**: This is a fast method used when the coefficient matrix R is **triangular** (upper or lower). The system $Rx=b$ is solved by finding the components of x one by one, starting from the last component ($x_n$​) in an upper triangular system, or the first component ($x_1$​) in a lower triangular system.
	- **Method:** For an upper triangular matrix R, solve for $x_n$​ first, substitute that value into the n−1 equation to find $x_n−1$​, and continue upwards.
	- **Complexity:** This takes only $n^2$ flops, making it very fast.
2. Solving Ax=b via QR Factorization (Algorithm 11.2)
	This is the standard, efficient method for finding x when A is square and invertible.
	- **Formula Derivation:** Since A is invertible, it has a QR factorization A=QR. Substituting this into $x=A^{−1}b$ yields $x=R^{−1}Q^Tb$.
	- **Steps (Factor-Solve):**
	    1. **Factor:** Compute the QR factorization A=QR (Cost: $2n^3$ flops).
	    2. **Solve (Part 1):** Compute the vector $y=Q^Tb$ (Cost: $2n^2$ flops).
	    3. **Solve (Part 2):** Solve the triangular system Rx=y using back substitution (Cost: $n^2$ flops).
	- **Total Complexity:** The process is dominated by the factorization step, costing approximately $2n^3$ flops.
3. **Factor-Solve with Multiple Right-Hand Sides**: When solving multiple linear systems simultaneously, AX=B, the factorization of A only needs to be computed once.
	- **Method:** Perform QR factorization A=QR once. Then, for each column $b_k$​ in B, compute $x_{k}=R^{−1}Q^Tb_{k}$.
	- **Advantage:** If k systems are solved, the total cost is only $2n^3+3kn^2$ flops. If the number of systems k is small relative to n, solving k systems costs essentially the same as solving one.
## 11.5 Pseudo-Inverse
The pseudo-inverse (A†) is a generalized inverse that exists even when A is non-square (tall or wide) or singular. Key Formulas:
- The definition of A† depends on whether the columns of A or the rows of A are linearly independent.

| Matrix Case               | Independence Condition                | Pseudo-Inverse Formula (A is m×n) | Role of A†                                 |
| ------------------------- | ------------------------------------- | --------------------------------- | ------------------------------------------ |
| **Tall/Square (**m≥n**)** | Columns are $LI (⟹ATA$ is invertible) | $A^†=(A^TA)^{−1}A^T$              | Acts as the unique Left Inverse: $A^†A=I$. |
| **Wide/Square (**m≤n**)** | Rows are $LI (⟹AAT$ is invertible)    | $A^†=A^T(AA^T)^{−1}$              | Acts as a Right Inverse: $AA^†=I$.         |
How to Use the Pseudo-Inverse: The pseudo-inverse is the central tool for solving linear least squares problems, including over-determined and under-determined cases, provided the necessary independence condition holds.
1. **Solving Over-determined Systems (Tall** A):
	- The least squares approximate solution x^ that minimizes $∣∣Ax−b∣∣^2 is x=A^†b$.
	- If A has linearly independent columns (LI columns), this choice is unique.
2. **Solving Under-determined Systems (Wide** A): 
	- If A has linearly independent rows (LI rows), $x=A^†b$ provides **a solution** to Ax=b. This particular solution is known as the _least norm solution_ (Chapter 16).
3. *Computational Method (via QR Factorization)*: For efficient computation, especially when A is tall, the pseudo-inverse is derived from the QR factorization A=QR: $A^†=R^{−1}Q^T$.
	This is computed exactly using Algorithm 12.1 for least squares problems, which has a complexity of approximately $3mn^2$ flops.
---
# #Lecture Lecture
## #Jupyter Jupyter
### Polynomial Interpolation
Polynomial interpolation is a frequent task in various machine learning and applied computational settings. For example if one has data that is missing, one can apply polynomial interpolation to infer what the missing data may have been.
1. *Hand-coded polynomials*:
	- Example functions:
	    - $f(x) = x^2$
	    - $g(x) = x^5 - x^4 - x^3 - x^2 - x$
	- To generate data, pick an interval $[a,b]$, number of points mmm, step $dx = \frac{b-a}{m}$​, then loop:
	    - xi=a+i dxx_i = a + i\,dxxi​=a+idx   
	    - yi=f(xi)y_i = f(x_i)yi​=f(xi​) or g(xi)g(x_i)g(xi​)
	- This _works_ but every time we change the polynomial, we must rewrite the function.
2. *Polynomial as a vector dot product*: For $g(x) = x^5 - x^4 - x^3 - x^2 - x$
	- **Coefficient vector** $$\begin{bmatrix} c_0\ c_1\ c_2\ c_3\ c_4\ c_5 \end{bmatrix} \begin{bmatrix} 0\ -1\ -1\ -1\ -1\ 1 \end{bmatrix}$$
	- **Evaluation vector at $x=\alpha$**: $$\begin{bmatrix}  
    1\ \alpha\ \alpha^2\ \alpha^3\ \alpha^4\ \alpha^5  
    \end{bmatrix}$$
	- **Key formula (evaluation = dot product)**: $$g(\alpha) = \vec c^{\,T}\vec x_\alpha$$So the polynomial is completely described by $\vec c$; evaluating is just a dot product with powers of the input.
3. *Generating data using the vector form*: For each sample point $\alpha_i$​:
	1. Build $\vec x_{α_{i}}=[1,αi,αi2,…,αi5]^T$.
	2. Compute: $y_i = \vec c^{\,T}\vec x_{\alpha_i}$​​.
	3. Store the pair $(\alpha_i, y_i)$.
	Same output as the hand-coded function, but now everything is linear-algebra friendly.
4. *From many points to a linear system (Vandermonde)*: If we evaluate at several points $\alpha, \beta, \gamma, \dots$ we stack the equations.$$\vec c^{\,T}\vec x_\alpha = g(\alpha),\quad \vec c^{\,T}\vec x_\beta = g(\beta),\quad \vec c^{\,T}\vec x_\gamma = g(\gamma),\dots$$into matrix form:
	- **Vandermonde matrix V** (rows are evaluation vectors): $$V = \begin{bmatrix} 1 & \alpha & \alpha^2 & \dots & \alpha^5\\ 1 & \beta & \beta^2 & \dots & \beta^5\\ \vdots & \vdots & \vdots & \ddots & \vdots\\ 1 & \gamma & \gamma^2 & \dots & \gamma^5 \end{bmatrix}$$​
	- **Coefficient vector**: $$\vec c = \begin{bmatrix} c_0\\ c_1\\ c_2\\ c_3\\ c_4\\ c_5 \end{bmatrix}$$
	- **Right-hand side vector**: $$\vec b = \begin{bmatrix} g(\alpha)\\ g(\beta)\\ \vdots\\ g(\gamma) \end{bmatrix}$$Together: $\vec c = \vec b$.
	- If we have exactly 6 distinct points → V is 6×6, usually invertible → $\vec c = V^{-1}\vec b$.
	- If we have more than 6 points → V is tall → use least squares / pseudo-inverse.
## #Quiz Quiz - 8
1. ass
2. QR factorization works for **any** $m\times n$ matrix A (square, tall, wide).
	- If A is square & full rank → QR gives an exact solution.
	- If A is rectangular → QR gives the **least–squares** solution (over- or under-determined).
3. Back substitution only works when the coefficient matrix is **triangular** (upper or lower) and non-singular.
	- For a general messy matrix, you can’t start from “last variable and move backwards” because every equation mixes many variables.
	- You typically first do some factorization (like QR, LU) to get a triangular system, _then_ you use back substitution.
4. Write the coefficient matrix: $$A = \begin{bmatrix} 3 & 2 & -1\\ 0 & 2 & -1\\ 0 & 0 & 1 \end{bmatrix}$$This **is upper triangular** (zeros below the diagonal), so back substitution works:
	1. From third equation: $x_3 = -2$.
	2. Plug into second: $2x_2 - (-2) = 4 \Rightarrow x_2 = 1$
	3. Plug into first: $3x_1 + 2(1) - (-2) = 7 \Rightarrow 3x_1 + 4 = 7 \Rightarrow x_1 = 1$.
	Because it has that triangular form, the statement is **True**.
5. [[#Polynomial Interpolation]] - $V \vec c= \vec g$
---
# #Homework Coding HW 8
1. What it’s doing conceptually: For a polynomial of degree n−1, $$p(x) = c_0 + c_1 x + \dots + c_{n-1} x^{n-1}$$ and each data point $(x_i, y_i)$ we want $$c_0\cdot 1 + c_1 x_i + c_2 x_i^2 + \dots + c_{n-1} x_i^{n-1} \approx y_i$$If we put all these equations together for all m data points, we get $A \vec c \approx \vec b$ where
	- **Row i of A** is $[1, x_i, x_i^2, \dots, x_i^{n-1}]$
	- **Entry $b_i$** is $y_i$​.
		That matrix A is exactly the **rectangular Vandermonde matrix**.
	- How the code builds it, For each data point:
		- `x_i, y_i = data[i]`
		- `b_vals[i] = y_i` ⇒ builds vector $\vec b$.
		- `A_data[i][0] = 1.0` ⇒ the $x^0$ term.
		- `A_data[i][j] = A_data[i][j-1]*x_i` ⇒ recursively multiply by $x_i$​ to get $x_i^1, x_i^2, \dots, x_i^{n-1}$.
		So row i ends up as`[1, x_i, x_i**2, ..., x_i**(n-1)]`.
		That’s **exactly** the Vandermonde row.
2. Conceptually:
	- Build Vandermonde matrix A and RHS $\vec b$.
	- Solve the **least squares** problem $\min_{\vec c} \|A\vec c - \vec b\|^2$ using your QR solver.
	From Chapter 11:
	- For tall A (more data points than coefficients), QR solver is implementing: $A = QR,\quad \vec c = R^{-1} Q^T \vec b$
	- That is equivalent to $\vec c = A^\dagger \vec b$ (pseudo-inverse).
	So `Interpolate` is the function “**given data and a degree n−1n-1n−1, find the best-fit polynomial coefficients $\vec c$**”.
3. **Error + RMS**
	1. `error(c, data)`:
	```python
	def error(c,data):
    """computes the error in the approximation"""
    m = len(data)
    s = 0.0
    for i in range(m):
        x_i, y_i = data[i]
        y_hat = f(c, x_i)        # predicted value from polynomial
        s += (y_hat - y_i)**2    # squared residual

    rms_error = (s / m)**0.5
    return rms_error
	```
	- For each data point, you compute:
	    - Prediction: $\hat{y}_i = p(x_i)$, where `f(c, x_i)` evaluates the polynomial with coefficients `c`.
	    - Residual: $r_i = \hat{y}_i - y_i$​.
	    - Add up $r_i^2$​.
	- Then you compute: *RMS error*: $$\text{RMS error} = \sqrt{\frac{1}{m} \sum_{i=1}^m r_i^2}$$which is “average size of the residual”.
	2. `rms(data)`
	```python
	def rms(data):
    """computes the root mean squared of the y-values (output) of data"""
    m = len(data)
    s = 0.0
    for i in range(m):
        y_i = data[i][1]
        s += y_i**2

    rms_val = (s / m)**0.5
    return rms_val
	```
	This is $$\text{RMS}_y = \sqrt{\frac{1}{m} \sum y_i^2}$$i.e. the typical “size” of the actual output values.
	3. *Relative prediction error*: In the loop (tasks 4 & 5), you compute:
	```python
	rms_y = rms(data)   # or rms(train_data / test_data)
	e = error(c, data)
	print("relative prediction error:", e / rms_y)
	```
	This matches the definition: $$\text{Rel. error} = \frac{\text{RMS residual}}{\text{RMS of actual }y}$$
	- If this ratio ≈ 1 → your model error is as big as the signal → terrible.
	- If this ratio ≪ 1 → your model describes the data well.
4. See the lab for more details
5. same as 4.
---

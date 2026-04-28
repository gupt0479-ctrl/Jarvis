---
type: class
status: archived
created: 2025-10-24
updated: 2025-10-25
area:
  - "[[Final]]"
  - "[[Complexity]]"
  - "[[Jacobi Method]]"
  - "[[Matrix Tools]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Lecture"
  - "#Jupyter"
  - "#Quiz"
  - "#Homework"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2033/Week - 8|Week - 8]]"
---
# #Textbook Textbook (Ch - 7 & 8) 
## Chapter 7
### 7.1 Geometric Transformations
If x is a vector representing a position (in 2-D or 3-D space), multiplying it by a transformation matrix A produces a new vector $y=Ax$, which is the resulting position after the operation.

|                |                                                                                                                                           |                                                                                                                                                                                            |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Transformation | Simplified Concept                                                                                                                        | Key Insight                                                                                                                                                                                |
| **Scaling**    | Changes the magnitude (length) of the vector uniformly in all directions. The matrix used is proportional to the identity matrix, $A=aI$. | If $a<0$, the transformation flips the vector's direction.                                                                                                                                 |
| **Dilation**   | Changes the magnitude of the vector differently along different axes. The matrix D is a diagonal matrix.                                  | A diagonal matrix $D=diag(d1​,d2​)$ stretches the vector along the first axis by d1​ and along the second axis by d2​.                                                                     |
| **Rotation**   | Changes the orientation of the vector. A specific matrix is used to rotate a 2D vector counterclockwise by an angle θ.                    | Rotation matrices are critical for converting positions between different coordinate systems, such as converting aircraft position from body-fixed coordinates to earth-fixed coordinates. |
| **Reflection** | Mirrors the vector across a specific line passing through the origin.                                                                     |                                                                                                                                                                                            |
| **Projection** | Maps the original vector x onto the point closest to it that lies on a specified line through the origin.                                 |                                                                                                                                                                                            |
**Finding the Matrix:** For any linear transformation, the columns of the matrix A are simply the resulting vectors obtained when that transformation is applied to the standard unit vectors (e.g., e1​,e2​,…).
### 7.2 Selectors
A selector matrix is a simple, highly structured matrix primarily used for copying or selecting specific entries from a vector.
- **Structure:** An m×n selector matrix A is built such that **each row is a transposed unit vector** (e.g., ekT​), where k is an index between 1 and n.
- **Function:** When A multiplies a vector x (so y=Ax), the i-th entry of the resulting vector y is simply the ki​-th entry selected from x.
- **Applications:**
	- **Slicing:** A selector matrix can be constructed to extract a specific portion of a vector, known as a slice (xr:s​).
	- **Down-sampling:** It can be used in signal processing, such as taking a time series x and producing a new vector y containing only every second entry (x1​,x3​,x5​,…).
	- **Image Cropping:** A large vector representing an image can be multiplied by a selector matrix to yield a new, smaller vector representing a cropped version of the image.
	- **Permutation Matrices:** A special type of selector matrix that must be square. These matrices have exactly one '1' in every row and every column. Multiplying a vector by a permutation matrix simply **re-orders (permutes) the entries** of the vector x.
### 7.3 Incidence Matrix
The incidence matrix (A, size n×m) is used to model a directed graph or network that has n nodes (vertices) and m directed edges (links).
- **Structure:** It is a sparse matrix where every column corresponds to an edge and has exactly two nonzero entries: a +1 for the node the edge points **to**, and a −1 for the node the edge points **from**.
This matrix is central to modeling two key network concepts: flows and potentials.
1. **Flow Conservation (Flows on Edges)**: If an m-vector x represents the flow rate along each edge (positive in the direction of the edge), the resulting vector y=Ax (an n-vector) represents the **net flow surplus** at each node.
	1. **Circulation:** If $Ax=0$, flow conservation holds, meaning that the total flow coming into a node equals the total flow leaving it.
	2. **Sources and Sinks:** If external flows (s) are present (sources inject flow, sinks remove flow), the balance equation becomes $Ax+s=0$. This models the conservation of flow when external injection or removal occurs at the nodes.
2. **Node Potentials and Roughness (Potentials on Nodes)**: If an n-vector v represents potentials (like electrical voltage or temperature) at the n nodes, the related matrix multiplication $u=A^T v$ calculates the **potential differences** across the m edges.
	- **Dirichlet Energy (**D(v)**):** The squared norm of the potential differences, $D(v)=∥A^T v∥^2$, measures the sum of the squared potential differences across all edges. This quantity is used to quantify the **non-smoothness or "roughness"** of the potentials v across the graph.
	- **Chain Graph Example:** For a simple linear chain of nodes (like samples in a time series), minimizing the Dirichlet energy forces adjacent entries to be similar, as D(v) becomes the sum of squares of differences between consecutive entries.
### 7.4 Convolution
Convolution $c=a∗b$ is an operation between two vectors (a of size n, b of size m) that results in a vector c of size $n+m−1$.
- **Function:** Convolution essentially calculates a weighted sum where the weights are derived from one vector, applied sequentially to shifted versions of the other vector.
- **Polynomials:** If a and b contain the coefficients of two polynomials, their convolution $c=a∗b$ yields the coefficients of the resulting product polynomial.
- **Matrix Representation:** Because convolution is a linear operation, it can be expressed as a matrix-vector product, such as $c=T(a)b$. The matrix T(a) is a **Toeplitz matrix**, meaning its entries are constant along diagonals, and its columns are shifted versions of the vector a, typically padded with zeros.
- **Applications:**
	- **Signal Processing:** Convolution is fundamental in representing how linear systems respond to inputs. The output (y) of a linear system is often the convolution of the input (u) and the system's impulse response (h), $y=h∗u$.
	- **Smoothing/Filtering:** Convolution is used for operations like calculating a moving average (time series smoothing) or audio filtering.
	- **2D Convolution:** This extends to matrices (A?B), used heavily in image processing, often to model effects like **blurring** (where B is the point spread function) or calculating vertical/horizontal differences.
## Chapter 8
### 8.1 Linear and Affine Functions
1. *Vector-Valued Functions*: A function $f:Rn→Rm$ means that the function f takes an input vector with n entries (an n-vector x) and produces an output vector with m entries (an m-vector f(x)). Each of the m entries of the output vector, $f_{i}​(x)$, is itself a scalar value determined by all n components of the input vector x.
2. *Linearity and Superposition*:  A function is defined as **linear** if and only if it can be represented by multiplying the input vector by a matrix. This mathematical relationship is formally defined by the **superposition property**: $$f(αx+βy)=αf(x)+βf(y).$$
	- **Simpler Meaning:** If you take a mixture of two inputs $(αx+βy)$ and feed it into a linear function, the output is exactly the same as if you fed the inputs in separately, processed them, and then mixed the results $(αf(x)+βf(y))$.
	- **Decomposition:** Linearity implies two smaller properties must hold: **Homogeneity** (scaling the input scales the output: $f(αx)=αf(x))$ and **Additivity** (adding inputs adds the outputs: $f(x+y)=f(x)+f(y))$.
3. *Matrix Representation of Linear Functions*: If a function f is linear, there is a **unique** m×n matrix A such that f(x)=Ax for all input vectors x.
	- **Key Construction:** The structure of the matrix A is determined entirely by how the function acts on the standard unit vectors (e1​,e2​,…,en​). **The** k-th column of **A is simply the result of applying the function to the unit vector** ek​ (A⋅,k​=f(ek​)). This is a crucial concept, as it means that once you know the output for n specific inputs (e1​ through en​), you can predict the output for _any_ other input x just by using matrix multiplication.
4. **Affine Functions**: An **affine function** is defined as a linear function plus a constant offset term b: $f(x)=Ax+b$.
	- **Superposition for Affine Functions:** An affine function does _not_ satisfy the general superposition property; it only satisfies it for **affine combinations**, meaning the coefficients must sum to one (α+β=1).
	- **Uniqueness:** The matrix A and offset vector b are uniquely determined. The offset b is simply the function evaluated at the zero vector (b=f(0)).
	- **Linear vs. Affine:** While often colloquially called "linear" (especially when plotting a line), an affine function is mathematically linear only if the offset b is the zero vector.
### 8.2 Linear Function Models
1. **Affine Approximation using Taylor Series**: When dealing with a complex, differentiable function f:Rn→Rm, the **first-order Taylor approximation** (f^​) allows us to approximate it locally as an affine function near a specific point z.
	- **Formula (Compact Form):** $f'(x)=f(z)+Df(z)(x−z).$
	- **The Jacobian Matrix (**Df(z)**):** This derivative matrix is central to the approximation. It is an m×n matrix whose entries capture the instantaneous rate of change (partial derivative) of each output component fi​ with respect to each input component xj​, evaluated at point z.
	- **Interpretation:** The approximation f(z) gives the value at the reference point, and the term Df(z)(x−z) linearly estimates the change in the output based on the input deviation (x−z). This step is vital for solving complicated nonlinear problems because it replaces the nonlinear relationship with an approximate, manipulable affine one.
2. **Regression Model**: Regression is a common application where an affine model is used to predict a scalar outcome (y^​) based on an input feature vector (x).
	- **Model Form:** $y`=x^T β+v$.
	- β is the vector of coefficients (weights).
	- v is the offset (intercept).
	- **Data Modeling:** If we have N samples of data, we form vectors of actual outcomes (yd) and predicted outcomes (y^​d). The difference is the **residual vector** (rd): $rd=yd−y^​d=yd−X^Tβ−v1$. Here, X is the n×N feature matrix (columns are the sample feature vectors), and 1 is the ones vector.
	- **Key Insight:** The relationship $yd=X^T β+v_{1}$ shows that the entire vector of predictions is a **linear function** of the parameters (β,v).
### 8.3 Systems of Linear Equations
This section establishes the definitive matrix notation for solving multiple linear equations simultaneously.
1. **Standard Matrix Form**: A set of m linear equations in n variables x1​,…,xn​ is represented by the expression: Ax=b.
	- **Terminology:** A is the coefficient matrix, b is the right-hand side, and x is the solution vector (unknown variables).
2. **Geometric Interpretation (Column View)**: Solving Ax=b is geometrically equivalent to finding weights (x1​,…,xn​) such that the target vector b can be expressed as a **linear combination of the columns of** A: x1​a1​+x2​a2​+⋯+xn​an​=b.
3. **Dimensional Classification**: The relationship between the number of equations (m) and the number of unknowns (n) determines the general behavior of the system:
	1. **Over-determined (**m>n**):** The matrix A is **tall**. There are more constraints than variables. Solutions generally do not exist.
	2. **Under-determined (**m<n**):** The matrix A is **wide**. There are fewer constraints than variables. Multiple solutions typically exist.
	3. **Square (**m=n**):** Equal number of equations and variables.
	4. **Homogeneous (**Ax=0**):** The right-hand side is zero. The trivial solution x=0 always exists.

---
# #Lecture Lecture
## #Jupyter Jupyter
### [[Matrix Tools]]
### Graphs and Adjacency Matrix
1. Graph recap: For this example we have a **simple undirected graph**:
	- **Vertices** : V={0,1,2,3,4,5,6}
	- **Edges**: E = { (0,1), (0,5), (0,6), (1,2), (1,3), (1,4), (1,6), (2,3), (2,4), (5,6) }
	Because the graph is **undirected**, every edge (i,j) is the same as (j,i).
2. What is an adjacency matrix?
	For a graph with n vertices ($0,\dots,n-1$), the **adjacency matrix** A is an n×n matrix where: 
	$A[i,j] = \begin{cases} 1 & \text{if there is an edge between vertex } i \text{ and } j \\ 0 & \text{otherwise} \end{cases}$
- **Row i** = “neighbors of vertex i”
- **Column j** = “is vertex j connected to i?”
For an **undirected** graph (like this one), the adjacency matrix is **symmetric**: $A[i,j]=A[j,i]$
### Geometric Transformations
A matrix `A` is a **machine** that takes x to a new vector: $y = A x$
In the plots: (Which color is which isn’t important; focus on how length/orientation change.)
- one segment is the **original vector** x.
- the other segment is the **transformed vector** Ax
For any linear transformation: [[50_Archive/UMN/Classes/Previous Classes/CSCI 2033/Week - 6#7.1 Geometric Transformations|Geometric Transformations in detail]]
> **Columns of A = images of the standard basis vectors.**  
> First column = $A e_{1}$​, second column = $A e_{2}$​, etc.

So if you know what happens to $e_{1} = (1,0)$ and $e_{2} = (0,1)$, you know the whole matrix.
1. *Scaling (uniform)*: Mathematically, for scale factor a: $$A = a I = \begin{bmatrix} a & 0 \\ 0 & a \end{bmatrix}$$Effect:
	- Every vector is stretched or shrunk by the **same factor** a.
	- Direction stays the same (unless a<0, then it also flips).
	In the plot:
	- The two arrows lie on the **same line** (same direction).
	- One is **longer** (scaled up by 3) and the other is shorter.
	- That shows: scaling changes **length**, not **angle**.
	Basis-vector view:
	- $A e_{1} = (a, 0)$ → first column
	- $A e_{2} = (0, a)$ → second column
	Both axes are scaled equally → shapes keep their form, just get bigger/smaller.
2. *Dilation (non-uniform scaling)*: Matrix form: $$D = \operatorname{diag}(d_1, d_2) = \begin{bmatrix} d_1 & 0 \\ 0 & d_2 \end{bmatrix}$$Effect:
	- Each coordinate is scaled by a **different** factor.
	- The vector’s **direction can change**, because x and y components are stretched differently.
	In the first plot `dilate([4,1])`:
		- x-component multiplied by 4
		- y-component unchanged
		- The transformed vector becomes much more “horizontal” than the original.
	In the second plot `dilate([1,10])`:
		- x-component unchanged
		- y-component multiplied by 10
		- The transformed vector becomes very “vertical”.
	Basis-vector view:
	- $A e_{1} = (d_{1}, 0)$ → first column (stretch of x-axis)
	- $A e_{2} = (0, d_{2})$ → second column (stretch of y-axis)
	So dilation is “stretch differently along each axis”.
3. *Rotation*: Standard 2-D rotation matrix (counterclockwise by angle $\theta$): $$R(\theta) = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$Effect:
	- Length of the vector is **preserved**.
	- The direction is changed by **angle θ\thetaθ**.
	- All points rotate around the **origin**.
	In the plot:
	- The two arrows have **same length**.
	- One has been **swung** around by a small angle.
	- That shows: rotation moves the vector around the origin without stretching.
	Basis-vector view:
	- $R e_{1} = (\cos\theta, \sin\theta)$ → first column
	- $R e_{2} = (-\sin\theta, \cos\theta)$ → second column
	So the matrix columns literally are the rotated axes.
4. *Reflection*: Concept: A reflection “flips” the plane across some **line through the origin**. That line is the **mirror line** (points on it don’t move). Special cases: Reflect across **x-axis**: $$\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$
	- Reflect across **y-axis**: $$\begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$$In your example:
	- `angle = 3.14/4` means the mirror line is at about $45^\circ$ to the x-axis.
	- The original and reflected vectors lie on **opposite sides** of that line, symmetric to it.
	- Length stays the same, only orientation is flipped.
	Key properties to remember:
	- Reflecting twice gets you back: $A^2 = I$.
	- Reflection preserves lengths and angles but reverses orientation (clockwise vs counterclockwise).
5. *Projection*: For projection onto the line spanned by a **unit vector** u, the matrix is: $P = u u^\top$. For the x-axis, we use u = (1,0), so $$P = \begin{bmatrix} 1 \\ 0 \end{bmatrix} [1 \ 0] = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$Effect:
	- Any vector (x, y) is sent to (x, 0).
	- Geometrically: drop a perpendicular down to the **x-axis**.
	In the plot:
	- One arrow is the original vector.
	- The other arrow lies **exactly on the x-axis** (same x, y=0).
	- You can imagine “shadow of the vector on the x-axis”.
	Key properties:
	- Projection **flattens** things onto a subspace.
	- Applying twice does nothing extra: $P^2 = P$ (idempotent).
### Linear Equations
#### Jacobi method
We want to solve a linear system: $Ax=b$.
Instead of doing exact algebra (Gaussian elimination, $A^{-1}$, etc.), we build an **iterative algorithm**: start with a guess $x^{(0)}$, then repeatedly improve it until it’s “good enough”.
1. **Deriving the Jacobi iteration**: Start from the equation: $A x = b$, Insert the split A = M + N: $(M + N) x = b$. Rearrange: $M x = b - N x$
	- Multiply by $M^{-1}$ (we can, because all diagonal entries are nonzero): $x = M^{-1}(b - N x)$. This is a **fixed-point equation** of the form. 
	- $x = T(x), \quad T(x) = M^{-1}(b - N x)$
2. Idea of Jacobi method: Start with a guess $x^{(0)}$. Define a sequence $$x^{(k+1)} = M^{-1}(b - N x^{(k)})$$and hope it converges to the true solution $x^*$. That recurrence is exactly what the code implements.
3. [[Jacobi Method|Code for the Jacobi method]]
## #Quiz Quiz - 5
- cA: multiplies **every entry** by scalar c.
- AD (diagonal D): multiplies **columns** of A.
- DA (diagonal D): multiplies **rows** of A.
- PA (permutation matrix P): **reorders rows** of A.
- AP: **reorders columns** of A.
- $A^T$: swaps rows and columns (row i ↔ column i).
### Effect of multiplying by a diagonal matrix
Let
- A be an m×n times matrix
- D be an n.n times **diagonal** matrix:  
    $D = \operatorname{diag}(d_1,d_2,\dots,d_n)$
#### Right-multiplication: ADA DAD → scales **columns**
Entry wise: $$(AD)_{ij} = \sum_{k=1}^n A_{ik} D_{kj}$$​
But D is diagonal, so $D_{kj} = 0$ unless k = j. So only one term survives: $(AD)_{ij} = A_{ij} D_{jj} = A_{ij} \, d_j$
For a fixed column j, every entry in that column gets multiplied by the same diagonal value dj.
> **Rule:** Right-multiplying by a diagonal matrix multiplies **column j** of A by the diagonal entry dj.
#### Left-multiplication: DAD ADA → scales **rows**
Now let D be m×m times diagonal and compute: $$(DA)_{ij} = \sum_{k=1}^m D_{ik} A_{kj}$$​
Again, only the diagonal term k = i is nonzero: $(DA)_{ij} = D_{ii} A_{ij} = d_i A_{ij}$
For a fixed row iii, every entry in that row gets multiplied by di.
> **Rule:** Left-multiplying by a diagonal matrix multiplies **row i** of A by the diagonal entry $d_{i}$

---
# #Homework Coding HW - 5
1. **For calculating the graph values for each person or point**: Create a table that has all the names of people in the graph as the column and the people that they are connecting with as 1st row. Now mark each person 1 if they connect and 0 if they don't.  
2. *Why is $C^2$ computed using dot products?* 
	By definition, **matrix multiplication** is built from dot products: $$(C^2)_{ij} = (C \cdot C)_{ij} = \sum_{k} C_{ik} \, C_{kj}$$Interpretation:
	- Fix people i and j. Look at every possible “middle person” k.
	- The term $C_{ik} C_{kj}$ equals 1 **only if**
		- $C_{ik} = 1$: i is friends with k, **and**
		- $C_{kj} = 1$: k is friends with j.
	So: For a specific k, $C_{ik} C_{kj} = 1$ means there is a path $i \to k \to j$ (two hops). When you **sum over all k**, you count how many such middle people there are.
	Therefore: $(C^2)_{ij} = \text{number of distinct 2-step paths } i \to \text{(someone)} \to j$
	In the “friends” language: $(C^2)_{ij}$​ = number of **mutual friends** that i and j share.
	- Code Pattern - $A^3$: Entry (i, j) counts 3-step path $i \to \cdots \to j$.
```bash
A2 = A @ A 
A3 = A @ A2   # or A2 @ A
```
5. Review the method used to scale the columns of the matrix.

---

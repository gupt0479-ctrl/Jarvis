---
type: class
status: archived
created: 2025-10-10
updated: 2025-10-18
area:
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2033/Midterm - 1|Midterm - 1]]"
  - "[[CSCI 2033 Board]]"
  - "[[Final]]"
tags:
  - "#class"
next: "[[Final]]"
---
## Overview
All main concepts covered in the week's 1-5.
### Chapter - 1
1. Linear Combinations: A **linear combination** of $n$-vectors $a_1, \ldots, a_m$, using scalars $\beta_1, \ldots, \beta_m$ as **coefficients**, is defined as the vector: $$ \beta_1 a_1 + \cdots + \beta_m a_m $$
2. **Inner product**: (or dot product) of two $n$-vectors $a$ and $b$ is a **scalar** defined as the sum of the products of their corresponding entries: $$ a^T b = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n $$**Selecting an Entry:** $e_i^T a = a_i$. The inner product with the $i$th unit vector selects the $i$th element $a_i$.
	- **Sum:** $\mathbf{1}^T a = a_1 + \cdots + a_n$, where $\mathbf{1}$ is the vector of ones.
	- **Average (Mean):** $(\mathbf{1}/n)^T a = (a_1 + \cdots + a_n)/n$. This average is denoted $\text{avg}(x)$.
	- **Sum of Squares:** $a^T a = a_1^2 + \cdots + a_n^2$.
	- **Block Vectors:** The inner product of conforming block vectors is the sum of the inner products of the corresponding blocks.
```python
def inner_product(x,y):
    """accumulate the sum products of corresponding elements from x and y"""
    # check the length of the vectors
    if x.n != y.n:
        raise Exception("inner_product(x,y): Vector size of x = "+str(x.n)+", but vector size of y = "+str(y.n))
    total = 0                          #initialize the accumulation variable
    for i in range(x.n):               #loop for the vector length
        total += x.data[i] * y.data[i] #add product of corresponding entries
    return total                       #return the accumulation (sum)
```
3. If $a$ and $b$ are Boolean vectors (0 or 1 entries), $a^T b$ is the total number of indices where both entries are one. For example the Boolean vector $[0,1,1,0]^T$ would be written using this alternative encoding as $[−1,+1,+1,−1]^T$. A **Boolean n-vector** is simply a list (vector) of _n_ binary entries: $$x=[x1,x2,…,xn]^T$$Where each $x_i∈{0,1}$.
	- $x_i=1$ → means the condition, feature, or item _i_ is **present/true/on**.
	- $x_i=0$ → means it is **absent/false/off**.
	**Hw 2**: The norm gives the **magnitude or count of “true” entries”** — i.e., how many features are active. 
	The distance ddd measures **how many features differ** between x and y.  
	It’s exactly the **Hamming distance** (up to a square root): $d = \sqrt{\text{number of differing entries}}$
	If two sparse Boolean vectors differ only in a few active features, their **distance is small** — meaning they’re similar.
### Chapter - 2
1. A function $f$ is **linear** if it satisfies the **superposition** property for all $n$-vectors $x, y$ and all scalars $\alpha, \beta$: $$ f(\alpha x + \beta y) = \alpha f(x) + \beta f(y) $$ **If a function $f: \mathbb{R}^n \to \mathbb{R}$ is linear, it can always be expressed as the inner product of its argument $x$ with some fixed vector $a$**: $$ f(x) = a^T x $$ An **affine function** is a linear function plus a constant (offset) $b$: $$ f(x) = a^T x + b $$An affine function satisfies a restricted form of superposition: $$f((1 - \theta)x + \theta y) = (1 - \theta)f(x) + \theta f(y)$$
- If $b \ne 0$, an affine function is **not** linear.
 2. The **first-order Taylor approximation** provides a structured way to form an affine approximation of a differentiable function $f: \mathbb{R}^n \to \mathbb{R}$ near a specific point $z$: $$ \hat{f}(x) = f(z) + \nabla f(z)^T (x - z) $$$\nabla f(z)$ is the **gradient**(dx/dy) of $f$ evaluated at $z$. This approximation is generally very good when $x$ is near $z$. 
	 - Since the approximation $\hat{f}(x)$ has the form $a^T x + \text{constant}$, it is an **affine function**.
3. The **regression model** is a commonly used affine function, especially in the context of feature vectors $x$: $$ \hat{y} = x^T \beta + v $$
- $\hat{y}$ is the **prediction** of some true value $y$ (the **dependent variable/outcome/label**). 
- The entries of $x$ are the **regressors**.
- $\beta$ is the $n$-vector of **weights** or **coefficients**.
- $v$ is the **offset** (or intercept).
```python
def f(x,b,v):
    """Generic Linear Regression Function"""
    
    return inner_product(x,b) + v
```
```python
import random

# parameters
b = Vector([1,1,1]) # beta
v = -105            # offset

# input
x = Vector([random.randrange(5) for i in range(3)])

# compute (predicted) output
f(x,b,v)
```
### Chapter - 3
1. **Norm** - provides a measure of a vector's magnitude or "length".$$
\|x\|= \sqrt{x_1^2+x_2^2+\cdots+x_n^2}
$$
It can also be expressed concisely as the square root of the inner product of the vector with itself: **inner product form**
$$
\|x\|= \sqrt{x^T x}
$$ **Sum of a Norm**:
$$
\|x+y\|^2 = \|x\|^2 + 2x^Ty + \|y\|^2
$$ This formula is derived from $\|x+y\|^2 =(x+y)^T(x+y)$.
The **root-mean-square (RMS)** value of an n-vector x is defined as: 
$$
\text{rms}(x)= \frac{\|x\|}{\sqrt{n}} = \sqrt{\frac{x_1^2+\cdots+x_n^2}{n}}
$$
The **Chebyshev inequality** provides a limit on how many entries of a vector can be large relative to its RMS value. If k entries of vector x satisfy $|x_i|\ge a$ (where $a>0$), then: 
$$
k\le \frac{\|x\|^2}{a^2}
$$
or, more simply,  
$$
\frac{k}{n}\le\left(\frac{\text{rms}(x)}{a}\right)^2
$$
This inequality partially justifies the idea that the RMS value is representative of a typical entry size.
2. The Euclidean distance between two n-vectors a and b is the norm of their difference: 
$$
\text{dist}(a,b)=\|a-b\|
$$ The RMS value of the difference, $\|a-b\|/\sqrt{n}$, is called the RMS deviation between a and b.
**Triangle Inequality Interpretation**: The triangle inequality, $\|a-c\|\le\|a-b\|+\|b-c\|$, gains its name from geometry, stating that the length of one side of a triangle cannot exceed the sum of the lengths of the other two sides.
3. **Standard deviation** measures how much the entries of a vector deviate from their mean value. The de-meaned vector $\tilde{x}$ of an n-vector x is formed by subtracting the mean (average) value of x from every entry:
$$
\tilde{x}=x-\text{avg}(x)\mathbf{1}
$$
The mean of the entries of $\tilde{x}$ is always zero. **Definition of Standard Deviation ($\text{std}(x)$)**: The standard deviation of x is the RMS value of the de-meaned vector: 
$$
\text{std}(x)= \frac{\|\tilde{x}\|}{\sqrt{n}} = \sqrt{\frac{(x_1-\text{avg}(x))^2+\cdots+(x_n-\text{avg}(x))^2}{n}}
$$
- A small standard deviation means the entries of x are nearly the same.
- In some applications, std(x) is called risk (e.g., when x is a return time series).
Relationship between rms, avg, and std: These three measures are related by the identity: 
$$
\text{rms}(x)^2=\text{avg}(x)^2+\text{std}(x)^2
$$
The standardized version of x, denoted z, has a mean of zero and a standard deviation of one: $$
z=\frac{x-\text{avg}(x)\mathbf{1}}{\text{std}(x)}
$$
The entries $z_i$ are called the **z-scores** and indicate how many standard deviations $x_i$ is above or below the mean avg(x).
4. The angle between two vectors is defined using their inner product and norms.
**Cauchy–Schwarz Inequality**:$$
|a^Tb|\le\|a\|\|b\|
$$
This inequality ensures that the argument of the arc cos function used in the angle definition always lies between −1 and 1.
**Angle Definition**: For two nonzero n-vectors a and b, the angle between them, θ, is defined as: 
$$
\theta=\arccos\left(\frac{a^Tb}{\|a\|\|b\|}\right)
$$
The angle θ lies in the interval [0,π].
Key Angle Cases:
- **Orthogonal**: $a⊥b$ if $a^Tb=0$ (angle is π/2 or 90°).
- Aligned: $a^Tb=\|a\|\|b\|$ (angle is 0). Each vector is a positive multiple of the other.
- Anti-aligned: $a^Tb=-\|a\|\|b\|$ (angle is π or 180°). Each vector is a negative multiple of the other.
- Acute Angle: $a^Tb>0$ (angle is less than 90°).
- Obtuse Angle: $a^Tb<0$ (angle is greater than 90°).
- Vector Projections:
	- Vector projection of $\vec{b}$ onto $\vec{a}: \hspace{0.5in} \text{proj}_{\vec{a}}(\vec{b}) = \left(\frac{\vec{a}\cdot\vec{b}}{\|\vec{a}\|}\right)\frac{\vec{a}}{\|\vec{a}\|} = \left( \frac{\vec{a}\cdot\vec{b}}{\vec{a}\cdot\vec{a}} \right) \vec{a}$
	- Component of $\vec{b}$ orthogonal to $\vec{a}: \hspace{0.5in} \vec{b}_{\perp \vec{a}} = \vec{b} - \text{proj}_{\vec{a}}(\vec{b})$
		- Meaning
		- `parallel()` → “shadow” of self on other.
		- `perp()` → the remainder at 90° to other.
```python
def parallel(self,other):
      """returns the component of self parallel to other (projection)"""
       coeff = (self @ other) / (other @ other)
       return Vector([coeff * x for x in other.data])
def rms(self):
        total = 0
        for x in self.data:
            total += x * x
        return (total/self.n) ** 0.5
def mean(self):
        """returns the average(mean) of the data"""
        total = 0
        for x in self.data:
            total += x
        return total/self.n
def std(self):
        """returns the standard deviation of the data"""
        m = self.mean()
        total = 0
        for x in self.data:
            total += (x-m) * (x-m)
        return (total/self.n) ** 0.5
def standardize(self):
        """convert vector entries to z-score (standardized) values"""
        m = self.mean()
        s = self.std()
        for i in range(self.n):
            self.data[i] = (self.data[i] - m) / s
```
**Pythagorean Theorem**:If x and y are orthogonal vectors (θ=90°), the Pythagorean theorem holds: 
$$
\|x+y\|^2=\|x\|^2+\|y\|^2
$$
1. **MNSIT** - Each image = a **vector in ℝ⁷⁸⁴**, because 28 × 28 = 784 pixels.
```python
mnist = fetch_openml('mnist_784', version=1, as_frame=False)

# Convert arrays into `Vector` objects
N_train = 600 
L_train = [Vector(X_train[i]) / 255 for i in range(N_train)] 
y_train = Vector(y_train[:N_train])
  
N_test = 100 
L_test  = [Vector(X_test[i]) / 255 for i in range(N_test)]
y_test  = Vector(y_test[:N_test])
```
### Chapter - 4
1. **Clustering** aims to partition a collection of N vectors $(x_1, …, x_N)$ into k groups or clusters. The goal is for vectors within the same cluster to be "close" to each other, measured by the distance between them.
	1. Specifying the Clustering:
	**Assignment Vector ($c$)**: The clustering is specified by an N-vector $c$, where the i-th entry, $c_i$, is the number (1 to k) of the group that the vector $x_i$ belongs to.  
	**Index Sets ($G_j$)**: The cluster groups themselves are defined by index sets $G_j = \{ i \mid c_i = j \}$, meaning $G_j$ contains the indices of all vectors assigned to group j. $$z_{j} = \frac{1}{||G_{j}||} \sum_{i = G_{j}}(x_{i})$$ Entries of $z_j$ are the average of entries in $x_i$.
	2. Group Representatives (**Centroids**): Each group j has an associated n-vector representative, $z_j$. These representatives do not have to be actual data points. The goal is for $z_{c_i}$ (the representative for $x_i$) to be close to $x_i$.
	3. **The Objective Function** ($J_{clust}$): The standard measure of clustering quality is the mean square distance from the vectors to their assigned representatives: $$
     J_{clust} = \frac{1}{N} \sum_{i=1}^{N} \|x_i - z_{c_i}\|^2
     $$The goal of clustering is to minimize $J_{clust}$. A smaller value means a better clustering.
     4. Optimizing Representatives (Fixed Assignment): If the cluster assignments (c) are fixed, the value of the representative  that minimizes $J_{clust}$ for that specific group j is simply the average (centroid) of all vectors belonging to group j.
2. **k-means Algorithm** - The algorithm requires a list of N vectors $(x_1, …, x_N)$ and an initial list of k representative vectors $(z_1, …, z_k)$.
	1. **Partition the vectors (Assignment Step)**: For every vector $x_i$, assign it to the group associated with the representative $z_j$ that is its nearest neighbor (the closest one).
	2. **Update Representatives (Update Step)**: For each new group j, calculate the new representative $z_j$ by setting it to the mean (average) of all vectors currently assigned to that group.
	3. (**Complexity**): The complexity per iteration is approximately $(3k + 1)Nn$ flops, meaning the computational cost scales linearly with the total number of data points (N), the dimension (n), and the number of clusters (k).
### Chapter - 6
1. Matrix Types: 
	- **Square matrix:** $m = n$.
	- **Tall matrix:** $m > n$.
	- **Wide matrix:** $n > m$.
	- An $n$-vector is an $n \times 1$ matrix (column vector). A $1 \times n$ matrix is a **row vector**.
	**Submatrices**
	An $m \times n$ matrix $A$ can be viewed as:
	- A concatenation of its $n$ column vectors $a_1, \ldots, a_n$.
	- **Zero Matrix ($0$):** All entries are zero. The size is usually determined by context.
	- **Identity Matrix ($I$):** A square matrix with ones on the diagonal and zeros elsewhere. Its columns are the standard unit vectors $e_1, \ldots, e_n$.
	- **Sparse Matrix:** A matrix with many zero entries. The **density** is $\text{nnz}(A)/(m.n)$.
	- **Diagonal Matrix:** A square matrix where all off-diagonal entries are zero ($A_{ij}=0$ for $i \ne j$). Notation: $\text{diag}(a_1, \ldots, a_n)$.
	- **Triangular Matrices:** Upper triangular ($A_{ij}=0$ for $i>j$) or lower triangular ($A_{ij}=0$ for $i<j$). A triangular n.m matrix A has upto $n(n+1)/2$ non-zero entries, i.e. ,around half its entries are zero. 
2. The **transpose** of an $m \times n$ matrix $A$, denoted $A^T$, is an $n \times m$ matrix where $(A^T)_{ij} = A_{ji}$. The rows and columns are swapped. $(A^T)^T = A$. A square matrix $A$ is **symmetric** if $A = A^T$.
	- **Addition:** Matrices of the same size are added element-wise. 
	- Property: $(A + B)^T = A^T + B^T$.
	- **Scalar Multiplication:** Multiply every element by the scalar $\gamma$.
	- **Matrix Norm**: The **norm of an $m \times n$ matrix $A$** (or Frobenius norm, $|A|_F$) is the square root of the sum of the squares of its entries:__$$ ||A|| = \sqrt{\sum_{i=1}^m \sum_{j=1}^n A_{ij}^2} $$
3. If $A$ is an $m \times n$ matrix and $x$ is an $n$-vector, the product $y = Ax$ is an $m$-vector. Interpretations:
	1. **Row interpretation:** The $i$th element of $y$ ($y_i$) is the **inner product** of the $i$th row of $A$ and the vector $x$.
	2. **Column interpretation:** $y = Ax$ is a **linear combination of the columns of $A$**, where the coefficients are the elements of $x$: $$ y = x_1 a_1 + x_2 a_2 + \cdots + x_n a_n $$
	Special Examples: The product of $A$ and the unit vector $e_j$ selects the $j$th column of $A$: $A e_j = a_j$.
	- The **difference matrix** $D$ (6.5) yields the differences of consecutive entries of $x$: $(Dx)_i = x_{i+1} - x_i$.
---

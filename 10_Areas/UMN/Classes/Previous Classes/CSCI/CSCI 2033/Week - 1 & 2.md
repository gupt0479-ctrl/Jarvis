---
type: class
status: archived
created: 2025-09-17
updated: 2025-10-16
area:
  - "[[Python]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Midterm - 1]]"
  - "[[Final]]"
  - "[[Complexity]]"
tags:
  - "#class"
  - "#Textbook"
  - "#Jupyter"
  - "#Homework"
  - "#Lecture"
  - "#Quiz"
next: "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2033/Week - 3|Week - 3]]"
---
# #Textbook Textbook (Ch - 1 & 2) 
## Chapter - 1 Vectors
A **vector** is formally defined as an ordered finite list of numbers. Vectors are typically represented as **vertical arrays** enclosed in square or curved brackets, although they can also be written horizontally enclosed in parentheses.
**Dimensions and Indexing**: An **$n$-vector $x$** has $n$ entries, or elements. In standard mathematical notation used in this textbook, $n$-vectors are **indexed from $i = 1$ to $i = n$**. The $i$th entry of vector $x$ is denoted $x_i$. Notation:
- **Vector Equality:** Two vectors are equal if they have the same size, and their corresponding entries are all equal.
- **Subvectors and Slicing:** Colon notation, such as $x_{r:s}$, denotes a subvector containing entries from $r$ to $s$.
- **Stacked Vectors:** Vectors can be "stacked" vertically or horizontally using brackets or parentheses. A stacked vector is a single, longer vector. For example, a stacked vector $(a, b)$ has length $2n$ if $a$ and $b$ are $n$-vectors.
### Sparsity
A vector is considered **sparse** if many of its entries are zero.
- The **sparsity pattern** is the set of indices where the entries are nonzero.
- The **number of nonzero entries** of an $n$-vector $x$ is denoted $\text{nnz}(x)$.
**Unit vectors** ($e_i$), which have only one nonzero entry (the $i$th entry is 1, and all others are 0), are sparse.
- The **zero vector** ($\mathbf{0}$) has all entries equal to zero and is the sparsest possible vector.
### Applications and Interpretation
$N$-vectors are used to represent $n$ quantities or values. The textbook gives several examples:
- **Location and Displacement:** 2-vectors or 3-vectors represent positions or displacements in 2-D or 3-D space.
- **Quantities/Bill of Materials:** A vector representing amounts of resources needed or held.
- **Proportions/Probabilities:** A vector $w$ whose nonnegative entries sum to one, representing fractions, recipes, or probabilities.
- **Time Series/Signals:** A vector whose entries give the value of some quantity at different times (e.g., hourly temperature or acoustic pressure samples).
- **Cash Flow:** A vector where positive entries are payments received and negative entries are payments made.
- **Images/Video:** Images (or videos) can be linearized into long vectors representing pixel values (e.g., RGB values for color images).
- **Word Count/Histogram:** A vector representing the frequency or count of words in a document based on a dictionary.
- **Features or Attributes:** A vector collecting different quantities pertaining to a single object (e.g., age, height, weight of a patient).
### Vector Addition
Vector addition is defined only for two vectors of the **same size**. The sum of two vectors is found by **adding the corresponding elements** to form another vector of the same size. Vector subtraction is performed similarly. Properties of Vector Addition:
- **Commutativity:** $a + b = b + a$.
- **Associativity:** $(a + b) + c = a + (b + c)$.
- **Zero Vector:** $a + 0 = a$.
- **Self-Subtraction:** $a - a = 0$.
Applications of Vector Addition
- **Displacements:** $a+b$ is the net displacement.
- **Word Counts:** $a+b$ is the combined word count vector of two documents.
- **Market Clearing:** The sum $s = q_1 + \cdots + q_N$ of consumption/production vectors $q_i$ represents the total net surplus (or shortfall). $s=0$ means the market clears.
- **Time Series:** $a+b$ represents the sum of the quantities in the time series.
- **Portfolio Trading:** If $s$ is the initial portfolio vector and $b$ is the trade vector (buys/sells), the new portfolio is $s+b$.
### Scalar-Vector Multiplication
**Scalar-vector multiplication** involves multiplying every element of a vector by a scalar (number). This operation is denoted by juxtaposition, typically with the scalar on the left (e.g., $\beta a$). Properties of Scalar-Vector Multiplication
- **Associativity:** $\alpha(\beta a) = (\alpha\beta)a$.
- **Identity:** $1a = a$.
- **Zero Multiplier:** $0a = 0$ (The zero vector).
- **Inverse Multiplier:** $(-1)a = -a$.
- **Distributivity over Scalar Addition:** $(\beta + \gamma)a = \beta a + \gamma a$.
- **Distributivity over Vector Addition:** $\beta(a+b) = \beta a + \beta b$.
Linear Combinations: A **linear combination** of $n$-vectors $a_1, \ldots, a_m$, using scalars $\beta_1, \ldots, \beta_m$ as **coefficients**, is defined as the vector: $$ \beta_1 a_1 + \cdots + \beta_m a_m $$**Affine Combinations:** When the coefficients $\beta_1 + \cdots + \beta_m = 1$, the linear combination is an affine combination. If $a$ and $b$ are vectors, $c = (1 - \theta)a + \theta b$ describes a point on the line passing through $a$ and $b$.
**Convex Combinations:** If, additionally, $0 \le \theta \le 1$, $c$ is a convex combination and lies on the segment between $a$ and $b$.
### Inner Product
The (standard) **inner product** (or dot product) of two $n$-vectors $a$ and $b$ is a **scalar** defined as the sum of the products of their corresponding entries: $$ a^T b = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n $$ The superscript 'T' is used in the notation $a^T b$. Properties of the Inner Product:
- **Commutativity:** $a^T b = b^T a$. The order of the arguments does not matter.
- **Associativity with Scalar Multiplication:** $(\gamma a)^T b = \gamma(a^T b)$, often written as $\gamma a^T b$
- **Distributivity over Vector Addition:** $(a + b)^T c = a^T c + b^T c$.
Key Interpretations and Identities
- **Selecting an Entry:** $e_i^T a = a_i$. The inner product with the $i$th unit vector selects the $i$th element $a_i$.
- **Sum:** $\mathbf{1}^T a = a_1 + \cdots + a_n$, where $\mathbf{1}$ is the vector of ones.
- **Average (Mean):** $(\mathbf{1}/n)^T a = (a_1 + \cdots + a_n)/n$. This average is denoted $\text{avg}(x)$.
- **Sum of Squares:** $a^T a = a_1^2 + \cdots + a_n^2$.
- **Block Vectors:** The inner product of conforming block vectors is the sum of the inner products of the corresponding blocks.
Applications of Inner Product:
- **Co-occurrence:** If $a$ and $b$ are Boolean vectors (0 or 1 entries), $a^T b$ is the total number of indices where both entries are one (e.g., counting objects in the intersection of two subsets).
- **Score/Weighted Sum:** If $f$ is a feature vector and $w$ is a weight vector, $w^T f$ is a weighted sum often referred to as a score (e.g., credit score).
- **Price-Quantity:** If $p$ is a price vector and $q$ is a quantity vector, $p^T q$ is the total cost.
- **Expected Value:** If $p$ is a probability vector and $f$ is a vector of outcome values, $f^T p$ is the expected value of the quantity.
- **Polynomial Evaluation:** If $c$ holds polynomial coefficients and $z$ holds powers of a number $t$, $c^T z$ evaluates the polynomial at $t$.
### Complexity of Vector Computations
Complexity analysis measures the computational effort required for operations, typically by counting the number of floating point operations (**flops**). [[Complexity]]
- **Vector Addition (length $n$):** $n$ flops.
- **Scalar-Vector Multiplication (length $n$):** $n$ flops.
- **Inner Product (length $n$):** $2n$ flops ($n$ multiplications and $n$ additions).
The textbook also notes that the memory storage requirement for an $n$-vector is typically $8n$ bytes.

---
## Chapter 2: Linear Functions
### Linear Functions
A function $f$ that maps $n$-vectors to real numbers ($f: \mathbb{R}^n \to \mathbb{R}$) is a **scalar-valued function of $n$-vectors**. Superposition and Linearity: A function $f$ is **linear** if it satisfies the **superposition** property for all $n$-vectors $x, y$ and all scalars $\alpha, \beta$: $$ f(\alpha x + \beta y) = \alpha f(x) + \beta f(y) $$ This property can be broken down into two components:
- **Homogeneity:** $f(\alpha x) = \alpha f(x)$ (scaling the argument scales the function value).
- **Additivity:** $f(x + y) = f(x) + f(y)$ (adding arguments is the same as adding function values).
The **inner product function** $f(x) = a^T x$ (where $a$ is a fixed $n$-vector) is a linear function.
Inner Product Representation of a Linear Function: The converse is also true: **If a function $f: \mathbb{R}^n \to \mathbb{R}$ is linear, it can always be expressed as the inner product of its argument $x$ with some fixed vector $a$**: $$ f(x) = a^T x $$This is called the **inner product representation** of $f$. The fixed vector $a$ is determined by evaluating $f$ at the standard unit vectors $e_i$: $$ a = (f(e_1), f(e_2), \ldots, f(e_n)) $$
#### Affine Functions
An **affine function** is a linear function plus a constant (offset) $b$: $$ f(x) = a^T x + b $$An affine function satisfies a restricted form of superposition: $$f((1 - \theta)x + \theta y) = (1 - \theta)f(x) + \theta f(y)$$
- If $b \ne 0$, an affine function is **not** linear in the standard mathematical sense.
- The parameters $a$ and $b$ can be found from $n+1$ evaluations: $b = f(0)$ and $a_i = f(e_i) - f(0)$.
### Taylor Approximation
Many functions in science and engineering can be **approximated** by linear or affine functions. The **first-order Taylor approximation** provides a structured way to form an affine approximation of a differentiable function $f: \mathbb{R}^n \to \mathbb{R}$ near a specific point $z$: $$ \hat{f}(x) = f(z) + \nabla f(z)^T (x - z) $$$\nabla f(z)$ is the **gradient**(dx/dy) of $f$ evaluated at $z$. This approximation is generally very good when $x$ is near $z$. 
- Since the approximation $\hat{f}(x)$ has the form $a^T x + \text{constant}$, it is an **affine function**.
### Regression Model
The **regression model** is a commonly used affine function, especially in the context of feature vectors $x$: $$ \hat{y} = x^T \beta + v $$
- $\hat{y}$ is the **prediction** of some true value $y$ (the **dependent variable/outcome/label**). 
- The entries of $x$ are the **regressors**.
- $\beta$ is the $n$-vector of **weights** or **coefficients**.
- $v$ is the **offset** (or intercept).
#### Notation Simplification
The regression model can be simplified by augmenting the feature vector $x$ to $\tilde{x} = [1, x]^T$ and the coefficient vector to $\tilde{\beta} = [v, \beta]^T$, allowing the model to be written as $\hat{y} = \tilde{x}^T \tilde{\beta}$. This is equivalent to assuming the first feature always has the constant value 1.
- Interpretation of Coefficients: The coefficients $\beta$ indicate how the prediction $\hat{y}$ changes with respect to changes in the features $x_i$. For example, in a house price regression model, $\beta_1$ relates to house area and $\beta_2$ relates to the number of bedrooms. A coefficient like $\beta_2$ gives the change in predicted price when $x_2$ increases while keeping other features constant.
---
# #Lecture Lecture
## In Class
1. Variable linear function
y = m.x + b 
f(x) = mx + b, dy/dx = m
on a graph this is a line 
2. Variable 
y = m1.x1 + m2.x2 + b
y = scalar output, x1 and x2 are inputs, m1, m2 and b are constants(scalar)
on a graph this would be a plane on a plane
3. n - variable 
y = m1.x1 + m2.x2 + ..... + mn.xn + b --->Scalar form
y = m(vector)x(vector) + b 	---> Vector form
y = scalar output, m (vector) = m1 m2 ... mn are vector coefficients, x (vector) = x1, x2, ..., xn, vector of constants.
## #Jupyter Jupyter
### Week - 1
Vector equality method: Child class for Vector class.
```python
class VectorEQ(Vector):
    """A child class of the Vector class with the __eq__ method added"""
    
    def __eq__(self,other):
        """return true if "lists" a and b are the equal"""
    
        # step 1 -check the size
        if self.n!=other.n:
            raise Exception("Vectors are not the same length and cannot be equal")
    
        # step 2 - loop
        for i in range(self.n):
            # step 3 - check components
            if self.data[i] != other.data[i]:
                return False
        
        # step 4 - return default case
        return True
```
The class below implements vectors in $\mathbb{R}^n$. The vector components are stored in a python list `data`.
### Vector Class
```python
class Vector:
    """A simple vector class"""

    def __init__(self,X=[]):
        """constructor for vectors"""
        self.data = [x for x in X] # create a new list (in memory)
        self.n = len(X)            # store the size of the list
        
	def __getitem__(self,i):
        """used to access elements via x[i] notation"""
        if 0 <= i < self.n:
            return self.data[i]
        else:
            raise Exception("Index out of bounds")
    
    def __setitem__(self,i,other):
        """used to modify elements via x[i] = other notation"""
        if 0 <= i < self.n:
            self.data[i] = other
        else:
            raise Exception("Index out of bounds")
            
    def __add__(self,other):
        """returns the sum of the vector and the other vector"""
        
        if self.n!=other.n: raise Exception("Vector sizes do not match")
        
        output = Vector(self.data)           # copy current vector
        
        for i in range(self.n):              # loop over current vector
            output.data[i] += other.data[i]  # add value from other vector
        
        return output    # return the output vector
    
    def __sub__(self,other):
        """returns the difference of the vector and the other vector"""
        
        if self.n!=other.n: raise Exception("Vector sizes do not match")
        
        output = Vector(self.data)           # copy current vector
        
        for i in range(self.n):              # loop over current vector
            output.data[i] -= other.data[i]  # add value from other vector
        
        return output    # return the output vector

    def __neg__(self):
        """returns the opposite of the vector"""

        output = Vector(self.data)           # copy current vector
        
        for i in range(self.n):      # loop over current vector
            output.data[i] *= -1     # multiply by -1
        
        return output    # return the output vector

    def __mul__(self,other):
        """multiply by scalar (on the right)"""
        output = Vector(self.data)           # copy current vector
        
        for i in range(self.n):      # loop over current vector
            output.data[i] *= other  # multiply value from other
        
        return output    # return the output vector
    
    def __rmul__(self,other):
        """multiply by scalar (on the left)"""
        output = Vector(self.data)           # copy current vector
        
        for i in range(self.n):      # loop over current vector
            output.data[i] *= other  # multiply value from other
        
        return output    # return the output vector
	
	def __matmul__(self,other):
        """computes the inner product of two vectors -usage x @ y = xTy = x.y"""
        
        if self.n!=other.n: raise Exception("Vector sizes do not match")
        
        output = 0.0
        for i in range(self.n):
            output += self.data[i]*other.data[i]
        
        return output
        
    def __repr__(self):
        """basic printing utility"""
        return str(self.data)
```
### Week - 2
The command `%run file_path` is not python code rather a command to the Jupyter Server to run the code that is in another notebook. This can be used as an alternative to the python code below.
```python
import math
PI = math.pi
```
#### [[#Inner Product]]
$$ a^T b = a_1 b_1 + a_2 b_2 + \cdots + a_n b_n $$
Which computes the sum of products of corresponding entries of the two vectors a and b. To compute a sum, we can recall the accumulator pattern used to compute the sum of the elements in a list.
```python
def loop_sum(L):
    """accumulate the sum of elements from L"""
    total = 0
    for i in range(len(L)):
        total += L[i]
    return total
```
The same expression can be represented in a simpler format using the vector operations. If we consider the list `L` to be a `Vector` object, then we would use the dot product with the ones vector $1^T$ with the following mathematical formula: $sum(x) = x^T(1)$
The method `vector_sum(x)` below implements this vector formula using our Vector class.
```python
def vector_sum(x):
    """accumulate the sum of the elements from Vector x"""
    n = x.n                                # determine the size of x
    ones = Vector([1 for i in range(n)])   # create a ones vector of size n
    return inner_product(x,ones)           # return the dot product
```
Inner product implementation:
```python
def inner_product(x,y):
    """accumulate the sum products of corresponding elements from x and y"""
    # check the length of the vectors
    if x.n != y.n:
        raise Exception("inner_product(x,y): Vector size of x = "+str(x.n)+", but vector size of y = "+str(y.n))
    total = 0                             # initialize the accumulation variable
    for i in range(x.n):                  # loop for the vector length
        total += x.data[i] * y.data[i]    # add the product of corresponding entries
    return total                          # return the accumulation (sum)
```
#### [[#Regression Model]]
A _regression model_ is an [[#Affine Functions]] (linear) function. The input is a vector typically containing data. The output is a scalar which is often a prediction. The function has the form below: $$ \hat{y} = x^T \beta + v $$where $\beta$ is a vector of weights and $v$ is a scalar.
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
## #Quiz [[Quiz]]
1. Each arithmetic operation (`*`, `+`) **creates a new Vector object** using the constructor:
	- `3*e1` → calls `__rmul__`, which calls `Vector(self.data)` once → **1 constructor call**
	- `(-2)*e2` → same → **1 more constructor call**
	- `4*e3` → same → **1 more constructor call**
Now the additions:
	- `(3*e1) + (-2)*e2` → calls `__add__`, which again calls `Vector(self.data)` inside → **1 more constructor call**
	- Then you add `+ 4*e3` → another `__add__` → **1 more constructor call**
**Total constructor calls:** `3 (from scalar multiplications) + 2 (from additions) = 5 constructor calls`
**Concept**: Each arithmetic operation (`*`, `+`) creates new `Vector` objects → leading to multiple constructor calls and memory usage. This helps you understand **computational efficiency** when chaining vector operations.
2. Multiplying a vector by a scalar **scales** its magnitude (length) without changing its direction (except when α is negative, which reverses direction).
- q5. Linear combinations like av⃗+bw⃗a\vec{v} + b\vec{w}av+bw represent **combined effects** of multiple cost (or force, or velocity) components. Each coefficient acts as a scaling factor on its vector’s contribution.

---
# #Homework Coding HW
[[Python]]
```python
class Vector1(Vector):
    """a sub-class of the class above with addition methods"""

    def __getitem__(self,k):
        """returns the component with index k from the vector (if possible)"""
        ###################################################################
        # insert your code here
        if -self.n <= k < self.n:  # allow negatives
            return self.data[k]
        else:
            raise Exception("Index out of bounds")

    def __setitem__(self,k,v):
        """sets the value of component with index k to value v (if possible)"""
        ###################################################################
        # insert your code here
        if -self.n <= k < self.n:  # allow negatives
            self.data[k] = v
        else:
            raise Exception("Index out of bounds")
```
The classes `zeros` and `ones` below are sub-classes of the `Vector` class and are a sort of convenience for our Linear Algebra coding.
```python
class zeros(Vector):
    """a class to construct all zeros vectors"""

    def __init__(self,n):
        ###################################################################
        #super().__init__(...insert code/modify here...)
        # or here
        super().__init__([0]*n)
```
```python
class ones(Vector):
    """a class to construct all ones vectors"""

    def __init__(self,n):
        ###################################################################
        #super().__init__(...insert code/modify here...)
        # or here
        super().__init__([1]*n)
```
The "in-place" methods `__iadd__`, `__isub__`, and `__imul__` are used to implement the usage of the `+=`, `-=`, and `*=` with our vector class.
```python
class Vector3(Vector):
    """a sub-class of the class above with addition methods"""

    def __iadd__(self,other):
        """adds other vector to self in-place"""
        ###################################################################
        # insert code here
        if self.n != other.n:
            raise Exception("Vector sizes not same")
        for i in range(self.n):
            self.data[i] += other[i]
        return self

    def __isub__(self,other):
        """subtracts other vector from self in-place"""
        ###################################################################
        # insert code here
        if self.n != other.n:
            raise Exception("Vector sizes not same")
        for i in range(self.n):
            self.data[i] -= other[i]
        return self

    def __imul__(self,other):
        """multiplies vector self with scalar other in-place"""
        ###################################################################
        # insert code here
        for i in range(self.n):
            self.data[i] *= other
        return self
```
The `__len__` function is to implement the python syntax `len(v)`. For our `Vector` class we should implement the function to return the number of components of the vector.
```python
class Vector4(Vector):
    """a sub-class of the class above with addition methods"""

    def __len__(self):
        """returns the number of components of the vector"""
###################################################################
        # insert code here
        return self.n
```
The `__iter__` function is used in python for a loop by value. The usage for the loop is:
```python
for e in v:
    print(e)
```
This allows us to loop over the elements without explicitly writing `range()` and `len()`.
```python
class Vector5(Vector):
    """a sub-class of the class above with addition methods"""

    def __iter__(self):
        """iterates through the components of the vector yielding the values"""
        ###################################################################
        # insert code here
        for value in self.data:
            yield value
```
---

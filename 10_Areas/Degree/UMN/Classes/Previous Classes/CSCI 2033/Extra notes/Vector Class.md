---
type: class
status: archived
created: 2025-09-19
updated: 2025-10-04
area:
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Midterm - 1|Midterm - 1]]"
  - "[[Final]]"
  - "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 1 & 2]]"
tags:
  - "#class"
next: "[[10_Areas/Degree/UMN/Classes/Previous Classes/CSCI 2033/Week - 1 & 2]]"
---
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
```python
# creating the standard basis vectors for R^3
e1 = Vector([1,0,0])
e2 = Vector([0,1,0])
e3 = Vector([0,0,1])

# computing the norm squared
e1 @ e1
# 1.0
# checking orthogonality
e1 @ e2
# 0.0
x = 3*e1 - 2*e2 + 4*e3  # create vector with linear combination
y = Vector([1,1,1])     # create vector with constructor

# Computing the sum of the components
x @ y                   # compute the dot product
# 5.0
```

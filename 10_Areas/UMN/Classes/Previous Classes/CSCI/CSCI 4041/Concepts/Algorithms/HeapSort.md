---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 0
created: 2026-02-19
topics:
  - "[[Chapter - 6 & 12]]"
  - "[[Introduction to Algorithms]]"
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
related:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5|Week - 5]]"
  - "[[Sorting Algorithms]]"
  - "[[Elementary Data Structures]]"
---
# [[HeapSort]]
## MOC
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5#Jupyter Notebook Explanations|Week - 5]]
- [[Chapter - 6 & 12#Chapter - 6 Heapsort|Chapter - 6 & 12 - Heapsort]]
- [[Sorting Algorithms#Complexity + Tradeoffs|Sorting Algorithms - Complexity + Tradeoffs]]
- [[Elementary Data Structures#Definition|Elementary Data Structures]]

## Definition
- **Heap** means an array interpreted as a nearly complete binary tree.
- **Max-heap** means every parent key is at least as large as its children.
- **Heapsort** builds a max-heap and then repeatedly removes the root into the sorted tail.
- **Priority queue** uses the heap to support fast repeated access to the current maximum or minimum.

## Core Ideas (Textbook)
### Heap Structure
- The shape property is what makes the index formulas work.
- The heap property gives only parent-child order, not full sorted order.
- That weaker invariant is enough for priority queue operations and heapsort.
- The root of a max-heap is always the maximum.

### Heapify and Build
- `MAX-HEAPIFY` repairs one local violation by pushing a bad value downward.
- `BUILD-MAX-HEAP` works bottom-up because leaves are already heaps.
- The linear-time build proof comes from counting node heights, not just counting calls.
- This is one of the standard examples where worst-case-per-call times are too loose for total cost.

### Heapsort and Priority Queues
- Heapsort is in-place and worst-case $O(n \lg n)$.
- It is not stable because swaps move equal keys past one another.
- Priority queue operations are balanced: no operation is constant except reading the maximum.
- Heaps are the compromise structure when we care about repeated best-element access but do not need full sorted traversal all the time.

## Core Ideas (Lecture)
### 0-Indexed Heap Arithmetic
```python
left(i) = 2*i + 1
right(i) = 2*i + 2
parent(i) = (i - 1) // 2
```

The lecture treated this as the key translation from tree to array. If these formulas are automatic, most heap code becomes readable immediately.

### `increase_key` and `extract_max`
```python
def increase_key(i, key):
    A[i] = key
    while i > 0 and A[(i - 1) // 2] < A[i]:
        A[i], A[(i - 1) // 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2
```

```python
def extract_max():
    m = A[0]
    A[0] = A[heap_size - 1]
    heap_size -= 1
    max_heapify(0)
    return m
```

These two routines are the cleanest way to remember directional repair:
- bigger key -> may need to move up
- root replacement with unknown key -> may need to move down

### `arraytree` and `heappriorityqueue`
- `arraytree` stores `A`, `size`, and `capacity`.
- `add_left` and `add_right` compute child slots directly.
- `heappriorityqueue` subclasses that structure and adds heap-specific repair operations.
- The plotting support in the notebook matters because it helps connect the array to the conceptual tree picture.

### CodingHW4 Variants
#### Min-Heap Priority Queue
- Reverse all comparison directions.
- `extract_min` removes the root.
- `decrease_key` bubbles upward instead of downward.

#### Max-Heap Decrease-Key
- Decreasing a key in a max-heap can only create a violation with children.
- That means the repair path is downward, not upward.

#### Heap Delete
- Raise the target to `∞`.
- Bubble it to the root with increase-key.
- Remove it using extract-max.

#### k-Way Merge
- Heap stores `(value, list_index, element_index)`.
- After extracting the smallest current value, push the next value from the same list.
- Total cost is $O(n \lg k)$ because the heap never grows beyond k elements.

## Professor Code From Lecture
### Ch6_ArrayTree.ipynb — `arraytree` Base Class
The `arraytree` class is the foundation for all heap structures in the lecture. It stores the array `A`, `size` (current number of elements), and `capacity` (maximum). The index arithmetic methods `left(i) = 2*i + 1`, `right(i) = 2*i + 2`, and `parent(i) = (i-1)//2` are the 0-indexed translations of the textbook formulas. The `add_left` and `add_right` methods compute child slots directly from the parent index. This class makes the array-to-tree mapping concrete and reusable.
```python
class arraytree:
    """an array-based binary tree"""

    def __init__(self,n,A=None):
        """constructor for array-based binary trees"""
        if A:
            self.A = A
            self.size = n
        else:
            self.A = [None for i in range(n)]
            self.size = 0
        self.capacity = n

    def add_root(self,k):
        """adds key k as root of the tree, returning the index"""
        if self.size == 0:
            self.A[0] = k
            self.size = 1
            return 0
    
    def add_left(self,p,k):
        """adds key k as the left child of node p"""        
        if p < self.capacity and self.A[p] is not None:
            l = self.left(p)           # left child index
            if l < self.capacity:      # check if there is room
                self.A[l] = k
                self.size += 1
            return l               # return index of the new node
    
    def add_right(self,p,k):
        """adds key k as the right child of node p"""        
        if p < self.capacity and self.A[p] is not None:
            r = self.right(p)         # right child index
            if r < self.capacity:     # check if there is room
                self.A[r] = k
                self.size += 1
            return r              # return index of the new node

    def delete(self,x):
        """deletes node x (if it has no children)"""
        l = left(x)     # left child index
        r = right(x)    # right child index
        
        if l < self.capacity and self.A[l] == None:
            if r < self.capacity and self.A[r] == None:
                self.A[x] = None
                self.size -= 1
            elif r >= self.capacity:
                self.A[x] = None
                self.size -= 1
            else:
                print("node",x,"is not a leaf")
        else:
            print("node",x,"is not a leaf")
    
    def left(self,i):
        """returns the index of the left child in a complete array-based tree"""
        return 2*i + 1
    
    def right(self,i):
        """returns the index of the right child in a complete array-based tree"""
        return 2*i + 2
    
    def parent(self,i):
        """returns the index of the parent in a complete array-based tree"""
        return (i-1)//2
```

### Ch6_Heaps.ipynb — `heap` Class (Heapsort)
The `heap` class inherits from `arraytree` and adds the core heap operations. `build_max_heap` iterates from `size//2` down to 0, calling `max_heapify` on each internal node — this is the bottom-up linear-time build. `max_heapify(i)` compares node `i` with its children, swaps with the largest if needed, and recurses downward. This is the local repair operation that fixes one violation. `sort()` implements heapsort: repeatedly swap the root (maximum) with the last element, shrink the heap size, and heapify the new root. The result is an in-place $O(n \lg n)$ sort. The constructor automatically builds a max-heap if data is passed.
```python
class heap(arraytree):
    """a heap class which is a child of the arraytree class based on chapter 6 of CLRS"""

    def __init__(self,n,A=None):
        """constructor for heaps with capacity n"""
        super().__init__(n,A)        # if data is passed here, arraytree will not copy it (in-place).
        if A:                        # if data array is passed to constructor
            self.build_max_heap()    # heapify the data in-place
    
    def sort(self):
        """heap-sort algorithm from CLRS-chapter 6"""
        n = self.size # save original size
        
        for i in range(self.size-1,0,-1):
            self.A[0],self.A[i] = self.A[i],self.A[0]
            self.size = self.size - 1
            self.max_heapify(0)
        
        self.size = n # restore original size (for printing)
    
    def build_max_heap(self):
        """constructs the heap for array A of size n from CLRS-chapter 6"""
        for i in range(self.size//2,-1,-1):
            self.max_heapify(i)
    
    def max_heapify(self,i):
        """max-heapify algorithm from CLRS-chapter 6"""
        
        l = self.left(i)     # left child index
        r = self.right(i)    # right child index
        
        if l < self.size and self.A[l] > self.A[i]: # check for larger child
            largest = l
        else:
            largest = i
        
        if r < self.size and self.A[r] > self.A[largest]:
            largest = r
    
        if largest != i:
            self.A[i],self.A[largest] = self.A[largest],self.A[i]
            self.max_heapify(largest)

    def __str__(self):
        """returns a string for text printing purposes"""
        return str(self.A)
```

### Ch6_Heaps-PriorityQueue.ipynb — `heappriorityqueue` Class
The `heappriorityqueue` class extends the heap with priority queue operations. `maximum()` returns `A[0]` in $O(1)$. `extract_max()` saves the root, replaces it with the last element, shrinks the heap, and heapifies downward — $O(\lg n)$. `increase_key(idx)` bubbles a node upward by comparing with its parent and swapping if the parent is smaller — this is the upward repair direction. `insert(k)` places the new key at the end and calls `increase_key` to restore the heap property. The directional repair pattern is the key insight: bigger key → may need to move up; root replacement → may need to move down.
```python
class heappriorityqueue(arraytree):
    """a heap priority queue class which is a child of the arraytree class based on chapter 6 of CLRS"""

    def __init__(self,n,A=None):
        """constructor for heaps with capacity n"""
        super().__init__(n,A)
        if A:
            self.build_max_heap()
    
    def sort(self):
        """heap-sort algorithm from CLRS-chapter 6"""
        n = self.size
        for i in range(self.size-1,0,-1):
            self.A[0],self.A[i] = self.A[i],self.A[0]
            self.size = self.size - 1
            self.max_heapify(0)
        self.size = n
    
    def maximum(self):
        """returns the max-value from the top of the heap from CLRS-chapter 6"""
        if self.size < 1:
            print("heap underflow")
            return
        return self.A[0]
    
    def extract_max(self):
        """removes the max-value from the top of the heap from CLRS-chapter 6"""
        out = self.A[0]
        self.A[0] = self.A[self.size - 1]
        self.A[self.size - 1] = None
        self.size = self.size - 1
        self.max_heapify(0)
        return out

    def increase_key(self,idx):
        """correct the max heap property, loosely based on CLRS-chapter 6"""
        parent = self.parent(idx)
        while parent >= 0:
            if self.A[parent] < self.A[idx]:
                self.A[parent],self.A[idx] = self.A[idx],self.A[parent]
                idx = parent
                parent = self.parent(idx)
            else:
                break
    
    def insert(self,k):
        """insert key k into the max-heap from CLRS-chapter 6"""
        if self.size==self.capacity:
            print("heap overflow")
            return
        insert_idx = self.size
        self.A[insert_idx] = k
        self.size += 1
        self.increase_key(insert_idx)
    
    def build_max_heap(self):
        """constructs the heap for array A of size n from CLRS-chapter 6"""
        for i in range(self.size//2,-1,-1):
            self.max_heapify(i)
    
    def max_heapify(self,i):
        """max-heapify algorithm from CLRS-chapter 6"""
        l = self.left(i)
        r = self.right(i)
        if l < self.size and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        if r < self.size and self.A[r] > self.A[largest]:
            largest = r
        if largest != i:
            self.A[i],self.A[largest] = self.A[largest],self.A[i]
            self.max_heapify(largest)

    def __str__(self):
        """returns a string for text printing purposes"""
        return str(self.A)
```

## Proof / Reasoning Toolkit
### `BUILD-MAX-HEAP` Linear-Time Checklist
1. Group nodes by height.
2. Count how many nodes can appear at each height.
3. Multiply "nodes at height h" by "heapify cost O(h)."
4. Use the convergent series $\sum h/2^h$ to finish the bound.

### Direction-of-Repair Checklist
1. Ask whether the changed key got bigger or smaller.
2. Ask whether the possible violation is with ancestors or descendants.
3. Repair only along that one possible path.

### Heap/Tree Translation Checklist
1. Decide whether you are working in 1-indexed or 0-indexed form.
2. Translate parent/child formulas once.
3. Keep the formulas consistent across every routine.

## Complexity + Tradeoffs
| Operation / Structure | Time | Why |
| --- | --- | --- |
| `MAX-HEAPIFY` | $O(\lg n)$ | follows one root-to-leaf path |
| `BUILD-MAX-HEAP` | $O(n)$ | most nodes are shallow |
| Heapsort | $O(n \lg n)$ | build once, then n-1 heap repairs |
| `MAXIMUM` | $O(1)$ | root lookup |
| `EXTRACT-MAX` | $O(\lg n)$ | root replacement plus downward repair |
| `INCREASE-KEY` | $O(\lg n)$ | upward bubbling |

## Canonical Examples (Max 5)
### 1. Array-to-Tree Mapping
- Index 0 is the root.
- Index 1 is the left child of the root.
- Index 2 is the right child of the root.
- This is the mental map behind every heap operation.

### 2. Why Build-Heap Is Not $O(n \lg n)$
- There are many leaves and almost-leaves.
- Only a few nodes are near the root with large repair cost.
- The weighted sum of heights is linear.

### 3. Extract-Max
- Save the root.
- Move the last element to index 0.
- Heapify downward until the max-heap property returns.

### 4. Max-Heap Delete
- Inflate target to infinity.
- Bubble it upward.
- Remove it as though it were the root.

### 5. k-Way Merge
- Keep only one frontier element per list in the heap.
- This is the reason the logarithmic factor depends on k, not on the total number of elements.

## Practice Map
- Kth Largest Element
- Top K Frequent Elements
- Merge k Sorted Lists
- Find Median from Data Stream
- Any priority-queue simulation problem where repeated best-choice extraction matters
- CodingHW_4(chapter6_and_12-CLRS).ipynb: min-heap priority queue, max-heap decrease-key, heap delete, k-way merge
- Paper HW - 4 (Ch - 6 & 12).pdf: written problems on heap properties, heapsort analysis, and BST operations

## Mini-test
1. Why does a heap not need full sorted order to support extract-max efficiently?
2. Why is `BUILD-MAX-HEAP` linear?
3. What determines whether heap repair goes up or down?
4. Why does k-way merge use a heap of size k instead of n?
5. Why is heapsort not stable?

## Flashcards
#cards/CSCI4041
1. 0-index heap parent formula::`(i - 1) // 2`.
2. Root of a max-heap::Always the maximum element.
3. `MAX-HEAPIFY` direction::Downward.
4. `INCREASE-KEY` direction in a max-heap::Upward.
5. `BUILD-MAX-HEAP` runtime::$O(n)$.
6. Heapsort stability::Not stable.
7. k-way merge runtime::$O(n \lg k)$.

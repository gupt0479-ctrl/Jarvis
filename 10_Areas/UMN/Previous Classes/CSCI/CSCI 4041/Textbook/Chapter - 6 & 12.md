---
type: class
input_kind: book
status: sprout
created: 2026-02-16
updated: 2026-04-28
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Textbook/Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5|Week - 5]]"
---
# Chapter - 6 Heapsort
## Summary Links
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5#Chapter 6 and Chapter 12 - Heaps, Priority Queues, and BST Operations|Week - 5]]
- [[HeapSort#Definition|HeapSort]]
- [[Elementary Data Structures#Definition|Elementary Data Structures]]

Heapsort is a sorting algorithm with a running time of $O(n \lg n)$. It combines the best attributes of insertion sort and merge sort: it sorts *in place* but maintains asymptotic efficiency. It uses a specialized data structure called a *heap* to manage information.

## 6.1 Heaps
The binary heap is an array object that can be viewed as a nearly complete binary tree. Each node in the tree corresponds to an element of the array.

### Shape + Height Facts
- A heap is a **nearly complete** binary tree: every level is full except possibly the last, which is filled from **left to right**.
- The height of an n-element heap is $\lfloor \lg n \rfloor$.
- In a max-heap, the root of any subtree contains the largest key in that subtree.
- In 1-indexing, the leaves are exactly the indices $\lfloor n/2 \rfloor + 1$ through n.

### Array Mapping
> [!IMPORTANT] **Indexing Translation**
>
> **CLRS 1-indexed**
> - `PARENT(i) = floor(i/2)`
> - `LEFT(i) = 2i`
> - `RIGHT(i) = 2i + 1`
>
> **Python / 0-indexed**
> - `PARENT(i) = (i - 1) // 2`
> - `LEFT(i) = 2i + 1`
> - `RIGHT(i) = 2i + 2`

### Lecture Emphasis
The lecture treated the index formulas as more than notation. They are the reason a heap gives tree behavior without tree pointers. Once you know how to compute parent and child positions in constant time, a plain array becomes a fully navigable nearly complete binary tree.

### `arraytree` Class from Lecture
The `Ch6_ArrayTree.ipynb` notebook made this translation concrete:
- constructor `__init__(self, n, A=None)` either stores an existing array or allocates `[None] * n`
- attributes: `A`, `size`, `capacity`
- `add_left(p, k)` computes `2p + 1`
- `add_right(p, k)` computes `2p + 2`
- in-order traversal uses recursive coordinate generation for plotting

That notebook matters because it shows the array/tree mapping as executable code rather than only formulas.

## 6.2 Maintaining the Heap Property
`MAX-HEAPIFY` is the core repair operation.

```python
MAX-HEAPIFY(A, i)
  l = LEFT(i)
  r = RIGHT(i)
  if l <= A.heap-size and A[l] > A[i]:
      largest = l
  else:
      largest = i
  if r <= A.heap-size and A[r] > A[largest]:
      largest = r
  if largest != i:
      exchange A[i] with A[largest]
      MAX-HEAPIFY(A, largest)
```

- **Precondition:** the left and right subtrees are already max-heaps.
- **Postcondition:** the subtree rooted at i becomes a valid max-heap.
- **Runtime:** $O(\lg n)$ in the worst case because the element may sink along a root-to-leaf path.

### Lecture Emphasis
The lecture rephrased this as "float the bad value down." That is a good mental model. The only node that may violate the heap property is the current root of the local subtree, so the repair follows one downward path rather than branching recursively everywhere.

## 6.3 Building a Heap
The `BUILD-MAX-HEAP` procedure converts an unordered array into a max-heap.

```python
BUILD-MAX-HEAP(A, n)
  A.heap-size = n
  for i = floor(n/2) downto 1:
      MAX-HEAPIFY(A, i)
```

- Leaves need no work because one-element subtrees are already heaps.
- The algorithm proceeds bottom-up from the last internal node to the root.

### Why `BUILD-MAX-HEAP` Is Linear
The naive upper bound is $O(n \lg n)$ because there are O(n) calls to a logarithmic routine. The tight bound is better because most nodes are near the bottom and have very small height.

The textbook proof groups nodes by height:
$$
\sum_{h=0}^{\lfloor \lg n \rfloor} \left\lceil \frac{n}{2^{h+1}} \right\rceil O(h)
$$

Using the geometric-series identity
$$
\sum_{h=0}^{\infty} \frac{h}{2^h} = 2
$$
the total becomes $O(n)$.

That proof is important because it is one of the first cases where "number of calls times worst cost per call" is not tight enough.

## 6.4 The Heapsort Algorithm
`HEAPSORT` uses the heap data structure to sort an array in place.

```python
HEAPSORT(A, n)
  BUILD-MAX-HEAP(A, n)
  for i = n downto 2:
      exchange A[1] with A[i]
      A.heap-size = A.heap-size - 1
      MAX-HEAPIFY(A, 1)
```

- `BUILD-MAX-HEAP` costs $O(n)$.
- The loop runs n-1 times, and each iteration calls `MAX-HEAPIFY`.
- Total running time is $O(n \lg n)$.
- Heapsort is **in-place** but **not stable**.

## 6.5 Priority Queues
A heap is an efficient structure for implementing a priority queue.

### Max-Priority Queue Operations
- `MAXIMUM(S)`: return the largest key.
- `EXTRACT-MAX(S)`: remove and return the largest key.
- `INCREASE-KEY(S, x, k)`: increase a key and bubble it upward.
- `INSERT(S, x, k)`: append a sentinel value and then call increase-key.

### Implementation Comparison Table
| Structure | Insert | Extract-Max | Why It Loses / Wins |
| --- | --- | --- | --- |
| Sorted linked list | $Θ(n)$ | $O(1)$ | Great removal, slow insert |
| Unsorted linked list | $O(1)$ | $Θ(n)$ | Great insert, slow removal |
| Sorted array | $Θ(n)$ | $O(1)$ or $O(\lg n)$ lookup | Shifting is expensive |
| Heap | $O(\lg n)$ | $O(\lg n)$ | Best overall balance |

### Lecture `heappriorityqueue`
The notebook implementation added:
- `build_heap`
- `increase_key(i, key)` with upward bubbling
- `extract_max` by moving the last element to the root and heapifying down

### CodingHW4 Extensions
- **Min-heap PQ:** flip all comparisons, so extract-min removes the root and decrease-key bubbles upward.
- **MAX-HEAP-DECREASE-KEY:** decreasing a key in a max-heap means the violation can only move downward.
- **MAX-HEAP-DELETE:** set the target to infinity, float it to the root, then extract-max.
- **k-way merge:** store `(value, list_index, element_index)` in a min-heap of size k for total $O(n \lg k)$ work.

# Chapter - 12 Binary Search Trees
A binary search tree supports dynamic-set operations including `SEARCH`, `MINIMUM`, `MAXIMUM`, `PREDECESSOR`, `SUCCESSOR`, `INSERT`, and `DELETE`.

## 12.1 What is a Binary Search Tree?
A BST is a linked structure where each node has:
- `key`
- `left`
- `right`
- `p`

The BST property says:
- keys in the left subtree are `<= x.key`
- keys in the right subtree are `>= x.key`

Because of this, an inorder tree walk prints the keys in sorted order.

## 12.2 Querying a Binary Search Tree
All query operations run in $O(h)$ time where h is the tree height.

- **Search:** go left if the target is smaller, right if larger.
- **Minimum:** follow left pointers until None.
- **Maximum:** follow right pointers until None.
- **Successor:** if there is a right subtree, take its minimum; otherwise move upward until you come from a left child.
- **Predecessor:** symmetric version using the left subtree or upward traversal.

### Lecture Emphasis
The Week 5 homework made predecessor explicit:

```python
TREE-PREDECESSOR(x)
    if x.left != None:
        return max(x.left)
    y = x.p
    while y != None and x == y.left:
        x = y
        y = y.p
    return y
```

This is a useful exam template because it mirrors the successor logic cleanly.

## 12.3 Insertion and Deletion
Insertion adds a new node in $O(h)$ time by following the search path until a None child is reached.

Deletion is more complex and is easiest to remember through the case breakdown.

### BST Delete — Full Walkthrough
1. **Case 1: no left child**
   - `transplant(z, z.right)`
2. **Case 2: no right child**
   - `transplant(z, z.left)`
3. **Case 3: two children and successor is `z.right`**
   - `y = min(z.right)`
   - `transplant(z, y)`
   - `y.left = z.left`
   - `y.left.p = y`
4. **Case 4: two children and successor is deeper in the right subtree**
   - `y = min(z.right)`
   - `transplant(y, y.right)`
   - `y.right = z.right`
   - `y.right.p = y`
   - `transplant(z, y)`
   - `y.left = z.left`
   - `y.left.p = y`

### Transplant
`TRANSPLANT(T, u, v)` replaces the subtree at u with the subtree at v.

- if `u.p == None`, make v the root
- else if `u` is a left child, set `u.p.left = v`
- else set `u.p.right = v`
- if `v != None`, set `v.p = u.p`

It does **not** touch `u.left` or `u.right`. That is why the delete routine must reconnect those explicitly.

### Worked Successor Example
The lecture example worth memorizing is:
- delete node 67
- its right child is 89
- but 89 has a left subtree containing 77

Then `min(89)` is 77, so **77 replaces 67**, not 89. This is the cleanest way to remember that successor means "next key in sorted order," not "immediate right child."

### CodingHW4 BST Items
- predecessor routine
- proof that `TREE-MINIMUM` followed by repeated `TREE-SUCCESSOR` visits all nodes in $Θ(n)$ total time because each edge is traversed at most twice

> [!IMPORTANT] **Implementation Reminder**
> The chapter is written conceptually in 1-indexed CLRS style, but the actual BST implementation is pointer-based. Once you are in Python or Java, the important translation is not array indexing; it is keeping the parent/child references consistent after every mutation.

---

## Overview
- Chapters 6 and 12 pair an array-based tree structure with a pointer-based search tree structure.
- In CSCI 4041, this note supports heapsort, priority queues, BST search/update operations, and later algorithms that reuse priority queues such as Prim, Dijkstra, and Huffman coding.
- The course implementation emphasis is translation: CLRS often presents 1-indexed pseudocode, while the lecture code uses Python 0-indexed arrays and linked nodes.

## Core Definitions
- **Binary heap:** an array representing a nearly complete binary tree that satisfies the heap property.
- **Max-heap property:** every node has key at least as large as its children.
- **Priority queue:** an abstract data type supporting operations such as maximum/minimum, extract, and key update.
- **Binary search tree:** a linked binary tree where all keys in a node's left subtree are at most the node key and all keys in the right subtree are at least it.
- **Successor/predecessor:** next larger / next smaller key in sorted order.
- **Transplant:** BST helper that replaces one subtree with another while preserving parent links.

## Main Algorithms
- `MAX-HEAPIFY`: repairs one possible heap violation by pushing a key down.
- `BUILD-MAX-HEAP`: calls heapify bottom-up from the last internal node.
- `HEAPSORT`: repeatedly swaps the max element to the end and heapifies the reduced heap.
- `HEAP-EXTRACT-MAX`, `HEAP-INCREASE-KEY`, `MAX-HEAP-INSERT`: implement max-priority queue behavior.
- `TREE-SEARCH`, `TREE-MINIMUM`, `TREE-MAXIMUM`, `TREE-SUCCESSOR`, `TREE-DELETE`: core BST operations.

## Correctness Ideas
- `MAX-HEAPIFY` assumes the left and right subtrees are already heaps; only the root of that subtree may violate the heap property.
- `BUILD-MAX-HEAP` works because every leaf is already a heap, and processing internal nodes bottom-up satisfies the heapify precondition.
- Heapsort maintains the invariant that the suffix after `heap_size` is sorted and contains the largest elements.
- BST search correctness follows from the ordering invariant at every node.
- BST deletion correctness is mostly pointer hygiene: after replacing a node with its successor, the in-order key order must remain unchanged.

## Complexity
- `MAX-HEAPIFY` is `O(lg n)` because it moves down at most the heap height.
- `BUILD-MAX-HEAP` is `Theta(n)`, not `Theta(n lg n)`, because most nodes are near the leaves.
- Heapsort is `Theta(n lg n)` time and `O(1)` extra array space.
- BST search/insert/delete are `O(h)`, where `h` is tree height; this is `O(lg n)` for balanced trees and `O(n)` in the worst unbalanced case.

## Lecture Emphasis
- `Lectures/Week - 5/Ch6_ArrayTree.ipynb` grounds heaps in the array-tree representation.
- `Lectures/Week - 5/Ch6_Heaps.ipynb` implements `heap`, `build_max_heap`, `max_heapify`, and `sort`.

```python
def build_max_heap(self):
    for i in range(self.size//2,-1,-1):
        self.max_heapify(i)
```

- `Lectures/Week - 5/Ch6_Heaps-PriorityQueue.ipynb` extends the heap into a priority queue with `maximum`, `extract_max`, and insert/key-update behavior.
- `Lectures/Week - 5/Ch12_BinarySearchTree.ipynb` implements the pointer-based BST. The most important bridge is that textbook `left`, `right`, and `p` fields become node references.
- `Homework/Coding/CodingHW_4(chapter6_and_12-CLRS).ipynb` asks for a min-priority queue and BST predecessor/successor-style operations, directly matching this note.
- Weekly/concept links: [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5|Week - 5]], [[HeapSort|HeapSort]], [[Elementary Data Structures|Elementary Data Structures]].

## Examples
- In a 0-indexed heap array, children of `i` are `2*i+1` and `2*i+2`; this is the lecture translation of CLRS's 1-indexed formulas.
- In a BST, the successor of a node with a right child is the minimum of the right subtree.
- If a BST node has two children, deletion usually copies/transplants the successor, because the successor is the smallest key larger than the deleted node.

## Connections
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5|Week - 5]]
- [[HeapSort|HeapSort]]
- [[Elementary Data Structures|Elementary Data Structures]]
- [[Chapter - 21|Chapter - 21]] and [[Chapter - 22|Chapter - 22]] reuse priority queues in Prim and Dijkstra.
- Source homework read: `Homework/Coding/CodingHW_4(chapter6_and_12-CLRS).ipynb` and `Homework/Paper/Paper HW - 4 (Ch - 6 & 12).pdf`.
- TODO: source gap - no vault Homework/Paper Homework note exists for direct wikilinking.

## Common Pitfalls
- Calling `BUILD-MAX-HEAP` `Theta(n lg n)` because it calls heapify many times; the tighter bound is `Theta(n)`.
- Mixing CLRS 1-indexed heap formulas with Python 0-indexed formulas.
- Assuming BST operations are always logarithmic without a balance guarantee.
- Losing parent pointers during BST deletion/transplant.

## Review Checklist
- [ ] Translate heap parent/left/right formulas between 1-indexed and 0-indexed arrays.
- [ ] Implement `max_heapify`, `build_max_heap`, heapsort, and priority-queue operations.
- [ ] Explain why `BUILD-MAX-HEAP` is linear.
- [ ] Implement BST search, min/max, successor/predecessor, insert, and delete.
- [ ] Analyze BST operations in terms of height.

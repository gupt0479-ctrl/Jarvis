---
type: class
input_kind: lecture
status: sprout
created: 2026-02-16
updated: 2026-04-16
area:
  - "[[CSCI 4041 Board]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/DSA|DSA]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Introduction to Algorithms|Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]]"
---
# Entire Week
## What you must be able to do
- [[Chapter - 6 & 12#6.1 Heaps|Chapter - 6 heaps]], [[Chapter - 6 & 12#6.3 Building a Heap|build-max-heap]], and [[HeapSort#Proof / Reasoning Toolkit|HeapSort - Proof / Reasoning Toolkit]]: translate between tree and array indices, explain `MAX-HEAPIFY`, and prove why `BUILD-MAX-HEAP` is linear instead of $O(n \lg n)$.
- [[Chapter - 6 & 12#6.5 Priority Queues|priority queues]], [[HeapSort#Core Ideas (Lecture)|HeapSort - Core Ideas (Lecture)]], and [[Elementary Data Structures#BST Delete — 4 Cases|Elementary Data Structures - BST Delete — 4 Cases]]: compare priority queue implementations and know the standard heap operations and their coding-homework variants.
- [[Chapter - 6 & 12#12.2 Querying a Binary Search Tree|BST queries]] and [[Chapter - 6 & 12#12.3 Insertion and Deletion|BST deletion]]: explain successor, predecessor, transplant, and the full delete case breakdown.
- [[HeapSort#Practice Map|HeapSort - Practice Map]] and [[Elementary Data Structures#Practice Map|Elementary Data Structures - Practice Map]]: top-k heap problems and BST validation/delete practice are still open.

## Key ideas (textbook)
- **A heap is a tree encoded by index arithmetic.** The structure looks like a binary tree conceptually, but the implementation uses constant-time formulas for parent and child positions. That is why heaps are fast without needing pointer-heavy node objects.
- **`MAX-HEAPIFY` is a local repair routine.** It assumes the left and right subtrees are already heaps and only fixes the current root by sinking it downward. This local guarantee is what makes bottom-up heap construction work.
- **`BUILD-MAX-HEAP` is linear because most nodes are shallow.** The proof groups nodes by height instead of giving every node the full logarithmic worst-case cost. This is one of the first places where a naive "n calls times log n each" bound is too pessimistic.
- **Priority queues are about operation balance.** Sorted and unsorted lists each make one priority-queue operation cheap and another expensive. Heaps win because they keep both insertion and removal logarithmic.
- **BST deletion is a pointer-rewiring problem, not just a search problem.** The algorithm is easy to lose track of unless you separate successor selection from transplant and from child reconnection. The full case breakdown is worth memorizing exactly.

## Concepts created / updated today
- [[HeapSort#Definition|HeapSort]]
- [[Elementary Data Structures#BST Delete — 4 Cases|Elementary Data Structures - BST Delete — 4 Cases]]
- [[Chapter - 6 & 12#12.3 Insertion and Deletion|Chapter - 6 & 12 - BST insertion and deletion]]

## Lecture
### Chapter 6 and Chapter 12 - Heaps, Priority Queues, and BST Operations
This week connected two different structures that both support priority-style operations, but in very different ways. Heaps are array-based and intentionally sacrifice sorted order everywhere except along parent-child relationships. BSTs preserve a full search-tree ordering, which makes successor, predecessor, and inorder traversal meaningful. The lecture contrast was useful because it forces the right question: what operations do we actually want to optimize? If we only need repeated access to the maximum or minimum, a heap is a better fit than a fully ordered tree.

The heap half of the week emphasized that the tree picture is not just conceptual decoration. The formulas `left(i) = 2i + 1`, `right(i) = 2i + 2`, and `parent(i) = (i - 1) // 2` are the entire reason heaps are efficient in arrays. The `arraytree` notebook made this visual by building a binary tree directly inside a list and plotting it. Once that mapping is clear, `MAX-HEAPIFY` becomes straightforward: only one node may violate the heap property, so the bad value sinks down one path until the ordering is repaired. `BUILD-MAX-HEAP` is then just repeated local repairs from the bottom upward. The lecture's proof that this is linear, not $O(n \lg n)$, matters because it is the first big example where "do the tight summation" beats the naive bound by a full logarithmic factor.

The BST half of the week focused on mutation logic. Search, minimum, maximum, successor, and predecessor are all just path-following routines, but delete is the first time tree structure really changes. The transplant helper was the lecture's main simplifier: instead of rewriting parent-boundary pointer logic every time, transplant encapsulates "plug subtree v into the place where subtree u used to be." Once you understand that transplant does only parent-boundary rewiring, the delete cases make more sense. The famous "67 is replaced by 77, not 89" example is useful because it forces you to think of successor as `min(z.right)` rather than as "whatever is on the right."

### Jupyter Notebook Explanations
#### Ch6_ArrayTree.ipynb
This notebook turns index arithmetic into a real class.

```python
# 0-index formulas used by the lecture code
left(i) = 2*i + 1
right(i) = 2*i + 2
parent(i) = (i - 1) // 2
```

The `arraytree` class stores an array `A`, a `size`, and a `capacity`. `add_left(p, k)` and `add_right(p, k)` compute child indices using those formulas and then store the new value directly into the correct array slot. The plotting support matters because it makes the "array as tree" view much easier to internalize.

#### Ch6_Heaps.ipynb and Ch6_Heaps-PriorityQueue.ipynb
These notebooks add heap behavior on top of the array tree.

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

`increase_key` is an upward repair because increasing a key can only violate the max-heap property with ancestors. `extract_max` is a downward repair because moving the last element to the root can only violate the property with children. That directional difference is worth memorizing because the homework later asks for the symmetric variants.

#### CodingHW_4(chapter6_and_12-CLRS).ipynb
This homework made the heap story more complete:
- **Min-heap priority queue:** reverse the comparison direction so the smallest item lives at the root.
- **MAX-HEAP-DECREASE-KEY:** when a max-heap key gets smaller, the damage can only move downward.
- **MAX-HEAP-DELETE:** raise the target to `∞`, bubble it to the root, then extract-max.
- **k-way merge:** keep one current element from each list in a min-heap of size k so the total merge time is $O(n \lg k)$ instead of flattening and resorting.
- **TREE-PREDECESSOR** and the repeated-successor traversal proof extended the BST query side of the chapter.

#### Ch12_BinarySearchTree.ipynb and Ch12_Examples.ipynb
The BST notebooks supply the exact traversal and delete logic used all week.

```python
def in_order(T, node):
    if node:
        in_order(T, node.left)
        print(node.key)
        in_order(T, node.right)
```

```python
def transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v != None:
        v.p = u.p
```

The lecture stressed that transplant does not "fix the tree." It only replaces one subtree at the parent boundary. The delete routine has to reconnect `y.left`, `y.right`, and their parent pointers explicitly in the two-child cases.

## Examples worth keeping
- **Heap index formulas:** in 0-index form, left = `2i+1`, right = `2i+2`, parent = `(i-1)//2`.
- **Build-max-heap proof idea:** many nodes have height 0 or 1, so the average heapify cost is small even though the worst-case single call is logarithmic.
- **k-way merge:** min-heap stores `(value, list_index, element_index)` so the next element from the same list is found in $O(1)$ after each extraction.
- **Successor example:** deleting 67 with right child 89 and left descendant 77 means 77 is the replacement.
- **Predecessor logic:** if a node has a left subtree, predecessor is the maximum in that left subtree; otherwise walk upward until you come from the right.

## Takeaways (questions to resolve)
- [ ] Why is `BUILD-MAX-HEAP` linear even though `MAX-HEAPIFY` is logarithmic?
- [ ] When does heap repair move upward versus downward?
- [ ] Why does the k-way merge heap need both list index and element index?
- [ ] What exactly does transplant do, and why is that not enough by itself for delete?
- [ ] Why is the successor of a node with two children not always its direct right child?

## Flashcards
#cards/CSCI4041
1. 0-index heap left child formula::`2i + 1`.
2. 0-index heap right child formula::`2i + 2`.
3. 0-index heap parent formula::`(i - 1) // 2`.
4. Why is `BUILD-MAX-HEAP` linear::Because most nodes are near the leaves and require very little sinking work.
5. What does `EXTRACT-MAX` do after removing the root::Move the last element to the root and heapify downward.
6. Successor of a BST node with a right subtree::The minimum node in that right subtree.
7. What does transplant deliberately not do::It does not reconnect the deleted node's left and right children for you.

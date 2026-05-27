---
type: concept
course: CSCI 4041
status: sprout
mastery (1/10): 0
created: 2026-02-11
topics:
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
  - "[[Chapter - 7 & 10]]"
  - "[[CSCI 4041 Board]]"
related:
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4|Week - 4]]"
---
# [[Elementary Data Structures]]
## MOC
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 4#Jupyter Notebook Explanations|Week - 4]]
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 5#Jupyter Notebook Explanations|Week - 5]]
- [[Chapter - 7 & 10#10.1 Simple Array-Based Data Structures|Chapter - 7 & 10 - Simple Array-Based Data Structures]]
- [[Chapter - 6 & 12#Chapter - 12 Binary Search Trees|Chapter - 6 & 12 - Binary Search Trees]]

## Definition
- **Dynamic set** means a collection that supports updates over time instead of staying fixed.
- **Stack** is a last-in, first-out structure.
- **Queue** is a first-in, first-out structure.
- **Linked list** stores order through pointers instead of array positions.
- **Binary search tree** stores keys so that left-subtree keys are smaller and right-subtree keys are larger, making search directional rather than linear.

## Core Ideas (Textbook)
### Array-Based Structures
- Arrays are contiguous memory, which makes indexing constant time.
- Stacks and queues become simple because the structure chooses which item may be removed next.
- The textbook queue is circular because wraparound avoids shifting elements.
- Implementation details like full versus empty detection are part of the data-structure invariant, not an afterthought.

### Linked Lists
- Linked lists trade direct indexing for flexible insertion and deletion.
- Doubly linked lists add `prev` so deletion is constant time once the node is known.
- Singly linked lists save space but make some operations harder.
- Sentinels eliminate edge-case branching by making head and tail updates look like ordinary pointer rewiring.

### Trees and BSTs
- Tree nodes store parent/child relationships instead of relying on array position.
- In-order traversal is the most important BST traversal because it exposes sorted order.
- Search, minimum, maximum, successor, predecessor, insert, and delete all depend on the tree height.
- BST deletion is the first nontrivial tree-structure mutation, so its cases are worth memorizing.

## Core Ideas (Lecture)
### Array Stack and Circular Queue
```python
# stack
top = -1
# push: top += 1; A[top] = x
# pop:  if top == -1 -> underflow
```

```python
# circular queue
# empty: head == tail
# full: (tail + 1) % n == head
```

The lecture point was that these are not just formulas to memorize. They encode the representation invariant of the structure. If you lose track of what `top`, `head`, or `tail` mean, the implementation falls apart immediately.

### CodingHW3 Variants
#### Two Stacks in One Array
```python
l_top = -1
r_top = n
# overflow when l_top + 1 == r_top
```

- Left stack grows right from index 0.
- Right stack grows left from index `n-1`.
- Neither stack needs a fixed capacity upfront; they share the array until they meet.

#### Linked Stack and Linked Queue
- Linked stack: push = prepend, pop = remove head.
- Linked queue: enqueue must append to a tail pointer, dequeue removes from head.
- The tail pointer is the missing detail that keeps queue operations at $O(1)$.

#### Reverse Linked List
```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev, curr = curr, nxt
return prev
```

What this code is doing:
1. `prev` tracks the reversed prefix.
2. `curr` tracks the remaining unreversed suffix.
3. `nxt` temporarily saves the old forward link so the rest of the list is not lost.
4. Each loop iteration moves one node from the unreversed part to the front of the reversed part.

### BST Node Structure and Traversals
```python
class node:
    def __init__(self, k=None, parent=None, left_child=None, right_child=None):
        self.key = k
        self.p = parent
        self.left = left_child
        self.right = right_child
```

```python
def in_order(T, node):
    if node:
        in_order(T, node.left)
        print(node.key)
        in_order(T, node.right)
```

The lecture treated the parent pointer `p` as essential, not optional. Later delete, predecessor/successor, AVL rebalancing, and transplant all depend on the ability to walk back up the tree.

### BST Delete — 4 Cases
1. **No left child**
   - `transplant(z, z.right)`
2. **No right child**
   - `transplant(z, z.left)`
3. **Two children, successor is z.right**
   - `transplant(z, y)` then attach `z.left` under y
4. **Two children, successor is deeper in the right subtree**
   - `transplant(y, y.right)`
   - `y.right = z.right`
   - `transplant(z, y)`
   - `y.left = z.left`

### BST Delete — 4 Cases
The important lecture correction was that the successor is **not automatically the right child**. It is the minimum of the right subtree. That is why deleting 67 in a tree where the right child is 89 but 89 has left child 77 means 77 replaces 67.

### Transplant
`TRANSPLANT(u, v)` only does parent-side rewiring:
- if `u.p == None`, then the root becomes v
- else replace the correct child pointer of `u.p`
- if `v != None`, set `v.p = u.p`

It does **not** touch `u.left` or `u.right`. That is why the delete routine has to reconnect those manually in the two-child cases.

## Proof / Reasoning Toolkit
### Structure-Invariant Checklist
1. Identify the state variables that define the structure.
2. Say exactly what each variable means.
3. Show how one operation preserves those meanings.
4. Use the invariant to explain correctness, not just complexity.

### Pointer-Manipulation Checklist
1. Save any pointer you are about to overwrite.
2. Rewire one local edge at a time.
3. Recheck parent and child links in both directions.
4. Use a tiny example mentally before trusting the general case.

### BST Delete Checklist
1. Decide whether the node has 0, 1, or 2 children.
2. If 2 children, compute the successor as `min(z.right)`.
3. Separate the `y == z.right` case from the deeper-successor case.
4. Use transplant for parent-boundary rewiring, then reconnect children explicitly.

## Complexity + Tradeoffs
| Structure | Search | Insert | Delete | Key Tradeoff |
| --- | --- | --- | --- | --- |
| Stack (array) | N/A | $O(1)$ | $O(1)$ | Fast, simple, fixed contiguous storage |
| Queue (array) | N/A | $O(1)$ | $O(1)$ | Circular indexing needed |
| Linked list | $Θ(n)$ | $O(1)$ local | $O(1)$ local | Easy local updates, poor random access |
| BST (balanced) | $O(\lg n)$ | $O(\lg n)$ | $O(\lg n)$ | Ordered operations supported |
| BST (skewed) | $O(n)$ | $O(n)$ | $O(n)$ | Sensitive to insertion order |

## Canonical Examples (Max 5)
### 1. Circular Queue Detection
- Empty: `head == tail`
- Full: `(tail + 1) % n == head`
- Common mistake: trying to use all n slots without adding another variable to distinguish states.

### 2. Two Stacks in One Array
- Left stack grows right.
- Right stack grows left.
- Overflow only when the two fronts collide.

### 3. Reverse Linked List
- `[1 -> 2 -> 3]` becomes `[3 -> 2 -> 1]`.
- The saved `nxt` pointer is what prevents the rest of the list from being lost.

### 4. BST Successor Example
- Deleting 67 with right child 89 and 89.left = 77 gives successor 77.
- Common mistake: replacing with 89 just because it is the direct right child.

### 5. In-Order Traversal
- Left, root, right prints a BST in sorted order.
- This is the easiest sanity check after insert or delete.

## Practice Map
- Valid Parentheses
- Implement Queue using Stacks
- Reverse Linked List
- Binary Tree Inorder Traversal
- Validate BST
- CodingHW_3(chapter10-CLRS).ipynb: two stacks in one array, deque, linked-stack/queue, list reversal
- Paper HW - 3 (Ch - 7 & 10).pdf: written problems on stacks, queues, linked lists, and BST operations

## Mini-test
1. Why does a circular queue waste one array slot?
2. Why is a tail pointer required for an $O(1)$ linked queue?
3. What does the parent pointer buy you in a BST?
4. Why is `min(z.right)` the right way to define the successor in delete?
5. What does transplant do, and what does it deliberately not do?

## Flashcards
#cards/CSCI4041
1. Stack underflow in 0-index form::`top == -1`.
2. Circular queue empty condition::`head == tail`.
3. Circular queue full condition::`(tail + 1) % n == head`.
4. In-order traversal meaning::It prints BST keys in sorted order.
5. BST successor of a node with a right subtree::The minimum node in that right subtree.
6. Why is `TRANSPLANT` useful::It centralizes parent-boundary subtree replacement logic.
7. Reverse linked list extra space::$O(1)$.

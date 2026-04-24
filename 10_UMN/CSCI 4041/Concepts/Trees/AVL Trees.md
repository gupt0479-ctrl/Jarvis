---
type: concept
course: CSCI 4041
status: tree
mastery (1/10): 4
created: 2026-02-23
updated: 2026-04-16
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[10_UMN/CSCI 4041/Textbook/Chapter - 13]]"
related:
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Elementary Data Structures]]"
  - "[[B-Trees]]"
  - "[[10_UMN/CSCI 4041/Week - 6|Week - 6]]"
---
# [[AVL Trees]]
## MOC
- [[10_UMN/CSCI 4041/Week - 6#Jupyter Notebook Explanations|Week - 6]]
- [[10_UMN/CSCI 4041/Week - 7#Jupyter Notebook Explanations|Week - 7]]
- [[10_UMN/CSCI 4041/Textbook/Chapter - 13#AVL Notes Anchored to Chapter 13|Chapter - 13 - AVL notes anchored to Chapter 13]]
- [[10_UMN/CSCI 4041/Concepts/Data Structures & Methods/Elementary Data Structures#BST Delete — 4 Cases|Elementary Data Structures - BST Delete — 4 Cases]]

## Definition
- **AVL tree** is a BST in which the left and right subtree heights at every node differ by at most 1.
- **Balance factor** is `left_height - right_height`.
- **Rotation** is a local pointer rewiring that preserves BST order while improving shape.
- **Goal** is worst-case logarithmic height for search, insert, and delete.

## Core Ideas (Textbook)
### Why Balanced Trees Matter
- A plain BST can become a chain on sorted insertions.
- Once height becomes linear, every query and update becomes linear.
- Balanced trees exist to force height back to logarithmic scale.
- Chapter 13 supplies the rotation machinery that AVL reuses.

### Rotation View
- Left and right rotations are local operations.
- They preserve inorder key ordering.
- Their job is to move one "heavy" child upward and move the middle subtree across.
- The correctness argument is about preserved key intervals, not just pointer assignments.

### Height Bound Idea
- The original AVL paper studies the minimum number of nodes needed for a given height.
- That minimum obeys a Fibonacci-like recurrence.
- Faster-than-Fibonacci growth in node count implies logarithmic growth in height.
- That is the structural reason AVL operations are logarithmic.

## Core Ideas (Lecture)
### `balancedtree` Height Scaffold
```python
def compute_height(x):
    left_height = 1 + x.left.height if x.left else 0
    right_height = 1 + x.right.height if x.right else 0
    return left_height, right_height

def update_height(x):
    L, R = compute_height(x)
    x.height = max(L, R)
    return L, R
```

The lecture's visualization made these two functions central. Stored height is one thing; the freshly computed `(L, R)` pair is another. The balance factor is `L - R`, not the stored height itself.

### Rotation Primitive
```python
y = x.right
x.right = y.left
if y.left != T.nil:
    y.left.p = x
y.p = x.p
...
y.left = x
x.p = y
```

The lecture kept a simple checklist:
1. identify the new subtree root
2. move the middle subtree across
3. repair parent pointers

### Four Rotation Cases in AVLTree
| Case | Condition | Repair |
| --- | --- | --- |
| LL | `bf(x) == 2` and `bf(x.left) >= 0` | `right_rotate(x)` |
| RR | `bf(x) == -2` and `bf(x.right) <= 0` | `left_rotate(x)` |
| LR | `bf(x) == 2` and `bf(x.left) < 0` | `left_rotate(x.left)` then `right_rotate(x)` |
| RL | `bf(x) == -2` and `bf(x.right) > 0` | `right_rotate(x.right)` then `left_rotate(x)` |

### Trigger Sequences
- LL -> `[30,20,10]`
- RR -> `[10,20,30]`
- LR -> `[30,10,20]`
- RL -> `[10,30,20]`

### AVL Project / Experiment Notebook
```python
def insertion_seq(n):
    keys = list(range(1, n + 1))
    result = []
    def pick(arr):
        if not arr:
            return
        mid = len(arr) // 2
        result.append(arr[mid])
        pick(arr[:mid])
        pick(arr[mid + 1:])
    pick(keys)
    return result
```

This creates a near-best-case insertion order with zero rotations. The lecture paired this with ascending and descending worst cases to show how rotation counts depend on insertion order even when the final structure stays logarithmic.

### Validation Checks
- `is_bst`
- `is_avl`
- `check_parent_pointers`
- `check_heights`

These checks are important because AVL bugs often preserve one invariant while breaking another.

## Proof / Reasoning Toolkit
### Rotation Correctness Checklist
1. Identify the three affected key ranges.
2. Show the middle subtree still stays between the same two keys after rotation.
3. Conclude inorder order is unchanged.

### AVL Height-Bound Checklist
1. Define `N_h` as the minimum nodes in any AVL tree of height h.
2. Observe that the two child heights must differ by at most 1.
3. Derive `N_h = N_{h-1} + N_{h-2} + 1`.
4. Compare this growth to Fibonacci to conclude logarithmic height.

### Debugging Checklist
1. Recompute balance factors from scratch, do not trust stored heights.
2. Verify child-to-parent pointers in both directions.
3. Check inorder traversal separately from balance.
4. Test all four rotation trigger patterns directly.

## Complexity + Tradeoffs
| Operation | AVL Tree | Why |
| --- | --- | --- |
| Search | $O(\lg n)$ | height is logarithmic |
| Insert | $O(\lg n)$ | update path plus local rotations |
| Delete | $O(\lg n)$ | successor logic plus upward repair |
| Extra storage | $O(1)$ per node | height field |

AVL trees are usually more tightly balanced than red-black trees, which often means faster lookups but stricter update bookkeeping.

## Canonical Examples (Max 5)
### 1. LL Case
- Insert `[30,20,10]`.
- Root becomes left-heavy by 2.
- One right rotation repairs the tree.

### 2. RR Case
- Insert `[10,20,30]`.
- Root becomes right-heavy by 2.
- One left rotation repairs the tree.

### 3. LR Case
- Insert `[30,10,20]`.
- The heavy side bends inward.
- Requires a left rotation on the child, then a right rotation on the root.

### 4. RL Case
- Insert `[10,30,20]`.
- Mirror of LR.
- Requires right rotate on the child, then left rotate on the root.

### 5. Best-Case Insertion Sequence
- `insertion_seq(n)` inserts medians before extremes.
- This keeps the tree balanced as it grows.
- It shows that AVL trees do not always rotate often.

## Practice Map
- Balanced Binary Tree
- Validate BST
- Convert Sorted Array to BST
- Trace AVL insertions by hand
- Write out LL/RR/LR/RL repairs on small trees without code

## Mini-test
1. Why does AVL need a height field in this implementation?
2. How do you distinguish LR from LL once you know a node is left-heavy?
3. What does `(L, R)` represent in the lecture visualization?
4. Why does the Fibonacci-style recurrence imply logarithmic height?
5. Why are parent-pointer checks separate from BST-order checks?

## Flashcards
#cards/CSCI4041
1. AVL balance rule::At every node, the left and right subtree heights differ by at most 1.
2. LL repair::Right rotate the imbalanced node.
3. RR repair::Left rotate the imbalanced node.
4. LR repair::Left rotate the left child, then right rotate the imbalanced node.
5. RL repair::Right rotate the right child, then left rotate the imbalanced node.
6. AVL minimum-node recurrence::$N_h = N_{h-1} + N_{h-2} + 1$.
7. Why store height::To compute local balance factors efficiently during upward fix-up.

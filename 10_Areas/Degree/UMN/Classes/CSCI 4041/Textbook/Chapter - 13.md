---
type: class
input_kind: book
status: sprout
created: 2026-02-23
updated: 2026-04-16
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Elementary Data Structures]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 6|Week - 6]]"
---
# Chapter - 13 Red-Black Trees
## Summary Links
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 6#Chapter 13 and Chapter 18 - Balanced Trees, Rotations, and B-Trees|Week - 6]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 7#Chapter 13 and AVL Project Notes - Red-Black Trees and AVL Validation|Week - 7]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Trees/AVL Trees#Definition|AVL Trees]]
- [[B-Trees#Definition|B-Trees]]

Red-black trees are a variation of [[Chapter - 6 & 12#Chapter - 12 Binary Search Trees|binary search trees]] that are balanced enough to guarantee that basic dynamic-set operations take $O(\lg n)$ time in the worst case.

## 13.1 Properties of Red-Black Trees
A red-black tree is a BST where each node has an extra bit of storage, its **color**, which is either **RED** or **BLACK**. The colors ensure that no simple path from the root to a leaf is more than twice as long as any other.

1. **The 5 Red-Black Properties**
	1. Every node is red or black.
	2. The root is black.
	3. Every leaf (`NIL`) is black.
	4. If a node is red, then both its children are black.
	5. For each node, all simple paths from that node to descendant leaves contain the same number of black nodes.

2. **Sentinels and `T.nil`**
	- The textbook uses a single black sentinel object `T.nil` for every `NIL` pointer.
	- This simplifies code because the root's parent and all external leaves point to the same black node.

3. **Black-Height**
	- The black-height `bh(x)` of node x is the number of black nodes on any simple path from x down to a leaf, not counting x itself.

> [!NOTE] **Lemma 13.1:** A red-black tree with n internal nodes has height at most $2 \lg(n+1)$.

### Lecture Emphasis
The lecture used red-black trees mainly to motivate why balanced trees matter and why rotations are the fundamental repair tool. The full CLRS fix-up cases are important, but for this course the larger structural insight is that red-black trees enforce logarithmic height indirectly through coloring invariants rather than through an explicit stored balance factor.

## 13.2 Rotations
Rotations are local operations that change the pointer structure while preserving the BST property.

### `LEFT-ROTATE(T, x)`
```python
y = x.right
x.right = y.left
if y.left != T.nil:
    y.left.p = x
y.p = x.p
if x.p == T.nil:
    T.root = y
elif x == x.p.left:
    x.p.left = y
else:
    x.p.right = y
y.left = x
x.p = y
```

### `RIGHT-ROTATE(T, y)`
This is the exact mirror image of left rotation.

### Lecture Emphasis: `balancedtree` Scaffold
The lecture notebooks used Chapter 13 as the bridge from ordinary BSTs to AVL trees.

- `balancedtree` inherits `binarysearchtree`
- the node class adds a `height` field
- `compute_height(x)` returns `(left_height, right_height)`
- `update_height(x)` stores `x.height = max(L, R)`
- rotations are reused exactly as the local pointer-repair operation

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

The lecture visualization printed three lines per node:
- key
- stored height
- `(L, R)` from `compute_height`

That makes `(2, 0)` a visual sign of AVL imbalance because the balance factor is `L - R = 2`.

## 13.3 Insertion
Insertion into a red-black tree has three phases:
1. Insert the node as in an ordinary BST.
2. Color the new node red.
3. Run `RB-INSERT-FIXUP`.

### Fix-up Cases
- **Case 1:** uncle is red -> recolor and move up.
- **Case 2:** uncle is black and current node is on the "inside" -> rotate to convert to Case 3.
- **Case 3:** uncle is black and current node is on the "outside" -> recolor and rotate.

### Lecture Emphasis
The course used the red-black insertion cases mostly as contrast against AVL trees. Red-black trees may allow more structural looseness, but they need less strict local balancing information. AVL trees are stricter and therefore often shorter, while red-black trees often do less rebalancing work on updates.

## 13.4 Deletion
Deletion is more complex because removing a black node can violate multiple red-black properties at once.

### Extra Black Concept
The textbook repairs deletion by imagining that the replacement node temporarily carries an **extra black**.
- If the node was red, it becomes red-and-black.
- If it was black, it becomes doubly black.

`RB-DELETE-FIXUP` then moves or removes that extra black until the tree becomes valid again.

### Fix-up Cases (x is a left child)
- **Case 1:** sibling is red
- **Case 2:** sibling is black and both sibling children are black
- **Case 3:** sibling is black, sibling's left child red, sibling's right child black
- **Case 4:** sibling is black and sibling's right child red

The "x is a right child" cases are symmetric.

## AVL Notes Anchored to Chapter 13
Although AVL trees are not the chapter's main textbook structure, the lecture used this chapter's rotation machinery to build the AVL implementation.

### AVL Balance Property
- `bf(x) = left_height - right_height`
- AVL requires `|bf(x)| <= 1`

### Four AVL Imbalance Cases
| Case | Condition | Fix |
| --- | --- | --- |
| LL | `bf(x) == 2` and `bf(x.left) >= 0` | `right_rotate(x)` |
| RR | `bf(x) == -2` and `bf(x.right) <= 0` | `left_rotate(x)` |
| LR | `bf(x) == 2` and `bf(x.left) < 0` | `left_rotate(x.left)` then `right_rotate(x)` |
| RL | `bf(x) == -2` and `bf(x.right) > 0` | `right_rotate(x.right)` then `left_rotate(x)` |

### Trigger Sequences from the Project Notebook
- LL -> `[30, 20, 10]`
- RR -> `[10, 20, 30]`
- LR -> `[30, 10, 20]`
- RL -> `[10, 30, 20]`

### Original 1962 AVL Paper
The lecture and project notes linked the modern implementation back to Adel'son-Vel'skii and Landis:
- "admissible tree" means each node's left and right branch lengths differ by at most 1
- minimum-node recurrence: $N_n = N_{n-1} + N_{n-2} + 1$
- solving the recurrence gives a logarithmic height bound
- original terminology stores branch-state information rather than today's direct "balance factor" vocabulary

That is the reason AVL search, insert, and delete are all logarithmic in the worst case.

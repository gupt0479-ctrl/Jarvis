---
type: class
input_kind: lecture
status: sprout
created: 2026-02-23
updated: 2026-04-16
area:
  - "[[UMN Board]]"
  - "[[CSCI 4041 Board]]"
  - "[[10_UMN/CSCI 4041/CSCI 4041/Concepts/Introduction to Algorithms|Introduction to Algorithms]]"
tags:
  - "#Lecture"
  - "#class"
next:
  - "[[10_Areas/Degree/UMN/Classes/CSCI 4041/Week - 7|Week - 7]]"
---
# Entire Week
## What you must be able to do
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 13#13.2 Rotations|Chapter - 13 rotations]], [[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 13#AVL Notes Anchored to Chapter 13|AVL notes anchored to Chapter 13]], and [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Trees/AVL Trees#Core Ideas (Lecture)|AVL Trees - Core Ideas (Lecture)]]: explain why balance matters, compute balance factors, and identify LL, RR, LR, and RL repair cases.
- [[Chapter - 18#18.1 Definition of B-Trees|Chapter - 18 B-tree definition]], [[Chapter - 18#18.2 Basic Operations|basic operations]], and [[B-Trees#Core Ideas (Lecture + Ch18_B-Tree.ipynb)|B-Trees - Core Ideas (Lecture + Ch18_B-Tree.ipynb)]]: describe B-tree nodes, minimum degree, split strategy, and why large branching factors matter for disk-based structures.
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Trees/AVL Trees#Proof / Reasoning Toolkit|AVL Trees - Proof / Reasoning Toolkit]] and [[B-Trees#Proof / Reasoning Toolkit|B-Trees - Proof / Reasoning Toolkit]]: understand the AVL height-bound recurrence and the B-tree height bound.
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Trees/AVL Trees#Practice Map|AVL Trees - Practice Map]] and [[B-Trees#Practice Map|B-Trees - Practice Map]]: rotations, height-balanced checks, and B-tree tracing are still open practice.

## Key ideas (textbook)
- **Balance is about height control.** A BST can degrade into a linear chain, so the point of balanced trees is not cosmetic symmetry but guaranteed logarithmic search/update paths.
- **Rotations are local structural repairs.** The key property is that they preserve inorder key order while changing shape. Once that is clear, AVL and red-black trees stop looking like completely different families of algorithms.
- **AVL trees use stricter local balance than red-black trees.** The lecture used Chapter 13's rotation machinery to build the AVL interpretation: store height information, compute a balance factor, and rotate when the difference becomes 2.
- **B-trees trade binary branching for page efficiency.** They are balanced search trees designed around secondary storage. Instead of minimizing pointer depth in RAM, they minimize expensive page reads by storing many keys per node.
- **Both structures are best understood by invariants.** AVL maintains a bounded left/right height difference. B-trees maintain key-count bounds per node and equal leaf depth. The actual code is just the machinery for preserving those invariants under updates.

## Concepts created / updated today
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Concepts/Trees/AVL Trees#Definition|AVL Trees]]
- [[B-Trees#Definition|B-Trees]]
- [[10_Areas/Degree/UMN/Classes/CSCI 4041/Textbook/Chapter - 13#AVL Notes Anchored to Chapter 13|Chapter - 13 - AVL notes anchored to Chapter 13]]

## Lecture
### Chapter - 13 Red-Black Trees

**Example**: Drawing a binary search tree for A = [1, 2, 3, 4, 5, 6, 7] results in a *degenerate tree* with maximum height. Another array of random sorted values to make a *balanced/complete tree* gives these values:

- Height = $2^n - 1$

- It starts at height = 0

- All ==paths== have the same length(paths - Search paths from the root to a leaf)

- Path length from the root to leaf, Search cost = $Θ(\log n)$

> [!summary] *Goal*: Insert and Delete maintaining

> - BST Property: $T_{1}.KEY\leq X.KEY\leq T_{2}.KEY\leq Y.KEY\leq T_{3}.KEY$

> - Balance Property

#### AVL Trees (1962)

Left-Right Rotation fixes the Binary search Tree Property.

> **Property**: At any node, the left height and right *height differ* by at most 1.

> When reached at a the violation of the AVL trees: We have to balance the tree and rotate it.

#### AVL Property (1962 — Adel'son-Vel'skii & Landis)

- At every node: $|bf(x)| = |\text{left\_height} - \text{right\_height}| \leq 1$.

- Height bound: $h \leq \frac{3}{2}\log_2(N+1)$ from Fibonacci-based argument in original paper.

- $N_n = N_{n-1} + N_{n-2} + 1$ (min nodes for height-$n$ AVL); solves like Fibonacci → $h = O(\log N)$.

### Chapter 18 - B-Trees

Bayer (1927/4) released B-Trees which are *Multiway Trees*.

Properties of Multiway Trees:

1. All non-root nodes have $n$ *keys* and $n+1$ *children*.

2. **All leaves** are at the *same depth*.

3. All non root nodes have *at least* $t-1$ keys and $t$ children.

4. All non root nodes have *at least* $2t-1$ keys and $2t$ children.

> [!EXAMPLE] Model Parameter(t) = 2

> - Min = 2-1 =1 key per node

>   - Has 2 children

> - Max = 2(2) - 1 = 3 keys

>   - 4 children

> - Gives a (2-3-4)-tree

- Min: $t-1=1$ key, $t=2$ children. Max: $2t-1=3$ keys, $2t=4$ children.

- Search pseudocode: `while node: scan keys; follow correct child pointer`.

- Split: when full node ($2t-1$ keys), median key rises to parent; both halves get $t-1$ keys.

Pseudocode for the Searc(N, node)

```

Search(N, node)

  while node != none:

    scan access control key > N

    node = node.childre[...]    // Moves tree down

```

### Jupyter file explaination

#### Ch13 - BalancedSearchTrees Notebook (helper scaffold)  

- It is a BST subclass that adds:  

- `height` stored in nodes  

- `update_height` while walking upward  

- `left_rotate` / `right_rotate`

- visualization that prints extra info per node  

> [!NOTE] This notebook still isn’t a full AVL by itself.  

> It maintains heights and gives you rotations, but your AVL version must also *detect imbalance* and *choose which rotation case to apply*.  

#### The “helper class” pattern (how Ch13 builds on Ch12)  

- `balancedtree` **inherits** from the BST class (so you don’t rewrite search/min/max/transplant structure).  

- It overrides:  

- node definition (adds `height`)  

- `insert` (calls BST insert, then updates heights on the path upward)  

- `delete` (does BST delete structure, then updates heights upward)  

This is the same approach you’ll use for AVL:  

- keep the base BST work  

- add a rebalance pass after updates  

#### Height helpers (what the visualization is actually showing)  

##### `compute_height(x)`  

- Returns **two numbers**:

    - `left_height = 1 + x.left.height` if left child exists else `0`

    - `right_height = 1 + x.right.height` if right child exists else `0`

- So it returns `(left_height, right_height)`

> [!IMPORTANT] That `(L, R)` display is not the balance factor yet.

> - For AVL, you typically compute: `bf(x) = L - R`  

##### `update_height(x)`  

- Sets `x.height = max(L, R)`  

- This is the value stored in the node and printed on the second line of each circle.  

- Sets: `x.height = max(left_height, right_height)`

- Returns `(left_height, right_height)` again (so it can be shown in the graph)

**Mental model**

- `height` is stored _at the node_

- `(left_height, right_height)` is a snapshot derived from children

#### Rotations (the part you said feels confusing)  

##### Rotation goal (one sentence)  

A rotation rewires a **constant number of pointers** so in-order order stays the same, but the shape becomes better balanced.

##### Left rotation: `left_rotate(x)`  

**When you even can do it**  

- `x.right` must exist (call it `y`).  

**Before**  

- `x` is above `y`, and `y` is the right child.  

**After**  

- `y` becomes the new root of that local subtree  

- `x` becomes `y.left`  

- `y.left` (old) moves over to become `x.right`  

**Pointer checklist (what you should verify in your head)**  

- Parent link from above subtree now points to `y` (or root becomes `y`)  

- `y.p` becomes the old `x.p`  

- `x.p` becomes `y`  

- The “moved subtree” also gets its parent pointer fixed  

##### Right rotation: `right_rotate(x)` (mirror)  

- Same idea, swapped left/right.  

> [!NOTE] If rotations feel slippery, your best move is to track only 3 things:  

> 1) who becomes subtree root  

> 2) which “middle subtree” gets moved across  

> 3) which parent pointers must be repaired  

#### Rotations (Ch13_BalancedSearchTrees.ipynb)

**Left-rotate on $x$** (requires `x.right = y`):

```

y = x.right

x.right = y.left          # "middle subtree" moves to x

if y.left: y.left.p = x

y.p = x.p                 # wire y into x's parent

[update x.p's child pointer to y]

y.left = x; x.p = y

```

**3-thing checklist**: (1) new subtree root = $y$; (2) middle subtree `y.left` → `x.right`; (3) repair `y.p`, `x.p`, moved subtree's `p`.

**4 imbalance cases**:

  

| Case | Shape | Fix |

|---|---|---|

| LL | inserted left-left | right_rotate($x$) |

| RR | inserted right-right | left_rotate($x$) |

| LR | inserted left-right | left_rotate($x$.left) then right_rotate($x$) |

| RL | inserted right-left | right_rotate($x$.right) then left_rotate($x$) |

#### Height Tracking (balancedtree scaffold)

- `compute_height(x)` returns `(left_height, right_height)`.

- `update_height(x)`: `x.height = max(left_height, right_height)`.

- `(L, R)` display = NOT balance factor. $bf = L - R$. AVL violation when $|bf| = 2$.

> [!NOTE] The `balancedtree` class in Ch13 is a scaffold — it inherits BST and adds `height` + rotations. Your AVL must add: imbalance detection + rotation dispatch after insert/delete.

#### Ch18_B-Tree.ipynb

- `btree` class: `keys` list, `children` list, `leaf` bool, `n` count.

- Insert: pre-split full nodes on descent → always room when leaf reached.

- Traversal for sorted output: visit children[i] then keys[i] in alternation.

- By-hand testing from CLRS Figure 18.3 used to verify correctness.
### Chapter 13 and Chapter 18 - Balanced Trees, Rotations, and B-Trees
This week is where "tree" stops meaning just a BST and starts meaning "a family of data structures with different balancing strategies." The lecture's first move was to remind us why any of this is necessary: an ordinary BST built from sorted input can become a chain, which means all operations degrade to linear time. Balanced trees exist to stop that degeneration. Chapter 13 gives the rotation mechanics through red-black trees, but the lecture used those mechanics immediately for AVL-style reasoning. That made the week feel less like "learn two unrelated tree types" and more like "learn one local repair tool and see how different invariants use it."

The `balancedtree` scaffold was the key lecture bridge. It extends the BST code by adding stored height information and rotation helpers. `compute_height(x)` returns the heights of the left and right sides, and `update_height(x)` stores the larger one as the node's height. Once those are available, AVL imbalance becomes a local numeric condition rather than something vague about the tree looking tilted. The `(L, R)` display in the visualization notebook was especially useful because it made a case like `(2, 0)` immediately recognizable as an AVL violation. The four cases LL, RR, LR, and RL are just the four ways the path into the heavy subtree can bend.

The B-tree half of the week changed the setting entirely. Instead of worrying about pointer depth in RAM, the lecture framed B-trees around disk I/O. If one node corresponds to one page, then reading a page full of many keys is cheap compared with descending many levels of a binary tree and paying multiple page reads. That is why B-tree nodes hold many keys and why their branching factor is high. The insert logic also feels different for the same reason: you split full nodes on the way down so the recursive descent never gets stuck at a full child. The Bayer and McCreight paper added historical language like catenation and underflow, but the modern invariant is easier to remember: keep all leaves at the same depth and keep every non-root node within the allowed key-count range.

### Jupyter Notebook Explanations
#### Ch13_BalancedSearchTrees.ipynb
This notebook is the lecture's main AVL scaffold even though the chapter itself is about red-black trees.

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

These functions matter because they separate "what are the subtree heights right now?" from "what value should be stored at this node?" The notebook's visualization uses both. That is why it can show the raw `(L, R)` values and also the stored height field.

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

This left-rotation code is the shared repair primitive behind both red-black and AVL-style balancing. The lecture kept the mental checklist simple:
1. who becomes the new local root
2. which middle subtree moves across
3. which parent pointers must be repaired

#### Ch18_B-Tree.ipynb
This notebook gave the course's concrete B-tree class.

```python
def traverse(node):
    for i in range(node.n):
        if not node.leaf:
            traverse(node.children[i])
        print(node.keys[i])
    if not node.leaf:
        traverse(node.children[node.n])
```

The traversal code is useful because it proves the structure is still a search tree, not just a page-oriented container. The notebook also followed the textbook insert strategy of pre-splitting full nodes on descent, which is the central algorithmic idea to remember.

## Examples worth keeping
- **AVL LL case:** `[30, 20, 10]` triggers a right rotation at 30.
- **AVL LR case:** `[30, 10, 20]` needs a left rotation on 10 and then a right rotation on 30.
- **B-tree minimum degree example:** with `t = 2`, every non-root node has 1 to 3 keys and 2 to 4 children, giving a 2-3-4 tree.
- **Visualization cue:** `(L, R) = (2, 0)` means balance factor 2 and therefore an AVL violation.
- **B-tree height intuition:** a huge page size can make a tree with billions of keys only a few levels tall.

## Takeaways (questions to resolve)
- [ ] Why does AVL use explicit height information while red-black trees use color?
- [ ] How do you decide between LL/RR and LR/RL when the heavy side is known?
- [ ] Why is pre-splitting full nodes the cleanest way to implement B-tree insert?
- [ ] What is the real meaning of B-tree minimum degree t?
- [ ] Why does the original AVL height recurrence look Fibonacci-like?

## Flashcards
#cards/CSCI4041
1. AVL balance property::At every node, `|left_height - right_height| <= 1`.
2. LL repair::Right rotation at the imbalanced node.
3. LR repair::Left rotation on the left child, then right rotation on the imbalanced node.
4. Why do B-trees exist::To reduce expensive secondary-storage page accesses.
5. B-tree minimum degree meaning::It sets the minimum and maximum keys/children allowed in each node.
6. Root split in a B-tree::The only event that increases the tree height.
7. What does `(L, R)` show in the AVL scaffold::The current left and right subtree heights used to compute balance.

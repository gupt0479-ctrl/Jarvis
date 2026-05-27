---
type: concept
course: CSCI 4041
status: evergreen
mastery (1/10): 4
created: 2026-02-25
updated: 2026-04-16
topics:
  - "[[DSA]]"
  - "[[CSCI 4041 Board]]"
  - "[[Chapter - 18]]"
related:
  - "[[AVL Trees]]"
  - "[[Elementary Data Structures]]"
  - "[[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]]"
---
# [[B-Trees]]
## MOC
- [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6#Jupyter Notebook Explanations|Week - 6]]
- [[Chapter - 18#18.1 Definition of B-Trees|Chapter - 18 - Definition of B-Trees]]
- [[Chapter - 18#18.3 Deletion|Chapter - 18 - Deletion]]
- [[AVL Trees#Complexity + Tradeoffs|AVL Trees - Complexity + Tradeoffs]]

## Definition
- **B-tree** is a balanced multiway search tree designed for secondary storage.
- **Minimum degree t** controls how many keys and children each node may contain.
- **All leaves are at the same depth**, so the structure is height-balanced.
- **Main design goal** is to minimize expensive page accesses by keeping height very small.

## Core Ideas (Textbook)
### Secondary-Storage Motivation
- Disk and page access dominate cost when the structure does not fit in RAM.
- A B-tree node is intended to match a disk page.
- High branching factor reduces height dramatically.
- The right complexity measure is often "number of page reads" rather than CPU instructions.

### Node Constraints
- Every non-root node has between `t - 1` and `2t - 1` keys.
- Every internal non-root node has between `t` and `2t` children.
- The root is allowed to be smaller.
- A full node has exactly `2t - 1` keys.

### Search / Insert / Delete
- Search scans keys in the current node, then follows one child interval.
- Insert is top-down and pre-splits full nodes.
- Delete ensures the next child on the descent path is safe before recursing into it.
- Root split is the only way height increases.

## Core Ideas (Lecture + Ch18_B-Tree.ipynb)
### Python Node Shape
- `keys` list
- `children` list
- `leaf` boolean
- `n` current key count
- tree-level parameter `t`

This is the lecture's concrete equivalent of the textbook record fields.

### Inorder-Style Traversal
```python
def traverse(node):
    for i in range(node.n):
        if not node.leaf:
            traverse(node.children[i])
        print(node.keys[i])
    if not node.leaf:
        traverse(node.children[node.n])
```

This code is worth studying because it makes the search-tree ordering visible. Each child lives between two adjacent keys.

### Insert Strategy
- if the root is full, split it before descending
- before descending into a child, split that child if it is full
- this guarantees that insertion always reaches a non-full leaf

The lecture emphasized that this is the opposite feel of BST insertion. The structure is proactively repaired on the way down.

### Bayer and McCreight Notes
- designed for indexed files on disk
- guaranteed at least 50% page utilization
- operations are logarithmic in base k, the effective branching factor
- catenation = merge
- underflow = redistribution case
- height grows only when the root splits

## Professor Code From Lecture
### Ch18_B-Tree.ipynb — Full `Btree` Implementation
The professor's complete B-tree class from [[50_Archive/Previous Classes/CSCI/CSCI 4041/Week - 6|Week - 6]] (`Lectures/Week - 6/Ch18_B-Tree.ipynb`). This is a direct Python translation of the CLRS Chapter 18 pseudocode.

```python
class Btree:
    """A B-Tree implementation based on chapter 18 of CLRS"""
    
    ####################################################################################
    class node:
        """a nested node class for Btree objects based on page 502 of CLRS-chapter 18"""

        def __init__(self,n=0,keys=[],children=[],leaf=True):
            """constructor for Btree nodes"""
            self.n = n        # number of keys
            self.key = keys  # sorted list of n keys
            self.c = children # list of n+1 child links
            self.leaf = leaf  # boolean for leaves
    ####################################################################################
    
    def __init__(self,t=2):
        """constructor for Btree python objects -see B-TREE-CREATE(T) on page 506"""
        self.root = self.node(n=0,keys=[],children=[],leaf=True)            # create an initial empty node
        self.t = t # B-tree parameter
    
    def search(self,x,k):
        """multi-way search algorithm based on page 505 of CLRS-chapter 18"""
        i = 0
        while i < x.n and k > x.key[i]:    # walk forward through keys / links
            i = i + 1
        if i < x.n and k == x.key[i]:      # success
            return x,i
        elif x.leaf:
            return None                    # failure
        else:
            return self.search(x.c[i],k)        # move down the tree (recursively)

    def split(self,x,i):
        """this is B-TREE-SPLIT-CHILD(x,i) from page 506 in CLRS-chapter 18
        
            splits y (which is child i of node x) into siblings y and z 
                where y.key    <    y.key[self.t-1] = key    <    z.key
        """
        y = x.c[i]         # this is the node that is chopped up
        
        z = self.node()    # this is new
        z.leaf = y.leaf
        z.n = self.t - 1   # z should be the last self.t - 1
        z.key = y.key[self.t:]
        if not y.leaf:                     # check for children
            z.c = y.c[self.t:]             # split the children
        
        key = y.key[self.t-1]     # this key is moved up below
        
        y.key = y.key[:self.t-1]  # extract the first t-1 keys
        y.n = self.t - 1        # this is the first self.t - 1
        y.c = y.c[:self.t]      # extract the first t children
        
        # insert new node z into x's child links
        x.c.insert(i+1,z)
        
        # push middle key up to (the parent) x in position i
        x.key.insert(i,key)
        x.n = x.n + 1
    
    def insert(self,k):
        """this is B-TREE-INSERT(T,k) from page 508 in CLRS-chapter 18"""
        r = self.root
        if r.n == 2*self.t - 1:       # check for max size
            s = self.split_root()     # split root
            self.insert_nonfull(s,k)  # insert into new root
        else:
            self.insert_nonfull(r,k)  # insert at root
    
    def split_root(self):
        """this is B-TREE-SPLIT-ROOT(T) from page 509 in CLRS-chapter 18"""
        s = self.node(n=0,keys=[],children=[self.root],leaf=False)         # create a node
        self.root = s         # set as the root
        self.split(s,0)       # split the child
        return s
    
    def insert_nonfull(self,x,k):
        """this is B-TREE-INSERT-NONFULL(x,k) from page 511 in CLRS-chapter 18"""
        i = x.n - 1#-------------# the minus one is for 0-index
        
        if x.leaf:
            #----------------------------------- insert at leaf ----------------------
            while i >= 0 and k < x.key[i]: # find the insert location
                 i = i - 1
            x.key.insert(i+1,k)            # insert
            x.n = x.n + 1
        else:
            #----------------------------- move down the tree-------------------------
            while i >= 0 and k < x.key[i]:
                i = i - 1
            i = i + 1
            if x.c[i].n == 2*self.t - 1:         # check for split on the way down (top-down)
                self.split(x,i)
                if k > x.key[i]:                 # check branch for change (after split)
                    i = i + 1
            self.insert_nonfull(x.c[i],k)        # move down the tree to child link i
```

#### Method-by-Method Breakdown
- **Node structure** (`class node`): Each node stores `n` (key count), `key` (sorted list of keys), `c` (list of child links), and `leaf` (boolean). This maps directly to the CLRS textbook fields on page 502. The professor uses a nested class so every node belongs to a specific `Btree` instance.
- **Constructor** (`__init__` on `Btree`): Creates an empty root node with `t=2` by default (making it a 2-3-4 tree). This corresponds to `B-TREE-CREATE(T)` on page 506. The tree stores its minimum degree `t` as an instance variable.
- **Search** (`search(x, k)`): Multi-way search walks forward through keys in the current node to find the correct child interval, then recurses. Returns `(node, index)` on success or `None` on failure. Time: $O(\log_t n)$.
- **Split** (`split(x, i)`): Splits child `i` of node `x` when it is full (`2t-1` keys). The middle key (`y.key[t-1]`) moves up to the parent. The left half stays in the original child `y`, the right half goes to a new sibling `z`. This is the core structural repair operation — it keeps nodes within the legal size range.
- **Insert** (`insert(k)`): Top-down insertion. If the root is full, split it first via `split_root` (the only way height increases). Then call `insert_nonfull`. This guarantees we never descend into a full node.
- **split_root**: Creates a new empty node, makes the old root its only child, then splits that child. The new node becomes the tree's root. This is the only operation that increases tree height.
- **insert_nonfull** (`insert_nonfull(x, k)`): If at a leaf, find the correct position and insert directly. If at an internal node, find the correct child, split it if full, then recurse. The `i = x.n - 1` adjustment is for 0-indexing — the professor's comment marks this explicitly.
- The professor emphasized that B-tree insertion is "top-down" — the tree is proactively repaired on the way down, unlike BST insertion which inserts first and repairs afterward. This means every node we visit is guaranteed to have room for a new key if needed.

## Proof / Reasoning Toolkit
### Height-Bound Checklist
1. Start with the sparsest legal B-tree.
2. Count how many nodes must appear at each depth.
3. Convert node count to key count.
4. Solve for h to get the logarithmic height bound.

### Insert-Reasoning Checklist
1. Never descend into a full node.
2. If a child is full, split it first.
3. Continue only after the child interval is safe.
4. Use "root split is the only height increase" as a sanity check.

### Delete-Reasoning Checklist
1. Decide whether the target key is in the current node.
2. If not, make sure the target child has enough keys before descending.
3. Borrow if a sibling has spare keys.
4. Merge only when necessary.

## Complexity + Tradeoffs
| Operation | Disk Accesses | Main Reason |
| --- | --- | --- |
| Search | $O(\log_t n)$ | very small height |
| Insert | $O(\log_t n)$ | one descent with occasional splits |
| Delete | $O(\log_t n)$ | one descent with borrow/merge repairs |

Compared with balanced binary trees, B-trees use more work per node but far fewer levels.

## Canonical Examples (Max 5)
### 1. t = 2 Special Case
- Each non-root node has 1 to 3 keys.
- Each internal non-root node has 2 to 4 children.
- This is the familiar 2-3-4 tree case.

### 2. Root Split
- Root is full.
- Create a new root.
- Split the old root into two children.
- Height increases by exactly 1.

### 3. Search Interval Logic
- Compare the target against the ordered keys in one node.
- Descend into the unique child interval that can still contain it.
- Same search-tree idea as BST, just with many keys per node.

### 4. Merge / Catenation
- Two minimum-size siblings plus a separator key are combined into one node.
- This may force a repair upward if the parent loses too many keys.

### 5. Height Intuition
- Large page size means huge branching factor.
- Huge branching factor means tiny height.
- Tiny height means very few disk reads.

## Practice Map
- Trace B-tree insertion by hand
- Trace B-tree deletion borrow/merge cases by hand
- Compare B-tree and AVL search paths conceptually
- Explain why databases like high branching factors
- Reconstruct a B-tree from a sequence of insertions for small t
- [[Multiway Search Tree Project|Midterm Project - Multiway Search Tree]]: B-tree / multiway search tree implementation option

## Mini-test
1. Why is minimum degree t the most important B-tree parameter?
2. Why is pre-splitting full children so helpful during insertion?
3. What is the only event that increases B-tree height?
4. Why do B-trees outperform balanced binary trees on secondary storage?
5. What is catenation in the original paper's terminology?

## Flashcards
#cards/CSCI4041
1. B-tree leaf-depth property::All leaves are at the same depth.
2. Non-root key range::Between `t - 1` and `2t - 1` keys.
3. When does B-tree height increase::Only when the root splits.
4. Why do B-trees reduce disk I/O::They store many keys per node, reducing height.
5. What is a full node::A node with exactly `2t - 1` keys.
6. Insert invariant::Never descend into a full node.
7. Catenation meaning::Merge two siblings together with the separator key from the parent.

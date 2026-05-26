---
type: class
input_kind: project
status: seed
created: 2026-02-22
updated: 2026-03-30
area:
  - "[[CSCI 4041 Board]]"
  - "[[DSA]]"
  - "[[Introduction to Algorithms]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 7|Week - 7]]"
---
# AVL Trees
## Overview
**What this project is asking you to build (your part = implementation)**  
- You’re taking the professor’s Week 5 BST notebook (`Ch12_BinarySearchTree.ipynb`) and the Week 6 “balanced tree helper” notebook (`Ch13_BalancedSearchTrees.ipynb`) and turning them into a real **AVL tree** implementation.  
- AVL = BST ordering **plus** a strict height-balance rule: for every node, the left and right subtree heights differ by at most 1.
**Where each notebook fits**  
- **Ch12** is your “pointer correctness + delete structure” reference:  
- parent pointers (`p`)  
- BST insert search path + attach leaf  
- `transplant(u, v)` helper  
- BST delete (0/1 child vs 2 children using successor)  
- **Ch13** is your “AVL building blocks” reference:  
- node `height`  
- `update_height` while walking upward using `p`  
- left/right rotations  
- visualization that prints key + height + a height-tuple
## Plan
- [ ] Implement AVL **insert** and **delete** (modified from BST so balance is preserved). 
- [ ] Keep code style consistent with the professor’s template notebooks.  
- [ ] Keep invariants correct:
	1. **BST property** always holds.  
	2. **AVL balance** always holds: `|height(left) - height(right)| ≤ 1`.
	3. **Parent pointers** (`p`) always correct after every pointer rewrite (insert, transplant, delete, rotations).
## Work log
1. Multi way Trees use the file in the lecture 10: Ch18 B-Trees. 
	- The Data algorithms have given another way to solve the multi way trees, can use this as well. But stick to the file given by the professor.
## Concepts used
- [[Concept - BST invariant (ordering)]]  
- [[Concept - Parent pointers (p)]]  
- [[Concept - Inorder traversal ⇒ sorted output]]  
- [[Concept - Successor (min of right subtree)]]  
- [[Concept - Transplant]]  
- [[Concept - Height + Balance factor]]  
- [[Concept - Rotations (left/right)]]  
- [[Concept - AVL cases (LL/RR/LR/RL)]]
## Implementation
AVL is a BST **plus** a height-balance rule:
### Core invariants you must preserve
1. **BST property** (from your Ch. 12 notes): ===left subtree keys ≤ node.key ≤ right subtree keys===.
2. **AVL balance property**: for every node, `|height(left) - height(right)| ≤ 1`.
### What changes vs normal BST insert/delete
- **BST insert/delete** still does the structural change (same search path logic).
- Then you walk back up the path and **update heights** and **rebalance** using rotations.
### Rotations (the shared “language” with CLRS Ch. 13)
CLRS doesn’t teach AVL directly in Ch. 13, but it gives the exact rotation mechanics used by balanced BSTs. Your notes already highlight rotations as the key local pointer rewrite that preserves inorder order.
- Left rotation: (what pointers change in our code)  
- Right rotation: (what pointers change in our code)
### You’ll use the 4 classic AVL cases
- **LL** (left-left): single right rotation
- **RR** (right-right): single left rotation
- **LR** (left-right): left rotation on child, then right rotation
- **RL** (right-left): right rotation on child, then left rotation
#### Test sequences  
- Insert LL: [...]  
- Insert RR: [...]  
- Insert LR: [...]  
- Insert RL: [...]  
- Delete rebalance: [...]
## Using this [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 5#Jupyter file explaination|BST file]] to implement AVL for the project
AVL insert/delete is: **BST insert/delete + rebalance**. What stays the same from this file:
- The basic BST search path logic for insert and delete
- The transplant helper idea (or a similar pointer-replace helper)
- The inorder-sorted correctness check (inorder traversal should always be sorted)
What AVL adds on top:
1. **Extra field on each node**: `height` (or equivalent)
2. **After insert**
	- Start from the inserted node’s parent (`p`)
	- Move upward using `p`:
	    - update heights
	    - compute balance factor
	    - if unbalanced: rotate (LL / RR / LR / RL)
3. **After delete**
	- Start from the first affected parent (often the parent of the node that got physically removed / moved)
	- Move upward using `p`:
		- update heights
		- rebalance as needed (can cascade upward)
> [!NOTE] Why your `p` pointer matters even more in AVL:
> - AVL fixing happens “on the way back up”.
> - Without `p`, you’d need extra recursion or an explicit stack to find ancestors.
## How to convert Ch13 scaffold into *your* AVL implementation (the missing piece)  
You’ll add:  
1. Define **AVL balance factor**: `balance_factor(x) = left_height - right_height`  
2. An upward rebalance loop:  
	- starting at the affected node, repeat:  
	- update height  
	- check `bf`  
	- if `bf` is 2 or -2, choose one of the 4 cases:  
		- **LL** → right rotate  
		- **RR** → left rotate  
		- **LR** → left rotate on child, then right rotate  
		- **RL** → right rotate on child, then left rotate
	Make sure heights are correct **after every rotation** (your scaffold already updates two nodes; AVL may need continued upward updates).

## Post-submit reflection
- What failed first?
- What pattern repeats?
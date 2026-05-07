---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-02-25
topics:
  - "[[OCaml]]"
  - "[[10_Areas/Degree/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2|Chapter - 1 & 2]]"
  - "[[UMN Board]]"
  - "[[CSCI 2041 Board]]"
related:
  - "[[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]"
---
# OCaml - BST Problems
## MOC
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2|Chapter - 1 & 2]]
- [[OCaml - Types of Programming|OCaml - Types of Programming]]
- [[OCaml - Pattern Matching|OCaml - Pattern Matching]]
## Definition
A **Binary Search Tree (BST)** is a binary tree with an ordering invariant:
- all keys in left subtree < node key
- all keys in right subtree > node key
> [!NOTE] Course emphasis: BST functions should be explainable using: recursion + pattern matching + persistence.
## Resources
- [[10_UMN/CSCI 2041/Textbook/Chapter - 1 & 2#1.4 Code Example: [[OCaml - BST Problems#BST Insert|BST Insert]]|Chapter 1.4 BST Insert]]
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]
- [[OCaml - Pattern Matching|Pattern matching]]
### How to use them
1. For every BST function: write base case + recursive case first.
2. State the invariant you’re preserving (ordering) before you explain the code.
## Week 1: Persistent BST Insert (lecture code)
### Links
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2|Chapter - 1 & 2]] → see the BST insert explanation block
- [[OCaml - Types of Programming#Persistence (the “copy as little as possible” model)|Persistence]]
- [[OCaml - Pattern Matching#Canonical forms|Pattern matching forms]]
### Problem: insert a key into a BST **without modifying the original**
**Goal:** `bst_insert tree key` returns a new tree.
**What the professor cares about**
- You must use recursion (no loops).
- You must use `match` to split empty vs node.
- You must keep persistence: copy only the path you traverse.
### BST Insert (from your Chapter 1 & 2 note)
```ocaml
let rec bst_insert tree key =
  let rec inserting subtree =
    match subtree with
    | BSTempty -> BSTnode (key, BSTempty, BSTempty)
    | BSTnode (other_key, left, right) ->
        if key < other_key then
          BSTnode (other_key, inserting left, right)
        else if key > other_key then
          BSTnode (other_key, left, inserting right)
        else subtree
  in inserting tree
```
### Explanation (midterm-ready)
- **Base case**: `BSTempty` → create the new node (the insertion point).
- **Recursive case**: `BSTnode (...)`
    - choose left vs right based on comparisons
    - rebuild the node you are standing on, but only change one child
    - the untouched subtree is reused “as-is” (sharing pointers)
> [!INFO] Why this is persistent? Only nodes on the search path are reconstructed. Everything else is reused.
### Quick complexity reasoning (what to say on an exam)
- copies exactly the path from root to insertion point
- number of copied nodes is proportional to height `h`
- balanced: `h = O(log n)`; worst-case skewed: `h = O(n)`
## Week 2: BST follow-ups (placeholder until more lecture/lab problems are added)
### Links
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 2|Week - 2]]
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4|Chapter - 3 & 4]] (for scoping + pattern matching patterns used in tree code)
### Problems to add here (when you upload them)
-  `bst_mem` / membership search
-  `bst_min` / `bst_max`
-  traversal functions (inorder/preorder)
-  “structural sharing” diagram questions (what gets copied?)
> [!NOTE] When you add a new BST problem. Put it under the week it appeared, and include: goal, base/recursive cases, invariant.
## Canonical “BST problem patterns” (use for any new BST function)
### Shape recursion (structural recursion)
Always begin with: 
```ocaml
match tree with
| BSTempty -> ...
| BSTnode (k, left, right) -> ...
```
### Invariant sentence (say this first)
- “Assume left subtree keys are smaller and right subtree keys are larger.”
- “My recursive step preserves this by only inserting into the correct side.”
### Persistence sentence (say this second)
- “I rebuild only the nodes along the path; untouched subtrees are reused.”
## Common mistakes
- Treating constructors like functions (trying to use them as values).
- Forgetting the base case (`BSTempty`) or making it do recursion.
- Violating the BST invariant (inserting into the wrong side).
- Accidentally writing a version that mutates (not persistent).
## Mini-test (answer without looking)
- [ ] In `bst_insert`, which nodes get copied and why?
- [ ] What is the base case and what does it represent?
- [ ] How would your time complexity change if the tree is skewed?
- [ ] Where does pattern matching show up in BST code?
## Flashcards (best 3–8)
#cards/CSCI2041
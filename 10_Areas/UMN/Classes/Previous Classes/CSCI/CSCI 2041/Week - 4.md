---
type: class
input_kind: lecture
status: seed
created:
updated:
area:
  - "[[UMN Board]]"
tags:
next: []
---
# Entire Week
## What you must be able to do
- 
## Key ideas (textbook)
- 
## Concepts created today
- [[Chapter - 9 & 10|Textbook Chapter - 9]]
- [[Concept - ...]]
## Examples worth keeping
- 
## Lecture
### Lecture (Feb 9) 
- BSTs in OCaml (Lab 3): review BST property, `type 'key bst`, `bstIsIn`, `bstInsert`, persistence + “copy as little as possible”  
#### BSTs (Binary Search Trees) - what the professor is assuming you already know 
- A BST is a structure that **maps keys to values**.  
	- In lecture examples, we often **omit the value slot** to focus on the key + structure.  
- Average-case idea (for “*reasonable*” trees):  
	- search / insert take about **O(log n)** for **n keys**  
- Worst-case idea (*degenerate/skewed* tree):  
	- can degrade to **O(n)**  
- Node mental model (professor sketch: “4 slots”):  
	- key  
	- (optional) value  
	- left subtree pointer  
	- right subtree pointer  
- *BST property* (strict ordering, keys appear at most once):  
	- left subtree keys **<** node key  
	- right subtree keys **>** node key  
	- each key appears **at most once**  
	- for keys `k1`, `k2`, **exactly one** is true: `k1 < k2` OR `k1 = k2` OR `k1 > k2`  
- OCaml ordering note: the professor says OCaml objects of the *same type* are “*totally ordered,*” so you can use (almost) anything as keys (within a consistent type).  
#### Persistent + immutable BSTs (why this is a big deal in OCaml)  
- The tree is **immutable**: you do not modify the original.  
- The data structure is **persistent**:  
	- operations return a new tree 
	- the old tree still exists and can still be used 
	- Efficiency principle the professor repeats:  
- **copy part of an existing BST as little as possible** specifically: copy only the nodes on the path you traverse; reuse untouched subtrees  
1. **Empty subtrees**: 
	- ==OCaml has no “general null pointer”==  
	- Imperative languages often use null pointers to represent empty subtrees.  
	- OCaml has no general null pointer.  
		- professor notes (C.A.R. Hoare / “billion dollar mistake” reference)  
	- Instead: represent emptiness with a constructor (like `BstEmpty`).  
#### BST type in OCaml (parameterized type)  
**Code from lecture**  
```ocaml  
type 'key bst =  
  | BstEmpty  
  | BstNode of 'key * 'key bst * 'key bst  
;;
```
- The type defines constructors you can use in code:
    - `BstEmpty`
    - `BstNode (key, left, right)`
#### `bstIsIn` (membership test) — tail recursive
- Purpose: check if a key appears in a BST.
- Signature the professor writes:
    - `'a -> 'a bst -> bool`
    - key → tree → boolean result
- Structure:
    - internal helper that takes a subtree, pattern match on subtree:
        - *base case*: empty subtree → `false`
        - *node case*: compare search key vs node key:
            - if smaller: recurse left
            - if larger: recurse right
            - else: equal → `true`
- Why it can be tail recursive:
    - each recursive call is the chronologically last step in its branch (no extra work afterward)
**Code from lecture**
```ocaml
let bstIsIn key tree =  
  let rec isInning subtree =  
    match subtree with  
    | BstEmpty -> false  
    | BstNode (otherKey, leftSubtree, rightSubtree) ->  
        if key < otherKey then isInning leftSubtree  
        else if key > otherKey then isInning rightSubtree  
        else true  
  in isInning tree   (* tail call *) 
;;
```
#### `bstInsert` (persistent insert) — not tail recursive
- Purpose: return a BST “like the original” but with `key` added (if missing).
- Critical constraint:
    - you cannot modify the original tree
    - you must return a **partial copy** with the key added
- *Base case*: inserting into an empty subtree → create a new node:
    - `BstNode (key, BstEmpty, BstEmpty)`
- *Recursive case*:
    - if $key < otherKey$: rebuild the current node with a new left child (result of recursive insert)
        - reuse the right subtree as-is
    - if $key > otherKey$:
        - rebuild the current node with a new right child
        - reuse the left subtree as-is
    - else: key already exists → return subtree unchanged
- Why it is *not* tail recursive:
    - after the recursive call returns, you still must build a `BstNode(...)`
    - the recursive call is not the chronologically last action
**Code from lecture**
```ocaml
let bstInsert tree key =  
  let rec inserting subtree =  
    match subtree with  
    | BstEmpty -> BstNode (key, BstEmpty, BstEmpty)  
    | BstNode (otherKey, leftSubtree, rightSubtree) ->  
        if key < otherKey 
        then BstNode (otherKey, inserting leftSubtree, rightSubtree)  (* recursive case *)  
        else if key > otherKey 
        then BstNode (otherKey, leftSubtree, inserting rightSubtree)  (* recursive case *)
        else subtree       (* Base case *)
  in inserting tree  ;;
(* Type: 'key bst -> 'key -> 'key bst *)
```
#### Complexity + stack frames (professor’s comfort argument)
- Balanced-ish tree:
    - about **O(log n)** comparisons / time
    - about **O(log n)** stack frames (because recursion depth ≈ height)
- Worst case:
    - **O(n)** time and **O(n)** stack frames
- Professor attitude:
    - “this doesn’t happen often”
    - and the next lecture will show visually how insert does not copy the entire tree
Links to connect:
- [[OCaml - BST Problems]]
- [[OCaml - Types of Programming#Persistence (the “copy as little as possible” model)|Persistence]]
- [[OCaml - Pattern Matching#Pattern matching on user-defined constructors (BST / tautology style)|Constructor matching]]
- [[OCaml - Basics#Tail recursion and stack frames (Jan 30 lecture)|Tail recursion test]]
### Lecture (Feb 11)
- Finish BST insert example (structural sharing + GC), then environments + closures + static binding, operators as functions
#### Finish BST: worked example of `bstInsert t 103`
- Professor uses the concrete tree from the board (keys like 100, 70, 53, 137, 102, 140).
- Insert 103:
    1. start at root `100`
        - `103 > 100` → go right
        - you will rebuild a new node for 100 in the returned tree (because one of its children changes)
        - left subtree pointer (the 70 side) can be reused unchanged
    2. at `137`
        - `103 < 137` → go left
        - rebuild a new node for 137
        - reuse right subtree pointer (the 140 side) unchanged
    3. at `102`
        - `103 > 102` → go right
        - rebuild a new node for 102
        - reuse left subtree pointer unchanged
    4. hit empty subtree
        - create new leaf `BstNode (103, BstEmpty, BstEmpty)`
- Visual takeaway the professor marks:
    - **the copy path is highlighted** (red in your notes)
    - everything not on the path is shared
> [!NOTE] This is the persistence story for trees: “Only the search path nodes are new; untouched subtrees are reused.”
#### “Is this efficient?” (professor answers his own question)
- Time: about **O(log n)** for n keys (when tree height is log-ish)
- Space: you temporarily allocate new nodes on the path
- If you don’t need the old tree:
    - it can become unreachable and be garbage collected
    - so space can be okay over time
1. *Shadowing example (`let t = ...` twice)*:
	- Professor writes a pattern like:
	    - `let t = <some tree>;;`
	    - `let t = bstInsert t 103;;`
	- Meaning:
	    - there are now two “t” names in the story:
	        - the second `t` shadows the first
	    - if no other names point to the old tree, GC can reclaim it
#### Transition: environments + closures + curried functions (why we need this next)
- The course now needs a precise model of:
    - how functions remember names defined outside them
    - how “defined vs called” matters (static binding)
    - why higher-order functions behave consistently
#### Environments + bindings (professor’s definitions)
- **Binding**: a name is bound to a value (example: `b` bound to 1).
- **Environment**: an internal data structure recording bindings of names.
    - the environment contains lots of bindings (including operators like `+`).
1. The plusB / mystery example (*static binding proof*)
```ocaml
let b = 1;;  
let plusB a = a + b;;  
  
let mystery a =  
	let b = 2 in plusB a;;  
	mystery 10;;  (* professor: result is 11 *)
```
- Key question the professor asks: “*Which `b` does `plusB` use?*”
- Answer:
    - `plusB` uses the `b` from where `plusB` was defined (`b = 1`)
    - not the `b` from where `plusB` is called (`b = 2` inside `mystery`)
- Name for this rule:
    - **static binding** (aka lexical binding)
- Dynamic binding contrast (professor mentions):
    - if `plusB` used `b = 2` from the call site, that would be dynamic binding
    - he notes some Lisps historically had variants of this
#### Closures (how static binding works internally) - 3 parts
- Functions are represented as **closures**:
    1. **parameters**
    2. **body** (not evaluated yet)
    3. **environment pointer** (the environment that existed when the function was defined)
- The professor draws a “closure box” and a “cloud” environment.
#### Function call model (professor step list)
When you do `plusB 10`:
1. start from `plusB`’s **defining environment**
2. create a new environment (based on it)
3. bind parameter `a` to 10 in that new environment
4. evaluate the body `a + b` using:
    - `a = 10`
    - `b = 1` (from defining environment)
5. return the value and restore the previous environment context
#### Operators are functions (`(+)`, `(*)`) and punctuation issues
- If `o` is an operator, then `(o)` is the name of the function that implements it.
    - `2 + 2` is like `(+) 2 2`
- Multiplication:
    - its function name is `(*)`
    - but `(* ... *)` is also comment syntax
    - so spacing and parentheses matter when you write multiplication-as-a-function
Links to connect:
- [[OCaml - Let bindings, Scope & Closures]]
- [[OCaml - Types of Programming]] (first-class functions motivation)
- [[OCaml - Basics#Operators you must not confuse|`=` vs `==` and operator functions]]
- [[OCaml - BST Problems]] (persistent copying example)
### Lecture (Feb 13)
- Higher-order functions: `map`, anonymous functions (`fun`), `filter`, `reduce` (right-reduce), tail recursion analysis, predicates
#### Higher-order functions (course definition)
- Functions that take other functions as arguments (today’s focus).
- Professor lists classic examples:
    - `map`
    - `filter`
    - `reduce`
- Why this works:
    - functions are first-class objects
    - closures preserve the needed environment info
#### `map` (copy a list while applying a change)
- Meaning written by professor:
    - `map f [e0; e1; ...; e(n-1)]` produces `[f e0; f e1; ...; f e(n-1)]`
- Interpretation:
    - “copy a list while making changes as you go”
- Example:
    - `map add1 [2; 3; 5; 1]` ⇒ `[3; 4; 6; 2]`
- Tail recursion note:
    - professor marks it as **not tail recursive**
    - reason: you do `(func head) :: (mapping tail)`
        - the cons `::` happens after the recursive call returns
- Parentheses note (professor emphasis):
    - parentheses can be needed so the code parses the way you intend
    - particularly around function application inside `::`
**Code used (lecture)**
```ocaml
let map func objects =  
  let rec mapping objects =  
    match objects with  
    | [] -> []  
    | head :: tail -> (func head) :: (mapping tail)  
  in mapping objects  
;;  
(* type: ('a -> 'b) -> 'a list -> 'b list *)
```
#### Anonymous functions `fun ... -> ...`
- Professor’s motivation:
    - you don’t name the number `1` before using it
    - so why name a helper function used only once?
- Definition on board:
    - `fun p1 p2 ... pn -> e`
    - parameter names can be patterns (ties back to “pattern matching everywhere”)
- Example:
    - anonymous version of add1:
        - `fun number -> number + 1`
- Example usage:
    - `map (fun number -> number + 1) [2; 3; 5; 1]`
**Code used (lecture)**
```ocaml
map (fun number -> number + 1) [2; 3; 5; 1];;
```
#### `filter` (keep elements that satisfy a predicate)
- Predicate definition (professor words):
    - “one argument, returns bool”
    - type: `'a -> bool`
- Meaning written:
    - `filter p [e0; e1; ...; e(n-1)]` returns a list like the original,  
        except only those `ei` remain where `p ei` is true
- Style warning (professor calls it out hard):
    - don’t write `pred head = true`
    - write `if pred head then ...`
- Tail recursion analysis (professor’s “yes & no”)
    - if you keep the head:
        - `head :: (filtering tail)` → not tail
    - if you drop the head:
        - `filtering tail` → tail call
    - so the definition contains both tail and non-tail paths
- Professor joke scribble about redundant boolean comparisons:
    - `(((b = true) = true) = true) = true ...` (don’t do this)
**Code used (lecture)**
```ocaml
let filter pred objects =  
  let rec filtering objects =  
    match objects with  
    | [] -> []  
    | head :: tail ->  
        if pred head  
        then head :: (filtering tail)  
        else filtering tail  
  in  
  filtering objects  
;;  
(* type: ('a -> bool) -> 'a list -> 'a list *)
```
**Example used (lecture)**: `filter (fun number -> number mod 2 = 0) [1; 2; 3; 4; 5; 6];;  
* => [2; 4; 6] *`
#### `reduce` (right-reduce / right fold idea)
- Professor writes a defining shape:
    - reduces a list to a single value using a function `f`
- Default/base value:
    - `reduce f [] e` ⇒ `e`
    - professor literally points at the `e` asking “what’s this?” → it is the default object
- Nesting shape for non-empty lists:
    - `reduce f [e0; e1; ...; e(n-1)] e`
    - becomes `f e0 (f e1 (... (f e(n-1) e)...))`
    - professor labels this as a right-nesting behavior
- Tail recursion note:
    - professor marks **not tail recursive**
    - because `func head (reducing tail)` must wait for `reducing tail` to return
**Code used (lecture)**
```ocaml
let reduce func objects defaultObject =  
  let rec reducing objects =  
    match objects with  
    | [] -> defaultObject  
    | head :: tail -> func head (reducing tail)  
  in  
  reducing objects  
;;  
(* type: ('a -> 'b -> 'b) -> 'a list -> 'b -> 'b *)
```
**Examples used (lecture)**
```ocaml
reduce (+) [1; 2; 3] 0;;     (* => 6 *)  
reduce ( * ) [1; 2; 3] 1;;   (* => 6 *)
```
#### Meta takeaway (what the professor wants you to internalize)
- `map`, `filter`, `reduce` are templates:
    - you supply “the missing piece” as a function argument
- They express “copy a list” and “combine a list” patterns once,  
    instead of rewriting recursion for every new task.
- Tail recursion vs not-tail recursion:
    - list-building with `::` usually makes the recursion non-tail
    - dropping elements can be tail in that branch
    - right-nesting reduce is not tail
Links to connect:
- [[OCaml - Basics#Functions and function types|Function types + parentheses for higher-order args]]
- [[OCaml - Let bindings, Scope & Closures|Closures as the reason higher-order functions work]]
- [[OCaml - Pattern Matching#Pattern matching on lists (most common)|List patterns `[]` and `h :: t`]]
- [[OCaml - Types of Programming|First-class functions + applicative style]]
## Midterm Questions
### Chapter 6
- [ ] **Constructor Syntax:** In the definition `type color = red | Blue`, one constructor is legal and one is not. Which one is invalid and why?.
- [ ] **Null Pointers:** Explain how OCaml's `'a option` type provides a safer alternative to the "null" values found in languages like C or Java.
- [ ] **Polymorphic Variants:** What is the primary difference between a "closed" variant type `[< ... ]` and an "open" variant type `[> ... ]`?.
## Takeaways (questions to resolve)
- [ ] Why does ...?
- [ ] What changes if ...?
## Flashcards
#cards/
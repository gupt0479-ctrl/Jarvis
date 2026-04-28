---
type: class
input_kind: book
status: sprout
created: 2026-02-25
updated: 2026-02-26
area:
  - "[[UMN Board]]"
  - "[[CSCI 2041 Board]]"
  - "[[OCaml]]"
  - "[[Midterm]]"
  - "[[OCaml - BST Problems]]"
  - "[[OCaml - Basics]]"
  - "[[OCaml - Pattern Matching]]"
  - "[[OCaml - Types of Programming]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[50_Archive/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]"
---
# Chapter 1 - Introduction to OCaml
This chapter introduces OCaml as a member of the ML (Meta-Language) family, originally designed for the Logic of Computable Functions (LCF) theorem prover. It establishes the foundational philosophy of **functional programming** and sets the stage for how it differs from the imperative style found in languages like C or Java.
## 1.1 Core Principles of OCaml
According to the textbook, OCaml is defined by several key features:
- [[OCaml - Types of Programming#Applicative / functional programming (OCaml default in this course)|Functional programming]] (Applicative): Functions are treated as **first-class values**. They can be nested, passed as arguments, and stored in data structures.
- **Strongly Typed:** The type of every variable and expression is determined at compile-time. Programs that pass the type checker are **safe**, meaning they will never produce illegal instructions or memory faults.
- **[[Type inference]]:** Even though OCaml is strongly typed, the programmer rarely has to annotate code with type constraints; the compiler "infers" them.
- [[OCaml - Polymorphism|Polymorphism]]: You can write generic programs that work for any type, such as a list that can hold integers, strings, or even other lists.
- [[OCaml - Pattern Matching|Pattern matching]]: A mechanism that unifies case analysis and data destruction.
- **[[Module system]]:** Allows data structures to be specified and defined abstractly using features like functors.
- **[[Object system]]:** OCaml includes a system for inheritance and re-use, complementing the module system.
- **Separate Compilation:** Includes a byte-code compiler (for portability) and a native-code compiler (for efficiency).
- **Formal Semantics:** Programs have a mathematical interpretation, making them easier to explain and understand.
> [!INFO] **First-Class Value** A value that can be passed as an argument, returned from a function, and stored in a data structure. The professor likens this to **"First-class citizens"** who have all the rights of a society, such as the right to vote, marry, or own property.
## 1.2 Functional vs. Imperative Programming
The textbook highlights the contrast between these two paradigms using Euclid's algorithm for the **Greatest Common Divisor (GCD)**.
### [[OCaml - Types of Programming#Imperative programming (what the professor expects you to recognize)|Imperative programming]]
- **Mechanism:** Relies on **loops** (e.g., `while` loops) and **side-effects**.
- **State:** Progress is made by modifying the **program state** via assignment statements (e.g., `a = b`).
- **Reasoning:** Requires tracking loop invariants and showing how the state changes toward a goal.
### [[OCaml - Types of Programming#Applicative / functional programming (OCaml default in this course)|Functional programming]]
- **Mechanism:** Relies on [[OCaml - Types of Programming#Recursion in functional/applicative programming|Recursion]].
- **State:** There are typically no side-effects or permanent assignments in pure functional code.
- [[OCaml - Types of Programming|Persistence]]: Data structures are never destroyed. When you "change" a structure, you actually create a new one while the original remains accessible.
- **Intermediate approach (ML/OCaml):** Mostly functional, but assignment and other side-effects exist (often used when interacting with the outside world, e.g., I/O).  
- **Why not “pure functional only”:** In fully pure code, you may have to pass every updatable structure to every function ("threading the state"), which can become awkward when there are many such structures.  
- **Course alignment:** Default to functional style; use imperative features only when they genuinely simplify an otherwise messy state-threading design.
## 1.3 Professor’s Lecture Analogies
To help visualize these abstract concepts, the professor uses several recurring analogies:
- **The Snake:** Used to describe the structure of a *list*. The **head** is the tongue/front, and the **tail** is everything else behind it. It is a linear chain of nodes.
- **Clouds and Boxes (Pointers):** Used to explain how persistent data structures work in *memory*. A *list or tree is a "box"* that ==points== to a *"cloud" containing the value* and more pointers. The key is that multiple structures can share the same pointers.
- **The Dispatcher:** Used to describe [[OCaml - Types of Programming#“Mix-match logic” (how the course expects you to use both styles)|Match–with]] logic. Like a 911 dispatcher, the code looks at the "emergency" (the incoming data type) and decides which "unit" (the code branch) to send to handle it.
## 1.4 Code Example: [[OCaml - BST Problems#Week 1 Persistent BST Insert (lecture code)|BST Insert]]
_Relating Chapter 1's concepts (Recursion and Persistence) to Lecture Code._ The textbook notes that in OCaml, we use **recursion** where an imperative language would use a loop. Below is the `bst_insert` function from the lectures, which adds a key to a Binary Search Tree without modifying the original. When inserting into a BST:  
1. Start at the root. Decide whether to go left or right.  
2. Copy the current node as you traverse.  
3. Once you hit the insertion spot, create a new node.  
4. Rebuild the path back up by connecting the copied nodes.  
This results in a new tree where only the path to the inserted node is new. Everything else (subtrees) is reused.
#### Efficiency Insight  
Suppose you insert into a BST of height **O(log n)**:  
- Only the nodes along the path from root to insertion point must be copied.  
- The rest of the tree is shared.
So insertion copies O(log n) nodes, not the entire tree.  
### Another professor analogy - **Persistent Tree**:  
Each tree node points to a cloud. Every insertion only rebuilds the path down, reusing entire untouched subtrees.  
1. **Root**: Copy the root node.
2. **Branch**: Decide whether to go left or right depending on the key.
3. **Copy** each node along the path.
4. **Insert** a new node where the recursion bottoms out.
5. **Re-use** the untouched subtree pointers rather than copying them.  
	Example: Insert into a BST:
	- Insert 10, then 5, then 15, then 12.
	- When inserting 12, only nodes 10 and 15 are copied; the 5 subtree is simply re-used by pointer.
6. **Efficiency**: Because we only copy the "path" down the tree, we only copy O(logn) nodes, keeping the rest of the original tree's "Clouds" (subtrees) intact.
```ocaml
let rec bst_insert tree key =
  let rec inserting subtree =
    match subtree with
    | BSTempty -> BSTnode (key, BSTempty, BSTempty) (* Base case: Ch 1 recursion *)
    | BSTnode (other_key, left, right) ->
        if key < other_key then
          BSTnode (other_key, inserting left, right) (* Create new node: Persistence *)
        else if key > other_key then
          BSTnode (other_key, left, inserting right) (* Copy path only *)
        else subtree (* Key exists, return original *)
  in inserting tree
```
Line-by-Line Explanation:
1. **let rec**: Declares a *recursive function*, the functional alternative to a loop mentioned in Section 1.1 of the text.
2. **match subtree with**: Uses [[OCaml - Pattern Matching#`match ... with`|Pattern matching]] to "discriminate" between an empty tree and a node.
3. **BSTempty -> ...**: The *base case*. Instead of a "null pointer" (the "billion-dollar mistake"), OCaml uses an explicit constructor.
4. **BSTnode (other_key, inserting left, right)**: This demonstrates [[OCaml - Types of Programming#Persistence (the “copy as little as possible” model)|Persistence]]. We do not change the old `left` subtree. Instead, we create a **new node** that points to a newly created left subtree, while the `right` subtree is simply re-used by pointer.
5. **Efficiency**: Because we only copy the "path" down the tree, we only copy O(logn) nodes, keeping the rest of the original tree's "Clouds" (subtrees) intact.
# Chapter 2 - Simple Expressions
This chapter moves from the high-level philosophy of OCaml into the literal "words" and "punctuation" of the language. It focuses on the **toploop** (interactive evaluator) and the **primitive data types** that form the foundation of all OCaml programs.
## 2.1 Comment Convention and Interaction
- OCaml uses `(* ... *)` for comments.  
- Each expression entered ends with `;;`, signaling OCaml to evaluate.  
	Example: `#2 + 2;;` = `: int = 4`
- **The Toploop:** The interactive system (invoked via `ocaml`) prints a `#` prompt, reads an expression terminated by `;;`, and returns the evaluated **value** and its **type**.
    - _Professor's Note:_ The `;;` is an "end of input" signal for the toploop.
## 2.2 Primitive Data Types
OCaml is **strongly typed**; every expression has exactly one type, and types cannot be implicitly coerced (e.g., you cannot add an `int` to a `float` without explicit conversion).
- unit: Contains a single value `()`. Used for expressions with side-effects.  
- int: Machine integers.  
- float: Floating-point numbers.  
- bool: Booleans (`true`, `false`).  
- char: Single characters.  
- string: Strings.
### 2.2.1 [[OCaml - Basics#unit|unit]]: The Singleton Type
The simplest type, containing only one element: `()`. It corresponds to `void` in C and is used for functions that compute via **side-effects** rather than returning a mathematical value.
- **Note:** In OCaml, even an assignment returns a value (the trivial value `()` of type `unit`). This is why the language is expression-based rather than having “pure commands.”
### 2.2.2 [[OCaml - Basics#int|int]]: Integers
Signed integers represented by a machine word minus one bit (reserved for the garbage collector).
- **Radixes:** Supports decimal, octal (`0o`), binary (`0b`), and hexadecimal (`0x`).
- **Operators:** Includes standard arithmetic (`+`, `-`, `*`, `/`, `mod`) and bitwise operations (`lnot`, `lsl`, `lsr`, `asl`, `asr`, `land`, `lor`, `lxor`).
### 2.2.3 [[OCaml - Basics#float|float]]: Floating-Point Numbers
Requires a decimal point or an exponent (`e` or `E`).
- **Operators:** Must include a dot: `+.`, `-.`, `*.`, `/.`.
- **Conversion:** Use `int_of_float` and `float_of_int`.
### 2.2.4 [[OCaml - Basics#char|char]]: Characters
ASCII characters enclosed in single quotes, e.g., `'a'`. Supports escape sequences like `\n` (newline) or `\ddd` (decimal code).
- **Functions:** `Char.code` (char to int) and `Char.chr` (int to char).
### 2.2.5 [[OCaml - Basics#string|string]]: Character Strings
Fixed-length sequences delimited by double quotes `"`. They are **not** null-terminated arrays.
- **Concatenation:** Uses the `^` operator.
- **Access/Update:** `s.[i]` to read and `s.[i] <- c` to update (this returns `unit`).
### 2.2.6 [[OCaml - Basics#bool|bool]]: Boolean Values
The values `true` and `false`.
- **Logic:** `not` (negation), `&&` (conjunction), and `||` (disjunction).
- **Short-Circuiting:** `&&` and `||` are "short-circuit": the second clause is only evaluated if the first cannot determine the result.
## 2.3 Relations and Conditionals
OCaml provides several relations $=, <>, <, >, <=, >=, ==$ (physical identity), and $!=$ (physical non-identity).
- [[OCaml - Basics#`if ... then ... else ...`|if–then–else]]: The standard conditional. Both branches must return the same type. If the else is omitted, it is treated as returning `unit`.
## 2.4 The Type System and Safety
OCaml is **safe**, meaning a valid program will never produce an invalid machine operation or memory fault.
- **Evaluation results:** An expression either results in a **value**, raises an **exception**, fails to terminate, or exits.
## 2.5 Professor’s Lecture Analogies
- **The Punctuation Mania:** The professor notes that OCaml "loves punctuation marks," using symbols like `->` (the arrow) to define function types and = for name bindings.
- **The Boxes:** When discussing [[primitive data types]], the professor often visualizes them as **"Boxes"** in memory that hold specific types of data.
- **The Pointer Rule:** In OCaml, "almost everything... is a pointer" (an address in memory), which allows for efficient handling of complex types.
## 2.6 Code Example: [[OCaml - Tautology Problems|Tautology Checker]] (Evaluate)
_Relating Chapter 2 (Bools and Operators) to Lecture Code._
The `evaluate` function from the lectures relies heavily on the **Boolean values** and **short-circuit operators** discussed in Section 2.2.6.
```ocaml
let rec evaluating prop =
  match prop with
  | False -> false                 (* Chapter 2: bool value *)
  | True -> true                   (* Chapter 2: bool value *)
  | Not p -> not (evaluating p)    (* Chapter 2: logical negation *)
  | And (p1, p2) -> (evaluating p1) && (evaluating p2) (* Short-circuit AND *)
  | Or (p1, p2) -> (evaluating p1) || (evaluating p2)  (* Short-circuit OR *)
  | Imply (p1, p2) -> (not (evaluating p1)) || (evaluating p2)
  | Equiv (p1, p2) -> (evaluating p1) = (evaluating p2) (* Chapter 2: relation *)
```
Line-by-Line Explanation:
1. **False -> false**: Maps the custom constructor `False` (uppercase) to the OCaml primitive `false` (lowercase).
2. **Not p -> not ...**: Uses the `not` function defined in the textbook for logical negation.
3. **And -> ... && ...**: Uses the short-circuiting conjunction. If `evaluating p1` is false, `evaluating p2` is never called.
4. **Imply -> ...**: Implements the logical identity A⟹B≡¬A∨B using the Chapter 2 primitive `||`.
5. **Equiv -> ... = ...**: Uses the equality relation = to check if both Booleans are the same.
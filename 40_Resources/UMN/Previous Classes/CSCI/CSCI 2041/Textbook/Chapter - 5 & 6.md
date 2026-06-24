---
type: class
input_kind: book
status: sprout
created: 2026-02-19
updated: 2026-02-27
area:
  - "[[UMN Board]]"
tags:
  - "#class"
  - "#Textbook"
next: week
---
# Chapter 5 - Tuples, Lists, and Polymorphism
This chapter explores how OCaml organizes and composes data in structured ways, moving beyond simple primitive types to aggregate data structures and the powerful concept of generic programming.
## 5.1 [[OCaml - Polymorphism|Polymorphism]] (Parametric)
OCaml uses **parametric polymorphism**, meaning types and expressions can be parameterized by **type variables**.
- **Type Variables:** Represented by a leading single quote (e.g., `'a`, pronounced "alpha"). They act as placeholders for any type.
- **The Pointer Rule:** The professor explains that polymorphism works because "almost everything in OCaml is a pointer" (a memory address). Because pointers are a uniform size, a function can handle a list of any type by simply passing around these addresses.
- **Type Constraints:** If the compiler infers a type that is too general, you can restrict it using the syntax `(expression : type)`.
### 5.1.1 Value Restriction and Eta-expansion
This is a critical "safety" feature. An expression is only truly polymorphic if it is an **immutable value**.
- **Weak Polymorphism:** If you apply a polymorphic function to another polymorphic function (e.g., `let id' = identity identity`), OCaml assigns it a type like `'_a`. This underscore means it is "waiting" to be assigned a type; once it is used as an `int`, it can **never** be used as a `string` again.
- **Why?** This prevents type errors in the presence of mutable state (like reference cells).
- **[[Eta-expansion]]:** You can bypass this restriction by wrapping the expression in an anonymous function: `(fun x -> identity identity x)`.
### 5.1.2 Other Kinds of Polymorphism
- **Overloading:** OCaml **does not** provide overloading (ad-hoc polymorphism), largely because it makes type inference difficult and programs harder to understand.
- **Subtype Polymorphism:** Fully supported in the object system (Chapter 14).
> [!INFO] **The Pointer Rule** The professor emphasizes that in OCaml, "almost everything... is a pointer" (a memory address). This allows polymorphic functions to handle data of any size because they are simply passing around pointers.
## 5.2 [[OCaml - Tuples|Tuples]]
Tuples are the simplest aggregate data type, representing ordered collections of values of arbitrary types.
- **Syntax:** Expressions are separated by commas (e.g., `1, "Hello"`).
- **Type Syntax:** Uses the `*` symbol to separate component types (e.g., `int * string`).
- **Deconstruction:** Tuples are "taken apart" using pattern matching in `let` bindings or function parameters.
- **Functions:** The built-in functions `fst` and `snd` extract the first and second elements of a pair, respectively.
- **Simultaneous Assignment:** Tuples allow for swapping values without a temporary variable: `let x, y = y, x`.
## 5.3 [[OCaml - Lists|Lists]]
A list is a sequence of values that must all have the **same type**.
- **Constructors:**
    - `[]`: The empty list (nil).
    - `::`: The **cons** operator, which adds a new element to the front of a list.
- **Syntax Shorthand:** `[e1; e2; e3]` is syntactic sugar for `e1 :: e2 :: e3 :: []`.
- **Types:** The type of a list of integers is `int list`.
- **[[Association list]]:** Lists of pairs (tuples) used to represent key-value relationships.
[!INFO] **The Snake Analogy** The professor describes a list as a **Snake**. The **head** (`hd`) is the tongue/front, and the **tail** (`tl`) is everything behind the head.
## 5.4 [[Tail recursions|Tail Recursion]] Masterclass
Recursion is the primary way to express iteration in functional programming.
- **Definition:** A function is **tail recursive** if the recursive call is the very last thing the function does.
- **Optimization:** The compiler can reuse the current **stack frame** for a tail call, making it as efficient as an imperative loop.
- **Accumulators:** A common technique to achieve tail recursion is using an extra parameter to "accumulate" the result as you go.
- **Lists:** Tail recursion is vital for lists because non-tail-recursive functions will crash on long lists by exceeding the maximum stack size.
## Code Example: `append` (Concatenation)
_Relating Chapter 5 (Lists and Persistence) to Lecture 2 Code._
The professor uses the `append` function (equivalent to the `@` operator) to demonstrate list construction and **Persistence**.
```ocaml
let rec append l1 l2 = 
  match l1 with
  | [] -> l2                          (* Base Case: Ch 5.3 Nil *)
  | h :: t -> h :: (append t l2)      (* Recursive Case: Ch 5.3 Cons *)
```
Line-by-Line Explanation:
1. **let rec**: Declares a recursive function, the functional alternative to a loop.
2. **match l1 with**: Uses **[[Match–with]]** to analyze the structure of the list.
3. **[] -> l2**: If the first list is empty, return the second list.
4. **h :: t -> ...**: Uses **Pattern Matching** to extract the head (`h`) and tail (`t`) of the first list.
5. **h :: (append t l2)**: This is **NOT tail-recursive**. The last thing the function does is a `cons` (`::`) operation, not the recursive call.
6. **[[Persistence]]**: This code never changes `l1` or `l2`. It creates a **new list** by copying `l1` and pointing the end of the copy to `l2`.
# Chapter 6 - Unions
According to the textbook, **[[disjoint unions]]** (also called tagged unions, variant records, or **algebraic data types**) represent the union of several different types where each part is given a unique, explicit name. They are fundamental to the OCaml type system because they allow for sophisticated data representation beyond basic scalars.
## 6.1 Formal Definitions and Syntax
*Exact Union Types*: An exact union type is defined by a set of cases separated by the vertical bar `|` character. Each case has a **[[type constructors|constructor]]** name that **must be capitalized**.
- **Syntax:** `type typename = | Identifier1 of type1 | Identifier2 of type2 ...`.
- **Values:** Values are formed by applying a constructor to an expression of the appropriate type (e.g., `Integer 1`).
- **[[Pattern matching]]:** Patterns use the constructor name to deconstruct the value and perform case analysis.
## 6.1 Binary Trees
A binary tree is an acyclic graph where each node has zero or two children. In OCaml, this is represented as a recursive union type: `type 'a tree = Node of 'a * 'a tree * 'a tree | Leaf`. The textbook notes that while constructors take arguments like functions, they are **not functions** and cannot be used as values themselves.
## 6.2 & 6.3 Unbalanced and Ordered Binary Trees
- **Unbalanced:** Elements are added as new nodes without regard for tree symmetry.
- **Ordered (BST):** Maintains the **[[binary search tree]]** property where for any node `Node (x, left, right)`, all labels in `left` are smaller than `x` and all labels in `right` are larger than `x`.
- **Performance:** Membership testing in an ordered tree is O(l) where l is depth, but worst-case (increasing order insertion) remains O(n).
## 6.4 Balanced Red-Black Trees
To guarantee O(logn) performance, OCaml programs often use Red-Black trees which enforce four invariants regarding node coloring (Red/Black) to ensure the longest path is at most twice the shortest path.
## 6.5 Open Union Types ([[Polymorphic variants]])
Unlike exact unions, **open union types** (prefixed with a back-quote `` ` ``) allow subsequent definitions to add more cases.
- **Syntax:** Enclosed in `[> ... ]` for open types or `[< ... ]` for closed types.
- **Definitions:** Defining a type with polymorphic variants requires an explicit type variable (e.g., `type 'a number = [> 'Integer of int] as 'a`) because the type must be polymorphic over unspecified cases.
## 6.6 Common Built-in Unions
Several core OCaml types are implemented as unions:
1. **[[bool]]:** Effectively `type bool = true | false` (a special case where constructors are lowercase).
2. **[[OCaml lists|list]]:** Effectively `type 'a list = [] | :: of 'a * 'a list`.
3. **'a option:** Used to represent the presence (`Some of 'a`) or absence (`None`) of a value, replacing the "billion-dollar mistake" of null pointers.
## 6.2 Professor's Lecture Analogies
- **The Dispatcher:** The professor likens **[[match–with]]** on union types to a **911 Dispatcher**. When a piece of data (the emergency) arrives, the dispatcher looks at the "tag" (constructor) and decides which "unit" (code branch) to send to handle it.
- **The Billion-Dollar Mistake:** The professor notes that OCaml has **no general null pointer**. Instead of checking for "null" everywhere, you use union constructors like `BSTempty` or `None`, forcing you to handle the empty case via pattern matching.
- **Boxes and Arrows:** When defining recursive types like `inti-chain`, the professor draws **"Boxes"** with internal slots and **"Arrows"** representing pointers to other nodes.
- **Discriminator:** Unlike C's "undiscriminated" unions (where you must track the type manually), OCaml's unions are **discriminated**, meaning the language itself "discriminates" or tells the difference between cases using the constructor labels.
## 6.3 Code Example: Proposition Representation
_Relating Chapter 6 (Recursive Unions) to Lecture 11._
The professor uses a recursive union to represent logical propositions for a **[[tautology checker]]**.
```
type proposition = 
  | False                          (* Constant case [2] *)
  | True                           (* Constant case [2] *)
  | Var of string                  (* Case with value [2] *)
  | Not of proposition            (* Recursive case [4] *)
  | And of proposition * proposition (* Recursive tuple case [5] *)
  | Imply of proposition * proposition
```
Line-by-Line Explanation:
1. **type proposition =**: Declares a new **[[disjoint union]]**.
2. **| False**: Defines a constructor for the constant False. It must be capitalized.
3. **| Var of string**: Defines a constructor that carries a payload (a string name).
4. **| Not of proposition**: This is a **recursive type definition**; the type `proposition` is mentioned in its own definition to allow for nested expressions like `Not(Not(True))`.
5. **| And of proposition * proposition**: Uses a **tuple type** within the constructor to store two sub-propositions, a common and efficient implementation for binary connectives.
6. **Dispatcher Connection:** To evaluate this, the professor uses a `match` expression to "dispatch" logic based on whether the proposition is an `And`, an `Or`, or a `Var`.
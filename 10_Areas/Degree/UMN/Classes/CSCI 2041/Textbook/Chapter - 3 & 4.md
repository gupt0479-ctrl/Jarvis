---
type: class
input_kind: book
status: sprout
created: 2026-02-11
updated: 2026-02-26
area:
  - "[[UMN Board]]"
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Basics]]"
  - "[[OCaml - Types of Programming]]"
  - "[[OCaml]]"
  - "[[OCaml - Let bindings, Scope & Closures]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 2|Week - 2]]"
---
# Chapter 3 - Variables and Functions
This chapter marks the transition from simple expressions to the structural logic of OCaml. It introduces how names are bound to values, the architecture of functions, and the rules governing the scope and visibility of those names.
## 3.1 [[OCaml - Types of Programming#Applicative / functional programming (OCaml default in this course)|Functional programming]] and Functions
In OCaml, functions are **first-class values**, meaning they can be constructed, passed as arguments, and stored in data structures.
- **Definition:** Functions are defined using the `fun` keyword for **[[anonymous functions]]** or via `let` for named functions.
	- Anonymous: `fun v1 v2 ... vn -> expression`
    - Named (common OCaml sugar): `let identifier v1 v2 ... vn = expression`
- **[[Function types]]:** The arrow `->` denotes a function type. `int -> int` describes a function taking an integer and returning an integer.
- **Application:** Function application is performed by placing the function before its argument (concatenation). Application binds tighter than most operators, so:
    - `increment 2 * 3` means `(increment 2) * 3`
    - `increment (2 * 3)` forces multiplication first.
- **[[Curried functions]]:** OCaml follows "Currying" logic - every function actually takes exactly one argument. Multi-argument functions like `let sum i j = i + j` are actually nested functions of type `int -> (int -> int)`.
- **Partial Application:** You can apply a function to only some of its arguments to return a new function, such as `let incr = sum 1`.
- **Parentheses alternative (textbook):** `begin ... end` is equivalent to parentheses for grouping.
> [!INFO] **First-Class Citizen** The professor compares functions to "First-class citizens" who possess full societal rights, such as voting or owning property. Similarly, functions can be passed around and returned just like any integer or string.
### 3.1.1 [[OCaml - Let bindings, Scope & Closures|Scoping]] and Nested Functions
OCaml uses **static binding** (lexical scoping). The value of a variable is determined by its defining environment, not its calling environment.
- **Shadowing:** If a variable is redefined, the new definition "==shadows==" the old one within its scope, making the previous version inaccessible.
- **Nested Bindings:** Using `let ... in ...` allows variables to be defined locally within a specific expression body.
- **Static binding rule (textbook wording):** the value of a variable is determined by the nearest enclosing `let` definition in the program text, not by where the function is called.
- **Shadowing detail (textbook):** a new definition makes the older one inaccessible inside the new scope, but the old one remains in effect outside that scope.
- **Crucial `let ... in ...` rule (textbook):**
    - In `let x = e1 in e2`, the name `x` is defined only inside `e2`, not inside `e1`.
    - The value of the whole `let` expression is the value of its body (`e2`).
> [!INFO] **The Cloud** The professor uses "Clouds" to represent the **environment**—the internal data structure that tracks name bindings. When a function is created, it captures a "Cloud" (environment) to remember its definitions.
### 3.1.2 [[OCaml - Types of Programming#Tail recursion preview (ties to Jan 30 lecture + your Basics file)|Recursion]] and Recursive Functions
To define a function that calls itself, the `rec` modifier must follow the `let` keyword.
- **[[Recursive functions]]:** Essential for repetition/looping in functional programming.
- **[[Tail recursions]]:** A specific form where the recursive call is the last action of the function, allowing the compiler to optimize stack space.
- **Mutually Recursive Functions:** Multiple functions that call each other are defined together using the `and` keyword.
- **What happens if you forget `rec` (textbook example):**
    - The name is treated as not being in scope inside its own body, producing an “unbound value” error.
- **Mutual recursion (textbook):**
    - Use `let rec f ... = ... and g ... = ...` when the functions call each other.
### 3.1.3 [[OCaml - Let bindings, Scope & Closures|Higher anonymous functions]]
Higher-order functions either take functions as arguments or return them as results.
- **Example:** A numerical derivative function `deriv f` takes a function `f` and returns a new function representing its derivative.
- **Lecture Connection:** This topic was covered extensively in **Lectures 8 and 9**, focusing on how [[function closure|closures]] enable higher-order behavior.
- **Arrow association reminder (textbook):**
	- `int -> int -> int` means `int -> (int -> int)`
	- `(float -> float) -> float -> float` means `(float -> float) -> (float -> float)`.
## 3.2 [[Variable names]] and Operators
- **Naming Rules:** Names can include letters, digits, `'`, and `_`, but must start with a lowercase letter or underscore.
- **Infix Operators:** Standard operators like `+` or `-` can be treated as functions by enclosing them in parentheses, e.g., `(+) 2 3`.
- **Custom Operators:** You can define new infix operators like `( ** )` for power functions.
- **Name character set (textbook):**
    - Can contain letters, digits, `'`, `_`
    - Must start with lowercase letter or `_`
    - A single `_` by itself is not allowed as a variable name.
- **Operators as names (textbook):**
    - Infix symbols like `+ - * /` can be used as identifiers.
    - Prefix form is written with parentheses: `( + )`, `( * )`, etc.
    - `(*)` needs spacing because `(*` starts a comment.
- **New operator precedence (textbook):**
    - The precedence/associativity of a new operator depends on its first character.
> [!INFO] **Punctuation Mania** The professor notes that OCaml is "crazy for punctuation marks," often using them to draw symbols that resemble mathematical logic, like `->` or `( * )`.
## 3.3 [[Labeled parameters]] and Optional Arguments
- **Labels:** Use `~label: pattern` to define parameters that can be passed in any order.
- **[[Optional parameters]]:** Use `?(label = expression)` to define default values if an argument is omitted.
- **Rules of Thumb:** Optional parameters should usually be followed by a non-optional parameter so the compiler can detect when they are omitted.
- **Labeled params (textbook):**
    - Parameter: `~label:pattern`
    - Argument: `~label:expression`
    - If all parameters are labeled, argument order does not matter.
- **Shorthand (textbook):**
    - `let f ~x ~y = ...` is shorthand for `let f ~x:x ~y:y = ...`
    - `f ~x ~y` uses variables named `x` and `y` as the arguments.
- **Optional params (textbook):**
    - `?(x = default)` defines an optional parameter with default.
    - Optional args can be omitted entirely.
- **Rules of thumb (textbook):**
    - An optional parameter should be followed by a non-optional parameter (often unlabeled).
    - For higher-order functions, label/optional intent can be mis-inferred; add explicit type annotations if needed.
## 1.4 Code Example: `plusB` and Scoping
_Relating Chapter 3 (Scoping and Closures) to Lecture 8 Code._
This example from the professor demonstrates the **[[Scoping]]** rules discussed in Section 3.1.1.
```ocaml
let b = 1;; (* Top-level binding *)

let plusB a = a + b;; (* b is captured here as 1 *)

let mystery a = 
  let b = 2 in (* Shadowing b inside this scope *)
  plusB a;;    (* Calling the function *)
```
Line-by-Line Explanation:
1. **let b = 1**: A global name binding for `b` is added to the "Cloud" (environment).
2. **let plusB a = a + b**: A **[[function closure]]** is created. It stores the parameter `a`, the body `a + b`, and a pointer to the current environment where `b = 1`.
3. **let b = 2 in**: This creates a local environment where `b` is 2, **shadowing** the global `b` only for the subsequent expression.
4. **plusB a**: When `plusB` is called (e.g., `mystery 10`), it ignores the `b = 2` in the **calling environment** and uses the `b = 1` from its **defining environment**.
5. **Result**: `mystery 10` returns **11**, proving that OCaml uses static (lexical) binding as defined in the textbook.
# Chapter 4 - Basic Pattern Matching
This chapter explores one of OCaml's most powerful features: **[[Pattern matching]]**. It is a mechanism used to define computation by case analysis, allowing a program to examine data structures and "dispatch" logic based on their specific form.
## 4.1 The `match` Expression
The textbook defines the `match` expression as a way to compare a value against a series of patterns in order.
- **Logic:** The expression to be matched is evaluated first, then compared with patterns (`pattern1`, `pattern2`, etc.) sequentially.
- **Result:** The first pattern that matches the value triggers the evaluation of its corresponding expression, which becomes the result of the entire `match` block.
- **Punctuation:** The first vertical bar `|` is optional, but OCaml programmers often use it to keep the code visually aligned. The professor calls this OCaml's **"Punctuation Mania,"** where the language uses marks like `|` and `->` to draw mathematical logic.
**Exact evaluation order (textbook):**
1. evaluate the matched expression once
2. compare to patterns from top to bottom
3. evaluate the right-hand expression of the first matching arm
> [!INFO] **The Dispatcher** The professor compares `match-with` logic to a **911 Dispatcher**. When a "call" (data) comes in, the dispatcher looks at the "emergency" (the pattern) and decides which unit (the code branch) to send: the police, the fire department, or Batman.
## 4.2 Pattern Types: Constants and Variables
Patterns are built using two primary components:
- **Constants:** A constant pattern (like `0` or `"hello"`) matches values that are exactly equal to it.
- **Variables:** A variable pattern (like `x` or `j`) matches _any_ expression.
- **Binding:** When a variable pattern matches a value, that variable is **bound** to that value within the scope of that specific match arm.
**Critical rule (textbook):** variables in patterns are always _binding occurrences_.
- If you write `zero -> ...`, that `zero` matches anything and binds a new variable named `zero`.
- This can make later cases unreachable and the compiler warns “unused match case”.
> [!WARNING] **Binding Danger** Variables in patterns are _always_ binding occurrences. If you try to match against a pre-defined name (like `let zero = 0`), the pattern matching will treat `zero` as a new variable that matches anything, shadowing your original definition and often leading to "unused match case" warnings.
## 4.3 Functions with Matching (`function`)
Since it is common for a function body to be a single `match` expression, OCaml provides the **function** keyword. **Textbook definition:** `function` is shorthand for `fun x -> match x with ...` where the single argument is the value being matched.
- It acts as a shorthand for `fun x -> match x with ...`.
- It is particularly useful for recursive functions like Fibonacci or list traversals.
## 4.4 Advanced Pattern Expressions
The textbook details three ways to make patterns more expressive:
1. **Choice Patterns (****|****):** You can combine multiple patterns into one if they lead to the same result (e.g., `0 | 1 -> i`).
2. **as** **Identifier:** This matches a value against a pattern and simultaneously binds the whole value to a name (e.g., `(0 | 1) as i -> i`).
3. **when** **Guards:** A pattern can be qualified by a predicate: `pattern when expression`. The match only succeeds if the pattern matches _and_ the `when` expression evaluates to `true`.
- **Choice pattern constraints (textbook):** when combining `p1 | p2`, both sides must bind the same variables with compatible types.
- **`as` precedence note (textbook):** `as` has very low precedence, so parentheses are usually clearer.
## 4.5 Patterns for Primitives and Wildcards
Pattern matching works across all primitive types:
- **Characters/Strings:** You can match specific strings or character ranges like `'A' .. 'Z'`.
- **Wildcard Pattern (__):** A single underscore matches anything but does not bind it to a name.
- **Floating-Point:** While supported, matching against floats is discouraged due to precision issues (e.g., `3.1` might not exactly match a computed float).
## 4.6 Exhaustiveness and Safety
OCaml enforces **Safe Case Analysis**.
- **Incomplete Matches:** If you miss a possible case, the compiler will issue a warning.
- **Runtime Failure:** If an unmatched value occurs at runtime, OCaml raises a `Match_failure` exception.
- **Heed the Warnings:** The professor and textbook both emphasize: **do not ignore compiler warnings** regarding inexhaustive patterns. Use a wildcard `_` to raise an `Invalid_argument` if a case "should be impossible".
- **What happens if you ignore it (textbook):**
    - compiler warns about inexhaustive patterns and even suggests an example not matched
    - at runtime, unmatched values raise `Match_failure`
- **“Don’t ignore warnings” practice (textbook):**
    - add a wildcard arm and raise `Invalid_argument "function_name"` when you believe the missing cases are impossible.
## 4.7 Patterns are Everywhere
Patterns are not restricted to `match` blocks; they appear in all binding mechanisms:
- **let** **bindings:** `let (a, b) = f x` uses a tuple pattern to deconstruct the result.
- **fun** **parameters:** You can put a pattern directly in a function’s parameter list, such as `let head (h :: _) = h`.
- **Unit pattern:** Using `()` in a parameter list allows you to simulate a function with no arguments.
- **General forms (textbook):**
    - `let pattern = expression`
    - `let identifier pattern ... pattern = expression`
    - `fun pattern -> expression`
- **Important limitation (textbook):**
    - Constant patterns as function parameters are usually inexhaustive (except `()`), so they often produce warnings and can crash at runtime.
## 1.4 Code Example: `evaluate` (Tautology Checker)
_Relating Chapter 4 (The Dispatcher) to Lecture 11._
This function uses **[[Pattern matching]]** to evaluate a logical proposition. It acts as the "911 Dispatcher" for the different types of logical connectives.
```ocaml
let rec evaluating prop =
  match prop with
  | False -> false                 (* Constant pattern [3] *)
  | True -> true                   (* Constant pattern [3] *)
  | Var name -> alget pairs name   (* Variable pattern with binding [3, 28] *)
  | Not p -> not (evaluating p)    (* Deconstructing a constructor [28] *)
  | And (p1, p2) -> (evaluating p1) && (evaluating p2) (* Nested pattern [29] *)
  | Or (p1, p2) -> (evaluating p1) || (evaluating p2)
  | Imply (p1, p2) -> (not (evaluating p1)) || (evaluating p2)
```
Line-by-Line Explanation:
1. **match prop with**: Starts the "Dispatcher" logic described in Section 4.1.
2. **False -> false**: A simple constant match. If the data is the `False` constructor, it returns the primitive `false`.
3. **Var name -> ...**: This is a **binding occurrence**. The variable `name` is bound to the string inside the `Var` constructor so it can be passed to `alget`.
4. **Not p -> ...**: This demonstrates how patterns "unify case analysis and data destruction". It identifies the `Not` case and extracts the inner proposition `p`.
5. **And (p1, p2)**: A complex pattern matching an **Ordered Pair** (tuple) inside a constructor. It extracts two separate propositions at once to evaluate them individually.
---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-02-25
topics:
  - "[[CSCI 2041 Board]]"
  - "[[Midterm]]"
  - "[[OCaml]]"
  - "[[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4|Chapter - 3 & 4]]"
related:
  - "[[50_Archive/UMN/Classes/CSCI 2041/Week - 2|Week - 2]]"
---
# Let Bindings, Scope, and Closures
## MOC  
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4#3.1.1 Scoping and nested functions|Textbook: Ch3.1.1 Scoping]]  
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4#1.4 Code Example: plusB and Scoping|Textbook: plusB example]]  
- [[Midterm]]  
- 
## Definition  
- **Binding:** a name refers to a value.  
- **`let x = e1 in e2`:** binds `x` to the value of `e1` **only inside** `e2` (the body). `x` is not in scope inside `e1`.  
- **Static (lexical) binding:** a function uses variable values from where it was defined (nearest enclosing `let` in the program text), not where it is called.  
- **Shadowing:** a newer `let x = ...` hides the older `x` within its scope.  
## Canonical forms  
- Top-level binding:  
- `let x = e;;`  
- Local binding:  
- `let x = e1 in e2`  
- Nested lets:  
- `let x = e1 in let y = e2 in e3`  
“OCaml thinks all functions take one argument” and multi-arg is nested functions. So:
- `let add x y = x + y` really has type `int -> (int -> int)`
- When you apply `add 1`, you get back a function waiting for `y` (partial application).
### `let` vs `let ... in ...` (all “let concepts” you listed)
Your let-binding concept note states the key rule:
- `let x = e1 in e2`: `x` is available only inside `e2`, and the value of the whole expression is the value of `e2`.
Beginner interpretation:
- `e1` is computed first
- bind the name `x` to that value
- then evaluate `e2` _using_ that binding
- outside `e2`, `x` doesn’t exist
Also from Week-2: this is lexical scoping (static binding), and shadowing creates a new binding in a smaller region.
### Recursive functions + tail recursion
Week-2 lecture summary gives the exact definitions:
- recursive function: uses `let rec` and calls itself
- tail recursion: all recursive calls are in the tail (last action)
### Labeled parameters + optional arguments
Your Chapter-3&4 notes define the syntax:
- labeled parameter: `~label:pattern`
- labeled argument: `~label:expression`
- optional parameter: `?(x = default)`
“Which parameter is being labeled?”  
The _function parameter_ is labeled (the name after `~`). That lets callers pass arguments out of order when labels are used.
# anonymous functions
## Definition
- Function values written without naming them first: `fun p1 p2 ... pn -> e`
## Why we use them
- Passing functions as arguments (higher-order functions).
- Quick one-off behavior without creating a named function.
## Common mistake
- Forgetting `->` or thinking it “runs immediately”. It doesn’t; it creates a function value.
# Function types
## Definition
- `t1 -> t2` means: input type `t1`, output type `t2`.
## Right association (midterm trap)
- `t1 -> t2 -> t3` means `t1 -> (t2 -> t3)`.
## Application precedence
- `f x + y` means `(f x) + y`.
# Curried functions
## Definition
- Multi-argument functions are nested single-argument functions.
- Example type: `int -> int -> int` is `int -> (int -> int)`.
## Partial application
- Give fewer args → get a function waiting for the rest.
# Labeled and Optional Arguments
## Labeled parameters
- Parameter form: `~label:pattern`
- Argument form: `~label:expression` :contentReference[oaicite:41]{index=41}
## Optional parameters
- Form: `?(x = default)`
- Can be omitted by caller. :contentReference[oaicite:42]{index=42}
## Why this exists
- Improves readability and call-site clarity.
## Key rules that show up on exams 
- The value of a `let ... in ...` expression is the value of its body.  
- Shadowing does not “overwrite” old values globally; it only creates a new binding in a smaller region.  
- A function closes over (captures) the bindings that are visible at its definition point.  
## Worked example (plusB / mystery) 
Paste your exact example here and keep it as the “static binding proof” for the midterm:  
- `plusB` uses `b` from where `plusB` was defined, not the `b` from inside `mystery`.  
## Common mistakes  
- Thinking `let x = e1 in e2` makes `x` available inside `e1` (it doesn’t).  
- Expecting a function to use a variable value from the call site (that would be dynamic binding; OCaml is static).  
- Confusing “shadowing” with “mutation.”  
## Mini-test (answer without looking)
- [ ] In `let x = 1 in let x = 2 in x`, what does the final `x` refer to?  
- [ ] In `let x = 1 in let y = x in y`, which `x` is used for `y`?  
- [ ] If a function uses a free variable `b`, where does `b` come from?
## Flashcards (best 3–8)

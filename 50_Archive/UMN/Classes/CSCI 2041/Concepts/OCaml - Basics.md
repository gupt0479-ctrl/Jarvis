---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-02-25
topics:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Pattern Matching]]"
  - "[[UMN Board]]"
  - "[[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2|Chapter - 1 & 2]]"
related:
  - "[[50_Archive/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]"
---
# Basics
## MOC
- [[50_Archive/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2|Chapter - 1 & 2]]
- [[OCaml - Types of Programming|OCaml - Types of Programming]]
- [[OCaml - Pattern Matching|OCaml - Pattern Matching]]
- [[OCaml - Let bindings, Scope & Closures|OCaml - Let bindings, Scope & Closures]]
## Definition
- **Toploop (REPL):** Interactive OCaml prompt that evaluates expressions and prints both the value and its type.  
- **End of input:** In the toploop you end a phrase with `;;`.  
- **Bindings:** `let name = expr` binds `name` to the value of `expr`.  
- **Recursive bindings:** `let rec f x = ...` lets `f` call itself.  
> [!NOTE] *“Everything has a type.”*. Your default habit should be: *ask what type OCaml inferred* and *why*.
## How to talk to OCaml (Toploop workflow)
### Start / stop
- Run `ocaml` in a shell → you get `#`
- End a phrase with `;;`
- Exit with Control-D
### What the output means
- `- : <type> = <value>` → you didn’t bind a name
- `val <name> : <type> = <value>` → you used `let`
### Comments
- `(* comment *)`
- comments can be nested
Links:
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.1 Comment Convention and Interaction|Textbook Ch2.1]]
- [[50_Archive/UMN/Classes/CSCI 2041/Week - 1|Week - 1]]
## Core OCaml keywords you must recognize
### `let`
- binds a name to a value
```ocaml  
let n = 4;;
```
### `let ... in`
- creates a _local_ binding usable only in the following expression
```ocaml
let x = 1 in x + 2
```
### `let rec`
- required for self-calling functions
```ocaml
let rec fact n = ...
```
### `if ... then ... else ...`
- both branches must have the same type
- missing `else` behaves like returning `()`
Link:
- [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.3 Relations and Conditionals|Textbook Ch2.3]]
## Strong typing + type inference (the exam framing)
- OCaml is strongly typed: expressions of one type can’t be used where another type is expected.
- you usually don’t write types; OCaml infers them.
> [!WARNING] No implicit numeric coercions: `1 + 2.0` is invalid because `+` expects ints and `+.` expects floats.
## Primitive data types (with interlinks)
Link: [[50_Archive/UMN/Classes/CSCI 2041/Textbook/Chapter - 1 & 2#2.2 Primitive Data Types|Textbook Ch2.2]]
### unit
- only value: `()`
- used for side-effecting expressions (like updates/printing)
### int
- integer literals: decimal, `0b` binary, `0o` octal, `0x` hex
- operators: `+ - * / mod`
### float
- needs decimal point or exponent
- operators: `+. -. *. /.`
- conversions: `int_of_float`, `float_of_int`
### bool
- values: `true`, `false`
- logic: `not`, `&&`, `||`
- `&&` and `||` short-circuit
### char
- `'a'`, escape sequences like `'\n'`
### string
- `"hello"`
- concatenation: `^`
- indexing: `s.[i]`
## Operators you must not confuse
### Arithmetic
- ints: `+ - * / mod`
- floats: `+. -. *. /.`
### Comparisons
- structural equality: = and `<>`
- ordering: `< > <= >=`
### Physical equality
- == physical identity (same object in memory)
- `!=` physical non-identity
> [!NOTE] Exam-level explanation  
> = asks “same structure/value?”  
> == asks “same exact object?”
## Functions and function types
### Function type
- `t1 -> t2` means: input `t1`, output `t2`
### Multi-argument function type (curried model)
- `t1 -> t2 -> t3` means:
    - takes `t1`
    - returns a function `t2 -> t3`
### Function application
- no parentheses required for single-arg calls
- application has high precedence:
    - `f x + 1` means `(f x) + 1`
> [!INFO] “OCaml thinks all functions take one argument”: Multi-arg functions are nested functions.
## Lists (the professor’s “snake” model)
### Syntax
- empty list: `[]`
- list literal: `[e1; e2; e3]`
- cons: `h :: t`
- append: `@`
### `hd` and `tl`
- `hd (h :: t) = h`
- `tl (h :: t) = t`
- `hd []` and `tl []` are errors
### Persistence reminder
- `0 :: xs` creates a new list; `xs` unchanged
- `xs @ ys` copies the left spine
Link:
- [[OCaml - Types of Programming#Persistence (the “copy as little as possible” model)|Persistence]]
## Recursion (must-know structure)
### Base + recursive case
- base case does not call itself
- recursive case reduces input toward base
### Helper functions
Two common patterns:
1. **External helper** (defined outside)
2. **Internal helper** (defined inside using `let ... in` to inherit parameters)
Link:
- [[50_Archive/UMN/Classes/CSCI 2041/Week - 1#Lecture (Jan 28) - Multi-argument function types, append, immutability/persistence, helpers|Week - 1]] (internal helper mention)
## Tail recursion and stack frames (Jan 30 lecture)
- **Stack frame (activation record):** parameters, local names, return point.
- **Tail of a function:** chronologically last thing it does (not `tl`).
- **Tail call:** a call that occurs in the tail.
- **Tail recursive:** iff all recursive calls are tail calls.
- **Why it matters:** tail recursion can run in constant stack space because a compiler can reuse frames for tail calls.
### Canonical “is it tail recursive?” test
- If the recursive call returns and you still do work like `*`, `+`, `@`, `::`, etc., it is **not** tail-recursive.
- If the recursive call is the final action and you immediately return its result, it **can be** tail-recursive.
### Canonical rewrite pattern (accumulator helper)
- Introduce a helper with an accumulator.
- Move the “work” (like `*`) into the accumulator update.
- Make the recursive call the last action.
> [!NOTE] Lecture summary sentence: “We don’t need loops because we can write loops as tail recursions.”
## Common mistakes
- Forgetting `;;` in the toploop (OCaml keeps waiting).
- Forgetting `rec` for a self-calling function.
- Reading `t1 -> t2 -> t3` as “3-arg” instead of “returns a function”.
- Using `hd`/`tl` on `[]`.
## Mini-test (answer without looking)
- [ ] What does `;;` do in the toploop?
- [ ] What changes if you remove `rec` from a recursive definition?
- [ ] Explain `t1 -> t2 -> t3` in words.
- [ ] Why is `1 + 2.0` invalid, and what operator fixes it?
- [ ] What’s the difference between = and ==
## Flashcards (best 3–8)
#cards/CSCI2041 

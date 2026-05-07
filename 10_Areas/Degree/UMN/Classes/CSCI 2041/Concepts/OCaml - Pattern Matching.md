---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-02-25
topics:
  - "[[Midterm]]"
  - "[[CSCI 2041 Board]]"
  - "[[OCaml]]"
  - "[[10_Areas/Degree/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4|Chapter - 3 & 4]]"
related:
  - "[[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 2|Week - 2]]"
---
# Pattern Matching
## MOC  
- [[OCaml - Basics|OCaml - Basics]]  
- [[OCaml - BST Problems|OCaml - BST Problems]]  
- [[OCaml - Tautology Problems|OCaml - Tautology Problems]]
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Textbook/Chapter - 3 & 4#Chapter 4 Basic pattern matching|Textbook: Chapter 4]]
- [[10_Areas/Degree/UMN/Classes/CSCI 2041/Week - 2|Week - 2]]
- [[OCaml - BST Problems#Week 1: Persistent BST Insert (lecture code)|BST Insert (pattern split)]]
## Definition  
- **match evaluation rule:** evaluate matched expression once, try patterns top to bottom, first match wins.  
- **Variable patterns always bind:** a name in a pattern does not “check against” an existing binding.  
> [!INFO] “Dispatcher” analogy: A `match` block routes your input value to the correct branch, like a dispatcher sending the right response team.
## Why pattern matching is a “core skill” in this course
Pattern matching is how OCaml expects you to:
- do case analysis (instead of long if-chains)
- take data structures apart safely (instead of null pointers)
- write recursion cleanly (base case + recursive case)
This is why pattern matching appears everywhere:
- lists (`[]` vs `h :: t`)
- trees (`Leaf` vs `Node (...)` / `BSTempty` vs `BSTnode (...)`)
- your own data types (later: tautology checker / unions)
## Canonical forms  
### `match ... with`
```ocaml
match v with
| p1 -> e1
| p2 -> e2
| _  -> e_default
```
### `function` keyword (shorthand)
```ocaml
let f = function
| p1 -> e1
| p2 -> e2
```
> [!NOTE] When `function` is preferred: When your function’s body is “just a match on its single argument.”  
> - It avoids writing `fun x -> match x with ...`.
## Pattern vocabulary (what counts as a pattern)
### Constants
- `0`, `1`, `'a'`, `"hi"`, `true`, `false`, `()`
- match only if the value is exactly equal
### Variables (binding occurrences)
- `x`, `y`, `name`, `prop`, etc.
- matches anything and **binds the name** to the matched value
> [!WARNING] Binding danger (midterm favorite)  
> - If you write a name in a pattern, OCaml treats it as “bind a new variable,” not “compare to an existing name.”  
> - This can silently shadow earlier bindings and create useless branches.
### Wildcard `_`
- matches anything
- binds nothing
- used to “ignore” parts of a structure or provide a default
## Pattern matching on lists (most common)
### Empty vs non-empty
```ocaml
match xs with
| [] -> ...
| h :: t -> ...
```
### Safe “head” example pattern
```ocaml
let head = function
| h :: _ -> h
| [] -> raise (Invalid_argument "head")
```
> [!NOTE] Why the last line is good style? You avoid silent failure, and you make the missing case explicit.
## Pattern matching on tuples
```ocaml
match pair with
| (a, b) -> ...
```
Also appears in `let` bindings: `let (a, b) = pair in ...`
## Pattern matching on user-defined constructors (BST / tautology style)
### BST insert split (shape split)
```ocaml
match subtree with
| BSTempty -> ...
| BSTnode (k, left, right) -> ...
```
This is exactly the “safe case analysis + data destruction” model:
- you check which constructor you got
- you pull out the payload safely
## Advanced patterns (Ch4.2)
### Choice patterns: `p1 | p2`
```ocaml
| 0 | 1 -> ...
```
### Alias patterns: `p as name`
```ocaml
| (0 | 1) as i -> i
```
### Guards: `p when condition`
```ocaml
| x when x > 0 -> ...
| _ -> ...
```
> [!WARNING] Guard rule: A guard is checked only _after_ the pattern matches.
## Values of other types (Ch4.3 level)
Pattern matching works on:
- ints, bools, chars, strings, tuples, lists
- constructors of your types
**Float matching**: technically possible but usually avoided due to precision.
## Exhaustiveness + runtime failure (Ch4.4)
### What the compiler warns you about
If your patterns don’t cover all possibilities:
- OCaml warns “inexhaustive pattern matching”
### What happens at runtime
If an uncovered case happens:
- `Match_failure` can be raised
> [!NOTE] Exam-safe response pattern  
> - If a case should be “impossible,” you still either cover it with `_ -> ...` or raise an exception.
## Patterns are everywhere (Ch4.5)
Patterns show up in:
1. `match ... with`
2. `function`
3. `let` bindings (`let (a,b) = ...`)
4. function parameters (`let f (a,b) = ...`)
5. list parameters (`let f (h :: t) = ...`) _(use with care; handle `[]` too)_
6. unit parameters (`let f () = ...`)
## Midterm triggers (what to drill)
### “Already-used name in a pattern”
If you do: 
```ocaml
let x = 5 in
match y with 
| x -> ...
```
This branch matches **everything** and binds a new `x`.
### `match` vs `function`
- `match expr with ...` matches on an explicit expression
- `function ...` is shorthand for matching on the function’s single parameter
## Mini-test (answer without looking)
- [ ] Why do variable patterns not compare against existing bindings?
- [ ] When is `function` better than `fun x -> match x with ...`?
- [ ] What is a guard and when is it checked?
- [ ] What happens if pattern matching is inexhaustive at runtime?
## Flashcards (best 3–8)
#cards/CSCI2041 

---
type: concept
status: seed
created: 2026-04-27
updated: 2026-04-27
tags:
  - concept
notes:
  - "[[10_UMN/CSCI 2041/Concepts/OCaml - Pattern Matching]]"
  - "[[10_UMN/CSCI 2041/Concepts/OCaml - Basics]]"
track:
  - algorithms
prerequisites:
  - "[[10_UMN/CSCI 2041/Concepts/OCaml - Basics]]"
used_in: []
evidence: []
difficulty: 3
mastery_level: novice
drill_interval: 10
last_drilled: 2026-04-25
next_drill: 2026-05-05
---

# OCaml Pattern Matching

> Distilled from [[10_UMN/CSCI 2041/Concepts/OCaml - Pattern Matching|CSCI 2041 — Pattern Matching]]

## Deep Dive

### One-Sentence Version

Pattern matching is OCaml's primary mechanism for case analysis, data destruction, and recursion — it replaces if-chains, null checks, and manual field access with a single, compiler-checked construct.

### What It Is

A `match` expression evaluates the matched value once, tries patterns top to bottom, and the first match wins. Patterns can be:
- **Constants**: `0`, `true`, `[]` — match exact values
- **Variables**: `x`, `name` — match anything and bind the name (this is a new binding, not a comparison)
- **Wildcards**: `_` — match anything, bind nothing
- **Constructors**: `h :: t`, `BSTnode(k, left, right)` — destructure data types
- **Guards**: `x when x > 0` — checked only after the pattern matches

The `function` keyword is shorthand for `fun x -> match x with ...` when the function body is just a match on its single argument.

### Why It Matters

Pattern matching is how OCaml expects you to do case analysis (instead of if-chains), take data structures apart safely (instead of null pointers), and write recursion cleanly (base case + recursive case). It appears in every OCaml program: lists (`[] vs h :: t`), trees (`Leaf vs Node`), custom types. The compiler warns about inexhaustive patterns, catching bugs before runtime.

### Real Example

BST insert in OCaml:
```ocaml
match subtree with
| BSTempty -> BSTnode(key, BSTempty, BSTempty)
| BSTnode(k, left, right) ->
    if key < k then BSTnode(k, insert key left, right)
    else BSTnode(k, left, insert key right)
```
This is safe case analysis plus data destruction: you check which constructor you got and pull out the payload. No null checks, no casting, no field access on the wrong variant.

### Contrast With

- **Pattern matching vs if-else chains**: Pattern matching destructures data and binds variables in one step. If-else chains require separate field access and can miss cases without compiler help.
- **Variable patterns vs equality checks**: Writing a name in a pattern creates a new binding — it does not compare against an existing variable. This is a common exam trap: `match y with | x -> ...` matches everything and shadows the outer `x`.
- **`match` vs `function`**: `match expr with ...` matches on an explicit expression. `function ...` is shorthand for matching on the function's single parameter. Use `function` when the body is just a match.

### Source Anchors

- [[10_UMN/CSCI 2041/Concepts/OCaml - Pattern Matching]] — full lecture notes with all pattern forms
- [[10_UMN/CSCI 2041/Textbook/Chapter - 3 & 4]] — textbook coverage of pattern matching
- [[10_UMN/CSCI 2041/Concepts/OCaml - BST Problems]] — applied pattern matching on trees

## Diagnostic Questions

- Why do variable patterns not compare against existing bindings?
- When is `function` better than `fun x -> match x with ...`?
- What is a guard and when is it checked relative to the pattern?
- What happens if pattern matching is inexhaustive at runtime?

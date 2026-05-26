---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-05-08
updated: 2026-05-08
topics:
  - "[[CSCI 2041 Board]]"
related:
---

# OCaml - Association Lists

- An association list stores key-value bindings as a list-like chain searched from front to back.

## 30-Second Explanation
- Lab 8 implements `Association` with `Empty` and `Pair (key, value, rest)`. Lab 11 environments use the built-in OCaml-list version: `(string * thing) list`. In both cases, new bindings go in front, lookup returns the first matching key, and later bindings can shadow earlier ones.

## Teach It To A Beginner
- An association list is a tiny dictionary implemented as a list. To find a key, check the first pair; if it is not the key, check the rest.
- Lab 8's `put 4 "IV" a0` places a new `4` binding before the older `4 -> "IIII"` binding, so `get` returns `"IV"` first. After deleting that first `4`, lookup sees the older `"IIII"` again.

```ocaml
type ('a, 'b) t =
  | Empty
  | Pair of 'a * 'b * ('a, 'b) t ;;
```

## Definition
- Association list: a sequence of key-value pairs where lookup searches by key.
- Shadowing: when a newer binding for a key appears earlier and hides an older binding.

## Mental Model
- `put`: cons a binding to the front.
- `get`: scan front to back.
- `delete`: remove the first matching binding.
- Environment: association list from symbol names to values.

## Contrast With
- [[OCaml - Memoization]]: hash table lookup is mutable and optimized; association-list lookup is linear and structurally recursive.
- [[OCaml - Environments and Closures]]: environments are association lists with string keys and `thing` values.
- OCaml maps/hash tables: more structured or efficient, but less directly tied to course source.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 8]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 15]].
- Labs: [[Lab - 8 Association Module]], [[Lab - 11 Lisp Evaluator]].
- Projects: Project 2's `environment` type depends on `(string * thing) list`, though parser itself does not lookup names.
- Textbook: Hickey Ch. 5 lists, Ch. 8 hash tables as contrast.

## Common Mistakes
- Updating an old pair when the source pattern expects front insertion.
- Deleting every matching key instead of the first matching key in Lab 8.
- Forgetting the missing-key exception.
- Assuming lookup is constant time.

## Diagnostic Questions
- What does `Association.get a1 4` return after putting `"IV"` in front?
- Why does deleting the first `4` reveal the older `4`?
- How does environment lookup use the same front-to-back idea?
- What does `NoSuchKey` signal?

## Mini-Test
- [ ] Trace `put 4 "IV"` followed by `get 4`.
- [ ] Trace `delete 4` on a list with two `4` bindings.
- [ ] Explain shadowing in the evaluator environment.

## Flashcards
#cards/CSCI2041
- What is an association list::A list-like collection of key-value bindings.
- How does Lab 8 add a binding::At the front with `Pair`.
- What does `get` return if a key appears twice::The first matching binding.
- What exception does Lab 8 use for missing keys::`NoSuchKey`.
- How are evaluator environments represented::As `(string * thing) list`.

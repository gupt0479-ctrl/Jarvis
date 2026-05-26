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

# OCaml - Lisp Lists and Cons

- A Lisp list in the course interpreter is a chain of `Cons` cells ending in `Nil`.

## 30-Second Explanation
- The `thing` type uses `Cons of thing * thing` and `Nil` to represent Lisp list structure. A proper list has every `cdr` eventually reach `Nil`. This matters for Lab 9 recursion, Lab 10 printing, Project 2 parsing, and Lab 11 primitives like `car`, `cdr`, `cons`, and `list`.

## Teach It To A Beginner
- Lisp lists are built from pairs. The first part is the current element; the second part is the rest of the list. In OCaml source, the Lisp list `(a b)` is:

```ocaml
Cons (Symbol "a", Cons (Symbol "b", Nil))
```

- `car` returns the first part of a nonempty `Cons`. `cdr` returns the rest. `cons` builds a new `Cons`, but the Lab 11 implementation requires the rest argument to already be list-shaped.

## Definition
- `Cons (car, cdr)`: a Lisp pair/list node.
- Proper list: a `Cons` chain whose final `cdr` is `Nil`.
- `Nil`: empty list and false.

## Mental Model
- `(a b c)` means `a` linked to `b` linked to `c` linked to `Nil`.
- `car`: first link's value.
- `cdr`: everything after the first link.
- Printer/parser/evaluator all assume proper-list shape in important places.

## Contrast With
- OCaml lists: similar idea, different type and constructors.
- [[OCaml - Lisp Thing Representation]]: `Cons` is one constructor inside the larger `thing` universe.
- [[OCaml - Recursive Descent Parsing]]: parser builds `Cons` chains from parenthesized input.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 9]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 15]].
- Labs: [[Lab - 9 Lisp Data Recursion]], [[Lab - 10 Lisp Printer]], [[Lab - 11 Lisp Evaluator]], [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 2 Lisp Parser]].
- Textbook: Hickey Ch. 5 lists, Ch. 6 unions.

## Common Mistakes
- Ending a list with a symbol or number instead of `Nil`.
- Applying `car` or `cdr` to an atom.
- Printing a `Cons` chain with OCaml constructor syntax instead of Lisp syntax.
- Forgetting that `Nil` is both empty list and false in this interpreter.

## Diagnostic Questions
- Is `Cons (Symbol "a", Symbol "b")` a proper list?
- What does `cdr` return for `(a b c)`?
- What does the parser return for `()`?
- Why does Lab 10 reject improper lists in `printingThings`?

## Mini-Test
- [ ] Represent `(a (b c))`.
- [ ] Trace `(car (quote (a b)))`.
- [ ] Trace `(cdr (quote (a b)))`.

## Flashcards
#cards/CSCI2041
- What terminates a proper Lisp list::`Nil`.
- What does `car` return::The first element of a nonempty `Cons`.
- What does `cdr` return::The rest of a nonempty `Cons`.
- How is `(a)` represented::`Cons (Symbol "a", Nil)`.
- What does `cons` build::A new `Cons (first, rest)`.

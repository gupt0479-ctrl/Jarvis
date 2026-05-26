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

# OCaml - Lisp Thing Representation

- The course interpreter represents Lisp code and values as OCaml `thing` constructors, not as raw strings.

## 30-Second Explanation
- `Labs/lab9.ml` starts with `Nil`, `Number`, `Symbol`, and `Cons`. `Labs/lab10.ml`, `lab11.ml`, and `lab12.ml` expand `thing` with `Closure` and `Primitive`. This representation lets scanner/parser/printer/evaluator code share one internal language value shape.

## Teach It To A Beginner
- Lisp text like `(a b c)` is not convenient for evaluation. The parser turns it into an OCaml tree:

```ocaml
Cons (Symbol "a",
  Cons (Symbol "b",
    Cons (Symbol "c", Nil)))
```

- `Nil` is special: it is the empty list and false. `Cons (a, d)` is the Lisp pair/list node. `Symbol "x"` represents a name, and `Number 3` represents an integer literal.
- Later, `Closure` represents user functions made by `lambda`, and `Primitive` represents built-in functions implemented in OCaml.

## Definition
- `thing` is the course's algebraic data type for Lisp objects.
- In the evaluator version:

```ocaml
type thing =
  Closure of thing * thing * environment
| Cons of thing * thing
| Nil
| Number of int
| Primitive of (thing -> environment -> thing)
| Symbol of string
and environment = (string * thing) list ;;
```

## Mental Model
- Parser output is a `thing`.
- Printer input is a `thing`.
- Evaluator input and output are `thing` values.
- `Cons` chains are the spine of Lisp lists.

## Contrast With
- OCaml lists: `Cons` here is a constructor inside the Lisp object type, not OCaml's built-in `::`.
- [[OCaml - Scanners and Tokens]]: tokens are intermediate lexical units; `thing` values are parsed syntax/data.
- [[OCaml - Environments and Closures]]: environments map symbol strings to `thing` values.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 9]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 13]], [[Week - 15]].
- Labs: [[Lab - 9 Lisp Data Recursion]], [[Lab - 10 Lisp Printer]], [[Lab - 11 Lisp Evaluator]], [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 2 Lisp Parser]].
- Textbook: Hickey Ch. 4 pattern matching, Ch. 6 unions, Ch. 11-12 modules.

## Common Mistakes
- Parsing `"nil"` as `Symbol "nil"` instead of `Nil`.
- Treating a Lisp list as an OCaml list.
- Forgetting that a proper list ends in `Nil`.
- Printing or evaluating a raw string instead of first converting it to `thing`.

## Diagnostic Questions
- Which `thing` constructors can the parser produce directly?
- Which constructors are added for evaluator behavior?
- How is `(a (b c))` represented?
- Why is `Nil` both empty list and false?

## Mini-Test
- [ ] Write the `thing` for `(define x 3)`.
- [ ] Identify whether a given `Cons` chain is a proper list.
- [ ] Explain why `Closure` needs an `environment`.

## Flashcards
#cards/CSCI2041
- What is the internal representation of Lisp values::The `thing` type.
- How is Lisp false represented::`Nil`.
- How is a Lisp symbol represented::`Symbol of string`.
- How is a nonempty Lisp list represented::Nested `Cons` cells.
- What extra constructors appear in the evaluator::`Closure` and `Primitive`.

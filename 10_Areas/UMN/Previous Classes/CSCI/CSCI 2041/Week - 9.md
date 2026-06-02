---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Lisp Thing Representation]]"
  - "[[OCaml - Lisp Lists and Cons]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Week - 10]]"
---
# Entire Week
## What you must be able to do
- Explain how Lisp expressions are represented as OCaml values, not strings.
- Write structural recursion over nested `thing` values.
- Trace `every`, `substitute`, and `questyEqual` from `Labs/lab9.ml`.
- Explain how `Cons` and `Nil` encode Lisp lists (proper list = `Cons` chain ending in `Nil`).
- Connect the `thing` representation to the later scanner, parser, printer, and evaluator.

## Key ideas (textbook)
- Hickey Ch. 6 `Unions`: the `thing` type is an ADT. Each constructor names a different case.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 4]] `Pattern matching`: every operation over `thing` dispatches by constructor.
- Hickey Ch. 5 `Lists`: Lisp lists are *not* OCaml lists in the interpreter — they're nested `Cons` values terminated by `Nil`.
- Hickey Ch. 11-12: the interpreter grows into a multi-module program, so signatures matter.

## Concepts created / updated today
- [[OCaml - Lisp Thing Representation]]
- [[OCaml - Lisp Lists and Cons]]
- [[OCaml - Algebraic Data Types and Structural Recursion]]
- [[OCaml - Modules and Signatures]]

## Lecture
### Week 9 lecture map - from OCaml modules to Lisp as data
Week 9 is the start of the Lisp interpreter arc. The course moves from OCaml's module system into the question that will drive the rest of the class: how can one language represent, print, parse, and evaluate another language?

Source anchors:
- `Lecture - 21.txt` finishes language history: lambda calculus, Lisp, Hindley-Milner, Caml, and OCaml. The reason for the history is practical: the class is about to write a Lisp interpreter in OCaml.
- The same lecture introduces Lisp's `cons`, `car`, and `cdr`, plus list functions such as append and equality.
- `Lecture - 22.txt` develops Lisp syntax through examples: true/false, empty list, comments, symbols, `is-member`, `has-member`, and `equal`.
- `Lecture - 23.txt` defines the interpreter direction: REPL, internal Lisp-object representation, `thing`, `environment`, and a reader based on scanner/parser ideas.
- `Labs/lab9.ml` is the first small interpreter-data lab: `thing`, `every`, `substitute`, and `questyEqual`.

The key source-grounded claim: Lisp expressions stop being text as soon as the parser has done its job. They become `thing` values. From there, every operation is pattern matching and structural recursion.

### Mar 23 — Finishing Modules, Moving Toward Lisp
Sources: `Lecture - 21.txt`, professor notes `23Mar26/`, Hickey Ch. 11-12.

The history section matters because Lisp is not random flavor text. The course is about to implement a Lisp reader/evaluator, so the professor uses lambda calculus, Lisp, Hindley-Milner, Caml, and OCaml to explain why Lisp code-as-data and OCaml typed functions belong in the same final project arc.

Transition from isolated OCaml functions to a system whose pieces communicate through explicit data representations. Modules matter because the interpreter won't be one tiny function — scanner, parser, printer, evaluator, REPL all have separate jobs with small interfaces and hidden state.

### Mar 25 — Lisp Values as OCaml Data
Sources: `Lecture - 22.txt`, professor notes `25Mar26/`, `Labs/lab9.ml`.

The lecture teaches Lisp through examples: true and false, empty list, comments, symbols, and small list functions. The key convention for this course's Lisp is that `nil` is both the empty list and false, while almost anything else counts as true. That convention drives evaluator primitives such as `and`, `or`, `if`, and `not`.

```ocaml
type thing =
  Nil |
  Number of int |
  Symbol of string |
  Cons of thing * thing ;;
```

This is the interpreter's first important design choice. A Lisp expression is not raw text — once parsed, it becomes an OCaml tree built from constructors. Later functions are ordinary structural recursions.

**`Nil` does double duty:** empty list *and* false.
**`Cons (first, rest)`** builds list structure. A proper list ends in `Nil`. An improper list has a final rest that's not `Nil` or another `Cons` — printers and evaluators have to care about that shape.

### Mar 27 — Recursive Operations on Lisp Things
Sources: `Lecture - 23.txt`, professor notes `27Mar26/`, `Labs/lab9.ml`, `Labs/tests9.ml`.

This lecture names the interpreter shape explicitly: read, evaluate, print loop. Before the REPL can exist, the course needs internal forms for Lisp objects and environments. The `thing` type is the bridge: the reader/parser produces it, the printer consumes it, and the evaluator interprets it.

```ocaml
let rec every predicate elements = ...
let rec substitute elements oldThing newThing = ...
let rec questyEqual left right = ...
```

**`every`** — predicate over a Lisp list. Must understand that a list is a chain of `Cons` cells ending in `Nil`. Don't treat `Cons` like OCaml's `::`.

**`substitute`** — tree walk. If current `thing` equals old target, return replacement. If `Cons`, recursively substitute in both first and rest. If atom, leave alone. This pattern comes back in the if-based tautology checker.

**`questyEqual`** — structural equality for `thing` values. Compares matching constructors and recursively compares nested `Cons` cells. `Symbol "?"` acts as a wildcard. This is exactly the kind of recursion the interpreter needs everywhere.

## Labs / Projects
### Lab 9 — Lisp Data Recursion
Source: `Labs/lab9.ml` | Tests: `Labs/tests9.ml`

Tests the first small Lisp `thing` model. Main functions: `every`, `substitute`, `questyEqual`.

Concepts: [[OCaml - Lisp Thing Representation]], [[OCaml - Lisp Lists and Cons]], [[OCaml - Algebraic Data Types and Structural Recursion]]

**Final check:** be able to explain how a proper Lisp list is a `Cons` chain ending in `Nil` and how `questyEqual` treats `?`.

## Examples worth keeping
- `Cons (Symbol "a", Cons (Symbol "b", Nil))` — Lisp list `(a b)` in internal form.
- `Nil` — both empty list and false in the course's Lisp.
- `substitute` — same recursive shape as many tree transformations.
- Proper list invariant: keep following `Cons (_, rest)` until `Nil`.

## Takeaways (questions to resolve)
- [ ] Why does the interpreter use `thing` values instead of raw strings?
- [ ] What makes a Lisp list proper vs improper?
- [ ] How is `Cons` different from OCaml's `::`?
- [ ] What should `substitute` do to nested `Cons` values?
- [ ] Why does structural equality matter before evaluation starts?

## Flashcards
#cards/CSCI2041
- What constructors are in Lab 9's `thing` type::`Nil`, `Number`, `Symbol`, and `Cons`.
- How is Lisp `(a b)` represented internally::`Cons (Symbol "a", Cons (Symbol "b", Nil))` — right-nested Cons chain ending in Nil.
- What does `Nil` mean in the course Lisp::Empty list *and* false — it does double duty.
- What is structural recursion over `thing`::Recursion that follows the shape of the constructors: base cases for atoms, recursive cases for `Cons`.
- What does `questyEqual` do with `Symbol "?"`::Treats it as a wildcard that matches any `thing` value.
- Why is `Cons` not the same as OCaml `::`::OCaml `::` builds OCaml lists; `Cons` builds Lisp `thing` trees. Different types, different operations.

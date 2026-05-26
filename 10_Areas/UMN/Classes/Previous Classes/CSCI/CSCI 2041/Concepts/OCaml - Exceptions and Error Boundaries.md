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

# OCaml - Exceptions and Error Boundaries

- Exceptions mark cases where a function cannot produce a normal result under its contract.

## 30-Second Explanation
- Week 6 onward uses explicit exceptions as API boundaries: `LazyListError` for empty lazy-list head/tail, `NoSuchKey` for association lookup failure, `SolvingError` for invalid equation solving, `Can'tParse` for parser errors, and `EvaluatorError` for invalid Lisp evaluation.

## Teach It To A Beginner
- A function's type may say it returns a value, but not every input is valid. Exceptions are the course's way of saying "this input violates the contract."
- The important part is not just raising any exception. The exception name belongs to the component boundary: association errors use `Association.NoSuchKey`, parser errors use `Can'tParse`, evaluator errors use `EvaluatorError of string`.

```ocaml
module type Parserish =
sig
  exception Can'tParse of string ;;
  val initialize : string -> unit ;;
  val nextThing : unit -> thing ;;
end ;;
```

## Definition
- Exception: a non-normal control path used to report an error.
- Error boundary: the place where a module exposes a specific exception as part of its public contract.

## Mental Model
- Empty lazy list head: caller asked for a value that does not exist.
- Missing association key: lookup failed.
- Bad parse: token stream violates grammar.
- Bad evaluation: Lisp expression violates evaluator rules.

## Contrast With
- Returning `option`: not the source pattern for these labs.
- Silent default values: would hide errors and make tests misleading.
- [[OCaml - Modules and Signatures]]: signatures expose exceptions that callers are allowed to know about.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 8]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 10]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 11]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 12]], [[Week - 15]].
- Labs: [[Lab - 7 Lazy Lists]], [[Lab - 8 Association Module]], [[Lab - 11 Lisp Evaluator]], [[Lab - 12 Lisp Integration]].
- Projects: [[Project - 1 Equation Solver]], [[Project - 2 Lisp Parser]].
- Textbook: Hickey Ch. 9 exceptions.

## Common Mistakes
- Returning `Nil` for parser errors.
- Catching too broadly and hiding the actual error.
- Raising the wrong module's exception.
- Omitting the exception from the signature when outside code/tests need to catch it.

## Diagnostic Questions
- Which exception belongs to parser failure?
- Which exception belongs to evaluator failure?
- What should `Association.get` do when the key is absent?
- Why should `lazyHead LazyEmpty` not return a dummy value?

## Mini-Test
- [ ] Match each source exception to its component.
- [ ] Explain why `EndToken` inside a list is a parser error.
- [ ] Explain why `(car 3)` is an evaluator error.

## Flashcards
#cards/CSCI2041
- What exception does Project 2 parser expose::`Can'tParse of string`.
- What exception does Lab 8 expose::`NoSuchKey`.
- What exception does Lab 7 expose::`LazyListError`.
- What exception does Project 1 define::`SolvingError of string`.
- What textbook chapter covers exceptions::Hickey Ch. 9.

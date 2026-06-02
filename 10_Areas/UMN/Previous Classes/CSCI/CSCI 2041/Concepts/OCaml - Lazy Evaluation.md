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

# OCaml - Lazy Evaluation

- Lazy evaluation delays a computation until the program explicitly demands its value.

## 30-Second Explanation
- `Labs/lab7.ml` represents a lazy list with delayed heads and delayed tails: `LazyNode of 'a Lazy.t * 'a lazyList Lazy.t`. `lazyHead` and `lazyTail` use `Lazy.force`. The tests show that a value prints its "Computed ..." message only when forced, and repeated forcing reuses the already-computed lazy value.

## Teach It To A Beginner
- Eager code does the work before handing you the value. Lazy code hands you a promise. You can carry that promise around, and only when you call `force` does OCaml do the work inside it.
- A lazy Fibonacci list would not terminate if it tried to compute every Fibonacci number now. It works because each tail is a promise for the rest of the list, not the rest itself.
- Textbook connection: Hickey Ch. 7 matters because evaluation order becomes visible when there are effects; the lab deliberately prints messages to show when work happens.
- Lecture connection: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 7]] introduces lazy lists; [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 8]] gives the eager-vs-lazy framing.

```ocaml
open Lazy ;;

type 'a lazyList =
  | LazyEmpty
  | LazyNode of 'a Lazy.t * 'a lazyList Lazy.t ;;

let lazyHead list =
  match list with
  | LazyEmpty -> raise LazyListError
  | LazyNode (head, _) -> force head ;;
```

## Definition
- Lazy evaluation is an evaluation strategy where an expression is packaged for later computation and evaluated only when forced.
- In Lab 7, `Lazy.t` is the package and `Lazy.force` is the demand.

## Mental Model
- A lazy value is a sealed envelope.
- `lazy (...)` writes the work inside the envelope.
- `force envelope` opens it.
- A lazy list is a chain of envelopes, so a finite `lazyTake` opens only a finite prefix.

## Contrast With
- [[OCaml - Streams]]: streams store an explicit next function; Lab 7 lazy lists use `Lazy.t`.
- Eager lists: every list node already exists when the list value exists.
- [[OCaml - References and Mutation]]: laziness is about timing of computation; mutation is about changing stored state.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 8]], [[Week - 15]].
- Labs: [[Lab - 7 Lazy Lists]] from `lab7.ml` and `tests7.ml`.
- Projects: not a direct project requirement, but the "do only the demanded work" idea helps explain special forms in [[OCaml - Interpreter Primitives and Special Forms]].
- Textbook: Hickey Ch. 7 for effects/evaluation order; Hickey Ch. 3 for functions used to delay work.

## Common Mistakes
- Forcing the whole lazy list while trying to write a helper.
- Forgetting that both the head and tail in `lab7.ml` are lazy values.
- Treating `LazyEmpty` as an error everywhere; `lazyTake LazyEmpty n` should return `[]`.
- Confusing the first call that computes a value with later calls that reuse it.

## Diagnostic Questions
- What is the type of the head inside `LazyNode`?
- Why does `lazyFibs ()` terminate when it creates an infinite lazy list?
- Which function actually demands the delayed value?
- Why do the Lab 7 tests print computation messages only once for repeated `lazyTake`?

## Mini-Test
- [ ] Implement `lazyHead`, `lazyTail`, and `lazyTake`.
- [ ] Explain why `lazyTake allTheFibs 10` can finish.
- [ ] Predict which messages print when taking 3 values, then taking 9 values, then taking 9 again.

## Flashcards
#cards/CSCI2041
- What does `lazy` create::A delayed computation of type `Lazy.t`.
- What does `Lazy.force` do::Computes or retrieves the delayed value.
- What is delayed in Lab 7's lazy list::Both the head value and the tail list.
- Why does a lazy infinite list work::Only demanded nodes are forced.
- What exception does Lab 7 use for empty-head/tail errors::`LazyListError`.

---
type: concept
course: CSCI 2041
status: sprout
mastery (1/10): 0
created: 2026-05-08
updated: 2026-05-09
topics:
  - "[[CSCI 2041 Board]]"
related:
  - "[[OCaml - Lazy Evaluation]]"
  - "[[OCaml - Higher-Order Functions]]"
  - "[[OCaml - Environments and Closures]]"
---

# OCaml - Streams

## One-Line Answer
A stream stores a current value, private state, and a next function — finite requests pull from a conceptually infinite sequence because the tail is computed on demand.

## 30-Second Explanation
In `Labs/lab5.ml`, a stream is `((this, state), next)`. `first` returns `this`. `rest` calls `next this state` and reuses the same `next` function. The stream isn't an infinite list in memory — it's a bookmark plus a rule for advancing.

## Definition
- A pair: `(current_value, state)` + a next function.
- The next function computes the next `(current_value, state)` pair.
- A consumer like `take` asks for a finite prefix by repeated calls to `rest`.

## OCaml Shape
```ocaml
let makeStream this state next = ((this, state), next) ;;
let first ((this, state), next) = this ;;
let rest ((this, state), next) = (next this state, next) ;;

let rec take count stream =
  match count with
  | 0 -> []
  | _ -> first stream :: take (count - 1) (rest stream) ;;
```

## Mental Model
- Stream cell = "value now, recipe for later."
- `first` = inspect current value.
- `rest` = run the recipe once.
- `take` = repeat "inspect, advance" a fixed number of times.

## Contrast With
- **[[OCaml - Lazy Evaluation]]**: lazy lists use `Lazy.t` and `Lazy.force`; Lab 5 streams store a custom next function. Different mechanism, similar goal.
- **OCaml lists**: ordinary lists store their tail structurally; streams compute the next cell on demand.
- **[[OCaml - Continuation Passing]]**: CPS sends results to a continuation; streams return a new stream state.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 6]], [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 8]], [[Week - 15]].
- Labs: Lab 5 (`lab5.ml`, `tests5.ml`).
- Textbook: Hickey Ch. 3 (functions/scoping); Ch. 14 (object-style comparison).

## Common Mistakes
- Treating a stream as if it already contains all future elements.
- Forgetting that `rest` must return *another stream*, not just the next value.
- Losing the state needed by `scale` or `sum`.
- Calling `take` with unbounded count or trying to print the whole stream.
- Thinking state always equals the current value (works for `naturals`, breaks for `sum`).

## Diagnostic Questions
- What three pieces does `makeStream` store?
- What exactly does `rest odds` compute?
- Why does `sum left right` keep two streams in its state?
- Why can `take 7 odds` terminate even though `odds` is conceptually infinite?

## Flashcards
#cards/CSCI2041
- What is a Lab 5 stream made of::A current value, a state value, and a next function.
- What does `rest` do to a stream::Calls the stored next function on current value and state, producing the next stream cell.
- Why can streams represent infinite sequences::Only the requested next cell is computed — the tail is a function, not a prebuilt list.

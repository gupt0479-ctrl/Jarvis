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

# OCaml - Tail Recursion and Internal Helpers

- Tail recursion puts the recursive call in final position; internal helpers keep fixed outer values available while the changing state is passed recursively.

## 30-Second Explanation
- Week 15's final review explicitly contrasts mutually recursive functions with embedded/internal helper functions. The Week 14 `tautology.ml` source also uses helper functions such as `uniquifying things uniqueThings`, where the accumulator is passed forward. The reusable pattern: the public function sets up a helper; the helper recurses over the changing part.

## Teach It To A Beginner
- A recursive call is in tail position when the function has nothing left to do after that call returns. An accumulator carries the partial answer.
- An internal helper is useful when one value should stay fixed across recursive calls. In final review, the protected example shape is like `contains target things`, where `target` stays in the outer scope and the helper only changes `things`.
- Textbook connection: Hickey Ch. 3 covers recursive functions, nested functions, and scoping.

```ocaml
let uniquify things =
  let rec uniquifying things uniqueThings =
    match things with
    | [] -> uniqueThings
    | firstThing :: otherThings ->
        if isIn firstThing uniqueThings
        then uniquifying otherThings uniqueThings
        else uniquifying otherThings (firstThing :: uniqueThings)
  in
  uniquifying things [] ;;
```

## Definition
- Tail recursion: recursion where the recursive call is the last operation in the current branch.
- Internal helper: a locally defined function, often recursive, used to carry accumulators or inherit fixed outer variables.
- Accumulator: an argument that stores work already completed.

## Mental Model
- Normal structural recursion: "solve rest, then combine."
- Tail recursion: "update the accumulator, then continue."
- Internal helper: "public function chooses the initial state; helper does the loop."

## Contrast With
- [[OCaml - Algebraic Data Types and Structural Recursion]]: structural recursion mirrors data; tail recursion reorganizes work for stack/control behavior.
- [[OCaml - Mutual Recursion]]: mutual recursion is for functions that call each other; internal helpers are inside one outer function.
- [[OCaml - Continuation Passing]]: CPS also controls what happens next, but passes an explicit continuation instead of a simple accumulator.

## Where It Appears
- Weekly notes: [[Week - 14]], [[Week - 15]].
- Labs: review source in `Labs/Practice/tautology.ml`; indirect review across earlier list labs.
- Projects: useful for parser/printer/evaluator helpers, though not always tail recursive.
- Textbook: Hickey Ch. 3.

## Common Mistakes
- Adding work after the recursive call and still calling it tail recursive.
- Exposing the helper as the main API even when it has awkward accumulator arguments.
- Using mutual recursion when a nested helper with a fixed outer value would be simpler.
- Reversing output accidentally because accumulators often build with `::`.

## Diagnostic Questions
- In `uniquifying`, what changes on every recursive call?
- What value stays fixed in an internal helper pattern?
- Why is `let rec f ... and g ...` not the same as `let rec helper ... in ...`?
- How can an accumulator change output order?

## Mini-Test
- [ ] Convert a simple list length function to tail recursion.
- [ ] Explain why `uniquifying` needs `uniqueThings`.
- [ ] Decide whether a pair of functions needs `and` or an internal helper.

## Flashcards
#cards/CSCI2041
- What makes a recursive call tail-recursive::Nothing remains to do after the recursive call returns.
- What is an accumulator::An argument carrying the partial result.
- Why use an internal helper::To carry changing state while keeping outer values in scope.
- What source file shows `uniquifying`::`Labs/Practice/tautology.ml`.
- What final-review distinction matters here::Mutual recursion vs internal helper functions.

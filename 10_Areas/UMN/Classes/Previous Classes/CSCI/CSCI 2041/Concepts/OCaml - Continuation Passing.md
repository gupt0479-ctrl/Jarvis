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

# OCaml - Continuation Passing

- Continuation passing gives a function another function that represents what to do with each result.

## 30-Second Explanation
- Week 14's `Labs/Practice/permute.ml` uses continuations in `indexes min max etc` and `permute chars etc`. Earlier `tautology.ml` generators also call continuations on generated booleans or environments. Instead of returning one giant list, the generator calls `etc` for each result.

## Teach It To A Beginner
- A continuation is a "next step" function. If `indexes 0 2 etc` generates `0`, `1`, and `2`, it does not return `[0;1;2]`; it calls `etc 0`, then `etc 1`, then `etc 2`.
- In `permute`, the continuation prints or consumes each permutation when the algorithm reaches a complete arrangement.

```ocaml
let indexes min max etc =
  let rec indexing index =
    if index <= max
    then (etc index;
          indexing (index + 1))
    else ()
  in
  indexing min ;;
```

## Definition
- Continuation: a function representing the remaining work to do with a produced value.
- CPS-style generator: a function that produces results by calling a continuation instead of returning a collection.

## Mental Model
- Ordinary return: "Here is my one result."
- Generator with continuation: "For each result I find, I will call this function."
- Backtracking: mutate/choose, recurse, undo, continue.

## Contrast With
- [[OCaml - Higher-Order Functions]]: CPS is one specific use of higher-order functions.
- [[OCaml - Tail Recursion and Internal Helpers]]: accumulators collect results; continuations consume results as they appear.
- Streams/lazy lists: streams expose pull-based next values; CPS generators push values to `etc`.

## Where It Appears
- Weekly notes: [[Week - 14]], [[Week - 15]].
- Labs/practice: `Labs/Practice/permute.ml`, `Labs/Practice/tautology.ml`.
- Projects: no direct Week 6 onward project requirement, but parser/evaluator callbacks would use the same function-as-next-step idea.
- Textbook: Hickey Ch. 3 functions and recursion.

## Common Mistakes
- Expecting a CPS generator to return a list.
- Forgetting to undo mutation after a recursive permutation branch.
- Calling the continuation too early before the result is complete.
- Ignoring the order in which continuation calls occur.

## Diagnostic Questions
- What does `etc` mean in `indexes`?
- When does `permute` call its continuation?
- Why does `permute` swap back after recursion?
- How does `generateAndTestPairs` use continuation-like testing?

## Mini-Test
- [ ] Trace `indexes 0 2 print_int`.
- [ ] Explain how `permute [|'A'; 'B'; 'C'|]` reaches `ABC`.
- [ ] Rewrite a simple list-returning generator as a continuation-calling generator.

## Flashcards
#cards/CSCI2041
- What is a continuation::A function representing what to do next with a result.
- What parameter name does the course use for continuations::`etc`.
- What does `indexes` generate::Integers from `min` through `max`.
- How does `permute` output many results::It calls `etc` on each complete permutation.
- What source file anchors Week 14 CPS review::`Labs/Practice/permute.ml`.

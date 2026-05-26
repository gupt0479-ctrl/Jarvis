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
  - "[[OCaml - References and Mutation]]"
  - "[[OCaml - Lazy Evaluation]]"
  - "[[OCaml - Higher-Order Functions]]"
---

# OCaml - Memoization

## One-Line Answer
Cache function results by input so recursive code doesn't recompute the same subproblem.

## 30-Second Explanation
`Labs/lab6.ml` compares `c n k` (plain recursive binomial coefficients) with `memyC n k` (same recurrence + local `Hashtbl` cache). The math stays identical; the operational behavior changes because repeated `(n, k)` calls return cached values. `tests6.ml` makes the point by timing both — `c 40 10` takes seconds, `memyC 40 10` runs instantly.

## Definition
- Optimization pattern: store previously computed input→output pairs.
- Return stored output when the same input appears again.
- In Lab 6: cache key is `(n, k)`, cached value is the binomial coefficient.

## OCaml Shape
```ocaml
let memyC n k =
  let table = Hashtbl.create ~random:false 1000 in
  let rec memo n k =
    match Hashtbl.find_opt table (n, k) with
    | Some v -> v
    | None ->
        let result =
          if k = 0 then 1
          else if n = 0 then 0
          else if k > n then 0
          else memo (n - 1) k + memo (n - 1) (k - 1)
        in
        Hashtbl.add table (n, k) result ;
        result
  in memo n k ;;
```

## Mental Model
- Without memoization: recursion tree with repeated branches.
- With memoization: first branch computes; later branches point to saved answer.
- Local cache: each call to `memyC` owns its own table.

## Contrast With
- **[[OCaml - References and Mutation]]**: mutation is the *mechanism*; memoization is the *design pattern*.
- **Dynamic programming (tabulation)**: memoization is top-down caching; tabulation is bottom-up table filling.
- **[[OCaml - Lazy Evaluation]]**: laziness *delays* work; memoization *avoids repeated* work.

## Where It Appears
- Weekly notes: [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[Week - 15]].
- Labs: Lab 6 (`lab6.ml`, `tests6.ml`).
- Textbook: Hickey Ch. 7 (references/side effects), Ch. 8 (hash tables).

## Common Mistakes
- Using only `n` or only `k` as the key instead of the pair `(n, k)`.
- Creating the table *inside* the recursive helper — erases the cache every call.
- Forgetting to store the result before returning it.
- Thinking memoization changes the recurrence's mathematical answer. It shouldn't.

## Diagnostic Questions
- Why does `c 40 10` recompute so much?
- Where is the hash table created in `memyC`?
- Why is `(n, k)` the cache key and not just `n`?
- What should happen if a cached result is found?
- What's the bug if a memoized function is still exponential?

## Flashcards
#cards/CSCI2041
- What is memoization::Caching function results by input to avoid recomputation.
- What is Lab 6's cache key::`(n, k)` — the pair of both arguments.
- What does memoization change::Runtime behavior (exponential → polynomial), not the recurrence's answer.

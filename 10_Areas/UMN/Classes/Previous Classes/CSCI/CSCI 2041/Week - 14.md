---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - If Normalization and Tautology Checking]]"
  - "[[OCaml - Continuation Passing]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[Week - 15]]"
---
# Entire Week
## What you must be able to do
- Explain the if-based proposition representation: `T`, `F`, `V of string`, `If of proposition * proposition * proposition`.
- Explain how `makeIf` simplifies while constructing `If` nodes (smart constructor).
- Trace `normalize`, `substitute`, and `isTautology`.
- Explain what `isEquivalent` decides.
- Connect the if-based checker to the earlier brute-force checker in `tautology.ml`.
- Explain the CPS permutation example without rewriting Week 5.

## Key ideas (textbook)
- [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 4]]: tautology code is almost entirely constructor dispatch.
- Hickey Ch. 6 `Unions`: proposition forms are algebraic data constructors.
- Hickey Ch. 3: CPS and transformation functions depend on functions as values.
- Hickey Ch. 5: earlier brute-force tautology uses lists of assignments.

## Concepts created / updated today
- [[OCaml - If Normalization and Tautology Checking]]
- [[OCaml - Continuation Passing]]
- [[OCaml - Algebraic Data Types and Structural Recursion]]

## Lecture
### Week 14 lecture map - symbolic tautology checking and final CPS
Week 14 is the last full lecture week. The main topic is a symbolic tautology checker based on `If`, followed by a final continuation-passing permutation example.

Source anchors:
- `Lecture - 37.txt` says the week will finish the tautology checker based on ifs, especially simplification rules 6 through 11 and OCaml functions `makeIf`, `normalize`, `substitute`, and `isTautology`.
- `Lecture - 38.txt` finishes the checker and emphasizes that the final exam is cumulative: concatenate the midterm topic list and final topic list.
- `Lecture - 39.txt` is the last ordinary lecture and gives a CPS permutation/anagram example.
- `Labs/Practice/iffyTaut.ml` is the source file for the if-based checker, including rules 1-11, `makeIf`, `normalize`, `substitute`, `isEquivalent`, and `isTautology`.
- `Labs/Practice/permute.ml` is the source file for the CPS/backtracking example: `indexes`, `permute`, `swap`, `permuting`, and the continuation `etc`.

The checker's progression:
1. Represent all logic with `T`, `F`, `V`, and `If`.
2. Encode connectives by rules 1-5.
3. Use rule 6 to normalize nested tests.
4. Use rules 7-11 to simplify constants, identity cases, and repeated variable tests.
5. Decide tautology by checking whether the normalized/simplified proposition becomes `T`.

The final CPS example has the same continuation idea as Week 5 and Lab 4, but with arrays and backtracking. `permute` swaps a character into position, recursively permutes the suffix, calls `etc` on a completed arrangement, then swaps back.

### Apr 27 — If-Based Tautology Rules
Sources: `Lecture - 37.txt`, professor notes `27Apr26/`, `Labs/Practice/iffyTaut.ml`.

The lecture frames the week as the last full week and names the OCaml functions the checker needs: `makeIf`, `normalize`, `substitute`, and `isTautology`. It also calls out the remaining mystery: how to decide whether two if-expressions are equivalent.

Rules 1-5 encode ordinary logical operators using `If`. Rules 6-11 simplify and normalize. The source file makes this concrete: `makeIf` implements rules 7-9 directly, while `normalize`, `substitute`, and `simplify` handle the more recursive work.

Smaller representation than full propositional logic:
```ocaml
type proposition =
  T | F | V of string | If of proposition * proposition * proposition ;;
```

Instead of separate `And`, `Or`, `Not`, `Imply` constructors, everything is encoded through `If`:
```ocaml
let (!) alpha = If (alpha, F, T) ;;         (* not *)
let (&&) alpha beta = If (alpha, beta, F) ;; (* and *)
let (||) alpha beta = If (alpha, T, beta) ;; (* or *)
```

Rules 6-11 simplify and normalize if-expressions. The study target: know what shape each rule removes — constant tests, equal branches, nested tests, repeated variables.

### Apr 29 — Normalize, Substitute, and Tautology
Sources: `Lecture - 38.txt`, professor notes `29Apr26/`, `Labs/Practice/iffyTaut.ml`, `Labs/Practice/tautology.ml`.

The lecture repeats the exam warning: the final is cumulative, so the final list and midterm list must be combined. For this topic, the contrast with the older brute-force checker is part of the study target. The old checker enumerates assignments; the new checker transforms the proposition.

`isEquivalent` is recursive in an interesting way: two propositions are equivalent if they are structurally equal or if the biconditional between them is itself a tautology. That feeds back into `isTautology`.

Function sequence in `iffyTaut.ml`:
- **`makeIf`** — smart constructor. Doesn't blindly return `If (pi, alpha, beta)`. Checks for cases that simplify immediately. Smart constructors enforce invariants at construction time.
- **`normalize`** — recursively rewrites if-expressions into a more regular shape.
- **`substitute phi v b`** — replaces a variable with a truth value inside a proposition.
- **`isTautology`** — uses transformations to decide whether a proposition is always true.
- **`isEquivalent`** — the mystery to solve.

**Contrast with brute-force:** `tautology.ml` generates Boolean assignments, evaluates propositions, tests all possibilities. The if-based version is symbolic — transforms the proposition itself rather than enumerating truth tables.

### May 1 — Final Lecture and CPS Example
Sources: `Lecture - 39.txt`, professor notes `01May26/`, `Labs/Practice/permute.ml`.

The last ordinary lecture returns to CPS with an anagram/permutation generator. `indexes` acts like an imperative `for` loop by calling a continuation on each integer in a range. `permute` uses mutation and backtracking: swap, recurse, call the continuation when a complete arrangement is ready, then swap back.

This example is deliberately connected to earlier CPS. The function does not compute one single return value; it produces many possible results by calling `etc` for each result.

CPS/backtracking shape:
```ocaml
let indexes min max etc = ...
let permute chars etc = ...
```

The continuation `etc` says what to do with a result once available. In permutation generation, the function doesn't return one giant list — it calls the continuation on each generated arrangement.

Links back to [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2041/Week - 5]] and [[OCaml - Continuation Passing]] (Week 5 stays protected).

## Labs / Projects
- No new numbered lab this week.
- Practice files are the source: `Labs/Practice/iffyTaut.ml`, `Labs/Practice/tautology.ml`, `Labs/Practice/permute.ml`.

## Examples worth keeping
- `If (alpha, F, T)` — negation encoded using if.
- `If (alpha, beta, F)` — conjunction encoded using if.
- `makeIf` — smart constructor that simplifies while building.
- `substitute phi v b` — recursively replace a variable with `T` or `F`.
- `permute chars etc` — generate results by calling a continuation.

## Takeaways (questions to resolve)
- [ ] Why can `If` represent `not`, `and`, `or`, and implication?
- [ ] What does `makeIf` simplify? (constant tests, equal branches, etc.)
- [ ] What is the purpose of normalization before tautology checking?
- [ ] How is the if-based checker different from brute-force? (symbolic vs enumerative)
- [ ] What does a continuation receive in the permutation example?

## Flashcards
#cards/CSCI2041
- How does `iffyTaut.ml` encode negation::`If (alpha, F, T)` — if alpha then false else true.
- What is a smart constructor::A function that simplifies or enforces invariants while building a value, rather than blindly wrapping constructors.
- What does `substitute` do::Replaces a variable with a truth value (`T` or `F`) inside a proposition tree.
- How is the if-based tautology checker different from brute-force::It transforms proposition structure symbolically instead of enumerating all truth assignments.
- How does CPS generation return many results::By calling a continuation for each result instead of building and returning a list.
- What does `normalize` do::Recursively rewrites if-expressions into a regular shape so later checks are simpler.

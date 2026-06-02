---
type: class
input_kind: lecture
status: sprout
created: 2026-05-08
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Streams]]"
  - "[[OCaml - Environments and Closures]]"
tags:
  - "#class"
  - "#Lecture"
next:
  - "[[10_Areas/UMN/Previous Classes/CSCI/CSCI 2021/Week - 7|Week - 7]]"
---
# Entire Week
## What you must be able to do
- Write `makeStream`, `first`, `rest`, and `take` from memory.
- Explain why a stream can act infinite without building the whole sequence: the tail is a function, not a prebuilt list.
- Trace `trim`, `scale`, and `sum` — know what state each keeps.
- Explain why streams require first-class functions (the next function lives inside the data).
- Explain how a closure simulates an object: group of functions sharing hidden state.
- Separate this course's closure-object simulation from full OCaml object syntax (Hickey Ch. 14).

## Key ideas (textbook)
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 3]]: functions are values, can be returned, stored inside other values. Streams depend on this directly.
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 2041/Textbook/Chapter - 3 & 4|Ch. 3]] scoping: closure behavior explains why a stream's next function remembers the state it needs.
- Hickey Ch. 14 `Objects`: lecture introduces object-style behavior *before* real object syntax. The closure simulation is smaller: encapsulate state by returning functions that see a hidden environment.

## Concepts created / updated today
- [[OCaml - Streams]]
- [[OCaml - Higher-Order Functions]]
- [[OCaml - Environments and Closures]]

## Lecture
### Week 6 lecture map - streams, closures, and the first mutation boundary
Week 6 is the hinge after the early recursion/tree material and before the interpreter arc. The main move is: OCaml functions are values, so they can be stored inside data structures and can remember environments. That one fact explains both stream objects and closure-based object simulation.

Source anchors:
- `Lecture - 13.txt` opens with streams: an object containing a function as a part, used to imitate an infinite series while only a finite portion is accessible.
- Professor notes `23Feb26/` and `Labs/lab5.ml` give the concrete stream API: `makeStream`, `first`, `rest`, `take`.
- `Lecture - 14.txt` frames object-oriented programming as a contrast case, then uses closures to simulate object-like state.
- Professor notes `25Feb26/` introduce OCaml variables/mutation vocabulary: `ref`, `:=`, and `!`. This is the conceptual entrance to later memoization and global interpreter state.

The week should be read as a sequence:
1. A stream is a finite object that carries a recipe for continuing.
2. The recipe is a function stored as data.
3. A closure can also hide state by remembering the environment where it was made.
4. OCaml mutation appears as a separate mechanism, useful but no longer purely applicative.

### Feb 23 — Streams and Functions Inside Data
Sources: `Lecture - 13.txt`, professor notes `23Feb26/`, `Labs/lab5.ml`, `Labs/tests5.ml`.

The lecture opens by naming the lab topic directly: streams. The professor's definition is practical rather than abstract: a stream is an object containing a function as one of its parts. Because OCaml functions are first-class objects, the course can build a data object whose next piece is computed by a function stored inside that same object.

The promise is not true infinity in memory. The stream only pretends to be an infinite series. At any moment the program can access a finite prefix, and the next element is produced by the `next` function when `rest` is called. That is why the `rest` function is the central mechanism, not a helper detail.

The stream representation in one line:
```ocaml
let makeStream this state next = ((this, state), next) ;;
```

A stream is a pair: `(current_value, state)` + a next function. The next function is called *only when rest is requested*. That's the whole trick — the stream isn't infinite in memory, it's a value with a recipe for continuing.

```ocaml
let first ((this, state), next) = this ;;
let rest ((this, state), next) = next this state ;;
```

`rest` calls the stored function. It doesn't read a prebuilt tail. This is why streams need first-class functions — the function *is* the data.

`take` bridges infinite idea to finite output:
```ocaml
let rec take count stream =
  match count
  with 0 -> [] |
       _ -> first stream :: take (count - 1) (rest stream) ;;
```

Each recursive step forces exactly one `rest`. No unbounded computation.

**Common mistake:** thinking state always equals the current value. In `naturals`, maybe. In `sum`, the state is *two streams* because computing the next sum requires advancing both inputs.

### Feb 25 — Objects with Functions as Parts
Sources: `Lecture - 14.txt`, professor notes `25Feb26/`, Hickey Ch. 14.

The professor frames this as an academic exercise: simulating object-based programming with function closures. The point is not that this is the best way to write objects in OCaml. The point is that closures can package behavior together with hidden environment, which is exactly the mechanism the later Lisp evaluator will reuse for user-defined functions.

The same lecture also begins the course's mutation vocabulary. `ref` creates a mutable reference cell, `:=` changes the cell, and `!` reads from the cell. This is the first clear boundary where the course steps outside pure applicative programming. That boundary matters later for memoization tables and for the Lisp evaluator's `global` environment.

If a function remembers the environment where it was created, then a group of functions can act like an object with private state. Same closure mechanism as lexical scoping — function carries code + environment.

**The useful contrast:**
- Stream: stores a function that computes the next cell.
- Closure-object: returns functions that remember hidden state.
- Later Lisp closure: stores parameters, body, and environment so a user-defined function runs later.

This is *not* OCaml classes. Hickey Ch. 14 covers real objects (encapsulation, `self`, subtyping). The lecture's version is smaller and more useful for the interpreter work later.

## Labs / Projects
### Lab 5 — Streams
Source: `Labs/lab5.ml` | Tests: `Labs/tests5.ml`

Tests the `((this, state), next)` representation. Main functions: `odds`, `trim`, `scale`, `sum`.
- `trim` skips a finite prefix without trying to build all naturals.
- `scale` maps a factor over a stream while preserving stream behavior.
- `sum` uses *two streams as state* and advances both.

Concepts: [[OCaml - Streams]], [[OCaml - Higher-Order Functions]]

## Examples worth keeping
- `makeStream this state next = ((this, state), next)` — whole representation in one line.
- `rest ((this, state), next) = next this state` — rest is computed by calling a stored function.
- `trim 5 naturals` — skips prefix without materializing infinity.
- `sum naturals byFives` — state is a pair of streams.

## Takeaways (questions to resolve)
- [ ] What exactly is stored in a stream cell? (value, state, next function)
- [ ] Why does `rest` call a function instead of reading a prebuilt tail?
- [ ] How does `take` prevent infinite computation? (bounded count)
- [ ] What state does `sum` keep? (two streams)
- [ ] How is closure-object different from full OCaml object syntax?

## Flashcards
#cards/CSCI2041
- What are the three parts of the course's stream representation::Current value, state, and a next function.
- Why can streams imitate infinite sequences::They compute the next cell only when `rest` is called — the tail is a function, not a prebuilt list.
- What does `rest` do in `lab5.ml`::Calls the stored next function on the current value and state, producing the next stream cell.
- Why do streams require first-class functions::The next-step function is stored *inside* the stream object as data.
- What is the state in `sum left right`::A pair of two streams, because computing the next sum requires advancing both.

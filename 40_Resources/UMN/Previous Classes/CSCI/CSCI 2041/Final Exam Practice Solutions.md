---
type: class
input_kind: exam-practice
status: sprout
created: 2026-05-12
updated: 2026-05-12
area:
  - "[[CSCI 2041 Board]]"
tags:
  - "#class"
  - "#exam"
next:
  - "[[Final Review Map]]"
---
Concept links: [[OCaml - Lisp Evaluator]], [[OCaml - Interpreter Primitives and Special Forms]], [[OCaml - Environments and Closures]], [[OCaml - Algebraic Data Types and Structural Recursion]], [[OCaml - Pattern Matching]], [[OCaml - Tail Recursion and Internal Helpers]].
## Solution 1
```ocaml
primitive "max"
  (fun args env ->

    (* Other arguments. *)

    let rec maxing args oldMax =
      match args with
      | Nil ->
          Number oldMax
      | Cons (arg, args) ->
          let newMax = evaluating arg env in
          (match newMax with
           | Number newMax ->
               if newMax > oldMax
               then maxing args newMax
               else maxing args oldMax
           | _ ->
               oops "MAX expected a number")
      | _ ->
          oops "Bad call to MAX"

    (* 1st argument. *)

    in
    match args with
    | Nil ->
        oops "MAX expected one or more arguments"
    | Cons (arg, args) ->
        (match evaluating arg env with
         | Number oldMax ->
             maxing args oldMax
         | _ ->
             oops "MAX expected a number")
    | _ ->
        oops "Bad call to MAX") ;;
```
A primitive receives the unevaluated Lisp argument list and the current environment. Therefore each argument must be evaluated explicitly with `evaluating arg env`. The first argument is handled separately because `max` needs at least one number. There is no identity value for the maximum of an empty argument list in this language, so `(max)` must call `oops`. After the first number becomes `oldMax`, `maxing` scans the rest of the Lisp list. Each remaining argument is evaluated, checked to be a `Number`, and compared against the current maximum. The recursive calls to `maxing` are tail calls because the call is the last action in both numeric branches.
## Solution 2
```ocaml
type 'a binaryTree =
  | Empty
  | Node of 'a * 'a binaryTree * 'a binaryTree ;;
```
The type is polymorphic because the tag can have any type, but all tags in one tree must share the same type. The recursive occurrences of `'a binaryTree` describe the left and right subtrees.

```ocaml
let rec mirror t =
  match t with
  | Empty ->
      Empty
  | Node (tag, left, right) ->
      Node (tag, mirror right, mirror left) ;;
```
This is structural recursion over a recursive algebraic data type. The empty tree has no subtrees to exchange. A node keeps the same tag, recursively mirrors both subtrees, and swaps their positions in the rebuilt node. This function returns a new tree. It does not mutate the old tree. That matters in OCaml: rebuilding recursive structure is the normal applicative pattern.
## Solution 3
```ocaml
let a = 1 ;;
let f b = a * b + 1 ;;
```
```ocaml
(* Type of f. *)
int -> int
```
The operators `*` and `+` are integer operators here. Since `a` is `1`, it has type `int`. The argument `b` must also be an `int`, and the result is an `int`.
```ocaml
f 2 ;;
```
```ocaml
- : int = 3
```
The calculation is:
```ocaml
1 * 2 + 1 = 3
```
```ocaml
let a = 2 in f 2 ;;
```
```ocaml
- : int = 3
```

The local `a = 2` does not change the `a` captured by `f`. OCaml uses lexical scoping, also called static binding. The value of a free name inside a function is determined by the environment where the function was defined, not by the environment where the function is later called.
The closure for `f` can be drawn like this:
```text
f
├─ parameter: b
├─ body: a * b + 1
└─ saved environment:
   └─ a ↦ 1
```
When `f 2` is called, the call supplies `b ↦ 2`, and the closure supplies `a ↦ 1`. So the body evaluates as `1 * 2 + 1`.
This is the same idea used later by the Lisp interpreter's `Closure (pars, body, env)`: a function carries code plus the environment needed to run that code.
## Solution 4
```ocaml
let rec notany h i =
  match i with
  | [] ->
      true
  | first :: rest ->
      if h first
      then false
      else notany h rest ;;
```
This calls `h` as few times as possible. If `h first` is true, the answer is immediately false, so the function stops without inspecting the rest of the list. If `h first` is false, the current element does not disprove the result, so the function continues with the rest of the list. The empty-list case returns `true`, because there is no element for which `h` returns true.
```ocaml
(* Type of notany. *)
(int -> bool) -> int list -> bool
```
The function `h` is applied to elements of the list, so it has type `int -> bool`. The list is therefore an `int list`, and the whole function returns a `bool`.
Tail-recursion answer:
```text
Yes. The only recursive call is notany h rest, and it is a tail call.
```
In the `then` branch there is no recursive call. In the `else` branch, the recursive call is the final action. There is no pending `&&`, `not`, cons operation, or arithmetic waiting after it returns.
## Solution 5
```ocaml
let findElement a e =
  let rec searching l r =
    if l <= r then
      let m = (l + r) / 2 in
      if e < a.(m) then
        searching l (m - 1)
      else if e > a.(m) then
        searching (m + 1) r
      else
        m
    else
      -1
  in
  searching 0 (Array.length a - 1) ;;
```
This is the applicative version of binary search. The imperative variables `l` and `r` become parameters of the internal helper `searching`. Updating `l` or `r` in the loop becomes calling `searching` with a smaller interval.
The invariant is:
```text
If e is still possible, then it is inside indexes l through r.
```
When `e < a.(m)`, the right side is too large, so the next interval is `l` through `m - 1`. When `e > a.(m)`, the left side is too small, so the next interval is `m + 1` through `r`. When neither comparison is true, `a.(m) = e`, so the function returns `m`. When `l > r`, the possible interval is empty, so the function returns `-1`.
```ocaml
(* Type of findElement. *)
int array -> int -> int
```

Tail-recursion answer:
```text
Both recursive calls to searching are tail calls.
```
In each branch, the recursive call is the last action. There is no work left to do after `searching l (m - 1)` or `searching (m + 1) r` returns. This is the direct replacement for the original `while` loop.
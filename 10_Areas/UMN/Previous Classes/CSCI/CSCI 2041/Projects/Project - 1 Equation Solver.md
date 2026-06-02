---
type: class
input_kind: project
status: sprout
created: 2026-05-08
updated: 2026-05-09
area:
  - "[[CSCI 2041 Board]]"
  - "[[OCaml - Expression Trees and Equation Solving]]"
  - "[[OCaml - Algebraic Data Types and Structural Recursion]]"
tags:
  - "#class"
  - "#project"
next:
---

# Project - 1 Equation Solver

## Project Goal
Represent equations as recursive OCaml trees, search for a target variable, and isolate it by applying inverse transformations. The skill tested is structural recursion over an ADT, not algebra by hand.

Links: [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 7]], [[Week - 15]], [[OCaml - Expression Trees and Equation Solving]], [[OCaml - Pattern Matching]], [[OCaml - Exceptions and Error Boundaries]].

## File Map
- `Labs/project-1/expression.ml`: defines the `expression` ADT. This is the clean data model source.
- `Labs/project-1/project.ml`: implements `expression` again, defines `SolvingError`, and implements `isInside`, `solver`, and `solve`.
- `Labs/project-1/modStack.ml`: support/example material for modules, signatures, mutable refs, and exceptions. It is not the equation solver itself, but it shows the same course pattern of an interface hiding helper implementation through `Stackish` and `Stack`.

## Data Model
The central type is:

```ocaml
type expression =
  Var of string
| Neg of expression
| Add of expression * expression
| Div of expression * expression
| Equ of expression * expression
| Mul of expression * expression
| Sub of expression * expression ;;
```

- `Var name`: a variable leaf, such as `x`.
- `Neg e`: unary negation.
- `Add (l, r)`, `Sub (l, r)`, `Mul (l, r)`, `Div (l, r)`: binary arithmetic nodes.
- `Equ (l, r)`: an equation node, used by `solve` as the top-level input and returned as the solved result.

The exception is:

```ocaml
exception SolvingError of string ;;
```

It carries a message explaining why solving cannot continue. That puts Project 1 directly under [[OCaml - Exceptions and Error Boundaries]].

## Main Functions
### `isInside`
`isInside name expr` answers whether `Var name` appears anywhere inside `expr`.

```ocaml
let rec isInside name expr =
  match expr with
  | Var x -> x = name
  | Neg e -> isInside name e
  | Add (l, r)
  | Sub (l, r)
  | Mul (l, r)
  | Div (l, r)
  | Equ (l, r) -> isInside name l || isInside name r ;;
```

This is pure structural recursion. Every recursive constructor either searches one child (`Neg`) or both children (`Add`, `Sub`, `Mul`, `Div`, `Equ`).

### `solver`
`solver name left right` assumes the variable is inside `left` and solves the equation `left = right` by peeling away the outer constructor of `left`.

Core cases:
- `Var x`: succeeds only if `x = name`, returning `Equ (left, right)`.
- `Neg b`: transforms `-b = right` into `b = -right`.
- `Add (a, b)`: if the variable is in `a`, solve `a = right - b`; if it is in `b`, solve `b = right - a`.
- `Sub (a, b)`: if the variable is in `a`, solve `a = right + b`; if it is in `b`, solve `b = a - right`.
- `Mul (a, b)`: if the variable is in `a`, solve `a = right / b`; if it is in `b`, solve `b = right / a`.
- `Div (a, b)`: if the variable is in `a`, solve `a = right * b`; if it is in `b`, solve `b = a / right`.
- `Equ (_, _)`: error, because `solver` expects the left side to be an expression being peeled, not a nested equation.

Representative branch:

```ocaml
| Add (a, b) ->
    if isInside name a then solver name a (Sub (right, b))
    else if isInside name b then solver name b (Sub (right, a))
    else raise (SolvingError "variable not found in either side of addition")
```

The pattern is always: find which child contains the variable, move the other child across the equality using the inverse operation, and recurse.

### `solve`
`solve name equation` is the public entry point. It accepts only `Equ (left, right)`.

It computes:
- `in_left = isInside name left`
- `in_right = isInside name right`

Then:
- variable only on the left: call `solver name left right`
- variable only on the right: call `solver name right left`
- variable on both sides: raise `SolvingError "variable appears on both sides of equation"`
- variable on neither side: raise `SolvingError "variable does not appear in equation"`
- input not an `Equ`: raise `SolvingError "solve expected an equation"`

## Control Flow
1. Input is an `expression`, expected to be `Equ (left, right)`.
2. `solve` checks which side contains the target variable.
3. `solve` chooses the variable-containing side as the side to isolate.
4. `solver` pattern matches on the outer operation around the variable.
5. `solver` applies the inverse transformation and recurses on the smaller variable-containing subexpression.
6. When the left side becomes `Var name`, the result is returned as `Equ (Var name, solved_right_side)`.

Example shape:

```ocaml
solve "x" (Equ (Add (Var "x", Var "b"), Var "c"))
```

should conceptually become:

```ocaml
Equ (Var "x", Sub (Var "c", Var "b"))
```

## Tests / Expected Behavior
No separate Project 1 test file was included in the requested project source set. The expected behavior is therefore read from `project.ml` itself and from the Week 7 project discussion:
- `solve` accepts only top-level `Equ` expressions.
- `isInside` must find variables under every constructor.
- `solver` must reduce the variable-containing side by one outer layer each recursive call.
- `SolvingError` is expected when the problem is not a one-variable-isolating equation.

Important error cases:
- left side reaches `Var x` where `x <> name`
- variable not found in the operation branch being solved
- nested `Equ` reaches `solver`
- input to `solve` is not `Equ`
- variable appears on both sides
- variable appears on neither side

## Concepts Used
- [[OCaml - Expression Trees and Equation Solving]]
- [[OCaml - Algebraic Data Types and Structural Recursion]]
- [[OCaml - Pattern Matching]]
- [[OCaml - Exceptions and Error Boundaries]]
- [[OCaml - Modules and Signatures]]
- [[OCaml - References and Mutation]]
- [[10_Areas/UMN/Previous Classes/CSCI/CSCI 4041/Week - 7]]
- [[Week - 15]]

## Common Mistakes
- Treating the equation like text instead of an `expression` tree.
- Forgetting to check both sides of `Add`, `Sub`, `Mul`, and `Div`.
- Using the same inverse rule for both sides of subtraction or division. `a - b = c` and `a / b = c` depend on whether the variable is in `a` or `b`.
- Letting `solver` accept nested `Equ` instead of raising an error.
- Not distinguishing "variable appears on both sides" from "variable absent."
- Returning a raw expression instead of a solved `Equ`.

## Representative Code
```ocaml
let solve name equation =
  match equation with
  | Equ (left, right) ->
      let in_left = isInside name left in
      let in_right = isInside name right in
      if in_left && not in_right then solver name left right
      else if in_right && not in_left then solver name right left
      else if in_left && in_right then
        raise (SolvingError "variable appears on both sides of equation")
      else
        raise (SolvingError "variable does not appear in equation")
  | _ ->
      raise (SolvingError "solve expected an equation") ;;
```

```ocaml
| Div (a, b) ->
    if isInside name a then solver name a (Mul (right, b))
    else if isInside name b then solver name b (Div (a, right))
    else raise (SolvingError "variable not found in either side of division")
```

## Study Checklist
- [ ] Can I write the `expression` type from memory?
- [ ] Can I explain why `Equ` belongs at the top of `solve` but is an error inside `solver`?
- [ ] Can I trace `isInside "x"` through every constructor?
- [ ] Can I state the inverse rule for `Neg`?
- [ ] Can I state both inverse rules for `Add`?
- [ ] Can I state both inverse rules for `Sub`?
- [ ] Can I state both inverse rules for `Mul`?
- [ ] Can I state both inverse rules for `Div`?
- [ ] Can I list every `SolvingError` situation?
- [ ] Can I connect this project to ADTs, pattern matching, and structural recursion on the final exam?

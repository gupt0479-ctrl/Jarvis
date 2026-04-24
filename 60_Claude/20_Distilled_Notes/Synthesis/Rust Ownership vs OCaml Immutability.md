---
type: evergreen
status: seed
created: 2026-04-25
updated: 2026-04-25
tags:
  - evergreen
  - synthesis
concepts:
  - "[[20_Progress/UROP/Learning/Rust Patterns in BOOM]]"
  - "[[60_Claude/20_Distilled_Notes/OCaml Pattern Matching]]"
tracks:
  - systems
  - algorithms
---

# Rust Ownership vs OCaml Immutability

Two type systems that prevent bugs at compile time, but through different mechanisms.

## The Core Difference

Rust prevents data races and use-after-free through **ownership and borrowing**. Every value has exactly one owner. References are either shared (`&T`, read-only) or exclusive (`&mut T`, write-only). The borrow checker enforces this at compile time.

OCaml prevents mutation bugs through **immutability by default**. Values don't change after creation. Pattern matching destructures data without modifying it. When you "update" a tree, you create a new tree that shares structure with the old one.

## Where They Converge

Both languages force you to think about data flow explicitly:
- In Rust, you ask: "Who owns this? Can I borrow it? Will it outlive the reference?"
- In OCaml, you ask: "What constructor is this? What does the recursive case return? Am I handling all variants?"

Both catch bugs that would be runtime errors in Python, Java, or Go. The compiler is the first line of defense, not unit tests.

## Where They Diverge

- Rust allows mutation but controls it. OCaml discourages mutation entirely.
- Rust's ownership model is designed for systems programming (memory layout, zero-cost abstractions, no GC). OCaml's immutability model is designed for correctness in recursive algorithms (structural sharing, pattern exhaustiveness).
- Rust errors are about lifetimes and borrows. OCaml errors are about exhaustiveness and type mismatches.

## Transfer Value

If you understand both, you can explain:
- Why immutability makes concurrent code safer (OCaml insight applied to Rust)
- Why explicit ownership prevents resource leaks (Rust insight applied to any language)
- Why pattern matching is more powerful than if-chains for case analysis (OCaml insight that Rust also uses via `match`)

## Diagnostic Question

Can you explain to an interviewer why Rust's `match` and OCaml's `match` look similar but enforce different guarantees?

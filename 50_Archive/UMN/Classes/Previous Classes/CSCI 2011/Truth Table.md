---
type: class
status: archived
created: 2025-09-24
updated: 2025-10-11
area:
  - "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2011/Chapter - 1]]"
  - "[[Finals]]"
tags:
  - "#class"
next: "[[50_Archive/UMN/Classes/Previous Classes/CSCI 2011/Chapter - 1]]"
---
Truth Tables are used to summarize the truth values of Propositions and their Connectives. Each row in a truth table represents a possible combination of truth values for the Propositions involved. 
**Identifying Propositions**: 
- Determine if a statement is a declarative statement that can be classified as true or false.
- Using Connectives: Use lowercase letters (P, Q, R, etc.) to represent Propositions. Form compound Propositions using Connectives: 
	- Negation: ¬P (not P)
	- Conjunction: P ∧ Q (P and Q)
	- Disjunction: P ∨ Q (P or Q)
- Constructing Truth Tables: 
	- For a single proposition P:
		- Create two rows: one for true (T) and one for false (F).
		- Show the truth values for ¬P.
	- For two Propositions P and Q:
		- Create 4 rows (2²) to represent all combinations of truth values (TT, TF, FT, FF).
		- Determine the truth values for P ∧ Q and P ∨ Q based on the definitions of Conjunction and Disjunction.
# Truth Tables
### Truth Table for →
The implication is false only when P is true and Q is false.
	True (T), True (T) → True (T)
	True (T), False (F) → False (F)
	False (F), True (T) → True (T)
	False (F), False (F) → True (T)
## Conditional Statements
Let p and q be propositions. The conditional statement p → q is the proposition “if p, then q.” The conditional statement p → q is false when p is true and q is false, and true otherwise. In the conditional statement p → q, p is called the **hypothesis** (or antecedent or premise) and q is called the **conclusion** (or consequence).
 A conditional statement is also called an **implication**.
 - **Number of Rows:** The number of rows in a truth table is determined by the number of propositional variables: $$\text{Rows} = 2^{\text{number of propositions}}$$ Each proposition can be true or false, so all combinations must be covered.
 - **Number of Columns**:
	 - One column for each propositional variable (e.g., P, Q, R).
	 - One column for each sub-expression within the compound proposition.
	 - One final column for the overall compound proposition result.
- **Order of Operations (Operator Precedence)**: Understanding and applying the correct order of logical operations (e.g., negation, conjunction, disjunction, implication) is crucial, especially when parentheses are absent.
- When negations appear, create a separate column for the negated variable before using it in compound expressions.
- Step-by-Step Instructions for Constructing a Truth Table:
	- Identify propositional variables: Create columns for each variable (e.g., P, Q, R).
	- Determine the number of rows: Calculate $(2^n)$ where (n) is the number of propositional variables.
	- Fill in truth values for propositional variables: For the first variable, alternate half the rows true and half false. For the second variable, alternate every quarter of rows, and so forth. The video suggests a specific pattern for ease of checking (e.g., grouping all true values first, then false).
	- Create columns for each sub-expression: Break down the compound proposition into parts and create columns for each intermediate expression. Evaluate sub-expressions row-by-row: Apply logical operators (AND, OR, NOT, IMPLICATION) according to precedence rules.
	- Calculate the final compound proposition column: Use the results of sub-expressions to determine the truth value of the entire expression.
	- Verify results: Double-check the truth values, especially for implications, which are true if either the hypothesis is false or both hypothesis and conclusion are true.
**Example 1**: $( (P \lor Q) \to \neg R )$
Columns: $$P, Q, R, (P \lor Q), (\neg R), ((P \lor Q) \to \neg R)$$
Number of variables: 3 → (2^3 = 8) rows
Steps: Fill in truth values for P, Q, R. Calculate $(P \lor Q)$ (true if either P or Q is true). Calculate $(\neg R)$ (negate R’s truth value). Calculate implication: true unless $(P \lor Q)$ is true and $(\neg R)$ is false.

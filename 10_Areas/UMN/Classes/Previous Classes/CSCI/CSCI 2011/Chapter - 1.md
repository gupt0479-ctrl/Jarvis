---
type: class
status: archived
created: 2025-09-24
updated: 2025-09-30
area:
  - "[[Main Examples]]"
  - "[[Finals]]"
  - "[[Material]]"
tags:
  - "#class"
  - "#Homework"
  - "#Discussion"
  - "#Textbook"
next: "[[Chapter - 2]]"
---
# #Textbook Textbook & Videos
## 1.1
### Propositions
A proposition is a declarative statement that can be either true or false. 
Examples: "The sky is blue" (true) and "The moon is made of cheese" (false).
Non-propositional statements include commands (e.g., "Sit down") and expressions with variables (e.g., "x + 1 = 2" without a specified value for x).
### Connectives
Connectives are operators used to form compound Propositions from simpler Propositions. The main Connectives discussed include:
1. **Negation (¬)**: The Negation of a proposition P is represented as "not P" (¬P).
2. **Conjunction (∧)**: The Conjunction of Propositions P and Q is represented as "P and Q" (P ∧ Q). This is true only if both P and Q are true.
3. **Disjunction (∨)**: The Disjunction of Propositions P and Q is represented as "P or Q" (P ∨ Q). This is true if *at least one* of P or Q is true.
	- Inclusive or - The one listed above
	- **The exclusive or** of p and q, denoted by p ⊕ q (or p XOR q), is the proposition that is true when exactly one of p and q is true and is false otherwise.
4. **Implication (→)**: An Implication is represented as "if P then Q" (P → Q). 
	- [[Truth Table#Truth Table for →|Truth Table for →]]: The implication is false only when P is true and Q is false.
	- **Converse**: Switch the order of P and Q (If Q then P).
	- **Inverse**: Negate both P and Q (If not P then not Q).
	- **Contrapositive**: Switch and negate (If not Q then not P). The Contrapositive always has the same truth value as the original implication.
		- **Finding Converse, Inverse, and Contrapositive**: Start by writing the implication in "if-then" form. Apply the definitions of Converse, Inverse, and Contrapositive to derive the new statements.
5. **[[Truth Table]]**
6. **Biconditional (↔)**: A biconditional is represented as "P if and only if Q" (P ↔ Q), which is true only if both Propositions share the same truth value. The Truth Table for Biconditionals shows that they are true when both propositions are either true or false.
7. **[[Truth Table#Conditional Statements|Conditional Statements]]**
## 1.2
### Propositional Logic
Atomic Propositions break down English sentences into basic, indivisible statements (atomic propositions). For example, in the sentence “I go to the store or the movies,” the atomic propositions might be:
- P: I go to the store
- Q: I go to the movies
- R: I do my homework
- Positive Representation of Propositions Always represent propositions positively. For negations, apply logical negation to the proposition rather than representing a proposition as negative from the start.
	Example: Instead of representing “I won’t do my homework” as a proposition, represent “I do my homework” as R and then negate it as ¬R.
- **Logical Connectives** Identify connectives such as: Negation (¬), Disjunction (∨, “or”), Conjunction (∧, “and”), Implication (→, “if-then”), 
- **Translating English to Logic**: Identify propositions (P, Q, R, etc.) Identify logical connectives in the sentence. Construct the propositional logic statement accordingly.
- Implication and **“If” Statements**: “If” statements are translated as implications: If hypothesis then conclusion (Hypothesis → Conclusion) 
	Example: “You can get a free sandwich on Thursday if you buy a sandwich or a cup of soup” translates to: (P ∨ Q) → R where P = buy a sandwich Q = buy a cup of soup R = get a free sandwich on Thursday.
- **“Only If” Statements**: Reverse the implication direction: “A only if B” translates to B → A
	Example: “You can get a free sandwich only if you buy a sandwich or a cup of soup” translates to: R → (P ∨ Q)
- [[Main Examples#Propositional Logic|Examples]]
### [[Main Examples]]
### Logic Gates
Logic circuits visually represent propositional logic statements. They break down complex logical tasks into elementary logic functions using logic gates. ![[Pasted image 20251023130412.png]]
1. **NOT gate (Inverter)**: Takes a single input and outputs its negation (NOT).
	- Symbol: a triangle with a small circle at the output.
2. **OR gate**: Takes two inputs and outputs the disjunction (OR) of the inputs.
	- Symbol: curved shape.
3. **AND gate**: Takes two inputs and outputs the conjunction (AND) of the inputs.
	- Symbol: straight-edged shape.
4. **Instructions for Constructing Logic Circuits**: Identify all variables and note which are negated. Insert NOT gates for each negated variable. Group variables connected by AND operations using AND gates. Combine groups connected by OR operations using OR gates. 
	- When drawing: Use the standard symbols for NOT, AND, and OR gates. Label inputs clearly. Optional: label outputs of gates for clarity. Focus on the structure of the circuit rather than artistic quality.
![[Pasted image 20251023130820.png]]
## 1.3
### Propositional Equivalences
Logical Operators and Analogies:
- **Disjunction (OR, $(\lor)$)**: Think of OR as addition (true = 1, false = 0). Result is true if at least one operand is true.
- **Conjunction (AND, $(\land)$)**: Think of AND as multiplication. Result is true only if both operands are true.
- **Negation (NOT, $(\neg)$)**: Flips truth values (true → false, false → true).
Types of Propositions:
- **Tautology**: Always true, e.g., $(P \lor \neg P)$.
- **Contradiction**: Always false, e.g., $(P \land \neg P$).
- **Contingency**: Neither always true nor always false, e.g., a simple proposition (P) which can be true or false depending on the case.
**Logical Equivalence**: Two compound propositions (P) and (Q) are logically equivalent if $(P \iff Q)$ is a tautology. Logical equivalence is denoted by a special symbol resembling an equal sign with an extra line.
1. Using Truth Tables to Prove Logical Equivalences:
	- Determine the number of propositions (variables) involved (e.g., (P), (Q), (R)).
	- Calculate the number of rows: (2^n) for (n) propositions.
	- Create columns for each proposition and fill in all possible truth value combinations.
	- Add columns for intermediate expressions (e.g., (\neg P), (P \land Q), etc.) needed to build towards the final compound propositions.
	- Calculate truth values for the compound propositions you want to compare.
	- Compare the final columns: If they are identical for all rows, the propositions are logically equivalent.
Detailed Examples Covered
*Example 1*: Show $( \neg P \lor Q \equiv P \to Q )$
Set up truth table with columns for $(P), (Q), (\neg P), (\neg P \lor Q), and (P \to Q)$.
Calculate each intermediate column. Compare final columns to confirm equivalence.
### Laws
Tautology and Contradiction: A tautology is a proposition that is always true. A contradiction is a proposition that is always false. These concepts are important when understanding logical equivalences.
1. Identity Laws: 
	- $( P \land \text{True} \equiv P )$
	- $( P \lor \text{False} \equiv P )$
2. Domination Laws:
	- $( P \lor \text{True} \equiv \text{True} )$
	- $( P \land \text{False} \equiv \text{False} )$
3. Idempotent Laws:
	- $( P \lor P \equiv P )$
	- $( P \land P \equiv P )$
4. Double Negation Law:
	- $( \neg(\neg P) \equiv P )$
5. Absorption Laws:
	- $( P \lor (P \land Q) \equiv P )$
	- $( P \land (P \lor Q) \equiv P )$
6. Negation Laws: 
	- $( P \lor \neg P \equiv \text{True} )$ (Tautology)
	- $( P \land \neg P \equiv \text{False} )$ (Contradiction)
7. Commutative Laws: Order of propositions does not matter for $( \land )$ and $( \lor )$.
8. Associative Laws: Grouping of propositions does not matter for $( \land )$ and $( \lor )$.
9. Distributive Laws:
	- $( P \lor (Q \land R) \equiv (P \lor Q) \land (P \lor R) )$
	- $( P \land (Q \lor R) \equiv (P \land Q) \lor (P \land R) )$
10. **De Morgan’s Laws**: These laws are especially important for negating compound propositions.
	- $( \neg (P \land Q) \equiv \neg P \lor \neg Q )$ 
	- $( \neg (P \lor Q) \equiv \neg P \land \neg Q )$
11. Conditional & Biconditional statements: ![[Pasted image 20251023133901.png]]
- Using Truth Tables to Show Equivalence: Truth tables show that two propositions are logically equivalent if their truth values match in every case. Additional Equivalences Involving Conditionals and Biconditionals, some equivalences involve conditional statements (if-then) and biconditional statements (if and only if). These do not have special names and must be written out explicitly in proofs.
## 1.4
### Predicates
Limitations of Propositional Logic: Propositional logic deals with fixed true/false statements but cannot model relationships involving variables, such as: “All candy made with chocolate is delicious.”. 
**Predicate logic** is introduced to handle these more complex relationships. Components of Predicate Logic:
- Variables: Symbols like ( x, y, z ) that represent elements from a domain.
- Predicates: Properties or relations involving variables, denoted as ( P(x) ), ( R(x ,y ,z) ), etc.
Examples include: ( x < 2 ), ( x + y = z )
A **propositional function** is a predicate with variables that becomes a proposition (a true or false statement) only when variables are assigned specific values.
1. Propositional Functions vs. Propositions:
	A propositional function, e.g., ( P(x) ), does not have a truth value until ( x ) is replaced by a **value from the domain**. Once variables are assigned values, the propositional function becomes a proposition with a definite truth value.
	- Propositional function: Contains variables, no truth value yet.
	- Proposition: Variables replaced by values or bound by quantifiers, has a truth value.
*Domain (Universe) of Discourse*: The set of all possible values variables can take, denoted as ( U ). Examples of domains include integers, real numbers, etc.
**Examples**:  Predicate R(x, y, z)  defined as ( x + y = z ).
Assigning values: ( R(2, -1, 5) ) is false since $( 2 + (-1) = 1 \neq 5 )$. 
	( R(3, 4, 7) ) is true since ( 3 + 4 = 7 ).
	( R(x, 3, z) ) remains a propositional function (not a proposition) because ( x ) and ( z ) are unassigned.
**Relation to Propositional Logic**: Predicate logic extends propositional logic. Logical connectives (and, or, not, etc.) apply similarly to propositions formed from propositional functions. Expressions with variables alone are not propositions and have no truth value until variables are assigned or quantified.
### Quantifiers
A propositional function $( P(x) )$ is not a proposition until it has a truth value. Previously, truth values were assigned by substituting specific values for x. Quantifiers allow us to form propositions without assigning specific values by expressing statements about all or some elements in the domain. 
- An element for which P(x) is false is called a **counterexample** to ∀xP(x)
![[Pasted image 20251023154229.png]]
1. **Universal Quantifier $((\forall))$**
	Symbol: $(\forall)$ (an upside-down “A”)
	*Meaning*: “For all x,  P(x) is true.”
	*Truth condition*: **$( \forall x P(x) )$ is true if P(x) is true for every x in the domain.**
	*To prove false*: find a counterexample, a single x in the domain for which P(x) is false.
	Examples: Domain = integers $( \mathbb{Z} ) ( P(x) = x > 0 )$ False because ( x = -3 ) is in the domain and ( -3 > 0 ) is false.
	Domain = positive integers ( P(x) = x > 0 ) True because all positive integers satisfy ( x > 0 ).
	- To prove true: show ( P(x) ) holds for every ( x ) in the domain.
	- To prove false: find a single counterexample ( x ) where ( P(x) ) is false.
2. **Existential Quantifier $((\exists))$**
	Symbol: $(\exists)$ (a backward “E”)
	*Meaning*: “There exists some ( x ) such that ( P(x) ) is true.”
	*Truth condition*: **$( \exists x P(x) )$ is true if there is at least one ( x ) in the domain for which ( P(x) ) is true.**
	*To prove false*: show ( P(x) ) is false for every ( x ) in the domain.
	Examples: Domain = integers ( P(x) = x > 0 ) True because ( x = 7 ) satisfies ( 7 > 0 ).
	Domain = negative integers ( P(x) = x > 0 ) False because no negative integer is greater than zero.
	- To prove true: find one example ( x ) where ( P(x) ) is true.
	- To prove false: show ( P(x) ) is false for all ( x ) in the domain (requires proof).
3. Relationship Between Quantifiers and Logical Connectives: Universal quantifier corresponds to a logical AND over all elements. Existential quantifier corresponds to a logical OR over elements. 
	- **For $( \forall x P(x) )$, all P(x) must be true. For $( \exists x P(x) )$, at least one P(x) must be true.**
4. **Uniqueness Quantifier $((\exists!))$**
	Meaning: “There exists exactly one ( x ) such that ( P(x) ) is true.”
	Examples:
	- P(x): 2x = 4 has exactly one integer solution ( x=2 ), so true.
	- P(x): 2x > 4 is true for many integers, so uniqueness is false.
	- P(x): 2x = 3 has no integer solution, so false.
	- Prove there is exactly one x such that P(x) is true.
	- Show existence and uniqueness (no other x satisfies P(x) ).
5. **Negating Quantified Statements**: Negation affects both the quantifier and the propositional function:
	  - **Negation of a universal quantifier: ¬(∀x P(x)) ≡ ∃x ¬P(x)**  
		 *Interpretation:* "Not every student has taken the course" means "There exists a student who has not taken the course."
	   - **Negation of an existential quantifier:  ¬(∃x P(x)) ≡ ∀x ¬P(x)** 
		 *Interpretation:* "There is no student who has taken the course" means "Every student has not taken the course." These equivalences reflect De Morgan’s laws for quantifiers.
6. [[Main Examples#Quantifiers|Examples]]
## 1.5
### Nested Quantifiers
Quantifiers such as “for all” (∀) and “there exists” (∃) can be nested to form complex logical statements.
	*Example*: “Every real number has an additive inverse” can be expressed as: ∀x ∈ ℝ, ∃y ∈ ℝ such that x + y = 0.
	The domain matters: 
		- When the domain is infinite (like all real numbers), proof involves reasoning rather than enumeration. 
		- When the domain is finite (e.g., {0,1,2}), one can check each element individually.
- **Order of Quantifiers**: Changing the order of nested quantifiers can affect the meaning of the statement.
	*Example*: ∀x ∀y, $x * y = y *$ x is true. ∀y ∀x, $x * y = y * x$ is also true.
		Statement 1: ∀x ∃y such that x + y = 5 — This is true because for any x, y = 5 - x works.
		Statement 2: ∃y ∀x such that x + y = 5 — This is false because there is no single y that works for all x.
- Truth Values of Statements with Quantifiers: To determine truth, either prove the statement or provide a counterexample. For “for all” statements, one counterexample is enough to prove falsehood. For “there exists” statements, one example is enough to prove truth. 
1. **Negation of Nested Quantifiers**: Negating a statement with nested quantifiers involves switching quantifiers and negating the predicate. Rule: 
	- **Negation of ∀x P(x) is ∃x ¬P(x).**
	- **Negation of ∃x P(x) is ∀x ¬P(x).**
	Example: Negate ∀x ∃y P(x,y) (where P(x,y) is x = -y). Negation is ∃x ∀y ¬P(x,y), meaning there exists some x such that for all y, x ≠ -y.
	- Evaluating Nested Quantifier Statements: Identify the domain of variables. Translate the quantified statement into an English sentence.
		- Determine if the statement is true by: Constructing a proof or reasoning. Finding counterexamples for “for all” statements.
		- Finding at least one example for “there exists” statements.
	- Checking Order of Quantifiers: Understand how swapping quantifiers affects the statement. Test truth value after swapping. 
	- Negating Nested Quantifiers: 
		- Step 1: Move negation inside and switch quantifiers.
		- Step 2: Negate the predicate.
		- Step 3: Interpret the resulting statement in plain English.
2. **Translating nested quantifiers**: English or to logical expressions 
	- Identifying the domain and variables: Replace vague phrases (e.g., “two positive integers”) with quantified variables (e.g., “for all positive integers (x) and (y)“).
	- Defining predicates Assign predicates to key properties or relations (e.g., (P(x,y)) = “x + y > 0”, (E(x,y)) = “x sent an email to y”).
	- Writing logical expressions using quantifiers: Use universal quantifiers ((\forall)) for “every” or “all” statements. Use existential quantifiers ((\exists)) for “there exists” statements. 
	- Combining quantifiers with logical connectives Use conjunctions $((\wedge))$, disjunctions $((\vee))$, implications $((\to))$, and biconditionals $((\leftrightarrow))$ to accurately reflect the meaning. Handling special cases Exclude cases like a person emailing themselves by adding conditions such as $(x \neq y)$.
	- [[Main Examples#Quantifiers|Nested Quantifiers Negation Examples]]
3. **Important Notes**: Clearly defining predicates before translating is essential. The order of quantifiers significantly affects the meaning of statements. Special cases, such as excluding self-relations (e.g., a student emailing themselves), must be handled carefully. Negation of nested quantifiers requires careful application of logical equivalences and laws.
## 1.6
### Rules of Inference Explained
- **Purpose of Rules of Inference** To build valid logical arguments where the premises logically imply the conclusion. A valid argument means if all premises are true, the conclusion must also be true (the argument forms a tautology).
- **Structure of an Argument**
    - Premises: A sequence of propositions $(P1, P2, …, P_{n})$.
    - Conclusion: A proposition Q.
    - Validity: Premises imply the conclusion (if premises are true, conclusion is true).
- **Notation**
    - Propositions represented by letters (P, Q, R, etc.).
    - “If P then Q” written as $( P \to Q )$.
    - Logical connectives: and $((\land)), or ((\lor)), not ((\neg)).$
    - Three dots (∴) mean “therefore”.
Each rule is presented with its logical form, example, and how to write it as a tautology (implication).
1. **Modus Ponens**
    - **Form:** If $( P \to Q )$ and P are true, then conclude Q.
    - **Example:** If it rains (P), then I need an umbrella (Q). It is raining (P). Therefore, I need an umbrella (Q).
    - **Tautology:** $((P \to Q) \land P \to Q)$.
2. **Modus Tollens**
    - **Form:** If $( P \to Q )$ and $( \neg Q )$ are true, then conclude $( \neg P )$.
    - Equivalent to: $( \neg Q \to \neg P )$.
    - **Tautology:** $((P \to Q) \land \neg Q \to \neg P)$.
3. **Hypothetical Syllogism**
    - **Form:** If $( P \to Q )$ and $( Q \to R )$ are true, then conclude $( P \to R )$.
    - Like transitive property of implication.
    - **Tautology:** $((P \to Q) \land (Q \to R) \to (P \to R))$.
4. **Disjunctive Syllogism**
    - **Form:** If $( P \lor Q )$ and $( \neg P )$ are true, then conclude  Q.
    - **Tautology:** $((P \lor Q) \land \neg P \to Q)$.
5. **Addition**
    - **Form:** If P is true, then conclude $( P \lor Q )$ is true.
    - **Tautology:** $(P \to (P \lor Q))$.
6. **Simplification**
    - **Form:** If $( P \land Q )$ is true, then conclude $( P ) (or ( Q ))$ is true.
    - **Tautology:** $((P \land Q) \to P) and ((P \land Q) \to Q)$.
7. **Conjunction**
    - **Form:** If ( P ) and ( Q ) are both true, then conclude $( P \land Q )$ is true.
    - **Tautology:** $(P \land Q \to (P \land Q))$ (trivial but named for proofs).
8. **Resolution**
    - **Form:** If $( \neg P \lor R ) and ( P \lor Q )$ are true, then conclude $( Q \lor R )$ is true.
    - Used to combine clauses and simplify arguments.
### Methodology for Constructing Valid Arguments
- Start with **premises** (known true statements).
- Apply rules of inference step-by-step to derive new true statements.
- Each step includes:
    - The statement derived.
    - The reason (which rule of inference was applied and which premises/statements were used).
- Continue until the **conclusion** is reached, showing the argument is valid.
### [[Main Examples#Rules of Inference|Example Walkthroughs]]
### Rules of Inference for Quantified Statements
- **Universal Instantiation (UI):** From a universally quantified statement $(∀x P(x))$, you can infer P(c) for any specific element c in the domain. 
	- _Example:_ From “All dogs are cute,” infer “Oliver is cute” if Oliver is a dog.
- **Universal Generalization (UG):** If P(c) is true for an arbitrary element c, then P(x) is true for all x in the domain.
- **Existential Instantiation (EI):** From an existentially quantified statement $(∃x P(x))$, you can infer P(c) for some specific element c in the domain.
- **Existential Generalization (EG):** If P(c) is true for some element c, then ∃x P(x) is true.
- **Modus Ponens (MP) for Quantified Statements:** If $∀x (P(x) → Q(x))$ and P(a) are true, then Q(a) is true.
- [[Main Examples#Rules of Inference for Nested Quantifiers|Examples for Rules of Inference for Nested Quantifiers]]
## Detailed Methodology / Steps for Constructing Valid Arguments with Quantified Statements
1. Define predicates for relevant properties and relations.
2. Translate natural language premises and conclusions into predicate logic with quantifiers.
3. Identify applicable rules of inference (UI, UG, EI, EG, MP).
4. Apply Universal Instantiation to move from general statements to specific instances.
5. Use Modus Ponens to derive conclusions from conditional statements and known facts.
6. Use Existential Instantiation to work with existential quantifiers by introducing a specific element.
7. Use conjunction and simplification to combine or separate statements as needed.
8. Use Existential Generalization to conclude existential statements from specific instances.
9. Verify that the conclusion matches the desired statement logically.
## 1.7
### Direct Proof
- **Direct Proof Methodology:**
    - Start by assuming the antecedent P is true.
    - Use definitions, axioms, and rules of inference to logically deduce that the consequent Q is true.
    - This proves the implication $( P \implies Q )$.
- **Difference Between Formal and Informal Direct Proofs:**
    - Formal proofs explicitly cite each axiom or inference rule used.
    - Informal proofs are more conversational but still logically valid.
- **Key Logical Structure:**
    - Identify the implication $( P \implies Q )$.
    - Assume P is true.
    - Show Q must follow.
- [[Main Examples#Direct Proof|Direct Proof Examples]]
### Proof by Contraposition
- It is an indirect proof method.
- Relies on the logical equivalence: **If P then Q** is logically equivalent to **If not Q then not P**.
- Instead of proving “P implies Q” directly, you prove “not Q implies not P”.
- This approach can sometimes simplify proofs by working with the contrapositive statement.
- [[Main Examples#Proof by Contraposition|Examples]]
#### Methodology
1. Identify the implication you want to prove: **If P then Q**.
2. Write down the contrapositive statement: **If not Q then not P**.
3. Assume **not Q** (the negation of the conclusion).
4. Using this assumption, prove **not P** (the negation of the premise).
5. Conclude that since **not Q implies not P** is true, the original statement **If P then Q** is true.
6. End the proof with a QED symbol or equivalent.
### Direct Proof vs Contraposition
- Direct proof assumes **P** is true and shows **Q** is true.
- Contraposition assumes **not Q** and shows **not P**.
## Proof by Contradiction
- **Proof by Contradiction Overview:**
    - Unlike direct proof (which assumes the proposition ( P ) is true), proof by contradiction assumes the **negation** of the proposition $((\neg P))$ is true.
    - The goal is to show this assumption leads to a logical contradiction.
    - The contradiction implies that $(\neg P)$ is false, so ( P ) must be true.
- **Two Types of Propositions:**
    1. **Single Proposition ( P ):**
        - Assume $(\neg P)$ and derive a contradiction.
        - Example: Proving $(\sqrt{2})$ is irrational.
    2. **Implication $( P \implies Q )$:**
        - Assume ( P ) and $(\neg Q)$ (i.e., (P) is true and (Q) is false).
        - Derive a contradiction to prove the implication.
        - This is related to the contrapositive proof: $(\neg Q \implies \neg P)$.
- [[Main Examples#Proof By Contradiction|Examples]]
## 1.8
### Proof by Cases (Proof by Exhaustion)
#### What is Proof by Cases?
- **Main idea**: Break down a problem into ALL possible scenarios and prove each one separately  
- **Why it works**: If you cover every single possibility and prove each case, then your overall statement must be true 
- **Key requirement**: Your cases must be **exhaustive** (cover everything) and **mutually exclusive** (no overlap)
- [[Main Examples#Proof by Cases|Examples]]
### Proving n ≤ n² for integers
**What we're proving**: If n is an integer, then n ≤ n²
**The three cases** (covers ALL integers):  
- **Case 1**: n ≤ -1 (all negative integers)  
- **Case 2**: n = 0 (just zero) 
- **Case 3**: n ≥ 1 (all positive integers)
**Why these cases work**: Negative numbers, zero, and positive numbers often behave differently in math. These three cases literally cover every single integer that exists!
**Proving each case**:
- **Case 1 (n ≤ -1)**: If n is negative and you square it, n² becomes positive. Negative number ≤ positive number ✓.
	- *Example*: -3 ≤ (-3)² = 9 ✓
- **Case 2 (n = 0)**: Direct substitution: 0 ≤ 0² = 0 ✓
- **Case 3 (n ≥ 1)**: If n ≥ 1, multiply both sides by n: n² ≥ n. This means n ≤ n² ✓.
	- *Example*: 5 ≤ 5² = 25 ✓
### Important Takeaways
- **Proof by cases requires careful selection of cases** to ensure they are mutually exclusive and collectively exhaustive.  
- For integers, dividing by sign (negative, zero, positive) or parity (even, odd) are common strategies.  
- **Proof by contradiction and contrapositive** are powerful tools especially when direct proofs are complex.  
- Using **propositional logic** helps clarify implications and negations in proofs.  
- The concept of **without loss of generality** simplifies proofs by reducing redundant cases.  
- Each proof method depends critically on the domain (integers here), highlighting the importance of clearly defining the domain.
### Proofs of Existence and Uniqueness

#### What Are Existence and Uniqueness Proofs?
- **Existence proofs**: Show that something exists (at least one example)  
- **Uniqueness proofs**: Show that only ONE thing exists that meets the criteria  
- These are super common in math - you'll see them everywhere!
### Existence Proofs: Constructive Proof
**The Strategy**: Just find one example that works and you're done!
**Example Problem**: Prove there exists a pair of consecutive integers where one is a perfect square and the other is a perfect cube.
**Professor X's Solution**: Make a table of squares and cubes:
- 1² = 1, 1³ = 1
- 2² = 4, 2³ = 8
- 3² = 9, 3³ = 27  
- Look for consecutive numbers: 8 and 9 are consecutive!  
- 8 = 2³ (perfect cube) and 9 = 3² (perfect square)
- **BOOM!** Found one example = proof complete
### Method 2: Non-Constructive Proof
**The Strategy**: Assume the opposite is true, then show that leads to a contradiction
**Example Problem**: Prove there exists a rational number X and irrational number Y such that X^Y is irrational.
**Professor X's Solution**: Assume NO such X and Y exist. Pick X = 4 (rational) and Y = √2 (irrational). Calculate 4^√2 - this turns out to be irrational. **Contradiction!** We just found an example, so our assumption was wrong. Therefore, such X and Y DO exist
### The Two-Step Process:
1. **Prove existence** (show at least one solution exists)
2. **Prove uniqueness** (show there can't be more than one)
**Example Problem**: If a and b are real numbers and a ≠ 0, prove there is a UNIQUE real number R such that aR + b = 0. 
- Step 1: Prove Existence: Let R = -b/a (we get this by solving aR + b = 0 for R). Check it works: a(-b/a) + b = -b + b = 0 ✓  
	- So R = -b/a is definitely a solution
- Step 2: Prove Uniqueness: Suppose there's another solution S where aS + b = 0. Since both work: aR + b = aS + b = 0. This means: aR + b = aS + b. Subtract b from both sides: aR = aS. Divide by a: R = S. 
	- **This proves R and S must be the same!** So there's only one solution

---
# #Homework Homework's (1 & 2)


---
# #Discussion Discussions (1 & 2)
## Discussion 1
### Material implication
- Definition: $p \to q \equiv \neg p \lor q$
- Truth pattern: **false only** when p is T and q is F.
- Useful reformulations:
    - $p \to q \equiv \neg q \to \neg p$ (contrapositive)
    - $p \to q \equiv \neg(p \land \neg q)$
### Questions
*20* [[Truth Table#Truth Table for →|Truth Table for if-then statements]]
*26 to 29* - [[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2011/Chapter - 1#Laws|laws]] 
*37* - [[Truth Table]]
*44* and *45* - **This is just fancy notation for initial value and till what value**
*52-54* - **NOR**
NOR is defined by: $p↓q$ is true if both p and q are false. $p \downarrow q \text{ is true iff both } p \text{ and } q \text{ are false.}$ $p↓q$ is true if both p and q are false. Equivalently: $$p \downarrow q \equiv \neg(p \lor q).$$
*52* – Truth table: Just encode “true only when both p and q are false.”

| p   | q   | $p \downarrow q$ |
| --- | --- | ---------------- |
| T   | T   | F                |
| T   | F   | F                |
| F   | T   | F                |
| F   | F   | T                |
*53* – Equivalence with $¬(p ∨ q)$: Directly from definition: since both have exactly the same truth pattern, they’re equivalent.
*54* – Showing {↓} is functionally complete: We show we can build ¬, ∨, ∧ from ↓.
1. **NOT from NOR**: $p \downarrow p \equiv \neg(p \lor p) \equiv \neg p.$
2. **OR from NOR**: Use NOR on $p \downarrow q$ with itself:
	- $p \downarrow q \equiv \neg(p \lor q)$
    - $(p \downarrow q) \downarrow (p \downarrow q) \equiv \neg\neg(p \lor q) \equiv p \lor q.$
3. **AND from NOR**  
    Use De Morgan: $p ∧ q \equiv \neg(\neg p \lor \neg q)$.
    - $¬p ≡ p \downarrow p$,
    - $¬q ≡ q \downarrow q$
    - OR of those via step (2),
    - then NOR that result with itself to negate it.
Once you can do ¬, ∨, and ∧, you can build every other standard connective, so **{↓} is functionally complete.**
## Discussion 2
*47* - Idea: every truth table can be turned into a **disjunctive normal form (DNF)**:
- For each row where the function is true, make a conjunction (AND) of literals matching that row.
- OR all those conjunctions.
Each literal is either a variable $p_i$​ or its negation $\neg p_i$, so the whole DNF uses only ¬, ∧, ∨.
Since **every** truth table has an equivalent DNF, any propositional function can be expressed using just ¬, ∧, ∨. 
Therefore ${\neg,\land,\lor}$ is functionally complete.


---

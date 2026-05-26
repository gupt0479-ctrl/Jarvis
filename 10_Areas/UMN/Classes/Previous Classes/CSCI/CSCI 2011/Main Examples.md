---
type: class
status: archived
created: 2025-12-09
updated: 2025-12-13
area:
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2011/Chapter - 1]]"
  - "[[Chapter - 2]]"
  - "[[Chapter - 4]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2011/Chapter - 5]]"
  - "[[10_Areas/UMN/Classes/Previous Classes/CSCI/CSCI 2011/Chapter - 6]]"
  - "[[Chapter - 7]]"
  - "[[Chapter - 9]]"
  - "[[Material]]"
  - "[[Chapter - 3]]"
  - "[[Chapter - 10]]"
tags:
  - "#class"
next: "[[Finals]]"
---
# Chapter 1 
## Propositional Logic
**Instructions for Translating English to Propositional Logic**: 
1. Identify atomic propositions in the English sentence and assign propositional variables (P, Q, R, etc.) to the positive forms of these statements.
2. Identify logical connectives in the sentence (negation, and, or, if-then, only if). 
3. Translate negations by negating the propositional variable (¬P), rather than representing the proposition itself as negative.
4. Construct the propositional logic statement by combining propositions with the appropriate logical connectives. For “if” statements, translate as implication: Hypothesis → Conclusion. For “only if” statements, reverse the implication: Conclusion → Hypothesis.
5. When translating logic back to English, substitute propositions with their English meanings and interpret connectives accordingly.
*Example of Translating Negation in Implication: Sentence*: “The automated reply can’t be sent when the system is full”
- Translation: If the system is full then the automated reply cannot be sent
- Logic: P → ¬Q where P = system is full Q = automated reply can be sent
*Translating Logic to English*: Given propositions and a logic statement, replace variables with their English meanings and interpret connectives to form a meaningful English sentence.
- Example: Given, Q = “you can ride the rollercoaster”
	- R = “you are under 4 feet tall”
	- S = “you are older than 16 years old” and the statement (R ∨ ¬S) → ¬Q
	- English translation is: “If you are under 4 feet tall or you are not older than 16 years old, then you cannot ride the rollercoaster.”
## Knights and Knaves Logic Puzzle
Scenario: On an island, knights always tell the truth and knaves always lie. Two individuals, A and B, make statements about each other: - A says: “B is a knight.” - B says: “The two of us are of opposite types.”
Goal: Determine who is a knight and who is a knave.
Logical Variables: - P = “A is a knight” - Q = “B is a knight”
Methodology: 
- Consider all four possibilities for P and Q. Use reasoning to eliminate inconsistent cases.
- Conclusion: Both A and B are knaves (P = false, Q = false).
- If the speaker is a knight, their statement must be true.
- If the speaker is a knave, their statement must be false.
- Eliminate inconsistent assignments until one remains.
1. Using a Truth Table to Solve Knights and Knaves Puzzle: Construct a truth table with all combinations of P and Q. Evaluate the truth of each statement under each combination. Identify which combination satisfies both statements simultaneously. The truth table confirms the reasoning result that both are knaves.
	- Find the row where all statements align with the speaker’s identity
## Party Invitation Logic Puzzle
Scenario: Planning a party with three sensitive friends: Jasmine (J), Samir (S), and Conti (K). Each has conditions on attendance: - If Jasmine attends, Samir will not attend (J → ¬S). - Samir will only attend if Conti attends (S → K). - Conti will only attend if Jasmine attends (K → J).
Goal: Determine possible attendance combinations that satisfy all conditions.
Methodology: 
- Represent each condition as an implication statement. - Construct a truth table with all possible attendance combinations for J, S, and K. - For each row, check if all implications hold true. - Eliminate rows that violate any implication.
- Assign propositional variables to each person’s attendance. Translate each attendance condition into an implication:
	- J → ¬S
	- S → K
	- K → J
- Results: Valid attendance combinations are: - Jasmine and Conti attend, Samir does not (J = true, S = false, K = true) - Jasmine attends alone (J = true, S = false, K = false) - No one attends (J = false, S = false, K = false)
1. General Approach to Logic Puzzles in Discrete Math: Define propositional variables for key statements. Translate verbal statements into logical expressions (implications, conjunctions, negations). Use logical reasoning or truth tables to test all possibilities. Identify consistent solutions that satisfy all conditions.
	- Evaluate each implication.
	- Mark rows that violate any implication as invalid.
	- The remaining rows represent valid attendance combinations.
## Law Usage Examples
Constructing Logical Equivalences: Using known equivalences and laws to build new equivalences step-by-step.
Two Methods to Prove Logical Equivalence:
1. Truth Tables: Create columns for propositions and their negations. Compute intermediate compound propositions stepwise. Compare final columns to verify equivalence. 
2. **Two-Column Proofs Using Logical Laws**: Start with one side of the equivalence. Apply known logical laws to transform the expression stepwise. Continue until the expression matches the other side of the equivalence. Write down each transformation and the law used.
3. Key Logical Laws Used:
	1. De Morgan’s Laws: Negation of a disjunction becomes a conjunction of negations. Negation of a conjunction becomes a disjunction of negations.
	2. Double Negation Law: Negating a negation returns the original proposition.
	3. Distributive Law: Distributes conjunction over disjunction or vice versa.
	4. Commutative Law: Order of propositions in conjunction or disjunction can be swapped.
	5. Identity Law: Disjunction with false leaves the other proposition unchanged.
	6. Domination Law: Disjunction with true is always true.
	7. Negation Law: A proposition or its negation is always true (tautology).
	8. Implication Rewrite: “If P then Q” is equivalent to “not P or Q”.
**Example Walkthroughs**: Proving that ¬(P ∧ Q) ≡ ¬P ∨ ¬Q using truth tables and stepwise logical laws (De Morgan’s Law, double negation, distributive law, etc.).
Showing that the implication (P ∧ Q) → (P ∨ Q) is a tautology by rewriting it and applying the laws. A practice example proving ¬¬P ∨ Q ≡ ¬Q ∧ P using De Morgan’s law, double negation, and commutative law.
4. Instructions for Constructing Logical Equivalences: 
	1. Using Logical Laws in a Two-Column:
		- **Proof**: Write the original expression on the left side. Aim to transform it into the target expression on the right side. Apply one logical law per step, writing the resulting expression and naming the law used. Repeat until the expression matches the target.
5. **Verifying Tautologies**: Rewrite implications as disjunctions using the implication rewrite law. Use De Morgan’s laws and negation laws to simplify. Rearrange using commutative and associative laws. Identify tautologies using negation and domination laws.
## Quantifiers 
1. Translating English Statements to Logical Form: Define propositional functions clearly (e.g., H(x): “x is honest”). Specify the domain/universe of discourse (e.g., all politicians, all students). Translate English quantifiers into logical quantifiers accordingly.
	*Example*: - “All Americans eat cheeseburgers” → ∀x C(x), where C(x): “x eats cheeseburgers.” Negation: ¬(∀x C(x)) → ∃x ¬C(x) → “There exists an American who does not eat cheeseburgers.”
	- **Impact of Domain on Translation**: The domain significantly influences how a statement is translated.
		*Example*: - “Some student in this class has visited Mexico.” - Domain = students in this class: ∃x M(x), where M(x): “x has visited Mexico.” - Domain = all people: Need to specify student status as well. Use two propositional functions: - M(x): “x has visited Mexico” - C(x): “x is a student in this class” Statement: ∃x (M(x) ∧ C(x)).
	- *Importance of Parentheses* and Binding Variables: Parentheses ensure the correct scope of quantifiers and propositional functions. Every variable must be bound by a quantifier or assigned a value for the expression to have a truth value. 
	- More Complex Translations: When the domain is larger (e.g., all people), statements often require conditional (if-then) forms.
		*Example*: “For all people, if the person is a student in this class, then they have visited Canada or Mexico.” Logical form: ∀x (S(x) → (M(x) ∨ C(x))) where - S(x): “x is a student in this class” - M(x): “x has visited Mexico” - C(x): “x has visited Canada”
	- When domain is complex or larger, use conjunctions (AND) or implications (IF-THEN) to restrict the domain or conditions.
2. Truth Values of Statements with Quantifiers: To determine truth, either prove the statement or provide a counterexample. For “for all” statements, one counterexample is enough to prove falsehood. For “there exists” statements, one example is enough to prove truth. 
3. **Negating nested quantifiers**: Apply negation step-by-step, pushing negation inside quantifiers by switching $(\forall)$ to $(\exists)$ and vice versa. Use De Morgan’s laws to distribute negations over logical connectives. Interpreting complex logical expressions Break down expressions into parts, interpret the meaning of each predicate and quantifier, and then reconstruct the English sentence. 
	- *Examples* Translations Presented: 
		- Sum of two positive integers is always positive $[ \forall x \forall y ((x > 0 \wedge y > 0) \to (x + y > 0)) ]$
			- Every student in the class sent an email to Joe $[ \forall x (x \neq \text{Joe} \to E(x, \text{Joe})) ]$
			- There exists a student who has not received any text or email from any other student $[ \exists y \forall x ((x \neq y) \to (\neg E(x,y) \wedge \neg T(x,y))) ]$
		- All students use TikTok or have a friend who uses TikTok $[ \forall x (T(x) \vee \exists y (T(y) \wedge F(x,y))) ]$ 
			- There exist two distinct students who have taken exactly the same classes $[ \exists x \exists y (x \neq y \wedge \forall z (S(x,z) \leftrightarrow S(y,z))) ]$
		- There exists a man who has taken a flight on every airline $[ \exists m \forall a \exists f (P(m,f) \wedge Q(f,a)) ]$
			- Negation of the above statement $[ \forall m \exists a \forall f (\neg P(m,f) \vee \neg Q(f,a)) ]$
## Rules of Inference
### 1. Simple Modus Ponens Example
- **Premises:** $( P ), ( P \to Q )$.
- **Conclusion:** Use modus ponens to conclude ( Q ).
### 2. Intermediate Example with Negations
- **Premises:** $( P ), ( P \to \neg Q ), ( \neg Q \to \neg R )$.
- **Goal:** Show $( \neg R )$.
- **Steps:**
    - Use modus ponens on ( P ) and $( P \to \neg Q )$ to get $( \neg Q )$.
    - Use modus ponens on $( \neg Q )$ and $( \neg Q \to \neg R )$ to get $( \neg R )$.
### 3. Complex Example with Multiple Premises
- **Premises:**
    - $( (P \land T) \to (R \lor S) )$, $( Q \to (U \land T) )$, $( U \to P )$, $( \neg S ),( Q )$.
- **Goal:** Show $( Q \to R )$.
- **Steps:**
    - Apply modus ponens, simplification, conjunction, and disjunctive syllogism to reach the conclusion.
## Rules of Inference for Nested Quantifiers
### Translating Natural Language to Predicate Logic
- Define predicates to represent properties or relations, for example:
    - D(x): x is a dog - “Oliver is a dog” → D(O)
    - F(x): x has four legs - “Every dog has four legs” → $∀x (D(x) → F(x))$
    - B(x): x read the book - “A student in discrete math hasn’t read the book” → $∃x (D(x) ∧ ¬B(x))$
    - P(x): x passed the class - “Everyone in discrete math passed the class” → $∀x (D(x) → P(x))$
    - D(x): x is a student in discrete math - Conclusion: $∃x (P(x) ∧ ¬B(x))$
- Express premises and conclusions using quantifiers and predicates, for example:
### 3. Constructing Valid Arguments Using Rules of Inference
#### Example 1: Oliver has four legs
**Premises:** - ∀x (D(x) → F(x)) - D(o) (Oliver is a dog)
**Steps:** - Use UI on premise 1: D(o) → F(o) - Given D(o), use Modus Ponens to conclude F(o)
**Conclusion:** Oliver has four legs.
#### Example 2: Someone who passed discrete math has not read the book
**Premises:** - $∃x (D(x) ∧ ¬B(x))$ (There exists a student who hasn’t read the book) - $∀x (D(x) → P(x))$ (Everyone in discrete math passed).
**Goal:** $∃x (P(x) ∧ ¬B(x))$ (There exists a student who passed but hasn’t read the book)
**Steps:** - Use EI on premise:
1. $D(a) ∧ ¬B(a)$ for some specific a - Simplify to get D(a) and ¬B(a) separately - Use UI on premise
2. $D(a) → P(a)$ - Use Modus Ponens with D(a) to get P(a) - Conjoin P(a) and ¬B(a) - Use EG to conclude $∃x (P(x) ∧ ¬B(x))$.
## Direct Proof
### Important Definitions Used in Proofs
- **Even Integer:** An integer ( n ) is even if it can be expressed as $[ n = 2k ]$ where ( k ) is an integer.
- **Odd Integer:** An integer ( n ) is odd if it can be expressed as $[ n = 2k + 1 ]$ where ( k ) is an integer.
#### Example 1: Prove “If ( n ) is odd, then ( n^2 ) is odd”
**Proof Steps:**
1. Assume n is odd, so $n = 2k + 1$ for some integer ( k ).
2. Square both sides: $[ n^2 = (2k + 1)^2 = 4k^2 + 4k + 1 ]$
3. Factor out 2 from the first two terms: $[ n^2 = 2(2k^2 + 2k) + 1 ]$
4. Since ( 2k^2 + 2k ) is an integer (call it ( r )), rewrite as: $[ n^2 = 2r + 1 ]$
5. This matches the definition of an odd integer, so $( n^2 )$ is odd.
**Conclusion:** Therefore, $( n^2 )$ is odd.
#### Example 2: Prove “The sum of two even integers is even”
**Proof Steps:**
1. Express the statement as an implication: If ( A ) and ( B ) are even integers, then (A + B) is even.
2. Assume ( A ) and ( B ) are even: $[ A = 2k, \quad B = 2m ]$ where ( k, m ) are integers.
3. Add the two: $[ A + B = 2k + 2m = 2(k + m) ]$
4. Since ( k + m ) is an integer (call it ( r )), rewrite as: $[ A + B = 2r ]$
5. This matches the definition of an even integer, so the sum is even.
**Conclusion:** Therefore, (A + B) is even.
## Proof by Contraposition
### Example 1
- **Statement:** If _n_ is odd (P), then _3n + 2_ is odd (Q).
- **Contrapositive:** If _3n + 2_ is not odd (i.e., even) (not Q), then _n_ is not odd (i.e., even) (not P).
- **Proof steps:**
    - Assume _n_ is even → _n = 2k_ for some integer _k_.
    - Substitute into _3n + 2_: $3(2k) + 2 = 6k + 2 = 2(3k + 1)$, which is even.
    - Thus, not Q implies not P.
    - Therefore, the original statement is true.
### Example 2 (Exercise for the viewer)
- **Statement:** If _n_ is even (P), then _3n + 2_ is even (Q).
- **Contrapositive:** If _3n + 2_ is not even (i.e., odd) (not Q), then _n_ is not even (i.e., odd) (not P).
- **Proof steps:**
    - Assume _n_ is odd → _n = 2k + 1_.
    - Substitute into _3n + 2_: $3(2k + 1) + 2 = 6k + 3 + 2 = 6k + 5$.
    - Express _6k + 5_ as _2(3k + 2) + 1_, which is odd.
    - Thus, not Q implies not P.
    - Hence, the original statement is true.
## Proof By Contradiction
### Proof by Contradiction for a Single Proposition
**Example:** Prove $(\sqrt{2})$ is irrational.
- **Step 1:** Assume the negation: $(\sqrt{2})$ is rational.
- **Step 2:** By definition of rational numbers,$(\sqrt{2} = \frac{a}{b})$, where (a, b) are integers with no common factors and $(b \neq 0)$.
- **Step 3:** Square both sides: $[ 2 = \frac{a^2}{b^2} \implies 2b^2 = a^2 ]$
- **Step 4:** From $(a^2 = 2b^2)$, conclude $(a^2)$ is even, so (a) must be even.
- **Step 5:** Write (a = 2c) for some integer (c).
- **Step 6:** Substitute back: $[ 2b^2 = (2c)^2 = 4c^2 \implies b^2 = 2c^2 ]$
- **Step 7:** Similarly, $(b^2)$ is even, so (b) is even.
- **Step 8:** Since both (a) and (b) are even, they share a common factor of 2, contradicting the assumption that (a/b) was in simplest form.
- **Conclusion:** The assumption that $(\sqrt{2})$ is rational leads to contradiction, so $(\sqrt{2})$ is irrational.
### Proof by Contradiction for an Implication $(P \implies Q)$
**Example:** Prove that if (3n + 2) is even, then (n) is even, where (n) is an integer.
- **Step 1:** Assume (P): (3n + 2) is even.
- **Step 2:** Assume $(\neg Q)$: (n) is odd.
- **Step 3:** Since (3n + 2) is even, subtract 2 (even) from it:$[ 3n = (3n + 2) - 2 ]$ So (3n) is even.
- **Step 4:** Consider (3n - n = 2n).
- **Step 5:** Since (n) is odd, (3n - n = 2n) should be odd (difference of even and odd), but (2n) is always even.
- **Step 6:** This contradiction shows the assumption that (n) is odd is false.
- **Conclusion:** If (3n + 2) is even, then (n) must be even.
## Proof by Cases
### Example 1: Proving n² + 3n + 2 is always even
**What we're proving**: If n is an integer, then n² + 3n + 2 is even
**The cases** (based on **parity** - even/odd): 
- **Case 1**: n is even  
- **Case 2**: n = 0 (zero is neither even nor odd)  
- **Case 3**: n is odd
**Proving each case**:
1. **Case 1 (n is even)**: If n is even, then n = 2k for some integer k. Substitute: $(2k)² + 3(2k) + 2 = 4k² + 6k + 2$. Factor out 2: $2(2k² + 3k + 1)$. 
	- Since it's 2 times something, it's even ✓
2. **Case 2 (n = 0)**: Direct substitution: 0² + 3(0) + 2 = 2  
	- 2 is even ✓
3. **Case 3 (n is odd)**: If n is odd, then n = 2m + 1 for some integer m. Substitute: $(2m + 1)² + 3(2m + 1) + 2$. Expand: $4m² + 4m + 1 + 6m + 3 + 2 = 4m² + 10m + 6$. Factor out 2: $2(2m² + 5m + 3)$
	- Since it's 2 times something, it's even ✓
### Example 2: The Complex One (Using Contradiction + Cases)
**What we're proving**: If $x·y$ is even AND x + y is even, then both x and y are even
**Setting up with logic**: P = "$x·y$ is even", Q = "x + y is even", R = "both x and y are even", We want to prove: (P AND Q) → R.
**Proof by contradiction approach**:
- Assume R is FALSE (so at least one of x or y is odd)  
- Show that this leads to either P being false OR Q being false  
- This contradicts our assumption that both P and Q are true
**The cases for when R is false**:
- **Case 1**: Both x and y are odd  
- **Case 2**: x is odd, y is even  
- **Case 3**: x is even, y is odd  
- ~~Case 4~~: Both x and y are even (this is R being true, so we exclude it)
**Without Loss of Generality (WLOG)**: Cases 2 and 3 will give the same result (just swap x and y). So, we can assume x is odd and only prove cases 1 and 2. This saves time without losing mathematical rigor!
**Proving the cases**:
1. **Case 1 (both x and y odd)**: $x = 2m + 1, y = 2n + 1$
	- $x·y = (2m + 1)(2n + 1) = 4mn + 2m + 2n + 1 = 2(2mn + m + n) + 1 → ODD$
	- Since $x·y$ is odd, P is false ✓
	- We found our contradiction!
2. **Case 2 (x odd, y even)**: $x = 2m + 1, y = 2n$
	- $x·y = (2m + 1)(2n) = 4mn + 2n = 2(2mn + n) → EVEN$
	- $x + y = (2m + 1) + 2n = 2m + 2n + 1 = 2(m + n) + 1 → ODD$
	- Since x + y is odd, Q is false ✓  
	- We found our contradiction! 
# Chapter 2
## Set Operations
**Given**: A = {a,e,i,o,u} and B = "discrete math" = {d,i,s,c,r,e,t,e,m,a,t,h} = {d,i,s,c,r,e,t,m,a,h}
- **A ∪ B**: {a,e,i,o,u,d,s,c,r,t,m,h} (everything from both sets)  
- **A ∩ B**: {a,e,i} (only letters that appear in both)  
- **A - B**: {o,u} (vowels not in "discrete math")  
- **B - A**: {d,s,c,r,t,m,h} (letters in "discrete math" that aren't vowels)  
- **Complement of (A ∩ B)**: All alphabet letters except a, e, i  
- **Is A ⊆ B?**: NO, because o and u are in A but not in B
*Note*: Always check if sets are written in roster notation (list form) vs set-builder notation. Remember that duplicates are only counted once in unions. The universe (U) matters for complements. 
## Set Identities
1. **De Morgan's Law**:
	- Universe U = {1, 2, 3, 4}
	- Set A = {1, 2}
	- Set B = {2, 3}
	For first law:
		- A ∪ B = {1, 2, 3}
		- (A ∪ B)' = {4}
		- A' = {3, 4}, B' = {1, 4}
		- A' ∩ B' = {4} ✓ They match!
	For second law:
		- A ∩ B = {2}
		- (A ∩ B)' = {1, 3, 4}
		- A' ∪ B' = {3, 4} ∪ {1, 4} = {1, 3, 4} ✓ They match!
### Proving methods
**Method 1: ## Subset Proof (Two-Direction Proof)**
1. **Proving (A ∩ B)' ⊆ A' ∪ B'**:
	- Start by assuming x ∈ (A ∩ B)'  
	- This means x ∉ (A ∩ B) by definition of complement  
	- By definition of intersection: x ∉ (A ∩ B) means ¬(x ∈ A ∧ x ∈ B)  
	- Apply De Morgan's Law for propositional logic: ¬(x ∈ A ∧ x ∈ B) = (x ∉ A ∨ x ∉ B)  
	- Rewrite using complement notation: x ∈ A' ∨ x ∈ B'  
	- By definition of union: x ∈ A' ∪ B'  
	- Therefore: (A ∩ B)' ⊆ A' ∪ B'
2. **Proving A' ∪ B ⊆ (A ∩ B)'**:
	- Start by assuming x ∈ A' ∪ B'  
	- By definition of union: x ∈ A' ∨ x ∈ B'  
	- By definition of complement: x ∉ A ∨ x ∉ B  
	- Rewrite using negation: ¬(x ∈ A) ∨ ¬(x ∈ B)  
	- Apply De Morgan's Law for propositional logic: ¬(x ∈ A ∧ x ∈ B)  
	- By definition of intersection: ¬(x ∈ A ∩ B) = x ∉ (A ∩ B)  
	- By definition of complement: x ∈ (A ∩ B)'  
	- Therefore: A' ∪ B' ⊆ (A ∩ B)'
**Method 2: Set-Builder Notation with Propositional Logic**
**This method rewrites everything using set-builder notation and applies logical rules**. Step-by-Step Transformation:
- (A ∩ B)' = {x | x ∉ (A ∩ B)} (definition of complement)  
- = {x | ¬(x ∈ A ∩ B)} (definition of ∉ symbol) 
- = {x | ¬(x ∈ A ∧ x ∈ B)} (definition of intersection)  
- = {x | ¬(x ∈ A) ∨ ¬(x ∈ B)} (De Morgan's Law for propositional logic)  
- = {x | x ∉ A ∨ x ∉ B} (definition of negation)  
- = {x | x ∈ A' ∨ x ∈ B'} (definition of complement) 
- = {x | x ∈ A' ∪ B'} (definition of union) 
- = A' ∪ B'
**Method 3: Truth table(Best)**:
- **A∩B column:** Only 1 when both A and B are 1 (intersection needs both)  
- **(A∩B)' column:** Opposite of A∩B column (complement flips everything)  
- **A' column:** Opposite of A column  
- **B' column:** Opposite of B column  
- **A'∪B' column:** 1 if either A' OR B' is 1 (union needs at least one)
The Magic Moment: **The (A∩B)' column and A'∪B' column are IDENTICAL!**
- Both columns show: 0, 1, 1, 1
- This proves the identity is true!
## Functions
### Practice Problem 1: Discrete Function
**Given:** X = {0, 1, 2, 3}, Y = {a, b, c}, f(0) = c, f(1) = b, f(2) = b, f(3) = c
**Is it one-to-one?**
- NO! Because b is hit by both 1 and 2. Also c is hit by both 0 and 3  
- Multiple inputs giving same output = not one-to-one
**Is it onto?** 
- NO! Because 'a' is lonely - nothing maps to it. Range = {b, c} but codomain = {a, b, c}  
- Missing elements in codomain = not onto
### Practice Problem 2: f(x) = x² from Integers to Integers
**Is it one-to-one?**  
- NO! Take a = 2 and b = -2  
- f(2) = 4 and f(-2) = 4  
- Same output from different inputs = not one-to-one. Positive and negative numbers always give same square!
**Is it onto?**
- NO! Can you ever get -1 by squaring an integer?  
- Nope! Squares are always non-negative  
- Negative integers in codomain are lonely = not onto
**Key Insight:**  
- When dealing with infinite sets, look for counterexamples  
- For one-to-one: find two different inputs with same output  
- For onto: find an output that's impossible to achieve
### Inverse Functions
**Example 1 - Not Invertible:** Function f: {a,b,c} → {1,2,3,4} where f(a)=1, f(b)=3, f(c)=4. 
- This is NOT onto because element 2 in the codomain isn't mapped to by anything. 
- Since it's not a bijection, it's NOT invertible
**Example 2 - Invertible:** Function f: integers → integers where f(x) = x + 3. 
- **Checking one-to-one**: If f(a) = f(b), then a+3 = b+3, so a = b ✓  
- **Checking onto**: For any integer y, we can find x = y-3 that maps to it ✓. 
	- Since it's a bijection, it IS invertible  
- **Finding the inverse**: Replace f(x) with y, swap x and y, solve for y
	- y = x + 3 → x = y + 3 → y = x - 3
	- So f⁻¹(x) = x - 3 (subtracts 3 to undo the adding 3)
### Floor and Ceiling Function Questions
**Function**: f(x) = ⌊x²/2⌋ for x ∈ {0, 1, 2, 3}
- **f(0)**:
	- 0² ÷ 2 = 0 ÷ 2 = 0
	- ⌊0⌋ = 0
- **f(1)**:
	- 1² ÷ 2 = 1 ÷ 2 = 0.5
	- ⌊0.5⌋ = 0 (rounds down)
- **f(2)**:
	- 2² ÷ 2 = 4 ÷ 2 = 2
	- ⌊2⌋ = 2
- **f(3)**:
	- 3² ÷ 2 = 9 ÷ 2 = 4.5
	- ⌊4.5⌋ = 4 (rounds down)
**Final answer**: {0, 0, 2, 4}
## Sequences
### Example 1: Given a = 5, d = 2
- Explicit formula: a_n = 5 + 2n  
- First five terms:
- a_0 = 5 + 2(0) = 5
- a_1 = 5 + 2(1) = 7
- a_2 = 5 + 2(2) = 9
- a_3 = 5 + 2(3) = 11
- a_4 = 5 + 2(4) = 13
### Example 2: Find a and d from sequence 7, 4, 1, -2...
- First term a = 7  
- Common difference d = 4 - 7 = -3 (subtract any term from the next one)  
- Check: 1 - 4 = -3 ✓, -2 - 1 = -3 ✓  
- Explicit formula: a_n = 7 + (-3)n = 7 - 3n
### Example 1: Given a = 4, r = 3
- Explicit formula: a_n = 4 × 3^n  
- First five terms:
- a_0 = 4 × 3^0 = 4 × 1 = 4
- a_1 = 4 × 3^1 = 4 × 3 = 12
- a_2 = 4 × 3^2 = 4 × 9 = 36
- a_3 = 4 × 3^3 = 4 × 27 = 108
- a_4 = 4 × 3^4 = 4 × 81 = 324
### Example 2: Find a and r from sequence 3, 3/2, 3/4, 3/8...
- First term a = 3  
- Common ratio r = (3/2) ÷ 3 = (3/2) × (1/3) = 1/2  
- Check: (3/4) ÷ (3/2) = 1/2 ✓  
- Explicit formula: a_n = 3 × (1/2)^n  
- When r is between 0 and 1, the sequence decreases!
### Recurrence Relations and Iterations
#### Example 1
**Given**: a(n) = a(n-1) + 2×a(n-2) for n ≥ 2, with a₀ = 2 and a₁ = 5
- **Finding a₂**: a₂ = a₁ + 2×a₀ = 5 + 2×2 = 5 + 4 = 9  
- **Finding a₃**: a₃ = a₂ + 2×a₁ = 9 + 2×5 = 9 + 10 = 19  
- **Finding a₄**: a₄ = a₃ + 2×a₂ = 19 + 2×9 = 19 + 18 = 37  
- **Sequence**: 2, 5, 9, 19, 37, ...
#### Simple Arithmetic Example
**Given**: a(n) = a(n-1) + 6 for n ≥ 1, with a₀ = 3
- **Finding terms**:
	- a₁ = 3 + 6 = 9
	- a₂ = 9 + 6 = 15
	- a₃ = 15 + 6 = 21  
- **Pattern**: This is just an arithmetic sequence! (adding 6 each time)  
    - **Closed form**: a(n) = 3 + 6n
### Iterations Method (Finding Closed Forms)
#### Method 1: Bottom-Up Approach
Start with initial condition and work forward  
Look for patterns in how terms are built  
**Example**: Starting with a₀ = 2, adding 3 each time:
- a₁ = 2 + 3 = 2 + 1×3
- a₂ = 2 + 3 + 3 = 2 + 2×3
- a₃ = 2 + 3 + 3 + 3 = 2 + 3×3
- **Pattern**: a(n) = 2 + n×3
#### Method 2: Top-Down Substitution
Start with the recurrence equation and substitute backwards  
**Example**: a(n) = a(n-1) + 3
- Substitute: a(n) = [a(n-2) + 3] + 3 = a(n-2) + 2×3
- Keep going: a(n) = [a(n-3) + 3] + 2×3 = a(n-3) + 3×3
- **Pattern**: a(n) = a(n-n) + n×3 = a₀ + 3n = 2 + 3n
### Sigma Questions
#### Example 1: Writing in Sigma Notation
**Problem**: Express the sum of first 100 terms where $a_i = 1/i$
**Step 1**: Figure out what the sequence looks like  
- a_1 = 1/1, a_2 = 1/2, a_3 = 1/3, ..., a_100 = 1/100
**Step 2**: Write as regular addition  
- 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/100
**Step 3**: Convert to sigma notation  
- Σ (from i=1 to 100) of 1/i  
- **Key**: The "i" in the formula (1/i) matches the "i" in the limits!
#### Example 2: Calculating Values
**Problem 1**: Find Σ (from i=5 to 9) of i²
**Solution**: 
-  i=5: 5² = 25  
- i=6: 6² = 36  
- i=7: 7² = 49  
- i=8: 8² = 64 
- i=9: 9² = 81  
- **Sum**: 25 + 36 + 49 + 64 + 81 = 255
**Problem 2**: Find Σ (from i=7 to 10) of (-1)^i
**Solution**:  
- i=7: (-1)⁷ = -1  
- i=8: (-1)⁸ = +1  
- i=9: (-1)⁹ = -1  
- i=10: (-1)¹⁰ = +1  
- **Sum**: -1 + 1 + (-1) + 1 = 0
#### Summation Properties examples
**Problem**: Σₖ₌₀⁷ (2×3^k + 5×2^k)
**Step 1**: Split using sum property
- = Σₖ₌₀⁷ (2×3^k) + Σₖ₌₀⁷ (5×2^k)
**Step 2**: Apply geometric formula to each part
_First part_: a=2, r=3, n=7
- 2(3^8 - 1)/(3-1) = 2(6561-1)/2 = 6560
_Second part_: a=5, r=2, n=7
- 5(2^8 - 1)/(2-1) = 5(256-1)/1 = 1275
**Step 3**: Add results
- 6560 + 1275 = 7835
# Chapter 3
## Searching Algorithm Practice Problem
**Looking for 22 in this ordered list**: some numbers with 22 in 8th position
**Linear Search approach:** 
- Check position 1: not 22  
- Check position 2: not 22  
- Keep going... position 8: found 22!  
- **Answer**: 8
**Binary Search approach:**  
- Left = 1, Right = 10  
- Middle = floor((1+10)/2) = 5  
- 22 > value at position 5, so eliminate positions 1-5  
- New range: Left = 6, Right = 10  
- Middle = floor((6+10)/2) = 8  
- Check position 8: found 22!  
- **Answer**: 8
## Bubble Sort Algorithm Practice 
### Step-by-Step Example (Starting with: 4, 3, 5, 2, 1):
**Pass 1:**  
• Compare 4 & 3 → Wrong order → Switch → (3, 4, 5, 2, 1)  
• Compare 4 & 5 → Correct order → No switch → (3, 4, 5, 2, 1)  
• Compare 5 & 2 → Wrong order → Switch → (3, 4, 2, 5, 1)  
• Compare 5 & 1 → Wrong order → Switch → (3, 4, 2, 1, 5)
**Pass 2:**  
• Compare 3 & 4 → Correct → No switch  
• Compare 4 & 2 → Wrong → Switch → (3, 2, 4, 1, 5)  
• Compare 4 & 1 → Wrong → Switch → (3, 2, 1, 4, 5)  
• Compare 4 & 5 → Correct → No switch
**Pass 3:**  
• Compare 3 & 2 → Wrong → Switch → (2, 3, 1, 4, 5)  
• Compare 3 & 1 → Wrong → Switch → (2, 1, 3, 4, 5)  
• Compare 3 & 4 → Correct → No switch  
• Compare 4 & 5 → Correct → No switch
**Pass 4:**  
• Compare 2 & 1 → Wrong → Switch → (1, 2, 3, 4, 5)  
• All other comparisons are correct!
**Result**: Took 4 passes total - not super efficient but definitely effective!
### Pseudocode Structure:
**Input**: List with at least 2 values (if only 1 value, no sorting needed!)  
**Process**:
- For i from 1 to n-1
	- For j from 1 to n-i
		- Compare adjacent values
	- If first > second, then interchange them  
	    - **Output**: Values in increasing order
### Bubble Sort Solution:
**Pass 1:**  
• 42 vs 19 → Wrong → (19, 42, 32, 11, 8, 1)  
• 42 vs 32 → Wrong → (19, 32, 42, 11, 8, 1)  
• 42 vs 11 → Wrong → (19, 32, 11, 42, 8, 1)  
• 42 vs 8 → Wrong → (19, 32, 11, 8, 42, 1)  
• 42 vs 1 → Wrong → (19, 32, 11, 8, 1, 42)  
• **42 is now in correct final position!**
**Pass 2:**  
• 19 vs 32 → Correct → No change  
• 32 vs 11 → Wrong → (19, 11, 32, 8, 1, 42)  
• 32 vs 8 → Wrong → (19, 11, 8, 32, 1, 42)  
• 32 vs 1 → Wrong → (19, 11, 8, 1, 32, 42)  
• 32 vs 42 → Correct → No change  
• **32 is now in correct position!**
**Pass 3:**  
• 19 vs 11 → Wrong → (11, 19, 8, 1, 32, 42)  
• 19 vs 8 → Wrong → (11, 8, 19, 1, 32, 42)  
• 19 vs 1 → Wrong → (11, 8, 1, 19, 32, 42)  
• **19 is now in correct position!**
**Pass 4:**  
• 11 vs 8 → Wrong → (8, 11, 1, 19, 32, 42)  
• 11 vs 1 → Wrong → (8, 1, 11, 19, 32, 42)  
• **11 is now in correct position!**
**Pass 5:**  
• 8 vs 1 → Wrong → (1, 8, 11, 19, 32, 42)  
• **Final answer!**
## Insertion Sort Algorithm Practice problem
### Step-by-Step Example (Starting with: 4, 3, 5, 2, 1):
**Pass 1:**  
• Look at 3, compare to 4 → Place correctly → (3, 4, 5, 2, 1)
**Pass 2:**  
• Look at 5, compare to 3 and 4 → Already in right spot → (3, 4, 5, 2, 1)
**Pass 3:**  
• Look at 2, find where it goes in (3, 4, 5) → Goes at beginning → (2, 3, 4, 5, 1)
**Pass 4:**  
• Look at 1, find where it goes in (2, 3, 4, 5) → Goes at very beginning → (1, 2, 3, 4, 5)
### Pseudocode Structure:
**Input**: List with 2 or more values  
**Process**:
- For j = 2 to n (starting with second element)
- Starting at i = 1
- Compare current element to all previous elements
- Find correct position and insert  
    • **Output**: Values in increasing order
### Detailed Practice Example
Professor X gave us this killer example: **42, 19, 32, 11, 8, 1**
### Insertion Sort Solution:
**Pass 1:**  
• Take 19, compare to 42 → Place before → (19, 42, 32, 11, 8, 1)
**Pass 2:**  
• Take 32, compare to 19 and 42 → Place between → (19, 32, 42, 11, 8, 1)
**Pass 3:**  
• Take 11, compare to all previous → Place at beginning → (11, 19, 32, 42, 8, 1)
**Pass 4:**  
• Take 8, compare to all previous → Place at beginning → (8, 11, 19, 32, 42, 1)
**Pass 5:**  
• Take 1, compare to all previous → Place at beginning → (1, 8, 11, 19, 32, 42)  
• **Final answer!**
## Greedy Algorithm Examples
### Example 1: Making Change (The 97 Cents Problem)
**The Problem**: You owe someone 97 cents. You could give them 97 pennies, but that's annoying!
**The Greedy Strategy**: Always use the largest coin that doesn't exceed the remaining amount
**Step-by-step breakdown**:  
• Start with 97 cents  
• Step 1: Give a quarter (25¢) → 97 - 25 = 72 cents left  
• Step 2: Give another quarter → 72 - 25 = 47 cents left  
• Step 3: Give another quarter → 47 - 25 = 22 cents left  
• Step 4: Can't give quarter (25¢ > 22¢), so give a dime → 22 - 10 = 12 cents left  
• Step 5: Give another dime → 12 - 10 = 2 cents left  
• Step 6: Skip nickels (5¢ > 2¢), give a penny → 2 - 1 = 1 cent left  
• Step 7: Give final penny → 1 - 1 = 0 cents left
**Final change given**: 3 quarters + 2 dimes + 2 pennies = 97 cents
#### Pseudocode for Making Change
• **Setup**: Coins arranged by denomination (C₁ = highest value, like quarters)  
• **Process**: For each coin type, give as many as possible without exceeding remaining amount  
• **Loop**: Continue through all denominations until change is complete  
• **Count**: Track total number of coins given
### Example 2: Course Scheduling Problem
**The Problem**: Schedule as many classes as possible in one room, where no two classes can overlap (but one can start when another ends)
**Wrong Strategies**:  
• Picking classes that start earliest ❌  
• Picking shortest classes first ❌
**Correct Greedy Strategy**: Always pick the class with the **earliest end time**
**Example**:  
• Math 101: 9:30 AM - 10:45 AM  
• Math 205: 9:00 AM - 11:00 AM  
• **Choose Math 101** because it ends at 10:45 AM (earlier than 11:00 AM)  
• This leaves more room for additional classes later!
#### Why Earliest End Time Works
• **Logic**: Classes that end early free up the room sooner  
• **Benefit**: More opportunities to schedule additional classes  
• **Compatibility**: Next class can start exactly when previous one ends
#### Pseudocode for Course Scheduling
• **Input**: List of classes with start and end times  
• **Sort**: Arrange by earliest end times first  
• **Select**: Pick first class (earliest end time)  
• **Continue**: Add compatible classes (no time conflicts)  
• **Output**: Maximum set of scheduled classes
# Chapter 4
## Division Algorithm
### Example 1: Does 4 divide 21?
• Set up: 21 = 4×q + r  
• Calculate: 21 ÷ 4 = 5 remainder 1  
• Answer: 21 = 4×5 + 1  
• Since r = 1 ≠ 0, we know 4∤21
### Example 2: Does 7 divide 18?
• Set up: 18 = 7×q + r  
• Calculate: 18 ÷ 7 = 2 remainder 4  
• Answer: 18 = 7×2 + 4  
• **Quotient notation**: q = 18 ÷ 7 = 2  
• **Remainder notation**: r = 18 mod 7 = 4
### Example 4: Zero case (0 ÷ 14)
• Set up: 0 = 14×q + r  
• Answer: 0 = 14×0 + 0  
• **Quotient**: q = 0 ÷ 14 = 0  
• **Remainder**: r = 0 mod 14 = 0
## Arithmetic Rules
### Example 1: 7 + 11 (mod 5)
**Method 1** (do arithmetic first):  7 + 11 = 18 
- 18 ÷ 5 = 3 remainder 3  
- So 18 ≡ 3 (mod 5)
**Method 2** (use the theorem): 7 ≡ 2 (mod 5) and 11 ≡ 1 (mod 5)  
- So 7 + 11 ≡ 2 + 1 ≡ 3 (mod 5)
### Example 2: 7 × 11 (mod 5)
**Method 1**:  7 × 11 = 77  
- 77 ÷ 5 = 15 remainder 2. So 77 ≡ 2 (mod 5)
**Method 2**: 7 ≡ 2 (mod 5) and 11 ≡ 1 (mod 5)  
- So 7 × 11 ≡ 2 × 1 ≡ 2 (mod 5)
# Chapter 5
## Mathematical Induction: Summation
### Example 1: Sum Formula (1 + 2 + 3 + ... + n = n(n+1)/2)
**What we're proving**: P(n) = "1 + 2 + 3 + ... + n = n(n+1)/2"
**Basis Step**: P(1): 
- Left side: 1
- Right side: 1(1+1)/2 = 1(2)/2 = 1
- 1 = 1 ✓ TRUE!
**Inductive Step**: **Assume**: 1 + 2 + 3 + ... + k = k(k+1)/2  
**Must Show**: 1 + 2 + 3 + ... + k + (k+1) = (k+1)(k+2)/2
**The Proof**:  
• Start with: 1 + 2 + 3 + ... + k = k(k+1)/2  
• Add (k+1) to both sides: 1 + 2 + 3 + ... + k + (k+1) = k(k+1)/2 + (k+1)  
• Factor the right side: k(k+1)/2 + 2(k+1)/2 = (k+1)(k+2)/2  
• This matches what we wanted to show! ✓
### Example 2: Powers of 2 (1 + 2 + 2² + ... + 2ⁿ = 2ⁿ⁺¹ - 1)
**What we're proving**: P(n) = "1 + 2 + 2² + ... + 2ⁿ = 2ⁿ⁺¹ - 1"
**Important**: This starts at n = 0 (non-negative integers), so first term is 2⁰ = 1
**Basis Step**: P(0)  
• Left side: 2⁰ = 1  
• Right side: 2⁰⁺¹ - 1 = 2¹ - 1 = 2 - 1 = 1  
• 1 = 1 ✓ TRUE!
**Inductive Step**:  
• **Assume**: 1 + 2 + 2² + ... + 2ᵏ = 2ᵏ⁺¹ - 1  
• **Must Show**: 1 + 2 + 2² + ... + 2ᵏ + 2ᵏ⁺¹ = 2ᵏ⁺² - 1
**The Proof**:  
• Start with assumption and add 2ᵏ⁺¹ to both sides  
• Right side becomes: (2ᵏ⁺¹ - 1) + 2ᵏ⁺¹ = 2·2ᵏ⁺¹ - 1 = 2ᵏ⁺² - 1  
• This matches what we wanted! ✓
### Example 3: Sum of First n Odd Integers
**Finding the Pattern First**:  
• n = 1: sum = 1 = 1²  
• n = 2: sum = 1 + 3 = 4 = 2²  
• n = 3: sum = 1 + 3 + 5 = 9 = 3²  
• n = 4: sum = 1 + 3 + 5 + 7 = 16 = 4²
**Pattern**: The nth odd integer is 2n - 1, and the sum equals n²
**What we're proving**: P(n) = "1 + 3 + 5 + ... + (2n-1) = n²"
**Basis Step**: P(1)  
• Left side: 1  
• Right side: 1² = 1  
• 1 = 1 ✓ TRUE!
**Inductive Step**:  
• **Assume**: 1 + 3 + 5 + ... + (2k-1) = k²  
• **Must Show**: 1 + 3 + 5 + ... + (2k-1) + (2k+1) = (k+1)²
**The Proof**:  
• Start with assumption and add the next odd number (2k+1)  
• Right side: k² + (2k+1) = k² + 2k + 1 = (k+1)²  
• This matches what we wanted! ✓
## Recursive Definition Examples
### Example 1: F(0) = 2, F(n+1) = 3F(n) - 1
• **Starting point**: F(0) = 2  
• **Rule**: Multiply previous term by 3, then subtract 1  
• **Calculations**:
- F(1) = 3(2) - 1 = 5
- F(2) = 3(5) - 1 = 14
- F(3) = 3(14) - 1 = 41
- F(4) = 3(41) - 1 = 122
### Example 2: Powers $(a^n)$
**Basis step**: a^0 = 1  
**Recursive step**: $a^n = a^{(n-1)} × a$ for n ≥ 1  
**Pattern**: Each power is the previous power multiplied by a
### Example 3: Sequence $a_n = 2n + 1$
**First, find the pattern**:
- a_0 = 1, a_1 = 3, a_2 = 5, a_3 = 7, a_4 = 9
- Pattern: Add 2 each time!  
    • **Recursive definition**:
- Basis: a_0 = 1
- Recursive: $a_n = a_{(n-1)} + 2$ for n ≥ 1
# Chapter 6
## PNC Practice Examples
### Example 1: Poker Hands (COMBINATION)
• **Question**: How many 5-card poker hands from 52 cards?  
• **Why combination?** You don't care if you get the King first or last - just that you have it!  
• **Solution**: C(52,5) = 52!/(47! × 5!)  
• **Calculation**:
- Numerator: 52 × 51 × 50 × 49 × 48 = 311,875,200
- Denominator: 5! = 120
- Answer: **2,598,960 different poker hands**
### Example 2: Marathon Runners (PERMUTATION)
• **Question**: 100 runners, how many ways for 1st, 2nd, 3rd place?  
• **Why permutation?** 1st place ≠ 3rd place - order totally matters!  
• **Solution**: P(100,3) = 100!/(100-3)! = 100!/97!  
• **Calculation**: 100 × 99 × 98 = **970,200 ways**
## Counting Rules and Combinatorics Practice
### Basic Bit String Problems
**What are bit strings?**  
- Binary strings using only 0s and 1s  
- Each position can have exactly 2 choices (0 or 1)
**Problem 1: How many bit strings of length 6 are there?**  
- Use multiplication rule: 2 choices × 2 choices × 2 choices × 2 choices × 2 choices × 2 choices  
- Answer: 2^6 = 64 different bit strings
**Problem 2: How many bit strings of length 6 start with 1 OR end with 1?**  
- This is trickier because of the word "OR" - need inclusion-exclusion principle  
- Set A = strings starting with 1  
- Set B = strings ending with 1  
- Some strings can be in BOTH sets (start AND end with 1)  
- Formula: |A ∪ B| = |A| + |B| - |A ∩ B|
Breaking it down: Strings starting with 1: Fix first position as 1, remaining 5 positions have 2 choices each = 2^5 = 32.  
- Strings ending with 1: Fix last position as 1, remaining 5 positions have 2 choices each = 2^5 = 32  
- Strings starting AND ending with 1: Fix first and last as 1, middle 4 positions have 2 choices each = 2^4 = 16  
- Final answer: 32 + 32 - 16 = 48
**Problem 3: How many bit strings of length n (not counting empty string)?**  
- Total bit strings of length n = 2^n  
- Empty string = all zeros (only 1 such string)  
- Answer: 2^n - 1
### License Plate Problems
**Douglas County License Plates: 3 letters + 3 digits**  
- 26 choices for each letter position  
- 10 choices for each digit position  
- Total: 26^3 × 10^3 = 17,576,000 unique plates
**Modified version: No zero as first digit**  
- First digit now has only 9 choices (1-9)  
- Other positions unchanged  
- Total: 26^3 × 9 × 10^2 = 15,818,400 unique plates
### Subset Counting Proof
**Proving: Number of subsets of set S = 2^|S|**
Example verification:  
- If S = {0, 1}, then |S| = 2  
- Subsets: {}, {0}, {1}, {0,1} = 4 subsets  
- 2^2 = 4 ✓
**General proof concept:**  
- For each element in S, it's either IN a subset or NOT IN a subset  
- That's 2 choices per element  
- With |S| elements, total combinations = 2^|S|
### Cartesian Product
**If |A₁| = 7 and |A₂| = 4, how many elements in A₁ × A₂?**  
- Each ordered pair (a,b) where a ∈ A₁ and b ∈ A₂  
- 7 choices for first element × 4 choices for second element  
- Answer: 7 × 4 = 28 ordered pairs
### Password Problems
**Password rules: 5-6 characters, at least 1 digit, rest are digits or lowercase letters**
Strategy: Use complement counting  
- Total possibilities - (possibilities with no digits)  
- 36 total characters (26 letters + 10 digits)
For 5-character passwords:
- All possibilities: 36^5  
- No digits (letters only): 26^5
- With at least 1 digit: 36^5 - 26^5 = 48,584,000
For 6-character passwords: With at least 1 digit: 36^6 - 26^6 = 1,867,866,560
Total passwords: 48,584,000 + 1,867,866,560 = 1,916,450,560
### Wedding Party Arrangements
**Problem 1: 8 people (bride, groom, 6 wedding party), bride and groom must be adjacent** 
- Treat bride-groom as one unit  
- Now arranging 7 units: 7!  
- Bride and groom can be in 2 orders within their unit  
- Answer: 2 × 7! = 10,080
**Problem 2: 4 couples, each couple adjacent, bride left of groom**  
- Arrange 4 couple-units: 4!
- 3 couples can be in either order: 2^3  
- Bride-groom order is fixed
- Answer: 4! × 2^3 = 192
### Advanced Permutation Problem
**4-permutations of integers 1-100 with 3 consecutive integers in correct order**
This is super complex:  
- 98 ways to choose 3 consecutive integers (1,2,3 through 98,99,100)  
- 97 remaining numbers for the 4th position  
- 2 ways to arrange (consecutive block at start or end) But we double-counted cases with 4 consecutive integers.
- Answer: 2 × 98 × 97 - 97 = 18,915
### Committee Selection
**5 men, 6 women, committee of 4 with at least 1 of each gender**  
- Total ways to choose 4 from 11: C(11,4)  
- Subtract all-women committees: C(6,4)  
- Subtract all-men committees: C(5,4)  
- Answer: C(11,4) - C(6,4) - C(5,4) = 330 - 15 - 5 = 310
### Diagonal Counting
**Diagonals in a convex hexagon**  
- From each vertex, can draw diagonals to non-adjacent vertices  
- Each vertex connects to n-3 others (can't connect to itself or 2 adjacent)  
- For hexagon: each vertex has 6-3 = 3 diagonals  
- Total if counting from all vertices: 6 × 3 = 18  
- But each diagonal counted twice (once from each end)  
- Answer: 18 ÷ 2 = 9 diagonals
**General formula for n-sided polygon:** Number of diagonals = n(n-3)/2
This formula works because:
- n vertices each connect to (n-3) others
- Divide by 2 since each diagonal counted twice
## Binomial Theorem and Pascal's Triangle
### Real Example: (3x + 2)^3
• **Setup**: Use the formula with first term = 3x, second term = 2, n = 3  
• **Term 1**: 3 choose 0 × (3x)^3 × 2^0 = 1 × 27x^3 × 1 = 27x^3  
• **Term 2**: 3 choose 1 × (3x)^2 × 2^1 = 3 × 9x^2 × 2 = 54x^2  
• **Term 3**: 3 choose 2 × (3x)^1 × 2^2 = 3 × 3x × 4 = 36x  
• **Term 4**: 3 choose 3 × (3x)^0 × 2^3 = 1 × 1 × 8 = 8  
• **Final answer**: 27x^3 + 54x^2 + 36x + 8
### Finding Specific Coefficients (The Big Payoff!)
• **The Challenge**: Find the coefficient of x^62 in (3x + 2)^100  
• **The Strategy**:
- We want the power of x to be 62
- In the general term: (3x)^(100-j) × 2^j
- So we need: 100 - j = 62, which means j = 38  
    • **The Answer**: 100 choose 38 × 3^62 × 2^38  
    • **Key Point**: We don't actually calculate this huge number - we leave it in this form!
# Chapter 7
## Basic Examples to Lock This In
**Die Rolling Example:** P(rolling a 6) = 1/6 because there's 1 way to get a 6 out of 6 total possibilities
**Marble Bag Example:**  
• Bag has 4 green + 3 red + 2 blue = 9 total marbles  
• P(green) = 4/9, P(red) = 3/9 = 1/3, P(blue) = 2/9
**Two Dice Sum Example:**  
• Want P(sum = 3) when rolling two dice  
• Ways to get sum of 3: (1,2) and (2,1) = 2 ways  
• Total possible outcomes: 6 × 6 = 36 ways  
• Answer: P(sum = 3) = 2/36 = 1/18
## Discrete Probability Practice Problems
### Lottery Probability Basics
**The Setup**: Match 5 digits in order from randomly drawn digits (0-9)  
**Winning Probability**: Only 1 winning combination out of 10^5 total possibilities
- Calculation: 1/(10×10×10×10×10) = 1/100,000 = 0.00001
- That's a 1 in 100,000 chance!
**Money-Back Guarantee**: What if you get your money back for matching at least 1 digit?
- Use the complement rule: P(at least 1) = 1 - P(none)
- P(no matches) = (9/10)^5 = 0.59049
- P(at least 1 match) = 1 - 0.59049 = 0.40951
- About 41% chance you don't lose money (Professor X admits no real lottery would do this!)
### Card Deck Fundamentals
**Deck Composition**: 52 cards total
- 4 suits: hearts, diamonds, clubs, spades
- 13 cards per suit: Ace, 2-10, Jack, Queen, King
- 4 of each type of card
### Poker Hand Probability (Ace-King-Queen-Jack-Ten)
1. *Method 1: Sequential Drawing (The Tricky Way)*:
	- Start with: (4/52) × (4/51) × (4/50) × (4/49) × (4/48)  
	- **CRITICAL**: Must multiply by 5! because order doesn't matter in a hand  
	- Final answer: $[(4/52) × (4/51) × (4/50) × (4/49) × (4/48)] × 5!$
2. *Method 2: Combinations (Professor X's Preferred Way)*
	- Numerator: (4 choose 1) × (4 choose 1) × (4 choose 1) × (4 choose 1) × (4 choose 1) = 4^5 
	- Denominator: (52 choose 5)  
	- Result: 1,024/2,598,960 ≈ 0.000394  
- **Why this is better**: Calculator-friendly and less error-prone!
### Drawing Aces Four Times
1. *Without Replacement*: 
	- (4/52) × (3/51) × (2/50) × (1/49)  
	- Each draw reduces available aces and total cards
2. *With Replacement*:
	- (4/52)^4 = (1/13)^4 ≈ 0.0000035  
	- Same probability each time because cards go back
### Full House Probability (3 of one kind + 2 of another)
1. *Method 1: Permutation Approach*:
	- 13 × 12 × (4 choose 3) × (4 choose 2) / (52 choose 5)  
	- The 13 × 12 accounts for choosing which two card types to use
2. *Method 2: Choose Types First*:
	- (13 choose 1) × (4 choose 3) × (12 choose 1) × (4 choose 2) / (52 choose 5)
3. *Method 3: Choose Both Types Together:
	- (13 choose 2) × (4 choose 3) × (4 choose 2) / (52 choose 5)  
**All three methods give the same answer**: 0.00144 or about 1.44%
### Bit String Problems (10-bit sequences of 0s and 1s)
1. *At Least One Zero*:
	- **Don't calculate**: P(1 zero) + P(2 zeros) + ... + P(10 zeros) - too much work!  
	- **Smart approach**: P(at least 1 zero) = 1 - P(no zeros)  
	- P(no zeros) = P(all ones) = 1/2^10 = 1/1024  
	- Answer: 1 - 1/1024 = 1023/1024
### Divisibility Problems
1. *Integers 1-100 Divisible by 2 OR 5*:
	- Use formula: P(A or B) = P(A) + P(B) - P(A and B)  
	- Divisible by 2: floor(100/2) = 50 numbers  
	- Divisible by 5: floor(100/5) = 20 numbers  
	- Divisible by both (i.e., by 10): floor(100/10) = 10 numbers 
	- Answer: (50 + 20 - 10)/100 = 60/100 = 0.6  
**Pro tip**: Use floor function when the division isn't exact!
# Chapter 9 
## Random Variables
### Coin Flipping Example (3 flips)
• **All possible outcomes**: HHH, HHT, HTH, HTT, THH, THT, TTH, TTT (8 total outcomes)  
• **Random variable X = number of heads**:
- P(X = 3) = 1/8 (only HHH gives 3 heads)
- P(X = 2) = 3/8 (HHT, HTH, THH give 2 heads)
- P(X = 1) = 3/8 (HTT, THT, TTH give 1 head)
- P(X = 0) = 1/8 (only TTT gives 0 heads)
### Real-World Example: Discrete Math Class
• **Scenario**: 5 students, each has 92% chance of passing  
• **Question**: What's the probability exactly 4 students pass?  
• **Solution process**:
- Probability of passing = 0.92
- Probability of failing = 1 - 0.92 = 0.08
- Need to find: P(exactly 4 pass, 1 fails)
- Must consider ALL ways this can happen (not just pass-pass-pass-pass-fail)
- Number of ways = C(5,4) = 5 ways
- Final calculation: C(5,4) × (0.92)⁴ × (0.08)¹ = 0.2866
## Binomial Distribution
### Blood Drive Example #1
**Scenario**: 6% of people have O-negative blood  
**Question**: What's probability exactly 1 out of first 5 donors has O-negative?  
**Setup**:
- n = 5 trials
- k = 1 success
- P = 0.06 (probability of O-negative)
- q = 0.94 (probability of not O-negative)  
    - **Calculation**: C(5,1) × (0.06)¹ × (0.94)⁴ = 0.2342
### Calculator Method
• **TI-83/84 function**: binompdf(n, P, k)  
• **For above example**: binompdf(5, 0.06, 1) = 0.2342  
• **Remember order**: n first, then P, then k
### Calculator for "At Least" Problems
**Use**: 1 - binomcdf(n, P, k)  
**CDF vs PDF**:
- PDF = exact probability for one specific value
- CDF = cumulative probability (adds up from 0 to your chosen value)  
	- **For "at least 2"**: 1 - binomcdf(5, 0.06, 1) = 0.0319
### Blood Drive Example #2 - "At Least" Problems
**Question**: What's probability at least 2 donors have O-negative?  
**Two approaches**:
**Method 1 (Hard way)**: Add up P(X=2) + P(X=3) + P(X=4) + P(X=5)
**Method 2 (Smart way)**: Use complement rule  
- P(X ≥ 2) = 1 - P(X ≤ 1)  
- P(X ≤ 1) = P(X=0) + P(X=1)  
- Much easier to calculate!
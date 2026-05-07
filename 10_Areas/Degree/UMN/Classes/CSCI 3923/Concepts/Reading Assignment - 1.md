---
type: class
input_kind: book
status: sprout
created: 2026-01-30
updated: 2026-02-11
area:
  - "[[UMN Board]]"
  - "[[CSCI 3923 Board]]"
tags:
  - "#class"
  - "#Textbook"
next: "[[10_Areas/Degree/UMN/Classes/CSCI 3923/Week - 1|Week - 1]]"
---
# Chapter - 1
Chapter 1 of _Weapons of Math Destruction_, titled **"Bomb Parts: What Is a Model?"**, explains how mathematical "models" are built and why some of them turn into dangerous "weapons."
1. Thinking Like a Data Scientist (The Baseball Story): 
	The author begins with a story from 1946 about a baseball manager named Lou Boudreau. He noticed that a star player, Ted Williams, almost always hit the ball to the right side of the field. To stop him, Boudreau moved all his players to the right side to catch the ball.
	This is **thinking like a data scientist**:
	- **Data:** Looking at what happened in the past (where the ball was hit).
	- **Adjustment:** Changing your plan based on that data to get a better result in the future.
2. What Exactly Is a "Model"?
	A **model** is just an **abstract representation** of a process. Think of it as a **"toy version"** or a map of the real world. It takes the information we already have and uses it to predict what will happen in different situations.
3. A Good Model vs. a Bad Model
	The author compares baseball models to the "toxic" models she calls Weapons of Math Destruction (WMDs).
	**A "Healthy" Model (like Baseball) has:**
	- **Transparency:** Everyone can see the numbers and understand the rules.
	- **Relevance:** The data used is actually about the thing being measured (like hits and strikes).
	- **Feedback:** It is updated every day with new information. If the model is wrong, the statisticians see it and fix it.
	**A "WMD" Model often uses "Proxies":**
	- **Proxies** are "stand-in" data. If a modeler doesn't have data on how good you are at a job, they might use a proxy like your **zip code** or your **credit score** to guess. This can be very unfair and even illegal.
4. Personal Models: Cooking Dinner
	The author uses the example of **cooking dinner for her family** to show how we all use models in our heads.
	- **Inputs:** What’s in the fridge, how much energy she has, and knowing that one son loves chicken but hates burgers.
	- **Output:** The meal she decides to make.
	- **Dynamic Model:** If her kids are happy and full, she knows her "model" worked. If they complain, she updates her model for next time.
5. The Big Secret: Models are Opinions
	Many people think math is perfectly neutral, but the author says **models are opinions embedded in mathematics**.
	- Whoever makes the model decides what is important.
	- **Example:** If the author builds a "dinner model," she might decide "No Pop-Tarts allowed" because of her personal beliefs (**ideology**). If her kids built the model, "success" might be ice cream for every meal.
6. Blind Spots and Simplifications
	Because a model is a "toy" version of reality, it has to be **simple**. This means it always has **blind spots**—things it chooses to ignore.
	- **Google Maps** ignores buildings because they aren't roads.
	- **WMDs** often ignore human things, like a teacher’s ability to inspire a student, because it’s easier to just count test scores.
7. Racism as a "Slovenly" Model
	The author explains that **racism** is actually a very bad predictive model. It takes small amounts of bad data or "hearsay" and uses it to make a rule about an entire group of people. It rarely tests if it is right and settles for information that confirms what it already believes (**confirmation bias**).
8. The Scary Example: Recidivism (LSI-R)
	The chapter ends with a look at the **LSI-R**, a model used in prisons to guess if a person will commit another crime.
	- **The Problem:** It asks prisoners about their friends, their family, and their neighborhood.
	- **The Injustice:** If you grew up in a poor neighborhood where the police stop people a lot, your "score" will be high risk. You might get a **longer prison sentence** not for what you did, but for **who you know** or **where you were born**.
9. The Three Parts of a WMD
	For a model to be a Weapon of Math Destruction, it must have these three parts:
	1. **Opacity (Mystery):** The model is a **"Black Box."** The person being judged can't see how the score was made and has no way to argue if it’s wrong.
	2. **Damage:** The model works against the person's interest. It can ruin lives by keeping people from jobs or loans.
	3. **Scale:** The model is **massive**. It grows quickly and is used to judge millions of people at once.
10. The Feedback Loop
	A **feedback loop** is when a model's prediction makes the prediction come true.
	- **Example:** A model says a poor person is "high risk" for a loan. They get denied the loan and stay poor. The model then says, "See? I was right, they are still poor!" The math didn't just predict the problem; it **helped create it**.
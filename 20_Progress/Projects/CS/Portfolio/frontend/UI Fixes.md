---
type: class
input_kind: project
status: seed
created:
updated:
area:
tags:
  - "#class"
next:
---
# 

## Overview
- 
## Plan
- [ ] Break down tasks
- [ ] Solve core
- [ ] Writeup/tests
- [ ] Submit
## Detailed analysis of ui fixes
-  I'm going to tell you the detail and UI fix that needed to be implemented in my portfolio overall.

We are going to talk about V0. This is from localhost. Everything that we have done on the localhost is deployed, and it's all in sync. Actually, if you could verify that, that would also be great.

Now, diving into the UI fixes that we need to do: as soon as I open the landing screen, I want my image to be static. It should not be moving around. And the half wave over the photo should have a nice effect. It should have a comic card effect, but it shouldn't be very deep. It should be a very light effect. 

Let's remove the terminal because it didn't do much for the space. The wiggle effect is not really necessary.

I've received feedback that the initial part of the portfolio is not that great. As we scroll down, it gets better and better, but it's not really eye-catching as soon as the user opens it. So we need to work with the background and make it much more initially eye-catching. The background should do something else as soon as the portfolio opens up, and it should be a slow effect.

How about all these stars, all these particles around the revolving planet, being entirely scattered around the screen? The ball is inside a perimeter that is all scattered over, and slowly the entire ball connects like a very satisfying graph. It appears like these nodes are connected, and they form the perfect circle that it is currently at. This should resolve to exactly as it is right now. The background size and everything should resolve to this, but as soon as you open it, it's all scattered away.

Again, we are removing the terminal that is just below the landing screen. We're not deleting the file, but we're just removing it for now and deciding what we can do about it later.

We'll have to push up the About Me, and the About Me should be something that's toggleable. It should only show about 3 or 4 sentences in the nice format they're in right now. As soon as it is toggled, it changes into what is currently seen.

Basically, we need to build something that's going to shorten the About Me, and we're going to write something additional on top of it. We're not only going to shorten this so that when the user clicks on it, he sees something, but when it's not toggled, he sees something else.

The 4 boxes down there need to be enhanced further as something clickable that shows more detail. So we shorten everything over here, and the About Me should only be about a screen big when it is not toggled. Everything should be clickable in the About Me section.

Upon clicking these boxes, I want it to show a tiny graph about what exactly I am talking about. This could be something like my skill section graph, but much tinier. There's a summary just below it saying something about the specific thing written down. 

The toggle on the sidebar on a phone, especially the send button, is not entirely applicable for each and every screen. For a small phone, the send button gets outside the phone, and you have to zoom out to click the button. So, the sidebar is not exactly responsive for each and every single device.

We need to make sure that the layout for the send button and the writing button is clean.

Also, when writing a very long message, the user cannot see how long the message has been. I want the message part to be in a way that, when the user types more, the box increases. This can only increase to about 3 lines.

The character limit per line should be until the send button. Over here, I am going to give you an example of when the character limit hits for the send button, and the user can know more and see what is written exactly after this.

Also, I noticed that the cursor movement for left and right to switch between the text is not really working. Only if I click on the specific part of the text is that working.

Here is our text character limit upon gibberish that I typed: "ahshdahshdhshahshdhahshdhasgdhhshdagsdah".

![[Pasted image 20260711204507.png]]
![[Pasted image 20260711204540.png]]

The experience section just needs richer content. The summary should be much better. The bullet points need to be better. The achievements need to be better as well. The content is poor. UI-wise, that is alright. UI-wise, actually, it's perfect. I don't think there's anything else we can do for this.

Also, set a limit for each and every summary so it does not cross the page. The line limit should be there only till that much for each and every single summary. It should show three dots, and the card should just stop there. It should be a hard stop.

For the project section, we need to improve the UI for the section a lot. We have too many projects and too many buttons to click here. I don't want it to keep rolling all 9 projects. I want it to only keep auto-rolling the first 3 projects. It will roll through 1, 2, and then 3, and then go back to 1 again. It will not go through all 9 projects. But the user can see that there are 9 projects because it says the project number you are currently on. So the user can click more and find out more.

Also, the navigation link with the chatbot for each and every single project is not on point. The chatbot can't seem to go to the exact project number. I want this navigation link to be extremely strong, and the chatbot should show the exact correct project each and every single time.

Then, coming to skills and expertise, the UI effect on each and every single card could be improved much more. I'm talking about the skills that render down when clicked on a skill category. The UI effect on each of them seems to be laggy and not exactly the most eye-pleasing effect. There are very limited types of effects taking place on each and every single skill. I want these to be much more enhanced. Even the skill category UI effects almost seem to be laggy, but they need to have a much cleaner effect.

The graph should not be starting at 2021. The graph should be starting at 2022. Also, each and every single skill should not start above 35. No skill should be above the familiarity/applied depth starting point for any single type of skill in the graph.

The padding between the education section above and skill sections below is too much. The most highlighting part about the education is the middle school. The bachelor's in computer science is not highlighted at all.

To fix this, we are going to add a much better UI background and color contrast to the bachelor's in computer science sphere. We are gonna trace the dots movement in a manner that, as soon as the user lands on the education section, the dots start from middle school, with the bachelor's in computer science being the most deformed shape. When the dot gets to high school, it is in between the deformity of middle school and high school. The percentage for deformity should be just between that. As soon as it gets to bachelor's in computer science, the deformity of it is 0. It's a solid sphere.

This transition should be very UI-pleasing, and it should be clean between each and every single UI change.

Again, the padding between the certifications just above and education just below sections is too much. There is too much of a gap between them.

The background should have an effect of scattering away and rejoining back as the perimeter of the blast radius changes. What I mean by that is, the perimeter is going to be just above where the stars or the particles surrounding the sphere are. That is the blast radius capacity each and every single time. So upon clicking it, as the user scrolls, it scatters away in the same form that it was scattered away in at the start of the opening of the landing page. When the starting effect took place, it should have a similar effect, but adjusting itself to the zoom-in effect of the background.

What I mean by that is that the user can only display this effect if the user clicks inside the sphere, or clicks at the sphere, clicks inside the blast radius, basically. If the user clicks inside the blast radius, then the sphere scatters and the similar effect takes place. So there should be a perimeter around the stars in a manner that this blast radius is adjustable as these zoom and scroll effects take place. These stars are particles of the planet.

Something that we decided would be inside v2 was the dark mode effect.

There should be a color contrast on light mode for this entire portfolio, in a manner that the black, white, and purplish-purple-bluish color changes into another contrast on light mode. It should not exactly be white, but it should be something close to white. It should be an exact opposite contrast of the color combination we have on this portfolio.

The dark mode is an already applicable hovering button on the header, but it does absolutely nothing. So we need to make sure that this dark mode feature has been enabled.

Now, when talking about RB, we need to upgrade RB to be much more sophisticated and UI-pleasing to the eye. The hand movement for RB is still not that good, and the radio in hand is just a purple thing. It should actually look like a radio with an antenna on it. It should appear that he is talking to someone sometimes because his hand lifts up entirely to say hi. Right now, Orbi's hand does not entirely lift out to say hi either. Orbi does not stick to the ground entirely, as stated earlier.

We were working on RB before, but this seems to be alright because RB still sticks to the bottom majority of the portfolio. But as this is a very static moment of Orbi, it should still stick to the bottom, but it should still have multiple effects:

- walking around
- talking on his radio
- dropping funny comments

This should all be AI through the model that you are using. This should be generated from a backup model provider that we already have in the portfolio. Most of the RB messages are going to be AI-generated in this version, and AI RB talks much more than it was talking previously.

As the user clicks around, RB acts up and says something that is completely generated. If the user spends some time on a particular section, then RB also says something at that point. When RB moves around the entire portfolio as the user scrolls, RB should do something. It should probably be hovering or doing a lot of actions. Right now, all it does is slide around from one corner to another, and the movement is very lousy. All it does is zoom from one place to another.

The footer could be much more eye-pleasing, much better.

## Ui images of all fixes required
The sidebar has been shown above clearly, below are screenshots of further ui fixes that needs some viewing
![[Pasted image 20260711211130.png]]
![[Pasted image 20260711211213.png]]
![[Pasted image 20260711211259.png]]
![[Pasted image 20260711211336.png]]
![[Pasted image 20260711211404.png]]

## Concepts used
- [[Concept - ...]]
- [[Concept - ...]]
## Post-submit reflection
- What failed first?
- What pattern repeats?
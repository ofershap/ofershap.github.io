# Advanced Cursor guide - context window is the new game we play

Advanced Cursor guide - context window is the new game we play

To get it to work properly, I created for myself a set of rules (cursor rules) that load automatically at the start of every conversation. I phrased them in a martial arts tone, both so they'd be short and token-efficient (because they join every conversation - always apply mode), and so it's clear these are ground assumptions, not requests.

The rules tell it, among other things:
- Not to agree with me automatically
- To check the code before every response
- Not to change code that doesn't have to be changed
And a few more (according to the project's needs)

That said, I noticed that when the working conversation gets long and the context window fills up, the rules get forgotten. It simply stops behaving according to them, even if they're listed at the start of the conversation. The only way to bring them back into the picture is to remind it: "read the rules".

It's amazing to see the effect of the rules - suddenly it stops making assumptions, hallucinating, reduces mistakes and starts acting according to existing patterns. Especially when I ask it to first study the code or the context, before it responds.

To refine the work, I also put explanations in my Cursor rules of what *not* to do:
- Not to add comments in the code unless I asked (in line with the team's coding standard)
- Not to run npm run - because we use hot reload
- Not to write documentation on its own initiative (there is probably a system prompt pushing it to do that)

And I also gave it instructions on how to do things, based on past failed attempts, in which after a number of iterations we found out together how to do it, and then I anchored that in a sentence inside the file:
- How to call GitHub and extract PR comments
- How to use CURL when there is no MCP for a certain tool
- How we write tests in the project

You can look at the new programming world (the one based on LLMs) through 3 layers:
- The model layer (which model you use)
- The agent layer (which development tool you use)
- The rules layer (what adjustments you make for your personal needs)

The third layer is what turns Cursor from a "learner" developer who mostly makes educated guesses (because it doesn't have enough context) into a more attentive developer


Feel free to share your own tips on what worked and what didn't work for you with Cursor 🤓

Original: https://ofershap.github.io/posts/managing-cursor-through-rules-and-context-windows/
Source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%93%D7%A8%D7%99%D7%9A-cursor-%D7%9C%D7%9E%D7%AA%D7%A7%D7%93%D7%9E%D7%99%D7%9D-context-window-is-activity-7360565724680978433-4Ew5
Published: 2025-08-11T10:00:21.462000+03:00

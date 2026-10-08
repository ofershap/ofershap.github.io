# "What are you real? We talked about that exactly 10 years ago!"

"What are you real? We talked about that exactly 10 years ago!"

Suddenly in the middle of a conversation with a friend from the past while we dove deep into a conversation about AI's memory, or more precisely why it "forgets" things in the middle of a conversation. The friend from the past described how the context window works, and I heard "RAM memory management". What goes into the context window is available to the model immediately. What doesn't go in, as far as it's concerned, doesn't exist. Exactly like working memory in regular software.

Friends, everything repeats itself. There's nothing new under the sun and it's happening now too with the AI revolution.

The context window is memory for all intents and purposes - what goes into the context window is available to the model immediately, and what doesn't go in, as far as it's concerned, doesn't exist. Exactly like working memory in regular software. RAG is exactly like loading from a hard disk and the challenges that come with it. Conversation summarization is lossy compression. Prompt caching is a classic cache. A sliding window is a ring buffer. All these concepts have existed for decades, just with new names.

And this doesn't happen only at the infrastructure level. Every time a new technology arrives, we hold the same conversations again. When Angular arrived, there were arguments about state management, about separation of concerns, about component architecture. The very same arguments that existed years before in other contexts. Now with AI it's the same: what to keep, what to throw away, what to index, what to retrieve. Questions software engineers have been solving for generations.

And there's also a thinking tool here that's worth not missing. If you understand that the context window behaves like working memory, you can predict in advance which features will come next, because you already know the problems and the solutions from the classic software world. There are advantages to being a senior developer 🙂 

What doesn't change even more, but fools us a lot, is the basic practices of software engineering - precisely because AI accelerates development they are more important today than ever. 

The data from 2025 and 2026 is clear: code generated with AI contains more bugs, PR review time rises significantly, and readability problems pop up at a higher rate. The DORA report showed it best: AI is an amplifier. Teams with strong processes get stronger. Teams with weak processes get weaker.

Writing production-ready code with AI is the same challenge as without AI. 
You need small, readable PRs. You need SOLID principles to optimize the context of the agent that accesses the code. You need to think about scale in production when meeting thousands or millions of customers, something that it feels models still don't have enough context for. You need to plan and share with the team to get several points of view - each person and their area of expertise, to make sure we cover everything that can't really be put into the agent's context. 

In short, all the work practices that form the basis of good software development haven't changed. 
So the illusion of not writing code is true only for the part of actually writing the code. Code maintenance requires and forces synchronization between machine and human, with an aspiration to reduce this expensive and slow interface by means of high Trust layers.

Technology does change and renew itself, but the bugs remain. Let's get to work

Original: https://ofershap.github.io/posts/ai-changes-the-tools-not-the-engineering-problems/
Source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%94-%D7%90%D7%AA%D7%94-%D7%90%D7%9E%D7%99%D7%AA%D7%99-%D7%A2%D7%9C-%D7%96%D7%94-%D7%93%D7%99%D7%91%D7%A8%D7%A0%D7%95-%D7%9C%D7%A4%D7%A0%D7%99-10-%D7%A9%D7%A0%D7%99%D7%9D-activity-7477950706319208448-Pxzd
Published: 2026-07-01T08:06:21.992000+03:00

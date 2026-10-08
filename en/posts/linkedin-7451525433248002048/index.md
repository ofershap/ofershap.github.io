# A friend reached out and said he upgraded Cursor to a Pro subscription and after a day he had already used 13% of his subscription. So I sat down and wrote the following guide for him and for you:

A friend reached out and said he upgraded Cursor to a Pro subscription and after a day he had already used 13% of his subscription. So I sat down and wrote the following guide for him and for you:

* How to save on AI development costs (and save tokens) *

Here are a few tips that can help you from my experience, both for Cursor and for Claude Code:

Whether you're paying out of your own pocket or working in an organization, cost awareness is the first thing that worries you right after you've adopted the technology.

If you use Cursor - it does a lot of the work for you by itself, but there are still a few things you can do yourself: 
 
- Try to open a new conversation at the start of every new topic. If the content of the existing conversation matters to you but you want to reduce the size of the context (which affects the token cost), then after opening a new conversation you can ask it to read the conversation history by using @past and choosing the conversation.

- Expensive models are better but naturally... more expensive. 
One of the ways I use to save costs is by asking the model to run secondary agents on a cheaper model and supervise them. (I even have a rule like that).
Spawn subagents and use composer-2 for the work it can do, and supervise it
Sometimes (on big tasks) I add - then critic it and run subagent to fix
And then I get both high speed (because it can run in parallel) and also economical and proper management of tasks and even a fix of the code before I even looked at it

- Choosing models for the task is a muscle you need to work on. There are two keyboard shortcuts I really like, and they sit next to each other. Next to the right shift button on your keyboard there are the question mark and the final "ץ" (final tsadi, a Hebrew letter), so in English each of them together with cmd changes one of the two - either the model, or the mode (plan, agent, ask)
I adopted three models for myself and I switch between them all the time: composer-2, sonnet 4.6, opus 4.6. For many tasks I use Composer as long as they're not complicated. For tasks that require more complex thinking, or for Debug, I move to the smarter ones. 
I don't use Auto, I don't know what happens there and it's important to me to control the model that carries out my tasks.

Something that may be worth knowing: if you work in an organization and are on an enterprise account where there is "one blanket" that everyone pulls and there's a need to supervise costs, I released an open-source project that lets you track, monitor and get alerts on the company's expenses: https://lnkd.in/djZRK5ZP

And what about Claude Code? 
First thing I recommend installing the claude code statusline so it shows you how much context is currently in use, and when you see it bloating you can either open a new conversation or call /compact, to which you can also attach in a sentence what's important for you to keep and what can be dropped (or just let it decide)

In addition, there are also skills and libraries that can help a lot:

Artik (Hebrew: ארטיק): https://lnkd.in/eXKPNNvV
A proxy that saves tokens, works mainly with Claude Code (Cursor already handle this themselves)

"The Prehistoric Man" (Hebrew: האדם הקדמות): https://lnkd.in/eqrJanMQ 
Reduces the length of answers and content to a basic "caveman" language and saves the amount of text (= tokens) that accumulates over conversations. This comes at the cost of answers and explanations.


To sum up,
we've passed the technology adoption stage and moved up a grade to optimal work and an attempt to save on costs. The new playground forces us to be aware of costs because every action we take costs money, and just like driving a car you can't press the gas pedal all the way down all day and burn the whole tank of fuel, you need to manage "munitions economics" here and optimize our usage

Know other methods? I'd love to hear!

Original: https://ofershap.github.io/posts/cutting-token-costs-in-cursor-and-claude-code/
Source: https://www.linkedin.com/posts/ofershap_%D7%97%D7%91%D7%A8-%D7%A4%D7%A0%D7%94-%D7%90%D7%9C%D7%99-%D7%95%D7%90%D7%9E%D7%A8-%D7%A9%D7%94%D7%95%D7%90-%D7%A9%D7%93%D7%A8%D7%92-%D7%90%D7%AA-%D7%A7%D7%A8%D7%A1%D7%95%D7%A8-%D7%9C%D7%9E%D7%A0%D7%95%D7%99-activity-7451525433248002048-KmoP
Published: 2026-04-19T10:01:45.934000+03:00

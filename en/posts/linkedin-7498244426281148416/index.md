# How do we all work today? It's funny (or sad) but basically it's: ask agent → hope

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

How do we all work today? It's funny (or sad) but basically it's: ask agent → hope
It doesn't have to be this way. One of the respected developers (author of Total TypeScript) turned the random prompts into a repeatable engineering process with checkpoints the agent must pass.

What does that mean? Instead of giving one big prompt, you run a defined workflow according to the stage you're at:

If you have a vague idea or a feature that isn't baked yet: `/grill-me` and then `/to-spec`
The agent challenges your assumptions, and then writes a real spec.

If there's already a spec, but the task is too big to build: `/to-tickets` or `/wayfinder`
You get small, focused tickets or a decision map that lives inside GitHub or Linear.

If you're already ready to build: `/implement` together with `/tdd`
You move forward one piece at a time, red → green → refactor, instead of rewriting half the app in one go.

If you built but something broke: `/diagnosing-bugs`
Reproduce the problem → narrow it down → form a hypothesis → add measurement → fix.

Before merge: `/code-review`
The check runs on two axes in parallel: meeting the standards versus matching the spec.

This way you harness the AI to be much more attentive to you, with commands that know the limitations of the models and the agents, and it also keeps you within bounds over time, without jumping around or forgetting or getting tired.

It makes the agent behave more like a senior developer working with you who first demands clarifying, breaking down, testing and review, instead of like a junior developer who starts writing code immediately.

That is, you don't skip the "boring parts" of aligning expectations, defining the scope, testing and review, which usually get lost when doing vibe coding.

What's important to remember, though, is that it's not magic... it's a process packaged inside skills.
The most important part of the process is you. Remembering the commands, memorizing them, and using them at the right time.
No model and no skill can do that for you.

If you skip the initial setup with `/setup-matt-pocock-skills`, or simply don't actually use the slash commands, it's just another folder with Markdown files.

By the way, if you already have your own skills and commands, it's worth asking the chat to go over its commands and see what you already have and what's worth adopting.

Link to the project: https://lnkd.in/dqzMnXpN

Original: https://ofershap.github.io/posts/linkedin-7498244426281148416/
Source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%9A-%D7%9B%D7%95%D7%9C%D7%A0%D7%95-%D7%A2%D7%95%D7%91%D7%93%D7%99%D7%9D-%D7%94%D7%99%D7%95%D7%9D-%D7%96%D7%94-%D7%9E%D7%A6%D7%97%D7%99%D7%A7-%D7%90%D7%95-%D7%A2%D7%A6%D7%95%D7%91-activity-7498244426281148416-XmRj
Published: 2026-08-26T08:06:21.870000+03:00

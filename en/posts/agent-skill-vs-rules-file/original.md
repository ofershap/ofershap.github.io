Title: When do repeated agent instructions become a Skill?

**Short answer:** A fact about the project belongs in the rules file. A process that repeats itself belongs in a Skill. The practical difference: the rules file always loads and costs in every conversation, and a Skill loads only when needed. Rule of thumb: if you've pasted the same instruction three times, it's time to give it a home.

### A rules file is facts, a Skill is a process

The Claude Code docs draw the line explicitly: create a Skill when you keep pasting the same instructions, the same checklist, or the same multi-step process, or when part of the rules file grows into a process instead of a fact. "We work with TypeScript strict" is a fact. "This is how we open a PR, step by step" is a process.

Example: a rule saying "every PR includes a description of the decision" stays in the rules file. A six-step process for checking a migration before merging becomes a Skill.

### Why the fixed loading cost matters

Everything in the rules file loads into every conversation, even when it's irrelevant. A Skill loads only when the agent detects it's needed or when it's called by name. For a team, that means you can maintain a whole library of processes without inflating every conversation. The docs put it this way: the Skill body costs almost nothing until it's used.

### How to start in practice

First step: open your conversation history and look for an instruction you pasted twice or more. Second: write it once as a SKILL.md with a short name and a description of when to use it. Third: try it on a real task and fix the wording based on what the agent actually did, not what you wanted it to do.

In my work with the agent on its open source project, I learned that the name and description are what the agent reads to decide whether the Skill is relevant. A vague description means a Skill that never opens, or opens at exactly the wrong moment.

### Testing that the Skill works

After writing it, run the process on a real case and check three things: the agent opened the Skill on time, followed the steps in order, and the output matches what you would have done manually. If one of the three fails, fix the SKILL.md, not the output. Fixing the output hides the problem for next time.
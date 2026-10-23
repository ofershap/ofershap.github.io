Title: How do you run a long creative project with an AI agent through chat?

**Short answer:** Define a clear final output, grant access gradually by stage, agree on regular reporting with screenshots, fix one comment per round, and check the output in the real system. A short loop with verification works better than one big task with no stops.

### Start with a brief you can check

Before the agent touches a tool, write what the final output is and how you'll know it works. In my case the brief was a simple fighting game with chairs, short rules, and a name. The more measurable the result, the fewer rounds wasted on guessing.

Example: instead of "build me a fun game", write "a single-player fighting game, three weapons, a win after five minutes, a victory screen with the winner's name". Every line like that can be checked at the end.

### Grant access gradually, not all at once

A long project through chat means the agent works while you're not watching. Open only what the stage requires: environment installation at the start, write permission to one project, and publishing only after explicit approval. The Roblox Studio setup documentation separates installing the environment from opening a project, and that's the right working order even when an agent performs the steps.

If a stage requires a new account or a payment, that's your stop, not the agent's. Agree on this upfront, so the work doesn't get stuck on a payment screen in the middle of the night.

### Agree on regular reporting

The part that worked best for me: the agent reported to WhatsApp at fixed points, attached screenshots from the build, and waited for comments. Without regular reporting, a long project becomes a black box that arrives at the end with surprises.

Example: a report after every milestone, three lines - what was built, what actually came out versus the plan, and what the open question is. One screenshot is worth more than a paragraph of description.

### One comment per round

When a screenshot shows a problem, fix that alone. "The character is stuck in the wall" is a comment. "Improve the gameplay, change the lighting, and add a level" are three tasks that tangle together. Every round: a comment, a fix, a new screenshot proving the fix worked.

The wording of the comment matters too. "The chair doesn't look good" leaves the agent guessing. "The chair is half sunk in the floor, raise it to sitting height" is a comment that can be executed and checked.

### Check in the real system

A screenshot is evidence, not a test. At the end of every significant stage, enter the system yourself: run it, click, look for the scenarios from the brief. Only after that do you approve moving to the next stage.

Anything not checked in the real system doesn't count as closed, even if the agent reports "done".
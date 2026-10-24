---
title: "How do you run a long creative project with an AI agent through chat?"
published: 2026-10-19T13:00:00+03:00
updated: 2026-10-24
lang: en
canonical: https://ofershap.github.io/en/posts/agent-long-creative-build-feedback/
original: https://ofershap.github.io/posts/agent-long-creative-build-feedback/
---

# How do you run a long creative project with an AI agent through chat?

Define a clear final output, grant access gradually by stage, agree on regular reporting with screenshots, fix one comment per round, and check the output in the real system. A short loop with verification works better than one big task with no stops.

## In depth

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

## From my experience

In my post about the Roblox game I told how Instinct built Royal Chair within days, through my WhatsApp: it reported, sent screenshots, and got comments and fixes from me. This guide breaks that working method into steps. It documents one case that worked, not a promise that every project ends this way.

## Frequently asked questions

### Can you let the agent work a whole night without reports?

You can, but every hour without a report is an hour where a wrong direction gets more expensive. A reporting point every hour or two keeps the risk small.

### What do you do when the agent is stuck on the same problem?

Stop the round, ask it to phrase what it knows and what's missing, then decide: missing information, missing permission, or a wrong approach. Don't let it retry the same step again and again.

### Does the method fit code too, not just games?

Yes. A checkable brief, gradual access, regular reporting, and one comment per round work the same way on a feature, a document, or a deck.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-24

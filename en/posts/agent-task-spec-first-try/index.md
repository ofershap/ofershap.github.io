---
title: "How do you write a coding-agent task that succeeds on the first try?"
published: 2026-10-21T07:50:00+03:00
updated: 2026-10-24
lang: en
canonical: https://ofershap.github.io/en/posts/agent-task-spec-first-try/
original: https://ofershap.github.io/posts/agent-task-spec-first-try/
---

# How do you write a coding-agent task that succeeds on the first try?

A good agent task has four parts: context, a definition of done, boundaries, and verification. It takes five minutes to write and saves most rework cycles.

## In depth

### The context the agent can't guess

The agent sees the code, but not the reason it looks that way. One line on why the change is needed, and one more on what you already tried, saves most wrong directions. If one file holds the problem, point to it by name.

### A definition of done before you start

"Fix the form" is an open-ended task. "The form saves, shows an error on an empty field, and the existing tests pass" is a task you can check. An explicit definition of done turns your job from supervising every step into one check at the end.

### Boundaries in writing

An agent that finds a nearby problem tends to fix that too. Write what's in scope and what stays out: which folder it may touch, whether it may change an existing API, and whether it may upgrade a dependency. The boundary becomes part of the task, not a negotiation after the output.

### The check that proves the output works

Write how to verify: which command runs the tests, and what result to expect. The agent checks itself before handing back, and you look at evidence, not vibes.

### A full task in four lines

Example: "checkout.ts has a bug: double-clicking submit creates two orders. Done = double-click creates one order, all tests pass. Boundaries = only checkout.ts and its tests, no dependency upgrades. Verify = npm test checkout."

### How much time this saves

Five minutes of writing versus two or three fifteen-minute rework cycles. In my experience, most of those cycles start with a task missing one of the four parts.

## From my experience

I run coding agents every day, and the biggest difference in output comes from five minutes of task writing, long before the model choice. In my PR Description post I covered how to explain a change to a human reviewer. This is the exact same work, one step earlier: the moment you write the task for the agent.

## Frequently asked questions

### How long should an agent task be?

Long enough to cover the four parts. Usually five to ten lines. A task that's too long hides what matters, and a one-line task only fits a pinpoint change.

### What do you do when the agent steps out of bounds?

Stop, sharpen the boundary in the task, and rerun from a clean state. Fixing the output by hand leaves the next task at the same level.

### Do you need a full task for a small change too?

A one-line change in one file needs one line. The four parts come into play the moment the change touches more than one file or one decision.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-24

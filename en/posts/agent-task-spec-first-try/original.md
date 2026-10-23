Title: How do you write a coding-agent task that succeeds on the first try?

**Short answer:** A good agent task has four parts: context, a definition of done, boundaries, and verification. It takes five minutes to write and saves most rework cycles.

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
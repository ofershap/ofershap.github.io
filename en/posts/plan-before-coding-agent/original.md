Title: What should you decide before starting to build with a coding agent?

**Short answer:** Define who will use the product, where it will run, who will maintain it, and how it reaches users. Then choose a tool and ask the agent to build a small experiment that validates the choice.

A tool that produces a pretty screen still has to fit the product's life after the demo. When I plan the work, I separate the product decision from writing the code.

### Start from the user and the process
Write one action the user needs to complete. For example, a content editor needs to publish a page without opening a task for a developer. That is a test you can demo and check, not a general feature list.

### Check the way out
For an app: how do you distribute a version, who manages the store account, and how do you ship an update? For a content site: who edits the content, and how do you check the page is search-accessible? For a business system: where is the data, who is allowed to access it, and how do you recover from a failure? These are check questions. The answers depend on the product and the tool you choose.

### Write a short decision
You can use an ADR, an Architecture Decision Record. Martin Fowler describes it as a short document that records one decision, its context, and its consequences. Next to the choice, I suggest writing what the alternatives were and what would make us re-examine the decision.

A starter template:

- The problem the product solves and the first user.
- The constraints: distribution, permissions, maintenance and budget.
- Two alternatives worth checking.
- The choice and its reason.
- An experiment that proves the important action can be completed.
- Who owns it after the experiment works.

### Give the agent a bounded task
An example prompt, for illustration: "Before writing code, present two implementation approaches that fit these constraints. For each, state what we will need to operate and what is still unknown. Then propose a small experiment to test the main risk."

After deciding, ask for an implementation of the first action only. If the risk is deployment, the experiment must include deployment. If the risk is content editing, have a real editor test it. That way the choice rests on a working action, not on the impression from the first screen.
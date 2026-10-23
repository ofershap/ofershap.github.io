Title: How do you write a PR description for code an AI agent wrote?

**Short answer:** Start with the problem and the decision, then describe the change, the risks, and the test evidence. Give the reviewer a way to understand why the change should land before they read the diff. The agent can prepare the draft, and the change owner checks it describes what actually happened.

### Write an explanation, not a file list

A list like "updated three files and added tests" helps orientation, but leaves the decision out of the picture. What was the problematic behavior? Why does this solution fit? What changed for whoever uses the system?

In a good PR description you can separate two things: the decision you can discuss and the code that implements it. If the decision is still open, say so. A description confident in itself doesn't turn an assumption into agreement.

### A template you can start from

The following text is a suggested template, not a description of a real PR:

> The problem: what can't the user or the system do today?
>
> The decision: which solution was chosen, and why? Which alternative was considered and what was the tradeoff?
>
> The change: what is the new behavior, and which components are affected?
>
> Boundaries: what stayed as it was, and what is explicitly outside the change?
>
> Evidence: which tests or scenarios actually ran, on which version, and what was the result?
>
> Risks: what might break, how will we detect it, and how can we roll back?
>
> Open questions: which decisions or checks are still missing?

The template should fit the change. A small fix doesn't need a long document. A change to permissions, data, or an external interface justifies extra explanation even if the diff is short.

### Ask the agent for evidence you can check

The agent can read the diff and the run results and propose a draft. Ask it to distinguish between "I ran" and "recommended to run". Every line about a test should rest on output or a result you can locate, not on a list of tests it intended to run.

Example: a change in invoice handling should describe what happens to an invoice that was paid while the work was queued. Unit test output helps, but doesn't by itself prove the payment-provider connection was checked. This is a suggested example, not a client case.

If the agent used test data or a service substitute, note that. If an integration test didn't run, leave the limitation visible instead of writing "everything works".

### Keep the responsibility with the change owner

Before opening the PR, read the description without the diff. Can you explain the decision in your own words? Is there a claim you didn't check? Is there a risk left that someone else needs to decide on?

The agent is a draft writer. Whoever brings the change to the team needs to hold the explanation. If you can't answer why a certain solution was chosen, go back to the decision conversation instead of adding more words to the description.

### Make the template part of the repository

Per GitHub's documentation, a PR template in the repository is shown automatically in the PR body when it's opened. You can keep it in a .github/pull_request_template.md file. To be available, the template needs to be merged into the default branch. Multiple templates are also supported, when change types call for different questions.

The template reminds you what to explain. It doesn't prove the explanation is right and doesn't replace testing or review. Every so often, check which fields repeat without adding information and which important questions stay outside it.

### Start with one decision you can review

Success here is that whoever does the review can identify the problem, understand the choice, and find test evidence, without guessing from file names. If the important question comes up only after reading hundreds of lines, move it forward into the description or into a discussion before the implementation.
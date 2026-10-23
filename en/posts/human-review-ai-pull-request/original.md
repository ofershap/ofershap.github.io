Title: How do you review a PR an AI agent wrote?

**Short answer:** Check that the change solves the right problem, ask for test evidence, and verify the change's boundaries. Automatic review is another feedback layer, and human approval stays a decision about the product and the system.

### Start with the problem and the decision

Before reading a single line of code, ask for a short description: what changed, why it's needed, what stayed outside the task, and how the result was checked. Compare the description to the original request and the diff. A convincing explanation is not evidence the code does what was written.

Example: an agent was asked to fix handling of a missing file. If it also changed the output format, there's an extra product decision here that needs checking. The example isn't a client case, but a way to spot scope expansion.

### Demand a test that can fail

Ask for the commands that ran, their result, and what wasn't tested. A regression test should distinguish between the behavior before the fix and the behavior after it. A green result from tests that don't cover the fault isn't enough.

Also check error scenarios, permissions, and sensitive data when they're part of the change. A database change requires addressing migration and the way back. The level of testing should match the risk, not only the size of the diff.

### Use automatic review as additional feedback

GitHub's current documentation notes that Copilot code review can miss problems, and can also suggest an incorrect comment. The explicit recommendation is to verify the feedback and combine human review. So both code written by an agent and a fix suggested by a review tool need checking.

You can ask for early feedback on a draft-state PR, handle the relevant comments, and only then ask the team for review. Availability and settings depend on the plan and the account's permissions. You don't need to buy an extra tool to use this checklist.

### Re-check after a change

A review refers to a specific version of the code. In GitHub's documentation, Copilot doesn't necessarily check every push again unless configured to. After a significant fix, verify that the tests and the review cover the current version, and don't rely on an approval given before the change.

Branch protection rules can require checks and approvals before a merge, and dismiss approvals that went stale after a code change. That's an option for protecting the process, not a claim that every repository is set up this way.

### Finish with a decision you can explain

Before merging, check: does the result match the request, did the change stay within boundaries, is the evidence sufficient, and what risk remains. If information is missing, write what's missing instead of marking everything as checked.

An agent can shorten part of the preparation work. Whoever approves still needs to understand why the change should enter the system and what will happen if it fails.
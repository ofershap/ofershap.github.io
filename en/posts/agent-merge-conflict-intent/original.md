Title: How do you let a coding agent resolve merge conflicts without losing the change's intent?

**Short answer:** Hand the agent the goal of both changes, keep a return point, and check the combined result. Resolving a conflict isn't just removing markers from the file. You need to verify that the behavior each side meant to preserve still exists.

### Identify what's really colliding

A conflict says Git couldn't join part of the changes automatically. It doesn't decide which behavior is right. Both sides can be correct separately and still demand a new decision when joined.

Example: one branch adds a permission check before saving. Another branch changes the save to prevent a duplicate action. Choosing one side's version can erase the other's protection even if the code compiles. This is a synthetic example, not a fault recorded at a client.

### Keep a state you can explain and reconstruct

Before starting, check which branch you're on, which files changed, and what hasn't been saved yet. The Git documentation warns against merging with significant unsaved local changes. The git merge --abort command tries to restore the state before the merge, but doesn't guarantee restoring such local changes in every situation.

Ask the agent to identify the state and report it before acting. Don't let it delete local work to "clean" the working environment. A local commit or another form of saving should preserve the material, per the team's procedure. Secrets are not material you put in a commit.

### Give two intents, not just two files

Attach the reason for the change on each side, links to the discussion or PR description, and the tests that represent the behavior. Read the nearby code with the agent too. A variable-name change can hide a change in a function's contract.

A suggested request to the agent:

> Explain each side's intent and the collision. Propose a result that preserves both sides' requirements. If they contradict, stop with a focused question. Fix only the agreed conflict. Show a diff of the resolution and actual test results. Don't push or merge remotely without a separate instruction.

This defines an important boundary: the agent can prepare a local fix, but a product decision or a new permission requires whoever holds it to rule.

### Beware of automatic side-picking

In the Git documentation, the ours option inside a merge strategy prefers the current side in conflicting parts. The theirs option prefers the other side. These are technical rulings that can lose a requirement.

There's also a merge strategy called ours, which ignores the other side's changes and keeps the current side's tree. It's different from the option that prefers only conflicting parts. So a command that looks like a shortcut can change the meaning of the whole merge.

As a working default, ask for an explanation before a blanket choice. If the team decided to give up a change, document what was decided and why, instead of hiding the concession behind a "resolved" marker.

### Check the combination, not just the markers

The git diff --check command warns about conflict markers or whitespace errors added in the change. Per the Git documentation it returns a non-zero exit code when problems are found. It doesn't check that a permission, duplicate prevention, or other behavior was preserved.

Check a scenario representing each side, then a scenario exercising both together. In the permission-and-save example, check an authorized user, an unauthorized user, and a repeated action. The list is an illustration and depends on the code's real contract.

Alongside automated tests, go over the diff against the documented intents. Disappeared conflict markers are a stage in the process, not evidence of success.

### Return a short report before continuing

At the end the agent should present which conflicts were handled, what was preserved from each side, which commands ran, and what wasn't tested. An additional change needed to complete the join should be visible on its own.

If the result doesn't preserve both requirements, go back to the decision. The agent's role is to take down the mechanical work, without turning a business or engineering choice into something that happens by accident inside a file.
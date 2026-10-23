---
title: "How do you write review comments a coding agent or contributor can turn into a verified fix?"
published: 2026-10-14T13:00:00+03:00
updated: 2026-10-23
lang: en
canonical: https://ofershap.github.io/en/posts/review-feedback-to-verifiable-fix/
original: https://ofershap.github.io/posts/review-feedback-to-verifiable-fix/
---

# How do you write review comments a coding agent or contributor can turn into a verified fix?

Describe the problematic behavior, the conditions where it appears, and the result you want to keep. Ask for a focused fix and a test that fails against the old behavior. Separate a merge-blocking problem from an improvement suggestion that can wait.

## In depth

### Start from a scenario, not a preference

A comment like "this needs tidying" leaves the real work with whoever received it. To turn a comment into a task, write what you can do in the system and what happens as a result.

In the public discussion on PR number 60 in real-browser-mcp, concrete problems appear: two operations in parallel on the same tab can create two groups, and two debugger connections can leave more than one tab attached when only one is tracked. The reply in the PR also describes what should be tested. These are sources for a scenario, not proof that every possible browser environment was tested.

### Write a short contract for the fix

The following wording is a suggested template:

> When two requests reach the same resource before the first finishes, the system should preserve the agreed result. Show a test that reproduces the collision against the old version, fix the behavior, and show the same test against the new version. State what wasn't tested.

"The agreed result" needs to be replaced with a real requirement: one group, one connection, or a clear error message. Each of these is a different decision. If there's no agreement, open a discussion before asking the agent to choose.

### Separate a blocker from a suggestion

A review can address a bug, a design question, and code cleanliness. Mark which kind of comment was written. A variable-name suggestion isn't equivalent to a permission fix, even if both appear in the same discussion.

The GitHub documentation describes three review states: comment, approve, and request changes. The ability of a request-changes to block a merge depends on the branch protection rules. Merely writing the word "blocker" in a comment isn't a technical rule definition in the repository.

### Keep the discussion small enough to verify

When a change includes two separate mechanisms, you can ask for a split. In the public example, tab-group management and debugger handling were separated into two PRs. The split lets you check intent and evidence for each part without tying them into one package of changes.

Splitting is a working tool, not a goal in itself. If two parts must land together to keep behavior correct, document the dependency and the merge order. An agent can prepare the branches, but the decision about the shared contract stays with the change owner.

### Check what changed after the comment

Before approving, read the new diff and the added test. Make sure the test touches the behavior raised in the discussion, not just the way the current code is written. Ask for a run result, a version, and a command. A planned test list in a PR body is not a run result.

If the agent summarizes "all comments handled", return it to the original list. Every comment needs a fix, an explanation of why it isn't required, or a decision to defer it. A conversation that scrolled off the screen is not evidence the problem is solved.

### Finish with a decision you can reconstruct

A good fix connects the comment, the requirement, and the evidence. That way, whoever reads the PR later can understand why the change went in and what it's supposed to preserve. The goal of a review is to improve the behavior and give a way to check it, without turning the person receiving the comment into a guesser.

## From my experience

In my post about the real-browser-mcp contribution I told about a contributor who came back after review with two separate PRs and fixes for cases that came up in testing. This guide proposes a working method you can apply to another contribution, without assuming every change has already been tested.

## Frequently asked questions

### What's the difference between a comment and a request for changes?

GitHub supports comment, approve, and request changes as review states. Actual blocking depends on the branch rules, not only on the comment's wording.

### Can an agent handle all review comments?

It can prepare fixes and evidence within agreed boundaries. A design question or a contract change requires an explicit decision.

### When should you split a PR?

When there are separate mechanisms you can test separately. When there's a dependency, document it and the order the changes land.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-23

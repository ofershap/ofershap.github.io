---
title: "How do you translate a technical feature into an explanation for the marketing team with AI?"
published: 2026-10-09T12:56:40+03:00
updated: 2026-10-24
lang: en
canonical: https://ofershap.github.io/en/posts/feature-to-marketing-with-ai/
original: https://ofershap.github.io/posts/feature-to-marketing-with-ai/
---

# How do you translate a technical feature into an explanation for the marketing team with AI?

Give the agent the feature's changes and documents, ask for an explanation of the problem and the value to the user, and then check with the feature owner what is actually available before using the text externally.

## In depth

A developer thinks about implementation. A content person needs to explain who the feature helps and at what moment. The agent can prepare the draft that connects the two, as long as it gets the right source material.

### Prepare a source package
Pick the pull requests, the task description, the product documents and the tests related to the feature. State what is already merged and what is still open. If there is a usage limitation or a gradual rollout, attach that too. The distinction between planning and what is available right now matters especially in text that will reach customers.

### Ask for user value
An example prompt, for illustration:

"Analyze the attached changes and documents. Explain to a non-technical user what the feature does, which problem it solves, and when it is worth using. Separate available capabilities from work that is still open. For each major claim, state which source it rests on. If information is missing, mark it instead of filling it in yourself. Do not include code or infrastructure details in the user text."

### Check before publishing
Go over the draft with someone who knows the feature:

- Does the text describe the available version?
- Can the user perform the described action?
- Does the explanation leave out an important limitation?
- Is there a promised result that has no test behind it?

You can keep the source references in the internal document, and remove them from the customer version after the check. The goal is a clear explanation with a trail you can verify.

### Connect it to an existing process
At our place we used a dedicated Slack channel to start the work with Cursor. Per Cursor's current documentation, mentioning @cursor with a prompt can launch a Cloud Agent from inside Slack. The setup requires connecting a code provider, choosing a repository, a privacy check and billing settings. Check permissions and costs before connecting another team.

You can apply the same principle without Slack: prepare a source package, ask for a draft, check it, and hand it to the content team. The technical connection is chosen by the environment; the responsibility for correctness stays with the feature owner.

## From my experience

I wrote on LinkedIn about a process we ran in the team: we connected Cloud Cursor to a Slack channel, and the content person asked it to explain a feature from the commits, the pull requests and the documents. The interesting work was translating the development material into the language of users.

## Frequently asked questions

### What material should you give the agent?

Code changes, the task description, product documents and tests, with a clear distinction between merged work and open work.

### Who approves the text for customers?

The feature owner checks availability, limitations and claims. The content team adapts the text to the audience after the check.

### Do you have to connect Cursor to Slack?

You can prepare and check a draft without Slack. The connection is a way to start the work from inside the team's process.

## About the author

Ofer Shapira - The Israeli AI Agency - matching and installing AI agents for small businesses in Israel, in Hebrew, with long-term support.

Last updated: 2026-10-24

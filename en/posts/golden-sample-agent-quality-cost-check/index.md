---
title: "How do you check that a multi-agent process is worth its cost?"
published: 2026-10-17T13:00:00+03:00
updated: 2026-10-23
lang: en
canonical: https://ofershap.github.io/en/posts/golden-sample-agent-quality-cost-check/
original: https://ofershap.github.io/posts/golden-sample-agent-quality-cost-check/
---

# How do you check that a multi-agent process is worth its cost?

Build a small sample with known answers, run a single agent and a multi-agent process on it, and compare three metrics: how many of the right answers were found, how many errors were added, and what the cost was. Decide by the metrics, not by an impression from a demo.

## In depth

### Build a sample with known answers

Pick 10 to 30 items from the real material. For some items the right answer is known in advance: for example a document that contains a specific commitment, or a clean document with no finding at all. Write the answers down before any run.

Example: when testing 200 documents against a new policy, pick 20 documents, manually mark which commitments appear in them, and keep the list as an answer key.

### Run two setups on the same sample

One run with a single agent handling all items. A second run with a multi-agent process, for example reader agents, checker agents, and a report-joining step. Same items, same instruction, same model version.

### Measure three numbers

Accuracy: how many of the findings from the key were found in each run. Noise: how many wrong findings were added. Cost: tokens, run time, and how many repeat passes were needed.

In the Anthropic demo on Latent Space, a stock-list scan with a review stage cost much more than a single agent and also found more details in the example. That's the illustration of the tradeoff between cost and coverage. Your sample is what tells you whether the tradeoff pays off on your task.

### Decide by the result

If the multi-agent process found more correct findings at a cost you're willing to pay, expand gradually. If a single agent reached the same result, stay with it. For a small set of independent parts, even a simple script can be the answer.

### What to keep from the test

Keep the answer key, both reports, and the comparison table. When someone later asks why you chose one architecture over another, you have numbers from your task, not a quote from somebody else's demo.

## From my experience

In my post about Dynamic Workflows I mentioned an Anthropic demo on Latent Space: a multi-agent process that cost much more than a single agent and also found more. Before copying an approach like that to a real task, I build a sample of known answers and compare. Here is how the test is built.

## Frequently asked questions

### How big should a test sample be?

10 to 30 real items with known answers are enough for a first comparison. The goal is a signal on quality and cost, not statistical proof.

### What if a single agent and a multi-agent process reached the same result?

Stay with the single agent. It's simpler to run, maintain, and explain. Expand only when the sample shows a measurable gain.

### How do you measure the cost of an agent run?

Record tokens, run time, and the number of repeat passes for each run on the same sample, and compare against the accuracy gain you got.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-23

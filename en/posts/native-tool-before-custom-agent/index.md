---
title: "When should you pick an existing tool instead of building an AI agent?"
published: 2026-10-11T13:00:00+03:00
updated: 2026-10-23
lang: en
canonical: https://ofershap.github.io/en/posts/native-tool-before-custom-agent/
original: https://ofershap.github.io/posts/native-tool-before-custom-agent/
---

# When should you pick an existing tool instead of building an AI agent?

Start from the outcome and the constraints, check whether an existing tool meets them, and build an agent only for the gap that remains. Compare the whole process, including maintenance, permissions, and failure handling, not just the first demo.

## In depth

### Define the outcome before picking a tool

A request like "I need a bot to organize the tasks" already contains a solution. The outcome can be smaller: getting a clear list of open tasks with owners and dates. Sometimes a saved filter in the system that already exists is enough.

Write what needs to happen, who uses the result, where the data comes from, and which actions require approval. The distinction between reading and changing data matters even in a small process.

### Check the existing way on a real example

Example: a team wants an alert when a task is blocked. Before building an agent that searches conversations and updates tasks, you can check a blocking field and a built-in alert in the work management tool. If the system can't identify the reason from a conversation, that may be the gap where AI adds value.

The example is a suggested process, not a description of a client project. The check should use information you're allowed to share, and include a case with no change or no answer too.

### Compare the full process

An existing tool can save new code, but it also requires adaptation and permission checks. A custom agent can work across systems and understand free text, but you need to define what it does when the source is unavailable, when the reply is unclear, or when the action was already done.

Alongside the result, check human working time, errors, duplicates, ease of fixing, and ongoing cost. Don't present demo-building time as time saved in work. Also record separately the time the agent is only waiting.

### Build only the missing part

When an existing tool covers most of the way, you can keep the data and actions in it, and add an agent for one focused stage: summarizing a conversation, classifying a request, or suggesting the next step. That way you can test the addition without replacing the whole system.

In my public grok-bot-skills library, distill-need starts by identifying the need rather than sticking to the proposed solution. It's adapted from melech-distill-need by AdirD, with credit and license in the source. It's a useful framework for making a decision, not proof that every agent or every skill was tested in practice.

### Choose by evidence from the experiment

Continue with the option that delivers the outcome with clear boundaries and maintenance you can hold. If an existing tool is enough, that's a good engineering decision. If a clear gap remains, you can define a small agent task with a success check and a way back.

## From my experience

In my post about the wave of AI announcements I described an MCP tool for Jira that looked impressive, and then I found the plugin I already had was more convenient for my need. Since then this is a useful question before building: what's missing in the existing process, not which new tool can be added.

## Frequently asked questions

### How do you know if you really need an AI agent?

Define the outcome and check an existing tool on a real example. An agent is needed when a defined gap remains that the existing way doesn't cover.

### What do you compare in a small experiment?

Check the result, human working time, errors, duplicates, permissions, maintenance, and ongoing cost. Waiting time is recorded separately.

### Do you need to replace the existing system?

Sometimes it's enough to add an agent for a focused stage and keep the data and actions in the existing system.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-23

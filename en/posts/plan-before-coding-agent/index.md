---
title: "What should you decide before starting to build with a coding agent?"
published: 2026-10-09T12:56:40+03:00
updated: 2026-10-24
lang: en
canonical: https://ofershap.github.io/en/posts/plan-before-coding-agent/
original: https://ofershap.github.io/posts/plan-before-coding-agent/
---

# What should you decide before starting to build with a coding agent?

Define who will use the product, where it will run, who will maintain it, and how it reaches users. Then choose a tool and ask the agent to build a small experiment that validates the choice.

## In depth

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

## From my experience

In my post about consulting agents and coding agents, I told about a friend who started building in Claude Code and only near the end discovered the tool did not fit some of the requirements. From him came my principle: first figure out what you need to build and operate, then choose what to write the code with.

## Frequently asked questions

### What is the difference between a planning conversation and writing code?

The planning conversation clarifies requirements, constraints and alternatives. Writing the code implements a choice you can already test.

### Do you need an ADR for every small change?

The document is useful for a significant decision with alternatives and consequences. A simple local change can stay in the task description.

### What should the first experiment include?

The core action and the risk that needs validating, such as deployment or content editing by a user.

## About the author

Ofer Shapira - The Israeli AI Agency - matching and installing AI agents for small businesses in Israel, in Hebrew, with long-term support.

Last updated: 2026-10-24

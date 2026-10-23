---
title: "How do you give an AI agent a task that waits for a reply without creating duplicates?"
published: 2026-10-12T13:00:00+03:00
updated: 2026-10-23
lang: en
canonical: https://ofershap.github.io/en/posts/agent-wait-resume-without-duplicates/
original: https://ofershap.github.io/posts/agent-wait-resume-without-duplicates/
---

# How do you give an AI agent a task that waits for a reply without creating duplicates?

Define exactly what you're waiting to receive, when to stop waiting, and what needs re-checking before the action. Keep state and an identifier for the task, and verify the action is still needed when the reply arrives.

## In depth

### Turn waiting into part of the task

A task like "wait for a reply and then open a ticket" includes two different decisions. The first is identifying a relevant reply. The second is deciding whether a ticket is still needed. Between the request and the reply, a lot can change: someone else already handled it, a constraint was added, or the reply refers to a different request.

Write what the source is, which conversation or task it belongs to, and which reply allows continuing. A reply like "yes" without the context isn't a sufficient condition. Also keep the boundaries of the permitted action, instead of re-interpreting the consent hours later.

### Keep state you can return to

A short work record can hold a task identifier, the original request, the awaited source, the continuation condition, and the last verified state. Worth separating "waiting", "reply received", "current state checked", and "action completed".

Example: a request to collect a reply about a fault can stay in waiting state. After a reply that a ticket is sufficient, the agent checks whether a matching ticket exists. Only after creating or using an existing ticket and verifying the link can the task be marked completed. The example describes process design, not the outcome of a specific system.

The identifier should stay fixed even when an event is delivered twice. That way you can recognize a repeated delivery of the same reply instead of starting a new task.

### Re-check before acting

Before creating or updating, go back to the system where the action happens. Check whether the result already exists, who handled it, and whether the request is still valid. Memory of the state from before the wait is no substitute for this check.

If an earlier attempt ended without a clear response from the server, look for the result first. A timeout is not proof the action failed. Retrying without checking can create a duplicate precisely when the first action succeeded.

### Set an end to the wait

Write when the wait ends and what happens then: report to the task owner, close without action, or ask for a decision. A no-reply message should distinguish a source that didn't return a reply from a source that wasn't reachable.

When implementing part of the process in GitHub Actions, you can use concurrency to prevent overlapping runs in the same group. That's an execution mechanism, not a check that the business action hasn't happened yet.

It's important to read the queue behavior: a group's default allows one active run and one pending run, and a new pending run can replace the previous one. A setting that cancels an old run sometimes fits code testing, but can be wrong when every request needs handling. Even execution order is no guarantee of the order requests arrived.

### Test a duplicate event and a late reply too

The first experiment should include a reply on time, a reply after closure, the same reply twice, and a case where someone already performed the action. In each case, check the result in the system, not just the message the agent returned.

Success is one correct action, or a correct decision not to act, with state you can understand in hindsight. Merely receiving the reply is only a step along the way.

## From my experience

In my post about waiting in a thread I described a request to Grok Bot to wait for a reply, then handle it if a ticket was sufficient. When the reply came, it found an existing ticket and returned it instead of opening a duplicate. This guide translates that case into a decision list you can check in another process.

## Frequently asked questions

### What should you define before the agent starts waiting?

A source and identifier, a reply that allows continuing, the action boundaries, an end to the wait, and a last verified state.

### Does concurrency prevent duplicate tickets?

It can prevent overlapping runs, but it doesn't prove a ticket wasn't created yet. You need to check the system before acting.

### What do you do when a creation attempt ended in a timeout?

Check whether the result exists before retrying. No response is not proof the action failed.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-23

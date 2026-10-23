---
title: "How do you ask a coding agent to fix a bug with a regression test?"
published: 2026-10-12T13:00:00+03:00
updated: 2026-10-23
lang: en
canonical: https://ofershap.github.io/en/posts/regression-first-agent-bugfix/
original: https://ofershap.github.io/posts/regression-first-agent-bugfix/
---

# How do you ask a coding agent to fix a bug with a regression test?

Keep a way to reproduce the failure before the change, define the wanted behavior, and ask for a small fix. The same test should catch the fault in the old code and pass on the fixed code, alongside tests for error scenarios.

## In depth

### Start from a reproducible failure

A description like "the screen sometimes breaks" leaves the agent too many options. Attach the input, the action performed, the expected result, and the actual result. Note version and environment when they affect the behavior. Remove private information from the example.

If the failure depends on timing or an external service, document what's known and what's still a hypothesis. Difficulty reproducing is important information, not a reason to present a fix as if the fault were already understood.

### Preserve the failure before touching the code

Ask the agent to add a focused test or a reproduction command and run it on the old version. Keep the output and the code version. A test written only after the fix can end up testing what the agent implemented instead of what the user needs.

Example: a function should read a settings file, but new exception handling returns an empty dictionary even when the file is missing. The regression test should demand the agreed error behavior, not settle for the function returning a dictionary. This is a suggested example, not a description of a client fault.

### Separate the environment from the behavior

In the pytest documentation, the fixture called tmp_path gives a separate temporary folder per test. You can create a valid file, a corrupt file, and a path that doesn't exist in it, without using personal files or the regular working directory.

The monkeypatch tool lets you temporarily change environment variables, attributes, or a function's behavior. The changes are undone when the test or fixture ends. It's useful for isolating an external dependency, but the result still depends on the substitute representing the interface correctly.

A test with a service substitute is not a connection test to the real service. State separately what was verified locally and what still needs an integration test. For temporary folders, use the safe defaults. An option like basetemp deletes the contents of the folder set for it, so it doesn't fit a path holding material you want to keep.

### Give the agent boundaries for the fix

You can use this request as an illustration:

> First reproduce the fault and keep a test that fails for the right reason. Explain the hypothesis and propose a small fix. Preserve the interface and the agreed error behavior. At the end show the diff, the commands, and the actual results, and what hasn't been tested yet. Any additional change beyond the fix requires a separate decision.

The boundaries prevent an overly broad solution: replacing a library, changing an output format, or hiding an exception can make the test pass without solving the original need.

### Check that the test really distinguishes the versions

Make sure the test fails on the old code because of the fault, not because of a missing dependency or an installation error. Then run it on the fix. If possible, temporarily check the test against the old version too, to confirm it still catches the failure.

Also run tests adjacent to the changed interface. A fix for file reading should address valid input, a missing file, and corrupt input per the function's contract. The list depends on the fault, and is no substitute for understanding the code.

### Return a result with evidence boundaries

At the end, keep the code version, the run commands, the result, and the limitations. Write "these tests passed" instead of "everything works". A change covering a local fault can still leave questions about another environment, large data, or an external service.

The role of a regression test is to leave evidence you can run after the conversation with the agent. It helps keep the fix as the code keeps changing.

## From my experience

In my post about moving from ask agent → hope to a working process I presented bug diagnosis as a sequence: reproduce, narrow down, hypothesis, measurement, and fix. Here I focus on the evidence that remains after the fix: a test that catches the old failure.

## Frequently asked questions

### Is it enough that the agent wrote a passing test?

You need to verify the test catches the fault on the old version and passes on the fix. Green output alone doesn't prove that.

### How do you test files without touching private data?

You can create synthetic inputs in a separate folder per test using tmp_path. Pick examples that represent the interface.

### Does a mock replace an integration test?

It isolates a dependency and allows a focused test. The connection to the real service remains a separate test, and you should state if it wasn't done.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-23

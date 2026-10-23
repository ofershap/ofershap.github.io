Title: Which boundaries do you set before running dozens of AI agents in parallel?

**Short answer:** Four boundaries: a session budget, minimal permissions, a full coverage list, and output checked against a criterion. Write them before the first run, test on a small sample, and only then increase parallelism.

### Budget: set at session opening

In Claude Managed Agents you set the budget when creating the session. You can't add a budget to a session that's already running. When the session reaches the budget, runs are paused. Requests that already started can complete and exceed the budget. A run paused over budget resumes when you raise or remove it.

Example: in a session checking 200 documents against a new policy, set a budget that covers one full pass plus a little for repeat checks. If the run stops midway, you know the initial estimate was too low.

### Permissions: start read-only

The ability to split work among agents is no reason to give every agent permission to change data or send messages. Every thread inside the session has its own event stream, and tool permissions can be managed per thread.

A good opening check: reader agents return findings only. Only one stage, if any, gets write permission, and it's limited to a single destination.

### Coverage: a closed list of items

Define upfront the list of items the run should handle. Every item ends in one of two states: checked, or not checked with a reason. A report that looks complete without a coverage list is not evidence.

The Dynamic Workflows documentation lists system limits: up to 64 threads in parallel per run, and up to 1,000 agents over a run's lifetime. Those are technical ceilings. A useful starting point is on the order of dozens of items and a few agents.

### Verification: completed is not a sign the work succeeded

The documentation states explicitly: a completed status means the plan finished. It doesn't mean all the work succeeded. Check the output itself against a criterion defined upfront: how many items were covered, how many findings verified, how many rejected and why.

### A suggested working order

1. Write the four boundaries into the task itself, before the run.
2. Run on a small sample with known answers.
3. Compare output, coverage, and cost against a single agent.
4. Increase parallelism only after the metrics show a real gain.
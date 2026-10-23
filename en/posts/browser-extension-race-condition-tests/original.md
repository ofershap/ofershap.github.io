Title: How do you test race conditions in a browser extension an AI agent is changing?

**Short answer:** Define what must stay true when operations overlap, control their completion order in the test, and add a real-browser scenario. A test where two calls run one after the other doesn't prove the code handles overlap.

### Define the guarantee before writing the test

A browser extension connects local code to state that changes outside it. A tab can close, a group can change, and a debugging connection can end. So you need to ask what must hold between the start of an operation and its end.

In the public contribution to real-browser-mcp there was a case where two requests for a group name on the same tab could create two groups. PR number 71 describes a fix that serializes operations per tab and re-reads the tab state inside the lock. That's a concrete example of the same gap: the state read before the wait may be stale when the operation starts.

### Create overlap you can repeat

A synthetic illustration: two requests see a tab with no group. Each prepares to create a group. In a test you can hold the first call's promise open, start the second, and only then let the first complete.

At the end, check how many times group creation ran and what the tab's final state is. If the requirement is one group, two "success" results aren't enough. Ask the agent to show that under the same operation order the old version fails and the new one meets the requirement.

The example is a suggested way to test. The completion order should represent the real interface, not a substitute that only allows the order convenient for the code.

### Lock on the right resource

A per-tab lock can fit operations on the tab's group. A resource shared by the whole extension needs different thinking. PR number 72 describes a single queue for acquiring and using a debugger connection, to prevent two overlapping acquisitions with partial tracking.

The choice isn't "add a mutex" across the board. Define which operations share state, what can run in parallel, and when the protection is released. Also test an error inside the operation: a failure should leave a way for the next operation to proceed per the contract, not jam the queue.

### Separate an external signal from connection ownership

According to Chrome's documentation, a debugger connection that fails rejects the promise. An onDetach event arrives when the browser ends the session, for example when the tab closes or when DevTools opens on the connected tab.

A message about another debugger is not proof your extension holds the connection. PR number 72 describes a probe that tries to distinguish a connection the extension still holds after worker initialization from a connection failure. Both paths should be checked against the behavior the code actually implements.

### Add a test at the Chrome boundary

A unit test with a mock can control overlap and count calls. It doesn't prove that permissions, browser messages, and close events behave as you expected.

As suggested scenarios, check two overlapping requests, a tab closing mid-operation, and DevTools opening during a session. An extension using the debugger needs the debugger permission in the manifest. Using the tabGroups API requires the tabGroups permission. Match the permissions to the actual implementation, and don't add a permission just to make a test pass.

### Ask for a report that separates layers

At the end, the agent should state what was tested with a mock, what was tested in a browser, what the event order was, and on which version the test ran. There's no need to promise coverage of every possible race. There is a need for evidence of the discovered scenario and clear boundaries for what still needs testing.
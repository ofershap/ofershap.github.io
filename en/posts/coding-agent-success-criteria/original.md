Title: How do you define for a coding agent what counts as success?

**Short answer:** Attach to the task a result you can check, change boundaries, required tests, and who approves completion. The agent should return evidence from the run, alongside what wasn't checked.

When you ask to "fix the bug", the agent can pick a solution that looks reasonable but changes behavior nobody meant to change. A good definition narrows the choice before the code is written.

### Define behavior, not just a file to edit

Write what the user or the calling code should receive. For example, as an illustration: a file-reading function should return the same data after the fix. A missing or corrupt file should keep returning an error to the caller. Returning an empty dictionary instead of an error is not a fix of the same behavior.

### Give the test a chance to fail

Keep a case that shows the fault before the fix. The same test should pass after it. A test that passes on the original code too is not evidence this fault was fixed.

A public example from the DDD project illustrates the difference. A Python function passed tomllib.load a file opened in text mode. The experiment record documented a TypeError before the change. The fix was to open the file in binary mode, "rb", as the Python 3.11 documentation requires. After the fix two tests passed, and an additional test confirmed a corrupt TOML file still raises TOMLDecodeError. That's an experiment by the project's author, not mine and not a measure of time savings.

### Separate success from permissions

Write what may be changed and what stays outside the task: public interface, dependencies, secrets, other files, or deployment. You can allow a fix and running tests in a trial folder without allowing a global install or publishing.

An instruction file can remind the agent of the boundary. It doesn't replace access permissions, environment separation, or approval from whoever owns the system.

### Ask for a completion you can check

An illustrative template:

"Fix this fault without changing the public interface. Keep a test that fails on the original code and passes after the fix. Check the error behavior too. Edit only the permitted files, with no new dependency and no deployment. At the end show the change, the commands you ran, the actual results, and what remains untested."

In the completion report I want to distinguish four things: code written, a test run, an observed result, and approval for use. Those are different stages. You can complete the local fix and still wait for review or another environment check.

### Decide what happens when the test fails

Set upfront whether the agent may try another fix, should stop, or must return to a stable version. Also define when to turn to a human: missing information, a deviation from the permitted files, or a change touching real data.

That way the same task can move to another agent without losing its wanted result and boundaries.
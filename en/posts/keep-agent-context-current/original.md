Title: How do you keep context files and Cursor rules up to date?

**Short answer:** Check claims against the current code, tie the check to a change that could age them, and distinguish a real fault from an example or a historical document. The agent reports only a gap it can explain and prove.

A wrong rule attached to every task can mislead the agent again and again. A context file is part of the development process, so it needs maintenance too.

### Start with what's actually loaded

Pick claims you can verify: a package location, a test command, a service name, a path, or a component count. For each claim, look for a source in the code, a config file, or current documentation. If there's not enough source, mark "needs checking" instead of declaring the claim wrong.

### Check the rule type

Per Cursor's current documentation, project rules are kept in .mdc files under .cursor/rules. Fields like description, globs, and alwaysApply determine when the rule is attached. A rule with alwaysApply: true is included in every conversation, so a stale claim inside it gets wide distribution.

For a rule that applies to only part of the code you can set matching file patterns. For a simple instruction document you can use AGENTS.md. Check that the format and location fit your tool, not just that the file exists in the repo.

### Give the scan context

A path that doesn't exist is the start of a check, not a conclusion. It could be an example, output generated at runtime, content excluded from git, or a plan kept for history.

Check next to every finding: what the document tries to explain, whether the file was supposed to exist now, and whether the current change broke the reference. You can keep a historical document and mark it as such instead of rewriting it as if it describes the system today.

### Tie the update to the change

When a service is added, a folder structure changes, or a test command is replaced, check the instructions describing it in the same change. A review close to the changed code gets more context than a general scan months later.

The Cursor documentation recommends pointing to canonical examples instead of copying content that already exists in the code. A reference reduces duplication, but you still need to check that it's valid and that the example itself fits.

### Ask for a short report with evidence

An illustrative prompt:

"Check the context files related to this change. For every gap, show the sentence in the document and the current source that contradicts it. Distinguish an example, a historical document, and a fault. Propose a small fix only when there's evidence. If everything is fine, finish without unnecessary comments."

Silence isn't skipping the check. It's a valid result when the agent found no gap worth the team's attention.

### Check that the rule helps

After an update, try a small task the rule should apply to. Verify the agent uses the updated path, command, or instruction. Merely saving the file doesn't prove the tool loaded it or that the instruction improved the result.

Start with a few rules that recur in the work. Add a rule when a repeated mistake is found, and remove duplication already handled by code or a checking tool.
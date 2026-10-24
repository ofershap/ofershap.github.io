---
title: "How do you keep context files and Cursor rules up to date?"
published: 2026-10-10T12:53:36+03:00
updated: 2026-10-24
lang: en
canonical: https://ofershap.github.io/en/posts/keep-agent-context-current/
original: https://ofershap.github.io/posts/keep-agent-context-current/
---

# How do you keep context files and Cursor rules up to date?

Check claims against the current code, tie the check to a change that could age them, and distinguish a real fault from an example or a historical document. The agent reports only a gap it can explain and prove.

## In depth

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

## From my experience

In my post about context files I told how a check on a project found a description of six SDK packages when there were actually ten. Later, a scan surfaced 124 references that looked dead, and only four were a real problem. Those are numbers from that one case, not an error rate you can project onto other teams.

## Frequently asked questions

### When should you check that context files are current?

When a code change affects the structure, services, or work commands described in them, and in a periodic review of rules that always apply.

### Is every reference to a missing file a fault?

No. Check whether it's an example, output generated at runtime, content excluded from git, or a historical document.

### What's the difference between an .mdc file and AGENTS.md?

In Cursor, .mdc files under .cursor/rules include metadata for scope control. AGENTS.md is a simple alternative in Markdown format.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-24

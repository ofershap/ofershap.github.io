Title: How do you turn code review comments into rules Cursor can use?

**Short answer:** Collect comments that repeated across several pull requests, check the team actually agrees on them, and then write short, focused rules inside the repo.

A comment like "we already said you need to validate the input here" is a sign of team knowledge that never reached the place the agent reads. The goal is to move that knowledge into rules you can check and change.

**1. Collect evidence, not just phrasings.** Pick human comments from merged PRs. Check what changed following the comment. Repetition across several PRs is stronger evidence than two comments in the same discussion.

**2. Separate a convention from a momentary preference.** A recommendation that is right for one file may be wrong in the rest of the system. Next to each rule, keep a link to examples and to the original discussion, and someone from the team reviews it before use.

**3. Write a rule you can act on.** Instead of "write quality code", write what to check, when, and which file has a correct example. This is a suggested phrasing, not a client rule: "In new API routes, validate input before calling the database, following the pattern in the project's example file".

**4. Keep the rule in the right place.** Per Cursor's documentation, project rules are stored as `.mdc` files inside `.cursor/rules` and managed in Git. A rule can be applied by file type, by relevance, or manually. That way the whole team works against the same source, not against one developer's private prompt.

**5. Start small and test on real code.** Cursor recommends keeping rules focused, under 500 lines, and splitting topics. That is a guiding bound for a rule, not a target to fill. A short rule that prevents a repeating mistake beats a procedures book the agent struggles to apply.

In the documented pr-rulebook experiment, 15 PRs and 45 human review comments were scanned in the Ruff project. Two candidate rules were found, and only one passed testing. A good reminder: repetition in text is the start of a check, not an automatic approval to enforce a rule.

**When is this a fit?** When a team repeats the same comments over and over, and when it already uses Cursor or a coding agent. The rules help transfer context, but they do not replace tests and human review.

I accompany teams in building work rules, code review and AI tool adoption. Details: https://israeli-ai-agency.pages.dev/services/ai-native/ .
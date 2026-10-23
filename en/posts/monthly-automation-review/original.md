Title: How do you check after a month that the automation really works?

**Short answer:** Don't assume it ran. Open the actual output, compare it to what the automation was supposed to produce, and decide for each component: keep, change, or stop. Without comparing to real output, an automation can stop quietly and nobody notices.

### Why automations stop quietly

Most automations don't alert when they stop. A third-party service changes a permission, a process crashed and nobody restarted it, or the output keeps being produced but never reaches its destination. From the outside everything looks fine, because nobody looks at the output itself.

In the post I published I told how my meeting recordings stopped for a whole week, and I found out only when I asked the bot what it did with the material. That's exactly the problem: the check started only when someone asked.

### An end-of-month checklist

For each automation, three questions in order:

What was it supposed to produce? A concrete output: a recording per meeting, a daily summary, an updated file. If you can't phrase the output in one sentence, the automation isn't defined well enough.

What was actually created? Open the latest output itself. Not the log, not the settings. The artifact you were supposed to use.

What's the decision? For each component, one of three: keep, change, or stop. An automation whose output nobody reads costs more than it gives.

Example: an automation meant to summarize ten meetings a week. The review finds summaries for only six. Check the missing four: two meetings were canceled, one wasn't recorded because of a permission, and one was recorded but never sent. The decision: fix the permission and add an existence check for the output, not replace the tool.

### When to change and when to stop

Change when the output arrives but isn't usable: an inconvenient format, too-high frequency, noise instead of signal. Stop when usage has disappeared even though the output is fine. A review that ends without a single stop is a sign the list wasn't really made, or the check was shallow.

My full list for a review like this - what to keep, what to change, and what to stop - also went into my public skills library, so it can be run again and again without rewriting.
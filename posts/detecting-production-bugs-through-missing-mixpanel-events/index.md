# Detecting production bugs through missing Mixpanel events

July 2, 2026 · 1 min read

Originally posted on LinkedIn , July 2, 2026.

Tehila Adika, an excellent product manager from another team, found a bug in one of our buttons. It had been Disabled for weeks, and nobody had noticed. A bug had been in production for days without triggering a single alert.

These bugs work in the opposite way from the ones we usually monitor. If a tree falls in a forest and nobody hears it, did it make a sound? The same question applies to bugs caused by “dead code.”

When a button is Disabled for everyone, the system does not report an error. Instead, it goes quiet. You can detect that silence by looking for a drop in events.

I added a daily Mixpanel scan for cases with “zero daily events.” The scheduled script looks for anomalies and drops in events. I also added checks for spikes in the opposite kind of events: errors reported to Mixpanel. When it finds either, it posts to a dedicated monitoring channel.

If there are no drops, errors, or other problems, the script stays silent, just like the falling tree.

Bugs reported by customers are the worst kind. We could have caught them before they reached dozens of customers. They damage trust and create noise from support all the way to the developer who has to fix them in a cold sweat.

Every user report is an opportunity to improve the system’s alerting, even when the right alert works in the opposite direction from the usual threshold of errors .

Thanks to Tehila Adika for the inspiration.

Original source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%96%D7%94-%D7%A4%D7%93%D7%99%D7%97%D7%94-%D7%AA%D7%94%D7%99%D7%9C%D7%94-%D7%9E%D7%A0%D7%94%D7%9C%D7%AA-%D7%94%D7%9E%D7%95%D7%A6%D7%A8-%D7%94%D7%AA%D7%95%D7%AA%D7%97%D7%99%D7%AA-activity-7478355878308397056-_lmb


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

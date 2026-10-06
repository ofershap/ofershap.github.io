# An agent turns every merge into a release update

June 29, 2026 · 1 min read

Originally posted on LinkedIn , June 29, 2026.

Since I added this, the product and support teams have stopped asking me for updates.

One of the most painful gaps in any engineering organization is the difference between what developers merge into production and what everyone else knows. Product, support, marketing, and the help center all need to know what shipped and when. They depend on a developer stopping their work to explain it in language they understand.

Communicating the work is a big expectation to place on engineers. To put it mildly, not everyone has that skill.

I found a simple way to close the gap. I added a cloud agent to our CI pipeline that runs automatically whenever code is merged into master. It reads the merged code and the PR description, translates them into clear language from a product perspective, and posts the result to a dedicated Slack channel. If the developer attached a Loom video, that is included too.

It works better than I expected. Every message gives a simple, accurate explanation of the feature, often better than I could describe what went into production myself.

We are already a large group, with dozens of features shipping every day. This channel keeps everyone in sync without anyone stopping to write an update. The help center stays current. Support turns the updates into answers and videos. Marketing uses them for the newsletter and other content. Product can try features behind a feature flag as soon as the update appears.

The number of messages asking, “Has this shipped yet?” has dropped to zero. That saves developer time and gives end users better, more current information. It all comes from one simple agent in the build pipeline doing one job: translating code into human language without missing anything or getting tired.

Original source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%90%D7%96-%D7%A9%D7%A2%D7%A9%D7%99%D7%AA%D7%99-%D7%90%D7%AA-%D7%96%D7%94-%D7%94%D7%A4%D7%A8%D7%95%D7%93%D7%A7%D7%98-%D7%95%D7%94%D7%AA%D7%9E%D7%99%D7%9B%D7%94-%D7%9C%D7%90-%D7%A4%D7%A0%D7%95-%D7%90%D7%9C%D7%99-activity-7477348241332830209-D4JJ


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

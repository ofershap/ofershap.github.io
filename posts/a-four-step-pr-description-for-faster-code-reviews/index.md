# A four-step PR description for faster code reviews

July 29, 2026 · 1 min read

Originally posted on LinkedIn , July 29, 2026.

The bottleneck has moved from writing code to reviewing it. A large part of a development team's work is now judging what was built and how it was built.

One thing that has made this easier for me and my team is giving the agent that writes the PR Description a four-step structure. This works whether the agent runs as a command in Cursor or through LinearB's GitStream:

- What problem are we solving?

- What changed, where, and in which files?

- How does it work in practice? Describe the flow.

- What are the risks?

When the PR Description includes this level of detail, understanding the code becomes much faster and easier. I already know what I expect to find in the code itself. Sometimes I can even spot architectural issues or risks raised by the agent before reading a single line of code.

This worked so well for us that when I shared it with the other team leads, they decided to adopt it across all of R&D for every new PR.

Original source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%9A-%D7%A0%D7%9C%D7%97%D7%9E%D7%99%D7%9D-%D7%91%D7%9E%D7%A6%D7%91-%D7%94%D7%96%D7%94-%D7%A9%D7%99%D7%A9-%D7%A4%D7%AA%D7%90%D7%95%D7%9D-%D7%9B%D7%9C-%D7%9B%D7%9A-%D7%94%D7%A8%D7%91%D7%94-activity-7488097566912364545-K7N5


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

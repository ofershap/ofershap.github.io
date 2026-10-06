# Portless gives local development readable URLs

March 4, 2026 · 1 min read

Originally posted on LinkedIn , March 4, 2026.

Vercel released Portless , a new local development tool. Instead of addresses like localhost:3000 , it lets you use readable names such as app.localhost or api.localhost .

Behind the scenes, Portless creates a local proxy that maps those names to the correct ports on your machine. You no longer need to remember port numbers, and the addresses stay readable and stable even when a port changes.

This also mirrors production environments that use subdomains, and it works better with automation and AI agents. Portless does not expose the application to the internet. It simply makes local development more organized.

Original source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%A4%D7%AA%D7%97%D7%99%D7%9D-%D7%96%D7%94-%D7%91%D7%A9%D7%91%D7%99%D7%9C%D7%9B%D7%9D-vercel-%D7%A9%D7%97%D7%A8%D7%A8%D7%95-%D7%9B%D7%9C%D7%99-%D7%97%D7%93%D7%A9-%D7%9C%D7%A4%D7%99%D7%AA%D7%95%D7%97-activity-7434841649995730944-30cG


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

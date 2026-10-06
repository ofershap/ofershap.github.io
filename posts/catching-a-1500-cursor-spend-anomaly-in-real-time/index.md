# Catching a $1,500 Cursor spend anomaly in real time

March 5, 2026 · 1 min read

Originally posted on LinkedIn , March 5, 2026.

A developer spent $1,500 in a single day without realizing it. Worse, nobody else knew either.

We use Cursor through a shared Enterprise account, with one budget that every developer draws from. Keeping that budget under control is a challenge many companies now face.

The number of available models also keeps growing, which makes it hard to tell which model is better and which is cheaper. The developer innocently chose a model that sounded less expensive because its name included “Fast.” In practice, it cost 10 times more than the others.

That was an expensive lesson. I decided to build a tool that monitors Cursor usage, detects anomalies and budget overruns in real time, and reports them in Slack.

Beyond monitoring, it shows adoption across the organization, identifies empty seats where we are paying for unused subscriptions, helps developers improve their usage, compares teams, and shows the real costs of the models being used.

The tool helped us decide which models to block, understand which ones cost more or less, and teach the engineering department how to use Cursor more effectively.

I built it as open source so anyone dealing with the same problem can deploy it. The repository is available here .

Original source: https://www.linkedin.com/posts/ofershap_%D7%94%D7%9E%D7%A4%D7%AA%D7%97-%D7%94%D7%96%D7%94-%D7%A9%D7%A8%D7%A3-1500-%D7%91%D7%99%D7%95%D7%9D-%D7%90%D7%97%D7%93-%D7%91%D7%9C%D7%99-%D7%9C%D7%93%D7%A2%D7%AA-%D7%90%D7%AA-activity-7435246819657342976-0jYE


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

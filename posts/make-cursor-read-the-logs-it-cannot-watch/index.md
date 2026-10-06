# Make Cursor read the logs it cannot watch

September 8, 2025 · 1 min read

Originally posted on LinkedIn , September 8, 2025.

Cursor and other coding agents cannot see CLI output the way we do. Errors may appear directly on the screen or hide inside long lines of logs, but an agent cannot listen to those logs in real time, follow Tail, or automatically react to Watch Mode. If it made that kind of call, it would get stuck waiting for the process to finish.

That leaves a gap when an agent runs code for us. How do we make sure an automated run has not broken something? The answer is not MCP for the CLI.

My solution is simple. I changed my npm command to write its logs to a file. In my case, they go into a logs/ directory because the project has more than one environment, and that directory is listed in gitignore. I used the Tee command, which is similar to the better-known Tail, to write the logs.

I also added a Cursor Rule telling the agent to check these files after writing code or while debugging. At the end of each run, it now checks them for exceptions, warnings, or errors that otherwise slipped under the radar.

No complicated MCP setup and no external tools. Just logs written to a file. Sometimes one log file can tell you what a coding agent cannot see.

Original source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%A9%D7%AA%D7%9E%D7%A9%D7%99%D7%9D-%D7%91-cursor-%D7%94%D7%A0%D7%94-%D7%98%D7%99%D7%A4-%D7%96%D7%94%D7%91-%D7%A2%D7%91%D7%95%D7%A8%D7%9B%D7%9D-%D7%9B%D7%A9%D7%90%D7%A0%D7%97%D7%A0%D7%95-activity-7370712595852525569-wFyr


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

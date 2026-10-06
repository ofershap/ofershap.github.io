# Using Cursor? Here's a golden tip for you:

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

Using Cursor? Here's a golden tip for you:
When we run commands through the CLI, errors happen. Sometimes they're thrown to the screen, sometimes they hide inside long lines of logs. 

But what happens when we work with Cursor or other smart agents that run the code for us?

A gap forms here. The agent doesn't "see" what we see. It can't listen to logs in real time, can't follow a tail, and doesn't react automatically to Watch Mode.

That's not a bug - it's simply not part of its way of working. If it performed such a call it would "get stuck" and wait until it finished.

So how do you still make sure an automatic run doesn't break something?
And no, the answer isn't an MCP for the CLI 😄 

The solution I found is simple:
I wired my npm command to write its logs into a file (in my case inside a logs/ folder because I have more than one environment in the project) and the folder is of course set in gitignore. 
I used the Tee command (similar to the better-known Tail) to write the logs.

In addition, I added a Cursor Rule that asks it to check these files when it finishes writing code or when investigating faults.

So now at the end of the run, a proactive check of these files is performed to detect anomalies, warnings or errors that slipped under the radar.

No MCP complications, no external tools, just logging to a file.
Sometimes, what a smart agent doesn't see - a single log file can tell.

Original: https://ofershap.github.io/posts/make-cursor-read-the-logs-it-cannot-watch/
Source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%A9%D7%AA%D7%9E%D7%A9%D7%99%D7%9D-%D7%91-cursor-%D7%94%D7%A0%D7%94-%D7%98%D7%99%D7%A4-%D7%96%D7%94%D7%91-%D7%A2%D7%91%D7%95%D7%A8%D7%9B%D7%9D-%D7%9B%D7%A9%D7%90%D7%A0%D7%97%D7%A0%D7%95-activity-7370712595852525569-wFyr
Published: 2025-09-08T10:00:24.069000+03:00

# Everyone is talking about background agents, I built a foreground agent.

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

Everyone is talking about background agents, I built a foreground agent.
Cursor, ChatGPT and others offer the option of running a "code agent" that runs autonomously behind the scenes. There are a few problems with this - one is that you can't see what is actually being done, the second is that it requires Privacy approvals, and the third is that it has additional costs.

Since I already work with Cursor on a regular basis, and I needed to run a complex task, I found a solution that would save me the need to sit and approve every step in Cursor's process -
and it wasn't complicated at all.

I opened Cursor's Developer Tools through the Help menu, asked ChatGPT for a small JS script, and pasted it into the console. 

The script: every time messages appeared asking me to approve something - "accept", "run", "25 tools limit" - it clicked them for me.

The method: I copied the HTML that represented the button area, and asked in the prompt for a script that every 15 seconds samples whether it appears and if so clicks. I also like to explain what it's for - "so I can paste it into Cursor's Devtools". It always helps to give the AI context. 

The result: I gained work continuity, almost identical to a Background agent, but under my control.

So instead of using an Agent that is "in the background", I built one that is simply in front of me - clicks on my behalf, and lets me truly flow.

It's fun to re-engineer the boundaries of the interface itself, and amazing to see that it worked smoothly - a few minutes later I came back to the computer to find that my task had been completed successfully and in full.

One last small and important note: this is great for small projects and for vibe-coding style development (without needing to follow the quality of the code output) but can be destructive for changes to existing projects. 
In addition, it can get out of control very quickly and wastes tokens.
So if you imitate the method - use it wisely and carefully, and even if it runs on its own - keep track of everything it does.

Original: https://ofershap.github.io/posts/linkedin-7355484666633641984/
Source: https://www.linkedin.com/posts/ofershap_%D7%9B%D7%95%D7%9C%D7%9D-%D7%9E%D7%93%D7%91%D7%A8%D7%99%D7%9D-%D7%A2%D7%9C-background-agents-%D7%90%D7%A0%D7%99-%D7%91%D7%A0%D7%99%D7%AA%D7%99-activity-7355484666633641984-KicT
Published: 2025-07-28T09:30:02.822000+03:00

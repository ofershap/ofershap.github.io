# As a development team lead, one of the most useful things I've been doing lately is analyzing my team's Pull Requests with AI.

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

As a development team lead, one of the most useful things I've been doing lately is analyzing my team's Pull Requests with AI. 

I ask Cursor or Claude Code (connected to our repo via the GitHub CLI) to analyze the PRs (that is, it actually runs gh pr list with search commands) and return insights like - 
Performance: analyze the last sprint (or quarter), who touched the code most in a certain area, where the bottlenecks are, who does more reviews, who makes more bugs, etc.
Or fault analysis - locate the smoking gun that caused a production incident or a rise in errors we identified in our observability tools. 

This ability gives a clear picture of what each person did, where they contributed, and where they got stuck, and makes me a much more precise and data-based manager. 

I keep arguing this - we are in an era of moving from being Data driven to AI Driven. If data analysis and drawing conclusions required hours or days of investment and were reserved for analysts and mainly served product people, today any role holder can analyze almost effortlessly the data close to their needs and get digested, smart insights that serve and sharpen them.

The latest case I had prompted me to write this post. In real time I saw a fault in production, asked the model to locate the fault in the GCP logs, then go through all the PRs of the last two weeks and pinpoint exactly which change caused the problem. A kind of smoking gun that without AI would have taken hours to find and involved at least one developer if not more in this research.

When today you can simply ask a question in natural language and get an answer within seconds, team leads suddenly have a management tool that didn't exist before. This mindset shift of having an analysis and research tool in hand and not just a "code completion" tool is an enormous value that lets us be super-managers.

Original: https://ofershap.github.io/posts/using-ai-to-analyze-my-teams-pull-requests/
Source: https://www.linkedin.com/posts/ofershap_%D7%91%D7%AA%D7%95%D7%A8-%D7%A8%D7%90%D7%A9-%D7%A6%D7%95%D7%95%D7%AA-%D7%A4%D7%99%D7%AA%D7%95%D7%97-%D7%90%D7%97%D7%93-%D7%94%D7%93%D7%91%D7%A8%D7%99%D7%9D-%D7%94%D7%99%D7%95%D7%AA%D7%A8-%D7%A9%D7%99%D7%9E%D7%95%D7%A9%D7%99%D7%99%D7%9D-activity-7474342688310472705-v1mV
Published: 2026-06-21T09:09:23.465000+03:00

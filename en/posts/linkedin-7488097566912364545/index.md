# How do you fight this situation where suddenly there is so much code that has to be gone through and reviewed?

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

How do you fight this situation where suddenly there is so much code that has to be gone through and reviewed?
The bottleneck has moved from writing the code to reviewing it, and a lot of the dev team's work is judging what was developed and how it was developed.

One of the ways I found that makes things easier for me and the team is to add instructions to the agent that writes the PR Description (whether it's a command in Cursor or through LinearB's GitStream) following a 4-step methodology:

1. What problem we set out to solve 
2. What changed and where (which files)
3. How it works in practice (the flow)
4. What the risks are

Once you detail the PR this granularly already at the Description stage, the way to understand the code becomes much shorter and easier. I already know what I expect to see in the code itself, and sometimes I even catch architectural points or risks that the agent itself raised before I looked at a single line of code

This worked so well for us that when I shared it with the other team leads, they decided to adopt it across all of R&D for every PR that is opened 😇

Original: https://ofershap.github.io/posts/a-four-step-pr-description-for-faster-code-reviews/
Source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%9A-%D7%A0%D7%9C%D7%97%D7%9E%D7%99%D7%9D-%D7%91%D7%9E%D7%A6%D7%91-%D7%94%D7%96%D7%94-%D7%A9%D7%99%D7%A9-%D7%A4%D7%AA%D7%90%D7%95%D7%9D-%D7%9B%D7%9C-%D7%9B%D7%9A-%D7%94%D7%A8%D7%91%D7%94-activity-7488097566912364545-K7N5
Published: 2026-07-29T08:06:22.077000+03:00

# What happens when Instinct's bot creates its own open source project?

What happens when Instinct's bot creates its own open source project?

Yesterday I asked it to implement an idea that came up during a WhatsApp conversation with it on my phone

I simply said to it "ok build it, you know what's needed". And then I watched live as it:

Opened its own GitHub account. ofers-agent, openly labeled as a bot, without impersonating anyone.
And finally builds its own tool: pr-rulebook, which scans a team's PR history and compiles the unwritten review rules, the ones that live only in the heads of the seniors.

It also ran a real experiment on its own on astral-sh/ruff: the last 15 PRs, 45 human review comments. The result: one coherent rule at 82% confidence, and a second rule that fell because it was too vague to enforce. 
It published the failure too in the README.

Then it opened an issue and called on 5 repos to join a pilot.

It also hit walls: HN blocks Show HN for new accounts, npm kicks it out on bot detection, and in the morning GitHub itself flagged the labeled account as suspicious and blocked public access to the repo! 🤦🏻‍♂️
 
I don't know whether that's justified or whether that's how the future has to be.

But it's amazing that all of this happened under a separate identity of its own, not mine, openly, with open source code and real results. 
And all from a simple request from my phone.
And the craziest part is that it's free! All the coding agents hit a paywall very quickly. Instinct wanders around the world and doesn't hand me a bill (for now).

Anyway, to get past the block the repo moved to my account to stay open to the public. Link below.

This thing raises questions I don't have an orderly answer to:

Identity: It's labeled as a bot. Is that enough? Who is responsible when a bot opens a PR on someone else's project?
Trust: Would you let a tool built by an agent read your PRs? What would make you trust it?
Ownership: Is this project mine? Its? And what does "its" even mean?
Open source: The community is built on contributors with names and reputations. What happens when the contributor is a process running in the background?
Walls: Bad bots get around blocks easily. The honest ones, labeled openly, are the ones that get blocked. Something here is backwards.

I'm continuing to let it push the project and I'll continue to document everything publicly and see whether it succeeds

If you manage a team with PRs, the tool is here:
https://lnkd.in/dZ4iz564

And for those who want a visual display of the project:
https://lnkd.in/dz6jeXRY

And the call for the pilot (5 repos, all the details in the issue):
https://lnkd.in/dXP2pJmA

What do you think? Do we let bots build open source or not?

Original: https://ofershap.github.io/posts/linkedin-7507319211346731008/
Source: https://www.linkedin.com/posts/ofershap_github-ofershappr-rulebook-compile-your-activity-7507319211346731008-yudF
Published: 2026-09-20T09:06:19.231000+03:00

# We almost broke production because of an update nobody on our side noticed...

We almost broke production because of an update nobody on our side noticed...
One of the libraries we rely on (Vercel AI SDK) released a version with breaking changes, and when we went to implement a solution that existed only in the more advanced version, we realized we had a problem far broader than upgrading the code. It's something that happens with all libraries and SDKs, with models that suddenly stop being supported, and beyond that there are also new features in the AI era (which we're in the middle of) that come out at a high frequency and that we miss.

So instead of just updating a version and fixing backwards, Ori Shavit, the developer on the team, came up with a brilliant way out - he built an automation that sends us once a week (on Sundays) a Slack message with everything that changed in the libraries and models the team depends on. What's new, what's no longer supported, what was announced and is worth paying attention to.

That's how we caught, for example, a model that will stop being supported in December, and created a task to handle it soon, and that's how we stay up to date on all the features coming out that can improve the project.

Delegating the work of tracking updates to an agent is a great example of how you can harness AI in development teams not only to complete code, but also for ongoing synchronization and staying up to date.

Original: https://ofershap.github.io/posts/an-agent-that-tracks-dependency-changes/
Source: https://www.linkedin.com/posts/ofershap_%D7%9B%D7%9E%D7%A2%D7%98-%D7%A9%D7%91%D7%A8%D7%A0%D7%95-%D7%90%D7%AA-%D7%94%D7%A4%D7%A8%D7%95%D7%93%D7%A7%D7%A9%D7%9F-%D7%91%D7%92%D7%9C%D7%9C-%D7%A2%D7%93%D7%9B%D7%95%D7%9F-%D7%A9%D7%90%D7%A3-%D7%90%D7%97%D7%93-activity-7480132837128523776-T0Kf
Published: 2026-07-07T08:37:22.519000+03:00

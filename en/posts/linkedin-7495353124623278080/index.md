# How do you make sure your .env file is always up to date and that the whole team is in sync on it?

How do you make sure your .env file is always up to date and that the whole team is in sync on it?
Our solution was to redefine "what is an env file", and it's not a file that someone holds and updates manually, but a build artifact that is generated on its own every time you run the application.

For a long time our solution for managing the env was bad and manual: a Slack message. 
(If you relate, raise your hand...)
If someone adds a new environment variable, pushes the code, and three days later someone else pulls, runs, and gets a crash over a variable they've never heard of. And then comes the usual message or wandering through Slack messages. Even if you pass it through some secret manager like bitwarden, valuable time is still wasted on being out of sync...

In our product, which already has dozens of services (front and back), the problem gets much bigger because every project has its own env.

So our solution was to shift to the cloud - every service today has one secret in Google's Secret Manager that holds all the local development variables as a JSON object. It's enough to update a value in one place - and the whole team gets it, with history (and along the way also the ability to easily roll back).

And from the developer side (DevEx) syncing stopped being a command someone has to remember and became an automatic action: we wrote a small executor for Nx and defined it as a dependency of every dev target we have, so that even before the application comes up, Nx has already pulled the latest secrets and written a fresh env. 

And what do you do if you want to override locally?
We solved that elegantly too - everything you put in env.local is merged on top of what came from the cloud. The shared values stay shared, your machine stays yours.

There's a small price to pay - every so often we need to refresh our connection to GCP (the refresh happens automatically but you still need to approve the connection through the browser) and secret updates require working with Google's awful secrets interface (for which I also stitched together a solution in the form of a browser extension that tidies it up), but since we did this, "it works on my machine" stopped being a problem of environment variables.

If you're still struggling to sync env files in a team I highly recommend adopting this way of working, it saves a lot of headache and valuable developer time, and focuses on the things that really matter

Original: https://ofershap.github.io/posts/linkedin-7495353124623278080/
Source: https://www.linkedin.com/posts/ofershap_%D7%90%D7%99%D7%9A-%D7%90%D7%AA%D7%9D-%D7%93%D7%95%D7%90%D7%92%D7%99%D7%9D-%D7%A9%D7%94%D7%A7%D7%95%D7%91%D7%A5-env-%D7%A9%D7%9C%D7%9B%D7%9D-%D7%99%D7%94%D7%99%D7%94-%D7%AA%D7%9E%D7%99%D7%93-activity-7495353124623278080-oV7i
Published: 2026-08-18T08:37:21.837000+03:00

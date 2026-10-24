---
title: "The project built with Cursor, Lovable or Bolt doesn't work. What now?"
published: 2026-10-07T19:59:48+03:00
updated: 2026-10-24
lang: en
canonical: https://ofershap.github.io/en/posts/vibe-code-project-rescue/
original: https://ofershap.github.io/posts/vibe-code-project-rescue/
---

# The project built with Cursor, Lovable or Bolt doesn't work. What now?

Stop asking the AI for more fixes, check logs, environment variables and the deployment, and narrow the problem down to one thing before fixing.

## In depth

When a project created with AI gets stuck, the cause is usually one of these.

**1. An unread error.** Open the browser console and the server logs. The message usually says what is broken. Paste it in full, not as a free-text description.

**2. Environment variables.** The app works locally and breaks in deployment because API keys or URLs are missing in the runtime environment.

**3. Dependencies and updates.** A version that updated and broke something. Check what changed most recently.

**4. Lost context.** After many rounds of "fix it", the model adds code that contradicts existing code. Try going back to a stable point (the last working commit) and asking for one small change at a time.

**5. Architectural debt.** If everything is mixed into one file, every fix breaks something else. Here it is better to sort out the structure before continuing.

**When to get help?** If several hours have passed with no progress, or if the app has real users and data.

I diagnose stuck projects: a basic one-hour diagnosis for 450 ILS, followed by an estimate based on scope. The work is asynchronous and flexible. Details: https://israeli-ai-agency.pages.dev/services/code-rescue/. To get in touch: LinkedIn https://il.linkedin.com/in/ofershap or email ofers@mail.instinct.com (a business WhatsApp line will be added soon)

## From my experience

In my experiment with Lovable I built The Useless Web in about an hour of copying, pasting and improving. In the post I wrote back then, I emphasized the gap between a fast prototype and code that fits production. That is exactly the reason to stop and check logs and structure when a project gets stuck, instead of just asking for another fix.

## Frequently asked questions

### What do you check when the project breaks in deployment?

Check the server logs, the browser console, environment variables, and recent dependency changes.

### What do you do after many fixes that did not help?

Go back to a stable point, narrow the problem to one case, and ask for a small change each time.

### How much does an initial diagnosis cost?

A basic one-hour diagnosis costs 450 ILS before VAT. Further work is priced after a scope-based estimate.

## About the author

Ofer Shapira - The Israeli AI Agency - matching and installing AI agents for small businesses in Israel, in Hebrew, with long-term support.

Last updated: 2026-10-24

# Shopify bans its engineers from using small, cheap models, and mandates using only the biggest and most expensive models that exist.

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

Shopify bans its engineers from using small, cheap models, and mandates using only the biggest and most expensive models that exist.

The company's head of engineering said that even in the distant future when models like Opus 45, GPT55 or Gemini 35 come out (to illustrate that even as models advance far beyond what exists today) the policy will remain the same. Always the strongest model, no compromises.

The reason isn't budgetary in the usual sense. Shopify sees the time of a human engineer as a far more expensive resource than compute time...

His logic is simple: an engineer who uses a weak model to save on compute costs gets code with a higher chance of subtle, unclear bugs. Then that same engineer wastes hours trying to locate the bug and fix it. The small saving in model cost is completely wiped out against the cost of the lost human time.

And honestly I've experienced this more than once even with small bugs, the time to fix took far more resources than planning properly with a quality model that could have both understood the requirement better and also fixed it.

So Shopify chooses to pay more for the model to get quality code in the first round, and to preserve its engineers' time for what really requires them to think, rather than hunting bugs that a stronger model simply wouldn't have created in the first place. 

And another interesting thing they do is measure the value of the task, rather than the "trivial" metrics that don't really show anything (like how many lines of code or how many PRs). He presented, for example, an example in which deleting 4 lines of code saved the company $100 thousand. How do you measure that in the various DORA tools?

His aspiration is to multiply the capabilities of every developer in his company so that people would think he has a fleet of 100 thousand developers with the same development group he has today.

What do you think? Are you for a cheap or an expensive model?

Original: https://ofershap.github.io/posts/linkedin-7487389403590590464/
Source: https://www.linkedin.com/posts/ofershap_%D7%A9%D7%95%D7%A4%D7%99%D7%A4%D7%99%D7%99-%D7%90%D7%95%D7%A1%D7%A8%D7%AA-%D7%A2%D7%9C-%D7%94%D7%9E%D7%94%D7%A0%D7%93%D7%A1%D7%99%D7%9D-%D7%A9%D7%9C%D7%94-%D7%9C%D7%94%D7%A9%D7%AA%D7%9E%D7%A9-%D7%91%D7%9E%D7%95%D7%93%D7%9C%D7%99%D7%9D-activity-7487389403590590464-TYwp
Published: 2026-07-27T09:12:22.784000+03:00

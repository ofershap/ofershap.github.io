# Here's a TL;DR in Hebrew: the Lovable team published a technical blog post about how they moved their whole platform to run using... Lovable! They rebuilt the entire project so that it works on their own infrastructure.

Here's a TL;DR in Hebrew: the Lovable team published a technical blog post about how they moved their whole platform to run using... Lovable! They rebuilt the entire project so that it works on their own infrastructure. 

The post is long and in English, but here is its TL;DR:

The company Lovable moved their main site from Next.js to TanStack Start and now hosts it exactly like any site created with them.

The main reason: Dogfooding - using the infrastructure they sell themselves and discovering the problems before the users.
* The migration took about half a year. During that time the code grew from 350 thousand to more than 850 thousand lines.
* Instead of a hard cutover, they ran Next.js and TanStack in parallel and moved groups of routes gradually.
* They made about 97% of the code shared and framework-independent. A small adapters layer fit it to each framework.
* One developer carried out almost the entire migration with the help of a group of AI agents that wrote PRs, checked compatibility and identified new code that couldn't be migrated.
* Each group of routes went through a gradual rollout: internal, 1% of users, and then up to 100%.
* There was a serious incident in which the error rate jumped to about 50% because of exceeding the memory limit of Cloudflare Workers. 
The lesson: measure memory and performance from the start and don't ignore even 0.1% errors.
* Using TanStack Start gave them a significantly faster and lighter local development environment:
about 10 seconds and 1.5GB RAM.
Versus about 70 seconds and 8GB on Next.js.

They claim AI agents succeed more with TanStack, because the knowledge about it is small but consistent. Next.js has many versions and conflicting approaches.

The downside: in a large app TanStack requires many custom bundling settings. They have 17 custom plugins.

The result:
* Median TTFB improved by 49%.
* The production build dropped from 12+ minutes to 6-9 minutes.

The biggest advantage: now non-technical employees can edit lovable.dev using Lovable itself.
(Instead of developers dealing with every feature and every small change or A/B test or design changes).

The key point: gradual migration, shared code, controlled rollout and AI agents allowed one developer to carry out a huge migration that in the past would probably have required several teams.

So if I build in Lovable a system for building websites, then I'm building using a website-building system that sits on a website-building system, a website-building system... and if you build on the system I'm building then... well, you get it


The original article: https://lnkd.in/dtfsqhKx

Original: https://ofershap.github.io/posts/linkedin-7500903183968477184/
Source: https://www.linkedin.com/posts/ofershap_how-we-migrated-lovabledev-away-from-nextjs-activity-7500903183968477184-nJJP
Published: 2026-09-02T16:11:19.100000+03:00

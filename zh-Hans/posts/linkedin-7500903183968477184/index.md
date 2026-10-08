# 这是一份希伯来语的 TL;DR:Lovable 团队发布了一篇技术博客文章,讲述他们如何把整个平台迁移到使用……Lovable 本身来运行!他们重建了整个项目,使其运行在自己的基础设施上。

这是一份希伯来语的 TL;DR:Lovable 团队发布了一篇技术博客文章,讲述他们如何把整个平台迁移到使用……Lovable 本身来运行!他们重建了整个项目,使其运行在自己的基础设施上。 

这篇文章很长而且是英文的,但以下是其摘要:

Lovable 公司把他们的主站从 Next.js 迁移到了 TanStack Start,现在的托管方式与任何用他们的产品创建的网站完全一样。

主要原因:Dogfooding -- 自己使用他们售卖的基础设施,在用户之前发现问题。
* 迁移花了大约半年。在此期间代码从 35 万行增长到超过 85 万行。
* 他们没有一刀切,而是让 Next.js 和 TanStack 并行运行,逐步迁移一组组 route。
* 他们让约 97% 的代码成为共享的、与 framework 无关的代码。一个小型 adapters 层使其适配每个 framework。
* 一位开发者借助一组 AI agents 几乎完成了整个迁移,这些 agents 编写 PR、检查兼容性并识别出无法迁移的新代码。
* 每一组 route 都经历了渐进式 rollout:先内部,再 1% 的用户,然后逐步到 100%。
* 发生过一次严重事故,由于超出 Cloudflare Workers 的内存限制,错误率跃升到约 50%。 
教训:从一开始就衡量内存和性能,哪怕只有 0.1% 的错误也不要忽视。
* 使用 TanStack Start 让他们的本地开发环境显著更快、更轻:
约 10 秒和 1.5GB RAM。
而 Next.js 上约为 70 秒和 8GB。

他们声称 AI agents 在 TanStack 上更成功,因为关于它的知识量虽小但一致。Next.js 则有许多版本和相互矛盾的做法。

缺点:在大型应用中 TanStack 需要大量自定义的 bundling 配置。他们有 17 个自定义 plugin。

结果:
* TTFB 中位数改善了 49%。
* 生产环境 build 从 12 分钟以上降到 6–9 分钟。

最大的好处:现在非技术人员可以用 Lovable 本身来编辑 lovable.dev。
(而不是由开发者处理每一个功能、每一个小改动、A/B 测试或设计变更)。

核心要点:渐进式迁移、共享代码、受控的 rollout 以及 AI agents,让一位开发者完成了一次过去可能需要多个团队的庞大 migration。

所以,如果我在 Lovable 里构建一个用于构建网站的系统,那我就是在用一个构建网站的系统来构建,而它坐落在一个构建网站的系统之上,一个构建网站的系统……如果你们在我构建的系统上构建,那么……好吧,你们懂的


原文:https://lnkd.in/dtfsqhKx

Original: https://ofershap.github.io/posts/linkedin-7500903183968477184/
Source: https://www.linkedin.com/posts/ofershap_how-we-migrated-lovabledev-away-from-nextjs-activity-7500903183968477184-nJJP
Published: 2026-09-02T16:11:19.100000+03:00

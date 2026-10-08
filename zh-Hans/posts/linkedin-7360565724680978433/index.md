# Cursor 进阶指南 - context window is the new game we play

Cursor 进阶指南 - context window is the new game we play

为了让它正常工作,我给自己创建了一套规则(cursor rules),在每次对话开始时自动加载。我用武术(martial arts)的语气来写,一方面让它们简短、节省 token(因为它们会加入每一次对话 -- always apply 模式),另一方面也明确这些是基本前提,而不是请求。

这些规则除其他外告诉它:
- 不要自动同意我
- 每次回应前先检查代码
- 不要修改不必修改的代码
还有一些其他的(根据项目需要)

不过,我注意到,当工作对话变长、context window 被填满时,规则会被遗忘。它就是不再按规则行事,即使规则写在对话开头。让它们重新回到画面中的唯一办法是提醒它:"read the rules"。

看到规则的效果令人惊叹 -- 它突然不再做假设、不再幻觉,减少了错误,并开始按照现有模式行事。尤其是当我要求它在回应之前先学习代码或上下文时。

为了让工作更精准,我还在我的 Cursor rules 中写了说明,说明什么*不*该做:
- 除非我要求,否则不要在代码中添加注释(符合团队的 coding standard)
- 不要运行 npm run - 因为我们使用 hot reload
- 不要主动写文档(很可能有一个 system prompt 在推动它这样做)

我也根据过去失败的尝试,给了它如何*正确*做事的指令:在那些尝试中,经过几轮迭代,我们一起摸索出了该怎么做,然后我把它固化为文件中的一句话:
- 如何调用 GitHub 并提取 PR 的评论
- 在某个工具没有 MCP 时如何使用 CURL
- 我们在项目中如何编写测试

可以通过 3 个层次来看待新的编程世界(基于 LLM 的那个):
- 模型层(你使用哪个模型)
- 智能体层(你使用哪个开发工具)
- 规则层(你为个人需求做了哪些调整)

第三层让 Cursor 从一个主要靠有根据的猜测来工作的"学徒"开发者(因为它没有足够的上下文),变成了一个更专注的开发者


欢迎分享你们自己在 Cursor 上哪些有效、哪些无效的技巧 🤓

Original: https://ofershap.github.io/posts/managing-cursor-through-rules-and-context-windows/
Source: https://www.linkedin.com/posts/ofershap_%D7%9E%D7%93%D7%A8%D7%99%D7%9A-cursor-%D7%9C%D7%9E%D7%AA%D7%A7%D7%93%D7%9E%D7%99%D7%9D-context-window-is-activity-7360565724680978433-4Ew5
Published: 2025-08-11T10:00:21.462000+03:00

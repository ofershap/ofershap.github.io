# 所有人都在谈论 background agents,而我构建了一个 foreground agent。

本页为原文的机器翻译，未经人工译者审核。历史信息可能已发生变化。

所有人都在谈论 background agents,而我构建了一个 foreground agent。
Cursor、ChatGPT 等都提供运行"代码智能体"的选项,它在幕后自主运行。这有几个问题 - 一是看不到实际在执行什么,二是需要 Privacy 授权,三是有额外的成本。

由于我已经在日常使用 Cursor,并且需要运行一个复杂任务,我找到了一个能让我省去坐在那里批准 Cursor 流程中每一步的办法 -
而且一点也不复杂。

我通过 Help 菜单打开了 Cursor 的 Developer Tools,请 ChatGPT 写了一个小的 JS 脚本,并把它粘贴到控制台。 

脚本:每当出现要求我批准某些事情的消息 - "accept"、"run"、"25 tools limit" - 它就替我点击。

方法:我复制了代表按钮区域的 HTML,并在 prompt 中要求写一个脚本,每 15 秒检测一次它是否出现,如果出现就点击。我还喜欢解释它的用途 - "这样我就能把它粘贴到 Cursor 的 Devtools 里"。给 AI 提供上下文总是有帮助的。 

结果:我获得了工作的连续性,几乎和 Background agent 一样,但在我的掌控之下。

所以,与其使用"在后台"的 Agent,我构建了一个就在我面前的 -- 替我点击,让我真正进入心流。

重新设计界面本身的边界很有趣,而看到它运转顺畅更是令人惊叹 - 几分钟后我回到电脑前,发现我的任务已成功且完整地完成。

最后一点小而重要的说明:这对小项目和 vibe-coding 风格的开发(无需关注代码产出的质量)很棒,但对现有项目的修改可能是毁灭性的。 
此外,它可能很快失控并浪费 token。
所以如果你们模仿这种方法 - 请明智而谨慎地使用,即使它自己在跑,也要关注它所做的一切。

Original: https://ofershap.github.io/posts/linkedin-7355484666633641984/
Source: https://www.linkedin.com/posts/ofershap_%D7%9B%D7%95%D7%9C%D7%9D-%D7%9E%D7%93%D7%91%D7%A8%D7%99%D7%9D-%D7%A2%D7%9C-background-agents-%D7%90%D7%A0%D7%99-%D7%91%D7%A0%D7%99%D7%AA%D7%99-activity-7355484666633641984-KicT
Published: 2025-07-28T09:30:02.822000+03:00

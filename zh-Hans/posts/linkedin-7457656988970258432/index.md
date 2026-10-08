# 一个值得了解的酷概念 -- 谷歌开源了他们在 Stitch(他们的设计工具)中的工作方式。他们的想法是:将 UI 层与逻辑层分离,使智能体能够更轻松、更少出错地使用它。

一个值得了解的酷概念 -- 谷歌开源了他们在 Stitch(他们的设计工具)中的工作方式。他们的想法是:将 UI 层与逻辑层分离,使智能体能够更轻松、更少出错地使用它。 

他们是怎么做到的? 
记得 Microsoft .NET 时代的人都知道,当时也有类似的想法,用一个代表 ui 的 xml 文件来分离各层,而在 Android 上至今仍是这样工作的,所以现在针对智能体,他们使用 Markdown 来表示视觉元素(md 文件),本质上是构建一个基于描述它的文本的 UI 层。

当视觉界面层准备好(描述、展示它的"storybook")之后,智能体剩下要做的就是把各部分连接成一套逻辑,把元素放在屏幕上正确的位置,并为它们连接 business logic。

做 Web 系统的人都知道,挑战之一是让界面看起来和运行起来都好、而不是粗糙(sloppy),而 AI 在这方面很吃力,更不用说调试(debug)它了,所以他们提出并为我们发布的解决方案,可以成为通过 AI 更轻松地、更少故障和幻觉地构建高质量界面的跳板

如果你有兴趣深入了解并查看这个 repo,链接如下:

Original: https://ofershap.github.io/posts/how-google-stitch-describes-ui-for-ai-agents/
Source: https://www.linkedin.com/posts/ofershap_stitchs-designmd-format-is-now-open-source-activity-7457656988970258432-X-jV
Published: 2026-05-06T08:06:22.737000+03:00

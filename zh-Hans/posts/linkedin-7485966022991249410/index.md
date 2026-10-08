# 一群 AI 智能体仅通过阅读文档,就从零构建了整个 SQLite!

一群 AI 智能体仅通过阅读文档,就从零构建了整个 SQLite! 
他们并行运行 Cursor,用 Rust 开发,而且仅仅是通过阅读文档(835 页)做到的。没有源代码,没有现成的测试,也没有互联网访问!

更疯狂的是,这个集群达到了每秒一千次 commit 的速度! 
(Cursor 之前构建浏览器的那个集群,达到的是每小时一千次 commit)。 

由于 Git 根本不是为这样的速度而设计的,Cursor 构建了自己的版本控制系统,只是为了让智能体能够继续工作而不相互冲突。

结果以 100% 的得分通过了所有留作验证的 SQL 测试。

在我看来,这件事最重要的意义在于:当可以用一群智能体以这样的速度端到端地产出一个项目时,所有按人类节奏构建的工具 -- 评审(review)、合并(merge)、站会(standup)-- 都开始在重压下崩溃。 

Cursor 在这里证明了,只要有足够好的规格说明(以及相应的预算),就可以构建完整经历整个 SDLC、无需人工干预的整个项目。

来源:https://lnkd.in/eQvsRXwT

Original: https://ofershap.github.io/posts/cursors-sqlite-swarm-breaks-human-speed-workflows/
Source: https://www.linkedin.com/posts/ofershap_%D7%A0%D7%97%D7%99%D7%9C-%D7%A9%D7%9C-%D7%A1%D7%95%D7%9B%D7%A0%D7%99-ai-%D7%91%D7%A0%D7%95-%D7%90%D7%AA-%D7%9B%D7%9C-sqlite-%D7%9E%D7%90%D7%A4%D7%A1-%D7%A8%D7%A7-activity-7485966022991249410-bL6g
Published: 2026-07-23T10:56:22.404000+03:00

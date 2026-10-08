# 我整天都在使用 Cursor 的智能体模式(agent mode)。有一次我意识到自己总是在查看终端,看智能体是还在工作还是已经完成了。于是我做了这个:一个像素风办公室,位于底部面板中,并对智能体正在做的事情做出反应。

我整天都在使用 Cursor 的智能体模式(agent mode)。有一次我意识到自己总是在查看终端,看智能体是还在工作还是已经完成了。于是我做了这个:一个像素风办公室,位于底部面板中,并对智能体正在做的事情做出反应。

当智能体写代码时,角色会在办公桌前打字。空闲时会四处走动、逗猫。构建通过时会庆祝。每个物件都可以点击 -- 台灯、窗户、街机、书架、饮水机。

它的工作原理是监视 Cursor 的 JSONL 对话记录文件。只读,不需要 API 密钥,也不对 Cursor 打补丁。

整个东西只有 27KB。 

每个 sprite 都是用 TypeScript 逐像素绘制的,完全没有图片文件。 
我想看看在零资源(assets)的情况下,基于 canvas 的像素艺术能做到什么程度。

很想听听大家希望自己的办公室里有什么物件或功能。 
有一个插件 API,如果有人想添加自己的家具或新背景的话。

它可作为 Cursor 扩展使用: 
https://lnkd.in/dCpfVge8 

也可作为开源项目使用:
https://lnkd.in/d6a-Uu4u

Original: https://ofershap.github.io/posts/a-27kb-pixel-art-office-for-cursors-agent-mode/
Source: https://www.linkedin.com/posts/ofershap_i-use-cursors-agent-mode-all-day-at-some-activity-7439312614574174208-OIqS
Published: 2026-03-16T16:12:23.059000+02:00

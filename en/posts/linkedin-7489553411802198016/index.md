# Unbelievable! A guy named Matt Shumer posted a video of a shooter game that looks like Call of Duty, built entirely with one prompt with Claude Opus 5, with no external assets.

Unbelievable! A guy named Matt Shumer posted a video of a shooter game that looks like Call of Duty, built entirely with one prompt with Claude Opus 5, with no external assets.

The video got close to four million views(!) and many people were sure it was fake. Nobody ships a game like that from one prompt. So Shumer did the most obvious thing and published the whole prompt and all of his code. 

His prompt is really interesting because it's the opposite of what we all learned to do: instead of defining exactly what good means and detailing criteria, he wrote in the most general way possible: "Build a Call of Duty-level shooter, make it utterly perfect, every detail AAA quality, from the textures to the physics."

The quality doesn't come from that sentence (act surprised). It comes *from the structure* he gives his agents that carry out the task: 

- The lead agent breaks the game into small parts - the gun, the hands, the lighting, the movement, the enemy behavior - and for each part assigns a separate builder agent and reviewer agent. 
- The reviewer agent gets a clean context, without all of the builder's explanations of why it did what it did, and compares the result against real Call of Duty gameplay footage in a blind test. It approves only if what came out is really better.

Shumer called this a Gauntlet Loop. The difference from regular Reflection, where you simply ask the model to check and improve itself, is the separation. 

A builder agent tends to be forgiving toward its own work, because it remembers why it made each decision and it's easy for it to justify a mediocre result. A fresh agent with a clean context and an external bar simply doesn't hold that assumption.

Since he published the prompt, within a day people built space games, kart racing and more shooters of crazy quality with it. Shumer says he uses this on almost every project he works on, not only for games. 

Want to read and see more? Here:

His tweet: https://lnkd.in/dEdgEjFN 

His article: https://lnkd.in/dMikfdfe

Original: https://ofershap.github.io/posts/how-the-gauntlet-loop-built-a-game-from-one-prompt/
Source: https://www.linkedin.com/posts/ofershap_%D7%9C%D7%90-%D7%A0%D7%AA%D7%A4%D7%A1-%D7%91%D7%97%D7%95%D7%A8-%D7%91%D7%A9%D7%9D-%D7%9E%D7%90%D7%98-%D7%A9%D7%95%D7%9E%D7%A8-%D7%A4%D7%A8%D7%A1%D7%9D-%D7%95%D7%99%D7%93%D7%90%D7%95-%D7%A9%D7%9C-activity-7489553411802198016-kmG2
Published: 2026-08-02T08:31:22.547000+03:00

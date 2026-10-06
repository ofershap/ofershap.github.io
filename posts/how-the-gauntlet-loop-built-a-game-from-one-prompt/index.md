# How the Gauntlet Loop built a game from one prompt

August 2, 2026 · 1 min read

Originally posted on LinkedIn , August 2, 2026.

Matt Shumer published a video of a shooter that looked like Call of Duty, built entirely from one prompt with Claude Opus 5 and no external assets. The video received close to four million views, and many people assumed it was fake. Nobody produces a game like that from one prompt, so Shumer published the full prompt and all of his code.

The prompt is interesting because it does the opposite of what we have all learned to do. Instead of defining success precisely and listing detailed criteria, he kept it extremely broad: “Build a Call of Duty-level shooter that is utterly perfect, with every detail at AAA quality, from the textures to the physics.”

The quality does not come from that sentence. It comes from the structure he gives the agents doing the work:

- The lead agent breaks the game into small parts: the gun, hands, lighting, movement, enemy behavior, and more. It assigns a separate builder agent and critic agent to each part.

- The critic receives clean context, without the builder's explanations for its decisions. It compares the result against screenshots of real Call of Duty gameplay in a blind test and approves it only if the output is genuinely better.

Shumer calls this the Gauntlet Loop. The difference between this and standard Reflection, where you simply ask the model to review and improve its own work, is the separation.

An agent reviewing its own work tends to be forgiving. It remembers why it made each decision, which makes a mediocre result easy to justify. A new agent with clean context and an external standard does not carry that assumption.

Within a day of Shumer publishing the prompt, people used it to build space games, kart racing games, and more shooters at an extraordinary level of quality. Shumer says he uses this approach in almost every project he works on, not only games. He shared the details in his tweet and his article .

Original source: https://www.linkedin.com/posts/ofershap_%D7%9C%D7%90-%D7%A0%D7%AA%D7%A4%D7%A1-%D7%91%D7%97%D7%95%D7%A8-%D7%91%D7%A9%D7%9D-%D7%9E%D7%90%D7%98-%D7%A9%D7%95%D7%9E%D7%A8-%D7%A4%D7%A8%D7%A1%D7%9D-%D7%95%D7%99%D7%93%D7%90%D7%95-%D7%A9%D7%9C-activity-7489553411802198016-kmG2

# How Google Stitch describes UI for AI agents

May 6, 2026 · 1 min read

Originally posted on LinkedIn , May 6, 2026.

Google open-sourced the way its design tool, Stitch, separates the UI layer from the logic layer. The goal is to represent the UI in a format that an agent can use easily and with fewer errors.

Microsoft .NET used a similar separation, with an XML file representing the UI, and Android still works this way. For agents, Stitch uses Markdown and md files to represent visual elements, creating a text-based description of the UI layer.

Once that visual layer is ready, including its descriptions and the “storybook” that displays it, the agent only needs to assemble the pieces into a single application. It places the elements in the right parts of the screen and connects them to the business logic.

One of the hardest parts of building web systems is making the interface look and behave well instead of feeling sloppy. AI struggles badly with this, and debugging the result is even harder. Stitch’s approach could make it much easier to build high-quality interfaces with AI while reducing errors and hallucinations.

Original source: https://www.linkedin.com/posts/ofershap_stitchs-designmd-format-is-now-open-source-activity-7457656988970258432-X-jV

# A cool concept worth knowing - Google open-sourced how they work in Stitch (their design tool). Their idea: to separate the UI layer from the logic layer in such a way that an agent can use it easily and with fewer failures.

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

A cool concept worth knowing - Google open-sourced how they work in Stitch (their design tool). Their idea: to separate the UI layer from the logic layer in such a way that an agent can use it easily and with fewer failures. 

How did they do it? 
Those who remember the Microsoft .NET era had a similar idea of separating the layers with an xml file that represents the ui, and on Android it still works that way, so now for agents they use Markdown to represent the visual elements (md files) and basically build a UI layer based on text that describes it.

When the visual interface layer is ready (the descriptions, the "storybook" that displays it) then all that's left for the agent is to connect the pieces into one logic, place the elements in the right places on the screen and connect business logic to them.

Anyone who deals with building web systems knows that one of the challenges is getting the interface to look and work well and not sloppy, and that AI struggles a lot with this, not to mention debugging it, so the solution they propose and release for us can serve as a springboard for quality interfaces that are built more easily and with fewer failures and hallucinations by means of AI

If you're interested in diving in and seeing the repo, here's the link:

Original: https://ofershap.github.io/posts/how-google-stitch-describes-ui-for-ai-agents/
Source: https://www.linkedin.com/posts/ofershap_stitchs-designmd-format-is-now-open-source-activity-7457656988970258432-X-jV
Published: 2026-05-06T08:06:22.737000+03:00

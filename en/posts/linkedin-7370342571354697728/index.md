# Start speaking LLM-ish! 🈯

Start speaking LLM-ish! 🈯 
Until now, prompt engineering tried to get by with a language that wasn't built for it. Microsoft has now released a new language structure that is economical, efficient and organized.

Until today there was no truly efficient way to write prompts for AI (for engineers who develop systems that work against the API)
Markdown was used to organize text, but without a real logical hierarchy. 
JSON tried to describe structure - but the format is loaded with unnecessary characters, and hard to read and write by hand. 

In both, it's hard to produce complex, dynamic, maintainable prompts. Every small change becomes a cumbersome task, and every duplication of a prompt creates duplicates and scattered logic.

As models get stronger, the demands on them get more precise - and the need for a new language, one that understands prompts not as text but as modular code, keeps growing.

Here Microsoft comes in, with a new language:
 POML – Prompt Orchestration Markup Language.

POML is an "open" markup language that brings order, hierarchy and scalability to prompt engineering. Instead of maintaining "loose" textual code, you can finally work with tags, templates, variables and styles.

We're going back in time a little to the XML era (remember it? before the JSON era)

How does it work in practice?

- You use elements like `<role>`, `<task>`, `<example>` to define logical parts of the prompt.
- You pull in external information with `<document>`, `<table>`, `<image>` without hard-coding it by hand.
- You separate formatting from logic with `<stylesheet>`, similar to CSS.
- You define variables, conditions and loops with an engine of `<let>`, `if`, `for` – to create dynamic templates.
- Of course there is already support in VS Code (with a dedicated extension that includes autocompletion, preview, and diagnostics).

The result: consistent management of prompts, reduced duplication, high flexibility for updates, and mainly - saving unnecessary tokens and quickly improving performance.

When the format itself gets smart and there is real optimization of the whole LLM value chain, the result is savings in resources and costs.

Worth trying!

How do you start? From here: https://lnkd.in/dQnXbH3t

Original: https://ofershap.github.io/posts/poml-treats-prompts-as-modular-code/
Source: https://www.linkedin.com/posts/ofershap_%D7%AA%D7%AA%D7%97%D7%99%D7%9C%D7%95-%D7%9C%D7%93%D7%91%D7%A8-llm%D7%99%D7%AA-%D7%A2%D7%93-%D7%A2%D7%9B%D7%A9%D7%99%D7%95-%D7%94%D7%A0%D7%93%D7%A1%D7%AA-%D7%A4%D7%A8%D7%95%D7%9E%D7%A4%D7%98%D7%99%D7%9D-activity-7370342571354697728-XUvc
Published: 2025-09-07T09:30:03.354000+03:00

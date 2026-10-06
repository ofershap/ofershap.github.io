# POML treats prompts as modular code

September 7, 2025 · 1 min read

Originally posted on LinkedIn , September 7, 2025.

Microsoft has released POML, Prompt Orchestration Markup Language, a more efficient and organized way to write prompts.

Until now, engineers building systems against an AI API had no truly effective format for prompts. Markdown organizes text, but it has no real logical hierarchy. JSON describes structure, but it is full of unnecessary characters and is hard to read and write by hand.

Both formats make complex, dynamic, maintainable prompts difficult to build. Every small change becomes cumbersome, and copying a prompt creates duplication and spreads logic across the codebase.

As models get stronger, our instructions need to become more precise. We need a language that treats prompts not as text, but as modular code.

POML is an “open” markup language that brings structure, hierarchy, and scale to prompt engineering. Instead of maintaining unstructured text, we can work with tags, templates, variables, and styles. In a way, we are going back to the XML era, before JSON.

In practice:

- Elements such as <role> , <task> , and <example> define logical parts of a prompt.

- <document> , <table> , and <image> pull in external information without encoding it manually.

- <stylesheet> separates presentation from logic, much like CSS.

- <let> , if , and for add variables, conditions, and loops for dynamic templates.

- A dedicated VS Code extension already provides autocomplete, previews, and diagnostics.

The result is consistent prompt management, less duplication, and more flexibility when making changes. More importantly, it cuts wasted tokens and makes performance easier to improve. When the format itself becomes smarter and the full LLM chain can be optimized, it saves resources and money.

Microsoft's POML documentation and project page explains how to get started.

Original source: https://www.linkedin.com/posts/ofershap_%D7%AA%D7%AA%D7%97%D7%99%D7%9C%D7%95-%D7%9C%D7%93%D7%91%D7%A8-llm%D7%99%D7%AA-%D7%A2%D7%93-%D7%A2%D7%9B%D7%A9%D7%99%D7%95-%D7%94%D7%A0%D7%93%D7%A1%D7%AA-%D7%A4%D7%A8%D7%95%D7%9E%D7%A4%D7%98%D7%99%D7%9D-activity-7370342571354697728-XUvc


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

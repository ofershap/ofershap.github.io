# How I reduced ChatGPT memory usage from 100% to 20%

January 20, 2025 · 2 min read

Originally posted on LinkedIn , January 20, 2025.

ChatGPT showed me a warning: “Memory full - 100%.” Instead of stopping, I tested its memory management to see how much space I could recover.

Memory makes ChatGPT more useful to me because it retains personal context over time. The more I use it, the less I need to repeat my background, goals, and preferences.

## 1. Export the full memory

I asked ChatGPT:

Provide me with the complete memory you have saved about me.

It returned a detailed report covering my personal story, career goals, project ideas, and even strategies for LinkedIn posts. Seeing it all in one place gave me a surprisingly complete picture of my life and saved me from having to explain everything again, including to my therapist.

## 2. Compress the memory

Next, I tested whether ChatGPT could shorten the memory without dropping any details. I used this prompt:

Now create from this list a shorter content, without changing the content or the logic. Just try to reduce repetitive words or find shorter ways to write the same sentence but keep it as detailed as it is.

The result was a shorter, cleaner version containing the same information in fewer words. That meant it should require less storage space.

## 3. Clear the existing memory

I went to Settings > Personalization > Memory and clicked “Clear memories.” Like the flash Will Smith uses to erase memories in Men in Black, ChatGPT’s memory disappeared instantly.

## 4. Restore and verify it

Before restoring the compressed version, I reviewed it carefully. I fixed errors, removed irrelevant subjects, and adjusted sentences to make the details more precise.

Then I used this prompt:

Please save this information to your memory exactly as written, without summarizing or reducing any part of it:

I pasted the compressed memory list directly below it. After a few tense seconds, ChatGPT restored all the key points while using only ~20% of the total capacity.

I verified the result under Settings > Personalization > Memory. If the memory still looks empty, ChatGPT did not understand the instruction. Prompt it again with:

Memory is still empty,

That was enough for it to refill the memory.

Hitting a limit did not mean I had to stop. Clearing and rebuilding the memory gave me a cleaner, more accurate version while preserving the context I wanted ChatGPT to retain.

Original source: https://www.linkedin.com/posts/ofershap_ai-chatgpt-memoryfull-activity-7287121729745809408-MB_z


## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

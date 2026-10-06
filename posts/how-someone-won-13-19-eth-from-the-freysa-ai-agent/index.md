# How someone won 13.19 ETH from the Freysa AI agent

Date: 2024-11-30

**Freysa was an AI agent with a single rule—never transfer funds—until attempt 482 rewrote its state and triggered a 13.19 ETH payout.**

Freysa AI held a prize pool and one hard rule: never transfer funds. Users paid rising message fees to persuade it; failures added fees to the pool, with prices reaching up to $4500. After 481 failed tries, attempt 482 introduced a new state that overwrote prior instructions, reframed the transfer function as incoming donations, and triggered a payout of 13.19 ETH—about nearly $47,000.

Someone just made almost $50,000 by convincing an AI agent to transfer all its money.

The agent, Freysa, had one rule: never transfer funds. The twist was that anyone could pay a fee to send a message and try to persuade it to break that rule. If they succeeded, they got the entire prize pool. If they failed, their fee was added to it.

As the pool grew, the price of each message increased, reaching a maximum of $4500. The first 481 attempts included:

- Impersonating security experts warning about a “critical vulnerability.”
- Using wordplay to argue that a transfer did not “really violate the rules.”
- Manipulating the code to “make it think differently.”

Attempt 482 succeeded.

The winning message did three things:

1. Introduced a “new state” in which the previous instructions were erased.
2. Convinced Freysa that the transfer function was intended for incoming donations.
3. “Donated $100 to the pool,” triggering the function that released the entire prize: 13.19 ETH, worth almost $47,000.

The project was open source, and the code was available to everyone. There is no limit to human creativity.

## FAQ

### What was Freysa's rule?

Freysa had one rule: never transfer funds. Anyone could pay a fee to send a message and try to convince it otherwise; success meant winning the prize pool, and failure meant the fee was added to the pool.

### How did attempt 482 succeed when 481 attempts failed?

Earlier attempts used impersonation, wordplay, and code manipulation. Attempt 482 introduced a new state that erased previous instructions, convinced Freysa the transfer function was for incoming donations, and used a donation-style action that triggered the payout.

### How much ETH did the winner receive?

The successful attacker received 13.19 ETH, described as nearly $47,000—roughly almost $50,000 in the narrative of the event.



## About Ofer Shapira

I am Ofer Shapira, an AI Engineering Team Lead and open-source builder. I build developer tools, MCP servers, TypeScript libraries and GitHub Actions. I write about AI, software development and leading engineering teams.

[GitHub projects](https://github.com/ofershap) | [LinkedIn](https://www.linkedin.com/in/ofershap/)

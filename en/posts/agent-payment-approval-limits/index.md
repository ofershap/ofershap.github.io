---
title: "How do you let an AI agent pay without losing control?"
published: 2026-10-20T13:30:00+03:00
updated: 2026-10-23
lang: en
canonical: https://ofershap.github.io/en/posts/agent-payment-approval-limits/
original: https://ofershap.github.io/posts/agent-payment-approval-limits/
---

# How do you let an AI agent pay without losing control?

The agent gets a dedicated payment rail with a cap, not an open card. Every unusual charge goes through human approval, and the log gets read once a week. The agent can order, compare prices, and close a purchase, but the amount it can get wrong is capped in advance.

## In depth

### Separate approval from execution

My first rule: the agent prepares the order, a human approves the payment. It sounds cumbersome, and in practice it's ten seconds of approval in chat. What you gain is that there's no scenario where one morning you discover a charge nobody asked for.

Example: the agent sends "Found the cable for 89 shekels including shipping, approve?". The answer "yes" is the approval. No "yes", no charge.

### A monetary cap, not a feeling of safety

A solution that works is a dedicated card or a separate allowance with a small monthly cap. If the agent gets it wrong, the maximum damage is the cap. On our team the same principle applies to paid dev tools: every new integration starts with a limited budget, and expands only after a month of clean usage.

A number worth keeping in mind: a monthly cap of 500 shekels costs less than one hour of a team member's work, and it turns the agent's most expensive mistake into something you can sign off calmly.

### A log that actually gets read

Every charge the agent makes goes into one list: what was bought, how much, when, and which request stood behind it. Once a week, five minutes of reading. Just like I found out my meeting recordings had stopped only after a whole week, small charges can pile up unnoticed. The weekly digest catches that.

### What not to do

Don't give the agent the business's main card. Don't rely on "it promised to ask". And don't connect a payment method without checking how to cancel: before the first connection, verify you can freeze the card or close the allowance in one click.

## From my experience

In my post about Hark I told about a company that handed out real pizzas worth a million dollars: you write to the agent in chat, and it orders from DoorDash on your card. My agent orders and pays for real things too. The question isn't whether to let it pay, but how to stay in control of every shekel.

## Frequently asked questions

### And how much time does it take a human to approve each time?

Ten seconds of approval in chat. That's the price of control, and it's cheap compared to a wrong charge you have to chase.

### Can you give the agent a budget with no approval at all?

Yes, within a low cap you're willing to lose. Above the cap, human approval comes back.

### What do you do if the agent already charged something wrong?

Freeze the payment method, contact the vendor for a refund, and update the rules so that case doesn't repeat. The log shows exactly which request led to the charge.

## About the author

Ofer Shapira builds and leads AI in engineering teams, and writes about agents, decisions, and workflows you can verify.

Last updated: 2026-10-23

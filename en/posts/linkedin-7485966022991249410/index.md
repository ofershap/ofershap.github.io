# A swarm of AI agents built all of SQLite from scratch just by reading the documentation!

Machine translation from the original post. Not reviewed by a human translator. Historical claims may no longer be current.

A swarm of AI agents built all of SQLite from scratch just by reading the documentation! 
They ran Cursor in parallel and developed in Rust and did it just by reading the documentation (835 pages). No source code, no existing tests and no internet access!

Even crazier is that the swarm reached a rate of a thousand commits per second! 
(Cursor's previous swarm, which built a browser, reached a thousand commits per hour). 

Since Git simply wasn't built for such a rate, Cursor built a version control system of their own just so the agents could keep working without colliding with each other.

The result passed all of the SQL tests that were held out for verification with a score of 100%.

The most significant thing in this event, in my eyes, is that when you can produce a project end to end at such a rate using a swarm of agents, then all the tools that were built at human pace, review, merge, standup, start to collapse under the weight. 

Cursor proved here that with a good enough spec (and a matching budget) you can build entire projects that go through the whole SDLC without a human hand.

Source: https://lnkd.in/eQvsRXwT

Original: https://ofershap.github.io/posts/cursors-sqlite-swarm-breaks-human-speed-workflows/
Source: https://www.linkedin.com/posts/ofershap_%D7%A0%D7%97%D7%99%D7%9C-%D7%A9%D7%9C-%D7%A1%D7%95%D7%9B%D7%A0%D7%99-ai-%D7%91%D7%A0%D7%95-%D7%90%D7%AA-%D7%9B%D7%9C-sqlite-%D7%9E%D7%90%D7%A4%D7%A1-%D7%A8%D7%A7-activity-7485966022991249410-bL6g
Published: 2026-07-23T10:56:22.404000+03:00

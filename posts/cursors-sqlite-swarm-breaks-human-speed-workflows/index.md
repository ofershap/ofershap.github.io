# Cursor’s SQLite swarm breaks human-speed workflows

July 23, 2026 · 1 min read

Originally posted on LinkedIn , July 23, 2026.

A swarm of AI agents rebuilt all of SQLite from scratch by reading its 835 pages of documentation. They ran Cursor in parallel, developed it in Rust, and did it without source code, existing tests, or internet access.

The swarm reached 1,000 commits per second. Cursor’s previous swarm, which built a browser, reached 1,000 commits per hour. Git was not built for this pace, so Cursor created its own version control system to let the agents keep working without colliding with each other.

The result scored 100% on every held-out SQL test.

The most significant part is what happens to software delivery at this speed. When a swarm of agents can produce an end-to-end project this quickly, every tool and process designed around human output, including review, merge, and standup, starts to collapse under the load.

Cursor showed that with a good enough specification, and the corresponding budget, agents can build complete projects that go through the entire SDLC without human intervention.

Source

Original source: https://www.linkedin.com/posts/ofershap_%D7%A0%D7%97%D7%99%D7%9C-%D7%A9%D7%9C-%D7%A1%D7%95%D7%9B%D7%A0%D7%99-ai-%D7%91%D7%A0%D7%95-%D7%90%D7%AA-%D7%9B%D7%9C-sqlite-%D7%9E%D7%90%D7%A4%D7%A1-%D7%A8%D7%A7-activity-7485966022991249410-bL6g

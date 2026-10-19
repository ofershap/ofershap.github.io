# AGENTS.md - working on this repository

Static blog of Ofer Shapira, served by GitHub Pages from this repo root. No framework; Python build scripts generate and patch the HTML.

## Build and test

- Build scripts are `build_*.py` (idempotent; run with `python3 build_<name>.py`).
- Tests are `test_*.py`; run all with `for t in test_*.py; do python3 "$t"; done`. All must pass before pushing.
- Pushing to `main` deploys the live site at https://ofershap.github.io/.

## Conventions

- Content is Hebrew-first with English companions; keep original-language source text byte-exact.
- Never fabricate capabilities: agent-facing files (`.well-known/`, `openapi.json`, llms.txt) describe only real, live endpoints. The test suites enforce this.
- The engagement API (`engagement-backend/`, Cloudflare worker) is the only dynamic backend; document it honestly, no auth theater.
- Recipe collection terminology: "ספרייה"/"ספריית המתכונים" in Hebrew, "Recipe library" in English.

# devops/github

Purpose

DevOps examples for GitHub-centric workflows: GitHub Actions CI, release automation, and infrastructure-as-code integration.

Prerequisites

- GitHub account
- Familiarity with Git and GitHub Actions

Run instructions

- See `.github/workflows/ci.yml` for CI examples.
- To run tests locally: `pip install -r requirements.txt` then `pytest`.

Notes

- Keep CI fast and focused; use matrix builds only when needed.
- Store secrets in GitHub Actions secrets or external vaults.

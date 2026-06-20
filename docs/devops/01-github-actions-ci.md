# A Practical GitHub Actions CI Workflow

Continuous integration (CI) provides fast feedback whenever repository content changes. For a tutorial repository, useful checks should be quick, deterministic, and directly related to reader experience.

## What this repository validates

The workflow in [`.github/workflows/ci.yml`](../../.github/workflows/ci.yml) runs for pushes and pull requests targeting `main`. It performs two checks:

1. Compile Python files to catch syntax errors without running demos that may download models or require credentials.
2. Validate relative links and local image references in Markdown files.

## Why demos are not all installed globally

Different tutorials need different SDKs and can eventually require incompatible versions. Each demo therefore owns its dependency file. CI can add a dedicated job for a demo once that demo has meaningful automated tests.

## Design principles

- A failed validation must fail the workflow; avoid hiding failures with `|| true`.
- Do not upload the entire repository as a test artifact.
- Pin action versions to stable major releases and review upgrades regularly.
- Keep credential-free checks in the default workflow.
- Put cloud integration tests in separate, explicitly authorized workflows.

## Running the same checks locally

From the repository root:

```powershell
python -m compileall -q demos scripts
python scripts/check_links.py
```

Local and CI commands should stay aligned so contributors can reproduce failures before pushing.

# Contributing

Contributions should make the repository easier to learn from, run, or maintain.

## Choose the right location

| Content | Location |
| --- | --- |
| Explanations and tutorials | `docs/<domain>/` |
| Runnable examples | `demos/<domain>/<demo-name>/` |
| Repository maintenance utilities | `scripts/` |
| Images and static media | `assets/<type>/<domain>/` |

Do not mix runnable code into a documentation folder. A tutorial can link to a companion demo.

## Tutorial conventions

- Use descriptive kebab-case filenames.
- Prefix sequential lessons with two digits: `01-topic.md`, `02-next-topic.md`.
- Begin with one `#` heading, then use heading levels in order.
- Explain prerequisites before steps that require accounts, tools, permissions, or spending.
- Include cleanup instructions when a tutorial creates billable resources.
- Link new content from the nearest section `README.md`.
- Prefer Mermaid for diagrams that do not require custom artwork.

## Demo conventions

Every demo must contain a README that explains its purpose, prerequisites, setup, run command, expected result, and related tutorial. Keep dependencies local to the demo instead of adding a repository-wide dependency file.

Never commit credentials, `.env` files, virtual environments, generated datasets, downloaded models, or cloud state files.

## Validate changes

From the repository root, run:

```powershell
python -m compileall -q demos scripts
python scripts/check_links.py
```

Run any demo-specific tests documented in that demo's README as well.

## Pull requests

1. Create a focused branch and keep the change small enough to review.
2. Explain what changed, why it changed, and how you validated it.
3. Update navigation and documentation with the implementation.
4. Address review feedback before merging into `main`.

Report vulnerabilities using [SECURITY.md](SECURITY.md), not a public issue.

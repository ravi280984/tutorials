# Practical AI, Cloud, and DevOps Tutorials

Learn modern platform engineering one concept at a time. This repository combines concise explanations with small, runnable examples for engineers working across AI, cloud architecture, and DevOps.

> The material is written for progressive learning: start with a concept, follow the related provider guide, and use a demo when you want to experiment locally.

## Start here

| Learning path | What you will learn | First topic |
| --- | --- | --- |
| [AI](docs/ai/README.md) | LLM foundations, embeddings, RAG, tools, and agents | [How modern AI systems fit together](docs/ai/01-modern-ai-systems.md) |
| [Cloud](docs/cloud/README.md) | Cloud fundamentals, governance, and landing zones | [Why cloud computing became popular](docs/cloud/01-cloud-computing.md) |
| [DevOps](docs/devops/README.md) | Automation and delivery practices used by this repository | [GitHub Actions CI](docs/devops/01-github-actions-ci.md) |

## Repository map

```text
.
|-- docs/                 # Tutorials and learning paths
|   |-- ai/
|   |-- cloud/
|   `-- devops/
|-- demos/                # Runnable, self-contained examples
|-- scripts/              # Repository validation and maintenance tools
|-- assets/               # Images and other static tutorial assets
`-- .github/workflows/    # Continuous integration
```

### Content boundaries

- Put explanations, diagrams, and learning material in `docs/`.
- Put runnable applications and experiments in `demos/`. Each demo owns its README and dependencies.
- Put repository maintenance utilities in `scripts/`.
- Put static files in `assets/` and keep them close to a clear domain path.

This separation prevents one global environment from becoming a dependency grab bag as the repository grows.

## Run a demo

Every demo is self-contained. For example, to run the semantic-search demo:

```powershell
cd demos/ai/semantic-search
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python semantic_search.py
```

Python 3.10 or newer is recommended. Cloud tutorials can additionally require the relevant provider account and CLI; prerequisites are documented in each guide.

## Add a topic

1. Choose the appropriate learning path under `docs/`.
2. Name ordered tutorials with a two-digit prefix, such as `03-networking-basics.md`.
3. Add the tutorial to that section's `README.md`.
4. Place runnable code in `demos/<domain>/<demo-name>/`, not beside the article.
5. Run `python scripts/check_links.py` before committing.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the complete content conventions and review checklist.

## Repository notes

- Examples favor clarity over production completeness.
- Cloud resources can incur charges; follow provider cleanup guidance after experiments.
- Never commit credentials, tokens, private keys, or real customer data.

Licensed under the [MIT License](LICENSE). Security concerns should follow [SECURITY.md](SECURITY.md).

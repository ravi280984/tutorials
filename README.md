# tutorials

Overview

This repository contains curated tutorials, examples, and starter templates for AI development, cloud integrations, and DevOps workflows. It is organized into subfolders to keep focused content and demos isolated and easy to follow.

Structure

- AI/
  - mcp/       - Model Context Protocol examples and local agent demos
  - rag/       - Retrieval-Augmented Generation examples and vector search demos
- cloud/
  - aws/       - AWS-focused tutorials and IaC examples
  - azure/     - Azure-focused tutorials and deployments
- devops/
  - github/    - CI/CD examples, GitHub Actions, and release workflows

Setup (local)

1. Install Python 3.10+ and Docker (optional).
2. Create and activate a virtual environment:
   - powershell: python -m venv .venv; .\.venv\Scripts\Activate.ps1
3. Install dependencies:
   - pip install -r requirements.txt
4. Optional: build with Docker:
   - docker build -t tutorials:latest .

Usage

- Read the folder-specific README files for step-by-step instructions for each tutorial.
- Use the `AI` folder to explore model/agent examples.
- Use the `cloud` folder for provider-specific deployment guides.
- Use the `devops` folder for CI/CD and infra automation samples.

Contributing

See `CONTRIBUTING.md` for contribution guidelines.

License

This project is licensed under the MIT License - see `LICENSE` for details.

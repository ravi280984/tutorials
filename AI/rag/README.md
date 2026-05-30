# AI/rag

Purpose

This folder demonstrates Retrieval-Augmented Generation (RAG) patterns: creating embeddings, vector indexes, and combining retrieval with LLMs for grounded generation.

Prerequisites

- Python 3.10+
- Install dependencies: `pip install -r requirements.txt`

Run instructions

- Example steps:
  1. Prepare documents in `data/` (not committed).
  2. Build embeddings: `python build_embeddings.py`.
  3. Run retrieval demo: `python rag_demo.py`.

Notes

- Use `faiss` or managed vector DBs for production scale.
- Store indexes and models in `models/` or external storage.

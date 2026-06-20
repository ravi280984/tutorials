# Semantic Search Demo

This small demo encodes three documents and a query with a sentence-transformer model, calculates cosine similarity, and prints the documents from most to least relevant.

It demonstrates the retrieval step used by many RAG systems; it is **not a complete RAG application** because it does not send retrieved context to a generative model.

## Prerequisites

- Python 3.10 or newer
- Internet access on the first run to download the model

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python semantic_search.py
```

The first result should discuss retrieval-augmented generation because it is closest in meaning to the sample query.

## Related tutorial

[How modern AI systems fit together](../../../docs/ai/01-modern-ai-systems.md)

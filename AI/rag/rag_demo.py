"""Minimal RAG demo script — builds a tiny in-memory index and queries it.

This file is a demo and intentionally small. Substitute real embeddings and vector stores for production.
"""

from sentence_transformers import SentenceTransformer
import numpy as np


SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "AI development requires data, compute, and iteration.",
    "Retrieval augmented generation combines search with generation.",
]


def build_embeddings():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(SENTENCES)


if __name__ == '__main__':
    print("Building embeddings...")
    embs = build_embeddings()
    print(embs.shape)

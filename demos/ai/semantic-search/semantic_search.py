"""Rank a small document collection by semantic similarity to a query."""

from sentence_transformers import SentenceTransformer


DOCUMENTS = [
    "The quick brown fox jumps over the lazy dog.",
    "AI development requires data, compute, and iteration.",
    "Retrieval-augmented generation combines search with text generation.",
]
QUERY = "How does an AI application retrieve useful context?"
MODEL_NAME = "all-MiniLM-L6-v2"


def rank_documents(query: str, documents: list[str]) -> list[tuple[float, str]]:
    """Return documents ordered by cosine similarity to the query."""
    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode([query, *documents], normalize_embeddings=True)
    query_vector, document_vectors = vectors[0], vectors[1:]
    scores = document_vectors @ query_vector
    return sorted(zip(scores.tolist(), documents), reverse=True)


def main() -> None:
    print(f"Query: {QUERY}\n")
    for position, (score, document) in enumerate(
        rank_documents(QUERY, DOCUMENTS), start=1
    ):
        print(f"{position}. {score:.3f} — {document}")


if __name__ == "__main__":
    main()

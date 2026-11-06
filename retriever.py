import chromadb
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).parent
KNOWLEDGE_FILE = BASE_DIR / "knowledge_base" / "rag_reference.md"

# Create a persistent vector database
client = chromadb.PersistentClient(
    path=str(BASE_DIR / "chroma_db")
)

collection = client.get_or_create_collection(
    name="rag_knowledge"
)


def load_knowledge():
    """Read trusted knowledge from the Markdown file."""

    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError(
            f"Knowledge base file not found: {KNOWLEDGE_FILE}"
        )

    return KNOWLEDGE_FILE.read_text(encoding="utf-8")


def split_into_chunks(text, chunk_size=700):
    """Divide knowledge into smaller pieces."""

    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def build_knowledge_base():
    """Store knowledge chunks in ChromaDB."""

    text = load_knowledge()
    chunks = split_into_chunks(text)

    if not chunks:
        raise ValueError("Knowledge base file is empty!")

    # Remove old records from this source
    collection.delete(
        where={"source": "rag_reference.md"}
    )

    ids = [f"rag_chunk_{i}" for i in range(len(chunks))]

    metadatas = [
        {"source": "rag_reference.md", "chunk": i}
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=metadatas
    )

    print(f"Successfully stored {len(chunks)} knowledge chunks!")


def retrieve_information(question, top_k=3):
    """Find relevant information from the knowledge base."""

    total_chunks = collection.count()

    if total_chunks == 0:
        return []

    results = collection.query(
        query_texts=[question],
        n_results=min(top_k, total_chunks)
    )

    return results["documents"][0]


if __name__ == "_main_":

    print("Building RAG knowledge base...")

    build_knowledge_base()

    question = "What is Retrieval Augmented Generation?"

    print("\nSearching for relevant information...")

    retrieved_data = retrieve_information(question)

    print("\nRetrieved Information:")

    for index, item in enumerate(retrieved_data, start=1):
        print(f"\nChunk {index}:")
        print(item)

    print("\nRetrieval process completed!")
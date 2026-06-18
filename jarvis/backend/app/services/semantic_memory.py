import chromadb

client = chromadb.PersistentClient(
    path="app/chroma/chroma_db"
)

collection = client.get_or_create_collection(
    name="jarvis_memory"
)


def save_semantic_memory(content: str):

    collection.add(
        documents=[content],
        ids=[str(hash(content))]
    )


def search_memories(
    query: str,
    limit: int = 5
):

    results = collection.query(
        query_texts=[query],
        n_results=limit
    )

    return results["documents"][0]
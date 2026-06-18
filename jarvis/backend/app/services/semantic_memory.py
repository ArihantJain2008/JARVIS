import chromadb

client = chromadb.PersistentClient(
    path="app/chroma/chroma_db"
)

collection = client.get_or_create_collection(
    name="jarvis_memory"
)


def save_semantic_memory(content: str):

    memory_id = str(hash(content))

    try:

        collection.get(
            ids=[memory_id]
        )

        return False

    except Exception:

        collection.add(
            documents=[content],
            ids=[memory_id]
        )
        return True

def search_memories(
    query: str,
    limit: int = 5
):

    results = collection.query(
        query_texts=[query],
        n_results=limit
    )

    return results["documents"][0]

def build_semantic_context(
    query: str,
    limit: int = 5
):

    memories = search_memories(
        query,
        limit
    )

    if not memories:
        return "No relevant memories."

    return "\n".join(
        [f"- {memory}" for memory in memories]
    )
from app.services.semantic_memory import (
    save_semantic_memory,
    search_memories
)

save_semantic_memory(
    "I use VS Code every day"
)

results = search_memories(
    "Which IDE do I prefer?"
)

print(results)
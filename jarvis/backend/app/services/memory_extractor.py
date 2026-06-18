MEMORY_TRIGGERS = [
    "my name is",
    "my favorite",
    "i like",
    "i love",
    "i use",
    "i work with",
    "i study",
    "i am a",
    "i prefer"
]


def should_store_memory(message: str) -> bool:

    text = message.lower()

    return any(
        trigger in text
        for trigger in MEMORY_TRIGGERS
    )
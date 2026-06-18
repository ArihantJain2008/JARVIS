from fastapi import APIRouter
from pydantic import BaseModel
from app.services.memory import save_memory

from app.services.llm import ask_llm

from app.services.conversation import (
    add_message,
    get_history
)

from app.services.memory import (
    build_memory_context
)

from app.services.semantic_memory import (
    save_semantic_memory
)

from app.services.memory_extractor import (
    should_store_memory
)

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat_endpoint(data: ChatRequest):

    add_message(
        "user",
        data.message
    )

    if should_store_memory(data.message):
        save_memory(data.message)
        save_semantic_memory(data.message)

    memory_context = build_memory_context()

    memory_message = {
        "role": "system",
        "content": f"""
Known facts about the user:

{memory_context}

Use these memories when relevant.
"""
    }

    messages = get_history().copy()

    messages.insert(
        1,
        memory_message
    )

    response = ask_llm(messages)

    add_message(
        "assistant",
        response
    )

    return {
        "response": response
    }
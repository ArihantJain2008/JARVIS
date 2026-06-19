from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm import ask_llm

from app.services.conversation import (
    add_message,
    get_history
)

from app.services.memory import (
    save_memory
)

from app.services.semantic_memory import (
    save_semantic_memory,
    build_semantic_context
)

from app.services.memory_ranker import (
    should_remember
)

from app.services.tool_selector import (
    select_tool
)

from app.services.tool_executor import (
    execute_tool
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

    if should_remember(data.message):

        stored = save_memory(
            data.message
        )

        if stored:
            save_semantic_memory(
                data.message
            )

    tool = select_tool(
        data.message
    )

    if tool:

        result = execute_tool(
            tool
        )

        return {
            "response": result
        }

    memory_context = build_semantic_context(
        data.message
    )

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

    response = ask_llm(
        messages
    )

    add_message(
        "assistant",
        response
    )

    return {
        "response": response
    }
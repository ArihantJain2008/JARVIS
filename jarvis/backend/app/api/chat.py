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

from app.services.tool_call_parser import (
    parse_tool_call
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

    # Memory Storage
    if should_remember(data.message):

        stored = save_memory(
            data.message
        )

        if stored:
            save_semantic_memory(
                data.message
            )

        # Tool Calling
    tool_response = select_tool(
        data.message
    )

    print("\nTOOL RESPONSE:")
    print(tool_response)

    tool_call = parse_tool_call(
        tool_response
    )

    print("\nTOOL CALL:")
    print(tool_call)

    if tool_call:

        result = execute_tool(
            tool_call
        )

        if result:

            return {
                "response": result
            }

    # Semantic Memory Retrieval
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

    # Normal Chat
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
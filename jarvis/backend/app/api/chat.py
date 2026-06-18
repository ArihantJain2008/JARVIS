from fastapi import APIRouter
from pydantic import BaseModel
from ollama import chat

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat_endpoint(data: ChatRequest):

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": """
You are Jarvis.

You are a local AI assistant.

Be concise.

Avoid roleplaying.

Give direct answers.

You help with productivity,
files, programming,
research and desktop tasks.
"""
            },
            {
                "role": "user",
                "content": data.message
            }
        ]
    )

    return {
        "response": response["message"]["content"]
    }
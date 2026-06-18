from fastapi import APIRouter
from pydantic import BaseModel

from app.services.llm import ask_llm
from app.services.conversation import (
    add_message,
    get_history
)

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat_endpoint(data: ChatRequest):

    add_message("user", data.message)

    response = ask_llm(get_history())

    add_message("assistant", response)

    return {
        "response": response
    }
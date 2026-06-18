from fastapi import APIRouter

from app.services.memory import (
    save_memory,
    get_memories
)

router = APIRouter()


@router.get("/memory/add/{fact}")
def add_memory(fact: str):

    save_memory(fact)

    return {
        "saved": fact
    }


@router.get("/memory/list")
def list_memories():

    return {
        "memories": get_memories()
    }
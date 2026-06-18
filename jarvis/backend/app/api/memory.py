from fastapi import APIRouter

from app.services.memory import (
    save_memory,
    get_memories
)

router = APIRouter()


@router.get("/memory/save")
def save():

    save_memory(
        "My favorite editor is VS Code"
    )

    return {"status": "saved"}


@router.get("/memory/list")
def list_memories():

    return {
        "memories": get_memories()
    }
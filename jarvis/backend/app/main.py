from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.database.db import init_db
from app.api.memory import router as memory_router

app = FastAPI()

init_db()

app.include_router(chat_router)

app.include_router(memory_router)
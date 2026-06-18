from fastapi import FastAPI
from ollama import chat

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Jarvis Backend Running"}


@app.get("/test")
def test_qwen():

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": "Say hello from Jarvis."
            }
        ]
    )

    return {
        "response": response["message"]["content"]
    }
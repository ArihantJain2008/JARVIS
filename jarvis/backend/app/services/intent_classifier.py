from ollama import chat


VALID_INTENTS = [
    "launch_app",
    "take_screenshot",
    "chat",
    "unknown"
]


def classify_intent(message: str):

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": f"""
You are an intent classifier.

Possible intents:

launch_app
take_screenshot
chat
unknown

Reply with ONLY one intent.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    intent = (
        response["message"]["content"]
        .strip()
        .lower()
    )

    if intent not in VALID_INTENTS:
        return "unknown"

    return intent
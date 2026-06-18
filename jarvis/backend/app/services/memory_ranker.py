from ollama import chat


def should_remember(message: str) -> bool:

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": """
You are a memory classifier.

Decide whether a message contains
long-term personal information
worth remembering.

Examples:

My name is Arihant -> YES
I study BCA -> YES
My favorite editor is VS Code -> YES

Hello -> NO
Thanks -> NO
Open Chrome -> NO

Reply ONLY with YES or NO.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    answer = (
        response["message"]["content"]
        .strip()
        .upper()
    )

    return "YES" in answer
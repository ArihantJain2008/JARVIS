from ollama import chat


def extract_app_name(message: str):

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": """
Extract only the application name.

Examples:

Open Chrome
Chrome

Launch Spotify
Spotify

Start VS Code
VS Code

Reply ONLY with the app name.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return (
        response["message"]["content"]
        .strip()
    )
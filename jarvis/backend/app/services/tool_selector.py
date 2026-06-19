from ollama import chat


AVAILABLE_TOOLS = [
    "open_notepad",
    "open_calculator",
    "none"
]


def select_tool(message: str):

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": f"""
You are a tool selector.

Available tools:

{chr(10).join(AVAILABLE_TOOLS)}

Rules:

Open Notepad -> open_notepad
Launch Notepad -> open_notepad

Open Calculator -> open_calculator
Start Calculator -> open_calculator

If no tool matches:
reply with none

Reply ONLY with the tool name.
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    tool = (
        response["message"]["content"]
        .strip()
        .lower()
    )

    if tool not in AVAILABLE_TOOLS:
        return None

    if tool == "none":
        return None

    return tool
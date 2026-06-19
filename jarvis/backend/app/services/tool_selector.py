from ollama import chat

AVAILABLE_TOOLS = """
open_notepad
open_calculator
take_screenshot
"""


def select_tool(message: str):

    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": f"""
You are a tool calling AI.

Available tools:

{AVAILABLE_TOOLS}

Return ONLY valid JSON.

Examples:

User: Open Notepad

{{
  "tool": "open_notepad",
  "arguments": {{}}
}}

User: Open Calculator

{{
  "tool": "open_calculator",
  "arguments": {{}}
}}

User: Take a screenshot

{{
  "tool": "take_screenshot",
  "arguments": {{}}
}}

If no tool is needed:

{{
  "tool": "none",
  "arguments": {{}}
}}
"""
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response["message"]["content"]
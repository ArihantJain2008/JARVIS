from ollama import chat

AVAILABLE_TOOLS = """
open_notepad
open_calculator
take_screenshot
create_folder
list_files
read_file
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

User: Create a folder called Notes

{{
  "tool": "create_folder",
  "arguments": {{
    "folder_name": "Notes"
  }}
}}

User: Show files in Downloads

{{
  "tool": "list_files",
  "arguments": {{
    "path": "Downloads"
  }}
}}

User: Read todo.txt

{{
  "tool": "read_file",
  "arguments": {{
    "path": "todo.txt"
  }}
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
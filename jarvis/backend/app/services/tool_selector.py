from ollama import chat

AVAILABLE_TOOLS = """
open_notepad
open_calculator
take_screenshot
create_folder
list_files
read_file
write_file
append_file
type_text
press_key
hotkey
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

For file creation requests, extract both the file path and content.

For append requests, extract both the file path and content.

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

User: Create a file called notes.txt and write hello world

{{
  "tool": "write_file",
  "arguments": {{
    "path": "notes.txt",
    "content": "hello world"
  }}
}}

User: Add milk to shopping.txt

{{
  "tool": "append_file",
  "arguments": {{
    "path": "shopping.txt",
    "content": "milk"
  }}
}}

User: Append meeting notes to notes.txt

{{
  "tool": "append_file",
  "arguments": {{
    "path": "notes.txt",
    "content": "meeting notes"
  }}
}}

User: Type hello world

{{
  "tool": "type_text",
  "arguments": {{
    "text": "hello world"
  }}
}}

User: Press Enter

{{
  "tool": "press_key",
  "arguments": {{
    "key": "enter"
  }}
}}

User: Press Control S

{{
  "tool": "hotkey",
  "arguments": {{
    "keys": ["ctrl", "s"]
  }}
}}

User: Press Alt Tab

{{
  "tool": "hotkey",
  "arguments": {{
    "keys": ["alt", "tab"]
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
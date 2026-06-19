from app.tools.app_tools import (
    open_notepad,
    open_calculator
)


TOOLS = {
    "open_notepad": open_notepad,
    "open_calculator": open_calculator
}


def execute_tool(tool_name):

    if tool_name not in TOOLS:
        return "Tool not found."

    return TOOLS[tool_name]()
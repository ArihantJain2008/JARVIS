from app.tools.app_tools import (
    open_notepad,
    open_calculator
)

from app.tools.screenshot_tools import take_screenshot

TOOLS = {
    "open_notepad": open_notepad,
    "open_calculator": open_calculator,
    "take_screenshot": take_screenshot
}


def execute_tool(tool_name):

    if tool_name not in TOOLS:
        return "Tool not found."

    return TOOLS[tool_name]()
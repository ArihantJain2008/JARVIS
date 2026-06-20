from app.tools.app_tools import (
    open_notepad,
    open_calculator
)

from app.tools.screenshot_tools import (
    take_screenshot
)

from app.tools.file_tools import (
    create_folder,
    list_files,
    read_file,
    write_file,
    append_file
)

from app.tools.desktop_tools import (
    type_text,
    press_key,
    hotkey
)


TOOLS = {
    "open_notepad": open_notepad,
    "open_calculator": open_calculator,
    "take_screenshot": take_screenshot,

    "create_folder": create_folder,
    "list_files": list_files,
    "read_file": read_file,
    "write_file": write_file,
    "append_file": append_file,

    "type_text": type_text,
    "press_key": press_key,
    "hotkey": hotkey
}


def execute_tool(tool_call):

    tool_name = tool_call["tool"]

    arguments = tool_call.get(
        "arguments",
        {}
    )

    if tool_name == "none":
        return None

    if tool_name not in TOOLS:
        return None

    return TOOLS[tool_name](
        **arguments
    )
def select_tool(message: str):

    text = message.lower()

    if "notepad" in text:
        return "open_notepad"

    if "calculator" in text:
        return "open_calculator"

    return None
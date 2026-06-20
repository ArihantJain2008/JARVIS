import pyautogui


def type_text(text: str):

    pyautogui.write(
        text,
        interval=0.02
    )

    return (
        f"Typed: {text}"
    )


def press_key(key: str):

    pyautogui.press(
        key
    )

    return (
        f"Pressed: {key}"
    )


def hotkey(keys: list):

    pyautogui.hotkey(
        *keys
    )

    return (
        f"Pressed hotkey: {' + '.join(keys)}"
    )
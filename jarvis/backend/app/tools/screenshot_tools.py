import pyautogui
from datetime import datetime


def take_screenshot():

    filename = (
        f"screenshot_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    )

    pyautogui.screenshot(
        filename
    )

    return f"Screenshot saved: {filename}"
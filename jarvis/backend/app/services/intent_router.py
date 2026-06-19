from app.services.intent_classifier import (
    classify_intent
)

from app.services.app_launcher import (
    execute_app_launch
)

from app.tools.screenshot_tools import (
    take_screenshot
)


def route_intent(message: str):

    intent = classify_intent(
        message
    )

    if intent == "launch_app":
        return execute_app_launch(
            message
        )

    if intent == "take_screenshot":
        return take_screenshot()

    return None
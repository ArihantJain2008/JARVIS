from app.tools.app_tools import (
    open_app
)

from app.services.app_name_extractor import (
    extract_app_name
)


def execute_app_launch(message: str):

    app_name = extract_app_name(
        message
    )

    return open_app(
        app_name
    )
import os


SEARCH_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(
        r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    )
]


def find_app(app_name: str):

    app_name = app_name.lower()

    for path in SEARCH_PATHS:

        if not os.path.exists(path):
            continue

        for root, _, files in os.walk(path):

            for file in files:

                if not file.endswith(".lnk"):
                    continue

                if app_name in file.lower():

                    return os.path.join(
                        root,
                        file
                    )

    return None
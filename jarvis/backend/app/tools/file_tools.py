from pathlib import Path


def create_folder(folder_name: str):

    try:

        path = Path(folder_name)

        path.mkdir(
            parents=True,
            exist_ok=True
        )

        return f"Folder created: {path}"

    except Exception as e:

        return str(e)


def list_files(path: str = "."):

    try:

        files = []

        for item in Path(path).iterdir():

            files.append(
                item.name
            )

        return "\n".join(files)

    except Exception as e:

        return str(e)


def read_file(path: str):

    try:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    except Exception as e:

        return str(e)
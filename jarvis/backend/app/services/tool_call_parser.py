import json


def parse_tool_call(response: str):

    try:
        return json.loads(response)

    except Exception:
        return None
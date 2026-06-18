conversation_history = [
    {
        "role": "system",
        "content": """
You are Jarvis.

You are a local AI assistant.

Be concise.

Avoid roleplaying.

Help with productivity,
programming,
research,
and desktop tasks.
"""
    }
]


def add_message(role: str, content: str):
    conversation_history.append({
        "role": role,
        "content": content
    })


def get_history():
    return conversation_history


def clear_history():
    global conversation_history

    conversation_history = [
        {
            "role": "system",
            "content": """
You are Jarvis.

You are a local AI assistant.

Be concise.

Avoid roleplaying.
"""
        }
    ]
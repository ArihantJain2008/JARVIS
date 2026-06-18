from app.database.db import get_connection

def save_memory(content: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM memories WHERE content = ?",
        (content,)
    )

    existing = cursor.fetchone()

    if existing:
        conn.close()
        return False

    cursor.execute(
        "INSERT INTO memories (content) VALUES (?)",
        (content,)
    )

    conn.commit()
    conn.close()

    return True


def get_memories():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT content FROM memories"
    )

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def build_memory_context():

    memories = get_memories()

    if not memories:
        return "No stored memories."

    return "\n".join(
        [f"- {memory}" for memory in memories]
    )
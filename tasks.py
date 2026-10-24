from datetime import datetime

from database import get_connection

VALID_PRIORITIES = ("baixa", "media", "alta")


def create_task(title, description="", priority="media", due_date=None):
    # 1. valida o título
    if not title or not title.strip():
        raise ValueError("O título não pode ser vazio.")

    # 2. valida a prioridade
    if priority not in VALID_PRIORITIES:
        raise ValueError(
            f"Prioridade inválida. Use: {', '.join(VALID_PRIORITIES)}."
        )

    # 3. valida o prazo (opcional)
    if due_date is not None:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Prazo inválido. Use o formato AAAA-MM-DD.")

    # 4. insere no banco
    conn = get_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, priority, due_date) "
            "VALUES (?, ?, ?, ?)",
            (title.strip(), description, priority, due_date),
        )
        conn.commit()
        # 5. devolve o id da tarefa criada
        return cursor.lastrowid
    finally:
        conn.close()
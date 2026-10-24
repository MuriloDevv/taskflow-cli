# tasks.py
from datetime import datetime

from database import get_connection

VALID_PRIORITIES = ("baixa", "media", "alta")
VALID_STATUSES = ("pendente", "concluida")


def _validate_priority(priority):
    if priority not in VALID_PRIORITIES:
        raise ValueError(
            f"Prioridade inválida. Use: {', '.join(VALID_PRIORITIES)}."
        )


def _validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Prazo inválido. Use o formato AAAA-MM-DD.")


def create_task(title, description="", priority="media", due_date=None):
    if not title or not title.strip():
        raise ValueError("O título não pode ser vazio.")
    _validate_priority(priority)
    if due_date is not None:
        _validate_due_date(due_date)

    conn = get_connection()
    try:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, priority, due_date) "
            "VALUES (?, ?, ?, ?)",
            (title.strip(), description, priority, due_date),
        )
        conn.commit()
        return cursor.lastrowid
    finally:
        conn.close()


def get_task(task_id):
    conn = get_connection()
    try:
        cursor = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
    finally:
        conn.close()

    if row is None:
        raise ValueError("Tarefa não encontrada.")
    return dict(row)


def list_tasks(status=None, priority=None):
    if status is not None and status not in VALID_STATUSES:
        raise ValueError(f"Status inválido. Use: {', '.join(VALID_STATUSES)}.")
    if priority is not None:
        _validate_priority(priority)

    query = "SELECT * FROM tasks"
    conditions = []
    params = []

    if status is not None:
        conditions.append("status = ?")
        params.append(status)
    if priority is not None:
        conditions.append("priority = ?")
        params.append(priority)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    query += " ORDER BY id"

    conn = get_connection()
    try:
        cursor = conn.execute(query, params)
        rows = cursor.fetchall()
    finally:
        conn.close()

    return [dict(row) for row in rows]


def complete_task(task_id):
    conn = get_connection()
    try:
        cursor = conn.execute(
            "UPDATE tasks SET status = 'concluida' WHERE id = ?", (task_id,)
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise ValueError("Tarefa não encontrada.")
    finally:
        conn.close()


def delete_task(task_id):
    conn = get_connection()
    try:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise ValueError("Tarefa não encontrada.")
    finally:
        conn.close()


def update_task(task_id, title=None, description=None):
    fields = []
import sqlite3

DB_NAME = "taskflow.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # permite acessar colunas pelo nome
    return conn


def init_db():
    conn = get_connection()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                title       TEXT NOT NULL CHECK (length(trim(title)) > 0),
                description TEXT,
                status      TEXT NOT NULL DEFAULT 'pendente'
                            CHECK (status IN ('pendente', 'concluida')),
                priority    TEXT NOT NULL DEFAULT 'media'
                            CHECK (priority IN ('baixa', 'media', 'alta')),
                due_date    TEXT,
                created_at  TEXT NOT NULL DEFAULT (datetime('now'))
            )
        """)
        conn.commit()
    finally:
        conn.close()


if __name__ == "__main__":
    init_db()
    print("Banco criado!")
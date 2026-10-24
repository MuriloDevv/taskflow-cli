from database import init_db
from tasks import create_task


def main():
    init_db()
    task_id = create_task("Estudar SQL")
    print("Tarefa criada com id:", task_id)


if __name__ == "__main__":
    main()
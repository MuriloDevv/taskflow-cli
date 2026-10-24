# cli.py
import sqlite3

from tasks import (
    complete_task,
    create_task,
    delete_task,
    get_task,
    list_tasks,
    update_task,
)


def print_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    print(f"{'ID':<4} {'Título':<20} {'Status':<10} {'Prioridade':<10} {'Prazo':<10}")
    print("-" * 58)

    for task in tasks:
        title = task["title"][:20]
        due_date = task["due_date"] or "-"
        print(
            f"{task['id']:<4} {title:<20} {task['status']:<10} "
            f"{task['priority']:<10} {due_date:<10}"
        )


def show_menu():
    print()
    print("=== TaskFlow ===")
    print("1. Listar tarefas")
    print("2. Adicionar tarefa")
    print("3. Consultar tarefa por ID")
    print("4. Editar tarefa")
    print("5. Concluir tarefa")
    print("6. Excluir tarefa")
    print("7. Filtrar tarefas")
    print("0. Sair")


def read_id():
    raw = input("ID da tarefa: ").strip()
    try:
        return int(raw)
    except ValueError:
        raise ValueError("ID inválido. Digite um número.")


def add_task_flow():
    title = input("Título: ")
    description = input("Descrição (Enter para pular): ")
    priority = input("Prioridade [baixa/media/alta] (Enter = media): ").strip() or "media"
    due_date = input("Prazo AAAA-MM-DD (Enter para pular): ").strip() or None

    task_id = create_task(title, description, priority, due_date)
    print(f"Tarefa criada com id {task_id}.")


def get_task_flow():
    task_id = read_id()
    task = get_task(task_id)
    print()
    print(f"ID:         {task['id']}")
    print(f"Título:     {task['title']}")
    print(f"Descrição:  {task['description'] or '-'}")
    print(f"Status:     {task['status']}")
    print(f"Prioridade: {task['priority']}")
    print(f"Prazo:      {task['due_date'] or '-'}")
    print(f"Criada em:  {task['created_at']}")


def update_task_flow():
    task_id = read_id()
    get_task(task_id)  # garante que existe antes de perguntar

    title = input("Novo título (Enter para manter): ")
    description = input("Nova descrição (Enter para manter): ")

    update_task(
        task_id,
        title=title if title.strip() else None,
        description=description if description.strip() else None,
    )
    print("Tarefa atualizada.")


def complete_task_flow():
    complete_task(read_id())
    print("Tarefa concluída.")


def delete_task_flow():
    task_id = read_id()
    task = get_task(task_id)
    confirm = input(f"Excluir '{task['title']}'? (s/n): ").strip().lower()
    if confirm == "s":
        delete_task(task_id)
        print("Tarefa excluída.")
    else:
        print("Cancelado.")


def filter_tasks_flow():
    status = input("Status [pendente/concluida] (Enter para todos): ").strip() or None
    priority = input("Prioridade [baixa/media/alta] (Enter para todas): ").strip() or None
    print_tasks(list_tasks(status=status, priority=priority))


def run():
    actions = {
        "1": lambda: print_tasks(list_tasks()),
        "2": add_task_flow,
        "3": get_task_flow,
        "4": update_task_flow,
        "5": complete_task_flow,
        "6": delete_task_flow,
        "7": filter_tasks_flow,
    }

    while True:
        show_menu()
        try:
            option = input("Escolha: ").strip()

            if option == "0":
                print("Até logo!")
                break

            action = actions.get(option)
            if action is None:
                print("Opção inválida.")
                continue

            action()
        except ValueError as error:
            print(f"Erro: {error}")
        except sqlite3.Error as error:
            print(f"Erro no banco de dados: {error}")
        except (KeyboardInterrupt, EOFError):
            print()
            print("Até logo!")
            break
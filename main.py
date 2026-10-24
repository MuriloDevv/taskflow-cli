# main.py
from cli import run
from database import init_db


def main():
    init_db()
    run()


if __name__ == "__main__":
    main()
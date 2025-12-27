from repository import TodoRepository
from services import TodoService
from cli import TodoCLI

def main():
    repository = TodoRepository()
    service = TodoService(repository)
    cli = TodoCLI(service)
    cli.run()

if __name__ == "__main__":
    main()
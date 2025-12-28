from services import TodoService
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt


class TodoCLI:
    def __init__(self, service: TodoService):
        self.service = service
        self.console = Console()

    def _make_todo_table(self, todos) -> Table:
        table = Table(title="Todos", show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Title", min_width=20)
        table.add_column("Description", min_width=20)
        table.add_column("Status", justify="right")

        for todo in todos:
            status_text = "✅ Completed" if todo.completed else "⏳ Pending"
            status_style = "green" if todo.completed else "red"
            description = todo.description if todo.description else "N/A"
            table.add_row(
                str(todo.id),
                todo.title,
                description,
                Text(status_text, style=status_style)
            )
        return table

    def run(self):
        self.console.print(Panel(Text("🚀 Welcome to Todo CLI 🚀", justify="center", style="bold blue")))
        while True:
            self.console.print("\n[bold]Options:[/bold]")
            self.console.print("1. [bold green]Add[/bold green] Todo")
            self.console.print("2. [bold cyan]View[/bold cyan] Todos")
            self.console.print("3. [bold yellow]Update[/bold yellow] Todo")
            self.console.print("4. [bold red]Delete[/bold red] Todo")
            self.console.print("5. [bold magenta]Mark[/bold magenta] Complete/Incomplete")
            self.console.print("6. [bold]Exit[/bold]")
            
            try:
                choice = Prompt.ask("[bold]Select an option[/bold]", choices=["1", "2", "3", "4", "5", "6"], default="2")
            except (EOFError, KeyboardInterrupt):
                self.console.print("\n[bold red]Exiting...[/bold red]")
                break

            if choice == '1':
                self._handle_add_todo()
            elif choice == '2':
                self._handle_view_todos()
            elif choice == '3':
                self._handle_update_todo()
            elif choice == '4':
                self._handle_delete_todo()
            elif choice == '5':
                self._handle_toggle_complete()
            elif choice == '6':
                self.console.print("[bold blue]Goodbye![/bold blue]")
                break

    def _handle_add_todo(self):
        self.console.print("\n[bold green]--- Add New Todo ---[/bold green]")
        try:
            title = Prompt.ask("[cyan]Enter title[/cyan]")
            description = Prompt.ask("[cyan]Enter description (optional)[/cyan]", default=None)
            
            created_todo = self.service.add_todo(title, description)
            self.console.print(f"[green]Todo added successfully:[/green]")
            self.console.print(self._make_todo_table([created_todo]))
            
        except ValueError as e:
            self.console.print(f"[red]Error: {e}[/red]")

    def _handle_view_todos(self):
        self.console.print("\n[bold cyan]--- All Todos ---[/bold cyan]")
        todos = self.service.get_all_todos()
        if not todos:
            self.console.print("[yellow]No todos available.[/yellow]")
            return

        sorted_todos = sorted(todos, key=lambda t: t.completed)
        self.console.print(self._make_todo_table(sorted_todos))

    def _handle_update_todo(self):
        self.console.print("\n[bold yellow]--- Update Todo ---[/bold yellow]")
        todos = self.service.get_all_todos()
        if not todos:
            self.console.print("[yellow]No todos available to update.[/yellow]")
            return

        self.console.print(self._make_todo_table(todos))
        
        try:
            todo_id = Prompt.ask("[cyan]Enter the ID of the todo to update[/cyan]",
                                 choices=[str(t.id) for t in todos])
            todo_id = int(todo_id)
        except ValueError:
            self.console.print("[red]Error: Invalid ID. Please enter a number.[/red]")
            return

        try:
            current_todo = self.service.repository.get_by_id(todo_id)
            if not current_todo:
                raise ValueError(f"Todo with ID {todo_id} not found.")

            new_title = Prompt.ask(f"[cyan]Enter new title[/cyan]", default=current_todo.title)
            new_description = Prompt.ask(f"[cyan]Enter new description (optional)[/cyan]", default=current_todo.description)
            
            updated_todo = self.service.update_todo(todo_id, new_title, new_description)
            self.console.print(f"[green]Todo with ID {todo_id} updated successfully:[/green]")
            self.console.print(self._make_todo_table([updated_todo]))
            
        except ValueError as e:
            self.console.print(f"[red]Error: {e}[/red]")
    
    def _handle_delete_todo(self):
        self.console.print("\n[bold red]--- Delete Todo ---[/bold red]")
        todos = self.service.get_all_todos()
        if not todos:
            self.console.print("[yellow]No todos available to delete.[/yellow]")
            return

        self.console.print(self._make_todo_table(todos))
        
        try:
            todo_id = Prompt.ask("[cyan]Enter the ID of the todo to delete[/cyan]",
                                 choices=[str(t.id) for t in todos])
            todo_id = int(todo_id)
        except ValueError:
            self.console.print("[red]Error: Invalid ID. Please enter a number.[/red]")
            return

        try:
            self.service.delete_todo(todo_id)
            self.console.print(f"[green]Todo with ID {todo_id} deleted successfully.[/green]")
        except ValueError as e:
            self.console.print(f"[red]Error: {e}[/red]")
    
    def _handle_toggle_complete(self):
        self.console.print("\n[bold magenta]--- Toggle Todo Completion Status ---[/bold magenta]")
        todos = self.service.get_all_todos()
        if not todos:
            self.console.print("[yellow]No todos available to toggle.[/yellow]")
            return

        self.console.print(self._make_todo_table(todos))

        try:
            todo_id = Prompt.ask("[cyan]Enter the ID of the todo to toggle completion status[/cyan]",
                                 choices=[str(t.id) for t in todos])
            todo_id = int(todo_id)
        except ValueError:
            self.console.print("[red]Error: Invalid ID. Please enter a number.[/red]")
            return
        
        try:
            updated_todo = self.service.toggle_complete(todo_id)
            status = "completed" if updated_todo.completed else "incomplete"
            self.console.print(f"[green]Todo with ID {todo_id} marked as {status}.[/green]")
        except ValueError as e:
            self.console.print(f"[red]Error: {e}[/red]")


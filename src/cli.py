from services import TodoService
import sys

class TodoCLI:
    def __init__(self, service: TodoService):
        self.service = service

    def run(self):
        print("Welcome to Todo CLI")
        while True:
            print("\nOptions:")
            print("1. Add Todo")
            print("2. View Todos")
            print("3. Update Todo")
            print("4. Delete Todo")
            print("5. Mark Complete/Incomplete") # New option
            print("6. Exit")
            
            try:
                choice = input("Select an option: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting...")
                break

            if choice == '1':
                self._handle_add_todo()
            elif choice == '2':
                self._handle_view_todos()
            elif choice == '3':
                self._handle_update_todo()
            elif choice == '4':
                self._handle_delete_todo()
            elif choice == '5': # New option handler
                self._handle_toggle_complete()
            elif choice == '6':
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")

    def _handle_add_todo(self):
        print("\n--- Add New Todo ---")
        try:
            title = input("Enter title: ").strip()
            description = input("Enter description (optional): ").strip()
            
            if not description:
                description = None

            created_todo = self.service.add_todo(title, description)
            print(f"Todo added successfully: {created_todo}")
            
        except ValueError as e:
            print(f"Error: {e}")

    def _handle_view_todos(self):
        print("\n--- All Todos ---")
        todos = self.service.get_all_todos()
        if not todos:
            print("No todos available.")
            return

        for todo in todos:
            status = "✓" if todo.completed else " "
            print(f"[{status}] ID: {todo.id}, Title: {todo.title}, Description: {todo.description if todo.description else 'N/A'}")
            print("-" * 20)

    def _handle_update_todo(self):
        print("\n--- Update Todo ---")
        todos = self.service.get_all_todos()
        if not todos:
            print("No todos available to update.")
            return

        print("Current Todos:")
        for todo in todos:
            print(f"[{todo.id}] {todo.title}")
        
        try:
            todo_id_str = input("Enter the ID of the todo to update: ").strip()
            todo_id = int(todo_id_str)
        except ValueError:
            print("Error: Invalid ID. Please enter a number.")
            return

        try:
            # Re-fetch the todo to display current values correctly in case a prior update failed silently
            current_todo = self.service.repository.get_by_id(todo_id)
            if not current_todo:
                raise ValueError(f"Todo with ID {todo_id} not found.")

            new_title = input(f"Enter new title (current: {current_todo.title}): ").strip()
            new_description = input(f"Enter new description (current: {current_todo.description if current_todo.description else 'N/A'} - optional): ").strip()

            if not new_description:
                new_description = None

            updated_todo = self.service.update_todo(todo_id, new_title, new_description)
            print(f"Todo with ID {todo_id} updated successfully: {updated_todo}")
            
        except ValueError as e:
            print(f"Error: {e}")
    
    def _handle_delete_todo(self):
        print("\n--- Delete Todo ---")
        todos = self.service.get_all_todos()
        if not todos:
            print("No todos available to delete.")
            return

        print("Current Todos:")
        for todo in todos:
            print(f"[{todo.id}] {todo.title}")
        
        try:
            todo_id_str = input("Enter the ID of the todo to delete: ").strip()
            todo_id = int(todo_id_str)
        except ValueError:
            print("Error: Invalid ID. Please enter a number.")
            return

        try:
            self.service.delete_todo(todo_id)
            print(f"Todo with ID {todo_id} deleted successfully.")
        except ValueError as e:
            print(f"Error: {e}")
    
    def _handle_toggle_complete(self):
        print("\n--- Toggle Todo Completion Status ---")
        todos = self.service.get_all_todos()
        if not todos:
            print("No todos available to toggle.")
            return

        print("Current Todos:")
        for todo in todos:
            status = "✓" if todo.completed else " "
            print(f"[{status}] ID: {todo.id}, Title: {todo.title}")

        try:
            todo_id_str = input("Enter the ID of the todo to toggle completion status: ").strip()
            todo_id = int(todo_id_str)
        except ValueError:
            print("Error: Invalid ID. Please enter a number.")
            return
        
        try:
            updated_todo = self.service.toggle_complete(todo_id)
            status = "completed" if updated_todo.completed else "incomplete"
            print(f"Todo with ID {todo_id} marked as {status}.")
        except ValueError as e:
            print(f"Error: {e}")


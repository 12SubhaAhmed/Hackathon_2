from typing import Optional
from models import Todo
from repository import TodoRepository

class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def add_todo(self, title: str, description: Optional[str] = None) -> Todo:
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        
        # ID 0 is a placeholder for a new item before persistence
        new_todo = Todo(id=0, title=title.strip(), description=description)
        saved_todo = self.repository.add(new_todo)
        return saved_todo

    def get_all_todos(self):
        return self.repository.list_all()

    def update_todo(self, todo_id: int, new_title: str, new_description: Optional[str] = None) -> Todo:
        if not new_title or not new_title.strip():
            raise ValueError("Title cannot be empty")

        todo_to_update = self.repository.get_by_id(todo_id)
        if not todo_to_update:
            raise ValueError(f"Todo with ID {todo_id} not found.")

        todo_to_update.title = new_title.strip()
        todo_to_update.description = new_description

        updated_todo = self.repository.update(todo_to_update)
        if not updated_todo: # Should not happen if get_by_id worked
            raise ValueError(f"Failed to update todo with ID {todo_id}.")
        return updated_todo

    def delete_todo(self, todo_id: int) -> None:
        if not self.repository.delete(todo_id):
            raise ValueError(f"Todo with ID {todo_id} not found.")

    def toggle_complete(self, todo_id: int) -> Todo:
        todo_to_toggle = self.repository.get_by_id(todo_id)
        if not todo_to_toggle:
            raise ValueError(f"Todo with ID {todo_id} not found.")
        
        todo_to_toggle.completed = not todo_to_toggle.completed
        updated_todo = self.repository.update(todo_to_toggle)
        if not updated_todo:
            raise ValueError(f"Failed to toggle completion for todo with ID {todo_id}.")
        return updated_todo


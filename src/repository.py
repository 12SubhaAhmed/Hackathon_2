from typing import List, Optional
from models import Todo

class TodoRepository:
    def __init__(self):
        self._todos: List[Todo] = []
        self._next_id: int = 1

    def add(self, todo: Todo) -> Todo:
        """
        Adds a todo to the repository.
        Assigns an ID if not already assigned (though logic usually handles this before).
        Actually, for in-memory auto-increment, it's safer if the repo handles ID generation 
        or the service does.
        Let's have the repo assign the ID to ensure uniqueness within its scope.
        """
        todo.id = self._next_id
        self._next_id += 1
        self._todos.append(todo)
        return todo

    def list_all(self) -> List[Todo]:
        return list(self._todos)

    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        for todo in self._todos:
            if todo.id == todo_id:
                return todo
        return None

    def update(self, updated_todo: Todo) -> Optional[Todo]:
        for i, todo in enumerate(self._todos):
            if todo.id == updated_todo.id:
                self._todos[i] = updated_todo
                return updated_todo
        return None  # Todo not found

    def delete(self, todo_id: int) -> bool:
        initial_len = len(self._todos)
        self._todos = [todo for todo in self._todos if todo.id != todo_id]
        return len(self._todos) < initial_len


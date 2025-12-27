Feature: Add Todo Item

Goal:
Allow the user to add a new todo item using the console interface.

Requirements:
- Each todo must have:
  - id (auto-increment integer)
  - title (string, required)
  - description (string, optional)
  - completed (boolean, default False)
- Todos are stored in memory only.
- IDs must be unique for the session.
- Empty titles are not allowed.

Acceptance Criteria:
- User is prompted for title and description.
- A todo is added successfully to memory.
- The todo can be viewed in the list immediately after creation.

Constraints:
- No database or file storage.
- Use clean, readable Python code.
- Follow existing project structure.
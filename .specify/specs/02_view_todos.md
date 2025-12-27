Feature: View Todos

Goal:
Allow the user to view all todo items added in the current session.

Requirements:
- List all todos with:
  - ID
  - Title
  - Description
  - Completed status
- Should display "No todos available" if list is empty
- Read-only, does not modify todos

Acceptance Criteria:
- User selects "View Todos" option from CLI
- Todos are displayed in a readable format
- Works immediately after adding todos

Feature: Delete Todo

Goal:
Allow the user to delete an existing todo item by its ID.

Requirements:
- User can select a todo by its ID to delete
- Validation:
  - ID must exist
- Deleted todo should be removed from memory immediately
- Confirmation message displayed after deletion

Acceptance Criteria:
- User selects "Delete Todo" option from CLI
- Todos list shows all todos with IDs before deletion
- After deletion, todo is removed
- Error shown if invalid ID

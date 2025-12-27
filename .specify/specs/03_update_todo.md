Feature: Update Todo

Goal:
Allow the user to update an existing todo item’s title and description.

Requirements:
- User can select a todo by its ID
- User can update:
  - Title (required, cannot be empty)
  - Description (optional)
- Completed status should remain unchanged
- Validation:
  - ID must exist
  - Title cannot be empty

Acceptance Criteria:
- User selects "Update Todo" option from CLI
- Todos list shows all todos with IDs
- After update, todo reflects new title/description
- Error shown if invalid ID or empty title

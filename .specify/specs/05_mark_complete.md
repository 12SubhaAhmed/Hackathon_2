Feature: Mark Todo Complete / Incomplete

Goal:
Allow the user to toggle the completion status of a todo item by its ID.

Requirements:
- User can select a todo by its ID
- User can mark it as:
  - Completed (True)
  - Incomplete (False)
- Validation:
  - ID must exist
- Confirmation message displayed after update

Acceptance Criteria:
- User selects "Mark Complete/Incomplete" from CLI
- Todos list shows all todos with IDs before updating
- After updating, completed status reflects the change
- Error shown if invalid ID

# CLI Interface Contract: Console Todo Application

**Feature**: Console Todo Application (001-todo-app)
**Date**: 2025-12-30
**Interface Type**: Console Menu-Driven
**Status**: Complete

## Purpose

This document defines the console interface contract for the todo application, specifying all user interactions, menu options, input prompts, output formats, and error messages.

## Main Menu

### Display Format

```
=== Todo Application ===

1. Add Task
2. List Tasks
3. Mark Task Complete/Incomplete
4. Update Task
5. Delete Task
6. Quit

Enter your choice (1-6):
```

### Input Specification

- **Prompt**: `Enter your choice (1-6): `
- **Valid Input**: Integer 1, 2, 3, 4, 5, or 6
- **Invalid Input Handling**:
  - Non-integer: Display "Error: Please enter a number between 1 and 6."
  - Out of range: Display "Error: Please enter a number between 1 and 6."
  - Behavior: Re-display menu and prompt again

### Navigation Flow

- After completing any operation (add, list, update, delete, toggle), return to main menu
- Loop continues until user selects option 6 (Quit)

## Operation 1: Add Task

### User Flow

1. User selects option 1
2. System prompts for title
3. User enters title
4. System validates title (non-empty)
5. System prompts for description
6. User enters description (optional, can press Enter for empty)
7. System creates task with auto-assigned ID
8. System displays success message
9. Return to main menu

### Prompts and Inputs

```
Enter task title: [user input]
Enter task description (optional): [user input]
```

### Success Response

```
✓ Task added successfully! (ID: [task_id])
```

### Error Responses

**Empty Title**:
```
Error: Title cannot be empty. Task not created.
```

### Examples

**Success Case**:
```
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
✓ Task added successfully! (ID: 1)
```

**Error Case**:
```
Enter task title:
Error: Title cannot be empty. Task not created.
```

## Operation 2: List Tasks

### User Flow

1. User selects option 2
2. System displays all tasks in formatted table
3. Return to main menu

### Output Format

**With Tasks**:
```
=== All Tasks ===

ID: 1  |  Status: [TODO]
Title: Buy groceries
Description: Milk, bread, eggs
---

ID: 2  |  Status: [DONE]
Title: Call dentist
Description:
---

ID: 3  |  Status: [TODO]
Title: Finish report
Description: Q4 summary for team meeting
---

Total: 3 task(s)
```

**No Tasks**:
```
=== All Tasks ===

No tasks found. Add a task to get started!
```

### Display Rules

- Each task separated by `---` line
- Empty description shows as blank line (not "None" or "N/A")
- Status indicator: `[TODO]` for incomplete, `[DONE]` for complete
- Tasks displayed in order they appear in storage (insertion order)
- Total count displayed at end

## Operation 3: Mark Task Complete/Incomplete

### User Flow

1. User selects option 3
2. System prompts for task ID
3. User enters task ID
4. System validates ID (integer, exists in list)
5. System toggles completion status
6. System displays success message with new status
7. Return to main menu

### Prompts and Inputs

```
Enter task ID to toggle: [user input]
```

### Success Response

**Marked Complete**:
```
✓ Task [task_id] marked as complete.
```

**Marked Incomplete**:
```
✓ Task [task_id] marked as incomplete.
```

### Error Responses

**Invalid ID Format**:
```
Error: Task ID must be a number.
```

**Task Not Found**:
```
Error: Task [task_id] not found.
```

### Examples

**Success Case (Toggle to Complete)**:
```
Enter task ID to toggle: 1
✓ Task 1 marked as complete.
```

**Success Case (Toggle to Incomplete)**:
```
Enter task ID to toggle: 1
✓ Task 1 marked as incomplete.
```

**Error Case**:
```
Enter task ID to toggle: 99
Error: Task 99 not found.
```

## Operation 4: Update Task

### User Flow

1. User selects option 4
2. System prompts for task ID
3. User enters task ID
4. System validates ID (integer, exists in list)
5. System prompts for new title with current value shown
6. User enters new title or presses Enter to keep current
7. System prompts for new description with current value shown
8. User enters new description or presses Enter to keep current
9. System validates at least one field changed and title not empty
10. System updates task
11. System displays success message
12. Return to main menu

### Prompts and Inputs

```
Enter task ID to update: [user input]

Current title: [current_title]
Enter new title (or press Enter to keep current): [user input]

Current description: [current_description]
Enter new description (or press Enter to keep current): [user input]
```

### Success Response

```
✓ Task [task_id] updated successfully.
```

### Error Responses

**Invalid ID Format**:
```
Error: Task ID must be a number.
```

**Task Not Found**:
```
Error: Task [task_id] not found.
```

**Empty Title Provided**:
```
Error: Title cannot be empty. Task not updated.
```

### Examples

**Update Both Fields**:
```
Enter task ID to update: 1

Current title: Buy groceries
Enter new title (or press Enter to keep current): Buy groceries and supplies

Current description: Milk, bread, eggs
Enter new description (or press Enter to keep current): Milk, bread, eggs, butter

✓ Task 1 updated successfully.
```

**Update Title Only**:
```
Enter task ID to update: 2

Current title: Call dentist
Enter new title (or press Enter to keep current): Call dentist for checkup

Current description:
Enter new description (or press Enter to keep current):

✓ Task 2 updated successfully.
```

## Operation 5: Delete Task

### User Flow

1. User selects option 5
2. System prompts for task ID
3. User enters task ID
4. System validates ID (integer, exists in list)
5. System deletes task
6. System displays success message
7. Return to main menu

### Prompts and Inputs

```
Enter task ID to delete: [user input]
```

### Success Response

```
✓ Task [task_id] deleted successfully.
```

### Error Responses

**Invalid ID Format**:
```
Error: Task ID must be a number.
```

**Task Not Found**:
```
Error: Task [task_id] not found.
```

### Examples

**Success Case**:
```
Enter task ID to delete: 3
✓ Task 3 deleted successfully.
```

**Error Case**:
```
Enter task ID to delete: abc
Error: Task ID must be a number.
```

## Operation 6: Quit

### User Flow

1. User selects option 6
2. System displays exit message
3. Application terminates

### Exit Message

```
Goodbye! All tasks will be lost (in-memory only).
```

### Behavior

- Graceful shutdown (no errors or exceptions)
- All task data is lost (per in-memory constraint)
- No prompts or confirmations

## Error Handling Standards

### Validation Principles

1. **Validate early**: Check input at UI layer before processing
2. **Fail gracefully**: Display error, return to menu (don't crash)
3. **Clear messages**: Tell user what went wrong and what to do
4. **No stack traces**: Never show Python errors to end user

### Common Error Patterns

**Non-Integer Task ID**:
- Input: "abc", "1.5", ""
- Response: "Error: Task ID must be a number."

**Non-Existent Task ID**:
- Input: Valid integer but not in current task list
- Response: "Error: Task [id] not found."

**Empty Title**:
- Input: "", "   " (whitespace only)
- Response: "Error: Title cannot be empty. Task not created/updated."

**Invalid Menu Choice**:
- Input: "0", "7", "abc"
- Response: "Error: Please enter a number between 1 and 6."

## Display Standards

### Visual Separators

- Main menu: `=== Todo Application ===`
- Task list header: `=== All Tasks ===`
- Between tasks: `---`

### Status Indicators

- Incomplete: `[TODO]`
- Complete: `[DONE]`
- Never use: ☐/☑, ✓/✗, or other Unicode symbols (for compatibility)

### Success Messages

- Pattern: `✓ [Action] [result].`
- Examples:
  - `✓ Task added successfully! (ID: 1)`
  - `✓ Task 2 marked as complete.`
  - `✓ Task 3 updated successfully.`

### Error Messages

- Pattern: `Error: [What went wrong]. [Optional: what to do].`
- Examples:
  - `Error: Task ID must be a number.`
  - `Error: Task 99 not found.`
  - `Error: Title cannot be empty. Task not created.`

## Input Handling

### String Inputs (Title, Description)

- Use `input()` function
- Apply `.strip()` to remove leading/trailing whitespace
- Empty string after strip is considered empty for title validation
- Preserve internal whitespace and formatting

### Integer Inputs (Task ID, Menu Choice)

- Use `input()` function to get string
- Attempt `int()` conversion
- Catch `ValueError` for non-integer input
- Validate range after successful conversion

### Optional Inputs (Description, Update Fields)

- Empty input (just pressing Enter) means:
  - For description during add: Use empty string ""
  - For update fields: Keep current value unchanged

## Compatibility

### Platform Support

- Must work on: Windows, macOS, Linux
- Use standard ASCII characters only (avoid Unicode box-drawing)
- Use `\n` for line breaks (cross-platform compatible)

### Terminal Requirements

- Standard console/terminal (80 column minimum recommended)
- No special terminal features required (colors, cursor control, etc.)
- No external terminal libraries needed

## Testing Scenarios

### Happy Path

1. Add task → List tasks → Mark complete → List tasks → Update task → List tasks → Delete task → Quit

### Edge Cases

1. List when no tasks exist
2. Update task with very long title/description
3. Delete all tasks, then list
4. Rapid creation of 100+ tasks
5. Special characters in title/description

### Error Cases

1. Invalid menu choice
2. Invalid task ID (non-integer)
3. Non-existent task ID
4. Empty title during add
5. Empty title during update

## Implementation Mapping

This contract maps to the following modules:

- **ui.py**: Implements all display, menu, and input functions
- **main.py**: Orchestrates menu loop and operation dispatch
- **storage.py**: Called by operations to manipulate task data
- **task.py**: Task object used in display formatting

## References

- Feature Specification: `specs/001-todo-app/spec.md`
- Data Model: `specs/001-todo-app/data-model.md`
- Research Document: `specs/001-todo-app/research.md`
- Success Criteria: SC-001, SC-002, SC-004, SC-008

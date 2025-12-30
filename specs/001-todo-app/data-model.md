# Data Model: Console Todo Application

**Feature**: Console Todo Application (001-todo-app)
**Date**: 2025-12-30
**Status**: Complete

## Purpose

This document defines the data entities and their relationships for the console todo application. Since this is an in-memory application with a single entity type, the model is intentionally simple.

## Entities

### Task

**Description**: Represents a single todo item that users can create, view, update, complete, and delete.

**Attributes**:

| Attribute    | Type    | Required | Default     | Validation Rules                          | Description                                |
|--------------|---------|----------|-------------|-------------------------------------------|--------------------------------------------|
| `id`         | int     | Yes      | Auto-assign | Must be positive integer ≥ 1              | Unique identifier, auto-incremented        |
| `title`      | str     | Yes      | None        | Non-empty after strip(), max length none  | Short summary of the task                  |
| `description`| str     | No       | ""          | No restrictions, can be empty             | Detailed description of the task           |
| `completed`  | bool    | Yes      | False       | Must be True or False                     | Completion status (True=done, False=todo)  |

**Immutable Fields**:
- `id` - Assigned once during creation, never changes

**Mutable Fields**:
- `title` - Can be updated via update operation (FR-006)
- `description` - Can be updated via update operation (FR-006)
- `completed` - Can be toggled via complete/incomplete operations (FR-004, FR-005)

**Lifecycle**:
1. **Creation**: User provides title and optional description → System assigns next available ID and sets completed=False
2. **Read**: Task can be retrieved by ID for display or operations
3. **Update**: Title and/or description can be modified (ID and completed unchanged via this operation)
4. **Toggle**: Completion status can be toggled between True and False
5. **Deletion**: Task is removed from storage, ID is not reused

**State Transitions**:

```
[Created] --→ completed=False (initial state)
    ↓
[Incomplete] ←--toggle--→ [Complete]
    ↓                          ↓
[Deleted]  ←--------------[Deleted]
```

## Relationships

None - This application has a single entity with no relationships.

## Storage Model

**Structure**: Python list of Task objects

**Access Patterns**:
- **Add**: Append new Task to end of list - O(1)
- **List All**: Iterate entire list - O(n)
- **Find by ID**: Linear search through list - O(n)
- **Update**: Find by ID, modify in-place - O(n) find + O(1) update
- **Delete**: Find by ID, remove from list - O(n) find + O(n) delete
- **Toggle**: Find by ID, flip boolean - O(n) find + O(1) toggle

**Capacity**: Limited only by available system memory (no artificial cap)

**Persistence**: None - all data lost when application exits

## Validation Rules

### Field-Level Validation

**title**:
- ✅ Valid: Any non-empty string after `strip()`
- ✅ Valid: "Buy groceries", "Meeting with client", "a"
- ❌ Invalid: "" (empty string)
- ❌ Invalid: "   " (whitespace only - becomes empty after strip)

**description**:
- ✅ Valid: Any string including empty string
- ✅ Valid: "", "Detailed notes here", "Line 1\nLine 2"
- No restrictions

**id**:
- ✅ Valid: Any positive integer ≥ 1
- ✅ Valid: 1, 2, 3, 100, 9999
- ❌ Invalid: 0, -1, "abc", 1.5 (not an integer)
- Note: Validation applies to user input when referencing tasks, not during assignment

**completed**:
- ✅ Valid: True or False only
- No user input - system manages this field

### Entity-Level Validation

**Task Creation**:
- Title must be non-empty (validated before Task object creation)
- Description defaults to empty string if not provided
- ID assigned automatically by storage layer
- Completed defaults to False

**Task Update**:
- At least one of title or description must be provided
- If title provided, must be non-empty
- If description provided, can be any string (including empty to clear)

**ID References**:
- ID must exist in current task list
- ID must be valid integer format

## Display Format

**List View**:
```
ID  Status    Title                Description
--  ------    -----                -----------
1   [TODO]    Buy groceries        Milk, bread, eggs
2   [DONE]    Call dentist
3   [TODO]    Finish report        Q4 summary for team meeting
```

**Status Indicators**:
- Incomplete: `[TODO]`
- Complete: `[DONE]`

**Empty List**:
```
No tasks found. Add a task to get started!
```

## Edge Cases

### Long Content
- **Long title** (e.g., 1000+ chars): Allowed, no truncation (display may wrap)
- **Long description** (e.g., 10,000+ chars): Allowed, no truncation

### Special Characters
- **Newlines in title/description**: Allowed, may affect display formatting
- **Tabs, quotes, special symbols**: Allowed, displayed as-is

### ID Management
- **Deleted IDs**: Never reused, creates gaps (e.g., 1, 2, 4, 5 after deleting 3)
- **Large ID values**: No upper limit (limited by Python int max)
- **ID exhaustion**: Not a concern (Python int is unbounded)

### Empty States
- **Zero tasks**: Valid state, display empty message
- **All tasks deleted**: Valid state, returns to zero tasks

## Implementation Notes

### Task Class (Python)

```python
class Task:
    """Represents a single todo task."""

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
```

**Design Choices**:
- Simple data class with no methods (data container only)
- Constructor parameters match attribute names for clarity
- Type hints for documentation (not enforced at runtime)
- No validation in constructor (handled by UI/storage layers per research.md)

## References

- Feature Specification: `specs/001-todo-app/spec.md`
- Research Document: `specs/001-todo-app/research.md`
- Functional Requirements: FR-001, FR-002, FR-003, FR-006, FR-008, FR-010

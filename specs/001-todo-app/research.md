# Research: Console Todo Application Architecture

**Feature**: Console Todo Application (001-todo-app)
**Date**: 2025-12-30
**Status**: Complete

## Purpose

This document captures architectural decisions and research findings for implementing the console todo application. All technical unknowns from the planning phase have been resolved.

## Architecture Decisions

### Decision 1: Module Organization

**Decision**: Use 4-module separation of concerns
- `task.py` - Task domain model (class definition)
- `storage.py` - In-memory task storage management
- `ui.py` - Console UI functions (display, input, menus)
- `main.py` - Application entry point and main loop

**Rationale**:
- Clear separation of concerns enables independent development and testing
- Follows single responsibility principle (SRP) from clean code practices
- Each module has < 150 LOC, keeping code readable and maintainable
- Modular structure allows easy extension in future phases

**Alternatives Considered**:
1. **Single-file monolith**: Rejected - violates clean code principle, hard to maintain as feature grows
2. **Deeper module hierarchy (models/, views/, controllers/)**: Rejected - over-engineered for ~500 LOC application, violates simplicity principle

### Decision 2: Task ID Generation Strategy

**Decision**: Auto-increment counter with no reuse after deletion

**Rationale**:
- FR-010 explicitly requires stable IDs (no renumbering after deletion)
- Simple implementation: track `next_id` counter, increment on each add
- Deleted task IDs create gaps in sequence - acceptable per spec
- No collision risk with single-user, single-session constraint

**Alternatives Considered**:
1. **UUID/GUID**: Rejected - overkill for single-session app, harder for users to reference ("task 3" vs "task a7f3...")
2. **Reuse deleted IDs**: Rejected - violates FR-010 stability requirement

### Decision 3: Task Storage Structure

**Decision**: Python list of Task objects with linear search

**Rationale**:
- Simple implementation using built-in list type
- Sufficient performance for 100+ tasks (SC-006 requirement)
- Linear search O(n) acceptable - worst case ~100 iterations
- No external dependencies required

**Alternatives Considered**:
1. **Dictionary with ID as key**: Considered but rejected - list is simpler, iteration order guaranteed, and performance difference negligible at this scale
2. **Sorted list with binary search**: Rejected - premature optimization, violates simplicity principle

### Decision 4: Console UI Pattern

**Decision**: Menu-driven loop with numbered options

**Rationale**:
- User-friendly for beginners (assumption in spec)
- Clear workflow: display menu → get choice → execute → repeat
- Matches common console app patterns (familiar UX)
- Enables 90% first-time user success (SC-008)

**Alternatives Considered**:
1. **Command-line arguments (e.g., `todo add "title"`)**: Rejected - less discoverable for first-time users, requires external docs
2. **REPL with text commands (e.g., "add task")**: Rejected - more complex to implement and use

### Decision 5: Input Validation Strategy

**Decision**: Validate at UI layer before calling storage operations

**Rationale**:
- UI layer best positioned to prompt user for corrections
- Keeps storage layer simple (no error handling complexity)
- Clear error messages displayed immediately (FR-009, SC-004)
- Follows fail-fast principle

**Alternatives Considered**:
1. **Validation in Task class constructor**: Rejected - makes error handling harder, violates single responsibility
2. **Validation in storage layer**: Rejected - storage shouldn't know about UI concerns

### Decision 6: Task Completion Toggle

**Decision**: Single operation toggles status (complete ↔ incomplete)

**Rationale**:
- Spec requires both FR-004 (mark complete) and FR-005 (mark incomplete)
- User input specifies "mark task as complete/incomplete" toggle behavior
- Simpler UX: one menu option instead of two
- Common pattern: if complete → make incomplete, if incomplete → make complete

**Alternatives Considered**:
1. **Separate menu options**: Rejected - adds menu clutter, user must remember current state
2. **Explicit complete/incomplete sub-menu**: Rejected - adds extra step, violates 3-step goal (SC-001)

## Best Practices Applied

### Python Standard Library Patterns

**String Formatting**:
- Use f-strings for readability (Python 3.13 feature)
- Example: `f"Task {task.id}: [{status}] {task.title}"`

**Input Handling**:
- `input()` for all user input
- `strip()` to handle whitespace
- `try/except ValueError` for integer parsing (task IDs)

**List Operations**:
- List comprehension for finding tasks: `[t for t in tasks if t.id == target_id]`
- `enumerate()` for displaying numbered menus

### PEP 8 Compliance

**Naming Conventions**:
- Classes: PascalCase (e.g., `Task`, `TaskStorage`)
- Functions/variables: snake_case (e.g., `add_task`, `task_id`)
- Constants: UPPER_CASE (e.g., `MENU_OPTIONS`)

**Code Organization**:
- Functions: < 20 lines each (constitution requirement)
- Modules: related functions grouped together
- Blank lines: 2 between top-level definitions, 1 between methods

**Documentation**:
- Docstrings for all public functions (one-line summary)
- Inline comments only where logic isn't self-evident

### Error Handling Patterns

**User Input Errors**:
```python
# Pattern: Try-except with clear error message
try:
    task_id = int(input("Enter task ID: "))
except ValueError:
    print("Error: Task ID must be a number.")
    return
```

**Task Not Found**:
```python
# Pattern: Check existence before operation
task = storage.find_task_by_id(task_id)
if task is None:
    print(f"Error: Task {task_id} not found.")
    return
```

**Empty Title Validation**:
```python
# Pattern: Validate before processing
title = input("Enter title: ").strip()
if not title:
    print("Error: Title cannot be empty.")
    return
```

## Implementation Order

Based on dependency analysis:

1. **task.py** - No dependencies, can implement first
2. **storage.py** - Depends on Task class from task.py
3. **ui.py** - Depends on Task class for display formatting
4. **main.py** - Depends on all above modules

## Open Questions

None - all technical decisions resolved.

## References

- Feature Specification: `specs/001-todo-app/spec.md`
- Project Constitution: `.specify/memory/constitution.md`
- PEP 8 Style Guide: https://peps.python.org/pep-0008/

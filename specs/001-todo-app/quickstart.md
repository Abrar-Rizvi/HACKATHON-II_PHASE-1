# Quickstart Guide: Console Todo Application

**Feature**: Console Todo Application (001-todo-app)
**Date**: 2025-12-30
**Audience**: Developers and hackathon reviewers

## Overview

This console application provides a simple todo list manager with in-memory storage. Users can add, view, update, complete, and delete tasks through a menu-driven interface.

**Key Features**:
- Add tasks with title and description
- List all tasks with completion status
- Mark tasks complete/incomplete (toggle)
- Update task details
- Delete tasks
- All data stored in memory (lost on exit)

## Prerequisites

- **Python**: Version 3.13 or higher
- **UV**: Package manager (for dependency management)
- **Platform**: Windows, macOS, or Linux with console/terminal

## Installation

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd console-app
```

### Step 2: Verify Python Version

```bash
python --version
# Should show Python 3.13.x or higher
```

If Python 3.13+ is not installed, download from [python.org](https://www.python.org/).

### Step 3: Install UV (if not already installed)

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:
```bash
uv --version
```

### Step 4: Install Dependencies (if any)

```bash
cd src
uv sync
```

Note: Phase I uses Python standard library only, so no external dependencies are required.

## Running the Application

### Start the Application

```bash
cd src
python main.py
```

You should see the main menu:

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

### Basic Workflow

1. **Add a task**: Choose option 1, enter title and description
2. **View tasks**: Choose option 2 to see all tasks
3. **Mark complete**: Choose option 3, enter task ID to toggle status
4. **Update task**: Choose option 4, enter task ID and new details
5. **Delete task**: Choose option 5, enter task ID to remove
6. **Exit**: Choose option 6 to quit (all data will be lost)

## Usage Examples

### Example 1: Add and View Tasks

```
Enter your choice (1-6): 1

Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
✓ Task added successfully! (ID: 1)

=== Todo Application ===
[menu displays again]

Enter your choice (1-6): 2

=== All Tasks ===

ID: 1  |  Status: [TODO]
Title: Buy groceries
Description: Milk, bread, eggs
---

Total: 1 task(s)
```

### Example 2: Mark Task Complete

```
Enter your choice (1-6): 3

Enter task ID to toggle: 1
✓ Task 1 marked as complete.

[List tasks to verify]

=== All Tasks ===

ID: 1  |  Status: [DONE]
Title: Buy groceries
Description: Milk, bread, eggs
---

Total: 1 task(s)
```

### Example 3: Update Task

```
Enter your choice (1-6): 4

Enter task ID to update: 1

Current title: Buy groceries
Enter new title (or press Enter to keep current): Buy groceries and supplies

Current description: Milk, bread, eggs
Enter new description (or press Enter to keep current): Milk, bread, eggs, butter, cheese

✓ Task 1 updated successfully.
```

### Example 4: Delete Task

```
Enter your choice (1-6): 5

Enter task ID to delete: 1
✓ Task 1 deleted successfully.
```

## Common Operations

### Add Multiple Tasks Quickly

```
1. Add Task → "Write report" → "Q4 summary"
2. Add Task → "Email client" → ""
3. Add Task → "Review code" → "PR #42"
4. List Tasks → See all 3 tasks
```

### Complete a Workflow

```
1. Add task
2. List tasks (see it's [TODO])
3. Mark complete
4. List tasks (see it's [DONE])
5. Delete task
6. List tasks (task is gone)
```

### Partial Update (Keep Title, Change Description)

```
Update Task → ID 2
New title → [Press Enter to keep current]
New description → "Updated details here"
```

## Error Scenarios

### Empty Title

```
Enter task title:
Error: Title cannot be empty. Task not created.
```

### Invalid Task ID

```
Enter task ID to delete: 99
Error: Task 99 not found.
```

### Non-Numeric ID

```
Enter task ID to toggle: abc
Error: Task ID must be a number.
```

### Invalid Menu Choice

```
Enter your choice (1-6): 9
Error: Please enter a number between 1 and 6.
```

## Important Notes

### Data Persistence

⚠️ **WARNING**: All tasks are stored in memory only. When you quit the application (option 6) or close the terminal, **all data is permanently lost**.

This is by design for Phase I. Future phases may add file or database persistence.

### Task ID Behavior

- Task IDs start at 1 and auto-increment
- **IDs are never reused** after deletion
- Example: If you delete task 2, the sequence becomes: 1, 3, 4, 5...
- This ensures ID stability throughout the session

### Input Handling

- **Whitespace**: Leading/trailing spaces are automatically removed from titles
- **Empty input**: Pressing Enter without typing:
  - For title: Error (title is required)
  - For description: Accepted as empty description
  - For update fields: Keeps current value
- **Special characters**: Allowed in titles and descriptions

## Troubleshooting

### "python: command not found"

- **Solution**: Install Python 3.13+ or use `python3` instead of `python`

### "No module named 'xyz'"

- **Solution**: This application uses standard library only. If you see this error, verify you're running the correct Python version (3.13+)

### Menu doesn't accept input

- **Solution**: Make sure you're pressing Enter after typing your choice

### Application crashes with error

- **Solution**: This shouldn't happen with valid input. If it does, please report as a bug with:
  - The menu option you chose
  - The input you provided
  - The full error message

## Project Structure

```
console-app/
├── src/
│   ├── main.py           # Application entry point (run this)
│   ├── task.py           # Task class definition
│   ├── storage.py        # In-memory task storage
│   └── ui.py             # Console UI functions
├── specs/
│   └── 001-todo-app/
│       ├── spec.md       # Feature specification
│       ├── plan.md       # Implementation plan
│       └── ...           # Other design docs
├── pyproject.toml        # UV configuration
└── README.md             # Project overview
```

## Development Workflow

For developers implementing this feature:

1. Read `specs/001-todo-app/spec.md` - Feature requirements
2. Read `specs/001-todo-app/plan.md` - Implementation strategy
3. Read `specs/001-todo-app/data-model.md` - Task entity details
4. Read `specs/001-todo-app/contracts/cli-interface.md` - UI contract
5. Implement in order: task.py → storage.py → ui.py → main.py
6. Test manually against acceptance scenarios in spec.md

## Testing Checklist

Before considering the feature complete, verify:

- [ ] Can add task with title and description
- [ ] Can add task with title only (empty description)
- [ ] Cannot add task with empty title (error shown)
- [ ] Can list all tasks showing ID, status, title, description
- [ ] Empty list shows "No tasks found" message
- [ ] Can mark task complete (status changes to [DONE])
- [ ] Can mark task incomplete (status changes back to [TODO])
- [ ] Marking non-existent task shows error
- [ ] Can update task title only
- [ ] Can update task description only
- [ ] Can update both title and description
- [ ] Cannot update to empty title (error shown)
- [ ] Can delete task by ID
- [ ] Deleted task doesn't appear in list
- [ ] Deleted task ID is not reused for new tasks
- [ ] Deleting non-existent task shows error
- [ ] Invalid menu choice shows error and re-prompts
- [ ] Option 6 quits gracefully with goodbye message
- [ ] All tasks lost after quitting (expected behavior)

## Performance Expectations

- **Response time**: All operations should feel instant for < 100 tasks
- **List display**: Should render within 2 seconds for 100 tasks
- **Memory usage**: Minimal (tasks are small objects)
- **Capacity**: Limited only by available RAM (no artificial cap)

## Support

For questions or issues:
- Check the feature specification: `specs/001-todo-app/spec.md`
- Review the implementation plan: `specs/001-todo-app/plan.md`
- Check the constitution: `.specify/memory/constitution.md`

## Next Steps

After Phase I completion:
- **Phase II**: Add persistent file storage
- **Phase III**: Add search and filtering
- **Phase IV**: Add due dates and priorities
- **Phase V**: Add categories and tags

Current phase focuses on core functionality only.

## License

[Add license information if applicable]

## Changelog

- **2025-12-30**: Initial quickstart guide created for Phase I

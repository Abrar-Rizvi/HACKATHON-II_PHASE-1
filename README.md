# Console Todo Application

A simple command-line todo application with in-memory task management, built for **Hackathon II - Phase I**.

## Features

- **Add Tasks**: Create tasks with a title and optional description
- **List Tasks**: View all tasks with their ID, status, title, and description
- **Toggle Completion**: Mark tasks as complete or incomplete
- **Update Tasks**: Modify task title and/or description
- **Delete Tasks**: Remove tasks by ID (IDs remain stable, never reused)

All task data is stored in memory only - tasks are lost when the application exits.

## Requirements

- Python 3.13+ (tested with Python 3.12.3)
- UV package manager (tested with UV 0.9.18)

## Installation

No external dependencies required. The application uses Python's standard library only.

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd console-app
   ```

## How to Run

From the project directory, run:

```bash
python src/main.py
```

Or using Python 3 explicitly:

```bash
python3 src/main.py
```

## Usage

The application presents a menu-driven interface with 6 options:

```
=== Todo Application ===

1. Add Task
2. List Tasks
3. Mark Task Complete/Incomplete
4. Update Task
5. Delete Task
6. Quit
```

### Example Workflow

1. **Add a task**: Select option 1, enter a title and optional description
2. **View tasks**: Select option 2 to see all tasks with their status ([TODO] or [DONE])
3. **Mark complete**: Select option 3, enter task ID to toggle completion status
4. **Update task**: Select option 4, enter task ID, then update title and/or description
5. **Delete task**: Select option 5, enter task ID to remove the task
6. **Quit**: Select option 6 to exit (all data will be lost)

## Project Structure

```
console-app/
├── src/
│   ├── __init__.py      # Package initialization
│   ├── task.py          # Task domain model
│   ├── storage.py       # In-memory task storage
│   ├── ui.py            # Console UI functions
│   └── main.py          # Application entry point
├── specs/               # Specification documents
└── README.md            # This file
```

## Design Principles

- **Simplicity**: Minimal dependencies, straightforward implementation
- **Clean Code**: PEP 8 compliant, well-documented with docstrings
- **In-Memory Only**: No persistence - simple and deterministic
- **Modular Architecture**: Separation of concerns across 4 modules

## Limitations

- No data persistence (all tasks lost on exit)
- No user authentication or multi-user support
- No task categories, tags, or due dates
- No search or filter functionality

## Development

For development guidelines and architecture decisions, see:
- `.specify/memory/constitution.md` - Project governance and standards
- `specs/001-todo-app/spec.md` - Feature specification
- `specs/001-todo-app/plan.md` - Implementation plan
- `specs/001-todo-app/tasks.md` - Task breakdown

## License

This is a Hackathon II Phase I project for educational purposes.

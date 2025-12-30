"""Console UI functions for todo application."""


def display_menu():
    """Display the main menu with 6 options."""
    print("\n=== Todo Application ===\n")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task Complete/Incomplete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Quit")
    print()


def get_menu_choice():
    """Get menu choice from user (1-6), handle errors.

    Returns:
        Integer between 1-6, or None if invalid input
    """
    try:
        choice = int(input("Enter your choice (1-6): "))
        if 1 <= choice <= 6:
            return choice
        else:
            display_error("Please enter a number between 1 and 6.")
            return None
    except ValueError:
        display_error("Please enter a number between 1 and 6.")
        return None


def get_task_input():
    """Prompt for task title and description, validate title is non-empty.

    Returns:
        Tuple of (title, description) if valid, or (None, None) if invalid
    """
    title = input("Enter task title: ").strip()
    if not title:
        display_error("Title cannot be empty. Task not created.")
        return None, None

    description = input("Enter task description (optional): ").strip()
    return title, description


def display_tasks(tasks):
    """Format and print all tasks with ID, status, title, description.

    Args:
        tasks: List of Task objects
    """
    print("\n=== All Tasks ===\n")

    if not tasks:
        print("No tasks found. Add a task to get started!")
        return

    for task in tasks:
        status = "[DONE]" if task.completed else "[TODO]"
        print(f"ID: {task.id}  |  Status: {status}")
        print(f"Title: {task.title}")
        print(f"Description: {task.description}")
        print("---\n")

    print(f"Total: {len(tasks)} task(s)")


def display_success(message):
    """Show success message with checkmark.

    Args:
        message: Success message to display
    """
    print(f"✓ {message}")


def display_error(message):
    """Show error message.

    Args:
        message: Error message to display
    """
    print(f"Error: {message}")


def get_task_id_input(prompt="Enter task ID: "):
    """Prompt for task ID and validate integer format.

    Args:
        prompt: Custom prompt message (default: "Enter task ID: ")

    Returns:
        Integer task ID if valid, None if invalid
    """
    try:
        task_id = int(input(prompt))
        return task_id
    except ValueError:
        display_error("Task ID must be a number.")
        return None


def get_task_update_input(task):
    """Get updated title and/or description for a task.

    Args:
        task: Task object with current values

    Returns:
        Tuple of (new_title, new_description) where None means keep current value
        Returns (None, None) if title validation fails
    """
    print(f"\nCurrent title: {task.title}")
    new_title = input("Enter new title (or press Enter to keep current): ").strip()

    print(f"Current description: {task.description}")
    new_description = input("Enter new description (or press Enter to keep current): ").strip()

    # If user provided empty title explicitly, that's an error
    if new_title == "":
        # User pressed Enter - keep current
        new_title = None
    else:
        # User provided something - validate it's not whitespace only
        if not new_title:
            display_error("Title cannot be empty. Task not updated.")
            return None, None

    # Empty description is valid (to clear it), but Enter means keep current
    if new_description == "":
        new_description = None

    return new_title, new_description

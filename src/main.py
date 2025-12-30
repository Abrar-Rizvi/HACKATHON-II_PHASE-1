"""Main application entry point and orchestration."""

import ui
from storage import TaskStorage


def add_task_flow(storage):
    """Handle the add task workflow.

    Args:
        storage: TaskStorage instance
    """
    title, description = ui.get_task_input()
    if title is not None:
        task = storage.add_task(title, description)
        ui.display_success(f"Task added successfully! (ID: {task.id})")


def list_tasks_flow(storage):
    """Handle the list tasks workflow.

    Args:
        storage: TaskStorage instance
    """
    tasks = storage.get_all_tasks()
    ui.display_tasks(tasks)


def toggle_task_flow(storage):
    """Handle the toggle task completion workflow.

    Args:
        storage: TaskStorage instance
    """
    task_id = ui.get_task_id_input("Enter task ID to toggle: ")
    if task_id is None:
        return

    task = storage.find_task_by_id(task_id)
    if task is None:
        ui.display_error(f"Task {task_id} not found.")
        return

    storage.toggle_completion(task_id)
    status = "complete" if task.completed else "incomplete"
    ui.display_success(f"Task {task_id} marked as {status}.")


def update_task_flow(storage):
    """Handle the update task workflow.

    Args:
        storage: TaskStorage instance
    """
    task_id = ui.get_task_id_input("Enter task ID to update: ")
    if task_id is None:
        return

    task = storage.find_task_by_id(task_id)
    if task is None:
        ui.display_error(f"Task {task_id} not found.")
        return

    new_title, new_description = ui.get_task_update_input(task)
    if new_title is None and new_description is None:
        # Check if this is an error case (both None from validation failure)
        # vs. user just pressed Enter for both (keeping current values)
        return

    storage.update_task(task_id, new_title, new_description)
    ui.display_success(f"Task {task_id} updated successfully.")


def delete_task_flow(storage):
    """Handle the delete task workflow.

    Args:
        storage: TaskStorage instance
    """
    task_id = ui.get_task_id_input("Enter task ID to delete: ")
    if task_id is None:
        return

    task = storage.find_task_by_id(task_id)
    if task is None:
        ui.display_error(f"Task {task_id} not found.")
        return

    storage.delete_task(task_id)
    ui.display_success(f"Task {task_id} deleted successfully.")


def main_loop(storage):
    """Main application loop: display menu, get choice, dispatch to flows.

    Args:
        storage: TaskStorage instance
    """
    while True:
        ui.display_menu()
        choice = ui.get_menu_choice()

        if choice is None:
            continue

        if choice == 1:
            add_task_flow(storage)
        elif choice == 2:
            list_tasks_flow(storage)
        elif choice == 3:
            toggle_task_flow(storage)
        elif choice == 4:
            update_task_flow(storage)
        elif choice == 5:
            delete_task_flow(storage)
        elif choice == 6:
            print("Goodbye! All tasks will be lost (in-memory only).")
            break


def main():
    """Application entry point."""
    storage = TaskStorage()
    main_loop(storage)


if __name__ == "__main__":
    main()

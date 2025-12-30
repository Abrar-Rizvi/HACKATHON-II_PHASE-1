"""In-memory task storage manager."""

from task import Task


class TaskStorage:
    """Manages in-memory storage of tasks with auto-incrementing IDs."""

    def __init__(self):
        """Initialize empty task storage."""
        self.tasks = []
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task with auto-assigned ID.

        Args:
            title: Task title (required, non-empty)
            description: Task description (optional)

        Returns:
            The newly created Task object
        """
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def find_task_by_id(self, task_id: int):
        """Find a task by its ID using linear search.

        Args:
            task_id: The ID to search for

        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self):
        """Get all tasks.

        Returns:
            List of all Task objects (returns reference to internal list)
        """
        return self.tasks

    def toggle_completion(self, task_id: int) -> bool:
        """Toggle task completion status.

        Args:
            task_id: ID of task to toggle

        Returns:
            True if task was toggled, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False
        task.completed = not task.completed
        return True

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """Update task title and/or description.

        Args:
            task_id: ID of task to update
            title: New title (None to keep current)
            description: New description (None to keep current)

        Returns:
            True if task was updated, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return True

    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID.

        Args:
            task_id: ID of task to delete

        Returns:
            True if task was deleted, False if task not found
        """
        task = self.find_task_by_id(task_id)
        if task is None:
            return False

        self.tasks.remove(task)
        return True

"""Task domain model for console todo application."""


class Task:
    """Represents a single todo task."""

    def __init__(self, task_id: int, title: str, description: str = "", completed: bool = False):
        """Initialize a new Task.

        Args:
            task_id: Unique integer identifier (auto-assigned by storage)
            title: Short summary of the task (required, non-empty)
            description: Detailed description (optional, defaults to empty string)
            completed: Completion status (defaults to False/incomplete)
        """
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed

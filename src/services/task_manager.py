"""TaskManager service for managing todo tasks."""

from typing import Optional
from src.models.task import Task


class TaskManager:
    """
    Manages a collection of tasks with CRUD operations.
    
    Uses a dictionary for O(1) lookup by task ID. Task IDs are monotonically
    increasing and never reused to prevent confusion.
    """
    
    def __init__(self):
        """Initialize an empty TaskManager."""
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        """
        Add a new task to the manager.
        
        Args:
            title: Task title (required, cannot be empty)
            description: Task description (optional)
        
        Returns:
            The newly created Task with auto-generated ID
        
        Raises:
            ValueError: If title is empty or contains only whitespace
        """
        # Create task (validation happens in Task.__post_init__)
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            is_complete=False
        )
        
        # Store task and increment ID counter
        self._tasks[task.id] = task
        self._next_id += 1
        
        return task
    
    def get_all_tasks(self) -> list[Task]:
        """
        Get all tasks in the manager.
        
        Returns:
            List of all tasks (empty list if no tasks exist)
        """
        return list(self._tasks.values())
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID.
        
        Args:
            task_id: The ID of the task to retrieve
        
        Returns:
            The Task if found, None otherwise
        """
        return self._tasks.get(task_id)
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.
        
        Args:
            task_id: The ID of the task to delete
        
        Returns:
            True if task was deleted, False if task not found
        """
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False
    
    def toggle_completion(self, task_id: int) -> bool:
        """
        Toggle the completion status of a task.
        
        Args:
            task_id: The ID of the task to toggle
        
        Returns:
            True if task was toggled, False if task not found
        """
        task = self._tasks.get(task_id)
        if task is None:
            return False
        
        # Create new task with toggled status (dataclasses are immutable-ish)
        updated_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            is_complete=not task.is_complete
        )
        self._tasks[task_id] = updated_task
        
        return True
    
    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> bool:
        """
        Update a task's title and/or description.
        
        Args:
            task_id: The ID of the task to update
            title: New title (optional, None means keep current)
            description: New description (optional, None means keep current)
        
        Returns:
            True if task was updated, False if task not found
        
        Raises:
            ValueError: If provided title is empty or whitespace only
        """
        task = self._tasks.get(task_id)
        if task is None:
            return False
        
        # Determine new values (keep old if not provided)
        new_title = title if title is not None else task.title
        new_description = description if description is not None else task.description
        
        # Create updated task (validation happens in Task.__post_init__)
        updated_task = Task(
            id=task.id,
            title=new_title,
            description=new_description,
            is_complete=task.is_complete
        )
        self._tasks[task_id] = updated_task
        
        return True

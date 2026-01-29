"""Command handlers for CLI operations."""

from src.services.task_manager import TaskManager
from src.cli.interface import (
    display_tasks,
    display_success,
    display_error,
    display_header,
    get_user_input,
    get_integer_input,
)


def handle_view_tasks(manager: TaskManager) -> None:
    """
    Handle the view all tasks command.
    
    Args:
        manager: TaskManager instance
    """
    tasks = manager.get_all_tasks()
    display_tasks(tasks)


def handle_add_task(manager: TaskManager) -> None:
    """
    Handle the add task command.
    
    Args:
        manager: TaskManager instance
    """
    display_header("Add Task")
    
    title = get_user_input("Title: ")
    description = get_user_input("Description (optional): ")
    
    try:
        task = manager.add_task(title=title, description=description)
        display_success(f"Task #{task.id} added successfully!")
    except ValueError as e:
        display_error(str(e))


def handle_update_task(manager: TaskManager) -> None:
    """
    Handle the update task command.
    
    Args:
        manager: TaskManager instance
    """
    display_header("Update Task")
    
    task_id = get_integer_input("Task ID: ")
    
    if task_id is None:
        display_error("Invalid task ID. Please enter a number.")
        return
    
    # Check if task exists
    task = manager.get_task_by_id(task_id)
    if task is None:
        display_error(
            f"Task #{task_id} not found. Use option 1 to view existing tasks."
        )
        return
    
    # Show current values
    print(f"\nCurrent title: {task.title}")
    print(f"Current description: {task.description}")
    print("\nLeave blank to keep current value.")
    
    new_title = get_user_input("New title: ")
    new_description = get_user_input("New description: ")
    
    # Only update if user provided new values
    title_to_update = new_title if new_title.strip() else None
    description_to_update = new_description if new_description else None
    
    # If both are None, nothing to update
    if title_to_update is None and description_to_update is None:
        display_error("No changes provided. Task not updated.")
        return
    
    try:
        success = manager.update_task(
            task_id,
            title=title_to_update,
            description=description_to_update
        )
        if success:
            display_success(f"Task #{task_id} updated successfully!")
        else:
            display_error(f"Task #{task_id} not found.")
    except ValueError as e:
        display_error(str(e))


def handle_delete_task(manager: TaskManager) -> None:
    """
    Handle the delete task command.
    
    Args:
        manager: TaskManager instance
    """
    display_header("Delete Task")
    
    task_id = get_integer_input("Task ID: ")
    
    if task_id is None:
        display_error("Invalid task ID. Please enter a number.")
        return
    
    success = manager.delete_task(task_id)
    
    if success:
        display_success(f"Task #{task_id} deleted successfully!")
    else:
        display_error(
            f"Task #{task_id} not found. Use option 1 to view existing tasks."
        )


def handle_toggle_completion(manager: TaskManager) -> None:
    """
    Handle the toggle task completion command.
    
    Args:
        manager: TaskManager instance
    """
    display_header("Toggle Task Completion")
    
    task_id = get_integer_input("Task ID: ")
    
    if task_id is None:
        display_error("Invalid task ID. Please enter a number.")
        return
    
    success = manager.toggle_completion(task_id)
    
    if success:
        task = manager.get_task_by_id(task_id)
        status = "complete" if task.is_complete else "incomplete"
        display_success(f"Task #{task_id} marked as {status}!")
    else:
        display_error(
            f"Task #{task_id} not found. Use option 1 to view existing tasks."
        )

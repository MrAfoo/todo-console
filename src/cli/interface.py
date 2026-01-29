"""CLI display and user interaction functions."""

from typing import Optional
from src.models.task import Task


def display_menu() -> None:
    """Display the main menu options."""
    print("\n=== Todo Application ===\n")
    print("1. View all tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Toggle task completion")
    print("6. Exit")
    print()


def display_tasks(tasks: list[Task]) -> None:
    """
    Display all tasks in a formatted list.
    
    Args:
        tasks: List of tasks to display
    """
    print("\n--- All Tasks ---")
    
    if not tasks:
        print("No tasks found. Add a task to get started!")
    else:
        for task in tasks:
            print(f"\n{task}")
    
    print()


def display_success(message: str) -> None:
    """
    Display a success message.
    
    Args:
        message: Success message to display
    """
    print(f"\n✓ {message}\n")


def display_error(message: str) -> None:
    """
    Display an error message.
    
    Args:
        message: Error message to display
    """
    print(f"\n✗ Error: {message}\n")


def get_user_input(prompt: str) -> str:
    """
    Get user input with a prompt.
    
    Args:
        prompt: Prompt to display to the user
    
    Returns:
        User input as a string
    """
    return input(prompt)


def get_integer_input(prompt: str) -> Optional[int]:
    """
    Get integer input from the user.
    
    Args:
        prompt: Prompt to display to the user
    
    Returns:
        Integer value or None if invalid
    """
    try:
        value = input(prompt)
        return int(value)
    except ValueError:
        return None


def display_header(title: str) -> None:
    """
    Display a section header.
    
    Args:
        title: Header title to display
    """
    print(f"\n--- {title} ---")

"""CLI interface components."""

from src.cli.interface import display_menu, display_tasks
from src.cli.commands import (
    handle_add_task,
    handle_view_tasks,
    handle_update_task,
    handle_delete_task,
    handle_toggle_completion,
)

__all__ = [
    "display_menu",
    "display_tasks",
    "handle_add_task",
    "handle_view_tasks",
    "handle_update_task",
    "handle_delete_task",
    "handle_toggle_completion",
]

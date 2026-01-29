"""Main entry point for the CLI Todo Application."""

import sys
from pathlib import Path

# Add parent directory to path to support both direct execution and module execution
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.services.task_manager import TaskManager
from src.cli.interface import display_menu, get_user_input, display_error
from src.cli.commands import (
    handle_view_tasks,
    handle_add_task,
    handle_update_task,
    handle_delete_task,
    handle_toggle_completion,
)


def main() -> None:
    """Run the main application loop."""
    manager = TaskManager()
    
    print("Welcome to the CLI Todo Application!")
    print("All tasks are stored in memory only.")
    
    while True:
        try:
            display_menu()
            choice = get_user_input("Choose an option (1-6): ")
            
            if choice == "1":
                handle_view_tasks(manager)
            elif choice == "2":
                handle_add_task(manager)
            elif choice == "3":
                handle_update_task(manager)
            elif choice == "4":
                handle_delete_task(manager)
            elif choice == "5":
                handle_toggle_completion(manager)
            elif choice == "6":
                print("\nGoodbye! All tasks have been cleared from memory.\n")
                sys.exit(0)
            else:
                display_error(
                    "Invalid option. Please choose a number between 1 and 6."
                )
        
        except KeyboardInterrupt:
            print("\n\nGoodbye! All tasks have been cleared from memory.\n")
            sys.exit(0)
        except Exception as e:
            display_error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

"""Unit tests for CLI interface display functions."""

import pytest
from io import StringIO
from unittest.mock import patch
from src.models.task import Task
from src.cli.interface import (
    display_menu,
    display_tasks,
    display_success,
    display_error,
    get_user_input,
    get_integer_input,
    display_header,
)


class TestDisplayFunctions:
    """Tests for display functions."""

    def test_display_menu_shows_all_options(self, capsys):
        """Test that display_menu shows all menu options."""
        # Act
        display_menu()
        captured = capsys.readouterr()
        
        # Assert
        assert "Todo Application" in captured.out
        assert "1. View all tasks" in captured.out
        assert "2. Add task" in captured.out
        assert "3. Update task" in captured.out
        assert "4. Delete task" in captured.out
        assert "5. Toggle task completion" in captured.out
        assert "6. Exit" in captured.out

    def test_display_tasks_empty_list(self, capsys):
        """Test displaying an empty task list."""
        # Act
        display_tasks([])
        captured = capsys.readouterr()
        
        # Assert
        assert "All Tasks" in captured.out
        assert "No tasks found" in captured.out

    def test_display_tasks_with_tasks(self, capsys):
        """Test displaying tasks."""
        # Arrange
        tasks = [
            Task(id=1, title="Task 1", description="Description 1"),
            Task(id=2, title="Task 2", description="Description 2", is_complete=True),
        ]
        
        # Act
        display_tasks(tasks)
        captured = capsys.readouterr()
        
        # Assert
        assert "All Tasks" in captured.out
        assert "Task 1" in captured.out
        assert "Task 2" in captured.out

    def test_display_success_message(self, capsys):
        """Test displaying success message."""
        # Act
        display_success("Task added successfully!")
        captured = capsys.readouterr()
        
        # Assert
        assert "✓" in captured.out or "success" in captured.out.lower()
        assert "Task added successfully!" in captured.out

    def test_display_error_message(self, capsys):
        """Test displaying error message."""
        # Act
        display_error("Task not found")
        captured = capsys.readouterr()
        
        # Assert
        assert "Error" in captured.out
        assert "Task not found" in captured.out

    def test_display_header(self, capsys):
        """Test displaying section header."""
        # Act
        display_header("Add Task")
        captured = capsys.readouterr()
        
        # Assert
        assert "Add Task" in captured.out


class TestInputFunctions:
    """Tests for input functions."""

    @patch("builtins.input", return_value="test input")
    def test_get_user_input(self, mock_input):
        """Test getting user input."""
        # Act
        result = get_user_input("Enter value: ")
        
        # Assert
        assert result == "test input"
        mock_input.assert_called_once_with("Enter value: ")

    @patch("builtins.input", return_value="42")
    def test_get_integer_input_valid(self, mock_input):
        """Test getting valid integer input."""
        # Act
        result = get_integer_input("Enter number: ")
        
        # Assert
        assert result == 42

    @patch("builtins.input", return_value="not a number")
    def test_get_integer_input_invalid(self, mock_input):
        """Test getting invalid integer input returns None."""
        # Act
        result = get_integer_input("Enter number: ")
        
        # Assert
        assert result is None

    @patch("builtins.input", return_value="")
    def test_get_integer_input_empty(self, mock_input):
        """Test getting empty integer input returns None."""
        # Act
        result = get_integer_input("Enter number: ")
        
        # Assert
        assert result is None

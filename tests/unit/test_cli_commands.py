"""Unit tests for CLI command handlers."""

import pytest
from unittest.mock import Mock, patch, call
from src.services.task_manager import TaskManager
from src.cli.commands import (
    handle_view_tasks,
    handle_add_task,
    handle_update_task,
    handle_delete_task,
    handle_toggle_completion,
)


class TestHandleViewTasks:
    """Tests for handle_view_tasks command."""

    @patch("src.cli.commands.display_tasks")
    def test_view_tasks_with_empty_list(self, mock_display):
        """Test viewing tasks when no tasks exist."""
        # Arrange
        manager = TaskManager()
        
        # Act
        handle_view_tasks(manager)
        
        # Assert
        mock_display.assert_called_once()
        args = mock_display.call_args[0]
        assert args[0] == []

    @patch("src.cli.commands.display_tasks")
    def test_view_tasks_with_multiple_tasks(self, mock_display):
        """Test viewing tasks when multiple tasks exist."""
        # Arrange
        manager = TaskManager()
        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")
        
        # Act
        handle_view_tasks(manager)
        
        # Assert
        mock_display.assert_called_once()
        args = mock_display.call_args[0]
        assert len(args[0]) == 2
        assert task1 in args[0]
        assert task2 in args[0]


class TestHandleAddTask:
    """Tests for handle_add_task command."""

    @patch("src.cli.commands.get_user_input")
    @patch("src.cli.commands.display_success")
    @patch("src.cli.commands.display_header")
    def test_add_task_with_title_and_description(
        self, mock_header, mock_success, mock_input
    ):
        """Test adding a task with both title and description."""
        # Arrange
        manager = TaskManager()
        mock_input.side_effect = ["Buy groceries", "Milk, eggs, bread"]
        
        # Act
        handle_add_task(manager)
        
        # Assert
        tasks = manager.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Buy groceries"
        assert tasks[0].description == "Milk, eggs, bread"
        mock_success.assert_called_once()

    @patch("src.cli.commands.get_user_input")
    @patch("src.cli.commands.display_success")
    @patch("src.cli.commands.display_header")
    def test_add_task_with_title_only(
        self, mock_header, mock_success, mock_input
    ):
        """Test adding a task with only a title."""
        # Arrange
        manager = TaskManager()
        mock_input.side_effect = ["Buy groceries", ""]
        
        # Act
        handle_add_task(manager)
        
        # Assert
        tasks = manager.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Buy groceries"
        assert tasks[0].description == ""

    @patch("src.cli.commands.get_user_input")
    @patch("src.cli.commands.display_error")
    @patch("src.cli.commands.display_header")
    def test_add_task_with_empty_title_shows_error(
        self, mock_header, mock_error, mock_input
    ):
        """Test that adding task with empty title shows error."""
        # Arrange
        manager = TaskManager()
        mock_input.side_effect = ["", "Description"]
        
        # Act
        handle_add_task(manager)
        
        # Assert
        tasks = manager.get_all_tasks()
        assert len(tasks) == 0
        mock_error.assert_called_once()


class TestHandleUpdateTask:
    """Tests for handle_update_task command."""

    @patch("src.cli.commands.get_user_input")
    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_success")
    @patch("src.cli.commands.display_header")
    def test_update_task_title_only(
        self, mock_header, mock_success, mock_int_input, mock_input
    ):
        """Test updating only the title of a task."""
        # Arrange
        manager = TaskManager()
        manager.add_task("Old Title", "Description")
        mock_int_input.return_value = 1
        mock_input.side_effect = ["New Title", ""]
        
        # Act
        handle_update_task(manager)
        
        # Assert
        task = manager.get_task_by_id(1)
        assert task.title == "New Title"
        assert task.description == "Description"
        mock_success.assert_called_once()

    @patch("src.cli.commands.get_user_input")
    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_success")
    @patch("src.cli.commands.display_header")
    def test_update_task_description_only(
        self, mock_header, mock_success, mock_int_input, mock_input
    ):
        """Test updating only the description of a task."""
        # Arrange
        manager = TaskManager()
        manager.add_task("Title", "Old Description")
        mock_int_input.return_value = 1
        mock_input.side_effect = ["", "New Description"]
        
        # Act
        handle_update_task(manager)
        
        # Assert
        task = manager.get_task_by_id(1)
        assert task.title == "Title"
        assert task.description == "New Description"

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_error")
    @patch("src.cli.commands.display_header")
    def test_update_nonexistent_task_shows_error(
        self, mock_header, mock_error, mock_int_input
    ):
        """Test that updating non-existent task shows error."""
        # Arrange
        manager = TaskManager()
        manager.add_task("Task 1")
        mock_int_input.return_value = 999
        
        # Act
        handle_update_task(manager)
        
        # Assert
        mock_error.assert_called_once()
        assert "not found" in mock_error.call_args[0][0].lower()

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_error")
    @patch("src.cli.commands.display_header")
    def test_update_with_invalid_id_shows_error(
        self, mock_header, mock_error, mock_int_input
    ):
        """Test that invalid task ID shows error."""
        # Arrange
        manager = TaskManager()
        mock_int_input.return_value = None
        
        # Act
        handle_update_task(manager)
        
        # Assert
        mock_error.assert_called_once()
        assert "invalid" in mock_error.call_args[0][0].lower()


class TestHandleDeleteTask:
    """Tests for handle_delete_task command."""

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_success")
    @patch("src.cli.commands.display_header")
    def test_delete_existing_task(
        self, mock_header, mock_success, mock_int_input
    ):
        """Test deleting an existing task."""
        # Arrange
        manager = TaskManager()
        manager.add_task("Task 1")
        mock_int_input.return_value = 1
        
        # Act
        handle_delete_task(manager)
        
        # Assert
        tasks = manager.get_all_tasks()
        assert len(tasks) == 0
        mock_success.assert_called_once()

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_error")
    @patch("src.cli.commands.display_header")
    def test_delete_nonexistent_task_shows_error(
        self, mock_header, mock_error, mock_int_input
    ):
        """Test that deleting non-existent task shows error."""
        # Arrange
        manager = TaskManager()
        manager.add_task("Task 1")
        mock_int_input.return_value = 999
        
        # Act
        handle_delete_task(manager)
        
        # Assert
        tasks = manager.get_all_tasks()
        assert len(tasks) == 1
        mock_error.assert_called_once()
        assert "not found" in mock_error.call_args[0][0].lower()

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_error")
    @patch("src.cli.commands.display_header")
    def test_delete_with_invalid_id_shows_error(
        self, mock_header, mock_error, mock_int_input
    ):
        """Test that invalid task ID shows error."""
        # Arrange
        manager = TaskManager()
        mock_int_input.return_value = None
        
        # Act
        handle_delete_task(manager)
        
        # Assert
        mock_error.assert_called_once()
        assert "invalid" in mock_error.call_args[0][0].lower()


class TestHandleToggleCompletion:
    """Tests for handle_toggle_completion command."""

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_success")
    @patch("src.cli.commands.display_header")
    def test_toggle_incomplete_to_complete(
        self, mock_header, mock_success, mock_int_input
    ):
        """Test marking an incomplete task as complete."""
        # Arrange
        manager = TaskManager()
        manager.add_task("Task 1")
        mock_int_input.return_value = 1
        
        # Act
        handle_toggle_completion(manager)
        
        # Assert
        task = manager.get_task_by_id(1)
        assert task.is_complete is True
        mock_success.assert_called_once()
        assert "complete" in mock_success.call_args[0][0].lower()

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_success")
    @patch("src.cli.commands.display_header")
    def test_toggle_complete_to_incomplete(
        self, mock_header, mock_success, mock_int_input
    ):
        """Test marking a complete task as incomplete."""
        # Arrange
        manager = TaskManager()
        manager.add_task("Task 1")
        manager.toggle_completion(1)
        mock_int_input.return_value = 1
        
        # Act
        handle_toggle_completion(manager)
        
        # Assert
        task = manager.get_task_by_id(1)
        assert task.is_complete is False
        mock_success.assert_called_once()
        assert "incomplete" in mock_success.call_args[0][0].lower()

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_error")
    @patch("src.cli.commands.display_header")
    def test_toggle_nonexistent_task_shows_error(
        self, mock_header, mock_error, mock_int_input
    ):
        """Test that toggling non-existent task shows error."""
        # Arrange
        manager = TaskManager()
        mock_int_input.return_value = 999
        
        # Act
        handle_toggle_completion(manager)
        
        # Assert
        mock_error.assert_called_once()
        assert "not found" in mock_error.call_args[0][0].lower()

    @patch("src.cli.commands.get_integer_input")
    @patch("src.cli.commands.display_error")
    @patch("src.cli.commands.display_header")
    def test_toggle_with_invalid_id_shows_error(
        self, mock_header, mock_error, mock_int_input
    ):
        """Test that invalid task ID shows error."""
        # Arrange
        manager = TaskManager()
        mock_int_input.return_value = None
        
        # Act
        handle_toggle_completion(manager)
        
        # Assert
        mock_error.assert_called_once()
        assert "invalid" in mock_error.call_args[0][0].lower()

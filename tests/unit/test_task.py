"""Unit tests for Task entity."""

import pytest
from src.models.task import Task


class TestTaskCreation:
    """Tests for Task creation and initialization."""

    def test_create_task_with_all_fields(self):
        """Test creating a task with all fields provided."""
        # Arrange & Act
        task = Task(
            id=1,
            title="Buy groceries",
            description="Milk, eggs, bread",
            is_complete=False
        )
        
        # Assert
        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == "Milk, eggs, bread"
        assert task.is_complete is False

    def test_create_task_with_minimal_fields(self):
        """Test creating a task with only required fields (id and title)."""
        # Arrange & Act
        task = Task(id=1, title="Buy groceries")
        
        # Assert
        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert task.is_complete is False

    def test_create_task_with_empty_description(self):
        """Test creating a task with explicitly empty description."""
        # Arrange & Act
        task = Task(id=1, title="Buy groceries", description="")
        
        # Assert
        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert task.is_complete is False

    def test_create_completed_task(self):
        """Test creating a task that is already complete."""
        # Arrange & Act
        task = Task(id=1, title="Buy groceries", is_complete=True)
        
        # Assert
        assert task.id == 1
        assert task.is_complete is True


class TestTaskValidation:
    """Tests for Task validation rules."""

    def test_create_task_with_empty_title_raises_error(self):
        """Test that creating a task with empty title raises ValueError."""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Task(id=1, title="")

    def test_create_task_with_whitespace_only_title_raises_error(self):
        """Test that creating a task with whitespace-only title raises ValueError."""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Task(id=1, title="   ")

    def test_create_task_with_negative_id_raises_error(self):
        """Test that creating a task with negative ID raises ValueError."""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            Task(id=-1, title="Buy groceries")

    def test_create_task_with_zero_id_raises_error(self):
        """Test that creating a task with zero ID raises ValueError."""
        # Arrange & Act & Assert
        with pytest.raises(ValueError, match="ID must be a positive integer"):
            Task(id=0, title="Buy groceries")


class TestTaskEdgeCases:
    """Tests for Task edge cases and special characters."""

    def test_task_with_very_long_title(self):
        """Test creating a task with a very long title (200 chars)."""
        # Arrange
        long_title = "A" * 200
        
        # Act
        task = Task(id=1, title=long_title)
        
        # Assert
        assert task.title == long_title
        assert len(task.title) == 200

    def test_task_with_very_long_description(self):
        """Test creating a task with a very long description (1000 chars)."""
        # Arrange
        long_description = "B" * 1000
        
        # Act
        task = Task(id=1, title="Title", description=long_description)
        
        # Assert
        assert task.description == long_description
        assert len(task.description) == 1000

    def test_task_with_special_characters_in_title(self):
        """Test creating a task with special characters in title."""
        # Arrange & Act
        task = Task(id=1, title='Buy "groceries" & supplies!')
        
        # Assert
        assert task.title == 'Buy "groceries" & supplies!'

    def test_task_with_unicode_characters(self):
        """Test creating a task with Unicode characters."""
        # Arrange & Act
        task = Task(id=1, title="Acheter du café ☕", description="Café français 🇫🇷")
        
        # Assert
        assert task.title == "Acheter du café ☕"
        assert task.description == "Café français 🇫🇷"

    def test_task_with_newlines_in_description(self):
        """Test creating a task with newlines in description."""
        # Arrange & Act
        task = Task(
            id=1,
            title="Multi-line task",
            description="Line 1\nLine 2\nLine 3"
        )
        
        # Assert
        assert task.description == "Line 1\nLine 2\nLine 3"
        assert task.description.count("\n") == 2


class TestTaskEquality:
    """Tests for Task equality and comparison."""

    def test_tasks_with_same_id_are_equal(self):
        """Test that tasks with the same ID are considered equal."""
        # Arrange
        task1 = Task(id=1, title="Task 1")
        task2 = Task(id=1, title="Task 1")
        
        # Act & Assert
        assert task1 == task2

    def test_tasks_with_different_ids_are_not_equal(self):
        """Test that tasks with different IDs are not equal."""
        # Arrange
        task1 = Task(id=1, title="Task 1")
        task2 = Task(id=2, title="Task 1")
        
        # Act & Assert
        assert task1 != task2

    def test_tasks_with_same_id_different_content_are_equal(self):
        """Test that tasks are equal based on ID, not content."""
        # Arrange
        task1 = Task(id=1, title="Task 1", description="Description 1")
        task2 = Task(id=1, title="Task 2", description="Description 2")
        
        # Act & Assert
        assert task1 == task2


class TestTaskRepresentation:
    """Tests for Task string representation."""

    def test_task_str_representation(self):
        """Test the string representation of a task."""
        # Arrange
        task = Task(id=1, title="Buy groceries", description="Milk, eggs")
        
        # Act
        result = str(task)
        
        # Assert
        assert "1" in result
        assert "Buy groceries" in result
        assert "incomplete" in result.lower() or "[ ]" in result

    def test_completed_task_str_representation(self):
        """Test the string representation of a completed task."""
        # Arrange
        task = Task(id=1, title="Buy groceries", is_complete=True)
        
        # Act
        result = str(task)
        
        # Assert
        assert "1" in result
        assert "Buy groceries" in result
        assert "complete" in result.lower() or "[✓]" in result or "[x]" in result.lower()

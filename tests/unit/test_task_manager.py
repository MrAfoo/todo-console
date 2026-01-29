"""Unit tests for TaskManager service."""

import pytest
from src.models.task import Task
from src.services.task_manager import TaskManager


class TestTaskManagerInitialization:
    """Tests for TaskManager initialization."""

    def test_create_task_manager(self):
        """Test creating a new TaskManager instance."""
        # Arrange & Act
        manager = TaskManager()
        
        # Assert
        assert manager is not None
        assert manager.get_all_tasks() == []

    def test_task_manager_starts_with_empty_task_list(self):
        """Test that a new TaskManager has no tasks."""
        # Arrange & Act
        manager = TaskManager()
        tasks = manager.get_all_tasks()
        
        # Assert
        assert len(tasks) == 0
        assert tasks == []


class TestAddTask:
    """Tests for adding tasks."""

    def test_add_task_with_title_only(self):
        """Test adding a task with only a title."""
        # Arrange
        manager = TaskManager()
        
        # Act
        task = manager.add_task(title="Buy groceries")
        
        # Assert
        assert task is not None
        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == ""
        assert task.is_complete is False

    def test_add_task_with_title_and_description(self):
        """Test adding a task with title and description."""
        # Arrange
        manager = TaskManager()
        
        # Act
        task = manager.add_task(title="Buy groceries", description="Milk, eggs, bread")
        
        # Assert
        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.description == "Milk, eggs, bread"
        assert task.is_complete is False

    def test_add_multiple_tasks_generates_unique_ids(self):
        """Test that adding multiple tasks generates unique, sequential IDs."""
        # Arrange
        manager = TaskManager()
        
        # Act
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        task3 = manager.add_task(title="Task 3")
        
        # Assert
        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3

    def test_add_task_with_empty_title_raises_error(self):
        """Test that adding a task with empty title raises ValueError."""
        # Arrange
        manager = TaskManager()
        
        # Act & Assert
        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.add_task(title="")

    def test_add_task_with_whitespace_only_title_raises_error(self):
        """Test that adding a task with whitespace-only title raises ValueError."""
        # Arrange
        manager = TaskManager()
        
        # Act & Assert
        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.add_task(title="   ")

    def test_added_task_appears_in_task_list(self):
        """Test that an added task appears in the task list."""
        # Arrange
        manager = TaskManager()
        
        # Act
        task = manager.add_task(title="Buy groceries")
        all_tasks = manager.get_all_tasks()
        
        # Assert
        assert len(all_tasks) == 1
        assert all_tasks[0] == task


class TestGetAllTasks:
    """Tests for retrieving all tasks."""

    def test_get_all_tasks_returns_empty_list_when_no_tasks(self):
        """Test that get_all_tasks returns empty list when no tasks exist."""
        # Arrange
        manager = TaskManager()
        
        # Act
        tasks = manager.get_all_tasks()
        
        # Assert
        assert tasks == []
        assert len(tasks) == 0

    def test_get_all_tasks_returns_all_added_tasks(self):
        """Test that get_all_tasks returns all tasks that were added."""
        # Arrange
        manager = TaskManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        task3 = manager.add_task(title="Task 3")
        
        # Act
        tasks = manager.get_all_tasks()
        
        # Assert
        assert len(tasks) == 3
        assert task1 in tasks
        assert task2 in tasks
        assert task3 in tasks

    def test_get_all_tasks_returns_copy_not_internal_reference(self):
        """Test that get_all_tasks returns a copy, not the internal list."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        tasks1 = manager.get_all_tasks()
        tasks1.append(Task(id=999, title="Fake task"))
        tasks2 = manager.get_all_tasks()
        
        # Assert
        assert len(tasks2) == 1
        assert tasks1 is not tasks2


class TestGetTaskById:
    """Tests for retrieving a task by ID."""

    def test_get_existing_task_by_id(self):
        """Test retrieving an existing task by its ID."""
        # Arrange
        manager = TaskManager()
        task = manager.add_task(title="Buy groceries")
        
        # Act
        retrieved_task = manager.get_task_by_id(1)
        
        # Assert
        assert retrieved_task is not None
        assert retrieved_task == task
        assert retrieved_task.id == 1

    def test_get_task_by_id_returns_none_for_nonexistent_id(self):
        """Test that get_task_by_id returns None for non-existent ID."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        retrieved_task = manager.get_task_by_id(999)
        
        # Assert
        assert retrieved_task is None

    def test_get_task_by_id_from_multiple_tasks(self):
        """Test retrieving specific task from multiple tasks."""
        # Arrange
        manager = TaskManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        task3 = manager.add_task(title="Task 3")
        
        # Act
        retrieved_task = manager.get_task_by_id(2)
        
        # Assert
        assert retrieved_task == task2
        assert retrieved_task.title == "Task 2"


class TestDeleteTask:
    """Tests for deleting tasks."""

    def test_delete_existing_task(self):
        """Test deleting an existing task."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        result = manager.delete_task(1)
        
        # Assert
        assert result is True
        assert len(manager.get_all_tasks()) == 0

    def test_delete_nonexistent_task_returns_false(self):
        """Test that deleting non-existent task returns False."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        result = manager.delete_task(999)
        
        # Assert
        assert result is False
        assert len(manager.get_all_tasks()) == 1

    def test_delete_task_from_multiple_tasks(self):
        """Test deleting one task from multiple tasks."""
        # Arrange
        manager = TaskManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        task3 = manager.add_task(title="Task 3")
        
        # Act
        result = manager.delete_task(2)
        remaining_tasks = manager.get_all_tasks()
        
        # Assert
        assert result is True
        assert len(remaining_tasks) == 2
        assert task1 in remaining_tasks
        assert task2 not in remaining_tasks
        assert task3 in remaining_tasks

    def test_delete_last_remaining_task(self):
        """Test deleting the last remaining task."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        result = manager.delete_task(1)
        
        # Assert
        assert result is True
        assert manager.get_all_tasks() == []

    def test_deleted_task_id_not_reused(self):
        """Test that deleted task IDs are not reused."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        manager.add_task(title="Task 2")
        manager.delete_task(1)
        
        # Act
        new_task = manager.add_task(title="Task 3")
        
        # Assert
        assert new_task.id == 3  # Not 1 (the deleted ID)


class TestToggleCompletion:
    """Tests for toggling task completion status."""

    def test_toggle_incomplete_task_to_complete(self):
        """Test marking an incomplete task as complete."""
        # Arrange
        manager = TaskManager()
        task = manager.add_task(title="Task 1")
        assert task.is_complete is False
        
        # Act
        result = manager.toggle_completion(1)
        updated_task = manager.get_task_by_id(1)
        
        # Assert
        assert result is True
        assert updated_task.is_complete is True

    def test_toggle_complete_task_to_incomplete(self):
        """Test marking a complete task as incomplete."""
        # Arrange
        manager = TaskManager()
        task = manager.add_task(title="Task 1")
        manager.toggle_completion(1)  # Mark as complete first
        
        # Act
        result = manager.toggle_completion(1)  # Toggle back to incomplete
        updated_task = manager.get_task_by_id(1)
        
        # Assert
        assert result is True
        assert updated_task.is_complete is False

    def test_toggle_nonexistent_task_returns_false(self):
        """Test that toggling non-existent task returns False."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        result = manager.toggle_completion(999)
        
        # Assert
        assert result is False

    def test_toggle_only_affects_specific_task(self):
        """Test that toggling only affects the specified task."""
        # Arrange
        manager = TaskManager()
        task1 = manager.add_task(title="Task 1")
        task2 = manager.add_task(title="Task 2")
        task3 = manager.add_task(title="Task 3")
        
        # Act
        manager.toggle_completion(2)
        
        # Assert
        assert manager.get_task_by_id(1).is_complete is False
        assert manager.get_task_by_id(2).is_complete is True
        assert manager.get_task_by_id(3).is_complete is False


class TestUpdateTask:
    """Tests for updating task details."""

    def test_update_task_title_only(self):
        """Test updating only the title of a task."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Old Title", description="Description")
        
        # Act
        result = manager.update_task(1, title="New Title")
        updated_task = manager.get_task_by_id(1)
        
        # Assert
        assert result is True
        assert updated_task.title == "New Title"
        assert updated_task.description == "Description"

    def test_update_task_description_only(self):
        """Test updating only the description of a task."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Title", description="Old Description")
        
        # Act
        result = manager.update_task(1, description="New Description")
        updated_task = manager.get_task_by_id(1)
        
        # Assert
        assert result is True
        assert updated_task.title == "Title"
        assert updated_task.description == "New Description"

    def test_update_both_title_and_description(self):
        """Test updating both title and description of a task."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Old Title", description="Old Description")
        
        # Act
        result = manager.update_task(1, title="New Title", description="New Description")
        updated_task = manager.get_task_by_id(1)
        
        # Assert
        assert result is True
        assert updated_task.title == "New Title"
        assert updated_task.description == "New Description"

    def test_update_nonexistent_task_returns_false(self):
        """Test that updating non-existent task returns False."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        result = manager.update_task(999, title="New Title")
        
        # Assert
        assert result is False

    def test_update_task_with_empty_title_raises_error(self):
        """Test that updating a task with empty title raises ValueError."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act & Assert
        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.update_task(1, title="")

    def test_update_task_preserves_completion_status(self):
        """Test that updating a task preserves its completion status."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        manager.toggle_completion(1)  # Mark as complete
        
        # Act
        manager.update_task(1, title="Updated Task 1")
        updated_task = manager.get_task_by_id(1)
        
        # Assert
        assert updated_task.is_complete is True

    def test_update_task_preserves_id(self):
        """Test that updating a task preserves its ID."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act
        manager.update_task(1, title="Updated Task 1")
        updated_task = manager.get_task_by_id(1)
        
        # Assert
        assert updated_task.id == 1


class TestTaskManagerEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_task_manager_handles_100_tasks(self):
        """Test that TaskManager can handle 100 tasks."""
        # Arrange
        manager = TaskManager()
        
        # Act
        for i in range(100):
            manager.add_task(title=f"Task {i+1}")
        
        # Assert
        assert len(manager.get_all_tasks()) == 100
        assert manager.get_task_by_id(1) is not None
        assert manager.get_task_by_id(100) is not None

    def test_task_manager_handles_1000_tasks(self):
        """Test that TaskManager can handle 1000 tasks efficiently."""
        # Arrange
        manager = TaskManager()
        
        # Act
        for i in range(1000):
            manager.add_task(title=f"Task {i+1}")
        
        # Assert
        assert len(manager.get_all_tasks()) == 1000
        assert manager.get_task_by_id(500) is not None

    def test_operations_after_deleting_all_tasks(self):
        """Test that operations work correctly after deleting all tasks."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        manager.add_task(title="Task 2")
        manager.delete_task(1)
        manager.delete_task(2)
        
        # Act
        new_task = manager.add_task(title="Task 3")
        
        # Assert
        assert new_task.id == 3
        assert len(manager.get_all_tasks()) == 1

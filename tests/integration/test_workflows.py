"""Integration tests for end-to-end user workflows."""

import pytest
from src.services.task_manager import TaskManager


class TestCompleteUserWorkflows:
    """Tests for complete user journeys through the application."""

    def test_add_view_complete_delete_workflow(self):
        """Test a complete workflow: add → view → complete → delete."""
        # Arrange
        manager = TaskManager()
        
        # Act & Assert: Add task
        task = manager.add_task(title="Buy groceries", description="Milk, eggs")
        assert task.id == 1
        assert task.is_complete is False
        
        # Act & Assert: View tasks
        tasks = manager.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].title == "Buy groceries"
        
        # Act & Assert: Mark complete
        result = manager.toggle_completion(1)
        assert result is True
        task = manager.get_task_by_id(1)
        assert task.is_complete is True
        
        # Act & Assert: Delete task
        result = manager.delete_task(1)
        assert result is True
        tasks = manager.get_all_tasks()
        assert len(tasks) == 0

    def test_multiple_tasks_workflow(self):
        """Test managing multiple tasks."""
        # Arrange
        manager = TaskManager()
        
        # Act: Add multiple tasks
        task1 = manager.add_task(title="Task 1", description="First task")
        task2 = manager.add_task(title="Task 2", description="Second task")
        task3 = manager.add_task(title="Task 3", description="Third task")
        
        # Assert: All tasks exist
        tasks = manager.get_all_tasks()
        assert len(tasks) == 3
        
        # Act: Complete task 2
        manager.toggle_completion(2)
        
        # Assert: Only task 2 is complete
        assert manager.get_task_by_id(1).is_complete is False
        assert manager.get_task_by_id(2).is_complete is True
        assert manager.get_task_by_id(3).is_complete is False
        
        # Act: Delete task 1
        manager.delete_task(1)
        
        # Assert: Tasks 2 and 3 remain
        tasks = manager.get_all_tasks()
        assert len(tasks) == 2
        assert manager.get_task_by_id(1) is None
        assert manager.get_task_by_id(2) is not None
        assert manager.get_task_by_id(3) is not None

    def test_update_task_workflow(self):
        """Test adding and updating a task."""
        # Arrange
        manager = TaskManager()
        
        # Act: Add task
        task = manager.add_task(title="Old Title", description="Old Description")
        
        # Act: Update title
        manager.update_task(1, title="New Title")
        task = manager.get_task_by_id(1)
        
        # Assert: Title updated, description unchanged
        assert task.title == "New Title"
        assert task.description == "Old Description"
        
        # Act: Update description
        manager.update_task(1, description="New Description")
        task = manager.get_task_by_id(1)
        
        # Assert: Both updated
        assert task.title == "New Title"
        assert task.description == "New Description"

    def test_toggle_task_multiple_times(self):
        """Test toggling task completion multiple times."""
        # Arrange
        manager = TaskManager()
        task = manager.add_task(title="Task 1")
        
        # Assert: Starts incomplete
        assert task.is_complete is False
        
        # Act & Assert: Toggle to complete
        manager.toggle_completion(1)
        task = manager.get_task_by_id(1)
        assert task.is_complete is True
        
        # Act & Assert: Toggle back to incomplete
        manager.toggle_completion(1)
        task = manager.get_task_by_id(1)
        assert task.is_complete is False
        
        # Act & Assert: Toggle to complete again
        manager.toggle_completion(1)
        task = manager.get_task_by_id(1)
        assert task.is_complete is True

    def test_error_recovery_workflow(self):
        """Test that system recovers gracefully from errors."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act: Try to delete non-existent task
        result = manager.delete_task(999)
        assert result is False
        
        # Assert: Original task still exists
        tasks = manager.get_all_tasks()
        assert len(tasks) == 1
        
        # Act: Try to update non-existent task
        result = manager.update_task(999, title="New Title")
        assert result is False
        
        # Assert: Original task unchanged
        task = manager.get_task_by_id(1)
        assert task.title == "Task 1"
        
        # Act: Try to toggle non-existent task
        result = manager.toggle_completion(999)
        assert result is False
        
        # Assert: Original task unchanged
        task = manager.get_task_by_id(1)
        assert task.is_complete is False

    def test_complex_multi_task_scenario(self):
        """Test a complex scenario with multiple operations."""
        # Arrange
        manager = TaskManager()
        
        # Add 5 tasks
        for i in range(1, 6):
            manager.add_task(
                title=f"Task {i}",
                description=f"Description for task {i}"
            )
        
        # Assert: All tasks exist
        assert len(manager.get_all_tasks()) == 5
        
        # Complete tasks 1, 3, 5
        manager.toggle_completion(1)
        manager.toggle_completion(3)
        manager.toggle_completion(5)
        
        # Assert: Correct tasks are complete
        assert manager.get_task_by_id(1).is_complete is True
        assert manager.get_task_by_id(2).is_complete is False
        assert manager.get_task_by_id(3).is_complete is True
        assert manager.get_task_by_id(4).is_complete is False
        assert manager.get_task_by_id(5).is_complete is True
        
        # Update task 2
        manager.update_task(2, title="Updated Task 2")
        assert manager.get_task_by_id(2).title == "Updated Task 2"
        
        # Delete tasks 1 and 4
        manager.delete_task(1)
        manager.delete_task(4)
        
        # Assert: Tasks 2, 3, 5 remain
        tasks = manager.get_all_tasks()
        assert len(tasks) == 3
        assert manager.get_task_by_id(1) is None
        assert manager.get_task_by_id(2) is not None
        assert manager.get_task_by_id(3) is not None
        assert manager.get_task_by_id(4) is None
        assert manager.get_task_by_id(5) is not None
        
        # Add new task (should get ID 6, not 1 or 4)
        new_task = manager.add_task(title="Task 6")
        assert new_task.id == 6


class TestEdgeCaseWorkflows:
    """Tests for edge case scenarios."""

    def test_delete_all_tasks_then_add_new(self):
        """Test deleting all tasks and adding new ones."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        manager.add_task(title="Task 2")
        manager.add_task(title="Task 3")
        
        # Act: Delete all tasks
        manager.delete_task(1)
        manager.delete_task(2)
        manager.delete_task(3)
        
        # Assert: No tasks remain
        assert len(manager.get_all_tasks()) == 0
        
        # Act: Add new task
        new_task = manager.add_task(title="Task 4")
        
        # Assert: New task has ID 4 (not reused)
        assert new_task.id == 4
        assert len(manager.get_all_tasks()) == 1

    def test_update_completed_task(self):
        """Test that updating a task preserves completion status."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1", description="Original")
        manager.toggle_completion(1)
        
        # Act: Update task
        manager.update_task(1, title="Updated Task", description="Updated")
        task = manager.get_task_by_id(1)
        
        # Assert: Task updated but still complete
        assert task.title == "Updated Task"
        assert task.description == "Updated"
        assert task.is_complete is True

    def test_rapid_consecutive_operations(self):
        """Test performing many operations in quick succession."""
        # Arrange
        manager = TaskManager()
        
        # Act: Rapid adds
        for i in range(50):
            manager.add_task(title=f"Task {i}")
        
        # Assert: All added
        assert len(manager.get_all_tasks()) == 50
        
        # Act: Rapid toggles
        for i in range(1, 51):
            manager.toggle_completion(i)
        
        # Assert: All complete
        for i in range(1, 51):
            assert manager.get_task_by_id(i).is_complete is True
        
        # Act: Rapid deletes (odd IDs)
        for i in range(1, 51, 2):
            manager.delete_task(i)
        
        # Assert: 25 tasks remain (even IDs)
        assert len(manager.get_all_tasks()) == 25


class TestValidationWorkflows:
    """Tests for validation throughout workflows."""

    def test_cannot_add_task_with_empty_title(self):
        """Test that empty title is rejected at any point."""
        # Arrange
        manager = TaskManager()
        
        # Act & Assert: Try to add with empty title
        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.add_task(title="")

    def test_cannot_update_task_to_empty_title(self):
        """Test that updating to empty title is rejected."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        
        # Act & Assert: Try to update to empty title
        with pytest.raises(ValueError, match="Title cannot be empty"):
            manager.update_task(1, title="")
        
        # Assert: Original task unchanged
        task = manager.get_task_by_id(1)
        assert task.title == "Task 1"

    def test_operations_on_deleted_task_fail_gracefully(self):
        """Test that operations on deleted tasks fail gracefully."""
        # Arrange
        manager = TaskManager()
        manager.add_task(title="Task 1")
        manager.delete_task(1)
        
        # Act & Assert: All operations fail gracefully
        assert manager.get_task_by_id(1) is None
        assert manager.delete_task(1) is False
        assert manager.toggle_completion(1) is False
        assert manager.update_task(1, title="New Title") is False

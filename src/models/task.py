"""Task entity for the todo application."""

from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a todo task.
    
    Attributes:
        id: Unique numeric identifier (must be positive integer)
        title: Short description of the task (required, cannot be empty)
        description: Detailed description of the task (optional)
        is_complete: Boolean flag indicating completion status
    """
    
    id: int
    title: str
    description: str = ""
    is_complete: bool = False
    
    def __post_init__(self):
        """Validate task attributes after initialization."""
        # Validate ID
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")
        
        # Validate title
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        
        # Ensure description is a string
        if self.description is None:
            self.description = ""
    
    def __str__(self) -> str:
        """Return a human-readable string representation of the task."""
        status = "✓" if self.is_complete else " "
        result = f"[{self.id}] [{status}] {self.title}"
        if self.description:
            result += f"\n    {self.description}"
        return result
    
    def __eq__(self, other: object) -> bool:
        """
        Compare tasks based on their ID.
        
        Two tasks are considered equal if they have the same ID.
        """
        if not isinstance(other, Task):
            return NotImplemented
        return self.id == other.id
    
    def __hash__(self) -> int:
        """Return hash based on task ID for use in sets and dicts."""
        return hash(self.id)

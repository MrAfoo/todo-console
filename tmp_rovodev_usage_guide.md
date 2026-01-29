# CLI Todo Application - Usage Guide

## Running the Application

```powershell
python src/main.py
```

## Example Session

```
Welcome to the CLI Todo Application!
All tasks are stored in memory only.

=== Todo Application ===

1. View all tasks
2. Add task
3. Update task
4. Delete task
5. Toggle task completion
6. Exit

Enter your choice (1-6): 2
Enter task title: Buy groceries
Enter task description (optional): Milk, eggs, bread
✓ Task added successfully! (ID: 1)

Enter your choice (1-6): 2
Enter task title: Call dentist
Enter task description (optional): Schedule appointment
✓ Task added successfully! (ID: 2)

Enter your choice (1-6): 1

Your Tasks:
------------
1. [ ] Buy groceries
   Description: Milk, eggs, bread
   
2. [ ] Call dentist
   Description: Schedule appointment

Enter your choice (1-6): 5
Enter task ID to toggle: 1
✓ Task completion toggled!

Enter your choice (1-6): 1

Your Tasks:
------------
1. [✓] Buy groceries
   Description: Milk, eggs, bread
   
2. [ ] Call dentist
   Description: Schedule appointment

Enter your choice (1-6): 3
Enter task ID to update: 2
Enter new title (or press Enter to keep current): Call dentist URGENT
Enter new description (or press Enter to keep current): 
✓ Task updated successfully!

Enter your choice (1-6): 4
Enter task ID to delete: 1
✓ Task deleted successfully!

Enter your choice (1-6): 6
Goodbye!
```

## Menu Options

1. **View all tasks** - Display all tasks with their status
2. **Add task** - Create a new task with title and optional description
3. **Update task** - Modify an existing task's title or description
4. **Delete task** - Remove a task permanently
5. **Toggle task completion** - Mark task as done/undone
6. **Exit** - Close the application

## Notes

- All tasks are stored **in memory only** (lost when you exit)
- Task IDs are auto-generated starting from 1
- Press Enter on description prompts to leave them empty
- [✓] indicates completed tasks, [ ] indicates pending tasks

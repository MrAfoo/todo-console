# CLI Todo Application

A command-line todo application with in-memory storage built with Python 3.13+.

## Features

- ✅ Add tasks with title and description
- ✅ View all tasks with status indicators
- ✅ Update task details (title/description)
- ✅ Delete tasks by ID
- ✅ Mark tasks as complete/incomplete
- 🔄 In-memory storage (no persistence between sessions)

## Requirements

- Python 3.13 or higher
- UV (recommended) or pip for dependency management

## Installation

### Using UV (Recommended)

```bash
# Install UV if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync

# Run the application
uv run python -m src.main
```

### Using pip

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -e ".[dev]"

# Run the application
python -m src.main
```

## Usage

The application provides a menu-driven interface:

```
=== Todo Application ===

1. View all tasks
2. Add task
3. Update task
4. Delete task
5. Toggle task completion
6. Exit

Choose an option (1-6):
```

### Example Workflow

1. **Add a task**: Choose option 2, enter title and description
2. **View tasks**: Choose option 1 to see all tasks with status
3. **Mark complete**: Choose option 5, enter task ID
4. **Delete task**: Choose option 4, enter task ID

### Task Display Format

```
[1] [ ] Buy groceries
    Milk, eggs, bread

[2] [✓] Complete project
    Finish the CLI todo app
```

- `[ ]` indicates an incomplete task
- `[✓]` indicates a completed task

## Development

### Running Tests

```bash
# Run all tests with coverage
uv run pytest

# Run specific test file
uv run pytest tests/unit/test_task.py

# Run with verbose output
uv run pytest -v

# Generate HTML coverage report
uv run pytest --cov-report=html
```

### Code Quality

```bash
# Format code
uv run black src tests

# Lint code
uv run flake8 src tests

# Type checking
uv run mypy src
```

### Project Structure

```
cli-todo-app/
├── src/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task entity
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_manager.py  # Business logic
│   └── cli/
│       ├── __init__.py
│       ├── interface.py     # Display functions
│       └── commands.py      # Command handlers
├── tests/
│   ├── unit/                # Unit tests
│   └── integration/         # Integration tests
├── pyproject.toml           # Project configuration
└── README.md
```

## Design Decisions

- **In-memory storage**: Tasks are stored in memory only. Data is lost when the application exits.
- **Menu-driven interface**: Numbered options for discoverability and ease of use.
- **Dictionary storage**: O(1) lookup performance by task ID.
- **Monotonic IDs**: Task IDs are never reused to prevent confusion.

## Limitations

- No data persistence between sessions
- Single-user, single-session only
- No task sorting or filtering
- No due dates, priorities, or categories

## License

This project is built following the Spec-Kit Plus methodology.

## Contributing

This project follows Test-Driven Development (TDD):
1. Write failing test (RED)
2. Implement minimal code (GREEN)
3. Refactor (REFACTOR)

All code must:
- Pass pytest with ≥90% coverage
- Follow PEP 8 style guidelines
- Include type hints
- Have descriptive function names (<50 lines each)

## Troubleshooting

### Python version issues
Ensure you have Python 3.13+ installed:
```bash
python --version
```

### Import errors
Make sure you're running from the project root and dependencies are installed:
```bash
uv sync
```

### Test failures
Check that all dependencies are installed:
```bash
uv sync
uv run pytest -v
```

## Support

For issues or questions, refer to the specification documents:
- `spec-cli-todo-app.md` - Feature specification
- `plan-cli-todo-app.md` - Implementation plan

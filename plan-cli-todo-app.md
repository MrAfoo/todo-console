# Implementation Plan: CLI Todo Application

**Branch**: `001-cli-todo-app` | **Date**: 2026-01-29 | **Spec**: `spec-cli-todo-app.md`  
**Input**: Feature specification from `spec-cli-todo-app.md`

## Summary

Build a command-line todo application in Python 3.13+ that stores tasks in memory (no persistence). Users can add tasks with title/description, view all tasks with status indicators, update task details, delete tasks by ID, and mark tasks as complete/incomplete. The application follows spec-driven development methodology using UV for dependency management, with comprehensive unit tests and clean code architecture.

## Technical Context

**Language/Version**: Python 3.13+  
**Primary Dependencies**: UV (project management), pytest (testing)  
**Storage**: In-memory (list/dict) - no file or database persistence  
**Testing**: pytest with ≥90% code coverage  
**Target Platform**: Cross-platform CLI (Linux, macOS, Windows)  
**Project Type**: Single project (CLI application)  
**Performance Goals**: All operations complete in <1 second for up to 1000 tasks  
**Constraints**: In-memory only, no external runtime dependencies beyond testing  
**Scale/Scope**: Small utility application, ~500-1000 lines of code, single-user session

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### ✅ Code Quality & Clean Design
- Functions MUST be <50 lines with single responsibility
- Modular design with clear boundaries (domain, service, interface layers)
- PEP 8 compliance enforced (black, flake8, mypy)
- Type hints for all function signatures

### ✅ Testing Standards (NON-NEGOTIABLE)
- Test-Driven Development (write tests first)
- ≥90% code coverage for all new code
- Tests cover edge cases, boundary conditions, error handling
- Tests follow Arrange-Act-Assert pattern

### ✅ User Experience Consistency
- Clear CLI prompts with explicit options
- Error messages explain what went wrong AND how to fix it
- Command structure follows intuitive patterns
- Graceful handling of Ctrl+C and invalid inputs

### ✅ Performance Requirements
- In-memory operations <10ms for datasets under 10,000 items
- CLI startup time <200ms
- Use appropriate data structures (dict for O(1) lookup by ID)

**Constitutional Violations**: None anticipated

## Project Structure

### Documentation (this feature)

```text
/
├── spec-cli-todo-app.md     # Feature specification (existing)
├── plan-cli-todo-app.md     # This file
└── tasks-cli-todo-app.md    # Created by sp.tasks command (next step)
```

### Source Code (repository root)

```text
/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point and main application loop
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task entity (dataclass)
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_manager.py  # TaskManager for CRUD operations
│   └── cli/
│       ├── __init__.py
│       ├── interface.py     # CLI display and user interaction
│       └── commands.py      # Command handlers for each operation
│
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_task.py
│   │   ├── test_task_manager.py
│   │   └── test_cli_commands.py
│   └── integration/
│       ├── __init__.py
│       └── test_workflows.py  # End-to-end user journeys
│
├── pyproject.toml           # UV project configuration
├── README.md                # Setup and usage instructions
├── CLAUDE.md                # Claude Code rules (existing)
└── .python-version          # Python version specification
```

**Structure Decision**: Single project structure with clear separation of concerns:
- **models/**: Domain entities (Task dataclass)
- **services/**: Business logic (TaskManager)
- **cli/**: User interface layer (display, input handling, commands)
- **main.py**: Application controller and main loop

This structure supports test-driven development and maintains clean architecture boundaries.

## Implementation Approach

### Phase 0: Project Setup
1. **Initialize UV project**
   - Create `pyproject.toml` with Python 3.13+ requirement
   - Add pytest as dev dependency
   - Create `.python-version` file
   - Set up basic folder structure

2. **Create README.md**
   - Installation instructions (UV setup)
   - Usage examples
   - Command reference

3. **Create initial test structure**
   - Set up pytest configuration
   - Create test directories

### Phase 1: Core Domain (P1 - MVP Foundation)

**TDD Cycle**: Write tests → Implement → Refactor

1. **Task Entity (models/task.py)**
   - Test: Task creation with required/optional fields
   - Test: Task validation (empty title)
   - Test: Task immutability of ID
   - Implement: Task dataclass with validation
   ```python
   @dataclass
   class Task:
       id: int
       title: str
       description: str = ""
       is_complete: bool = False
   ```

2. **TaskManager Service (services/task_manager.py)**
   - Test: Add task with auto-generated ID
   - Test: View all tasks (empty list, multiple tasks)
   - Test: Get task by ID (valid, invalid)
   - Test: ID generation (unique, monotonically increasing)
   - Implement: TaskManager with dict storage for O(1) lookup
   ```python
   class TaskManager:
       def __init__(self):
           self._tasks: dict[int, Task] = {}
           self._next_id: int = 1
       
       def add_task(title: str, description: str = "") -> Task
       def get_all_tasks() -> list[Task]
       def get_task_by_id(task_id: int) -> Task | None
   ```

3. **Basic CLI (cli/interface.py, cli/commands.py)**
   - Test: Display empty task list
   - Test: Display tasks with formatting
   - Test: Add task command flow
   - Test: View tasks command flow
   - Implement: Menu-driven interface with numbered options
   - Implement: Command handlers for add and view

4. **Main Application Loop (main.py)**
   - Test: Main loop handles valid commands
   - Test: Graceful exit on Ctrl+C
   - Test: Error handling for invalid menu choices
   - Implement: Application controller

**MVP Checkpoint**: At this point, users can add and view tasks (deliverable product)

### Phase 2: Task Status Management (P2)

**TDD Cycle**: Write tests → Implement → Refactor

5. **Toggle Task Completion**
   - Test: Mark incomplete task as complete
   - Test: Mark complete task as incomplete
   - Test: Invalid task ID error handling
   - Test: Status indicator in display
   - Implement: TaskManager.toggle_completion(task_id)
   - Implement: CLI command for toggle

6. **Delete Task**
   - Test: Delete existing task
   - Test: Delete non-existent task (error)
   - Test: Verify task removed from list
   - Test: Delete last task (empty list handling)
   - Implement: TaskManager.delete_task(task_id)
   - Implement: CLI command for delete

### Phase 3: Task Updates (P3)

**TDD Cycle**: Write tests → Implement → Refactor

7. **Update Task Details**
   - Test: Update title only
   - Test: Update description only
   - Test: Update both fields
   - Test: Invalid task ID error
   - Test: Empty title validation
   - Implement: TaskManager.update_task(task_id, title, description)
   - Implement: CLI command for update

### Phase 4: Edge Cases & Refinement

8. **Edge Case Testing**
   - Test: Special characters in title/description (quotes, newlines, unicode)
   - Test: Very long titles/descriptions (100+ chars)
   - Test: Rapid consecutive operations
   - Test: Invalid input types (letters when expecting numbers)
   - Implement: Input validation and sanitization
   - Implement: Error handling improvements

9. **Integration Testing**
   - Test: Complete user workflows (add → view → complete → delete)
   - Test: Multiple task manipulation in sequence
   - Test: Error recovery scenarios

10. **Performance Validation**
    - Test: 1000 tasks in memory
    - Test: Operation speed benchmarks
    - Verify: <10ms for operations, <200ms startup

### Phase 5: Documentation & Polish

11. **User Documentation**
    - Complete README with examples
    - Add command reference
    - Include troubleshooting section

12. **Code Quality Gates**
    - Run black formatting
    - Run flake8 linting
    - Run mypy type checking
    - Verify test coverage ≥90%
    - Review code for constitutional compliance

## Key Design Decisions

### CLI Pattern Choice
**Decision**: Menu-driven interface with numbered options  
**Rationale**: 
- More discoverable for first-time users
- No need to remember command syntax
- Clear visual feedback of available actions
- Simpler to implement and test

**Alternative Rejected**: Command-based interface (e.g., `> add "title"`)
- Requires users to remember command syntax
- More complex parsing logic
- Higher learning curve

### Data Structure Choice
**Decision**: Dictionary with integer keys for task storage  
**Rationale**:
- O(1) lookup by task ID
- Efficient for all CRUD operations
- Simple to implement and test
- Natural fit for unique ID pattern

**Alternative Rejected**: List with linear search
- O(n) lookup for get/update/delete operations
- Performance degradation at scale

### ID Generation Strategy
**Decision**: Monotonically increasing integers, never reused  
**Rationale**:
- Simple and predictable
- Prevents confusion from ID reuse
- No collision risk
- Easy to debug and test

**Alternative Rejected**: Reuse deleted IDs
- Could confuse users
- More complex bookkeeping

## Testing Strategy

### Test Pyramid
- **70% Unit Tests**: Test individual functions and methods in isolation
- **20% Integration Tests**: Test workflows and component interactions
- **10% Edge Cases**: Test boundary conditions and error scenarios

### Test Organization
```text
tests/
├── unit/
│   ├── test_task.py           # Task entity tests
│   ├── test_task_manager.py   # TaskManager service tests
│   └── test_cli_commands.py   # CLI command handler tests
└── integration/
    └── test_workflows.py       # End-to-end user journeys
```

### Coverage Goals
- Overall: ≥90%
- Core business logic (TaskManager): 100%
- Domain models (Task): 100%
- CLI layer: ≥85% (some display logic may be hard to test)

## Risk Mitigation

### Risk: Complex CLI interaction testing
**Mitigation**: 
- Separate display logic from business logic
- Use dependency injection for testability
- Mock user input in tests

### Risk: Unicode/special character handling
**Mitigation**:
- Test with diverse character sets early
- Use Python 3.13+ native Unicode support
- Add explicit encoding tests

### Risk: Time pressure vs. test coverage
**Mitigation**:
- Strict TDD discipline (no code without tests)
- P1 features fully tested before moving to P2
- Constitutional quality gates enforced

## Success Criteria Validation

This implementation satisfies all specification requirements:

1. ✅ **FR-001 to FR-012**: All functional requirements met through phased implementation
2. ✅ **TR-001 to TR-007**: Python 3.13+, UV, TDD, comprehensive tests, graceful error handling
3. ✅ **SC-001 to SC-007**: Operations <5s, clear errors, 100 task support, automated tests, intuitive CLI
4. ✅ **NFR-001 to NFR-010**: Clear prompts, graceful errors, <1s operations, PEP 8, docstrings
5. ✅ **User Stories**: All P1, P2, P3 stories implemented with acceptance tests
6. ✅ **Edge Cases**: Covered in Phase 4
7. ✅ **Constitution**: All principles satisfied (clean code, ≥90% coverage, clear UX, performance)

## Next Steps

1. Run `sp.tasks` command to create detailed task breakdown
2. Begin Phase 0: Project setup with UV
3. Follow TDD cycle for each component (RED → GREEN → REFACTOR)
4. Validate MVP (P1) before proceeding to P2
5. Run quality gates before final delivery

**Estimated Complexity**: Low-Medium (as per spec)  
**Estimated Time**: 4-8 hours of focused development  
**Development Order**: P1 (MVP) → P2 → P3 → Edge Cases → Documentation

---

## Appendix: Example CLI Flows

### Example 1: Menu-driven interface
```
=== Todo Application ===

1. View all tasks
2. Add task
3. Update task
4. Delete task
5. Toggle task completion
6. Exit

Choose an option (1-6): 2

--- Add Task ---
Title: Buy groceries
Description: Milk, eggs, bread

✓ Task #1 added successfully!

Choose an option (1-6): 1

--- All Tasks ---
[1] [ ] Buy groceries
    Milk, eggs, bread

Choose an option (1-6): 5

--- Toggle Task Completion ---
Task ID: 1

✓ Task #1 marked as complete!

Choose an option (1-6): 1

--- All Tasks ---
[1] [✓] Buy groceries
    Milk, eggs, bread
```

### Example 2: Error handling
```
Choose an option (1-6): 4

--- Delete Task ---
Task ID: 99

✗ Error: Task #99 not found. Use option 1 to view existing tasks.

Choose an option (1-6): 2

--- Add Task ---
Title: 

✗ Error: Title cannot be empty. Please provide a valid title.
```

This appendix demonstrates the expected user experience and helps guide implementation decisions.

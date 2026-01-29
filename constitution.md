<!--
SYNC IMPACT REPORT
==================
Version Change: [TEMPLATE] → 1.0.0
Date: 2026-01-29

Modified Principles:
- NEW: I. Code Quality & Clean Design
- NEW: II. Testing Standards (NON-NEGOTIABLE)
- NEW: III. User Experience Consistency
- NEW: IV. Performance Requirements

Added Sections:
- Development Standards
- Quality Gates

Templates Status:
- ✅ plan-template.md - Constitution Check section aligned
- ✅ spec-template.md - Success Criteria and Requirements aligned
- ✅ tasks-template.md - Testing phases aligned

Follow-up TODOs: None
-->

# SpecifyPlus Constitution

## Core Principles

### I. Code Quality & Clean Design

**Clean Functions**:
- Functions MUST have a single, well-defined responsibility
- Function length MUST NOT exceed 50 lines (excluding docstrings)
- Function names MUST clearly express intent using verb-noun patterns
- Complex operations MUST be broken into smaller, composable functions

**Modular Design**:
- Code MUST be organized into logical modules with clear boundaries
- Modules MUST have minimal coupling and high cohesion
- Dependencies between modules MUST flow in one direction (no circular dependencies)
- Each module MUST have a clearly documented public interface

**PEP 8 Compliance**:
- All Python code MUST adhere to PEP 8 style guidelines
- Line length MUST NOT exceed 100 characters
- Imports MUST be organized: standard library, third-party, local (separated by blank lines)
- Code MUST pass `flake8` and `black` formatting checks before commit
- Type hints MUST be used for all function signatures

**Rationale**: Clean, modular code reduces cognitive load, accelerates debugging, and enables confident refactoring. PEP 8 compliance ensures consistency across the codebase and reduces friction in code reviews.

### II. Testing Standards (NON-NEGOTIABLE)

**Unit Test Coverage**:
- All features MUST have unit tests before implementation (Test-Driven Development)
- Code coverage MUST be ≥90% for all new code
- Every public function and method MUST have at least one test
- Tests MUST be independent and executable in any order

**Edge Case Coverage**:
- Tests MUST cover boundary conditions (empty inputs, maximum values, null/None)
- Tests MUST verify error handling for invalid inputs
- Tests MUST validate state transitions and side effects
- Tests MUST include negative test cases (what should NOT happen)

**Test Quality**:
- Test names MUST clearly describe what is being tested using `test_<scenario>_<expected_outcome>` pattern
- Tests MUST follow Arrange-Act-Assert (AAA) structure
- Tests MUST NOT depend on external services (use mocks/stubs)
- Test fixtures MUST be minimal and focused on the test scenario

**Testing Workflow**:
1. Write failing test (RED)
2. Implement minimal code to pass test (GREEN)
3. Refactor while keeping tests green (REFACTOR)
4. Repeat

**Rationale**: Comprehensive testing prevents regressions, enables confident refactoring, and serves as living documentation. Test-first development ensures testable design and complete coverage.

### III. User Experience Consistency

**Clear CLI Prompts**:
- All user-facing prompts MUST be clear, concise, and action-oriented
- Error messages MUST explain what went wrong AND how to fix it
- Success messages MUST confirm the action taken and its result
- Interactive prompts MUST show available options explicitly

**Intuitive Commands**:
- Command names MUST use clear, standard verbs (init, create, update, delete, list)
- Commands MUST follow the pattern: `command <noun> [options]`
- Options MUST have both short (`-h`) and long (`--help`) forms
- Required vs optional parameters MUST be clearly distinguished
- Commands MUST provide helpful usage examples in help text

**Consistent Behavior**:
- Similar operations MUST use similar command structures across the CLI
- Output formats MUST be consistent (JSON, table, or plain text with clear selection)
- Exit codes MUST follow conventions: 0 = success, 1 = general error, 2 = usage error
- Destructive operations MUST require confirmation or `--force` flag

**Rationale**: Consistent, intuitive UX reduces learning curve, minimizes errors, and increases user confidence. Clear feedback prevents frustration and support burden.

### IV. Performance Requirements

**Fast In-Memory Operations**:
- Data structures MUST be optimized for common access patterns
- In-memory operations MUST complete in <10ms for datasets under 10,000 items
- Algorithms MUST have documented time complexity (Big O notation)
- Memory usage MUST be proportional to input size (avoid unnecessary copies)

**Minimal Overhead**:
- CLI startup time MUST be <200ms on modern hardware
- Import statements MUST be lazy-loaded where possible to reduce startup time
- Configuration loading MUST be cached and reused within a session
- File I/O MUST be minimized through efficient buffering and batch operations

**Performance Testing**:
- Performance-critical code MUST have benchmark tests
- Performance regressions MUST be caught in CI before merge
- Bottlenecks MUST be identified through profiling, not guessing
- Performance optimizations MUST be measured and documented

**Rationale**: Fast, efficient tools respect user time and enable integration into larger workflows. Performance budgets prevent gradual degradation over time.

## Development Standards

### Code Review Requirements
- All code changes MUST pass automated checks (linting, formatting, tests) before review
- Reviews MUST verify constitutional compliance explicitly
- Reviewers MUST approve both implementation AND test quality
- Feedback MUST be actionable and reference specific principles when applicable

### Documentation Requirements
- All public APIs MUST have docstrings following Google/NumPy style
- Complex algorithms MUST include inline comments explaining the "why" not the "what"
- README files MUST be updated when user-facing behavior changes
- Breaking changes MUST be documented in CHANGELOG with migration guidance

### Dependency Management
- New dependencies MUST be justified and approved
- Dependencies MUST be pinned to specific versions or version ranges
- Security vulnerabilities MUST be addressed within one sprint
- Unused dependencies MUST be removed promptly

## Quality Gates

**Pre-Commit Gates**:
- ✅ Code formatted with `black`
- ✅ Linting passes (`flake8`, `mypy`)
- ✅ Unit tests pass with ≥90% coverage
- ✅ No new type checking errors

**Pre-Merge Gates**:
- ✅ All automated tests pass (unit, integration)
- ✅ Code review approved by at least one maintainer
- ✅ Documentation updated for user-facing changes
- ✅ Performance benchmarks pass (no regressions >10%)
- ✅ Constitutional compliance verified

**Release Gates**:
- ✅ All quality gates passed
- ✅ Integration tests pass in staging environment
- ✅ Release notes prepared
- ✅ Migration guide provided for breaking changes

## Governance

**Constitution Authority**:
- This constitution supersedes all other development practices and guidelines
- When conflicts arise, constitution principles take precedence
- All pull requests and code reviews MUST explicitly verify compliance with this constitution

**Amendment Process**:
1. Proposed amendments MUST be documented with rationale and impact analysis
2. Amendments MUST be approved by project maintainers
3. Version number MUST be incremented following semantic versioning:
   - **MAJOR**: Backward-incompatible principle changes or removals
   - **MINOR**: New principles added or material expansions
   - **PATCH**: Clarifications, wording improvements, typo fixes
4. Migration plan MUST be provided for breaking changes
5. All dependent templates and documentation MUST be updated

**Compliance Enforcement**:
- Automated tooling MUST enforce objective rules (formatting, coverage, performance)
- Code reviews MUST verify subjective principles (modularity, clarity, design)
- Violations MUST be justified in writing and approved by maintainers
- Repeated violations indicate the need for tooling improvements or training

**Continuous Improvement**:
- Constitution MUST be reviewed quarterly for relevance and completeness
- Pain points and friction MUST be addressed through amendments
- Team feedback MUST be solicited before major changes

**Version**: 1.0.0 | **Ratified**: 2026-01-29 | **Last Amended**: 2026-01-29

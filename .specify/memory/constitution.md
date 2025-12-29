# Hackathon II - Phase I: Todo Console Application Constitution

<!--
Sync Impact Report:
Version: 1.0.0 (Initial constitution)
Changes: Initial creation based on project requirements
Modified Principles: N/A (initial version)
Added Sections: All sections newly created
Removed Sections: None
Templates Status:
  ✅ plan-template.md - Reviewed, no updates required (template generic enough)
  ✅ spec-template.md - Reviewed, no updates required (template generic enough)
  ✅ tasks-template.md - Reviewed, no updates required (template generic enough)
Follow-up TODOs: None
-->

## Core Principles

### I. Spec-Driven Development (NON-NEGOTIABLE)

All features MUST originate from written specifications. No code implementation may begin without:
- A complete feature specification in `specs/` directory
- Clear user scenarios with acceptance criteria
- Defined functional requirements
- Success criteria documented

**Rationale**: Ensures intentional design, prevents scope creep, and maintains traceability from requirements to implementation.

### II. Simplicity and Clarity

Code MUST be beginner-friendly and readable:
- Clear, descriptive variable and function names following PEP 8 conventions
- Small, focused functions with single responsibility
- Minimal complexity - prefer straightforward solutions over clever optimizations
- Self-documenting code structure

**Rationale**: Hackathon context requires rapid understanding and modification. Code clarity enables faster iteration and collaboration.

### III. Clean Code Practices

All code MUST follow clean code principles:
- PEP 8 style guide compliance (enforced via linting)
- Functions limited to one clear responsibility
- No code duplication - extract reusable logic
- Modular design enabling independent testing of components

**Rationale**: Maintainability is critical even in time-constrained contexts. Clean code reduces debugging time and enables confident changes.

### IV. In-Memory Data Handling Only

Data storage MUST use in-memory structures exclusively:
- Tasks stored in Python lists or dictionaries
- No file I/O for persistence
- No database connections
- State exists only during program execution

**Rationale**: Phase I scope limitation reduces complexity and focuses implementation on core business logic and user interaction patterns.

### V. Deterministic Console Behavior

Console output MUST be predictable and user-friendly:
- Consistent formatting for all output types
- Clear status indicators (complete/incomplete markers)
- User-friendly error messages
- Task IDs managed consistently and uniquely within session

**Rationale**: Predictable UX enables reliable testing and demo scenarios. Clear console output is the sole user interface in this application.

### VI. Direct Requirement Mapping

Every implemented feature MUST trace directly to Phase I requirements:
- Add tasks with title and description
- List all tasks with status indicators
- Update task title and description
- Delete tasks by task ID
- Mark tasks as complete or incomplete

**Rationale**: Scope discipline prevents feature bloat and ensures delivery focus on defined objectives.

## Technology Stack Requirements

**Language**: Python 3.13 or higher (MANDATORY)

**Package Management**: UV (MANDATORY)
- All dependencies installed and managed via UV
- `pyproject.toml` and `uv.lock` must be maintained

**Development Tools**: Claude Code with Spec-Kit Plus (MANDATORY)
- All specifications created using Spec-Kit Plus templates
- Development workflow follows Claude Code best practices
- Prompt History Records (PHRs) created for significant development sessions

**Application Type**: Command-line interface (CLI) only
- No web frameworks
- No GUI libraries
- Console-based interaction exclusively

**Storage Constraints**: In-memory only
- No external dependencies for persistence
- Python built-in data structures (list, dict) only

**External Frameworks**: None beyond approved stack
- Standard library usage permitted
- No third-party frameworks for core functionality

## Development Workflow

### Specification-First Process

1. **Feature Definition**: Create specification document in `specs-history/` using spec template
2. **Planning**: Generate implementation plan using plan template
3. **Task Breakdown**: Create task list using tasks template
4. **Implementation**: Code only after specs/plan/tasks complete
5. **Verification**: Validate against acceptance criteria in specification

### Code Quality Gates

All code MUST pass before commit:
- PEP 8 compliance verification
- Function length check (prefer < 20 lines)
- Single responsibility validation
- No duplicated logic

### Project Structure Standards

```
/src                    # All Python source code
specs-history/          # All specification files
  ├── spec.md
  ├── plan.md
  └── tasks.md
README.md               # Setup and run instructions
CLAUDE.md               # Claude Code usage documentation
CONSTITUTION.md         # This file
.specify/               # Spec-Kit Plus templates and memory
history/                # Prompt history records and ADRs
```

**Enforcement**:
- No code outside `/src` directory
- All specs in `specs-history/` directory
- Documentation files at repository root

### Task ID Management

Task IDs MUST be:
- Unique within the application session
- Consistently typed (integer recommended)
- Sequential or deterministically generated
- Preserved through all operations until deletion

**Enforcement**: Manual code review to verify ID uniqueness logic.

## Governance

This constitution supersedes all other project practices and guidelines.

**Amendment Process**:
1. Proposed amendment documented with rationale
2. Impact assessment on existing code and specs
3. Version increment per semantic versioning rules
4. Migration plan for affected artifacts
5. Update of all dependent templates

**Compliance Verification**:
- All pull requests MUST reference constitution compliance
- Spec reviews verify adherence to spec-driven principle
- Code reviews enforce clean code and simplicity principles

**Complexity Justification**:
- Any deviation from principles MUST be documented
- Alternatives considered and rejected MUST be stated
- Approval required before implementation

**Runtime Guidance**: Refer to `CLAUDE.md` for development workflow guidance and Claude Code-specific practices.

**Version**: 1.0.0 | **Ratified**: 2025-12-30 | **Last Amended**: 2025-12-30

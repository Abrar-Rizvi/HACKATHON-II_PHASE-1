# Tasks: Console Todo Application

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Phase I uses manual console testing only - no automated test tasks included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/` at repository root
- All Python modules in `src/` directory
- Paths shown below use absolute references from repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Verify Python 3.13+ installation and UV package manager availability
- [x] T002 [P] Create src/ directory in repository root
- [x] T003 [P] Initialize __init__.py file in src/ directory (if needed for imports)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task class in src/task.py with id, title, description, completed attributes
- [x] T005 Create TaskStorage class in src/storage.py with empty task list and next_id counter
- [x] T006 Implement add_task() method in src/storage.py (auto-assign ID, append to list)
- [x] T007 Implement find_task_by_id() method in src/storage.py (linear search, return Task or None)
- [x] T008 Implement get_all_tasks() method in src/storage.py (return copy of task list)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can add new tasks with title and description, and view all tasks in a formatted list

**Independent Test**: Launch app, add several tasks with different titles and descriptions, list all tasks, verify display shows IDs, titles, descriptions, and [TODO] status correctly

### Implementation for User Story 1

- [x] T009 [P] [US1] Create display_menu() function in src/ui.py (show 6 menu options)
- [x] T010 [P] [US1] Create get_menu_choice() function in src/ui.py (get integer 1-6, handle errors)
- [x] T011 [P] [US1] Create get_task_input() function in src/ui.py (prompt for title and description, validate title non-empty)
- [x] T012 [P] [US1] Create display_tasks() function in src/ui.py (format and print all tasks with ID, status, title, description)
- [x] T013 [P] [US1] Create display_success() function in src/ui.py (show success message with checkmark)
- [x] T014 [P] [US1] Create display_error() function in src/ui.py (show error message)
- [x] T015 [US1] Create add_task_flow() function in src/main.py (call ui.get_task_input, storage.add_task, ui.display_success)
- [x] T016 [US1] Create list_tasks_flow() function in src/main.py (call storage.get_all_tasks, ui.display_tasks)
- [x] T017 [US1] Create main_loop() function in src/main.py (display menu, get choice, dispatch to flows, loop until quit)
- [x] T018 [US1] Create main() entry point in src/main.py (initialize storage, call main_loop)
- [x] T019 [US1] Add if __name__ == "__main__" block in src/main.py to call main()

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Mark Tasks Complete (Priority: P2)

**Goal**: Users can mark tasks as complete or incomplete, toggling status between [TODO] and [DONE]

**Independent Test**: Add tasks using US1 functionality, mark specific tasks as complete by ID, list tasks to verify [DONE] status shows correctly, toggle back to [TODO] to verify bidirectional toggle works

### Implementation for User Story 2

- [x] T020 [US2] Implement toggle_completion() method in src/storage.py (find task by ID, flip completed boolean)
- [x] T021 [US2] Create get_task_id_input() function in src/ui.py (prompt for task ID, validate integer format)
- [x] T022 [US2] Update display_tasks() function in src/ui.py to show [DONE] for completed=True, [TODO] for completed=False
- [x] T023 [US2] Create toggle_task_flow() function in src/main.py (call ui.get_task_id_input, storage.toggle_completion, ui.display_success)
- [x] T024 [US2] Update main_loop() in src/main.py to handle menu option 3 (Mark Task Complete/Incomplete)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task Details (Priority: P3)

**Goal**: Users can update the title and/or description of existing tasks by task ID

**Independent Test**: Create tasks using US1, update their titles and descriptions using task IDs, list tasks to verify changes are reflected correctly, test partial updates (title only, description only)

### Implementation for User Story 3

- [x] T025 [US3] Implement update_task() method in src/storage.py (find task by ID, update title and/or description)
- [x] T026 [US3] Create get_task_update_input() function in src/ui.py (show current values, get new title/description, allow Enter to keep current)
- [x] T027 [US3] Create update_task_flow() function in src/main.py (get task ID, get updates, call storage.update_task, display success)
- [x] T028 [US3] Update main_loop() in src/main.py to handle menu option 4 (Update Task)

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Tasks (Priority: P4)

**Goal**: Users can delete tasks by ID, with IDs remaining stable (no renumbering)

**Independent Test**: Create several tasks using US1, delete specific tasks by ID, list tasks to verify deleted tasks don't appear, verify remaining task IDs are unchanged (stable IDs)

### Implementation for User Story 4

- [x] T029 [US4] Implement delete_task() method in src/storage.py (find task by ID, remove from list)
- [x] T030 [US4] Create delete_task_flow() function in src/main.py (get task ID, call storage.delete_task, display success)
- [x] T031 [US4] Update main_loop() in src/main.py to handle menu option 5 (Delete Task)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T032 [P] Add docstrings to all public functions in src/task.py
- [x] T033 [P] Add docstrings to all public functions in src/storage.py
- [x] T034 [P] Add docstrings to all public functions in src/ui.py
- [x] T035 [P] Add docstrings to all public functions in src/main.py
- [x] T036 [P] Verify PEP 8 compliance across all modules (check with linter if available)
- [x] T037 [P] Add graceful exit message when user selects option 6 (Quit)
- [x] T038 [P] Test edge case: empty task list display shows "No tasks found" message
- [x] T039 [P] Test edge case: invalid task ID shows clear error message
- [x] T040 [P] Test edge case: empty title validation shows clear error message
- [x] T041 [P] Update README.md with setup instructions (Python 3.13+, how to run)
- [ ] T042 Manual validation against quickstart.md testing checklist (22 items)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3 → P4)
- **Polish (Phase 7)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Extends US1 but is independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Extends US1 but is independently testable
- **User Story 4 (P4)**: Can start after Foundational (Phase 2) - Extends US1 but is independently testable

### Within Each User Story

**User Story 1 (Add and View Tasks)**:
1. UI functions (T009-T014) can be built in parallel - different functions
2. Main flows (T015-T016) depend on UI functions being complete
3. Main loop (T017-T019) depends on flows being complete

**User Story 2 (Mark Tasks Complete)**:
1. Storage method (T020) and UI functions (T021-T022) can be built in parallel
2. Flow (T023) depends on storage and UI being complete
3. Main loop update (T024) depends on flow being complete

**User Story 3 (Update Task Details)**:
1. Storage method (T025) and UI function (T026) can be built in parallel
2. Flow (T027) depends on storage and UI being complete
3. Main loop update (T028) depends on flow being complete

**User Story 4 (Delete Tasks)**:
1. Storage method (T029) can be built independently
2. Flow (T030) depends on storage being complete
3. Main loop update (T031) depends on flow being complete

### Parallel Opportunities

- All Setup tasks (Phase 1) can run in parallel (T001-T003)
- Foundational tasks (Phase 2) must run sequentially: T004 → T005-T008
- User Story 1 UI functions (T009-T014) can run in parallel - all marked [P]
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All Polish tasks marked [P] can run in parallel (T032-T041)

---

## Parallel Example: User Story 1

```bash
# Launch all UI functions for User Story 1 together:
Task: "Create display_menu() function in src/ui.py"
Task: "Create get_menu_choice() function in src/ui.py"
Task: "Create get_task_input() function in src/ui.py"
Task: "Create display_tasks() function in src/ui.py"
Task: "Create display_success() function in src/ui.py"
Task: "Create display_error() function in src/ui.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T003)
2. Complete Phase 2: Foundational (T004-T008) - CRITICAL, blocks all stories
3. Complete Phase 3: User Story 1 (T009-T019)
4. **STOP and VALIDATE**: Test User Story 1 independently
   - Add tasks with title and description
   - Add task with title only (empty description)
   - Try to add task with empty title (should error)
   - List all tasks and verify format
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 (T009-T019) → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 (T020-T024) → Test independently → Deploy/Demo
4. Add User Story 3 (T025-T028) → Test independently → Deploy/Demo
5. Add User Story 4 (T029-T031) → Test independently → Deploy/Demo
6. Add Polish (T032-T042) → Final validation → Production ready
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (T001-T008)
2. Once Foundational is done:
   - Developer A: User Story 1 (T009-T019)
   - Developer B: User Story 2 (T020-T024) - starts after US1 UI is built
   - Developer C: User Story 3 (T025-T028) - starts after US1 UI is built
   - Developer D: User Story 4 (T029-T031) - starts after US1 UI is built
3. Stories complete and integrate independently

**Note**: US2, US3, US4 can start once US1's UI functions (T009-T014) are complete, as they extend the same UI.

---

## Notes

- [P] tasks = different files/functions, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

## Task Count Summary

- **Total Tasks**: 42
- **Setup**: 3 tasks
- **Foundational**: 5 tasks
- **User Story 1**: 11 tasks
- **User Story 2**: 5 tasks
- **User Story 3**: 4 tasks
- **User Story 4**: 3 tasks
- **Polish**: 11 tasks

## Parallel Execution Opportunities

- **Phase 1**: All 3 tasks can run in parallel
- **Phase 3 (US1)**: 6 UI functions can run in parallel (T009-T014)
- **Phase 7**: All 10 documentation/testing tasks can run in parallel (T032-T041)
- **Total Parallelizable**: 19 tasks (45% of all tasks)

## Manual Testing Checklist (From quickstart.md)

After implementation, validate against these 22 acceptance criteria:

- [ ] Can add task with title and description
- [ ] Can add task with title only (empty description)
- [ ] Cannot add task with empty title (error shown)
- [ ] Can list all tasks showing ID, status, title, description
- [ ] Empty list shows "No tasks found" message
- [ ] Can mark task complete (status changes to [DONE])
- [ ] Can mark task incomplete (status changes back to [TODO])
- [ ] Marking non-existent task shows error
- [ ] Can update task title only
- [ ] Can update task description only
- [ ] Can update both title and description
- [ ] Cannot update to empty title (error shown)
- [ ] Can delete task by ID
- [ ] Deleted task doesn't appear in list
- [ ] Deleted task ID is not reused for new tasks
- [ ] Deleting non-existent task shows error
- [ ] Invalid menu choice shows error and re-prompts
- [ ] Option 6 quits gracefully with goodbye message
- [ ] All tasks lost after quitting (expected behavior)
- [ ] App handles 100+ tasks without slowdown
- [ ] List displays within 2 seconds for 100 tasks
- [ ] Special characters in title/description handled correctly

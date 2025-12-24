# Tasks: 12-Week Physical AI & Humanoid Robotics Course + Technical Book

**Input**: Design documents from `/specs/003-physical-ai-course/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md

**Tests**: The current feature specification does not explicitly request test tasks. Therefore, test tasks will not be generated.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create base project directories: `frontend/`, `backend/`, `tests/`
- [x] T002 Initialize Docusaurus project in `frontend/` by running `npx @docusaurus/init@latest website classic --typescript` within the `frontend/` directory.
- [x] T003 Initialize FastAPI project in `backend/` by creating a `main.py` and `requirements.txt` with `fastapi` and `uvicorn`.
- [x] T004 [P] Configure Python environment for `backend/`: Create `venv`, install `pip-tools`, `fastapi`, `uvicorn`, `qdrant-client`, `langchain`, `langchain-openai`, `openai`, `psycopg2-binary`, `python-dotenv`, `pydantic-settings`, `loguru`.
- [x] T005 [P] Configure JavaScript/TypeScript environment for `frontend/`: Install Node.js, npm/yarn, and Docusaurus dependencies including ChatKit UI framework.
- [x] T006 [P] Configure linting (ESLint, Black) and formatting (Prettier) tools: Add configuration files `.eslintrc.js`, `.prettierrc`, `pyproject.toml` for Black in `frontend/` and `backend/`.
- [x] T007 [P] Configure Context7 MCP server: Set up MCP server configuration for accessing OpenAI Agents SDK and ChatKit, store API keys securely in environment variables.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Setup Neon DB (PostgreSQL) instance: Create an account, provision a new database, retrieve connection string, and store securely in environment variables (e.g., `.env` in `backend/`).
- [x] T008 Configure database connection in `backend/src/db/database.py` using `SQLAlchemy` and `psycopg2-binary` for Neon DB.
- [x] T009 Setup Qdrant vector database instance: Create a Qdrant Cloud account, obtain API key and URL, store securely in environment variables (e.g., `.env` in `backend/`).
- [x] T010 Configure Qdrant client in `backend/src/db/qdrant_client.py` for textbook embeddings with collection schema for course content.
- [x] T011 Implement base API routing and middleware structure: Define `APIRouter` instances in `backend/src/api/v1/` and include them in `backend/src/main.py`. Add basic CORS middleware for Docusaurus integration.
- [x] T012 Configure logging (e.g., `loguru`) and error handling (e.g., custom `HTTPException` handlers) infrastructure for `backend/src/utils/`.
- [x] T013 Setup Context7 MCP server connection: Configure MCP client in `backend/src/services/context7_client.py` to access OpenAI Agents SDK and ChatKit.

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Acquire Foundational Knowledge (Priority: P1) 🎯 MVP

**Goal**: Student successfully grasps fundamental concepts of Embodied AI, robotics principles, and simulation environments, enabling them to build a strong theoretical base.

**Independent Test**: Can be fully tested by reviewing module quizzes and a short conceptual report. Delivers foundational understanding necessary for practical work.

### Implementation for User Story 1

- [x] T015 [P] [US1] Create Docusaurus structure for Module 1 in `frontend/src/docs/module1/` including `_category_.json`.
- [x] T016 [P] [US1] Draft content for Module 1, Chapter 1: Overview of Embodied AI and Physical Intelligence in `frontend/src/docs/module1/chapter1.md` (min 1500 words, include definitions, history, challenges, reactive vs deliberative AI, early robot examples).
- [x] T017 [P] [US1] Draft content for Module 1, Chapter 2: Robotics Fundamentals: Kinematics and Dynamics in `frontend/src/docs/module1/chapter2.md` (min 2000 words, include DOF, joint types, Jacobian, Euler-Lagrange, KUKA/ABB examples, 2-DOF arm kinematics, simple pendulum dynamics).
- [x] T018 [P] [US1] Draft content for Module 1, Chapter 3: Introduction to ROS 2: Architecture and Core Concepts in `frontend/src/docs/module1/chapter3.md` (min 1800 words, include ROS 2 nodes, topics, services, actions, DDS, QoS, rclpy/rclcpp, mobile robot example).
- [ ] T019 [P] [US1] Draft content for Module 1, Chapter 4: Gazebo Simulation for Robotics Development in `frontend/src/docs/module1/chapter4.md` (min 1800 words, include virtual environments, URDF/SDF, physics engines, plugins, custom URDF design, spawning in Gazebo).
- [ ] T020 [P] [US1] Draft content for Module 1, Chapter 5: Setting up Your Robotics Development Environment in `frontend/src/docs/module1/chapter5.md` (min 1200 words, include Linux, Python/C++, VS Code, Git, development environment concepts, toolchain overview, best practices).
- [ ] T021 [P] [US1] Draft content for Module 1, Chapter 6: Basic Robot Navigation with ROS 2 in `frontend/src/docs/module1/chapter6.md` (min 1500 words, include localization, SLAM, path planning, odometry, laser scan, occupancy grid, A* planner, TurtleBot example, navigation concepts).

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Develop Practical Robotics Skills (Priority: P1)

**Goal**: Student gains hands-on experience with control, perception, and planning using various tools and frameworks, translating theoretical knowledge into practical application.

**Independent Test**: Can be fully tested by evaluating lab assignments and smaller project deliverables. Delivers demonstrable skills in specific robotics sub-domains.

### Implementation for User Story 2

- [ ] T024 [P] [US2] Create Docusaurus structure for Module 2 in `frontend/src/docs/module2/` including `_category_.json`.
- [ ] T025 [P] [US2] Draft content for Module 2, Chapter 7: Motor Control Systems and Actuators in `frontend/src/docs/module2/chapter7.md` (min 1800 words, include motor types, drivers, PID control, joint-level control, servomotors, DC motors, encoders, bipedal robot joint control).
- [ ] T026 [P] [US2] Draft content for Module 2, Chapter 8: Robotic Perception: Vision and Depth Sensors in `frontend/src/docs/module2/chapter8.md` (min 2000 words, include camera principles, image processing, 3D perception, RGB-D sensors, point clouds, feature extraction, camera calibration, edge detection, point cloud visualization).
- [ ] T027 [P] [US2] Draft content for Module 2, Chapter 9: Advanced Planning and Decision Making in `frontend/src/docs/module2/chapter9.md` (min 1800 words, include task planning, motion planning, reinforcement learning basics, state-space search, RRT, FSMs, robot planning example).
- [ ] T028 [P] [US2] Draft content for Module 2, Chapter 10: NVIDIA Isaac Sim: High-Fidelity Simulation in `frontend/src/docs/module2/chapter10.md` (min 2000 words, include Isaac Sim architecture, Omniverse, USD, PhysX, RTX rendering, ROS 2 bridge concepts, robot manipulation policy training concepts, asset import workflows, scene creation, ROS 2 control integration patterns).
- [ ] T029 [P] [US2] Draft content for Module 2, Chapter 11: Whole-Body Control for Complex Robots in `frontend/src/docs/module2/chapter11.md` (min 1800 words, include control strategies, inverse dynamics, operational space control, torque/impedance/compliance/null-space control, humanoid balance example, control theory).
- [ ] T030 [P] [US2] Draft content for Module 2, Chapter 12: Locomotion for Mobile and Humanoid Robots in `frontend/src/docs/module2/chapter12.md` (min 1800 words, include wheeled/legged/aerial locomotion, gait generation, ZMP, centroidal dynamics, footstep planning, Digit/Unitree examples, locomotion theory).


**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Build Advanced Robotics Systems (Priority: P2)

**Goal**: Student applies advanced topics like reinforcement learning, RAG agents, and human-robot interaction to design, implement, and evaluate a comprehensive capstone project.

**Independent Test**: Can be fully tested by evaluating the capstone project's design, implementation, and demonstration. Delivers a tangible, complex robotics solution.

### Implementation for User Story 3

- [ ] T034 [P] [US3] Create Docusaurus structure for Module 3 in `frontend/src/docs/module3/` including `_category_.json`.
- [ ] T035 [P] [US3] Draft content for Module 3, Chapter 13: Robotics Agents with Retrieval Augmented Generation (RAG) in `frontend/src/docs/module3/chapter13.md` (min 2000 words, include LLMs, vector databases, prompt engineering, semantic search, robot assistant examples).
- [ ] T036 [P] [US3] Draft content for Module 3, Chapter 14: Humanoid Robotics: Leading Platforms and Future Trends in `frontend/src/docs/module3/chapter14.md` (min 2000 words, include Optimus, Digit, Unitree G1 architectures, actuation, sensing, control hierarchies, ethical considerations, comparative analysis).
- [ ] T037 [P] [US3] Draft content for Module 3, Chapter 15: Human-Robot Interaction (HRI): Principles and Design in `frontend/src/docs/module3/chapter15.md` (min 1800 words, include safe/natural interaction, human factors, gesture/voice command concepts, affective computing, shared autonomy, HRI design principles).
- [ ] T038 [P] [US3] Draft content for Module 3, Chapter 16: Reinforcement Learning for Complex Robotics Tasks in `frontend/src/docs/module3/chapter16.md` (min 2000 words, include PPO, SAC, reward function design, sim-to-real, MDPs, policy gradients, robot grasping example, RL theory).
- [ ] T039 [P] [US3] Draft content for Module 3, Chapter 17: Cloud Robotics: Distributed Systems and AI at Scale in `frontend/src/docs/module3/chapter17.md` (min 1800 words, include cloud platforms, ROS in cloud, microservices, fleet management, cloud data analytics, architecture patterns).
- [ ] T040 [P] [US3] Draft content for Module 3, Chapter 18: Edge Deployment and Real-World Robotics in `frontend/src/docs/module3/chapter18.md` (min 1800 words, include edge devices, NVIDIA Jetson, TensorFlow Lite, OpenVINO, power efficiency, real-time inference, deployment strategies).
- [x] T041 [US3] Implement content ingestion pipeline: Create script in `backend/src/utils/ingest.py` to load course content from markdown files, chunk text intelligently (preserving chapter/section context), generate embeddings using OpenAI API, and upload to Qdrant vector database with metadata (chapter, section, page).
- [x] T042 [US3] Implement RAG service with OpenAI Agents SDK: Create `backend/src/services/rag_service.py` using Context7 MCP to access OpenAI Agents SDK, implement semantic search against Qdrant, generate responses with source citations, handle conversation context.
- [ ] T043 [US3] Create FastAPI chatbot endpoints: Implement endpoints in `backend/src/api/v1/chatbot.py` for:
  - POST `/api/v1/chat/query` - Process user questions
  - POST `/api/v1/chat/query-highlighted` - Process questions with highlighted text context
  - GET `/api/v1/chat/history/{session_id}` - Retrieve conversation history
  - DELETE `/api/v1/chat/clear/{session_id}` - Clear conversation context
- [ ] T044 [US3] Integrate ChatKit UI in Docusaurus: Create React component in `frontend/src/components/Chatbot/` using ChatKit framework (accessed via Context7 MCP), implement chat interface with message history, typing indicators, and error handling.
- [ ] T045 [US3] Implement text highlighting feature: Add JavaScript functionality in `frontend/src/components/TextHighlight/` to:
  - Detect text selection on course content pages
  - Display "Ask about this" button on text selection
  - Send highlighted text as context to chatbot API
  - Highlight relevant sections when chatbot cites sources
- [ ] T046 [US3] Embed chatbot in Docusaurus: Integrate chatbot component into `frontend/docusaurus.config.js` and `frontend/src/theme/Root.js` to make it available on all course pages with persistent state.
- [ ] T047 [US3] Implement conversation context management: Create session management in `backend/src/services/session_service.py` to maintain conversation history, track user queries, and provide contextually relevant responses across multiple interactions.

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T048 Finalize Capstone Project Specification and Evaluation Rubric in `specs/003-physical-ai-course/capstone_spec.md` and `specs/003-physical-ai-course/evaluation_rubric.md`.
- [ ] T049 [P] Implement user progress tracking features in `backend/src/services/user_progress_service.py` and `frontend/src/components/UserProgress/` based on chapter completion and quiz scores.
- [ ] T050 [P] Implement multilingual translation (Urdu) for Docusaurus frontend: Integrate `docusaurus-plugin-content-docs` i18n features and add Urdu translation files in `frontend/i18n/ur/`.
- [ ] T051 [P] Test and optimize RAG chatbot: Evaluate response quality, accuracy, latency, and source citation correctness. Optimize embedding strategy and retrieval parameters.
- [ ] T052 Comprehensive review of all textbook content for accuracy, clarity, and completeness in `frontend/src/docs/`.
- [ ] T053 Code cleanup, refactoring, and performance optimization across `frontend/` and `backend/` directories.
- [ ] T054 Update Future of Physical AI (2030 predictions) in `specs/003-physical-ai-course/spec.md` by expanding on each prediction with current research and potential impact.

---

## Dependencies & Execution Order

### Phase Dependencies

-   **Setup (Phase 1)**: No dependencies - can start immediately
-   **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
-   **User Stories (Phase 3+)**: All depend on Foundational phase completion
    -   User stories can then proceed in parallel (if staffed)
    -   Or sequentially in priority order (P1 → P2 → P3)
-   **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

-   **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
-   **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
-   **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

-   Models before services
-   Services before endpoints
-   Core implementation before integration
-   Story complete before moving to next priority

### Parallel Opportunities

-   All Setup tasks marked [P] can run in parallel
-   All Foundational tasks marked [P] can run in parallel (within Phase 2)
-   Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
-   Models within a story marked [P] can run in parallel
-   Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all Docusaurus content drafting tasks for User Story 1 together:
Task: "Draft content for Module 1, Chapter 1: Overview of Embodied AI and Physical Intelligence in frontend/src/docs/module1/chapter1.md"
Task: "Draft content for Module 1, Chapter 2: Robotics Fundamentals: Kinematics and Dynamics in frontend/src/docs/module1/chapter2.md"
Task: "Draft content for Module 1, Chapter 3: Introduction to ROS 2: Architecture and Core Concepts in frontend/src/docs/module1/chapter3.md"
Task: "Draft content for Module 1, Chapter 4: Gazebo Simulation for Robotics Development in frontend/src/docs/module1/chapter4.md"
Task: "Draft content for Module 1, Chapter 5: Setting up Your Robotics Development Environment in frontend/src/docs/module1/chapter5.md"
Task: "Draft content for Module 1, Chapter 6: Basic Robot Navigation with ROS 2 in frontend/src/docs/module1/chapter6.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  Add User Story 3 → Test independently → Deploy/Demo
5.  Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: User Story 1
    -   Developer B: User Story 2
    -   Developer C: User Story 3
3.  Stories complete and integrate independently

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
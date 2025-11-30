# Data Model: 12-Week Physical AI & Humanoid Robotics Course & Technical Book

This document outlines the key data entities and their relationships for the course and learning platform, primarily targeting storage in Neon DB (PostgreSQL).

## Entities & Relationships

### 1. User
*   **Description**: Represents a student or user of the learning platform.
*   **Fields**:
    *   `user_id` (UUID, PK): Unique identifier for the user.
    *   `username` (VARCHAR, UNIQUE): User's chosen username.
    *   `email` (VARCHAR, UNIQUE): User's email address.
    *   `password_hash` (VARCHAR): Hashed password for authentication.
    *   `created_at` (TIMESTAMPTZ): Timestamp of user creation.
    *   `last_login` (TIMESTAMPTZ): Timestamp of last login.
    *   `profile_data` (JSONB, Optional): Stores personalization preferences (e.g., learning style, background - beginner, intermediate, advanced, preferred language).
*   **Relationships**: One-to-many with `CourseEnrollment`.

### 2. Course
*   **Description**: Defines the overall 12-week Physical AI & Humanoid Robotics program.
*   **Fields**:
    *   `course_id` (UUID, PK): Unique identifier for the course.
    *   `title` (VARCHAR): Title of the course.
    *   `description` (TEXT): Detailed description of the course.
    *   `duration_weeks` (INTEGER): Number of weeks for the course (e.g., 12).
    *   `created_at` (TIMESTAMPTZ): Timestamp of course creation.
    *   `updated_at` (TIMESTAMPTZ): Timestamp of last update.
*   **Relationships**: One-to-many with `Module`.

### 3. Module
*   **Description**: A thematic unit within a `Course`.
*   **Fields**:
    *   `module_id` (UUID, PK): Unique identifier for the module.
    *   `course_id` (UUID, FK): Foreign key referencing `Course`.
    *   `module_number` (INTEGER): Order of the module within the course.
    *   `title` (VARCHAR): Title of the module.
    *   `description` (TEXT): Overview of the module.
*   **Relationships**: Many-to-one with `Course`, One-to-many with `Chapter`.

### 4. Chapter
*   **Description**: A specific topic or section within a `Module`.
*   **Fields**:
    *   `chapter_id` (UUID, PK): Unique identifier for the chapter.
    *   `module_id` (UUID, FK): Foreign key referencing `Module`.
    *   `chapter_number` (INTEGER): Order of the chapter within the module.
    *   `title` (VARCHAR): Title of the chapter.
    *   `overview` (TEXT): Chapter overview.
    *   `key_concepts` (TEXT): Summary of key concepts.
    *   `robotics_examples` (TEXT): Real robotics examples (can be structured JSONB).
    *   `hands_on_tasks` (TEXT): Description of hands-on tasks (can be structured JSONB).
    *   `expected_output` (TEXT): Description of expected output for tasks (can be structured JSONB).
    *   `content_path` (VARCHAR): Path to the Docusaurus markdown file for this chapter.
*   **Relationships**: Many-to-one with `Module`, One-to-many with `LabAssignment` (if labs are chapter-specific).

### 5. LabAssignment
*   **Description**: Practical exercises or assignments associated with a `Chapter` or `Module`.
*   **Fields**:
    *   `assignment_id` (UUID, PK): Unique identifier for the assignment.
    *   `chapter_id` (UUID, FK, Optional): Foreign key referencing `Chapter`.
    *   `module_id` (UUID, FK, Optional): Foreign key referencing `Module` (if module-wide).
    *   `title` (VARCHAR): Title of the lab/assignment.
    *   `description` (TEXT): Full description of the lab/assignment.
    *   `type` (VARCHAR): e.g., 'lab', 'quiz', 'project'.
    *   `due_date` (TIMESTAMPTZ, Optional): Due date for the assignment.
    *   `resources` (JSONB, Optional): Links to external resources, code templates, tools.
*   **Relationships**: Many-to-one with `Chapter` or `Module`.

### 6. CourseEnrollment
*   **Description**: Tracks a `User`'s enrollment in a `Course`.
*   **Fields**:
    *   `enrollment_id` (UUID, PK): Unique identifier for enrollment.
    *   `user_id` (UUID, FK): Foreign key referencing `User`.
    *   `course_id` (UUID, FK): Foreign key referencing `Course`.
    *   `enrollment_date` (TIMESTAMPTZ): Date of enrollment.
    *   `completion_status` (VARCHAR): e.g., 'in_progress', 'completed', 'dropped'.
    *   `progress_data` (JSONB, Optional): Tracks chapter completion, lab scores, etc.
*   **Relationships**: Many-to-one with `User`, Many-to-one with `Course`.

### 7. UserSubmission
*   **Description**: Stores submissions for `LabAssignment`.
*   **Fields**:
    *   `submission_id` (UUID, PK): Unique identifier for the submission.
    *   `assignment_id` (UUID, FK): Foreign key referencing `LabAssignment`.
    *   `user_id` (UUID, FK): Foreign key referencing `User`.
    *   `submission_content` (TEXT): Submitted code, report, etc.
    *   `submitted_at` (TIMESTAMPTZ): Timestamp of submission.
    *   `grade` (INTEGER, Optional): Score for the submission.
    *   `feedback` (TEXT, Optional): Instructor feedback.
*   **Relationships**: Many-to-one with `LabAssignment`, Many-to-one with `User`.

### 8. VectorEmbeddings (Conceptual, stored in Qdrant)
*   **Description**: Conceptual entity representing vectorized textbook content for RAG.
*   **Fields**:
    *   `vector` (ARRAY of FLOAT): High-dimensional embedding of a text chunk.
    *   `text_content` (TEXT): Original text chunk.
    *   `metadata` (JSONB): Chapter ID, module ID, page range, section title, etc.
*   **Storage**: Qdrant (vector database).

## Validation Rules & State Transitions

*   **User Registration**: Email and username must be unique. Passwords must meet complexity requirements (handled by application logic).
*   **Course Progress**: `completion_status` in `CourseEnrollment` can transition from 'in_progress' to 'completed' only when all required `LabAssignment`s for the course are marked as complete or graded.
*   **Assignment Submission**: A user can submit multiple times, but only the latest (or highest-graded) submission is considered active, depending on policy. Submissions are linked to specific `LabAssignment` and `User`.

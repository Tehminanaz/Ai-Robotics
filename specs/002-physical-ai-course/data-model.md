# Data Model

## Entities

### User
- **Description**: Represents a student interacting with the platform.
- **Attributes**:
    - `id`: Unique identifier (Primary Key)
    - `email`: User's email (for email/password auth)
    - `github_id`: GitHub user ID (for GitHub auth)
    - `username`: Display name
    - `personalization_background`: User's background (e.g., beginner, intermediate, advanced)
    - `personalization_learning_style`: Preferred learning style
    - `course_progress`: JSONB or similar for tracking progress (e.g., `{'module1': {'chapter1': 'completed'}}`)
    - `created_at`: Timestamp of user creation
    - `updated_at`: Timestamp of last update

### Course Content
- **Description**: Structured educational material for the Physical AI course.
- **Structure**: Modules -> Parts -> Chapters -> Sections
- **Attributes**:
    - `id`: Unique identifier (Primary Key)
    - `type`: (e.g., 'module', 'part', 'chapter', 'section')
    - `title`: Title of the content unit
    - `slug`: URL-friendly identifier
    - `text_content`: Markdown content of the unit
    - `code_examples`: List of code snippets (if any)
    - `learning_objectives`: List of associated learning objectives
    - `module_id`: Foreign Key to Module (if type is part/chapter/section)
    - `parent_id`: Foreign Key to parent content unit (e.g., chapter's parent is a part)
    - `order`: Display order within its parent
    - `qdrant_embedding_id`: Reference to the vector embedding in Qdrant

### Chat Interaction
- **Description**: Represents a user's query to the RAG chatbot and the corresponding AI-generated response.
- **Attributes**:
    - `id`: Unique identifier (Primary Key)
    - `user_id`: Foreign Key to User
    - `query_text`: The user's input question
    - `response_text`: The AI-generated answer
    - `context_used`: List of `qdrant_embedding_id` or similar references to course content used for RAG
    - `timestamp`: Timestamp of the interaction
    - `language`: Language of the interaction (e.g., 'en', 'ur')

## Relationships
- `User` has many `Chat Interactions`
- `Course Content` is indexed in `Qdrant` (implicit relationship through `qdrant_embedding_id`)
- `Chat Interaction` references `Course Content` through `context_used`
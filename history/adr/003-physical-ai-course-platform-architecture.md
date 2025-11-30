# ADR-003: physical-ai-course Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-11-30
- **Feature:** physical-ai-course
- **Context:** The project aims to develop a Docusaurus-based interactive textbook for Physical AI & Humanoid Robotics, integrated with an AI-native RAG chatbot, personalization, and multilingual support. This ADR documents the high-level architectural decisions for the entire platform, encompassing frontend, backend, AI, and simulation components.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The platform architecture is comprised of:
*   **Frontend**: Docusaurus (for static content) with React for dynamic UI and interactive elements.
*   **Backend**: FastAPI for the core API gateway, handling chatbot, personalization, and translation logic.
*   **Databases**: Neon DB (PostgreSQL) for structured user data and Qdrant for vector embeddings of textbook content (RAG).
*   **AI Integration**: OpenAI APIs (LLM, Whisper) for chatbot intelligence and voice-to-text; Claude Code SDK for subagents/skills.
<!-- *   **Simulation & Robotics**: ROS 2 for robot communication, Gazebo/Unity for digital twin environments, NVIDIA Isaac Sim/Isaac ROS for advanced simulation, synthetic data, perception, and Nav2 for navigation. -->
*   **Multilingual Support**: Frontend-driven Urdu translation using localization libraries.
*   **User Personalization**: User background and progress data stored in Neon DB, influencing content depth and learning paths.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

*   Leverages well-established open-source (Docusaurus, FastAPI, ROS 2) and industry-leading (OpenAI, Unity) technologies.
*   Provides a robust, scalable foundation for an AI-native learning platform.
*   Enables rich interactive content and intelligent learning support.
*   Facilitates community contributions with an open-source license.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

*   High integration complexity across diverse technologies.
*   Steep learning curve for developers unfamiliar with all chosen frameworks.
*   Potential for vendor lock-in with proprietary AI/simulation platforms (OpenAI,).
*   Resource-intensive for development and simulation environments.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

*   **Alternative Frontend Frameworks**: Next.js, Gatsby.
    *   *Tradeoffs*: Docusaurus chosen for its strength in documentation-as-code and static site generation, which is ideal for a textbook. Alternatives offer more general-purpose web development capabilities but might require more setup for documentation features.
*   **Alternative Backend Frameworks**: Django, Node.js (Express/NestJS).
    *   *Tradeoffs*: FastAPI chosen for its high performance, ease of use for API development, and strong Python ecosystem integration, which aligns well with robotics and AI development. Alternatives are robust but might introduce more overhead or different language ecosystems.
*   **Alternative Vector Databases**: Pinecone, Milvus.
    *   *Tradeoffs*: Qdrant chosen for its balance of features, performance, and scalability, and open-source nature. Alternatives have similar capabilities but might differ in deployment options or community support.
*   **Alternative Simulation Platforms**: Webots, V-REP.
    *   *Tradeoffs*: Gazebo, Unity, and NVIDIA Isaac Sim chosen for their industry prominence, feature sets (physics, rendering, synthetic data), and ROS 2 integration. Alternatives might offer different levels of fidelity or specific domain strengths but less comprehensive feature sets for this project's scope.

## References

- Feature Spec: specs/003-physical-ai-course/spec.md
- Implementation Plan: specs/003-physical-ai-course/plan.md
- Related ADRs: null
- Evaluator Evidence: history/prompts/002-physical-ai-course/003-physical-ai-course-plan.plan.prompt.md

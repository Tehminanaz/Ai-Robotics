---
id: 1
title: Generate Robotics Course Spec
stage: spec
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: 003-physical-ai-course
branch: 003-physical-ai-course
user: user
command: /sp.specify
labels: ["specification","robotics","course","book","AI","rag-chatbot"]
links:
  spec: specs/003-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/003-physical-ai-course/spec.md
- specs/003-physical-ai-course/checklists/requirements.md
tests:
null
---

## Prompt

```text
@frontend\ Write a complete **12-Week Physical AI & Humanoid Robotics Course + Technical Book**, using a well-structured academic format.

### OUTPUT REQUIREMENTS
Structure the response in the following hierarchy:

1. **Title**
2. **Book Abstract**
3. **Target Audience**
4. **Learning Outcomes**
5. **Real Industry Use Cases**
6. **12-Week Course Roadmap (Table Format)**
   - Week
   - Topics
   - Labs & Assignments (Conceptual/Design focused)
   - Tools & Frameworks (Documentation/Study focused)
   - Deliverables
7. **Module & Chapter Breakdown**
   - Module Name
   - Chapters list (minimum 6 per module)
   - Each chapter must include:
     - Overview
     - Key Concepts
     - Real Robotics Examples
     - Hands-on Tasks (Analysis/Design/RAG Implementation)
     - Expected Output

### Core Topics Required
- Embodied AI & Physical Intelligence
- ROS 2 & Gazebo Simulation (Conceptual & Architecture)
- NVIDIA Isaac Sim (High-Fidelity Simulation Concepts)
- Whole-Body Control & Locomotion (Theory)
- Motor Control, Perception & Planning (Design)
- **RAG + Robotics Agents (Implementation Focus)**:
  - OpenAI Agents SDK via Context7 MCP
  - ChatKit UI Integration
  - Text Highlighting & Contextual Queries
- Humanoid Robotics (Optimus, Digit, Unitree G1 - Analysis)
- Human-Robot Interaction
- Reinforcement Learning for Robotics (Theory)
- Cloud Robotics & Edge Deployment (Architecture)

### Final Outcomes
- Capstone Project Specification (Design & Architecture)
- Evaluation Rubric
- Tools/Stack:
  - **Platform**: Docusaurus (TypeScript/React)
  - **Backend**: FastAPI (Python)
  - **AI/RAG**: OpenAI Agents SDK, Context7 MCP, ChatKit, Qdrant, LangChain
  - **Database**: Neon DB (PostgreSQL)
  - **Robotics**: ROS 2, Isaac Sim (Conceptual Study)
- Future of Physical AI (2030 predictions)

Write the full structure in a clean formatted style. Do not write prose paragraphs—write structured content only.
```

## Response snapshot

The specification for the "12-Week Physical AI & Humanoid Robotics Course + Technical Book" has been successfully created and validated.

**Feature Branch**: `003-physical-ai-course`
**Specification File**: `specs/003-physical-ai-course/spec.md`
**Checklist File**: `specs/003-physical-ai-course/checklists/requirements.md`

All checklist items have passed, and there are no pending clarifications. This feature is now ready for the planning phase. You can proceed with `/sp.plan`.

## Outcome

- ✅ Impact: Created a detailed specification for the robotics course and technical book, focusing on educational content and RAG chatbot.
- 🧪 Tests: Specification validated against checklist; no [NEEDS CLARIFICATION] markers.
- 📁 Files: Two files created: spec.md and requirements.md.
- 🔁 Next prompts: `/sp.plan`
- 🧠 Reflection: Successfully generated a comprehensive spec based on user requirements. Refined scope to remove hardware dependencies and focus on RAG implementation.

## Evaluation notes (flywheel)

- Failure modes observed: None observed in agent logic.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null

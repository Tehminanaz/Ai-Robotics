---
id: 1
title: Created Robotics Course Book Spec
stage: spec
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: 003-physical-ai-course
branch: 003-physical-ai-course
user: unknown
command: /sp.specify
labels: ["specification", "course-design", "robotics", "rag-chatbot"]
links:
  spec: specs/003-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/003-physical-ai-course/spec.md
- specs/003-physical-ai-course/checklists/requirements.md
tests:
- Spec validation checklist passed
---

## Prompt

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

## Response snapshot

The specification for the '12-Week Physical AI & Humanoid Robotics Course & Technical Book' has been successfully created and validated. The feature is now ready for the next phase: planning. You can run `/sp.plan` to generate the implementation plan.

## Outcome

- ✅ Impact: Spec created and validated, ready for planning.
- 🧪 Tests: Spec validation checklist passed.
- 📁 Files: `specs/003-physical-ai-course/spec.md` and `specs/003-physical-ai-course/checklists/requirements.md` created/updated.
- 🔁 Next prompts: `/sp.plan`
- 🧠 Reflection: Successfully created and validated the feature specification, refining scope to focus on educational content and RAG chatbot implementation while removing hardware dependencies.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): null

---
id: 001
title: Physical AI Course Specification
stage: spec
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: physical-ai-course
branch: 003-physical-ai-course
user: user
command: /sp.specify Write a complete **12-Week Physical AI & Humanoid Robotics Course + Technical Book**, using a well-structured academic format.

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
   - Labs & Assignments
   - Tools & Frameworks
   - Deliverables
7. **Module & Chapter Breakdown**
   - Module Name
   - Chapters list (minimum 6 per module)
   - Each chapter must include:
     - Overview
     - Key Concepts
     - Real Robotics Examples
     - Hands-on Tasks
     - Expected Output

### Core Topics Required
- Embodied AI & Physical Intelligence
- ROS 2 & Gazebo Simulation
- NVIDIA Isaac Sim
- Whole-Body Control & Locomotion
- Motor Control, Perception & Planning
- RAG + Robotics Agents
- Humanoid Robotics (Optimus, Digit, Unitree G1)
- Human-Robot Interaction
- Reinforcement Learning for Robotics
- Cloud Robotics & Edge Deployment

### Final Outcomes
- Capstone Project Specification
- Evaluation Rubric
- Tools/Stack (ROS2, Isaac, Python, FastAPI, NVidia Jetson, Unitree)
- Future of Physical AI (2030 predictions)

Write the full structure in a clean formatted style. Do not write prose paragraphs—write structured content only.
labels: [spec, course, robotics, physical-ai, humanoid]
links:
  spec: specs/003-physical-ai-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/003-physical-ai-course/spec.md
- specs/003-physical-ai-course/checklists/requirements.md
tests: null
---

## Prompt

Write a complete **12-Week Physical AI & Humanoid Robotics Course + Technical Book**, using a well-structured academic format.

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
   - Labs & Assignments
   - Tools & Frameworks
   - Deliverables
7. **Module & Chapter Breakdown**
   - Module Name
   - Chapters list (minimum 6 per module)
   - Each chapter must include:
     - Overview
     - Key Concepts
     - Real Robotics Examples
     - Hands-on Tasks
     - Expected Output

### Core Topics Required
- Embodied AI & Physical Intelligence
- ROS 2 & Gazebo Simulation
- NVIDIA Isaac Sim
- Whole-Body Control & Locomotion
- Motor Control, Perception & Planning
- RAG + Robotics Agents
- Humanoid Robotics (Optimus, Digit, Unitree G1)
- Human-Robot Interaction
- Reinforcement Learning for Robotics
- Cloud Robotics & Edge Deployment

### Final Outcomes
- Capstone Project Specification
- Evaluation Rubric
- Tools/Stack (ROS2, Isaac, Python, FastAPI, NVidia Jetson, Unitree)
- Future of Physical AI (2030 predictions)

Write the full structure in a clean formatted style. Do not write prose paragraphs—write structured content only.

## Response snapshot

The feature specification for the "12-Week Physical AI & Humanoid Robotics Course + Technical Book" has been successfully created and validated.

Branch Name: `003-physical-ai-course`
Spec File Path: `specs/003-physical-ai-course/spec.md`
Checklist File Path: `specs/003-physical-ai-course/checklists/requirements.md`

All items in the specification quality checklist have passed. The feature is ready for the next phase, which is `/sp.plan`.

## Outcome

- ✅ Impact: Feature specification created successfully.
- 🧪 Tests: Specification validated against quality checklist; all items passed.
- 📁 Files: Created spec.md and requirements.md checklist.
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Successfully generated feature specification and checklist following manual steps due to script execution issues. Ensured all required sections and output formats were met.

## Evaluation notes (flywheel)

- Failure modes observed: Script execution for create-new-feature.ps1 and create-phr.sh failed due to environment issues (pwsh/bash not found). Manual steps were performed.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment: Investigate environment setup for executing powershell/bash scripts directly.
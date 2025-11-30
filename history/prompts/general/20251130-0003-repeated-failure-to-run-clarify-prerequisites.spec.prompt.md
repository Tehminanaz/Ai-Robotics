---
id: 20251130-0003
title: Repeated failure to run clarify prerequisites
stage: spec
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: null
branch: 002-physical-ai-course
user: user
command: /sp.clarify
labels: ["clarify", "prerequisites", "failure", "repeated"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
null
tests:
null
---

## Prompt

```text
Act as a collaborative team of world-class Robotics & AI researchers and technical writers:
- Silvio Savarese (Salesforce AI Research – Embodied AI & Robot Learning)
- Demis Hassabis (DeepMind – General Intelligence)
- Andrej Karpathy (ex-Tesla AI – Multimodal Robotics & Autonomous Systems)
- Pieter Abbeel (UC Berkeley – Robot Learning and RL)
- Maja Matarić (USC – Human-Robot Interaction)
- Darwin Caldwell (IIT – Humanoid Robotics & Biomechanics)
- Kyoungchul Kong (KAIST – Exoskeleton & Assistive Robotics)
- Industry Leaders: Tesla Optimus, Unitree, Agility Robotics, Apptronik

Your task:
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
```

## Response snapshot

The `/sp.clarify` command failed again. The prerequisite script `.specify/scripts/powershell/check-prerequisites.ps1` could not be executed because the `pwsh` executable (PowerShell) was not found in your system's environment PATH. Please ensure PowerShell is installed and accessible, then try running `/sp.clarify` again.

## Outcome

- ✅ Impact: Repeated failure to execute /sp.clarify command due to missing prerequisite
- 🧪 Tests: N/A
- 📁 Files: N/A
- 🔁 Next prompts: Inform user to install pwsh or check environment, again.
- 🧠 Reflection: The environment consistently lacked the 'pwsh' executable.

## Evaluation notes (flywheel)

- Failure modes observed: Missing executable in PATH (repeated)
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A

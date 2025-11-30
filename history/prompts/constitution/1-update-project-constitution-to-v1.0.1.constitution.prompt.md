---
id: 1
title: Update project constitution to v1.0.1
stage: constitution
date: 2025-11-29
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-physical-ai-course
user: Kashan
command: /sp.constitution
labels: [constitution, update]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - null
---

## Prompt

In `physical-ai-book`, create a file named `project-spec.md`.
Populate it with a detailed technical specification for a Docusaurus website integrated with a FastAPI backend.

The project must include:
1. **Frontend:** Docusaurus for rendering a 12-week course on Physical AI, ROS 2, Gazebo, and NVIDIA Isaac.
2. **Backend:** FastAPI for handling RAG chat requests and User Auth.
3. **Database:** Neon Postgres for user data, Qdrant for vector embeddings.
4. **Auth:** Better-Auth for handling GitHub/Email signups.
5. **Content:** 4 Modules: (1) Robotic Nervous System/ROS2, (2) Digital Twin/Gazebo, (3) AI-Robot Brain/NVIDIA Isaac, (4) Vision-Language-Action.
6. **Features:** A floating RAG chatbot, a "Personalize" button at the start of chapters, and an "Urdu Translation" button.

Use the course syllabus details I provide here to flesh out the content structure in the spec:
The future of AI extends beyond digital spaces into the physical world. This capstone quarter introduces Physical AI—AI systems that function in reality and comprehend physical laws. Students learn to design, simulate, and deploy humanoid robots capable of natural human interactions using ROS 2, Gazebo, and NVIDIA Isaac.
Module 1: The Robotic Nervous System (ROS 2)
Focus: Middleware for robot control.
ROS 2 Nodes, Topics, and Services.
Bridging Python Agents to ROS controllers using rclpy.
Understanding URDF (Unified Robot Description Format) for humanoids.


Module 2: The Digital Twin (Gazebo & Unity)
Focus: Physics simulation and environment building.
Simulating physics, gravity, and collisions in Gazebo.
High-fidelity rendering and human-robot interaction in Unity.
Simulating sensors: LiDAR, Depth Cameras, and IMUs.


Module 3: The AI-Robot Brain (NVIDIA Isaac™)
Focus: Advanced perception and training.
NVIDIA Isaac Sim: Photorealistic simulation and synthetic data generation.
Isaac ROS: Hardware-accelerated VSLAM (Visual SLAM) and navigation.
Nav2: Path planning for bipedal humanoid movement.


Module 4: Vision-Language-Action (VLA)
Focus: The convergence of LLMs and Robotics.
Voice-to-Action: Using OpenAI Whisper for voice commands.
Cognitive Planning: Using LLMs to translate natural language ("Clean the room") into a sequence of ROS 2 actions.
Capstone Project: The Autonomous Humanoid. A final project where a simulated robot receives a voice command, plans a path, navigates obcles, identifies an object using computer vision, and manipulates it.

Why Physical AI Matters
Humanoid robots are poised to excel in our human-centered world because they share our physical form and can be trained with abundant data from interacting in human environments. This represents a significant transition from AI models confined to digital environments to embodied intelligence that operates in physical space.
Learning Outcomes
Understand Physical AI principles and embodied intelligence
Master ROS 2 (Robot Operating System) for robotic control
Simulate robots with Gazebo and Unity
Develop with NVIDIA Isaac AI robot platform
Design humanoid robots for natural interactions
Integrate GPT models for conversational robotics
Weekly Breakdown
Weeks 1-2: Introduction to Physical AI
Foundations of Physical AI and embodied intelligence
From digital AI to robots that understand physical laws
Overview of humanoid robotics landscape
Sensor systems: LIDAR, cameras, IMUs, force/torque sensors
Weeks 3-5: ROS 2 Fundamentals
ROS 2 architecture and core concepts
Nodes, topics, services, and actions
Building ROS 2 packages with Python
Launch files and parameter management
Weeks 6-7: Robot Simulation with Gazebo
Gazebo simulation environment setup
URDF and SDF robot description formats
Physics simulation and sensor simulation
Introduction to Unity for robot visualization
Weeks 8-10: NVIDIA Isaac Platform
NVIDIA Isaac SDK and Isaac Sim
AI-powered perception and manipulation
Reinforcement learning for robot control
Sim-to-real transfer techniques
Weeks 11-12: Humanoid Robot Development
Humanoid robot kinematics and dynamics
Bipedal locomotion and balance control
Manipulation and grasping with humanoid hands
Natural human-robot interaction design

Week 13: Conversational Robotics
Integrating GPT models for conversational AI in robots
Speech recognition and natural language understanding
Multi-modal interaction: speech, gesture, vision
Assessments
ROS 2 package development project
Gazebo simulation implementation
Isaac-based perception pipeline
Capstone: Simulated humanoid robot with conversational AI

 Book Hierarchy Structure (Modules → Parts → Chapters → Sections)

sta

## Response snapshot

Updated the project constitution to version 1.0.1. The constitution file `.specify/memory/constitution.md` has been modified to reflect this patch version bump and the `Sync Impact Report` has been updated.

## Outcome

- ✅ Impact: The project constitution has been updated with a patch version increment, reflecting minor non-breaking changes and clarifications.
- 🧪 Tests: No explicit tests were run as this was a documentation update. The updated constitution was validated against consistency rules.
- 📁 Files: One file was modified: `.specify/memory/constitution.md`.
- 🔁 Next prompts: The user can now proceed with the original `/sp.specify` command to create the feature specification for the Physical AI course project.
- 🧠 Reflection: The interruption by the user led to switching context to `/sp.constitution`. The constitution was successfully updated.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-phr.sh` script failed, requiring manual PHR creation.
- Graders run and results (PASS/FAIL): Not applicable for this stage.
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A

---
id: 001
title: Failed to generate tasks - prerequisites not met
stage: tasks
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: User
command: /sp.tasks
labels: [tasks, failure, prerequisites]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:

tests:

---

## Prompt

/sp.tasks

## Response snapshot

I was unable to generate tasks because the feature context is not established. It appears that a valid feature specification has not been created or loaded.

Please run `/sp.specify` with a clear feature description to establish the feature context and create the necessary specification files. For example:

`/sp.specify Implement a new user authentication system with OAuth2.`

Once the specification is created, you can then run `/sp.tasks` to generate the implementation tasks.

## Outcome

- ✅ Impact: Negative - task generation failed due to missing feature context.
- 🧪 Tests: N/A
- 📁 Files: None
- 🔁 Next prompts: User to run /sp.specify with a valid feature description.
- 🧠 Reflection: The `check-prerequisites.ps1` script failed to find a feature directory, defaulting to 'main'. The previous `/sp.specify` command was likely interrupted or provided an invalid feature description (a file path instead of natural language). The agent needs to ensure a proper feature context is established before attempting to generate tasks.

## Evaluation notes (flywheel)

- Failure modes observed: Script execution failure, missing feature context.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure robust feature context detection in `/sp.tasks` or prompt user for feature name explicitly.

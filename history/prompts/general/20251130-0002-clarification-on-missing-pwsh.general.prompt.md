---
id: 20251130-0002
title: Clarification on missing pwsh
stage: general
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: null
branch: 002-physical-ai-course
user: user
command: null
labels: ["clarify", "powershell", "error"]
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
why
```

## Response snapshot

The `/sp.clarify` command is designed to run a prerequisite check using a PowerShell script located at `.specify/scripts/powershell/check-prerequisites.ps1`. The error "No such file or directory" for `pwsh` means that the PowerShell executable (which is typically `pwsh`) was not found in your system's environment PATH. Without it, the script cannot be executed.

## Outcome

- ✅ Impact: User understood why the previous command failed.
- 🧪 Tests: N/A
- 📁 Files: N/A
- 🔁 Next prompts: User to install PowerShell or check PATH.
- 🧠 Reflection: Clearly explained the dependency on PowerShell and the cause of the error.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A

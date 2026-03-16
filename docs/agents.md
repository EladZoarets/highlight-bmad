# Agent Roles (BMAD Workflow)

This repository demonstrates a BMAD-style agent workflow.

Instead of a fixed specification → design → implementation pipeline,
the solution is produced through collaboration between specialized agents.

## Agents

### Product Agent
Defines the feature behavior and success criteria.

Responsibilities:
- interpret the assignment
- clarify user preferences
- define expected outcomes

### Architect Agent
Designs the technical approach.

Responsibilities:
- define the scoring strategy
- translate product intent into a technical model
- describe data flow

### Manager Agent
Orchestrates the workflow across agents.

Responsibilities:
- decide which agent to invoke for the current task
- track progress through workflow phases
- surface blockers and coordinate handoffs

### Senior Developer Agent
Implements the solution.

Responsibilities:
- write the Python implementation
- keep the code minimal and deterministic

### Reviewer Agent
Validates the implementation.

Responsibilities:
- check correctness against requirements
- verify scoring logic and ordering
- identify edge cases

### Chaos Agent
Stress-tests the solution using adversarial scenarios.

Responsibilities:
- challenge assumptions in the scoring logic
- test edge cases and adversarial inputs
- identify fragile or accidentally correct behavior

## Workflow

The agents collaborate in the following sequence:

Product → Architect → Manager → Senior Developer → Reviewer → Chaos

This reflects an iterative BMAD-style development loop.

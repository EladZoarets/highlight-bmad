# CLAUDE.md

## Scope
This repository implements Track 2 (BMAD) of the assignment.

The feature is AI Highlight Selector.

Do not implement Track 1 documentation flow here.
Do not create spec.md or design.md as the main workflow artifacts unless explicitly requested.

## Objective
Use a role-based BMAD workflow to build the same feature:
- input: game events JSON
- input: user preference
- output: selected highlights
- output: short explanation per selection

## Core Rules
- Keep the implementation minimal and demo-friendly.
- Use plain Python only.
- Prefer small functions over classes.
- No external libraries unless explicitly requested.
- No API, database, UI, or video processing.
- Logic only.

## Behavioral Rules
- Product agent focuses on requirements and success criteria.
- Architect agent focuses on technical approach and scoring logic.
- Engineer agent focuses on implementation only.
- Reviewer agent focuses on correctness and edge cases.
- Cause agent focuses on root cause and zero-trust validation.

## Output Rules
The final feature must:
- read structured JSON input
- score events deterministically
- return selected highlights sorted by score descending
- include a short plain-English reason for each selected highlight

## Validation Rules
Do not assume the implementation is correct.
Always validate outputs against:
- input
- scoring logic
- expected behavior
- edge cases

## Change Rules
- Keep changes scoped.
- Do not rewrite unrelated files.
- Avoid unnecessary architecture.
- Keep outputs concise and practical.

## Plan Rules
- Save plans to `.claude/plans/` inside the project directory.
- Name plan files as `{assignment-name}-plan.md` (e.g., `ai-highlight-selector-plan.md`).
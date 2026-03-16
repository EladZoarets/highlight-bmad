# BMAD Agents — AI Highlight Selector

This repository demonstrates a BMAD-style implementation of the same feature implemented in the Spec Kit track.

The purpose of this repo is not to invent a different product behavior.
The purpose is to implement the exact same feature contract using a BMAD workflow so the methodology comparison is valid.

## Canonical Feature Contract

This BMAD implementation intentionally uses the exact same feature contract as the Spec Kit track.

### Input
The system receives:
- a list of game events in JSON
- a user preference object with:
  - `favorite_player`
  - `favorite_team`

### Supported event types
Only these event types are supported:
- `goal`
- `assist`
- `card`

### Scoring rules
Each event gets a score using these exact rules:
- favorite player match = +8
- favorite team match = +5
- goal = +4
- assist = +3
- card = +1

### Filtering rules
- events with score `0` are excluded
- only relevant highlights are returned

### Output
Each selected highlight must include:
- `event`
- `score`
- `reason`

## BMAD Workflow

This repo keeps a BMAD-style delivery process while preserving the exact same functional behavior as the Spec Kit version.

### Business Agent
Responsibility:
- clarify the user need
- define what makes an event relevant
- keep the feature narrow and demo-friendly

Business conclusion:
Users want a lightweight highlight selector that promotes events relevant to their favorite player or favorite team.

### Manager Agent
Responsibility:
- translate the feature into a small execution scope
- keep implementation aligned with demo constraints
- ensure comparison parity with the Spec Kit track

Manager decision:
The BMAD implementation must remain behaviorally identical to the Spec Kit implementation so the comparison focuses on process, not on different logic.

### Architect Agent
Responsibility:
- define the scoring model
- define the input/output contract
- reduce ambiguity before implementation

Architect decision:
Use a deterministic scoring function:
- base score by event type
- bonus for favorite player
- bonus for favorite team
- include only events with score greater than zero
- sort results by descending score

### Developer Agent
Responsibility:
- implement the selector in Python
- keep the code small, readable, and deterministic
- return consistent structured output

Implementation requirements:
- support only `goal`, `assist`, `card`
- use exact scores from the canonical contract
- return `event`, `score`, `reason`
- sort by score descending

### Reviewer Agent
Responsibility:
- verify that the implementation matches the canonical contract
- check that unsupported event types are not part of the feature
- confirm output structure consistency

Reviewer checklist:
- same supported event types as Spec Kit
- same score values as Spec Kit
- same filtering behavior
- same output structure
- same ranking logic

### Chaos / Edge Case Agent
Responsibility:
- look for ambiguous or weak spots
- validate robustness on edge cases

Edge cases reviewed:
- event with no player match and no team match still may pass if event type has base score
- unsupported event types should not be scored
- empty input list should return empty output
- events with identical scores should still produce valid ordered output
- missing optional fields should not crash the script if handled safely

## Why BMAD Here

BMAD is used here to show an agent-oriented delivery process:
- business framing
- manager scoping
- architecture alignment
- implementation
- review
- edge-case validation

The feature itself is intentionally kept identical to the Spec Kit implementation.
That keeps the comparison fair:
- same feature
- same rules
- same expected output
- different working methodology

## Final Alignment Rule

Any future change in this repo must preserve parity with the Spec Kit feature contract unless the comparison explicitly requires a controlled divergence.
If parity breaks, the methodology comparison becomes invalid.
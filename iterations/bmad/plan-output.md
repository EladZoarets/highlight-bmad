# AI Highlight Selector — Plan Output

## Feature Summary
Given a list of game events and a user preference profile, score each event deterministically, filter out zero-score events, sort by score descending (stable), and return each qualifying event with its score and a human-readable reason.

## Technical Approach
Single flat module (`src/highlight_selector.py`) with five small pure functions and a `main()` smoke test. Data flows forward: score → filter → reason → sort → output. No state, no side effects, no external libraries.

## Scoring Rules

| Event Type    | Base Score |
|---------------|------------|
| `goal`        | 10         |
| `red_card`    | 8          |
| `assist`      | 6          |
| `save`        | 4          |
| `yellow_card` | 2          |
| unknown       | 0          |

**Preference boosts (additive):**
- `favorite_player` match: +5
- `favorite_team` match: +3

**Threshold:** score > 0
**Tie-breaking:** stable sort — preserve original input order on equal scores.

## Architecture

```
src/highlight_selector.py
  get_base_score(event_type: str) -> int
  get_preference_boost(event: dict, preferences: dict) -> int
  score_event(event: dict, preferences: dict) -> int
  build_reason(event: dict, preferences: dict) -> str
  select_highlights(events: list, preferences: dict) -> list
  main()

data/sample_input.json
  { "events": [...], "preferences": {...} }
```

## Data Flow

```
events + preferences
  → score_event() per event  [get_base_score + get_preference_boost]
  → filter: score > 0
  → build_reason() per passing event
  → sorted(key=score, stable)
  → [{ event, score, reason }, ...]
```

## Agents Involved
- **Product Agent** — defined inputs, outputs, edge cases, success criteria
- **Architect Agent** — defined scoring rules, function responsibilities, data flow
- **Manager Agent** — broke solution into 8 ordered tasks

# Execute — AI Highlight Selector

## Agent
Senior Developer

## Skill
implementation

## Plan source
iterations/bmad/ai-highlight-selector-plan.md

---

## Implemented Tasks

### Task 1 — score_event
- Looks up base score by event type (goal=4, assist=3, card=1)
- Returns 0 for unsupported event types
- Adds +8 if player matches favorite_player
- Adds +5 if team matches favorite_team

### Task 2 — build_reason
- Collects matched signals: favorite player, favorite team, event type
- Returns a comma-separated plain-English string
- Falls back to "relevant event" if no parts (should not happen after filtering)

### Task 3 — select_highlights
- Iterates events, calls score_event and build_reason for each
- Skips events with score == 0
- Sorts results by score descending (stable sort preserves input order for ties)
- Returns list of { event, score, reason }

### Task 4 — main
- Opens data/sample_input.json
- Calls select_highlights with events and preference
- Prints output as formatted JSON

---

## File Created
`src/highlight_selector.py`

---

## Output

Input: data/sample_input.json (preference: Messi / Inter Miami)

```json
[
  {
    "event": { "type": "goal", "player": "Messi", "team": "Inter Miami", "minute": 34 },
    "score": 17,
    "reason": "favorite player involved, favorite team, goal event"
  },
  {
    "event": { "type": "assist", "player": "Messi", "team": "Inter Miami", "minute": 20 },
    "score": 16,
    "reason": "favorite player involved, favorite team, assist event"
  },
  {
    "event": { "type": "goal", "player": "Suarez", "team": "Inter Miami", "minute": 55 },
    "score": 9,
    "reason": "favorite team, goal event"
  },
  {
    "event": { "type": "card", "player": "Ramos", "team": "Al Hilal", "minute": 67 },
    "score": 1,
    "reason": "card event"
  }
]
```

---

## Implementation Notes
- Scoring values match canonical contract in docs/agents.md exactly
- No classes, no external libraries, pure Python
- All 4 events scored > 0 so all are included
- Sorted 17 → 16 → 9 → 1 as expected

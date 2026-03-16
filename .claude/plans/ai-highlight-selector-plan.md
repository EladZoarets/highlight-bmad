# AI Highlight Selector — Implementation Plan

## Context
Building Track 2 (BMAD) of the assignment: an AI Highlight Selector that takes game events + user preferences and returns scored, sorted highlights with plain-English explanations. No external libraries, no APIs, no classes — plain Python logic only.

---

## Feature Summary
Given a list of game events and a user preference profile, score each event deterministically, filter out zero-score events, sort by score descending (stable), and return each qualifying event with its score and a human-readable reason.

---

## Technical Approach
Single flat module (`src/highlight_selector.py`) with five small pure functions and a `main()` smoke test. Data flows forward: score → filter → reason → sort → output. No state, no side effects.

---

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

**Threshold:** score > 0 (unknown type with no preference match = excluded)

**Tie-breaking:** stable sort — preserve original input order on equal scores.

---

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

Data flow:
```
events + preferences
  → score_event() per event  [get_base_score + get_preference_boost]
  → filter: score > 0
  → build_reason() per passing event
  → sorted(key=score, stable)
  → [{ event, score, reason }, ...]
```

---

## Ordered Task List

| # | Task | Purpose | Output |
|---|------|---------|--------|
| 1 | Scaffold `src/highlight_selector.py` | Runnable empty module with `main()` guard | File exists, importable |
| 2 | Implement `get_base_score(event_type)` | Score table: goal=10, red_card=8, assist=6, save=4, yellow_card=2, unknown=0 | Function returns correct int |
| 3 | Implement `get_preference_boost(event, preferences)` | +5 for player match, +3 for team match | Function returns 0–8 |
| 4 | Implement `score_event(event, preferences)` | Combine base + boost | Function returns total int |
| 5 | Implement `build_reason(event, preferences)` | Plain-English reason string reflecting type + preference matches | Non-empty accurate string |
| 6 | Implement `select_highlights(events, preferences)` | Entry point: score → filter → sort → return list | Correct sorted output |
| 7 | Create `data/sample_input.json` | Realistic fixture: 5–8 events, all types covered, preferences set | File exists with valid JSON |
| 8 | Wire `main()` smoke test | Load JSON, call `select_highlights`, print results | `python src/highlight_selector.py` runs and prints |

---

## Critical Files
- `src/highlight_selector.py` — create (all logic)
- `data/sample_input.json` — create (test fixture)
- `docs/assignment.md` — reference (input/output contract)

---

## Verification
Run `python src/highlight_selector.py` and confirm:
1. Output is non-empty for the sample input
2. Scores are sorted descending
3. Goal events score 10+ (or 15+ if player matches)
4. Reason strings reference the actual contributing factors
5. Unknown event types with no preference match are absent from output
6. Empty events list returns `[]`

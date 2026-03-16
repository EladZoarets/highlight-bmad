# Plan: AI Highlight Selector — BMAD /plan Command

## Context

The project implements Track 2 (BMAD) of the assignment. The previous `src/highlight_selector.py` was deleted because its scoring values diverged from the canonical contract defined in `docs/agents.md`. This plan re-implements the feature correctly using the BMAD workflow (Product → Architect → Manager phases) as defined in `.claude/commands/plan.md`.

---

## Phase 1 – Product Agent

**Feature summary:**
Users submit a list of game events (JSON) and a preference object. The system scores each event based on the user's favorite player and team, then returns the most relevant highlights ranked by score with a plain-English explanation for each.

**Inputs:**
- `events`: list of event objects (`type`, `player`, `team`, `minute`)
- `preference`: `{ "favorite_player": str, "favorite_team": str }`

**Outputs:**
- List of highlight dicts: `{ "event": {...}, "score": int, "reason": str }`

**Success criteria:**
- Supports only `goal`, `assist`, `card` event types
- Scores match canonical contract exactly
- Events with score `0` are excluded
- Output sorted by score descending
- Each entry has a non-empty `reason`

---

## Phase 2 – Architect Agent

**Scoring model (canonical — from `docs/agents.md`):**
| Signal | Points |
|---|---|
| favorite player match | +8 |
| favorite team match | +5 |
| goal | +4 |
| assist | +3 |
| card | +1 |

**Filtering:** exclude if final score == 0

**Ranking:** sort by score descending; ties keep original order (stable sort)

**Architecture (minimal):**
```
src/highlight_selector.py
  score_event(event, preference) -> int
  build_reason(event, preference) -> str
  select_highlights(events, preference) -> list[dict]
  main() — reads data/sample_input.json, prints JSON output
```

No classes. No external libraries. Pure Python.

---

## Phase 3 – Manager Agent (Task List)

Ordered implementation tasks:

1. Create `src/highlight_selector.py` with `score_event(event, preference) -> int`
   - Adds points for event type (goal/assist/card only)
   - Adds points for player match and team match
   - Returns 0 for unsupported event types

2. Implement `build_reason(event, preference) -> str`
   - Returns a plain-English string describing why the event was selected
   - Covers: player match, team match, event type combinations

3. Implement `select_highlights(events, preference) -> list[dict]`
   - Calls score_event and build_reason for each event
   - Filters out score == 0
   - Sorts by score descending (stable)
   - Returns list of `{ event, score, reason }` dicts

4. Implement `main()`
   - Reads `data/sample_input.json`
   - Calls `select_highlights`
   - Prints JSON output

---

## Critical Files

- `src/highlight_selector.py` — to be created
- `data/sample_input.json` — input fixture for validation
- `docs/agents.md` — canonical scoring contract (source of truth)
- `docs/validation.md` — expected output reference

---

## Verification

Run: `python3 src/highlight_selector.py`

Expected output for `data/sample_input.json` (preference: Messi / Inter Miami):
- Messi goal: score = 8+5+4 = **17** — "favorite player involved, goal event, favorite team"
- Messi assist: score = 8+5+3 = **16** — "favorite player involved, assist event, favorite team"
- Suarez goal (Inter Miami): score = 5+4 = **9** — "favorite team, goal event"
- Ramos card (Al Hilal): score = 1 — "card event" (no player/team match)

All 4 events have score > 0 so all are included, sorted 17 → 16 → 9 → 1.

# Review — AI Highlight Selector

## Agent
Reviewer

## Skill
validation

## Source
src/highlight_selector.py

## Contract reference
docs/agents.md

---

## Validation Checklist

### 1. Scoring correctness

| Signal | Expected | Observed |
|---|---|---|
| goal (base) | +4 | 4 ✓ |
| assist (base) | +3 | 3 ✓ |
| card (base) | +1 | 1 ✓ |
| favorite player match | +8 | 8 ✓ |
| favorite team match | +5 | 5 ✓ |
| goal + player + team | 17 | 17 ✓ |
| assist + player + team | 16 | 16 ✓ |
| card + player + team | 14 | 14 ✓ |

**Result: PASS**

---

### 2. Filtering

| Scenario | Expected | Observed |
|---|---|---|
| unsupported type (`"unknown"`) | excluded | excluded ✓ |
| unsupported type (`"save"`) with player match | excluded | excluded ✓ |
| supported type with no match | included (base score > 0) | included ✓ |

**Result: PASS**

---

### 3. Sorting and ranking

| Input scores | Expected order | Observed |
|---|---|---|
| 17, 16, 9, 1 | descending | [17, 16, 9, 1] ✓ |

**Result: PASS**

---

### 4. Output structure

Each highlight contains exactly:
- `event` — dict (shallow copy of original) ✓
- `score` — int ✓
- `reason` — non-empty string ✓

**Result: PASS**

---

### 5. Reason quality

| Score | Reason | Assessment |
|---|---|---|
| 17 | `"favorite player involved, favorite team, goal event"` | Clear ✓ |
| 16 | `"favorite player involved, favorite team, assist event"` | Clear ✓ |
| 9 | `"favorite team, goal event"` | Clear ✓ |
| 1 | `"card event"` | Clear ✓ |

**Result: PASS**

---

### 6. Assignment alignment

| Requirement | Status |
|---|---|
| Reads structured JSON input | ✓ |
| Supported event types: goal, assist, card only | ✓ |
| Scores events deterministically | ✓ |
| Returns highlights sorted by score descending | ✓ |
| Includes short plain-English reason per highlight | ✓ |
| Pure Python, no classes, no external libraries | ✓ |
| Parity with Spec Kit canonical contract | ✓ |

**Result: PASS**

---

## Validation Summary

| Check | Result |
|---|---|
| Scoring correctness | PASS |
| Filtering (score=0 excluded) | PASS |
| Sorting descending | PASS |
| Output structure (event, score, reason) | PASS |
| Reason quality | PASS |
| Assignment alignment | PASS |

**All checks pass. Implementation is correct and ready.**

---

## Issues Found
None.

## Fixes Needed
None.

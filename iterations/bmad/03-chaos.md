# Chaos Report — AI Highlight Selector (Final)

## Agent
Chaos

## Skill
chaos-testing

## Source
src/highlight_selector.py

---

## All Scenarios — Final State

### Round 1 — Case sensitivity and basic edge cases

| # | Scenario | Input | Expected | Result |
|---|---|---|---|---|
| R1-1 | Uppercase event type `"Goal"` | type="Goal" | score=17 | PASS |
| R1-2 | Lowercase player `"messi"` | player="messi", pref="Messi" | score=17 | PASS |
| R1-3 | Missing type field | no type key | score=0, excluded | PASS |
| R1-4 | Empty events list | `[]` | `[]` | PASS |
| R1-5 | Empty preference `{}` | pref={} | score=4 (base only) | PASS |
| R1-6 | None preference values | favorite_player=None | score=4 (base only) | PASS |
| R1-7 | Unsupported type with player match | type="save" | score=0, excluded | PASS |
| R1-8 | None event in events list | `[None]` | `[]` | PASS |

**Fixes applied:** `_norm()` with `.lower()`, `_match()` helper

---

### Round 2 — Non-string types and mutability

| # | Scenario | Input | Expected | Result |
|---|---|---|---|---|
| R2-1 | Int type field `123` | type=123 | score=0 | PASS |
| R2-2 | List type field `["goal"]` | type=["goal"] | score=0 | PASS |
| R2-3 | Whitespace in preference `"  Messi  "` | pref player with spaces | score=17 | PASS |
| R2-4 | Whitespace in event player `"  Messi  "` | event player with spaces | score=17 | PASS |
| R2-5 | `preference = None` | None | score=4 (base only) | PASS |
| R2-6 | Mutate input after call | mutate events[0] post-call | output unchanged | PASS |
| R2-7 | Empty string player, empty pref player | player="", fav_player="" | score=4 (no bonus) | PASS |

**Fixes applied:** `_norm()` guards non-string types, `preference or {}`, `dict(event)` copy, `_match` requires non-empty

---

### Round 3 — Invalid event types in list and tie-breaking

| # | Scenario | Input | Expected | Result |
|---|---|---|---|---|
| R3-1 | `True` in events list | `[True]` | `[]` | PASS |
| R3-2 | String in events list `"goal"` | `["goal"]` | `[]` | PASS |
| R3-3 | Missing `favorite_team` key in pref | no team key | score=12 (player+base) | PASS |
| R3-4 | Extra unknown keys in preference | extra key ignored | score=17 | PASS |
| R3-5 | Empty dict event `{}` | `{}` | excluded | PASS |
| R3-6 | Tie-breaking preserves input order | two equal-score events | stable order | PASS |

**Fixes applied:** `isinstance(event, dict)` guard in `select_highlights`

---

### Round 4 — Boundary guards and type coercion

| # | Scenario | Input | Expected | Result |
|---|---|---|---|---|
| R4-1 | `events = None` | None | `[]` | PASS |
| R4-2 | `score_event(None, pref)` | None event | 0 | PASS |
| R4-3 | Dict in player field `{"name": "Messi"}` | dict value | score=9 (no player bonus) | PASS |
| R4-4 | Unicode/accented names `"müller"` vs `"Müller"` | unicode | score=17 | PASS |
| R4-5 | Whitespace-only player `"   "` | spaces only | score=9 (no bonus) | PASS |
| R4-6 | Numeric preference player `10` vs `"10"` | int pref | score=17 | PASS |
| R4-7 | Player name equals team name | same value | score=17 (both bonuses) | PASS |
| R4-8 | Score output type | int check | `int` | PASS |

**Fixes applied:** `if not isinstance(event, dict): return 0` in `score_event`, `events or []` in `select_highlights`

---

## Final Summary

**29/29 scenarios pass.**

| Round | Focus | Issues Found | Fixed |
|---|---|---|---|
| 1 | Case sensitivity, basic edge cases | 2 | Yes |
| 2 | Non-string types, mutability, empty string | 4 | Yes |
| 3 | Non-dict events, tie-breaking | 2 | Yes |
| 4 | Boundary guards, type coercion | 2 | Yes |

Implementation is robust against all tested adversarial inputs.

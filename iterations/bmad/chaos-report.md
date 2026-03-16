# AI Highlight Selector — Chaos Report

Two rounds of adversarial testing were performed.

---

## Round 1 — Initial Implementation

| # | Scenario | Crash? | Silent Wrong Output? | Status |
|---|---|---|---|---|
| 1 | Case-sensitive name matching | No | Yes — boost silently dropped | FAIL |
| 2 | `null` type field → `.replace()` on `None` | Yes | — | FAIL |
| 3 | Empty-string preference/event fields | No | Yes — malformed reason | WARNING |
| 4 | Wrong-type fields (int, bool, list) | Yes (mid-loop) | Yes | FAIL |
| 5 | Non-dict items in events list | Yes (loop aborted, all results lost) | — | FAIL |
| 6 | Unknown type boosted above threshold | No | Yes — unknown events surfaced | WARNING |
| 7 | Duplicate score/reason logic | No | Yes — future maintenance trap | WARNING |
| 8 | Event dict mutation (aliasing) | No | Yes — stale score/reason possible | WARNING |

**Fixes applied after Round 1:**
- `isinstance(event, dict)` guard in loop (issue 5)
- `event.get("type") or "unknown"` for null-safety (issues 2, 4)
- `event.get("player") or "unknown player"` / `event.get("team") or "unknown team"` (issue 2b)
- `.lower()` on both sides of player/team comparison (issue 1)
- `event.get("type") or ""` in `score_event` (issue 4)

---

## Round 2 — Post-Fix Stress Test

| # | Scenario | Crash? | Silent Wrong Output? | Status |
|---|---|---|---|---|
| 1 | Non-string preference value (e.g. `123`) | Yes — `.lower()` on int | — | FAIL |
| 2 | `preferences=None` | Yes — `.get()` on None | — | FAIL |
| 3 | `minute` is dict or list | No | Yes — malformed reason | WARNING |
| 4 | Whitespace-only player/team (`"   "`) | No | Yes — wrong boost match | WARNING |
| 5 | `events=None` treated as empty list | No | Yes — silent upstream failure | WARNING |
| 6 | Null/unknown type boosted into output | No | Yes — `"Unknown by..."` in results | WARNING |

**Fixes applied after Round 2:**
- `preferences = preferences or {}` + `if events is None: return []` in `select_highlights`
- `isinstance(fav_player, str)` / `isinstance(fav_team, str)` before `.lower()` (issue 1)
- `isinstance(minute, (int, float))` replaces `is not None` (issue 3)
- `.strip()` applied to player/team fields before comparison and display (issue 4)

# AI Highlight Selector — Review Report

## Validation Summary

| Check | Status |
|---|---|
| Scoring correctness | PASS |
| Sorting and tie stability | PASS |
| Reason accuracy | PASS |
| Edge: empty events list | PASS |
| Edge: empty preferences `{}` | PASS |
| Edge: unknown event type (no preferences) | PASS |
| Edge: `None` preferences value | PASS |

## Scoring Trace (sample input)

| Event | Base | Player Boost | Team Boost | Total |
|---|---|---|---|---|
| goal / Messi / Barcelona | 10 | +5 | +3 | **18** |
| goal / Messi / Barcelona (88') | 10 | +5 | +3 | **18** |
| goal / Ronaldo / Real Madrid | 10 | 0 | 0 | **10** |
| assist / Xavi / Barcelona | 6 | 0 | +3 | **9** |
| red_card / Pepe / Real Madrid | 8 | 0 | 0 | **8** |
| save / Casillas / Real Madrid | 4 | 0 | 0 | **4** |
| offside_trap / Puyol / Barcelona | 0 | 0 | +3 | **3** |
| yellow_card / Ramos / Real Madrid | 2 | 0 | 0 | **2** |

## Issues Found & Resolved

| # | Issue | Severity | Fix |
|---|---|---|---|
| 1 | Case-sensitive name matching | FAIL | `.lower()` + `.strip()` on both sides |
| 2 | `null` type field crash | FAIL | `event.get("type") or "unknown"` |
| 2b | `null` player/team → `"None"` in output | WARNING | `event.get("player") or "unknown player"` |
| 3 | Empty-string type → malformed reason | WARNING | `or ""` fallback pattern |
| 4 | Wrong-type field crash mid-loop | FAIL | `event.get("type") or ""` |
| 5 | Non-dict items → loop crash, all results lost | FAIL | `isinstance(event, dict)` guard |
| 6 | Unknown type boosted above threshold | WARNING | Documented; acceptable per assignment spec |
| 7 | Duplicate score/reason logic | WARNING | Noted; low risk for current scope |
| 8 | Event dict aliasing | WARNING | Noted; no mutation in current pipeline |

## Final Output (sample run)

```
Selected 8 highlight(s):

  1. [score 18]  Goal by Messi (Barcelona) at 23' — favorite player +5, favorite team +3
  2. [score 18]  Goal by Messi (Barcelona) at 88' — favorite player +5, favorite team +3
  3. [score 10]  Goal by Ronaldo (Real Madrid) at 72'
  4. [score  9]  Assist by Xavi (Barcelona) at 23' — favorite team +3
  5. [score  8]  Red card by Pepe (Real Madrid) at 67'
  6. [score  4]  Save by Casillas (Real Madrid) at 41'
  7. [score  3]  Offside trap by Puyol (Barcelona) at 55' — favorite team +3
  8. [score  2]  Yellow card by Ramos (Real Madrid) at 35'
```

## Conclusion
Core logic is correct for all well-formed inputs. Two rounds of chaos testing identified and resolved all hard crash paths. Remaining warnings are either acceptable per the assignment spec or low-risk for the current demo scope.

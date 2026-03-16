# AI Highlight Selector — Task List

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

## Status
All 8 tasks completed.

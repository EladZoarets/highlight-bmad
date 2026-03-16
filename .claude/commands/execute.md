Use the Senior Developer agent with the implementation skill.

Goal
Implement the BMAD plan exactly as approved in the planning phase.

Important
Do not redesign the feature.
Do not introduce new event types.
Do not change scoring values.

Canonical feature contract
Supported event types:
- goal
- assist
- card

Scoring rules:
- goal = +4
- assist = +3
- card = +1
- favorite_player = +8
- favorite_team = +5

Filtering
- exclude events with score 0

Output format
Each result must contain:
- event
- score
- reason

Ranking
- sort by score descending
- preserve input order for ties

Implementation constraints
- pure Python only
- no classes
- no external libraries
- keep functions small and readable

Implementation targets
- src/highlight_selector.py
- data/sample_input.json

Execution rules
- implement tasks sequentially from the Manager task list
- keep code changes minimal
- do not add additional features
- do not change the architecture

Return
1. implemented tasks
2. the full contents of src/highlight_selector.py
3. the full contents of data/sample_input.json
4. the output of running `python3 src/highlight_selector.py`
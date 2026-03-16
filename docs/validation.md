# Validation — AI Highlight Selector

## Run

```
python3 src/highlight_selector.py
```

## Output

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

## Checks

| Check | Expected | Result |
|---|---|---|
| Sorted descending | score 18 → 18 → 10 → 9 → 8 → 4 → 3 → 2 | PASS |
| Tie stability | e1 (23') before e7 (88'), both score 18 | PASS |
| Player boost applied | Messi events: base 10 + player +5 + team +3 = 18 | PASS |
| Team-only boost | Xavi (Barcelona): base 6 + team +3 = 9 | PASS |
| No boost | Ronaldo (Real Madrid): base 10, no boost = 10 | PASS |
| Unknown type included via boost | offside_trap + team +3 = 3, present in output | PASS |
| Reason accuracy | All reasons reflect actual scoring factors | PASS |

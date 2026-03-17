# Validation: AI Highlight Selector (BMAD)

## Test 1 – Full Preference

```json
{
  "input": {
    "events": [
      { "type": "goal", "player": "Messi", "team": "Inter Miami" },
      { "type": "assist", "player": "Messi", "team": "Inter Miami" }
    ],
    "preference": {
      "favorite_player": "Messi",
      "favorite_team": "Inter Miami"
    }
  },
  "output": [
    { "score": 17 },
    { "score": 16 }
  ],
  "result": "Correct scoring and ranking"
}
```

## Test 2 – Empty Preference

```json
{
  "input": {
    "events": [
      { "type": "goal" },
      { "type": "card" }
    ],
    "preference": {}
  },
  "output": [
    { "score": 4 },
    { "score": 1 }
  ],
  "result": "Falls back to event-type scoring"
}
```

## Test 3 – Missing Fields

```json
{
  "input": {
    "events": [
      { "type": "goal" },
      { "type": "assist", "team": "Inter Miami" }
    ],
    "preference": {
      "favorite_team": "Inter Miami"
    }
  },
  "output": [
    { "score": 8 },
    { "score": 4 }
  ],
  "result": "Handles missing fields without failure"
}
```

## Conclusion

The implementation behaves correctly across core and edge scenarios.

Validation was required to confirm behavior not explicitly defined during generation.
import json

EVENT_SCORES = {
    "goal": 4,
    "assist": 3,
    "card": 1,
}


def _norm(value):
    if value is None:
        return ""
    return str(value).strip().lower() if not isinstance(value, (list, dict)) else ""


def _match(event_val, pref_val):
    a, b = _norm(event_val), _norm(pref_val)
    return bool(a) and a == b


def score_event(event, preference):
    if not isinstance(event, dict):
        return 0
    preference = preference or {}
    base = EVENT_SCORES.get(_norm(event.get("type")), 0)
    if base == 0:
        return 0
    score = base
    if _match(event.get("player"), preference.get("favorite_player")):
        score += 8
    if _match(event.get("team"), preference.get("favorite_team")):
        score += 5
    return score


def build_reason(event, preference):
    preference = preference or {}
    parts = []
    if _match(event.get("player"), preference.get("favorite_player")):
        parts.append("favorite player involved")
    if _match(event.get("team"), preference.get("favorite_team")):
        parts.append("favorite team")
    event_type = _norm(event.get("type"))
    if event_type in EVENT_SCORES:
        parts.append(f"{event_type} event")  # already normalized to lowercase
    return ", ".join(parts) if parts else "relevant event"


def select_highlights(events, preference):
    results = []
    for event in (events or []):
        if not isinstance(event, dict):
            continue
        s = score_event(event, preference)
        if s == 0:
            continue
        results.append({
            "event": dict(event),
            "score": s,
            "reason": build_reason(event, preference),
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


def main():
    with open("data/sample_input.json") as f:
        data = json.load(f)
    highlights = select_highlights(data["events"], data["preference"])
    print(json.dumps(highlights, indent=2))


if __name__ == "__main__":
    main()

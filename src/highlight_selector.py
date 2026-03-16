"""
AI Highlight Selector — Track 2 (BMAD)

Reads structured game events JSON, scores each event deterministically,
and returns selected highlights sorted by score descending with a
plain-English reason per selection.
"""

import json
import os

# ---------------------------------------------------------------------------
# Scoring constants
# ---------------------------------------------------------------------------

BASE_SCORES = {
    "goal": 10,
    "red_card": 8,
    "assist": 6,
    "save": 4,
    "yellow_card": 2,
}

PLAYER_BOOST = 5
TEAM_BOOST = 3
SCORE_THRESHOLD = 0  # score must be strictly greater than this


# ---------------------------------------------------------------------------
# Pure functions
# ---------------------------------------------------------------------------

def get_base_score(event_type: str) -> int:
    """Return the base score for a given event type. Unknown types score 0."""
    return BASE_SCORES.get(event_type, 0)


def get_preference_boost(event: dict, preferences: dict) -> int:
    """
    Return the preference boost for an event.

    +5 if the event's player matches preferences['favorite_player']
    +3 if the event's team  matches preferences['favorite_team']
    Boosts are cumulative.
    """
    boost = 0
    favorite_player = preferences.get("favorite_player")
    favorite_team = preferences.get("favorite_team")

    if favorite_player and isinstance(favorite_player, str) and (event.get("player") or "").strip().lower() == favorite_player.strip().lower():
        boost += PLAYER_BOOST

    if favorite_team and isinstance(favorite_team, str) and (event.get("team") or "").strip().lower() == favorite_team.strip().lower():
        boost += TEAM_BOOST

    return boost


def score_event(event: dict, preferences: dict) -> int:
    """Return the total score for a single event (base + preference boost)."""
    base = get_base_score(event.get("type") or "")
    boost = get_preference_boost(event, preferences)
    return base + boost


def build_reason(event: dict, preferences: dict) -> str:
    """
    Build a plain-English reason string explaining why this event was selected.

    Example:
      "Goal by Messi (Barcelona) at 45' — favorite player +5, favorite team +3"
    """
    event_type = (event.get("type") or "unknown").replace("_", " ")
    player = (event.get("player") or "").strip() or "unknown player"
    team = (event.get("team") or "").strip() or "unknown team"
    minute = event.get("minute")

    time_part = f" at {minute}'" if isinstance(minute, (int, float)) else ""
    base = f"{event_type.capitalize()} by {player} ({team}){time_part}"

    boosts = []
    fav_player = preferences.get("favorite_player")
    fav_team = preferences.get("favorite_team")
    if fav_player and isinstance(fav_player, str) and (event.get("player") or "").strip().lower() == fav_player.strip().lower():
        boosts.append(f"favorite player +{PLAYER_BOOST}")
    if fav_team and isinstance(fav_team, str) and (event.get("team") or "").strip().lower() == fav_team.strip().lower():
        boosts.append(f"favorite team +{TEAM_BOOST}")

    if boosts:
        return f"{base} — {', '.join(boosts)}"
    return base


def select_highlights(events: list, preferences: dict) -> list:
    """
    Score all events, filter those with score > 0, and return them sorted by
    score descending (stable — preserves input order on ties).

    Each result dict has the shape:
        {"event": <original event dict>, "score": <int>, "reason": <str>}
    """
    if events is None:
        return []
    preferences = preferences or {}
    if not events:
        return []

    scored = []
    for event in events:
        if not isinstance(event, dict):
            continue
        s = score_event(event, preferences)
        if s > SCORE_THRESHOLD:
            scored.append({
                "event": event,
                "score": s,
                "reason": build_reason(event, preferences),
            })

    # Python's sort is stable, so equal-score items preserve their input order.
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    """Load data/sample_input.json relative to this file, run selection, print results."""
    here = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(here, "..", "data", "sample_input.json")

    with open(data_path, "r") as f:
        data = json.load(f)

    events = data.get("events", [])
    preferences = data.get("preferences", {})

    highlights = select_highlights(events, preferences)

    print(f"Selected {len(highlights)} highlight(s):\n")
    for i, h in enumerate(highlights, 1):
        e = h["event"]
        print(f"  {i}. [score {h['score']:>2}]  {h['reason']}")

    return highlights


if __name__ == "__main__":
    main()

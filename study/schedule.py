"""Review queue for one local student.

Misses follow the SM-2 step in the study bot (`coach/sm2.py`): a wrong answer
resets the interval, a right answer lengthens it. The next item follows the
bot's review-first plan (`coach/planner.py`) without track weights: a miss or
a due card, then unseen items, then the soonest later card. Three rights in a
row leave the front of this exam queue. There is no daily cap and no second user.
"""

from __future__ import annotations

from datetime import date, timedelta

from study.bank import Item


def apply_review(state: dict, ok: bool, today: date) -> dict:
    """One SM-2 step. The bank's right/wrong is the quality: 5 or 1."""
    rating = 5 if ok else 1
    ef = float(state.get("ef", 2.5))
    reps = int(state.get("reps", 0))
    interval = int(state.get("interval", 0))
    if rating < 3:
        reps = 0
        interval = 1
    else:
        if reps == 0:
            interval = 1
        elif reps == 1:
            interval = 6
        else:
            interval = int(round(interval * ef))
        reps += 1
    ef = ef + (0.1 - (5 - rating) * (0.08 + (5 - rating) * 0.02))
    if ef < 1.3:
        ef = 1.3
    state["ef"] = ef
    state["interval"] = interval
    state["reps"] = reps
    state["due"] = (today + timedelta(days=interval)).isoformat()
    state["last_rating"] = rating
    state["seen"] = True
    return state


def order_items(
    items: list[Item],
    progress,
    *,
    ear_only: bool = False,
    today: date | None = None,
) -> list[Item]:
    """Next-item order. A miss is due now, even though SM-2 dates it tomorrow."""
    today_s = (today or date.today()).isoformat()
    pool = [item for item in items if item.channel == "ear"] if ear_only else list(items)
    misses: list[Item] = []
    due: list[Item] = []
    fresh: list[Item] = []
    ahead: list[Item] = []
    mastered: list[Item] = []
    for item in pool:
        state = progress.get(item.id)
        seen = item.id in progress.items
        last = state.get("last", "")
        streak = int(state.get("streak", 0))
        due_on = str(state.get("due") or "")
        if last == "wrong":
            misses.append(item)
        elif streak >= 3:
            mastered.append(item)
        elif seen and due_on and due_on <= today_s:
            due.append(item)
        elif not seen:
            fresh.append(item)
        else:
            ahead.append(item)

    def wrong_then_id(item: Item) -> tuple:
        state = progress.get(item.id)
        return (-int(state.get("wrong", 0)), item.id)

    def due_then_id(item: Item) -> tuple:
        state = progress.get(item.id)
        return (str(state.get("due") or "9999-99-99"), item.id)

    misses.sort(key=wrong_then_id)
    due.sort(key=due_then_id)
    fresh.sort(key=lambda item: item.id)
    ahead.sort(key=due_then_id)
    mastered.sort(key=due_then_id)
    return misses + due + fresh + ahead + mastered

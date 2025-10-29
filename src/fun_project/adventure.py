"""Core functionality for generating playful suggestions."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence

from .data import ACTIVITIES, CATEGORIES, Activity


@dataclass(frozen=True)
class ActivitySuggestion:
    """Represents a curated activity suggestion."""

    activity: Activity

    @property
    def name(self) -> str:
        return self.activity.name

    @property
    def category(self) -> str:
        return self.activity.category

    @property
    def description(self) -> str:
        return self.activity.description

    @property
    def soundtrack_options(self) -> Sequence[str]:
        return self.activity.soundtracks

    @property
    def snack_options(self) -> Sequence[str]:
        return self.activity.snacks


@dataclass(frozen=True)
class SpinResult:
    """Result of the spin-for-fun feature."""

    suggestion: ActivitySuggestion
    soundtrack: str
    snack: str


def _pick_from(items: Sequence[str], rng: random.Random) -> str:
    """Select a random item from a sequence using the provided RNG."""

    if not items:
        raise ValueError("Cannot pick from an empty sequence.")
    return rng.choice(list(items))


def _filter_by_category(
    activities: Iterable[Activity], category: Optional[str]
) -> List[Activity]:
    if category is None:
        return list(activities)
    normalized = category.strip().lower()
    filtered = [a for a in activities if a.category.lower() == normalized]
    if not filtered:
        raise ValueError(
            f"No activities found for category '{category}'. Available categories: {', '.join(CATEGORIES)}"
        )
    return filtered


def suggest_activity(category: Optional[str] = None, *, seed: Optional[int] = None) -> ActivitySuggestion:
    """Return a random activity suggestion, optionally filtered by category."""

    rng = random.Random(seed)
    filtered = _filter_by_category(ACTIVITIES, category)
    activity = rng.choice(filtered)
    return ActivitySuggestion(activity)


def spin_for_fun(category: Optional[str] = None, *, seed: Optional[int] = None) -> SpinResult:
    """Return a playful combination of activity, soundtrack, and snack."""

    rng = random.Random(seed)
    suggestion = suggest_activity(category, seed=seed)
    soundtrack = _pick_from(suggestion.soundtrack_options, rng)
    snack = _pick_from(suggestion.snack_options, rng)
    return SpinResult(suggestion, soundtrack, snack)


def list_categories() -> Sequence[str]:
    """Return all available activity categories."""

    return tuple(CATEGORIES)


def list_activities(category: Optional[str] = None) -> Sequence[Activity]:
    """Return all activities, optionally filtered by category."""

    return tuple(_filter_by_category(ACTIVITIES, category))

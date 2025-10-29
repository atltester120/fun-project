"""Static data that powers the fun suggestions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


data: List[dict[str, object]] = [
    {
        "name": "Backyard Stargazing",
        "category": "outdoor",
        "description": "Grab a blanket, lie down outside, and try to spot a constellation.",
        "soundtracks": [
            "Gustav Holst - The Planets",
            "Lo-fi Space Beats playlist",
            "Nature nighttime ambience",
        ],
        "snacks": ["hot cocoa", "trail mix", "sliced apples"],
    },
    {
        "name": "Kitchen Concert",
        "category": "creative",
        "description": "Turn utensils into instruments and perform your favorite song.",
        "soundtracks": [
            "Queen - Don't Stop Me Now",
            "Funky Kitchen Jams playlist",
            "Your own beatboxing!",
        ],
        "snacks": ["grapes", "popcorn", "sparkling water"],
    },
    {
        "name": "Mini Museum Walk",
        "category": "learning",
        "description": "Curate five objects around the house and give them museum labels.",
        "soundtracks": [
            "Classical focus playlist",
            "Studio Ghibli piano covers",
            "Instrumental jazz"
        ],
        "snacks": ["tea", "shortbread cookies", "berries"],
    },
    {
        "name": "Emoji Story Sprint",
        "category": "creative",
        "description": "Write a story told only with emojis and send it to a friend.",
        "soundtracks": [
            "Upbeat pop instrumentals",
            "Video game chiptunes",
            "Morning energy playlist",
        ],
        "snacks": ["fruit salad", "rice crackers", "smoothie"],
    },
    {
        "name": "Living Room Adventure Race",
        "category": "active",
        "description": "Design a small obstacle course and race the clock.",
        "soundtracks": [
            "Action movie soundtrack mix",
            "High-energy workout playlist",
            "Drum & bass essentials",
        ],
        "snacks": ["bananas", "protein bites", "electrolyte drink"],
    },
]


@dataclass(frozen=True)
class Activity:
    """Represents an activity available in the fun project."""

    name: str
    category: str
    description: str
    soundtracks: List[str]
    snacks: List[str]


# Convert dictionaries to dataclass instances at import time for type safety.
ACTIVITIES: List[Activity] = [Activity(**item) for item in data]


# Collect the unique categories for quick access in the CLI.
CATEGORIES = sorted({activity.category for activity in ACTIVITIES})

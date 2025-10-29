"""Fun Project package.

Provides utilities for suggesting joyful micro-adventures via the CLI.
"""

from .adventure import ActivitySuggestion, SpinResult, suggest_activity, spin_for_fun

__all__ = [
    "ActivitySuggestion",
    "SpinResult",
    "suggest_activity",
    "spin_for_fun",
]

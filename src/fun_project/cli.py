"""Command-line interface for the fun project."""

from __future__ import annotations

import argparse
import json
from typing import Any, Dict, Iterable, Sequence

from .adventure import (
    ActivitySuggestion,
    list_activities,
    list_categories,
    spin_for_fun,
    suggest_activity,
)


def _suggestion_to_dict(suggestion: ActivitySuggestion) -> Dict[str, Any]:
    return {
        "name": suggestion.name,
        "category": suggestion.category,
        "description": suggestion.description,
        "soundtrack_options": list(suggestion.soundtrack_options),
        "snack_options": list(suggestion.snack_options),
    }


def _format_categories(categories: Sequence[str]) -> str:
    return "\n".join(f"• {category}" for category in categories)


def _format_activities(activities: Iterable[Any]) -> str:
    lines = []
    for activity in activities:
        lines.append(f"- {activity.name} ({activity.category})")
        lines.append(f"  {activity.description}")
    return "\n".join(lines)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="fun-project",
        description="Spin for a fun micro-adventure suggestion!",
    )
    subparsers = parser.add_subparsers(dest="command")

    random_parser = subparsers.add_parser("random", help="Get a random activity suggestion")
    random_parser.add_argument(
        "-c",
        "--category",
        help="Filter suggestions by category",
    )

    spin_parser = subparsers.add_parser(
        "spin", help="Spin for an activity with soundtrack and snack pairings"
    )
    spin_parser.add_argument(
        "-c", "--category", help="Filter by category before spinning"
    )

    subparsers.add_parser("categories", help="List available categories")

    list_parser = subparsers.add_parser("list", help="List all curated activities")
    list_parser.add_argument(
        "-c", "--category", help="Filter activities by category"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output machine-readable JSON instead of text",
    )

    return parser


def handle_random(category: str | None, *, as_json: bool) -> str:
    suggestion = suggest_activity(category)
    if as_json:
        return json.dumps(_suggestion_to_dict(suggestion), indent=2)
    return (
        f"Try: {suggestion.name}\n"
        f"Category: {suggestion.category}\n"
        f"What to do: {suggestion.description}\n"
        f"Soundtracks: {', '.join(suggestion.soundtrack_options)}\n"
        f"Snacks: {', '.join(suggestion.snack_options)}"
    )


def handle_spin(category: str | None, *, as_json: bool) -> str:
    result = spin_for_fun(category)
    if as_json:
        payload = _suggestion_to_dict(result.suggestion)
        payload.update({
            "soundtrack": result.soundtrack,
            "snack": result.snack,
        })
        return json.dumps(payload, indent=2)
    return (
        f"Your micro-adventure is: {result.suggestion.name}\n"
        f"Category: {result.suggestion.category}\n"
        f"Cue up: {result.soundtrack}\n"
        f"Grab: {result.snack}\n"
        f"Description: {result.suggestion.description}"
    )


def handle_categories(*, as_json: bool) -> str:
    categories = list_categories()
    if as_json:
        return json.dumps({"categories": categories}, indent=2)
    return "Available categories:\n" + _format_categories(categories)


def handle_list(category: str | None, *, as_json: bool) -> str:
    activities = list_activities(category)
    if as_json:
        return json.dumps(
            {"activities": [_suggestion_to_dict(ActivitySuggestion(a)) for a in activities]},
            indent=2,
        )
    return "Curated activities:\n" + _format_activities(activities)


def main(argv: Sequence[str] | None = None) -> str:
    parser = create_parser()
    args = parser.parse_args(argv)

    command = args.command or "random"
    as_json = args.json

    category = getattr(args, "category", None)

    if command == "random":
        output = handle_random(category, as_json=as_json)
    elif command == "spin":
        output = handle_spin(category, as_json=as_json)
    elif command == "categories":
        output = handle_categories(as_json=as_json)
    elif command == "list":
        output = handle_list(category, as_json=as_json)
    else:
        parser.error(f"Unknown command: {command}")

    return output


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    print(main())

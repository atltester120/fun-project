# Fun Project

A tiny Python-powered inspiration machine that gives you whimsical micro-adventures on demand. Spin for a random activity, pick a category, or let the CLI assemble a full vibe with matching soundtrack and snack suggestions.

## Features

- 🎲 Random activity suggestions with friendly descriptions
- 🧭 Filter by category (creative, outdoor, active, learning)
- 🎧 "Spin" mode pairs the activity with a soundtrack and snack
- 🧾 JSON output for automation or integration in other tools
- ✅ Fully tested with `pytest`

## Getting Started

This project uses Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

The `requirements-dev.txt` file includes tooling used for development and testing.

## Usage

Run the CLI via `python -m fun_project.cli` or with the module path added to `PYTHONPATH`:

```bash
PYTHONPATH=src python -m fun_project.cli random
```

Examples:

```bash
# Get a random activity suggestion
PYTHONPATH=src python -m fun_project.cli random

# Spin up an activity with soundtrack and snack
PYTHONPATH=src python -m fun_project.cli spin

# View available categories
PYTHONPATH=src python -m fun_project.cli categories

# Output JSON for scripting
PYTHONPATH=src python -m fun_project.cli spin --json
```

## Running Tests

```bash
pip install -r requirements-dev.txt
PYTHONPATH=src pytest
```

## Contributing

1. Fork and clone the repository.
2. Create a feature branch.
3. Make your changes with tests.
4. Run `pytest` to ensure everything passes.
5. Open a Pull Request with details about the fun you added!

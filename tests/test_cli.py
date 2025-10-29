import json

from fun_project import adventure, cli


def test_handle_random_produces_expected_text(monkeypatch):
    suggestion = adventure.ActivitySuggestion(adventure.ACTIVITIES[0])
    monkeypatch.setattr(cli, "suggest_activity", lambda category=None: suggestion)

    output = cli.handle_random(None, as_json=False)

    assert suggestion.name in output
    assert suggestion.description in output


def test_handle_spin_json(monkeypatch):
    suggestion = adventure.ActivitySuggestion(adventure.ACTIVITIES[0])
    spin_result = adventure.SpinResult(
        suggestion=suggestion,
        soundtrack=suggestion.soundtrack_options[0],
        snack=suggestion.snack_options[0],
    )
    monkeypatch.setattr(cli, "spin_for_fun", lambda category=None: spin_result)

    output = cli.handle_spin(None, as_json=True)
    payload = json.loads(output)

    assert payload["soundtrack"] == suggestion.soundtrack_options[0]
    assert payload["snack"] == suggestion.snack_options[0]
    assert payload["name"] == suggestion.name


def test_main_defaults_to_random(monkeypatch):
    called = {}

    def fake_random(category=None, *, as_json):
        called["category"] = category
        called["as_json"] = as_json
        return "done"

    monkeypatch.setattr(cli, "handle_random", fake_random)

    output = cli.main([])

    assert output == "done"
    assert called == {"category": None, "as_json": False}

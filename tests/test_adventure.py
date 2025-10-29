from fun_project import adventure


def test_suggest_activity_with_seed():
    suggestion = adventure.suggest_activity(seed=42)
    assert suggestion.name == "Backyard Stargazing"
    assert suggestion.category == "outdoor"


def test_spin_for_fun_is_deterministic_with_seed():
    result = adventure.spin_for_fun(seed=1)
    assert result.suggestion.name == "Kitchen Concert"
    assert result.soundtrack == "Queen - Don't Stop Me Now"
    assert result.snack == "sparkling water"


def test_list_categories_sorted_unique():
    categories = adventure.list_categories()
    assert categories == tuple(sorted(set(categories)))


def test_list_activities_filters_by_category():
    activities = adventure.list_activities("creative")
    assert all(activity.category == "creative" for activity in activities)
    assert len(activities) == 2

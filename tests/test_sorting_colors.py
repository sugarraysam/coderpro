from src.sorting_colors import Solution


def test_sorting_colors():
    cases = [
        {"in": [], "want": []},
        {"in": [2, 0, 1, 0, 0, 2, 2], "want": [0, 0, 0, 1, 2, 2, 2]},
        {"in": [2, 0, 2, 1, 1, 0], "want": [0, 0, 1, 1, 2, 2]},
        {"in": [1, 1, 1], "want": [1, 1, 1]},
        {"in": [0, 2, 2, 2], "want": [0, 2, 2, 2]},
    ]
    for c in cases:
        assert Solution(c["in"]).quicksort() == c["want"]
        assert Solution(c["in"]).bubble() == c["want"]
from main import run_game_1, run_game_2


def test_example_1():
    example = """
        Time:      7  15   30
        Distance:  9  40  200
    """
    r = run_game_1(example)
    assert r == 288


def test_example_2():
    example = """
        Time:      7  15   30
        Distance:  9  40  200
    """
    r = run_game_2(example)
    assert r == 71503

from main import run_game_1, run_game_2


def test_example_1():
    example = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """
    r = run_game_1(example)
    assert r == 4361


def test_example_2():
    example = """
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """
    r = run_game_2(example)
    assert r == 467835


def test_example_2_2():
    example = """
        ....+467*114.....
    """
    r = run_game_2(example)
    assert r == 53238


def test_example_2_3():
    example = """
        467..114..
        ...*.....*
        ..35..633.
        ......#...
        617*50....
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    """
    r = run_game_2(example)
    assert r == 467835 + (617 * 50)


def test_example_2_4():
    example = """
        ....467.....
        ....*114....
    """
    r = run_game_2(example)
    assert r == 53238


def test_example_2_5():
    example = """
        ....467...
        ....*114..
        ....467...
    """
    r = run_game_2(example)

    result_1_3 = 467 * 467
    result_1_2 = 467 * 114
    result_2_3 = result_1_2
    assert r == result_1_3 + result_1_2 + result_2_3


def test_example_2_6():
    example = """
        ....2...
        ....3*4.
    """
    r = run_game_2(example)

    result_1_2 = (2 * 3) + (2 * 4)
    result_2_2 = 3 * 4
    assert r == result_1_2 + result_2_2


def test_example_2_7():
    example = """
        ....467.....
        ....10*114..
        ....467.....
    """
    r = run_game_2(example)

    result_1_3 = 467 * 467
    result_1_2 = (467 * 10) + (467 * 114)
    result_2_2 = 10 * 114
    result_2_3 = result_1_2
    assert r == result_1_3 + result_1_2 + result_2_2 + result_2_3


def test_example_2_8():
    example = """
        ..2*3*4.
    """
    r = run_game_2(example)

    assert r == 2 * 3 + 3 * 4


def test_example_2_9():
    example = """
        ........
        .24..4..
        ......*.
    """
    r = run_game_2(example)

    assert r == 0


def test_example_2_11():
    example = """
        .......5......
        ..7*..*.......
        ...*13*.......
        .......15.....
    """
    r = run_game_2(example)

    assert r == 442


def test_example_2_12():
    example = """
        ..7*..
        ...*13
    """
    r = run_game_2(example)

    assert r == (7 * 13) * 2


def test_example_2_13():
    example = """
        ......5......
        ..7..*.......
        ...13*.......
    """
    r = run_game_2(example)

    assert r == 5 * 13


def test_example_2_14():
    example = """
        .5.....23..$
        8...90*12...
    """
    r = run_game_2(example)

    assert r == 90 * 12 + 90 * 23 + 23 * 12


def test_example_2_15():
    example = """
        2.4......1
        .*........
        3.5..503+.
    """
    r = run_game_2(example)

    assert r == (2 * 3 + 2 * 4 + 2 * 5) + (4 * 3 + 4 * 5) + (3 * 5)


def test_example_2_16():
    example = """
        2....
        .*...
        3.4..
    """
    r = run_game_2(example)

    assert r == 2 * 3 + 2 * 4 + 3 * 4


def test_example_2_17():
    example = """
        2.3.....1
        .*.......
    """
    r = run_game_2(example)

    assert r == 2 * 3


def test_example_2_18():
    example = """
        .*.......
        2.3.....1
    """
    r = run_game_2(example)

    assert r == 2 * 3


def test_example_2_19():
    example = """
        2.4......12.
        .*.........*
        3.5..503+.56
    """
    r = run_game_2(example)

    assert r == (2 * 3 + 2 * 4 + 2 * 5) + (4 * 3 + 4 * 5) + (3 * 5) + 12 * 56


def test_example_2_20():
    example = """
        .5.....23..$
        8...90*12...
        ............
    """
    r = run_game_2(example)

    assert r == 90 * 23 + 90 * 12 + 23 * 12


def test_example_2_21():
    example = """
        .....24.*23.
        ..10........
        ..397*.610..
        .......50...
        1*2.........
    """
    r = run_game_2(example)

    assert r == 2


def test_example_2_22():
    example = """
        .......5......
        ..7*..*.......
        ...*13*.......
        .......15.....
    """
    r = run_game_2(example)

    assert r == 442


def test_example_2_23():
    example = """
        12.......*..
        +.........34
        .......-12..
        ..78........
        ..*....60...
        78.........9
        .5.....23..$
        8...90*12...
        ............
        2.2......12.
        .*.........*
        1.1..503+.56
    """
    r = run_game_2(example)

    assert (
        r
        == 78 * 78
        + 90 * 23
        + 90 * 12
        + 23 * 12
        + (2 * 2 + 2 * 1 + 2 * 1)
        + (1 * 2 + 1 * 2)
        + (1 * 1)
        + 12 * 56
    )

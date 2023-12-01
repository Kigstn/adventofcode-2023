from day1.main import run


def test_example_1():
    examples = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    r = run(examples)
    assert r == 142


def test_example_2():
    examples = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]
    r = run(examples)
    assert r == 281

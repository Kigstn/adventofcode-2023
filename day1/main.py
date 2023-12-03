import re
from pathlib import Path

from helpers import readlines_from_input_file


def get_numbers(text: str) -> tuple[int, int]:
    to_replace = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    # find all numbers
    # using regex lookahead to catch overlaps
    digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", text)
    first, last = digits[0], digits[-1]

    # make a dict lookup for the value to see if it should be replaced
    # default (for all numerical numbers) is no - as they are not found
    return to_replace.get(first, first), to_replace.get(last, last)


def run(texts: list[str]) -> int:
    total = 0
    for text in texts:
        first, last = get_numbers(text)
        total += int(f"{first}{last}")

    return total


if __name__ == "__main__":
    texts = readlines_from_input_file(Path("input.txt"))
    print(f"Puzzle Solution: `{run(texts)}`")

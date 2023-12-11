import re
from pathlib import Path


from helpers import read_from_input_file, split_and_strip_input


def run_game_1(text: str) -> int:
    texts = split_and_strip_input(text)

    times = [int(x) for x in re.findall(r"\d+", texts[0])]
    destinations = [int(x) for x in re.findall(r"\d+", texts[1])]

    total = 1
    for time_available, wr_destination in zip(times, destinations):
        wins = 0

        for time_spend_pressing in range(time_available + 1):
            time_spend_driving = time_available - time_spend_pressing

            destination = time_spend_driving * time_spend_pressing

            if destination > wr_destination:
                wins += 1

        total *= wins
    return total


def run_game_2(text: str) -> int:
    texts = split_and_strip_input(text)

    time_available = int("".join(re.findall(r"\d+", texts[0])))
    wr_destination = int("".join(re.findall(r"\d+", texts[1])))

    wins = 0
    for time_spend_pressing in range(time_available + 1):
        time_spend_driving = time_available - time_spend_pressing

        destination = time_spend_driving * time_spend_pressing

        if destination > wr_destination:
            wins += 1

    return wins


if __name__ == "__main__":
    inputs = read_from_input_file(Path("./input.txt"))
    print(f"Puzzle 1 Solution: `{run_game_1(inputs)}`")
    print(f"Puzzle 2 Solution: `{run_game_2(inputs)}`")

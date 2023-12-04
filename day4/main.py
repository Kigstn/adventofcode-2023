import re
from collections import Counter
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from helpers import read_from_input_file, split_and_strip_input


class LineInfo(BaseModel):
    id: int

    winner_numbers: list[int]
    ours_numbers: list[int]

    matches: int

def parse_string(text: str) -> LineInfo:
    game_id = re.search(r"\d+(?=:)", text).group()

    winner_string = re.search(r"(?<=:).*(?=[|])", text).group()
    winner_numbers = re.findall(r"\d+", winner_string)

    ours_string = re.search(r"(?<=[|]).*", text).group()
    ours_numbers = re.findall(r"\d+", ours_string)

    # count the matches
    match_count = 0
    counter = Counter([*set(winner_numbers), *set(ours_numbers)])
    for _, n in counter.most_common():
        if n >= 2:
            match_count += 1

    return LineInfo(id=int(game_id),winner_numbers=winner_numbers, ours_numbers=ours_numbers, matches=match_count)


def run_game_1(text: str) -> int:
    texts = split_and_strip_input(text)

    total = 0
    for text in texts:
        info = parse_string(text)

        if info.matches >= 1:
            line_total = 1
            matches = info.matches - 1
            for _ in range(matches):
                line_total *= 2
        else:
            line_total = 0

        total += line_total

    return total


def run_game_2(text: str) -> int:
    texts = split_and_strip_input(text)

    line_infos = {}
    total = 0
    for text in texts:
        info = parse_string(text)
        line_infos[info.id] = info

    # initial list is the tasklist
    tasks = list(line_infos.values())
    while tasks:
        total += 1

        task = tasks.pop()

        # add the next n entries to the tasklist
        new_task_id = task.id
        for _ in range(task.matches):
            new_task_id += 1
            tasks.append(line_infos[new_task_id])

    return total


if __name__ == "__main__":
    inputs = read_from_input_file(Path("./input.txt"))
    print(f"Puzzle 1 Solution: `{run_game_1(inputs)}`")
    print(f"Puzzle 2 Solution: `{run_game_2(inputs)}`")

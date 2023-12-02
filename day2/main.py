import re
from pathlib import Path
from typing import Annotated

from pydantic import BaseModel, BeforeValidator

from helpers import read_from_input_file


def _converter(x: list[str]) -> int:
    return max([int(y) for y in x])


class TextInfo(BaseModel):
    id: int

    # only save the max value -> since they get put back
    red: Annotated[int, BeforeValidator(_converter)]
    blue: Annotated[int, BeforeValidator(_converter)]
    green: Annotated[int, BeforeValidator(_converter)]


def parse_string(text: str) -> TextInfo:
    # get the game id
    game_id = re.search(r"(?<=Game )\d+", text).group()

    # get blues
    blues = re.findall(r"\d+(?= blue)", text)
    # get reds
    reds = re.findall(r"\d+(?= red)", text)
    # get greens
    greens = re.findall(r"\d+(?= green)", text)

    return TextInfo(id=game_id, blue=blues, red=reds, green=greens)


def run_game_1(texts: list[str], red: int, green: int, blue: int) -> int:
    total = 0
    for text in texts:
        info = parse_string(text)

        # is the game valid? If yes, add to total
        if info.red <= red and info.green <= green and info.blue <= blue:
            total += info.id
    return total


def run_game_2(texts: list[str]) -> int:
    total = 0
    for text in texts:
        info = parse_string(text)

        # multiply the max values together
        game_total = info.red * info.blue * info.green
        total += game_total
    return total


if __name__ == "__main__":
    texts = read_from_input_file(Path("input.txt"))
    print(f"Puzzle 1 Solution: `{run_game_1(texts, red=12, green=13, blue=14)}`")
    print(f"Puzzle 2 Solution: `{run_game_2(texts)}`")

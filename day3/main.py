import re
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from helpers import read_from_input_file, split_and_strip_input


class LineInfo(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    text: str

    symbols: list[re.Match] = []
    numbers: list[re.Match] = []

    line_total: int = 0


def parse_string(text: str) -> LineInfo:
    result = LineInfo(text=text)

    # get the line total with regex
    for found in re.finditer(r"(?<=[^\d.])\d+|\d+(?![\d.]|\Z)", text):
        result.line_total += int(found.group())

    # get the numbers (for multi line matching) that have not been found before
    for found in re.finditer(r"(?<![^.])\d+(?![^.])", text):
        result.numbers.append(found)

    # get the symbols (for multi line matching)
    for found in re.finditer(r"[^\d.]", text):
        result.symbols.append(found)

    return result


def check_meeting_lines(line: LineInfo, other_line: LineInfo) -> set[re.Match]:
    found = set()

    for special_symbol in other_line.symbols:
        # add 1 to their position, as diagonal counts as well
        symbol_indexes = list(
            range(special_symbol.start() - 1, special_symbol.end() + 1)
        )

        for number in line.numbers:
            number_indexes = list(range(number.start(), number.end()))

            # do any of those indexes match?
            match = any([v in number_indexes for v in symbol_indexes])
            if match:
                found.add(number)

    return found


def check_same_gear_lines(line: LineInfo) -> int:
    # check same line

    total = 0
    for match in re.findall(r"(?<!\d)(?=(\d+[*]\d+))", line.text):
        total += eval(match)
    return total


def check_two_gear_lines(line: LineInfo, other_line: LineInfo) -> int:
    # check two different lines

    total = 0

    r"\d+[*]|[*]\d+"
    r"(?=(?=([*]\d+))|((?<=[^\d])\d+[*]))"
    for special_symbol in re.finditer(
        r"(?=(?=([*]\d+))|((?<=[^\d])\d+[*]))", line.text
    ):
        for group_n in [1, 2]:
            text = special_symbol.group(group_n)
            if text:
                break
        if text.startswith("*"):
            start = special_symbol.start(group_n) - 1
            end = start + 3
        else:
            end = special_symbol.end(group_n) + 1
            start = end - 3
        l_number = int(text.replace("*", ""))
        symbol_indexes = list(range(start, end))

        other_match = None
        for number in re.finditer(r"\d+", other_line.text):
            number_indexes = list(range(number.start(), number.end()))

            # do any of those indexes match?
            match = any([v in number_indexes for v in symbol_indexes])
            if match:
                other_match = number

        # if both the prev and after line have numbers, we found something!!
        if other_match:
            total += int(other_match.group()) * l_number

    return total


def check_three_gear_lines(
    line: LineInfo, prev_line: LineInfo, after_line: LineInfo, one_line: bool = False
) -> int:
    # check three different lines

    total = 0
    for special_symbol in line.symbols:
        if special_symbol.group() == "*":
            # add 1 to their position, as diagonal counts as well
            symbol_indexes = list(
                range(special_symbol.start() - 1, special_symbol.end() + 1)
            )

            prev_match = []
            for number in re.finditer(r"\d+", prev_line.text):
                number_indexes = list(range(number.start(), number.end()))

                # do any of those indexes match?
                match = any([v in number_indexes for v in symbol_indexes])
                if match:
                    prev_match.append(number)

            if one_line:
                if len(prev_match) == 2:
                    total += int(prev_match[0].group()) * int(prev_match[1].group())

            else:
                after_match = []
                for number in re.finditer(r"\d+", after_line.text):
                    number_indexes = list(range(number.start(), number.end()))

                    # do any of those indexes match?
                    match = any([v in number_indexes for v in symbol_indexes])
                    if match:
                        after_match.append(number)

                # if both the prev and after line have numbers, we found something!!
                if prev_match and after_match:
                    for m1 in prev_match:
                        for m2 in after_match:
                            total += int(m1.group()) * int(m2.group())

    return total


def run_game_1(text: str) -> int:
    texts = split_and_strip_input(text)

    line_infos = []
    total = 0
    for text in texts:
        info = parse_string(text)
        line_infos.append(info)

    # parse the gear matches
    for i, info in enumerate(line_infos):
        found = set()

        # prev line
        try:
            res = check_meeting_lines(info, line_infos[i - 1])
            found.update(res)
        except IndexError: ...

        # next line
        try:
            res = check_meeting_lines(info, line_infos[i + 1])
            found.update(res)
        except IndexError: ...

        # add to total
        for number in found:
            total += int(number.group())

    return total


def run_game_2(text: str) -> int:
    texts = split_and_strip_input(text)

    line_infos = []
    total = 0
    for text in texts:
        info = parse_string(text)
        total += info.line_total
        line_infos.append(info)

    # parse the diagonal gear matches
    total = 0
    for i, info in enumerate(line_infos):
        # get prev, after line
        try:
            index = i - 1
            if index < 0:
                raise IndexError
            prev_line = line_infos[index]
        except IndexError:
            prev_line = None
        try:
            after_line = line_infos[i + 1]
        except IndexError:
            after_line = None

        total += check_same_gear_lines(info)

        if prev_line:
            total += check_two_gear_lines(info, prev_line)
            total += check_three_gear_lines(info, prev_line, prev_line, one_line=True)

        if after_line:
            total += check_two_gear_lines(info, after_line)
            total += check_three_gear_lines(info, after_line, after_line, one_line=True)

        if prev_line and after_line:
            total += check_three_gear_lines(info, prev_line, after_line)

    return total


if __name__ == "__main__":
    inputs = read_from_input_file(Path("./input.txt"))
    print(f"Puzzle 1 Solution: `{run_game_1(inputs)}`")
    print(f"Puzzle 2 Solution: `{run_game_2(inputs)}`")

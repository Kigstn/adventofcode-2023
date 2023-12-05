import re
from pathlib import Path

import numpy
from pydantic import BaseModel

from helpers import read_from_input_file, split_and_strip_input


class Map(BaseModel):
    source: int
    destination: int
    range: int


def get_entries(texts: list[str]) -> list[Map]:
    res = []

    for text in texts:
        if not re.search("[a-z]", text):
            numbers = [int(x.strip()) for x in text.split()]
            dest_range = numbers[0]
            source_range = numbers[1]
            multiplier_range = numbers[2]

            res.append(
                Map(source=source_range, destination=dest_range, range=multiplier_range)
            )
        else:
            break
    return res


def get_instance(input_value: int, map_inst: list[Map]) -> int:
    for inst in map_inst:
        if inst.source <= input_value <= (inst.source + inst.range):
            modifier = input_value - inst.source
            return inst.destination + modifier
    return input_value


def run_game(texts: list[str], seeds: list[int]) -> int:
    map_seed_to_location: dict[int, int] = {}

    for i, text in enumerate(texts):
        if "seed-to-soil map" in text:
            map_seed_to_soil = get_entries(texts[i + 1 :])
        elif "soil-to-fertilizer" in text:
            map_soil_to_fertilizer = get_entries(texts[i + 1 :])
        elif "fertilizer-to-water" in text:
            map_fertilizer_to_water = get_entries(texts[i + 1 :])
        elif "water-to-light map" in text:
            map_water_to_light = get_entries(texts[i + 1 :])
        elif "light-to-temperature map" in text:
            map_light_to_temperature = get_entries(texts[i + 1 :])
        elif "temperature-to-humidity map" in text:
            map_temperature_to_humidity = get_entries(texts[i + 1 :])
        elif "humidity-to-location map" in text:
            map_humidity_to_location = get_entries(texts[i + 1 :])

    for seed in seeds:
        soil = get_instance(seed, map_seed_to_soil)  # noqa
        fertilizer = get_instance(soil, map_soil_to_fertilizer)  # noqa
        water = get_instance(fertilizer, map_fertilizer_to_water)  # noqa
        light = get_instance(water, map_water_to_light)  # noqa
        temperature = get_instance(light, map_light_to_temperature)  # noqa
        humidity = get_instance(temperature, map_temperature_to_humidity)  # noqa
        location = get_instance(humidity, map_humidity_to_location)  # noqa

        map_seed_to_location[seed] = location

    return min(map_seed_to_location.values())


def run_game_1(text: str) -> int:
    texts = split_and_strip_input(text)

    seeds = [int(x.strip()) for x in texts[0].split(":")[1].split()]

    return run_game(texts[1:], seeds)


def run_game_2(text: str) -> int:
    texts = split_and_strip_input(text)

    seeds_range = re.findall(r"\d+ \d+", texts[0])
    seeds = None
    for seed in seeds_range:
        number = int(seed.split()[0])
        seed_range = int(seed.split()[1])
        seed_vals = numpy.arange(seed_range)
        seed_vals += number
        if seeds is None:
            seeds = seed_vals
        else:
            seeds = numpy.append(seeds, seed_vals)

    return run_game(texts[1:], seeds)


if __name__ == "__main__":
    inputs = read_from_input_file(Path("./input.txt"))
    print(f"Puzzle 1 Solution: `{run_game_1(inputs)}`")
    print(f"Puzzle 2 Solution: `{run_game_2(inputs)}`")

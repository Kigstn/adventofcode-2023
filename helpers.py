from pathlib import Path


def read_from_input_file(path: Path) -> list[str]:
    with open(path) as f:
        return f.readlines()

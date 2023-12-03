from pathlib import Path


def read_from_input_file(path: Path) -> str:
    with open(path) as f:
        return f.read()


def readlines_from_input_file(path: Path) -> list[str]:
    with open(path) as f:
        return f.readlines()


def split_and_strip_input(text: str) -> list[str]:
    texts = text.split("\n")
    return [t.strip() for t in texts if t.strip()]

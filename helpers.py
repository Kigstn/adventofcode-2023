from pathlib import Path


def read_from_input_file(path: Path) -> str:
    with open(path) as f:
        return f.read()


def readlines_from_input_file(path: Path) -> list[str]:
    with open(path) as f:
        return f.readlines()


def split_and_strip_input(text: str) -> list[str]:
    return strip_input(text).split("\n")


def strip_input(text: str) -> str:
    texts = text.split("\n")
    cleaned = [t.strip() for t in texts if t.strip()]
    return "\n".join(cleaned)

from pathlib import Path
from typing import Iterator


def get_file_path(filename: str) -> Path:
    path_2023 = Path(__file__).parent.parent.parent
    return path_2023 / filename


def iterate_input_lines(case, ignore_commented_lines=True) -> Iterator[str]:
    with open(case) as input_file:
        for line in input_file:
            if not ignore_commented_lines or not line.startswith("#"):
                yield line.strip()


from typing import Iterator


def iterate_input_lines(case, ignore_commented_lines=True) -> Iterator[str]:
    with open(case) as input_file:
        for line in input_file:
            if not ignore_commented_lines or not line.startswith("#"):
                yield line.strip()


from typing import Iterator


def iterate_input_lines(case) -> Iterator[str]:
    with open(case) as input_file:
        for line in input_file:
            if not line.startswith("#"):
                yield line.strip()

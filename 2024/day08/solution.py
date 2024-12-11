import string

import numpy as np
import polars as pl


def __read_fwf(input_file_path):
    # see https://medium.com/@arkimetrix.analytics/part-7-python-polars-working-with-fixed-width-files-edge-case-9a7b1e710b98
    df = pl.read_csv(input_file_path, has_header=False, skip_rows=0, new_columns=["full_str"])

    file_width = 12  # TODO this could be read from the first line of the file
    column_names = [f"{i}" for i in range(file_width)]
    widths = [1] * file_width

    # Calculate slice values from widths.
    slice_tuples = []
    offset = 0

    for i in widths:
        slice_tuples.append((offset, i))
        offset += i

    return df.with_columns(
        [
            pl.col("full_str").str.slice(slice_tuple[0], slice_tuple[1]).str.strip_chars().alias(col)
            for slice_tuple, col in zip(slice_tuples, column_names)
        ]
    ).drop("full_str")


def part1(input_file_path):
    puzzle_input = __read_fwf(input_file_path)
    antenna_map = puzzle_input.to_numpy()
    antinode_map = np.zeros_like(antenna_map)
    for char in string.ascii_uppercase + string.ascii_lowercase + string.digits:
        pass

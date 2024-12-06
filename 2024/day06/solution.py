import polars as pl
import numpy as np


def __read_fwf(input_file_path):
    # see https://medium.com/@arkimetrix.analytics/part-7-python-polars-working-with-fixed-width-files-edge-case-9a7b1e710b98
    df = pl.read_csv(input_file_path, has_header=False, skip_rows=0, new_columns=["full_str"])

    file_width = 130  # TODO this could be read from the first line of the file
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
    floor_map = puzzle_input.to_numpy()
    coordinates = np.where(floor_map == "^")
    coordinates_list = list(zip(coordinates[0], coordinates[1]))
    # we know there will be only one coordinate
    guard_position = coordinates_list[0]
    direction = "up"
    num_of_guard_positions = 1  # the first start position
    guard_coordinates = {guard_position}
    encountered_block = True

    def find_path(path):
        coordinates = np.where(path == "#")
        if len(coordinates[0]) == 0:
            return len(path), False
        return coordinates[0][0], True

    while encountered_block:

        if direction == "up":
            check_column = floor_map[:, guard_position[1]]
            check_path = np.flip(check_column[: guard_position[0]])
            num_of_steps, encountered_block = find_path(check_path)
            num_of_guard_positions += num_of_steps
            guard_coordinates = guard_coordinates.union(
                {(guard_position[0] - (i + 1), guard_position[1]) for i in range(num_of_steps)}
            )
            print(f"{num_of_steps} steps encountered")
            if encountered_block:
                guard_position = (guard_position[0] - num_of_steps, guard_position[1])
                direction = "right"
        elif direction == "right":
            check_row = floor_map[guard_position[0], :]
            check_path = check_row[guard_position[1] + 1 :]
            num_of_steps, encountered_block = find_path(check_path)
            num_of_guard_positions += num_of_steps
            guard_coordinates = guard_coordinates.union(
                {(guard_position[0], guard_position[1] + (i + 1)) for i in range(num_of_steps)}
            )
            print(f"{num_of_steps} steps encountered")
            if encountered_block:
                guard_position = (guard_position[0], guard_position[1] + num_of_steps)
                direction = "down"
        elif direction == "down":
            check_column = floor_map[:, guard_position[1]]
            check_path = check_column[guard_position[0] + 1 :]
            num_of_steps, encountered_block = find_path(check_path)
            num_of_guard_positions += num_of_steps
            guard_coordinates = guard_coordinates.union(
                {(guard_position[0] + (i + 1), guard_position[1]) for i in range(num_of_steps)}
            )
            print(f"{num_of_steps} steps encountered")
            if encountered_block:
                guard_position = (guard_position[0] + num_of_steps, guard_position[1])
                direction = "left"
        elif direction == "left":
            check_row = floor_map[guard_position[0], :]
            check_path = np.flip(check_row[: guard_position[1]])
            num_of_steps, encountered_block = find_path(check_path)
            num_of_guard_positions += num_of_steps
            guard_coordinates = guard_coordinates.union(
                {(guard_position[0], guard_position[1] - (i + 1)) for i in range(num_of_steps)}
            )
            print(f"{num_of_steps} steps encountered")
            if encountered_block:
                guard_position = (guard_position[0], guard_position[1] - num_of_steps)
                direction = "up"

    print(len(guard_coordinates))


if __name__ == '__main__':
    part1('input.txt')

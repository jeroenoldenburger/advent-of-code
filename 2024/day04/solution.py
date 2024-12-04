import numpy as np
import polars as pl


def __read_fwf(input_file_path):
    # see https://medium.com/@arkimetrix.analytics/part-7-python-polars-working-with-fixed-width-files-edge-case-9a7b1e710b98
    # for the initial idea
    # changes TODO:
    # - detect num of columns by the first line
    # - don't name columns as we don't need them
    df = pl.read_csv(input_file_path, has_header=False, skip_rows=0, new_columns=["full_str"])

    column_names = [f"{i}" for i in range(140)]
    widths = [1] * 140

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
    df = __read_fwf(input_file_path)
    matrix = df.to_numpy()
    num_of_rows = matrix.shape[0]
    num_of_xmas = 0

    word_to_find = "XMAS"

    # check matrix horizontally
    for line in matrix:
        line_as_string = ''.join(line)
        # left to right
        l_to_r = line_as_string.count("XMAS")
        num_of_xmas += l_to_r
        # right to left
        r_to_l = line_as_string[::-1].count("XMAS")
        num_of_xmas += r_to_l
        print(f"row - l_to_r: {l_to_r} - r_to_l: {r_to_l} - num_of_xmas: {num_of_xmas}")
    # check matrix "vertically"
    matrix2 = np.transpose(matrix)
    for line in matrix2:
        line_as_string = ''.join(line)
        # top to bottom
        l_to_r = line_as_string.count("XMAS")
        num_of_xmas += l_to_r
        # bottom to top
        r_to_l = line_as_string[::-1].count("XMAS")
        num_of_xmas += r_to_l
        print(f"column - t_to_b: {l_to_r} - b_to_t: {r_to_l} - num_of_xmas: {num_of_xmas}")

    # get left-right diagonals
    list_ = [''.join(np.diag(matrix, k=i).tolist()) for i in range(-num_of_rows + 1, num_of_rows)]
    for diag in list_:
        # bottom to top
        num_of_xmas += diag.count("XMAS")
        # top to bottom
        num_of_xmas += diag[::-1].count("XMAS")
    # get right-left reverse diagonals
    matrix3 = np.flipud(matrix)
    list_ = [''.join(np.diag(matrix3, k=i).tolist()) for i in range(-num_of_rows + 1, num_of_rows)]
    for diag in list_:
        # bottom to top
        num_of_xmas += diag.count("XMAS")
        # top to bottom
        num_of_xmas += diag[::-1].count("XMAS")

    print(num_of_xmas)


if __name__ == '__main__':
    part1("input.txt")
    exit(0)

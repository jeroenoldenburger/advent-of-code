import re

import numpy as np
import polars as pl


def __read_fwf(input_file_path):
    # see https://medium.com/@arkimetrix.analytics/part-7-python-polars-working-with-fixed-width-files-edge-case-9a7b1e710b98
    df = pl.read_csv(input_file_path, has_header=False, skip_rows=0, new_columns=["full_str"])

    file_width = 140  # TODO this could be read from the first line of the file
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


def __find_in_source(source, term):
    # left to right
    l_to_r = source.count(term)
    # right to left
    r_to_l = source[::-1].count(term)
    print(f"l_to_r: {l_to_r} - r_to_l: {r_to_l}")
    return l_to_r + r_to_l


def part1(input_file_path):
    df = __read_fwf(input_file_path)
    matrix = df.to_numpy()
    num_of_rows = matrix.shape[0]
    num_of_xmas = 0
    word_to_find = "XMAS"
    # check matrix horizontally
    for row in matrix:
        print("row")
        num_of_xmas += __find_in_source(''.join(row), word_to_find)
    # check matrix "vertically"
    matrix2 = np.transpose(matrix)
    for column in matrix2:
        print("column")
        num_of_xmas += __find_in_source(''.join(column), word_to_find)
    # get left-right diagonals
    list_ = [''.join(np.diag(matrix, k=i).tolist()) for i in range(-num_of_rows + 1, num_of_rows)]
    for diag in list_:
        print("diag l to r")
        num_of_xmas += __find_in_source(diag, word_to_find)
    # get right-left reverse diagonals
    matrix3 = np.flipud(matrix)
    list_ = [''.join(np.diag(matrix3, k=i).tolist()) for i in range(-num_of_rows + 1, num_of_rows)]
    for diag in list_:
        print("diag r to l")
        num_of_xmas += __find_in_source(diag, word_to_find)

    print(num_of_xmas)


def __find_positions(source, term):
    return [m.start() for m in re.finditer(f'(?={term})', source)]


def part2(input_file_path):
    df = __read_fwf(input_file_path)
    matrix = df.to_numpy()
    num_of_rows = matrix.shape[0]
    word_to_find = "MAS"
    # get right-left diagonals, starting from bottom
    for i in range(-num_of_rows + 1, num_of_rows):
        diag = ''.join(np.diag(matrix, k=i).tolist())
        print("######")
        print(diag)
        # find matches reading diagonal from left to right
        starts = __find_positions(diag, term=word_to_find)
        if starts:
            # find middles
            if i <= 0:
                # find zero base row and column indexes for the middle of MAS
                row = abs(i)
                # print middles
                for start in starts:
                    num_of_steps = start + 1
                    print(f"row: {row+num_of_steps}, column: {num_of_steps}")
            else:
                above_zero_rows = i
                row = -above_zero_rows
                # print middles
                for start in starts:
                    num_of_steps = len(diag) - start + 1
                    print(f"az row: {row+num_of_steps}, column: {num_of_steps}")

        # find matches reading diagonal from right to left
        print("-------")
        starts = __find_positions(diag[::-1], term=word_to_find)
        if starts:
            # find middles
            if i <= 0:
                # find zero base row and column indexes for the middle of MAS
                row = abs(i)
                # print middles
                for start in starts:
                    num_of_steps = len(diag) - start - 1
                    print(f"row: {row + num_of_steps}, column: {num_of_steps}")

        # starts += __find_positions(diag[::-1], term=word_to_find)

    # list_ = [''.join(np.diag(matrix, k=i).tolist()) for i in range(-num_of_rows + 1, num_of_rows)]
    # for diag in list_:
    #     print("diag l to r")
    #     num_of_xmas += __find_in_source(diag, word_to_find)
    # # get right-left reverse diagonals
    # matrix3 = np.flipud(matrix)
    # list_ = [''.join(np.diag(matrix3, k=i).tolist()) for i in range(-num_of_rows + 1, num_of_rows)]
    # for diag in list_:
    #     print("diag r to l")
    #     num_of_xmas += __find_in_source(diag, word_to_find)
    #
    # print(num_of_xmas)


if __name__ == '__main__':
    part2("example.txt")
    exit(0)

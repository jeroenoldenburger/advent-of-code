import copy

import polars as pl

from common import iterate_input_lines


def __get_puzzle_input(input_file_path) -> pl.DataFrame:
    # the input uses multiple spaces as separator
    # polars can only use single byte separator
    # therefore we need to use space a separator and ignore the extra columns that originate
    # from the additional spaces
    return pl.scan_csv(input_file_path, separator=" ", has_header=False).collect()


def part1(input_file_path):
    reports = pl.scan_csv(
        input_file_path, separator=" ", has_header=False, new_columns=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    )

    ever_incr = (
        (pl.col("1") > pl.col("2"))
        & (pl.col("2") > pl.col("3"))
        & (pl.col("3") > pl.col("4"))
        & (pl.col("4") > pl.col("5"))
    )
    ever_decl = (
        (pl.col("1") < pl.col("2"))
        & (pl.col("2") < pl.col("3"))
        & (pl.col("3") < pl.col("4"))
        & (pl.col("4") < pl.col("5"))
    )
    step_size_within_limits = (
        ((pl.col("1") - pl.col("2")).abs() < 4)
        & ((pl.col("2") - pl.col("3")).abs() < 4)
        & ((pl.col("3") - pl.col("4")).abs() < 4)
        & ((pl.col("4") - pl.col("5")).abs() < 4)
    )

    valid_reports = reports.filter((ever_incr | ever_decl)).filter(step_size_within_limits).collect()

    print(len(valid_reports))


def part1_pure_python(input_file_path):
    def is_incr(mylist: list[int]) -> bool:
        for idx, entry in enumerate(mylist):
            if idx > 0:
                if entry <= mylist[idx - 1]:
                    return False
        else:
            return True

    def is_decl(mylist: list[int]) -> bool:
        for idx, entry in enumerate(mylist):
            if idx > 0:
                if entry >= mylist[idx - 1]:
                    return False
        else:
            return True

    def step_size_limit(mylist: list[int]) -> bool:
        for idx, entry in enumerate(mylist):
            if idx > 0:
                if abs(entry - mylist[idx - 1]) > 3:
                    return False
        else:
            return True

    valid_reports = 0
    for line in iterate_input_lines(input_file_path):
        cols = [int(x) for x in line.split(" ")]
        if is_incr(cols) | is_decl(cols):
            if step_size_limit(cols):
                valid_reports += 1
    print(valid_reports)


def part2_pure_python(input_file_path):
    def is_incr(mylist: list[int], allow_retry=True) -> bool:
        for idx, entry in enumerate(mylist):
            if idx > 0:
                if entry <= mylist[idx - 1]:
                    if allow_retry:
                        newlist = copy.deepcopy(mylist)
                        newlist.pop(idx)
                        return is_incr(newlist, allow_retry=False)
                    return False
        else:
            return True

    def is_decl(mylist: list[int], allow_retry=True) -> bool:

        for idx, entry in enumerate(mylist):
            if idx > 0:
                if entry >= mylist[idx - 1]:
                    if allow_retry:
                        newlist = copy.deepcopy(mylist)
                        newlist.pop(idx)
                        return is_decl(newlist, allow_retry=False)
                    return False
        else:
            return True

    def step_size_limit(mylist: list[int], allow_retry=True) -> bool:
        for idx, entry in enumerate(mylist):
            if idx > 0:
                if abs(entry - mylist[idx - 1]) > 3:
                    if allow_retry:
                        newlist = copy.deepcopy(mylist)
                        newlist.pop(idx)
                        return step_size_limit(newlist, allow_retry=False)
                    return False
        else:
            return True

    valid_reports = 0
    for line in iterate_input_lines(input_file_path):
        cols = [int(x) for x in line.split(" ")]
        if is_incr(cols) | is_decl(cols):
            if step_size_limit(cols):
                valid_reports += 1
    print(valid_reports)


if __name__ == '__main__':
    part2_pure_python("input.txt")

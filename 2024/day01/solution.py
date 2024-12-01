# today is a matter of reading in lines, splitting into 2 array, sorting those arrays, computation of arrays
# feels like a perfect day for testing out polars https://pola.rs/
import polars as pl


def __get_puzzle_input(input_file_path) -> pl.DataFrame:
    # the input uses multiple spaces as separator
    # polars can only use single byte separator
    # therefore we need to use space a separator and ignore the extra columns that originate
    # from the additional spaces
    return (
        pl.scan_csv(input_file_path, separator=" ", has_header=False, new_columns=["first", "_", "__", "second"])
        .select(["first", "second"])
        .collect()
    )


def part1(input_file_path) -> None:
    puzzle_input = __get_puzzle_input(input_file_path)
    puzzle_input: pl.DataFrame = pl.DataFrame(
        {"first": puzzle_input["first"].sort(), "second": puzzle_input["second"].sort()}
    )
    distance: pl.Series = puzzle_input.fold(lambda first, second: abs(first - second))
    print(distance.sum())


def part2(input_file_path) -> None:
    puzzle_input = __get_puzzle_input(input_file_path)
    second: list[int] = puzzle_input["second"].to_list()
    print(sum([second.count(row["first"]) * row["first"] for row in puzzle_input.rows(named=True)]))


if __name__ == '__main__':
    part2("input.txt")

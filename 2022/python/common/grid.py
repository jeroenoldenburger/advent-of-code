from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


class Grid:
    grid: [[]]
    x_offset: int = 0
    y_offset: int = 0
    new_col: Any = None

    def __init__(self):
        self.grid = []
    #     self.x_offset = 0
    #     self.y_offset = 0

    def new_row(self):
        if len(self.grid):
            return [self.new_col for _ in self.grid[0]]
        else:
            return []

    def get_row_col(self, coord: Coordinate, grow_grid=True):
        row_idx = coord.y  + self.y_offset
        col_idx = coord.x + self.x_offset
        row_count = len(self.grid) - 1
        if row_idx < 0:
            if not grow_grid:
                raise ValueError("coord is not inside the grid")
            # grow the grid on the top
            amount_extra_rows = 0 - row_idx
            new_rows = [self.new_row() for _ in range(amount_extra_rows)]
            self.grid =  new_rows + self.grid
            self.y_offset += amount_extra_rows
            row_idx += self.y_offset
        if row_idx > row_count:
            if not grow_grid:
                raise ValueError("coord is not inside the grid")
            # grow the grid on the bottom
            amount_extra_rows = row_idx - row_count
            new_rows = [self.new_row() for _ in range(amount_extra_rows)]
            self.grid = self.grid + new_rows
        if col_idx < 0:
            if not grow_grid:
                raise ValueError("coord is not inside the grid")
            # grow the grid on the left
            amount_extra_cols = 0 - col_idx
            new_cols = [self.new_col for _ in range(amount_extra_cols)]
            self.grid = [new_cols + row for row in self.grid]
            self.x_offset += amount_extra_cols
            col_idx += self.x_offset
        col_count = len(self.grid[0]) - 1
        if col_idx > col_count:
            if not grow_grid:
                raise ValueError("coord is not inside the grid")
            #grow the grid on the right
            amount_extra_cols = col_idx - col_count
            new_cols = [self.new_col for _ in range(amount_extra_cols)]
            self.grid = [row + new_cols for row in self.grid]
        return row_idx, col_idx

    def draw(self, to_file=None):
        if to_file:
            output = open(to_file, 'w')
            for row in self.grid:
                output.write(self._draw_row(row) + "\n")
            output.close()
        else:
            for row in self.grid:
                print(self._draw_row(row))

    def _draw_row(self, row):
        return "".join(row)
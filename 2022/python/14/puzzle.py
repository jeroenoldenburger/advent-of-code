import copy

from common import iterate_input_lines

def get_rock_structures(case):
    structures = []
    for line in iterate_input_lines(case):
        structure = []
        for point in line.split("->"):
            x, y = point.strip().split(",")
            structure.append((int(x),int(y)))
        structures.append(structure)
    return structures


class Scan:
    grid: [[str]]
    x_transform: int

    def __init__(self, structures):
        x_points = [point[0] for structure in structures for point in structure]
        y_points = [point[1] for structure in structures for point in structure]
        self.x_transform = min(x_points)
        self.grid = []
        for _ in range(max(y_points) + 1):
            self.grid.append(["air" for __ in range(max(x_points) - self.x_transform + 1)])
        for structure in structures:
            x = None
            y = None
            for point in structure:
                if point[0] != x:
                    new_x = point[0]
                    if x is not None:
                        for line_x in range(min(x, new_x), max(x, new_x)+1):
                            self.grid[y][line_x - self.x_transform] = "rock"
                    x = new_x
                    if y is None:
                        # first point in path
                        y = point[1]
                        self.grid[y][x - self.x_transform] = "rock"
                elif point[1] != y:
                    new_y = point[1]
                    if y is not None:
                        for line_y in range(min(y, new_y), max(y, new_y)+1):
                            self.grid[line_y][x - self.x_transform] = "rock"
                    y = new_y
                else:
                    if x is not None:
                        raise ValueError("paths are only drawn in straight lines")

    def draw(self, grain_pos=None):
        if not hasattr(self, 'output_counter'):
            self.output_counter = 0
        self.output_counter += 1
        encoding = {
            "rock": '⬜',
            "sand": '🟡',
            "air": '⬛',
            "grain": '🔻',
        }
        draw_grid = copy.deepcopy(self.grid)
        if grain_pos:
            draw_grid[grain_pos[1]][grain_pos[0]] = "grain"
        with open(f"output/{self.output_counter}.txt", 'w') as output:
            for row in draw_grid:
                output.write("".join([encoding[col] for col in row]) + "\n")

    """
    pouring_point: [x, y]
    """
    def pour_sand(self, pouring_point:[int, int]):
        unit_of_sands = 0
        sand_falls_into_the_void = False
        x_min = 0
        x_max = len(self.grid[0]) - 1
        y_max = len(self.grid) - 1
        while not sand_falls_into_the_void:
            unit_of_sands += 1
            # loop until unit of sand is stuck
            unit_x, unit_y = pouring_point
            unit_x -= self.x_transform
            while True:
                if self.grid[unit_y + 1][unit_x] == "air":
                    unit_y += 1
                elif unit_x > x_min and self.grid[unit_y + 1][unit_x - 1] == "air":
                    unit_y += 1
                    unit_x -= 1
                elif unit_x < x_max and self.grid[unit_y + 1][unit_x + 1] == "air":
                    unit_y += 1
                    unit_x += 1
                else:
                    if unit_x == x_min or unit_x == x_max:
                        sand_falls_into_the_void = True
                        break
                    # sand is stuck
                    self.grid[unit_y][unit_x] = "sand"
                    break
                if unit_y == y_max:
                    sand_falls_into_the_void = True
                    break
        # -1 because the last unit felt into the void
        return unit_of_sands - 1


    def pour_sand2(self, pouring_point:[int, int]):
        unit_of_sands = 0
        sand_falls_into_the_void = False
        x_min = 0
        x_max = len(self.grid[0]) - 1
        y_max = len(self.grid) - 1
        while not sand_falls_into_the_void:
            unit_of_sands += 1
            # loop until unit of sand is stuck
            unit_x, unit_y = pouring_point
            unit_x -= self.x_transform
            while True:
                if unit_x == x_min:
                    # grow cave left-side
                    self.grid = [["air"] + row for row in self.grid]
                    self.grid[-1][0] = "rock"
                    x_max = len(self.grid[0]) - 1
                    unit_x += 1
                    pouring_point[0] += 1
                elif unit_x == x_max:
                    # grow cave right-side
                    self.grid = [row + ["air"] for row in self.grid]
                    self.grid[-1][-1] = "rock"
                    x_max = len(self.grid[0]) - 1

                if self.grid[unit_y + 1][unit_x] == "air":
                    unit_y += 1
                elif self.grid[unit_y + 1][unit_x - 1] == "air":
                    unit_y += 1
                    unit_x -= 1
                elif self.grid[unit_y + 1][unit_x + 1] == "air":
                    unit_y += 1
                    unit_x += 1
                else:
                    if unit_x == (pouring_point[0] - self.x_transform) and unit_y == pouring_point[1]:
                        sand_falls_into_the_void = True
                        break
                    # sand is stuck
                    self.grid[unit_y][unit_x] = "sand"
                    break
                if unit_y == y_max:
                    sand_falls_into_the_void = True
                    break
        return unit_of_sands


def solve(case):
    structures = get_rock_structures(case)
    scan = Scan(structures)
    units = scan.pour_sand([500,0])
    scan.draw()
    print(units)


def solve2(case):
    structures = get_rock_structures(case)
    scan = Scan(structures)
    scan.grid = scan.grid + [["air" for _ in scan.grid[0]],["rock" for _ in scan.grid[0]]]
    units = scan.pour_sand2([500,0])
    scan.draw()
    print(units)



if __name__ == '__main__':
    solve2("input.txt")
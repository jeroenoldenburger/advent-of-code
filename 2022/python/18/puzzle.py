from functools import lru_cache
from common import iterate_input_lines
import numpy as np

cubes = set()
count_coord_dimensions = 3
dimension_min = [0 for _ in range(count_coord_dimensions)]
dimension_max = [0 for _ in range(count_coord_dimensions)]

def get_cubes(case):
    for line in iterate_input_lines(case):
        x, y, z = map(int, line.split(","))
        cubes.add((x, y, z))
    for dim_idx in range(count_coord_dimensions):
        dimension_min[dim_idx] =  min(cubes, key=lambda cube:cube[dim_idx])[dim_idx]
        dimension_max[dim_idx] =  max(cubes, key=lambda cube:cube[dim_idx])[dim_idx]

def get_neighbour(cube:np.array, dimension:int, direction:int):
    delta = np.array([0, 0, 0])
    delta[dimension] = direction
    return tuple(cube + delta)

def relative_position_filled(cube:np.array, dimension:int, steps:int):
    nbr = get_neighbour(cube, dimension, steps)
    return nbr in cubes


@lru_cache(None)
def dfs_to_outside_grid(cube):
    stack = [cube]
    seen = set()
    if cube in cubes:
        return False
    while len(stack) > 0:
        cube_to_check = stack.pop()
        if cube_to_check in cubes:
            # this direction is block, maybe other is still possible
            continue
        for dim_idx in range(count_coord_dimensions):
            if not (dimension_min[dim_idx] <= cube_to_check[dim_idx] <= dimension_max[dim_idx]):
                return True
        if cube_to_check in seen:
            continue
        seen.add(cube_to_check)
        for dim_idx in range(count_coord_dimensions):
            stack.append(get_neighbour(cube_to_check, dim_idx, 1))
            stack.append(get_neighbour(cube_to_check, dim_idx, -1))

    return False


def solve(case):
    get_cubes(case)
    visible_sides = 0
    for cube in cubes:
        sides_covered = 0
        cube_coordinate = np.array(cube)
        for dim_idx in range(count_coord_dimensions):
            sides_covered += relative_position_filled(cube_coordinate, dim_idx, 1)
            sides_covered += relative_position_filled(cube_coordinate, dim_idx, -1)
        visible_sides += 6 - sides_covered

    return visible_sides


def solve2(case):
    get_cubes(case)
    visible_sides = 0
    for cube in cubes:
        cube_coordinate = np.array(cube)
        for dim_idx in range(count_coord_dimensions):
            visible_sides += dfs_to_outside_grid(get_neighbour(cube_coordinate,dim_idx,1))
            visible_sides += dfs_to_outside_grid(get_neighbour(cube_coordinate,dim_idx,-1))
    return visible_sides


if __name__ == '__main__':
    print(solve2("input.txt"))
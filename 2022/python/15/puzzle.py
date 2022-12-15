import math
from dataclasses import dataclass
from enum import Enum
from common import iterate_input_lines
from common.grid import Grid, Coordinate


def get_xy_input(input):
    x_input, y_input = input.split(',')
    return int(x_input.split('=')[1]), int(y_input.split('=')[1])

@dataclass(frozen=True)
class Location:
    sensor_coord: Coordinate
    closest_beacon_coord: Coordinate

def get_locations(case) -> [Location]:
    locations = []
    for line in iterate_input_lines(case):
        sensor_input, beacon_input = line.split(":")
        sensor_coord = get_xy_input(sensor_input)
        beacon_coord = get_xy_input(beacon_input)
        locations.append(Location(Coordinate(*sensor_coord), Coordinate(*beacon_coord)))
    return locations


def manhattan_distance(coord1: Coordinate, coord2: Coordinate):
    x_dist = math.dist([coord1.x], [coord2.x])
    y_dist = math.dist([coord1.y], [coord2.y])
    return int(x_dist) + int(y_dist)

def coords_within_manhattan_distance(coord: Coordinate, distance: int):
    coords = set([])
    distance += 2  # distance + start and end
    for delta_x in range(distance):
        delta_y = distance - delta_x
        for x in range(delta_x):
            for y in range(delta_y):
                coords.update([
                    Coordinate(coord.x + x, coord.y + y),
                    Coordinate(coord.x + x, coord.y - y),
                    Coordinate(coord.x - x, coord.y + y),
                    Coordinate(coord.x - x, coord.y - y)
                ])
    return coords

class Position(Enum):
    unknown = 0
    sensor = 1
    beacon = 2
    no_beacon = 3


class Map(Grid):
    new_col = Position.unknown
    encoding = {
        Position.unknown: '.',
        Position.sensor: 'S',
        Position.beacon: 'B',
        Position.no_beacon: '#'
    }

    def __init__(self, locations:[Location]):
        super().__init__()
        for location in locations:
            row, col = self.get_row_col(location.sensor_coord)
            self.grid[row][col] = Position.sensor
            row, col = self.get_row_col(location.closest_beacon_coord)
            self.grid[row][col] = Position.beacon
        for location in locations:
            dist = manhattan_distance(location.sensor_coord, location.closest_beacon_coord)
            for coord_at_dist in coords_within_manhattan_distance(location.sensor_coord, dist):
                try:
                    row, col = self.get_row_col(coord_at_dist)
                    if self.grid[row][col] == Position.unknown:
                        self.grid[row][col] = Position.no_beacon
                except ValueError:
                    pass

    def _draw_row(self, row):
        return "".join([self.encoding[pos] for pos in row])




def solve(case):
    locations = get_locations(case)
    map = Map(locations)
    row, _ = map.get_row_col(Coordinate(0,10))
    print(sum([1 for col in map.grid[row] if col == Position.no_beacon]))
    # map.draw(f"output/{case}")

if __name__ == '__main__':
    # solve("test1.txt")
    # solve("test2.txt")
    # solve("test3.txt")
    # solve("test4.txt")
    # solve("test5.txt")
    # solve("example2.txt")
    # solve("example3.txt")
    solve("input.txt")
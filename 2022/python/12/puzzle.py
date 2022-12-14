from dataclasses import dataclass
from common import iterate_input_lines

# THIS puzzle is not solved (yet)
# first tried networkx, found out that shortest path analysis couldn't check constraints
# and i made an error somewhere in the second attempt below ...

@dataclass
class Coordinate:
    x: int
    y: int

    def __hash__(self):
        return hash(f"{self.x},{self.y}")


@dataclass
class Point:
    char: str
    height: int


@dataclass
class HeightMap:
    start: Coordinate
    end: Coordinate
    grid:[[Point]]

    def __init__(self):
        self.grid = []

    def neighbours(self, origin: Coordinate):
        return [
            Coordinate(x, y)
            for (x, y) in [
                (origin.x - 1, origin.y), (origin.x + 1, origin.y),
                (origin.x, origin.y - 1), (origin.x, origin.y + 1)
            ]
            if 0 <= y < len(self.grid[0]) and 0 <= x < len(self.grid)
        ]

    def valid_neighbours(self, origin: Coordinate):
        max_height = self.point(origin).height + 1
        return [
            coord
            for coord in self.neighbours(origin)
            if self.point(coord).height <= max_height
        ]

    def point(self, coordinate: Coordinate):
        return self.grid[coordinate.x][coordinate.y]

    def find_path_length(self):
        queue: list[tuple[int, Coordinate, Coordinate]] = [(0, self.start, self.start)]
        visited = set([])
        while queue:
            steps, curr_coord, prev_coord = queue.pop(0)
            if curr_coord not in visited:
                visited.add(curr_coord)
                if curr_coord == self.end:
                    break
                else:
                    steps += 1
                    for next_coord in self.valid_neighbours(curr_coord):
                        queue.append((steps, next_coord, curr_coord))
                    queue.sort(key=lambda l: l[0])
        return steps

    def print(self):
        print("\n".join([ "".join([ col.char for col in row]) for row in self.grid]))

    def print_visited(self, visited):
        print("\n".join([ "".join([ "#" if Coordinate(x,y) in visited else "." for x, col in enumerate(row)]) for y, row in enumerate(self.grid)]))


def parse_input(case):
    map = HeightMap()
    for row, line in enumerate(iterate_input_lines(case)):
        map.grid.append([])
        for col, char in enumerate(line):
            if char == "S":
                height_char = 'a'
                map.start = Coordinate(y=row, x=col)
            elif char == "E":
                height_char = 'z'
                map.end = Coordinate(y=row, x=col)
            else:
                height_char = char
            map.grid[-1] += [Point(char=char, height=ord(height_char))]
    return map




def solve(case):
    map = parse_input(case)
    map.print()
    print(map.find_path_length())

    pass

if __name__ == '__main__':
    #solve("example.txt")
    pass
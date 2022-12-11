from dataclasses import dataclass
from common import iterate_input_lines

@dataclass
class Point:
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"({self.x},{self.y})"

def adjust_tail(head_pos, tail_pos):
    x_dist = head_pos.x - tail_pos.x
    y_dist = head_pos.y - tail_pos.y
    x_move = (1 if x_dist > 0 else -1)
    y_move = (1 if y_dist > 0 else -1)
    if abs(x_dist) >= 2:
        tail_pos.x += x_move
        if abs(y_dist) >= 1:
            tail_pos.y += y_move
    elif abs(y_dist)>=2:
        tail_pos.y += y_move
        if abs(x_dist) >= 1:
            tail_pos.x += x_move


def solve(case):
    moves = [line.split() for line in iterate_input_lines(case)]
    tail_history = set([])
    tail_9th_history = set([])
    head_pos = Point()
    tail_pos = [Point() for _ in range(9)]
    tail_history.add((tail_pos[0].x, tail_pos[0].y))
    tail_9th_history.add((tail_pos[8].x, tail_pos[8].y))
    for move in moves:
        direction, steps = move
        for i in range(int(steps)):
            if direction == 'U':
                head_pos.x -= 1
            elif direction == 'D':
                head_pos.x += 1
            elif direction == 'R':
                head_pos.y += 1
            elif direction == 'L':
                head_pos.y -= 1
            adjust_tail(head_pos, tail_pos[0])
            for i in range(1, 9):
                adjust_tail(tail_pos[i-1], tail_pos[i])
            tail_history.add((tail_pos[0].x, tail_pos[0].y))
            tail_9th_history.add((tail_pos[8].x, tail_pos[8].y))

    return len(tail_9th_history)

if __name__ == '__main__':
    print(solve("input.txt"))
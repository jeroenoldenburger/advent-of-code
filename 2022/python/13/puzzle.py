from collections.abc import Iterator
from common import iterate_input_lines

def iterate_input_per_2_lines(case) -> Iterator[str, str]:
    left = None
    for line in iterate_input_lines(case):
        if line:
            if left is None:
                left = line
            else:
                yield left, line
                left = None


def get_pairs(case):
    pairs = []
    for left,right in iterate_input_per_2_lines(case):
        pairs.append((eval(left), eval(right)))
    return pairs


def in_right_order(left, right, prefix="") -> int:
    """
    -1 if left is smaller
    0 if left == right
    1 of right is smaller
    """
    # print(f"{prefix}- Compare {left} vs {right}")
    if isinstance(left, int) and isinstance(right, int):
        compare = left - right
        if compare < 0:
            # print(f"{prefix}- Left side is smaller, so inputs are in the right order")
            return compare
        elif compare > 0:
            # print(f"{prefix}- Right side is smaller, so inputs are not in the right order")
            return compare
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            compare = in_right_order(left[i], right[i], prefix=prefix + "  ")
            if compare != 0:
                return compare
        compare = len(left) - len(right)
        if compare < 0:
            # print(f"{prefix}- Left side ran out of items, so inputs are in the right order")
            return -1
        elif compare > 0:
            # means left list is longer
            # print(f"{prefix}- Right side ran out of items, so inputs are not in the right order")
            return 1
        return 0
    elif isinstance(left, list) or isinstance(right, list):
        if isinstance(left, int):
            new_left = [left]
            # print(f"{prefix}- Mixed types; convert left to {new_left} and retry comparison")
        else:
            new_left = left
        if isinstance(right, int):
            new_right = [right]
            # print(f"{prefix}- Mixed types; convert right to {new_right} and retry comparison")
        else:
            new_right = right
        return in_right_order(new_left, new_right, prefix=prefix + "  ")
    return 0

def solve(case):
    pairs = get_pairs(case)
    ok_indexes = []
    for i, pair in enumerate(pairs):
        print(f"== Pair {i+1} ==")
        if in_right_order(pair[0], pair[1]) < 0:
            ok_indexes.append(i+1)
    val = sum(ok_indexes)
    print(val)


def get_packets(case):
    packets = []
    for line in iterate_input_lines(case):
        if line:
            packets.append(eval(line))
    return packets


def set_packets_in_order(packets: list):
    while True:
        for i in range(1, len(packets)):
            if in_right_order(packets[i-1], packets[i]) > 0:
                packets[i-1],packets[i]=packets[i],packets[i-1]
                break
        else:
            return packets
        print(".", end="")

def solve2(case):
    input_packets = get_packets(case)
    divider1 = [[2]]
    divider2 = [[6]]
    packets = [divider1, divider2] + input_packets
    set_packets_in_order(packets)
    idx1 = packets.index(divider1) + 1
    idx2 = packets.index(divider2) + 1
    print(idx1 * idx2)

if __name__ == '__main__':
    solve2("input.txt")
from typing import List
from utils import get_challenge_input


def parse_area(area: str) -> List[int]:
    return [int(i) for i in area.split('x')]


def calc_area(length: int, width: int, height: int) -> int:
    return (2 * length * width) + (2 * width * height) + (2 * height * length)


def calc_smallest_side(length: int, width: int, height: int) -> int:
    return min(length * width, width * height, height * length)


def calc_wrapping(area: str) -> int:
    area_list = parse_area(area)    
    l = area_list[0]
    w = area_list[1]
    h = area_list[2]
    smallest = calc_smallest_side(l, w, h)
    return calc_area(l, w, h) + smallest


def calc_smallest_perimeter(length: int, width: int, height: int) -> int:
    sides = [length, width, height]
    side_1 = min(sides)
    sides.remove(side_1)
    side_2 = min(sides)
    
    return (side_1 * 2) + (side_2 * 2)


def calc_cubic(length: int, width: int, height: int) -> int:
    return length * width * height


def calc_ribbon(area: str) -> int:
    area_list = parse_area(area)
    l = area_list[0]
    w = area_list[1]
    h = area_list[2]
    smallest = calc_smallest_perimeter(l, w, h)
    return calc_cubic(l, w, h) + smallest


def part_1():
    assert parse_area('2x3x4') == [2, 3, 4]
    assert parse_area('1x1x10') == [1, 1, 10]
    assert calc_area(2, 3, 4) == 52
    assert calc_area(1, 1, 10) == 42
    assert calc_smallest_side(2, 3, 4) == 6
    assert calc_smallest_side(1, 1, 10) == 1
    assert calc_wrapping('2x3x4') == 58
    assert calc_wrapping('1x1x10') == 43

    challenge_input = get_challenge_input(day=2)
    total = 0
    for area in challenge_input.split('\n'):
        if not area:
            continue
        total = total + calc_wrapping(area)

    print(total)


def part_2():
    assert calc_smallest_perimeter(2, 3, 4) == 10
    assert calc_smallest_perimeter(1, 1, 10) == 4
    assert calc_ribbon('2x3x4') == 34
    assert calc_ribbon('1x1x10') == 14

    challenge_input = get_challenge_input(day=2)
    total = 0
    for area in challenge_input.split('\n'):
        if not area:
            continue
        total = total + calc_ribbon(area)

    print(total)


if __name__ == "__main__":
    # part_1()
    part_2()

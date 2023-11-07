from utils import get_challenge_input


def find_floor(confusing_directions: str) -> int:
    result = 0
    for floor in confusing_directions:
        assert floor in ('(', ')')
        if floor == '(':
            result = result + 1
        else:
            result = result - 1
    return result


def find_first_basement_index(confusing_directions: str) -> int:
    level = 0
    for index, floor in enumerate(confusing_directions):
        assert floor in ('(', ')')
        if floor == '(':
            level = level + 1
        else:
            level = level - 1
        if level < 0:
            return index + 1
    return None


def part_1():
    assert find_floor('(())') == 0
    assert find_floor('()()') == 0
    assert find_floor('(((') == 3
    assert find_floor('(()(()(') == 3
    assert find_floor('))(((((') == 3
    assert find_floor('())') == -1
    assert find_floor('))(') == -1
    assert find_floor(')))') == -3
    assert find_floor(')())())') == -3

    challenge_input = get_challenge_input(day=1)
    print(find_floor(challenge_input))


def part_2():
    assert find_first_basement_index('))') == 1
    assert find_first_basement_index('()())') == 5

    challenge_input = get_challenge_input(day=1)
    print(find_first_basement_index(challenge_input))


if __name__ == "__main__":
    part_1()
    part_2()

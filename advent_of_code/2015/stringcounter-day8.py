from typing import List
from utils import get_challenge_input


def count_total_chars(string: str) -> int:
    return len(string)


def count_in_mem_chars(string: str) -> int:
    results = 0
    index = 1
    while index < len(string) - 1:
        if string[index:index + 4].startswith('\\x'):
            # print(f"A single funky char...{string[index:index + 4]}")
            index = index + 4
        elif string[index:index + 2].startswith('\\"') or string[index:index + 2].startswith('\\\\'):
            # print(f"Should be like a quote or slash or something...{string[index:index + 2]}")
            index = index + 2
        elif ord(string[index]) >= 65 and ord(string[index]) <= 122:
            # print(f"Should be anything else...{string[index]}")
            index = index + 1
        else:
            raise Exception(f"Unknown stuff for string {string} and index {index}")
        
        results = results + 1

    return results


def calculate(string: str) -> int:
    return count_total_chars(string) - count_in_mem_chars(string)


def calc_many(strings: List[str]) -> int:
    total = 0
    for string in strings:
        total = total + calculate(string)
    return total


def encoded_string(string: str) -> int:
    index = 0
    s = '"'
    while index < len(string):
        if string[index:index + 4].startswith('\\x'):
            s = f'{s}\\{string[index:index + 4]}'
            index = index + 4
        elif string[index] == '"':
            s = f'{s}\\"'
            index = index + 1
        elif string[index:index + 2].startswith('\\"'):
            s = f'{s}\\\\\\"'
            index = index + 2
        elif string[index:index + 2].startswith('\\\\'):
            s = f'{s}\\\\\\\\'
            index = index + 2
        elif ord(string[index]) >= 65 and ord(string[index]) <= 122:
            s = f'{s}{string[index]}'
            index = index + 1
        else:
            raise Exception("urrhhhh wut.")
   
    s = f'{s}"'
    print(f'{string} --> {s} w/ {len(s)}')
    return len(s)


def calculate_part_2(string: str) -> int:
    return encoded_string(string) - count_total_chars(string)


def calc_part_2(strings: List[str]) -> int:
    total = 0
    for string in strings:
        total = total + calculate_part_2(string)
    return total


def part_1():
    # assert count_total_chars("") == 2
    # assert count_in_mem_chars("") == 0
    # assert calculate("") == 2

    # assert count_total_chars("abc") == 5
    # assert count_in_mem_chars("abc") == 3
    # assert calculate("abc") == 2

    # assert count_total_chars("aaa\"aaa") == 10
    # assert count_in_mem_chars("aaa\"aaa") == 7
    # assert calculate("aaa\"aaa") == 3

    # assert count_total_chars("\x27") == 6
    # assert count_in_mem_chars("\x27") == 1
    # assert calculate("\x27") == 5

    # assert calc_many([
    #     "", "abc", "aaa\"aaa", "\x26"
    # ]) == 12

    # assert count_in_mem_chars("\x03") == 1
    # assert count_total_chars("\x03") == 6
    # assert count_total_chars("\\") == 4
    # assert count_in_mem_chars("\\") == 1

    challenge_input = get_challenge_input(day=8)
    res = calc_many([i for i in challenge_input.split('\n') if i])
    print(f"PART 1: {res}")

    # Things I tried:
    # ???
    # ???
    # ???
    # 1244

    # To try next:
    # 1371


def part_2():
    challenge_input = get_challenge_input(day=8)
    res = calc_part_2([i for i in challenge_input.split('\n') if i])
    print(f"PART 2: {res}")

    # Tried:
    # 1320 (too low...)
    # 1856 (too low...)

    # 2117

if __name__ == "__main__":
    print('\n\n')
    # part_1()
    part_2()

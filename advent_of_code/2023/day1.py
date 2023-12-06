from utils import get_challenge_input

def calibrate(s: str) -> int:
    front_index = 0
    f = None
    while front_index < len(s):
        if s[front_index].isnumeric():
            f = s[front_index]
            break
        front_index = front_index + 1
    

    back_index = len(s) - 1
    b = None
    while back_index >= 0:
        if s[back_index].isnumeric():
            b = s[back_index]
            break
        back_index = back_index - 1
    
    return int(f'{f}{b}')


def calibrate_with_words(s: str) -> int:
    word_numbers = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    front_index = 0
    f = None
    while front_index < len(s):
        if s[front_index].isnumeric():
            f = s[front_index]
            break
        else:
            for word_num, num in word_numbers.items():
                if s[front_index:].startswith(word_num):
                    f = num
                    break
            if f:
                break
        front_index = front_index + 1

    back_index = len(s) - 1
    b = None
    while back_index >= 0:
        if s[back_index].isnumeric():
            b = s[back_index]
            break
        else:
            for word_num, num in word_numbers.items():
                if s[:back_index + 1].endswith(word_num):
                    b = num
                    break
            if b:
                break
        back_index = back_index - 1
    
    return int(f'{f}{b}')


def part_1():
    assert calibrate('1abc2') == 12
    assert calibrate('pqr3stu8vwx') == 38
    assert calibrate('a1b2c3d4e5f') == 15
    assert calibrate('treb7uchet') == 77

    challenge_input = get_challenge_input(day=1)
    total = 0
    for i in challenge_input.split('\n'):
        if not i:
            continue
        total = total + calibrate(i)
    print(total)


def part_2():
    assert calibrate_with_words('two1nine') == 29
    assert calibrate_with_words('eightwothree') == 83
    assert calibrate_with_words('abcone2threexyz') == 13
    assert calibrate_with_words('xtwone3four') == 24
    assert calibrate_with_words('4nineeightseven2') == 42
    assert calibrate_with_words('zoneight234') == 14
    assert calibrate_with_words('7pqrstsixteen') == 76

    challenge_input = get_challenge_input(day=1)
    total = 0
    for i in challenge_input.split('\n'):
        if not i:
            continue
        total = total + calibrate_with_words(i)
    print(total)


if __name__ == "__main__":
    part_1()
    part_2()
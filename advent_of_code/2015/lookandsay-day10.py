# from typing import Set, Tuple
# from utils import get_challenge_input

def look_and_say(seq: str) -> str:
    result = ''

    index = 0
    while index < len(seq):
        count = 1
        while index + 1 < len(seq) and seq[index] == seq[index + 1]:
            index = index + 1
            count = count + 1
        result = f'{result}{count}{seq[index]}'
        index = index + 1
    return result


def part_1():
    assert look_and_say('1') == '11'
    assert look_and_say('11') == '21'
    assert look_and_say('21') == '1211'
    assert look_and_say('1211') == '111221'
    assert look_and_say('111221') == '312211'

    num = '1'
    for _ in range(5):
        num = look_and_say(num)
    print(num)
    
    challenge_input = '1113222113'
    for _ in range(40):
        challenge_input = look_and_say(challenge_input)
    print(len(challenge_input))


def part_2():
    challenge_input = '1113222113'
    for _ in range(50):
        challenge_input = look_and_say(challenge_input)
    print(len(challenge_input))


if __name__ == "__main__":
    part_1()
    part_2()

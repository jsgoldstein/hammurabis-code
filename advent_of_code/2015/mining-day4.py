from hashlib import md5

CHALLENGE_INPUT = 'yzbqklnj'


def mine(secret_key: str, start_with='00000', starting_guess=0) -> int:
    while not md5(f'{secret_key}{starting_guess}'.encode('utf-8')).hexdigest()[:len(start_with)].startswith(start_with):
        starting_guess = starting_guess + 1
    return starting_guess


def part_1():
    assert mine('abcdef') == 609043
    assert mine('pqrstuv') == 1048970

    # challenge_input = get_challenge_input(day=4)
    print(mine(CHALLENGE_INPUT))


def part_2():
    # challenge_input = get_challenge_input(day=4)
    print(mine(CHALLENGE_INPUT, start_with='000000', starting_guess=282749))


if __name__ == "__main__":
    part_1()
    part_2()

from utils import get_challenge_input


def has_three_vowels(string: str) -> bool:
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 3
    for i in string:
        if i in vowels:
            count = count - 1
        if count == 0:
            return True
    return False


def has_double_bubble(string: str) -> bool:
    index = 0
    while index < len(string) - 1:
        if string[index] == string[index + 1]:
            return True
        index = index + 1
    return False


def naughty_pairs(string: str) -> bool:
    pairs = ('ab', 'cd', 'pq', 'xy')
    index = 0
    while index < len(string) - 1:
        if string[index:index + 2] in pairs:
            return True
        index = index + 1
    return False


def nice_pairs(string: str) -> bool:
    return not naughty_pairs(string)


def is_nice(string: str) -> bool:
    return has_three_vowels(string) and has_double_bubble(string) and nice_pairs(string)


def incorrect_two_letters_twice(string: str) -> bool:
    # DOESN'T CHECK FOR OVERLAPPING!!!!!!!!!!!!!
    index = 0
    doubles = set()
    while index < len(string) - 1:
        if (pair := string[index: index + 2]) in doubles:
            print(pair)
            return True
        doubles.add(pair)
        index = index + 1
    return False


def two_letters_twice(string: str) -> bool:
    index = 0
    while index < len(string) - 1:
        if string[index: index + 2] in string[index + 2:]:
            print(string[index: index + 2])
            return True
        index = index + 1
    return False


def sandwhich(string: str) -> bool:
    index = 0
    while index < len(string) - 2:
        if string[index:index + 3] == string[index:index + 3][::-1]:
            return True
        index = index + 1
    return False


def is_nice_v2(string: str) -> bool:
    return two_letters_twice(string) and sandwhich(string)


def part_1():
    assert has_three_vowels('ugknbfddgicrmopn')
    assert has_double_bubble('ugknbfddgicrmopn')
    assert nice_pairs('ugknbfddgicrmopn')
    assert is_nice('ugknbfddgicrmopn')

    assert has_three_vowels('aaa')
    assert has_double_bubble('aaa')
    assert nice_pairs('aaa')
    assert is_nice('aaa')

    assert has_three_vowels('jchzalrnumimnmhp')
    assert not has_double_bubble('jchzalrnumimnmhp')
    assert nice_pairs('jchzalrnumimnmhp')
    assert not is_nice('jchzalrnumimnmhp')

    assert has_three_vowels('haegwjzuvuyypxyu')
    assert has_double_bubble('haegwjzuvuyypxyu')
    assert naughty_pairs('haegwjzuvuyypxyu')
    assert not is_nice('haegwjzuvuyypxyu')

    assert not has_three_vowels('dvszwmarrgswjxmb')
    assert has_double_bubble('dvszwmarrgswjxmb')
    assert nice_pairs('dvszwmarrgswjxmb')
    assert not is_nice('dvszwmarrgswjxmb')

    challenge_input = get_challenge_input(day=5)
    nice = 0
    for i in challenge_input.split():
        if not i:
            continue
        nice = nice + 1 if is_nice(i) else nice
    print(nice)


def part_2():
    assert two_letters_twice('xyxy')
    assert two_letters_twice('aabcdefgaa')

    assert sandwhich('xyx')
    assert sandwhich('abcdefeghi')
    assert sandwhich('aaa')

    assert two_letters_twice('qjhvhtzxzqqjkmpb')
    assert sandwhich('qjhvhtzxzqqjkmpb')
    assert is_nice_v2('qjhvhtzxzqqjkmpb')

    assert two_letters_twice('xxyxx')
    assert sandwhich('xxyxx')
    assert is_nice_v2('xxyxx')

    assert two_letters_twice('uurcxstgmygtbstg')
    assert not is_nice_v2('uurcxstgmygtbstg')

    assert sandwhich('ieodomkazucvgmuy')
    assert not is_nice_v2('ieodomkazucvgmuy')

    assert is_nice_v2('aaaa')

    assert is_nice_v2('xdwduffwgcptfwad')

    test()

    challenge_input = get_challenge_input(day=5)
    nice = 0
    for i in challenge_input.split():
        if is_nice_v2(i):
            nice = nice + 1
            # print(i)
    print(nice)

    for i in challenge_input.split():
        try:
            assert two_letters_twice(i) == incorrect_two_letters_twice(i)
        except AssertionError:
            print(i)


def test():
    nice_strings = [
        'xdwduffwgcptfwad',
        'zbgtglaqqolttgng',
        'ttgrkjjrxnxherxd',
        'qaqlyoyouotsmamm',
        'tadsdceadifqthag',
        'aohjxahenxaermrq',
        'ydpgwxxoxlywxcgi',
        'nscghlafavnsycjh',
        'aoojqakosnaxosom',
        'urybkdyvsrosrfro',
        'boaaruhalgaamqmh',
        'ephlkipjfnjfjrns',
        'ywfmuogvicpywpwm',
        'pkpkrqjvgocvaxjs',
        'usquiquspcdppqeq',
        'tornfzkzhjyofzqa',
        'ldymyvumyhyamopg',
        'azxynqididtrwokb',
        'uetoytptktkmewre',
        'afaefrwhcosurprw',
        'opmopgyabjjjoygt',
        'klvhlhuqhosvjuqk',
        'juududyojcazzgvr',
        'dxsvscqukljxcqyi',
        'rumwchfihhihpqui',
        'zrhemeqegmzrpufd',
        'pjtuxskkowutltlq',
        'yafopikiqswafsit',
        'sknufchjdvccccta',
        'oljkoldhfggkfnfc',
        'dijdacfteteypkoq',
        'xojwroydfeoqupup',
        'uoghiuosiiwiwdws',
        'twsgsfzyszsfinlc',
        'bsnansnfxduritrr',
        'eitavndozoezojsi',
        'qifbtzszfyzsjzyx',
        'kgjruggcikrfrkrw',
        'kbgufbosjghahacw',
        'cyypypveppxxxfuq',
        'lqbjwjqxqbfgdckc',
        'usfenmavvuevevgr',
        'evdqxevdacsbfbjb',
        'vrseaozoheawffoq',
        'ermaenjunjtbekeo',
        'komgvqejojpnykol',
        'gnnalgfvefdfdwwg',
        'nofhmbxififwroeg',
        'oibkuxhjmhxhhzby',
        'badkdgqrpjzbabet',
        'uuxufbwfegysabww',
        'wbqgqkwbibiilhzc',
        'bqzctiuaxpriuiga',
        'aetgqmiqzxbvbviz',
        'joakcwpfggtitizs',
        'wkkypomlvyglpfpf',
        'jcaqyaqvsefwtaya',
        'cmjpjjgndozcmefj',
        'zynfntqwblbnfqik',
        'obkbmflhyanxilnx',
        'iylmzraibygmgmqj',
        'mvhyerxfiljlotjl',
        'mtsynnfxunuohbnf',
        'imylyalawbqwkrwb',
        'mkzvquzvqvwsejqs',
        'kadkaftffaziqdze',
        'fpsrobmbqbmigmwk',
        'xbhjakklmbhsdmdt',
        'fkgrqbyqpqcworqc',
    ]
    assert(len(nice_strings)) == 69
    for i in nice_strings:
        assert(is_nice_v2(i))


if __name__ == "__main__":
    # part_1()
    part_2()

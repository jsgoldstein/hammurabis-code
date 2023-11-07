from typing import Dict, List

from utils import get_challenge_input

class Wire:
    def __init__(self, name: str, action: str) -> None:
        self.name: str = name

        self.value: str = ''
        self.operator: str = ''
        self.parents: List[str] = []
        self.shift: int = 0

        self.action: str = action
        self.resolved: bool = False

        self.parse_action(self.action)

        assert self.operator in ('STAM', 'NOT', 'LSHIFT', 'RSHIFT', 'OR', 'AND')
        if not self.resolved:
            assert len(self.parents) >= 1
    
    def __str__(self) -> str:
        return f'{self.name}: {self.action}. Parents: {self.parents}. Value: {self.value} ({self.to_int()})'
    
    def __repr__(self) -> str:
        return f'{self.name}: {self.action}. Parents: {self.parents}. Value: {self.value} ({self.to_int()})'
    
    def to_int(self) -> int:
        return int(self.value, 2) if self.value else -1
    
    def update(self, value: str):
        assert self.operator == 'STAM'
        assert value.isnumeric()
        self.value = format(int(value), '016b')
        assert len(self.value) == 16
    
    def parse_action(self, action: str) -> None:
        steps = action.split()

        if len(steps) == 1:
            self.operator = 'STAM'

            if (number := steps[0]).isnumeric():
                self.value = format(int(number), '016b')
                self.resolved = True
                assert len(self.value) == 16
            else:
                self.parents.append(number)
        elif steps[0] == 'NOT':
            self.operator = 'NOT'

            assert len(steps) == 2
            assert steps[1].isalpha()

            self.parents.append(steps[1])
        elif (operator := steps[1]) in ('LSHIFT', 'RSHIFT'):
            self.operator = operator

            assert len(steps) == 3
            assert steps[0].isalpha()
            assert steps[2].isnumeric()

            self.parents.append(steps[0])
            self.shift = int(steps[2])
        elif (operator := steps[1]) in ('AND', 'OR'):
            self.operator = operator

            assert len(steps) == 3
            first = steps[0]
            second = steps[2]
            if first.isnumeric():
                first = format(int(first), '016b')
            if second.isnumeric():
                second = format(int(second), '016b')
            self.parents.extend([first, second])
        else:
            raise Exception(f"Unknown action: {action}")
    
    def process(self, values: List[str]) -> str:
        if self.operator == 'STAM':
            assert len(values) == 1
            self.value = values[0]
        elif self.operator == 'NOT':
            assert len(values) == 1
            self.value = ''.join(['0' if i == '1' else '1' for i in values[0]])
        elif self.operator == 'LSHIFT':
            assert len(values) == 1
            assert self.shift
            self.value = f'{values[0]}{"0" * self.shift}'[self.shift:]
        elif self.operator == 'RSHIFT':
            assert len(values) == 1
            assert self.shift
            self.value = f'{"0" * self.shift}{values[0]}'[:-self.shift]
        elif self.operator == 'OR':
            assert len(values) == 2
            index = 0
            while index < 16:
                self.value = f'{self.value}{"1" if values[0][index] == "1" or values[1][index] == "1" else "0"}'
                index = index + 1
        elif self.operator == 'AND':
            assert len(values) == 2
            index = 0
            while index < 16:
                self.value = f'{self.value}{"1" if values[0][index] == "1" and values[1][index] == "1" else "0"}'
                index = index + 1

        self.resolved = True
        assert isinstance(self.value, str)
        assert len(self.value) == 16
        return self.value


def parse_instruction(instruction: str) -> Wire:
    instructions = instruction.split('->')
    assert len(instructions) == 2

    return Wire(name=instructions[1].strip(), action=instructions[0].strip())


def process(wire: Wire, all_wires: Dict[str, Wire]) -> None:
    if wire.resolved:
        return

    for parent in wire.parents:
        if parent.isnumeric():
            continue
        process(all_wires[parent], all_wires)

    wire.process([all_wires[i].value if i in all_wires else i for i in wire.parents])


def connect_wires(instructions: List[str]) -> Dict[str, Wire]:
    wires = {}

    for instruction in instructions:
        if not instruction:
            continue

        wire = parse_instruction(instruction)
        wires[wire.name] = wire
    
    return wires


def process_wires(wires: Dict[str, Wire]) -> None:
    for _, wire in wires.items():
        process(wire, wires)


def part_1():
    instructions = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i'
    ]
    connections = connect_wires(instructions)
    process_wires(connections)

    assert connections['d'].to_int() == 72
    assert connections['e'].to_int() == 507
    assert connections['f'].to_int() == 492
    assert connections['g'].to_int() == 114
    assert connections['h'].to_int() == 65412
    assert connections['i'].to_int() == 65079
    assert connections['x'].to_int() == 123
    assert connections['y'].to_int() == 456

    challenge_input = get_challenge_input(day=7)
    prod_connections = connect_wires(challenge_input.split('\n'))
    process_wires(prod_connections)
    print(f"Part 1: {prod_connections['a'].to_int()}")


def part_2():
    new_b = '46065'

    challenge_input = get_challenge_input(day=7)
    prod_connections = connect_wires(challenge_input.split('\n'))
    print(prod_connections['b'])
    prod_connections['b'].update(new_b)
    print(prod_connections['b'])
    process_wires(prod_connections)
    print(f"Part 2: {prod_connections['a'].to_int()}")


if __name__ == "__main__":
    part_1()
    part_2()

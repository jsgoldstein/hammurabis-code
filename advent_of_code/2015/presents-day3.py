from typing import Set, Tuple
from utils import get_challenge_input

class Locataion:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited: dict[Tuple[int, int], bool] = {}
        self.__mark_visit()
    
    def move(self, direction: str) -> None:
        assert direction in ('^', '>', 'v', '<')
        if direction == '^':
            self.y = self.y + 1
        elif direction == '>':
            self.x = self.x + 1
        elif direction == 'v':
            self.y = self.y - 1
        else:  # direction == '<':
            self.x = self.x - 1

        self.__mark_visit()
    
    def __mark_visit(self) -> None:
        pos = (self.x, self.y)
        self.visited[pos] = True
    
    def get_visited(self) -> int:
        return len(self.visited)

    def get_coords(self) -> Tuple[int, int]:
        return (self.x, self.y)


def walk_grid(steps: str):
    locs = Locataion()
    for step in steps:
        locs.move(step)

    return locs.get_visited()


def walk_grid_with_robo(steps: str):
    santa = Locataion()
    robot = Locataion()
    ledger: Set[Tuple[int, int]] = {(0, 0)}

    for turn, step in enumerate(steps):
        if turn % 2 == 0:
            santa.move(step)
            ledger.add(santa.get_coords())
        else:
            robot.move(step)
            ledger.add(robot.get_coords())

    return len(ledger)

def part_1():
    assert walk_grid('>') == 2
    assert walk_grid('^>v<') == 4
    assert walk_grid('^v^v^v^v^v') == 2

    challenge_input = get_challenge_input(day=3)
    print(walk_grid(challenge_input))


def part_2():
    assert walk_grid_with_robo('^v') == 3
    assert walk_grid_with_robo('^>v<') == 3
    assert walk_grid_with_robo('^v^v^v^v^v') == 11

    challenge_input = get_challenge_input(day=3)
    print(walk_grid_with_robo(challenge_input))


if __name__ == "__main__":
    # part_1()
    part_2()

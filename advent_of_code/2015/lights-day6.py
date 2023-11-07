from typing import Union

from utils import get_challenge_input


class Grid:
    def __init__(self) -> None:
        self.grid = [ [False] * 1000 for _ in range(1000)]
    
    def __str__(self) -> str:
        result = ''
        for i in self.grid:
            result = f'{result}\n{i}'
        return result
    
    def take_action(self, top_left: str, bottom_right: str, action: str) -> None:
        assert action in ('toggle', 'on', 'off')

        top = top_left.split(',')
        bottom = bottom_right.split(',')

        for i in range(int(top[0]), int(bottom[0]) + 1):
            for j in range(int(top[1]), int(bottom[1]) + 1):
                if action == 'on':
                    self.grid[i][j] = True
                elif action == 'off':
                    self.grid[i][j] = False
                elif action == 'toggle':
                    self.grid[i][j] = not self.grid[i][j]
    
    def count(self) -> int:
        result = 0
        for i in self.grid:
            for j in i:
                if j:
                    result = result + 1
        return result


class GridV2:
    def __init__(self) -> None:
        self.grid = [ [0] * 1000 for _ in range(1000)]
    
    def __str__(self) -> str:
        result = ''
        for i in self.grid:
            result = f'{result}\n{i}'
        return result
    
    def take_action(self, top_left: str, bottom_right: str, action: str) -> None:
        assert action in ('toggle', 'on', 'off')

        top = top_left.split(',')
        bottom = bottom_right.split(',')

        for i in range(int(top[0]), int(bottom[0]) + 1):
            for j in range(int(top[1]), int(bottom[1]) + 1):
                if action == 'on':
                    self.grid[i][j] = self.grid[i][j] + 1
                elif action == 'off':
                    self.grid[i][j] = self.grid[i][j] - 1
                    # Don't let a light's brightness drop below 0
                    if self.grid[i][j] < 0:
                        self.grid[i][j] = 0
                elif action == 'toggle':
                    self.grid[i][j] = self.grid[i][j] + 2
    
    def count(self) -> int:
        result = 0
        for i in self.grid:
            for j in i:
                if j:
                    result = result + j
        return result


def act(grid: Union[Grid, GridV2], action: str):
    command = action.split()

    top_left = command[-3]
    bottom_right = command[-1]

    if action.startswith('toggle'):
        grid.take_action(top_left, bottom_right, 'toggle')
    elif action.startswith('turn off'):
        grid.take_action(top_left, bottom_right, 'off')
    elif action.startswith('turn on'):
        grid.take_action(top_left, bottom_right, 'on')
    else:
        raise Exception("Unknown Command")


def part_1():
    grid = Grid()
    grid2 = Grid()
    assert len(grid.grid) == 1000
    for i in grid.grid:
        assert len(i) == 1000
        assert not any(i)

    grid.take_action('0,0', '999,999', 'on')
    for i in grid.grid:
        assert all(i)
    act(grid2, 'turn on 0,0 through 999,999')
    assert grid.count() == grid2.count()

    # grid.take_action('0,0', '999,0', 'toggle')
    # print(grid)
    # assert not any(grid.grid[0])
    # for i in grid.grid[1:]:
    #     assert all(i)

    prod_grid = Grid()
    challenge_input = get_challenge_input(day=6)
    for i in challenge_input.split('\n'):
        if not i:
            continue
        act(prod_grid, i)

    print(prod_grid.count())


def part_2():
    grid = GridV2()
    act(grid, 'turn on 0,0 through 0,0')
    assert grid.count() == 1

    act(grid, 'toggle 0,0 through 999,999')
    assert grid.count() == 2000000 + 1  # plus 1 'cause I re-used the grid here...


    prod_grid = GridV2()
    challenge_input = get_challenge_input(day=6)
    for i in challenge_input.split('\n'):
        if not i:
            continue
        act(prod_grid, i)

    print(prod_grid.count())


if __name__ == "__main__":
    # part_1()
    part_2()

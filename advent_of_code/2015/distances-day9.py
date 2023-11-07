import copy
from typing import Dict, Set, Optional
from utils import get_challenge_input

class Location:
    def __init__(self, name: str):
        self.name = name
        self.locations: Dict[str, int] = {}
    
    def __str__(self) -> str:
        return f'{self.name} -> {self.locations}'

    def __repr__(self) -> str:
        return f'{self.name} -> {self.locations}'
    
    def add_location(self, location: str, dist: int):
        assert location not in self.locations
        self.locations[location] = dist
    
    def get_locations(self, vistited: Optional[Dict[str, int]] = None) -> Dict[str, int]:
        vistited = vistited if vistited else dict()
        return {k: v for k, v in self.locations.items() if k not in vistited}


def update_map_from_dist(distances: str, locs: Dict[str, Location]) -> None:
    places, dist = distances.split('=')
    left, right = places.split('to')

    dist = int(dist.strip())
    left = left.strip()
    right = right.strip()

    if left not in locs:
        locs[left] = Location(left)
    if right not in locs:
        locs[right] = Location(right)

    locs[left].add_location(right, dist)
    locs[right].add_location(left, dist)


def crawl(locations: Dict[str, Location]) -> None:
    visited = dict()
    for name, location in locations.items():
        print(f'Working on {name}')
        for n, l in location.get_locations(vistited=visited).items():
            print(f'name: {n}. dist: {l}')

            print(hash(sorted((name, n))))
        # print(hash(sorted(name, )))


def part_1():
    instructions = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141'
    ]
    locs = {}
    for i in instructions:
        update_map_from_dist(i, locs)
    assert len(locs) == 3
    for _, loc in locs.items():
        assert len(loc.locations) == 2
    
    crawl(locs)


def part_2():
    pass


if __name__ == "__main__":
    part_1()
    part_2()

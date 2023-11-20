from itertools import permutations
from typing import Dict, List, Optional, Tuple
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


def get_all_pairs_v2(distances: List[str]) -> Dict[Tuple[str, ...], int]:
    pairs = {}
    for distance_pair in distances:
        places, dist = distance_pair.split('=')
        left, right = places.split('to')

        dist = int(dist.strip())
        left = left.strip()
        right = right.strip()

        key = tuple(sorted([left, right]))
        if key in pairs:
            continue
        else:
            pairs[key] = dist
    return pairs



def get_all_pairs(locations: Dict[str, Location]) -> Dict[Tuple[str, ...], int]:
    pairs = {}

    for name, location in locations.items():
        # print(f'Working on {name}')
        for n, l in location.get_locations().items():
            # print(f'name: {n}. dist: {l}')
            key = tuple(sorted([name, n]))
            if key in pairs:
                continue
            else:
                pairs[key] = l
    return pairs


def get_all_routes_v2(pairs: Dict[Tuple[str, ...], int]) -> List[str]:
    locations = None
    # This outer loop always breaks after the first iteration. I.e. O(1) time...
    for random_element, _ in pairs.keys():
        locations = [
            l if random_element == r else r 
            for l, r in pairs.keys() 
            if random_element == l or random_element == r
        ]
        locations.append(random_element)
        break

    assert locations
    print(locations)

    routes = []
    for route in permutations(locations, len(locations)):
        if route[::-1] not in routes:
            routes.append(route)

    return routes


def get_all_routes(locations: Dict[str, Location]) -> List[str]:
    result = []
    for route in permutations(locations.keys(), len(locations.keys())):
        if route[::-1] not in result:
            result.append(route)

    return result


def get_distances(routes: List[str], pairs: Dict[Tuple[str, ...], int]) -> List[int]:
    distances = []
    for route in routes:
        i = 0
        d = 0
        while i < len(route) - 1:
            key = tuple(sorted([route[i], route[i + 1]]))
            d = d + pairs[key]
            i = i + 1
        distances.append(d)
    return distances


def get_distances_v2(routes: List[str], pairs: Dict[Tuple[str, ...], int]) -> List[int]:
    seen = {}
    for route in routes:
        calc_route(route, seen)


def calc_route(route: str, seen: Dict[str, int]):
    print(route)
    exit()


def part_1():
    instructions = [
        'London to Dublin = 464',
        'London to Belfast = 518',
        'Dublin to Belfast = 141'
    ]
    pairs = get_all_pairs_v2(instructions)
    routes = get_all_routes_v2(pairs)
    print(routes)
    distances = get_distances(routes, pairs)
    print(distances)


    # locations = {}
    # for i in instructions:
    #     update_map_from_dist(i, locations)
    # assert len(locations) == 3
    # for _, loc in locations.items():
    #     assert len(loc.locations) == 2
    
    # pairs = get_all_pairs(locations)
    # routes = get_all_routes(locations)

    # distances = get_distances(routes, pairs)
    assert 982 in distances
    assert 605 in distances
    assert 659 in distances

    assert min(distances) == 605


    challenge_input = get_challenge_input(day=9)
    # prod_instructions = [i for i in challenge_input.split('\n') if i]
    # prod_locations = {}
    # for i in prod_instructions:
    #     update_map_from_dist(i, prod_locations)
    
    # prod_pairs = get_all_pairs(prod_locations)
    # prod_routes = get_all_routes(prod_locations)
    prod_pairs = get_all_pairs_v2([i for i in challenge_input.split('\n') if i])
    prod_routes = get_all_routes_v2(prod_pairs)
    print(prod_routes)
    prod_distances = get_distances_v2(prod_routes, prod_pairs)
    print(min(prod_distances))
    return prod_distances


def part_2(prod_distances: List[int]):
    print(max(prod_distances))


if __name__ == "__main__":
    distances = part_1()
    part_2(distances)

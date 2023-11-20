import math
from typing import List, Optional

from hypothesis import given
from hypothesis.strategies import lists
from hypothesis.strategies import integers


def search(items: List[int], value: int) -> Optional[int]:
    index = 0
    while index < len(items):
        if items[index] == value:
            return index
        index = index + 1
    return None


def binary_search(items: List[int], value: int, l: int, r: int) -> Optional[int]:
    while l <= r:
        mid = math.floor((l + r) / 2)
        if mid >= len(items):
            return None

        if value < items[mid]:
            r = mid - 1
        elif value > items[mid]:
            l = mid + 1
        elif value == items[mid]:
            return mid


def binary_search_rec(items: List[int], value: int, l: int, r: int) -> Optional[int]:
    if l > r:
        return None

    mid = math.floor((l + r) / 2)
    if mid >= len(items):
        return None

    if value < items[mid]:
        return binary_search_rec(items, value, l, mid - 1)
    elif value > items[mid]:
        return binary_search_rec(items, value, mid + 1, r)
    elif value == items[mid]:
        return mid


def search_sum(items: List[int], value: int) -> bool:
    for i in items:
        v = value - i
        copy_of_items = sorted(items.copy())
        copy_of_items.remove(i)
        if binary_search(copy_of_items, v, 0, len(copy_of_items)) is not None:
            return True
    return False


class TestSearches:
    @given(lists(integers(), min_size=1, unique=True), integers())
    def test_search(self, a: List[int], v: int) -> None:
        result = search(a, v)
        if v in a:
            assert a.index(v) == result
        else:
            assert result is None
    
    @given(lists(integers(), min_size=1, unique=True), integers())
    def test_binary_search(self, a: List[int], v: int) -> None:
        a = sorted(a)
        assert search(a, v) == binary_search(a, v, 0, len(a))

    @given(lists(integers(), min_size=1, unique=True), integers())
    def test_binary_search_rec(self, a: List[int], v: int) -> None:
        a = sorted(a)
        assert search(a, v) == binary_search_rec(a, v, 0, len(a))

    @given(lists(integers(min_value=1), min_size=2, unique=True), integers(min_value=1))
    def test_search_sum(self, a: List[int], v: int) -> None:
        result = search_sum(a, v)

        in_list = False
        for i in a:
            copy_of_a = a.copy()
            copy_of_a.remove(i)
            if (v - i) in copy_of_a:
                in_list = True
                break

        assert result == in_list
